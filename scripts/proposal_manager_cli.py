#!/usr/bin/env python3
"""
Proposal System Data Management CLI
All project and proposal CRUD operations must go through this script.
CSV is the source of truth; markdown files are derived from CSV.

CSV Schema:
- projects.csv: id, name, proposal_count, git_repo, local_path, description, last_update
- proposals.csv: id, title, owner, status, project_id, project_name, stage,
                 prd_path, tech_solution_path, project_path, git_repo, deployment_url,
                 deployment_branch, prd_confirmation, tech_expectations, acceptance,
                 research_direction, last_update, engine, target, game_type, notes
"""

import csv
import sys
import os
import re
import shutil
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Configuration paths
PROPOSALS_ROOT = Path("/home/hermes/proposals")
PROJECTS_CSV = PROPOSALS_ROOT / "projects.csv"
PROPOSALS_CSV = PROPOSALS_ROOT / "proposals.csv"

# Workspace directories
DEV_OUTPUT_DIR = PROPOSALS_ROOT / "workspace-dev"
PM_OUTPUT_DIR = PROPOSALS_ROOT / "workspace-pm"
TEST_OUTPUT_DIR = PROPOSALS_ROOT / "workspace-test"
RESEARCH_OUTPUT_DIR = PROPOSALS_ROOT / "workspace-research"

# Valid enum values
# Status state machine: which fields to auto-fill on each transition
STATUS_TRANSITIONS = {
    "intake": "clarifying",
    "clarifying": "prd_pending_confirmation",
    "prd_pending_confirmation": "approved_for_dev",
    "approved_for_dev": "in_tdd_test",
    "in_tdd_test": "in_dev",
    "in_dev": "in_test_acceptance",
    "in_test_acceptance": "accepted",
    "test_failed": "in_dev",
    "needs_revision": "in_dev",
    "accepted": "deployed",
    "deployed": "delivered",
    "deploying": "deployed",
    "research_direction_pending": "intake",
    "active": "active",
    "archived": "archived",
    "delivered": "delivered",
}

# Fields to auto-set when transitioning to a new status
AUTO_FILL_ON_TRANSITION = {
    "accepted": {"acceptance": "accepted"},
    "deployed": {},
    "in_test_acceptance": {},
    "test_failed": {},
}

VALID_PROPOSAL_STATUSES = {
    "intake", "clarifying", "prd_pending_confirmation", "approved_for_dev",
    "in_tdd_test", "in_dev", "in_test_acceptance", "test_failed",
    "accepted", "needs_revision", "deployed", "deploying",
    "research_direction_pending", "active", "archived", "delivered"
}
VALID_PROPOSAL_STAGES = {"ideation", "development", "research", "proposal", "in_dev", "in_acceptance", "accepted", "delivered", "active", "approved_for_dev", "prd_pending_confirmation"}
VALID_PRDS = {"pending", "confirmed", "timeout-approved", "rejected", ""}
VALID_TECH_EXPS = {"pending", "confirmed", "timeout-approved", ""}
VALID_ACCEPTANCES = {"pending", "accepted", "rejected", ""}
VALID_GAME_TYPES = {"", "休闲", "策略", "卡牌", "RPG", "消除", "塔防", "模拟", "动作", "射击"}

# CSV Headers
PROJECTS_CSV_HEADERS = ['id', 'name', 'proposal_count', 'git_repo', 'local_path', 'description', 'last_update']
PROPOSALS_CSV_HEADERS = ['id', 'title', 'owner', 'status', 'project_id', 'project_name', 'stage',
                          'prd_path', 'tech_solution_path', 'project_path', 'git_repo', 'deployment_url',
                          'prd_confirmation', 'tech_expectations', 'acceptance',
                          'last_update', 'engine', 'target', 'game_type', 'notes']

# ID patterns
PROJECT_ID_PATTERN = re.compile(r'^PRJ-\d{8}-\d{3}$')
PROPOSAL_ID_PATTERN = re.compile(r'^P-\d{8}-\d{3}$')


# Audit log path
AUDIT_LOG = PROPOSALS_ROOT / "audit.log"

def audit_log(action, target, details=""):
    """Write persistent audit log entry for CSV modifications."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] {action} | {target} | {details}\n"
    with open(AUDIT_LOG, 'a', encoding='utf-8') as f:
        f.write(entry)

def log(msg):
    print(f"[proposal-manager] {msg}", file=sys.stderr)


def die(msg):
    log(f"ERROR: {msg}")
    audit_log("ERROR", "die", msg)
    sys.exit(1)


def read_csv(path):
    """Read CSV, return (headers, rows)"""
    if not path.exists():
        return [], []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return reader.fieldnames or [], rows


def write_csv(path, headers, rows):
    """Atomic CSV write: write to .tmp first, then rename.
    Prevents partial writes from corrupting the CSV file.
    Records audit log entry for every write.

    Safety guards:
    - Refuses to write 0 rows to a file that has >10 existing rows (data loss prevention)
    - Raises on unknown CSV fields (no silent field dropping)
    - Verifies row count after rename (post-write verification)
    """
    tmp_path = Path(str(path) + '.tmp')
    bak_path = Path(str(path) + '.bak')

    # Guard: refuse to truncate a populated CSV to 0 rows
    if not rows:
        if path.exists():
            existing_rows = sum(1 for _ in open(path)) - 1  # -1 for header
            if existing_rows > 10:
                raise ValueError(
                    f"Refusing to write 0 rows to {path.name}: "
                    f"file currently has {existing_rows} rows. "
                    f"Backup data before overwriting."
                )

    # Write to temp file — extrasaction='raise' catches field mismatches
    with open(tmp_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers, extrasaction='raise')
        writer.writeheader()
        writer.writerows(rows)

    # Backup existing file BEFORE rename (crash-safe order: backup first)
    if path.exists():
        shutil.copy2(path, bak_path)

    # Atomic rename (Linux guarantees this is atomic on same filesystem)
    tmp_path.rename(path)

    # Post-write verification: confirm file has expected row count
    with open(path, newline='', encoding='utf-8') as f:
        actual_rows = sum(1 for _ in f) - 1  # -1 for header
    if actual_rows != len(rows):
        raise RuntimeError(
            f"Post-write mismatch for {path.name}: "
            f"wrote {len(rows)} rows but file has {actual_rows} rows. "
            f"Restore from {bak_path} if needed."
        )

    # Audit trail (row_count is actual data rows, header not counted)
    audit_log("CSV_WRITE", path.name, f"{len(rows)} rows, {len(headers)} fields")


def load_projects():
    headers, rows = read_csv(PROJECTS_CSV)
    return headers, rows


def load_proposals():
    headers, rows = read_csv(PROPOSALS_CSV)
    return headers, rows


# ==================== Validation ====================

def validate_project_id(project_id):
    if not PROJECT_ID_PATTERN.match(project_id):
        raise ValueError(f"Invalid project ID format: {project_id}, expected: PRJ-YYYYMMDD-XXX")


def validate_proposal_id(proposal_id):
    if not PROPOSAL_ID_PATTERN.match(proposal_id):
        raise ValueError(f"Invalid proposal ID format: {proposal_id}, expected: P-YYYYMMDD-XXX")


def validate_non_empty(value, field_name):
    if not value or not str(value).strip():
        raise ValueError(f"{field_name} cannot be empty")


def validate_enum(value, field_name, valid_values):
    if value and value not in valid_values:
        raise ValueError(f"Invalid {field_name}: {value}, valid values: {valid_values}")


def validate_url_or_empty(value, field_name):
    if value and not value.strip():
        return
    if value and not (value.startswith('http://') or value.startswith('https://') or value.startswith('git@')):
        raise ValueError(f"{field_name} must start with http://, https://, or git@")


def get_project_by_id(project_id, projects):
    for p in projects:
        if p['id'] == project_id:
            return p
    return None


def get_proposal_by_id(proposal_id, proposals):
    for p in proposals:
        if p['id'] == proposal_id:
            return p
    return None


def validate_project_exists(project_id, projects):
    if not get_project_by_id(project_id, projects):
        raise ValueError(f"Project does not exist: {project_id}")


def validate_proposal_exists(proposal_id, proposals):
    if not get_proposal_by_id(proposal_id, proposals):
        raise ValueError(f"Proposal does not exist: {proposal_id}")


# ==================== Workspace Initialization ====================

def init_project_workspace(project_id, project_name, workspace_type='dev'):
    """Initialize project workspace directory structure"""
    workspace_map = {
        'dev': DEV_OUTPUT_DIR,
        'pm': PM_OUTPUT_DIR,
        'test': TEST_OUTPUT_DIR,
        'research': RESEARCH_OUTPUT_DIR,
    }
    
    if workspace_type not in workspace_map:
        raise ValueError(f"Invalid workspace type: {workspace_type}, must be one of: {list(workspace_map.keys())}")
    
    workspace_root = workspace_map[workspace_type]
    project_dir = workspace_root / project_name / "proposals"
    docs_dir = project_dir / "docs"
    
    # Create directory structure
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    # Create initial docs/index.md
    index_file = docs_dir / "index.md"
    if not index_file.exists():
        index_content = f"""# {project_name} - Documents Index

## Project: {project_name}
**Project ID**: {project_id}
**Created**: {datetime.now().strftime('%Y-%m-%d')}
**Workspace**: {workspace_type}

## Document Versions

### Proposal
| Version | File | Updated | Notes |
|---------|------|---------|-------|

### PRD
| Version | File | Updated | Notes |
|---------|------|---------|-------|

### Technical Solution
| Version | File | Updated | Notes |
|---------|------|---------|-------|

### Test Cases
| Version | File | Updated | Notes |
|---------|------|---------|-------|

"""
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
    
    return str(project_dir)


# ==================== Project Operations ====================

def generate_project_id(projects):
    """Generate next project ID: PRJ-YYYYMMDD-XXX"""
    today = datetime.now().strftime('%Y%m%d')
    prefix = f"PRJ-{today}-"
    max_num = 0
    for p in projects:
        if p.get('id', '').startswith(prefix):
            try:
                num = int(p['id'].split('-')[-1])
                max_num = max(max_num, num)
            except:
                pass
    return f"{prefix}{max_num + 1:03d}"


def cmd_add_project(args):
    """Add new project"""
    headers, projects = load_projects()
    
    # Generate ID if not specified
    project_id = args.id
    if not project_id:
        project_id = generate_project_id(projects)
        log(f"Auto-generated project ID: {project_id}")
    
    # Validate
    validate_project_id(project_id)
    validate_non_empty(args.name, 'name')
    
    # Check for duplicate ID
    if get_project_by_id(project_id, projects):
        die(f"Project ID already exists: {project_id}")
    
    data = {
        'id': project_id,
        'name': args.name,
        'proposal_count': '0',
        'git_repo': args.git_repo or '',
        'local_path': args.local_path or '',
        'description': args.description or '',
        'last_update': datetime.now().strftime('%Y-%m-%d'),
    }
    
    # Write
    if not headers:
        headers = PROJECTS_CSV_HEADERS
    projects.append(data)
    write_csv(PROJECTS_CSV, headers, projects)
    
    # Initialize workspace if requested
    if args.init_workspace:
        for ws_type in ['dev', 'pm', 'test', 'research']:
            init_project_workspace(project_id, args.name, ws_type)
        log(f"Initialized workspaces for: {args.name}")
    
    log(f"Added project: {project_id} - {args.name}")
    print(project_id)


def cmd_list_projects(args):
    """List projects"""
    headers, projects = load_projects()
    
    if not projects:
        log("No projects found")
        return
    
    fields = args.fields.split(',') if args.fields else headers
    fields = [f for f in fields if f in headers]
    
    print('\t'.join(fields))
    for p in projects:
        row = [p.get(f, '') for f in fields]
        print('\t'.join(row))


def cmd_get_project(args):
    """Get single project"""
    _, projects = load_projects()
    
    p = get_project_by_id(args.id, projects)
    if not p:
        die(f"Project not found: {args.id}")
    
    if args.json:
        import json
        print(json.dumps(p, ensure_ascii=False, indent=2))
    else:
        for k, v in p.items():
            print(f"{k}: {v}")


def cmd_update_project(args):
    """Update project"""
    headers, projects = load_projects()
    
    p = get_project_by_id(args.id, projects)
    if not p:
        die(f"Project not found: {args.id}")
    
    # All updatable fields
    update_fields = {
        'name': args.name,
        'git_repo': args.git_repo,
        'local_path': args.local_path,
        'description': args.description,
    }
    
    for field, value in update_fields.items():
        if value is not None:
            if field in ('git_repo',):
                if value:
                    validate_url_or_empty(value, field)
            elif field == 'name' and not value:
                raise ValueError("name cannot be empty")
            p[field] = value
    
    p['last_update'] = datetime.now().strftime('%Y-%m-%d')
    
    write_csv(PROJECTS_CSV, headers, projects)
    log(f"Updated project: {args.id}")


def cmd_delete_project(args):
    """Delete project (removes from CSV)"""
    headers, projects = load_projects()
    
    p = get_project_by_id(args.id, projects)
    if not p:
        die(f"Project not found: {args.id}")
    
    if not args.force:
        _, proposals = load_proposals()
        active_count = sum(1 for pr in proposals 
                          if pr.get('project_id') == args.id 
                          and pr.get('status') not in ('archived', 'deployed'))
        if active_count > 0:
            die(f"Project has {active_count} active proposals. Delete proposals first or use --force")
    
    projects = [x for x in projects if x['id'] != args.id]
    write_csv(PROJECTS_CSV, headers, projects)
    
    log(f"Deleted project: {args.id}")


def cmd_init_workspace(args):
    """Initialize project workspace"""
    _, projects = load_projects()
    
    p = get_project_by_id(args.project_id, projects)
    if not p:
        die(f"Project not found: {args.project_id}")
    
    for ws_type in args.workspace.split(','):
        ws_type = ws_type.strip()
        path = init_project_workspace(args.project_id, p['name'], ws_type)
        log(f"Initialized {ws_type} workspace: {path}")
    
    print(f"Initialized workspace(s): {args.workspace}")


# ==================== Proposal Operations ====================

def generate_proposal_id(proposals):
    """Generate next proposal ID: P-YYYYMMDD-XXX"""
    today = datetime.now().strftime('%Y%m%d')
    prefix = f"P-{today}-"
    max_num = 0
    for p in proposals:
        if p.get('id', '').startswith(prefix):
            try:
                num = int(p['id'].split('-')[-1])
                max_num = max(max_num, num)
            except:
                pass
    return f"{prefix}{max_num + 1:03d}"


def update_project_proposal_count(project_id):
    """Update project's proposal count"""
    headers, projects = load_projects()
    for p in projects:
        if p['id'] == project_id:
            _, proposals = load_proposals()
            count = sum(1 for pr in proposals 
                       if pr.get('project_id') == project_id 
                       and pr.get('status') != 'archived')
            p['proposal_count'] = str(count)
            p['last_update'] = datetime.now().strftime('%Y-%m-%d')
            break
    write_csv(PROJECTS_CSV, headers, projects)


def cmd_add_proposal(args):
    """Add new proposal"""
    headers, proposals = load_proposals()
    _, projects = load_projects()
    
    # Generate ID if not specified
    proposal_id = args.id
    if not proposal_id:
        proposal_id = generate_proposal_id(proposals)
        log(f"Auto-generated proposal ID: {proposal_id}")
    
    # Validate
    validate_proposal_id(proposal_id)
    validate_non_empty(args.title, 'title')
    validate_project_exists(args.project_id, projects)
    project = get_project_by_id(args.project_id, projects)
    
    if get_proposal_by_id(proposal_id, proposals):
        die(f"Proposal ID already exists: {proposal_id}")
    
    # Determine local project path
    local_project_path = args.project_path or project.get('local_path', '')
    if not local_project_path:
        local_project_path = str(DEV_OUTPUT_DIR / project['name'] / "proposals")
    
    data = {
        'id': proposal_id,
        'title': args.title,
        'owner': args.owner or '',
        'status': args.status or 'intake',
        'project_id': args.project_id,
        'project_name': project['name'],
        'stage': args.stage or 'proposal',
        'prd_path': args.prd_path or '',
        'tech_solution_path': args.tech_solution_path or '',
        'project_path': local_project_path,
        'git_repo': args.git_repo or project.get('git_repo', ''),
        'deployment_url': args.deployment_url or '',
        'deployment_branch': args.deployment_branch or '',
        'prd_confirmation': args.prd_confirmation or '',
        'tech_expectations': args.tech_expectations or '',
        'acceptance': args.acceptance or '',
        'research_direction': args.research_direction or '',
        'last_update': datetime.now().strftime('%Y-%m-%d'),
        'engine': args.engine or '',
        'target': args.target or '',
        'game_type': args.game_type or '',
        'notes': args.notes or '',
    }
    
    # Write
    if not headers:
        headers = PROPOSALS_CSV_HEADERS
    proposals.append(data)
    write_csv(PROPOSALS_CSV, headers, proposals)
    
    # Update project proposal count
    update_project_proposal_count(args.project_id)

    # Auto-sync proposal-index.md from CSV
    cmd_sync_to_index(args)

    log(f"Added proposal: {proposal_id} - {args.title}")
    print(proposal_id)


def cmd_list_proposals(args):
    """List proposals"""
    headers, proposals = load_proposals()
    
    if not proposals:
        log("No proposals found")
        return
    
    # Apply filters
    if args.status:
        proposals = [p for p in proposals if p.get('status') == args.status]
    if args.project_id:
        proposals = [p for p in proposals if p.get('project_id') == args.project_id]
    if args.project:
        proposals = [p for p in proposals if args.project.lower() in p.get('project_name', '').lower()]
    
    # Determine output fields
    fields = args.fields.split(',') if args.fields else None
    if fields:
        fields = [f for f in fields if f in headers]
    else:
        default_fields = ['id', 'title', 'status', 'project_name', 'owner', 'last_update']
        fields = [f for f in default_fields if f in headers]
    
    print('\t'.join(fields))
    for p in proposals:
        row = [p.get(f, '') for f in fields]
        print('\t'.join(row))


def cmd_get_proposal(args):
    """Get single proposal"""
    _, proposals = load_proposals()
    
    p = get_proposal_by_id(args.id, proposals)
    if not p:
        die(f"Proposal not found: {args.id}")
    
    if args.json:
        import json
        print(json.dumps(p, ensure_ascii=False, indent=2))
    else:
        for k, v in p.items():
            print(f"{k}: {v}")


def cmd_update_proposal(args):
    """Update proposal - supports ALL CSV fields"""
    headers, proposals = load_proposals()
    _, projects = load_projects()
    
    p = get_proposal_by_id(args.id, proposals)
    if not p:
        die(f"Proposal not found: {args.id}")
    
    old_project_id = p['project_id']
    
    # All possible fields that can be updated
    update_specs = {
        'title': ('str', args.title),
        'owner': ('str', args.owner),
        'status': ('enum', args.status, VALID_PROPOSAL_STATUSES),
        'project_id': ('project', args.project_id),
        'stage': ('enum', args.stage, VALID_PROPOSAL_STAGES),
        'prd_path': ('str', args.prd_path),
        'tech_solution_path': ('str', args.tech_solution_path),
        'project_path': ('str', args.project_path),
        'git_repo': ('url', args.git_repo),
        'deployment_url': ('url', args.deployment_url),
        'deployment_branch': ('str', args.deployment_branch),
        'prd_confirmation': ('enum', args.prd_confirmation, VALID_PRDS),
        'tech_expectations': ('enum', args.tech_expectations, VALID_TECH_EXPS),
        'acceptance': ('enum', args.acceptance, VALID_ACCEPTANCES),
        'research_direction': ('str', args.research_direction),
        'engine': ('str', args.engine),
        'target': ('str', args.target),
        'game_type': ('enum', args.game_type, VALID_GAME_TYPES),
        'notes': ('str', args.notes),
    }
    
    for field, spec in update_specs.items():
        value = spec[1] if len(spec) == 2 else spec[2] if len(spec) == 3 else None
        # Find the actual value from args
        arg_val = getattr(args, field.replace('-', '_'), None)
        if arg_val is None:
            continue
        
        if spec[0] == 'enum':
            if arg_val:
                if spec[2] and arg_val not in spec[2]:
                    raise ValueError(f"Invalid {field}: {arg_val}, valid: {spec[2]}")
            p[field] = arg_val
        elif spec[0] == 'url':
            if arg_val:
                validate_url_or_empty(arg_val, field)
            p[field] = arg_val
        elif spec[0] == 'project':
            if arg_val:
                validate_project_exists(arg_val, projects)
                proj = get_project_by_id(arg_val, projects)
                p['project_id'] = arg_val
                p['project_name'] = proj['name']
                p['git_repo'] = proj.get('git_repo', '')
        else:
            p[field] = arg_val
    
    p['last_update'] = datetime.now().strftime('%Y-%m-%d')
    
    write_csv(PROPOSALS_CSV, headers, proposals)
    
    # Update project proposal count if project changed
    if args.project_id and args.project_id != old_project_id:
        update_project_proposal_count(old_project_id)
        update_project_proposal_count(args.project_id)

    # Auto-sync proposal-index.md from CSV
    cmd_sync_to_index(args)

    log(f"Updated proposal: {args.id}")


def cmd_delete_proposal(args):
    """Delete proposal"""
    headers, proposals = load_proposals()
    
    p = get_proposal_by_id(args.id, proposals)
    if not p:
        die(f"Proposal not found: {args.id}")
    
    project_id = p['project_id']
    
    proposals = [x for x in proposals if x['id'] != args.id]
    write_csv(PROPOSALS_CSV, headers, proposals)

    update_project_proposal_count(project_id)

    # Auto-sync proposal-index.md from CSV
    cmd_sync_to_index(args)

    log(f"Deleted proposal: {args.id}")


def cmd_archive_proposal(args):
    """Archive proposal"""
    headers, proposals = load_proposals()
    
    p = get_proposal_by_id(args.id, proposals)
    if not p:
        die(f"Proposal not found: {args.id}")
    
    p['status'] = 'archived'
    p['last_update'] = datetime.now().strftime('%Y-%m-%d')
    
    write_csv(PROPOSALS_CSV, headers, proposals)
    
    log(f"Archived proposal: {args.id}")


def cmd_archive(args):
    """Bulk archive proposals by project ID or date threshold. Uses regex-based parsing to handle embedded newlines."""
    import re as re_mod
    import io as io_mod

    with open(PROPOSALS_CSV, encoding='utf-8') as f:
        raw_content = f.read()

    FIELDNAMES_ARCH = ['id','title','owner','status','project_id','project_name','stage',
                        'prd_path','tech_solution_path','project_path','git_repo','deployment_url',
                        'deployment_branch','prd_confirmation','tech_expectations','acceptance',
                        'research_direction','last_update','engine','target','game_type','notes']

    p_lines = [l for l in raw_content.split('\n') if re_mod.match(r'^P-\d{8}-\d{3},', l)]
    parsed = {}
    for line in p_lines:
        try:
            reader = csv.DictReader(io_mod.StringIO(line), fieldnames=FIELDNAMES_ARCH)
            for row in reader:
                if row.get('id','').startswith('P-') and row['id'] not in parsed:
                    parsed[row['id']] = row
                    break
        except:
            pass

    to_archive = []
    for pid, row in parsed.items():
        match = True
        if args.project_id and row.get('project_id','') != args.project_id:
            match = False
        if args.before and row.get('last_update',''):
            if row['last_update'] >= args.before:
                match = False
        if match and row.get('status','') != 'archived':
            to_archive.append(pid)

    if not to_archive:
        print("No proposals match the archive criteria")
        return

    print(f"\n=== Archive Report ===")
    print(f"Matched: {len(to_archive)} proposals")
    for pid in sorted(to_archive):
        row = parsed[pid]
        print(f"  {pid} | {row.get('project_id','')} | {row.get('title','')[:50]} | last_update={row.get('last_update','')}")

    if args.dry_run:
        print(f"\n[Dry run] No changes made. Run without --dry-run to archive.")
        return

    # Apply archive: update status=archived for matched proposals
    fixed_lines = []
    for line in p_lines:
        try:
            reader = csv.DictReader(io_mod.StringIO(line), fieldnames=FIELDNAMES_ARCH)
            rows = list(reader)
            for row in rows:
                if row.get('id','').startswith('P-') and row['id'] in to_archive:
                    row['status'] = 'archived'
                    import io as io_module
                    output = io_module.StringIO()
                    writer = csv.DictWriter(output, fieldnames=FIELDNAMES_ARCH, extrasaction='ignore')
                    writer.writerow(row)
                    fixed_lines.append(output.getvalue().rstrip('\n'))
                    break
            else:
                fixed_lines.append(line)
        except:
            fixed_lines.append(line)

    header = "id,title,owner,status,project_id,project_name,stage,prd_path,tech_solution_path,project_path,git_repo,deployment_url,deployment_branch,prd_confirmation,tech_expectations,acceptance,research_direction,last_update,engine,target,game_type,notes\n"
    with open(PROPOSALS_CSV, 'w', encoding='utf-8') as f:
        f.write(header + '\n'.join(fixed_lines))

    print(f"\nArchived {len(to_archive)} proposals. Status set to 'archived'.")

    # Sync index
    class SyncArgs:
        quiet = False
    cmd_sync_to_index(SyncArgs())


def cmd_next_project_id(args):
    """Generate next project ID"""
    _, projects = load_projects()
    next_id = generate_project_id(projects)
    print(next_id)


def cmd_next_proposal_id(args):
    """Generate next proposal ID for a project"""
    _, proposals = load_proposals()
    project_id = args.project_id

    # Filter proposals for this project
    project_proposals = [p for p in proposals if p.get('project_id') == project_id]

    # Generate next ID based on today's date
    today = datetime.now().strftime('%Y%m%d')
    prefix = f"P-{today}-"
    max_num = 0
    for p in project_proposals:
        pid = p.get('id', '')
        if pid.startswith(prefix):
            try:
                num = int(pid.split('-')[-1])
                max_num = max(max_num, num)
            except:
                pass

    next_id = f"{prefix}{max_num + 1:03d}"
    print(next_id)


# ==================== Sync to Index ====================

PROPOSAL_INDEX_PATH = PROPOSALS_ROOT / "proposal-index.md"

def generate_proposal_entry(p, format='detailed') -> str:
    """Generate a single proposal entry in markdown format.
    
    Args:
        p: proposal dict
        format: 'compact' (ID + title + status) or 'detailed' (full 21-field entry)
    """
    pid = p.get('id', '')
    title = p.get('title', '')

    if format == 'compact':
        status = p.get('status', '')
        return f"- **{pid}**: {title} [{status}]"

    # Detailed format (full 21-field entry)
    lines = [f"### {pid}: {title}", ""]

    def add_field(key, value):
        if value:
            lines.append(f"- **{key}**: {value}")

    add_field("Project", p.get('project_name', ''))
    add_field("Owner", p.get('owner', ''))
    add_field("Stage", p.get('stage', ''))
    add_field("Acceptance", p.get('acceptance', ''))
    add_field("Last Update", p.get('last_update', ''))
    add_field("PRD Path", p.get('prd_path', ''))
    add_field("Technical Solution", p.get('tech_solution_path', ''))
    add_field("Project Path", p.get('project_path', ''))

    # Git info: show branch + commit SHA from notes if present
    git_parts = []
    if p.get('deployment_branch'):
        git_parts.append(f"分支: {p.get('deployment_branch')}")
    # Extract commit SHA from notes if present (format: ...Commit: XXXXXXXX)
    notes = p.get('notes', '')
    import re
    sha_match = re.search(r'Commit:\s*([0-9a-f]{7,40})', notes)
    if sha_match:
        git_parts.append(f"Commit: {sha_match.group(1)}")
    if p.get('git_repo'):
        git_parts.append(f"[GitHub]({p.get('git_repo')})")
    if git_parts:
        lines.append(f"- **Git**: {' | '.join(git_parts)}")

    # Deployment
    if p.get('deployment_url'):
        lines.append(f"- **Deployment**: [{p.get('deployment_url')}]({p.get('deployment_url')})")

    # Description from notes (strip commit info for display)
    desc = re.sub(r'Commit:\s*[0-9a-f]{7,40}\s*', '', notes).strip()
    if desc:
        add_field("Description", desc)

    lines.append("---")
    return '\n'.join(lines)


def cmd_sync_to_index(args):
    """Sync proposal-index.md from CSV data (CSV is source of truth).

    Supports --dry-run and --verbose flags.
    """
    _, proposals = load_proposals()
    _, projects = load_projects()

    dry_run = getattr(args, 'dry_run', False)
    verbose = getattr(args, 'verbose', False) or dry_run

    if not proposals:
        log("No proposals found in CSV — skipping index generation")
        return

    # Sort by last_update descending
    sorted_proposals = sorted(
        proposals,
        key=lambda p: p.get('last_update', ''),
        reverse=True
    )

    # Group by project_id for project-level headers
    project_ids = []
    seen_projects = set()
    for p in sorted_proposals:
        pid = p.get('project_id', '')
        if pid and pid not in seen_projects:
            seen_projects.add(pid)
            project_ids.append(pid)

    # Build project lookup
    project_map = {proj['id']: proj for proj in projects}

    # Generate markdown
    lines = [
        "# Proposal Index",
        "",
        f"Last updated: {datetime.now().strftime('%Y-%m-%d')}",
        f"Total: {len(proposals)} proposals, {len(project_ids)} projects",
        ""
    ]

    current_project_id = None
    for p in sorted_proposals:
        pid = p.get('project_id', '')

        # Project header when project changes
        if pid != current_project_id:
            current_project_id = pid
            proj = project_map.get(pid)
            if proj:
                lines.extend([
                    f"## {proj['id']}: {proj['name']}",
                    "",
                    f"- **Description**: {proj.get('description', '')}",
                    f"- **Git Repo**: {proj.get('git_repo', '')}",
                    f"- **Local Path**: {proj.get('local_path', '')}",
                    ""
                ])

        lines.append(generate_proposal_entry(p))
        lines.append("")

    content = '\n'.join(lines)

    if dry_run:
        # Show what would be written without touching files
        content_lines = content.split('\n')
        print(f"[DRY-RUN] Would write {PROPOSAL_INDEX_PATH}")
        print(f"  Total lines: {len(content_lines)}")
        print(f"  Proposals: {len(proposals)}")
        print(f"  Projects: {len(project_ids)}")
        print()
        if verbose:
            print("First 5 entries preview:")
            preview_count = 0
            for line in content_lines:
                if line.startswith('### P-'):
                    print(f"  {line}")
                    preview_count += 1
                    if preview_count >= 5:
                        break
            print()
            # Show skipped entries (would be skipped — none currently since we generate full index)
            # but check vs current index for verbose
            if PROPOSAL_INDEX_PATH.exists():
                with open(PROPOSAL_INDEX_PATH, encoding='utf-8') as f:
                    current_content = f.read()
                current_ids = set(re.findall(r'^### (P-\d{8}-\d{3}):', current_content, re.MULTILINE))
                new_ids = {p['id'] for p in proposals}
                missing = new_ids - current_ids
                extra = current_ids - new_ids
                if missing:
                    print(f"  Would add: {len(missing)} proposals")
                    for mid in sorted(list(missing))[:5]:
                        print(f"    + {mid}")
                if extra:
                    print(f"  Would remove: {len(extra)} proposals")
                    for eid in sorted(list(extra))[:5]:
                        print(f"    - {eid}")
                if not missing and not extra:
                    print("  No changes to existing entries")
            else:
                print("  (no existing index — would be created fresh)")
        print()
        print("[DRY-RUN] No files written. Remove --dry-run to apply changes.")
        return

    # Write atomically
    tmp_path = PROPOSAL_INDEX_PATH.with_suffix('.md.tmp')
    bak_path = PROPOSAL_INDEX_PATH.with_suffix('.md.bak')

    # Pre-write diff for verbose mode
    if verbose and PROPOSAL_INDEX_PATH.exists():
        with open(PROPOSAL_INDEX_PATH, encoding='utf-8') as f:
            current_content = f.read()
        current_ids = set(re.findall(r'^### (P-\d{8}-\d{3}):', current_content, re.MULTILINE))
        new_ids = {p['id'] for p in proposals}
        missing = new_ids - current_ids
        extra = current_ids - new_ids
        changed_count = 0
        for p in proposals:
            if p['id'] in missing:
                changed_count += 1

    with open(tmp_path, 'w', encoding='utf-8') as f:
        f.write(content)

    if PROPOSAL_INDEX_PATH.exists():
        import shutil
        shutil.copy2(PROPOSAL_INDEX_PATH, bak_path)

    tmp_path.rename(PROPOSAL_INDEX_PATH)

    log(f"Synced proposal-index.md: {len(proposals)} proposals, {len(project_ids)} projects")
    print(f"Written: {PROPOSAL_INDEX_PATH}")

    if verbose:
        adds = len(missing) if 'missing' in dir() else 0
        deletes = len(extra) if 'extra' in dir() else 0
        print(f"[VERBOSE] Adds: {adds}, Removes: {deletes}")


# ==================== Audit ====================

def cmd_audit(args):
    """Audit proposals.csv for data quality issues, optionally auto-fix.

    Uses regex-based parsing (each physical P- line = one row) to handle
    embedded newlines in notes fields correctly.
    """
    import re as re_mod
    from collections import defaultdict
    import io as io_mod

    with open(PROPOSALS_CSV, encoding='utf-8') as f:
        raw_content = f.read()

    FIELDNAMES_AUDIT = ['id','title','owner','status','project_id','project_name','stage',
                         'prd_path','tech_solution_path','project_path','git_repo','deployment_url',
                         'deployment_branch','prd_confirmation','tech_expectations','acceptance',
                         'research_direction','last_update','engine','target','game_type','notes']

    # Parse each physical line as a separate row (regex: lines starting with P-)
    p_lines = [l for l in raw_content.split('\n') if re_mod.match(r'^P-\d{8}-\d{3},', l)]
    parsed = []
    for line in p_lines:
        try:
            reader = csv.DictReader(io_mod.StringIO(line), fieldnames=FIELDNAMES_AUDIT)
            for row in reader:
                if row.get('id','').startswith('P-'):
                    parsed.append(row)
                    break
        except:
            pass

    issues = []
    fix_counts = {
        'true_duplicate': 0,
        'empty_title': 0,
        'empty_project_id': 0,
        'invalid_status': 0,
        'invalid_stage': 0,
        'empty_last_update': 0,
    }

    # 1. TRUE duplicate detection: same id + same project_id
    id_proj_count = defaultdict(int)
    for row in parsed:
        id_proj_count[(row['id'], row.get('project_id',''))] += 1

    true_dupes = {k: v for k, v in id_proj_count.items() if v > 1}
    if true_dupes:
        fix_counts['true_duplicate'] = sum(v - 1 for _, v in true_dupes.items())
        shown = 0
        for (pid, proj), count in sorted(true_dupes.items(), key=lambda x: -x[1]):
            if shown >= 5:
                issues.append(('info', f"... and {len(true_dupes) - 5} more duplicate groups", ""))
                break
            issues.append(('error', f"Duplicate ID '{pid}' in project '{proj}': {count} copies",
                          "keep last copy, archive others"))
            shown += 1

    # 2. Empty title
    for row in parsed:
        if not row.get('title', '').strip():
            issues.append(('error', f"[{row['id']}]: title is empty", f"title=UNTITLED-{row['id']}"))
            fix_counts['empty_title'] += 1

    # 3. Empty project_id
    for row in parsed:
        if not row.get('project_id', '').strip():
            issues.append(('error', f"[{row['id']}]: project_id is empty", "project_id=MISSING"))
            fix_counts['empty_project_id'] += 1

    # 4. Invalid status
    for row in parsed:
        status = row.get('status', '')
        if status and status not in VALID_PROPOSAL_STATUSES:
            issues.append(('warn', f"[{row['id']}]: invalid status='{status}'", "status=unknown"))
            fix_counts['invalid_status'] += 1

    # 5. Invalid stage
    for row in parsed:
        stage = row.get('stage', '')
        if stage and stage not in VALID_PROPOSAL_STAGES:
            issues.append(('warn', f"[{row['id']}]: invalid stage='{stage}'", "stage=proposal"))
            fix_counts['invalid_stage'] += 1

    # 6. Empty last_update
    for row in parsed:
        if not row.get('last_update', '').strip():
            issues.append(('warn', f"[{row['id']}]: last_update is empty", "last_update=2026-05-21"))
            fix_counts['empty_last_update'] += 1

    # Output report
    print(f"\n=== CSV Audit Report ===")
    print(f"Total rows (physical P- lines): {len(parsed)}")
    print(f"True duplicate groups (same ID + same project): {len(true_dupes)}")
    print(f"")
    print(f"Issues found:")
    print(f"  True duplicates:     {fix_counts['true_duplicate']}")
    print(f"  Empty title:         {fix_counts['empty_title']}")
    print(f"  Empty project_id:    {fix_counts['empty_project_id']}")
    print(f"  Invalid status:     {fix_counts['invalid_status']}")
    print(f"  Invalid stage:      {fix_counts['invalid_stage']}")
    print(f"  Empty last_update:  {fix_counts['empty_last_update']}")
    print(f"")

    if issues:
        print(f"Details (max 20):")
        for sev, desc, fix in issues[:20]:
            prefix = "ERROR" if sev == 'error' else "WARN "
            print(f"  [{prefix}] {desc}")
            print(f"         Fix: {fix}")
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more issues")

    total_issues = sum(fix_counts.values())
    print(f"\nTotal: {total_issues} issues")

    # Auto-fix
    if args.fix and total_issues > 0:
        today = datetime.now().strftime('%Y-%m-%d')

        # 6a. Fill empty last_update
        for row in parsed:
            if not row.get('last_update', '').strip():
                row['last_update'] = today

        # 6b. Fix empty title
        for row in parsed:
            if not row.get('title', '').strip():
                row['title'] = f"UNTITLED-{row['id']}"

        # 6c. Fix empty project_id
        for row in parsed:
            if not row.get('project_id', '').strip():
                row['project_id'] = 'MISSING'
                row['project_name'] = 'MISSING'

        # 6d. Fix invalid status
        for row in parsed:
            status = row.get('status', '')
            if status and status not in VALID_PROPOSAL_STATUSES:
                row['status'] = 'unknown'

        # 6e. Fix invalid stage
        for row in parsed:
            stage = row.get('stage', '')
            if stage and stage not in VALID_PROPOSAL_STAGES:
                row['stage'] = 'proposal'

        # 6f. Fix TRUE duplicates: keep last occurrence, archive others
        if true_dupes:
            seen = set()
            deduped = []
            for row in reversed(parsed):
                key = (row['id'], row.get('project_id',''))
                if key not in seen:
                    deduped.append(row)
                    seen.add(key)
                else:
                    row['id'] = f"{row['id']}-dup"
                    row['status'] = 'archived'
                    deduped.append(row)
            parsed = list(reversed(deduped))
            print(f"\nFixed {fix_counts['true_duplicate']} true duplicate rows")

        # Write back
        write_csv(PROPOSALS_CSV, FIELDNAMES_AUDIT, parsed)
        print(f"\nAuto-fixed {total_issues} issues in {PROPOSALS_CSV}")

        # Re-sync index (skip if --csv-only)
        if not getattr(args, 'csv_only', False):
            cmd_sync_to_index(args)
            print("Re-synced proposal-index.md")

    elif not args.fix and total_issues > 0:
        print(f"\nRun with --fix to auto-repair issues")


# ==================== Diff ====================

def cmd_diff(args):
    """Compare two proposals by ID and show field-level differences."""
    import re as re_mod
    import io as io_mod

    with open(PROPOSALS_CSV, encoding='utf-8') as f:
        raw_content = f.read()

    FIELDNAMES_DIFF = ['id','title','owner','status','project_id','project_name','stage',
                        'prd_path','tech_solution_path','project_path','git_repo','deployment_url',
                        'deployment_branch','prd_confirmation','tech_expectations','acceptance',
                        'research_direction','last_update','engine','target','game_type','notes']

    # Parse each physical line as a separate row
    p_lines = [l for l in raw_content.split('\n') if re_mod.match(r'^P-\d{8}-\d{3},', l)]
    parsed = {}
    for line in p_lines:
        try:
            reader = csv.DictReader(io_mod.StringIO(line), fieldnames=FIELDNAMES_DIFF)
            for row in reader:
                if row.get('id','').startswith('P-'):
                    parsed[row['id']] = row
                    break
        except:
            pass

    id1, id2 = args.id1, args.id2

    if id1 not in parsed:
        die(f"Proposal '{id1}' not found in CSV")
    if id2 not in parsed:
        die(f"Proposal '{id2}' not found in CSV")

    p1, p2 = parsed[id1], parsed[id2]

    # Fields to compare (exclude notes for readability)
    compare_fields = [f for f in FIELDNAMES_DIFF if f not in ('notes',)]

    print(f"\n=== Proposal Diff ===")
    print(f"  Left:  {id1}  [{p1.get('project_id','')}]")
    print(f"  Right: {id2}  [{p2.get('project_id','')}]")
    print()

    same = []
    diffs = []
    only_left = []
    only_right = []

    for field in compare_fields:
        v1 = p1.get(field, '').strip()
        v2 = p2.get(field, '').strip()
        if v1 == v2:
            if v1:  # Only show if non-empty
                same.append((field, v1))
        else:
            diffs.append((field, v1, v2))

    if diffs:
        print(f"--- Different ({len(diffs)}) ---")
        for field, v1, v2 in diffs:
            print(f"  {field}:")
            print(f"    - {v1 or '(empty)'}")
            print(f"    + {v2 or '(empty)'}")

    if same:
        print(f"\n--- Same ({len(same)}) ---")
        for field, v in same[:10]:
            print(f"  {field}: {v[:60]}{'...' if len(v) > 60 else ''}")
        if len(same) > 10:
            print(f"  ... and {len(same) - 10} more")

    print(f"\nTotal: {len(diffs)} different, {len(same)} same fields")


# ==================== Advance (State Machine) ====================

def cmd_advance(args):
    """Advance proposal to next state in lifecycle."""
    headers, proposals = load_proposals()

    p = get_proposal_by_id(args.id, proposals)
    if not p:
        die(f"Proposal not found: {args.id}")

    current = p.get('status', '')
    next_status = STATUS_TRANSITIONS.get(current)

    if not next_status:
        die(f"Cannot advance from status '{current}' — no transition defined")

    p['status'] = next_status
    p['last_update'] = datetime.now().strftime('%Y-%m-%d')

    # Auto-fill related fields
    auto_fills = AUTO_FILL_ON_TRANSITION.get(next_status, {})
    for field, value in auto_fills.items():
        if not p.get(field):
            p[field] = value

    write_csv(PROPOSALS_CSV, headers, proposals)
    log(f"Advanced {args.id}: {current} → {next_status}")
    print(f"{args.id}: {current} → {next_status}")

    if not args.no_sync:
        cmd_sync_to_index(args)


# ==================== Validate ====================

def cmd_validate(args):
    """Validate a single proposal's fields."""
    headers, proposals = load_proposals()

    p = get_proposal_by_id(args.id, proposals)
    if not p:
        die(f"Proposal not found: {args.id}")

    errors = []
    warnings = []

    # Required non-empty
    if not p.get('title', '').strip():
        errors.append("title is empty")
    if not p.get('project_id', '').strip():
        errors.append("project_id is empty")

    # Enum checks
    status = p.get('status', '')
    if status and status not in VALID_PROPOSAL_STATUSES:
        warnings.append(f"status '{status}' not in VALID_PROPOSAL_STATUSES")

    stage = p.get('stage', '')
    if stage and stage not in VALID_PROPOSAL_STAGES:
        warnings.append(f"stage '{stage}' not in VALID_PROPOSAL_STAGES")

    prd = p.get('prd_confirmation', '')
    if prd and prd not in VALID_PRDS:
        warnings.append(f"prd_confirmation '{prd}' not in VALID_PRDS")

    tech = p.get('tech_expectations', '')
    if tech and tech not in VALID_TECH_EXPS:
        warnings.append(f"tech_expectations '{tech}' not in VALID_TECH_EXPS")

    acc = p.get('acceptance', '')
    if acc and acc not in VALID_ACCEPTANCES:
        warnings.append(f"acceptance '{acc}' not in VALID_ACCEPTANCES")

    # Date format
    last_up = p.get('last_update', '')
    if last_up:
        import re
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', last_up):
            warnings.append(f"last_update '{last_up}' doesn't match YYYY-MM-DD")

    # ID format
    pid = p.get('id', '')
    if pid and not PROPOSAL_ID_PATTERN.match(pid):
        errors.append(f"id '{pid}' doesn't match P-YYYYMMDD-XXX format")

    proj_id = p.get('project_id', '')
    if proj_id and not PROJECT_ID_PATTERN.match(proj_id):
        errors.append(f"project_id '{proj_id}' doesn't match PRJ-YYYYMMDD-XXX format")

    print(f"\n=== Validate: {args.id} ===")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
    else:
        print("No errors.")

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")
    else:
        print("No warnings.")

    if errors:
        sys.exit(1)
    elif warnings:
        sys.exit(2)
    else:
        print("PASS")


# ==================== Search ====================

def cmd_search(args):
    """Search proposals by keyword across all text fields."""
    headers, proposals = load_proposals()
    keyword = args.keyword.lower()
    matched = []

    for p in proposals:
        searchable = ' '.join(str(v) for v in p.values()).lower()
        if keyword in searchable:
            matched.append(p)

    print(f"\n=== Search: '{args.keyword}' — {len(matched)} matches ===")
    fields = ['id', 'title', 'status', 'project_name', 'owner', 'last_update']
    print('\t'.join(fields))
    for p in matched:
        row = [p.get(f, '') for f in fields]
        print('\t'.join(row))


# ==================== Stats ====================

def cmd_stats(args):
    """Output proposal statistics summary."""
    _, proposals = load_proposals()
    _, projects = load_projects()

    from collections import Counter

    status_counts = Counter(p.get('status', '') for p in proposals)
    project_counts = Counter(p.get('project_name', '') for p in proposals)

    today = datetime.now().strftime('%Y-%m-%d')
    this_month = today[:7]  # YYYY-MM
    this_month_count = sum(1 for p in proposals if p.get('last_update', '').startswith(this_month))

    print(f"\n=== Proposal Stats ===")
    print(f"Total proposals : {len(proposals)}")
    print(f"Total projects  : {len(projects)}")
    print(f"This month      : {this_month_count}")
    print()

    print("By status:")
    for status, count in status_counts.most_common():
        print(f"  {status or '(empty)':<30} {count}")
    print()

    if args.top:
        print(f"Top {args.top} projects:")
        for proj, count in project_counts.most_common(args.top):
            print(f"  {proj:<30} {count}")


# ==================== Duplicate ====================

def cmd_duplicate(args):
    """Duplicate a proposal with a new ID."""
    headers, proposals = load_proposals()

    source = get_proposal_by_id(args.id, proposals)
    if not source:
        die(f"Proposal not found: {args.id}")

    new_id = generate_proposal_id(proposals)
    new_data = dict(source)
    new_data['id'] = new_id
    new_data['title'] = f"{source.get('title', '')} (copy)"
    new_data['status'] = 'intake'
    new_data['last_update'] = datetime.now().strftime('%Y-%m-%d')
    new_data['notes'] = f"Duplicated from {args.id}"

    proposals.append(new_data)
    write_csv(PROPOSALS_CSV, headers, proposals)

    # Update project count
    update_project_proposal_count(source.get('project_id', ''))

    log(f"Duplicated {args.id} → {new_id}")
    print(new_id)

    if not args.no_sync:
        cmd_sync_to_index(args)


# ==================== Migrate ====================

def cmd_migrate(args):
    """Migrate proposals from one project to another."""
    _, projects = load_projects()

    from_proj = get_project_by_id(args.from_project, projects)
    to_proj = get_project_by_id(args.to_project, projects)
    if not from_proj:
        die(f"Source project not found: {args.from_project}")
    if not to_proj:
        die(f"Target project not found: {args.to_project}")

    headers, proposals = load_proposals()
    migrated = []

    for p in proposals:
        if p.get('project_id') == args.from_project:
            p['project_id'] = args.to_project
            p['project_name'] = to_proj['name']
            p['git_repo'] = to_proj.get('git_repo', '')
            p['last_update'] = datetime.now().strftime('%Y-%m-%d')
            migrated.append(p['id'])

    if not migrated:
        die(f"No proposals found for project: {args.from_project}")

    write_csv(PROPOSALS_CSV, headers, proposals)

    # Update counts
    update_project_proposal_count(args.from_project)
    update_project_proposal_count(args.to_project)

    log(f"Migrated {len(migrated)} proposals: {args.from_project} → {args.to_project}")
    print(f"Migrated {len(migrated)} proposals")
    for pid in migrated:
        print(f"  {pid}")

    if not args.no_sync:
        cmd_sync_to_index(args)


# ==================== Stats ====================

def cmd_stats_proposals(args):
    """Show proposal statistics: totals, status/stage distribution, project counts, recent activity."""
    import json

    _, proposals = load_proposals()
    _, projects = load_projects()

    total_proposals = len(proposals)
    total_projects = len(projects)

    # Status distribution
    status_counts = {}
    for p in proposals:
        s = p.get('status', '') or '(empty)'
        status_counts[s] = status_counts.get(s, 0) + 1

    # Stage distribution
    stage_counts = {}
    for p in proposals:
        s = p.get('stage', '') or '(empty)'
        stage_counts[s] = stage_counts.get(s, 0) + 1

    # Proposals per project (top 10)
    project_counts = {}
    for p in proposals:
        pid = p.get('project_id', '') or '(none)'
        project_counts[pid] = project_counts.get(pid, 0) + 1
    top_projects = sorted(project_counts.items(), key=lambda x: -x[1])[:10]

    # Recent activity: last_update distribution
    now = datetime.now()
    cutoff_7 = (now - timedelta(days=7)).strftime('%Y-%m-%d')
    cutoff_30 = (now - timedelta(days=30)).strftime('%Y-%m-%d')

    count_7 = 0
    count_30 = 0
    count_older = 0
    for p in proposals:
        lu = p.get('last_update', '')
        if lu >= cutoff_7:
            count_7 += 1
        elif lu >= cutoff_30:
            count_30 += 1
        else:
            count_older += 1

    if args.format == 'json':
        stats = {
            'total_proposals': total_proposals,
            'total_projects': total_projects,
            'status_distribution': dict(sorted(status_counts.items(), key=lambda x: -x[1])),
            'stage_distribution': dict(sorted(stage_counts.items(), key=lambda x: -x[1])),
            'top_projects': [{'project_id': pid, 'count': c} for pid, c in top_projects],
            'recent_activity': {
                'last_7_days': count_7,
                'last_30_days': count_30,
                'older': count_older,
            }
        }
        print(json.dumps(stats, ensure_ascii=False, indent=2))
    else:
        # Plain text tab-separated output
        print(f"Total proposals\t{total_proposals}")
        print(f"Total projects\t{total_projects}")
        print()
        print("Status distribution")
        for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
            print(f"  {status}\t{count}")
        print()
        print("Stage distribution")
        for stage, count in sorted(stage_counts.items(), key=lambda x: -x[1]):
            print(f"  {stage}\t{count}")
        print()
        print("Proposals per project (top 10)")
        print(f"{'Project ID'}\t{'Count'}")
        for pid, count in top_projects:
            print(f"{pid}\t{count}")
        print()
        print("Recent activity (by last_update)")
        print(f"Last 7 days\t{count_7}")
        print(f"Last 30 days\t{count_30}")
        print(f"Older\t{count_older}")


# ==================== Validate ====================

def cmd_validate_proposals(args):
    """Validate proposals.csv against business rules and optionally fix issues."""
    import re as re_mod
    import io as io_mod

    _, proposals = load_proposals()
    _, projects = load_projects()

    # Build project ID set
    project_ids = {p['id'] for p in projects}
    project_ids_parsed = project_ids  # for CSV-based check below

    issues = []

    # 1. Every proposal has a project_id that exists in projects.csv
    for p in proposals:
        pid = p.get('project_id', '').strip()
        if not pid:
            issues.append(('error', f"[{p['id']}] project_id is empty", 'proposal references no project'))
        elif pid not in project_ids:
            issues.append(('error', f"[{p['id']}] project_id='{pid}' not found in projects.csv", 'project does not exist'))

    # 2. Every project_id in projects.csv has at least one proposal (warn if orphaned)
    proposal_project_ids = {p.get('project_id', '').strip() for p in proposals}
    for pid in project_ids:
        if pid and pid not in proposal_project_ids:
            issues.append(('warn', f"[project {pid}] no proposals found (orphaned project)", "consider linking or removing"))

    # 3. proposal-index.md is in sync with CSV (same number of proposals, same IDs)
    if PROPOSAL_INDEX_PATH.exists():
        with open(PROPOSAL_INDEX_PATH, encoding='utf-8') as f:
            index_content = f.read()
        # Count proposal entries in index (### P-YYYYMMDD-XXX: pattern)
        index_ids = set(re_mod.findall(r'^### (P-\d{8}-\d{3}):', index_content, re_mod.MULTILINE))
        csv_ids = {p['id'] for p in proposals}
        missing_in_index = csv_ids - index_ids
        extra_in_index = index_ids - csv_ids
        if missing_in_index:
            for mid in sorted(list(missing_in_index)[:5]):
                issues.append(('error', f"[index] proposal {mid} in CSV but missing from proposal-index.md", 'run sync-to-index'))
        if extra_in_index:
            for eid in sorted(list(extra_in_index)[:5]):
                issues.append(('error', f"[index] proposal {eid} in proposal-index.md but not in CSV", 'run sync-to-index'))
        if len(csv_ids) != len(index_ids):
            issues.append(('info', f"[index] count mismatch: CSV={len(csv_ids)} vs index={len(index_ids)}", 'run sync-to-index'))

    # 4. All deployment_url fields are valid URLs or empty
    for p in proposals:
        url = p.get('deployment_url', '').strip()
        if url and not (url.startswith('http://') or url.startswith('https://') or url.startswith('git@') or url.startswith('//')):
            issues.append(('error', f"[{p['id']}] deployment_url='{url}' is not a valid URL", 'must start with http://, https://, or git@'))

    # Report
    print(f"\n=== Validation Report ===")
    print(f"Proposals: {len(proposals)}")
    print(f"Projects: {len(projects)}")
    print()

    error_count = sum(1 for s, _, _ in issues if s == 'error')
    warn_count = sum(1 for s, _, _ in issues if s == 'warn')
    info_count = sum(1 for s, _, _ in issues if s == 'info')

    print(f"Issues: {len(issues)} total ({error_count} errors, {warn_count} warnings, {info_count} info)")
    print()

    if issues:
        print("Details:")
        for sev, desc, fix in issues[:50]:
            prefix = "ERROR" if sev == 'error' else "WARN " if sev == 'warn' else "INFO "
            print(f"  [{prefix}] {desc}")
            if fix:
                print(f"         → {fix}")
        if len(issues) > 50:
            print(f"  ... and {len(issues) - 50} more issues")
        print()
        if error_count > 0:
            print("VALIDATION: FAIL")
        else:
            print("VALIDATION: PASS (warnings only)")
    else:
        print("VALIDATION: PASS")

    if args.fix and issues:
        # --fix only fixes CSV issues (empty title, etc.) by delegating to audit --fix
        print("\n--fix passed but no auto-fixable issues in validate (try 'audit --fix' for CSV fixes)")


# ==================== Main ====================

def main():
    parser = argparse.ArgumentParser(
        description='Proposal System Data Management CLI - CSV is source of truth',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # ==================== Project Commands ====================
    proj_parser = subparsers.add_parser('project', help='Project management')
    proj_sub = proj_parser.add_subparsers(dest='subcommand')
    
    # project add
    p_add = proj_sub.add_parser('add', help='Add new project')
    p_add.add_argument('--id', help='Project ID (auto-generated if not specified)')
    p_add.add_argument('--name', '-n', required=True, help='Project name')
    p_add.add_argument('--git-repo', help='Git repository URL')
    p_add.add_argument('--local-path', help='Local workspace path')
    p_add.add_argument('--description', '-d', help='Project description')
    p_add.add_argument('--init-workspace', action='store_true', help='Initialize workspace directories')
    p_add.set_defaults(func=cmd_add_project)
    
    # project list
    p_list = proj_sub.add_parser('list', help='List projects')
    p_list.add_argument('--fields', '-f', help='Output fields (comma-separated)')
    p_list.set_defaults(func=cmd_list_projects)
    
    # project get
    p_get = proj_sub.add_parser('get', help='Get project details')
    p_get.add_argument('id', help='Project ID')
    p_get.add_argument('--json', action='store_true', help='JSON output')
    p_get.set_defaults(func=cmd_get_project)
    
    # project update
    p_update = proj_sub.add_parser('update', help='Update project')
    p_update.add_argument('id', help='Project ID')
    p_update.add_argument('--name', '-n', help='Project name')
    p_update.add_argument('--git-repo', help='Git repository URL')
    p_update.add_argument('--local-path', help='Local workspace path')
    p_update.add_argument('--description', '-d', help='Project description')
    p_update.set_defaults(func=cmd_update_project)
    
    # project delete
    p_del = proj_sub.add_parser('delete', help='Delete project')
    p_del.add_argument('id', help='Project ID')
    p_del.add_argument('--force', '-f', action='store_true', help='Force delete even with active proposals')
    p_del.set_defaults(func=cmd_delete_project)
    
    # project init-workspace
    p_init = proj_sub.add_parser('init-workspace', help='Initialize project workspace')
    p_init.add_argument('project_id', help='Project ID')
    p_init.add_argument('--workspace', '-w', default='dev,pm,test,research', help='Workspace types (comma-separated)')
    p_init.set_defaults(func=cmd_init_workspace)

    # project next-id
    p_next = proj_sub.add_parser('next-id', help='Generate next project ID')
    p_next.set_defaults(func=cmd_next_project_id)

    # ==================== Proposal Commands ====================
    prop_parser = subparsers.add_parser('proposal', help='Proposal management')
    prop_sub = prop_parser.add_subparsers(dest='subcommand')
    
    # proposal add
    pr_add = prop_sub.add_parser('add', help='Add new proposal')
    pr_add.add_argument('--id', help='Proposal ID (auto-generated if not specified)')
    pr_add.add_argument('--title', '-t', required=True, help='Proposal title')
    pr_add.add_argument('--project-id', required=True, help='Project ID')
    pr_add.add_argument('--owner', '-o', help='Owner')
    pr_add.add_argument('--status', '-s', default='intake', help='Status')
    pr_add.add_argument('--stage', default='proposal', help='Stage')
    pr_add.add_argument('--prd-path', help='PRD document path')
    pr_add.add_argument('--tech-solution-path', help='Technical solution path')
    pr_add.add_argument('--project-path', help='Local project path')
    pr_add.add_argument('--git-repo', help='Git repository URL')
    pr_add.add_argument('--deployment-url', help='Deployment URL')
    pr_add.add_argument('--deployment-branch', help='Deployment branch')
    pr_add.add_argument('--prd-confirmation', help='PRD confirmation status')
    pr_add.add_argument('--tech-expectations', help='Technical expectations status')
    pr_add.add_argument('--acceptance', help='Acceptance status')
    pr_add.add_argument('--research-direction', help='Research direction')
    pr_add.add_argument('--engine', help='Engine')
    pr_add.add_argument('--target', help='Target platform')
    pr_add.add_argument('--game-type', help='Game type')
    pr_add.add_argument('--notes', help='Notes')
    pr_add.set_defaults(func=cmd_add_proposal)
    
    # proposal list
    pr_list = prop_sub.add_parser('list', help='List proposals')
    pr_list.add_argument('--project-id', help='Filter by project ID')
    pr_list.add_argument('--project', help='Filter by project name (partial match)')
    pr_list.add_argument('--status', '-s', help='Filter by status')
    pr_list.add_argument('--fields', '-f', help='Output fields (comma-separated)')
    pr_list.set_defaults(func=cmd_list_proposals)
    
    # proposal get
    pr_get = prop_sub.add_parser('get', help='Get proposal details')
    pr_get.add_argument('id', help='Proposal ID')
    pr_get.add_argument('--json', action='store_true', help='JSON output')
    pr_get.set_defaults(func=cmd_get_proposal)
    
    # proposal update
    pr_update = prop_sub.add_parser('update', help='Update proposal (all fields)')
    pr_update.add_argument('id', help='Proposal ID')
    pr_update.add_argument('--title', '-t', help='Proposal title')
    pr_update.add_argument('--owner', '-o', help='Owner')
    pr_update.add_argument('--status', '-s', help='Status')
    pr_update.add_argument('--project-id', help='Project ID')
    pr_update.add_argument('--stage', help='Stage')
    pr_update.add_argument('--prd-path', help='PRD document path')
    pr_update.add_argument('--tech-solution-path', help='Technical solution path')
    pr_update.add_argument('--project-path', help='Local project path')
    pr_update.add_argument('--git-repo', help='Git repository URL')
    pr_update.add_argument('--deployment-url', help='Deployment URL')
    pr_update.add_argument('--deployment-branch', help='Deployment branch')
    pr_update.add_argument('--prd-confirmation', help='PRD confirmation status')
    pr_update.add_argument('--tech-expectations', help='Technical expectations status')
    pr_update.add_argument('--acceptance', help='Acceptance status')
    pr_update.add_argument('--research-direction', help='Research direction')
    pr_update.add_argument('--engine', help='Engine')
    pr_update.add_argument('--target', help='Target platform')
    pr_update.add_argument('--game-type', help='Game type')
    pr_update.add_argument('--notes', help='Notes')
    pr_update.set_defaults(func=cmd_update_proposal)
    
    # proposal delete
    pr_del = prop_sub.add_parser('delete', help='Delete proposal')
    pr_del.add_argument('id', help='Proposal ID')
    pr_del.set_defaults(func=cmd_delete_proposal)
    
    # proposal archive
    pr_archive = prop_sub.add_parser('archive', help='Archive proposal')
    pr_archive.add_argument('id', help='Proposal ID')
    pr_archive.set_defaults(func=cmd_archive_proposal)

    # proposal next-id
    pr_next = prop_sub.add_parser('next-id', help='Generate next proposal ID for a project')
    pr_next.add_argument('project_id', help='Project ID (e.g. PRJ-20260516-001)')
    pr_next.set_defaults(func=cmd_next_proposal_id)

    # proposal sync-to-index
    pr_sync = prop_sub.add_parser('sync-to-index', help='Sync proposal-index.md from CSV (CSV is source of truth)')
    pr_sync.add_argument('--dry-run', action='store_true', help='Show what would be written without making changes')
    pr_sync.add_argument('--verbose', '-v', action='store_true', help='Show per-proposal changes and counts')
    pr_sync.set_defaults(func=cmd_sync_to_index)

    # proposal audit
    pr_audit = prop_sub.add_parser('audit', help='Audit proposals.csv for data quality issues')
    pr_audit.add_argument('--fix', action='store_true', help='Auto-fix issues found')
    pr_audit.add_argument('--csv-only', action='store_true', help='Only audit and report, skip index sync')
    pr_audit.set_defaults(func=cmd_audit)

    # proposal validate-csv
    pr_validate_csv = prop_sub.add_parser('validate-csv', help='Validate entire proposals.csv against business rules (project refs, index sync, URLs)')
    pr_validate_csv.add_argument('--fix', action='store_true', help='Auto-fix issues (delegates to audit --fix)')
    pr_validate_csv.set_defaults(func=cmd_validate_proposals)

    # proposal archive-project
    pr_arch_proj = prop_sub.add_parser('archive-project', help='Archive all proposals for a project')
    pr_arch_proj.add_argument('--project-id', help='Project ID to archive')
    pr_arch_proj.add_argument('--before', help='Archive proposals with last_update before date (YYYY-MM-DD)')
    pr_arch_proj.add_argument('--dry-run', action='store_true', help='Show what would be archived without changes')
    pr_arch_proj.set_defaults(func=cmd_archive)

    # proposal diff
    pr_diff = prop_sub.add_parser('diff', help='Compare two proposals by ID')
    pr_diff.add_argument('id1', help='First proposal ID')
    pr_diff.add_argument('id2', help='Second proposal ID')
    pr_diff.set_defaults(func=cmd_diff)

    # proposal advance
    pr_advance = prop_sub.add_parser('advance', help='Advance proposal to next state')
    pr_advance.add_argument('id', help='Proposal ID')
    pr_advance.add_argument('--no-sync', action='store_true', help='Skip auto-sync to index')
    pr_advance.set_defaults(func=cmd_advance)

    # proposal validate
    pr_validate = prop_sub.add_parser('validate', help='Validate a proposal\'s fields')
    pr_validate.add_argument('id', help='Proposal ID')
    pr_validate.set_defaults(func=cmd_validate)

    # proposal search
    pr_search = prop_sub.add_parser('search', help='Search proposals by keyword')
    pr_search.add_argument('keyword', help='Keyword to search')
    pr_search.set_defaults(func=cmd_search)

    # proposal stats
    pr_stats = prop_sub.add_parser('stats', help='Show proposal statistics (totals, status/stage distribution, project counts, recent activity)')
    pr_stats.add_argument('--format', '-f', choices=['text', 'json'], default='text', help='Output format (default: text)')
    pr_stats.set_defaults(func=cmd_stats_proposals)

    # proposal duplicate
    pr_dup = prop_sub.add_parser('duplicate', help='Duplicate a proposal')
    pr_dup.add_argument('id', help='Source proposal ID')
    pr_dup.add_argument('--no-sync', action='store_true', help='Skip auto-sync to index')
    pr_dup.set_defaults(func=cmd_duplicate)

    # proposal migrate
    pr_migrate = prop_sub.add_parser('migrate', help='Migrate proposals between projects')
    pr_migrate.add_argument('--from-project', required=True, help='Source project ID')
    pr_migrate.add_argument('--to-project', required=True, help='Target project ID')
    pr_migrate.add_argument('--no-sync', action='store_true', help='Skip auto-sync to index')
    pr_migrate.set_defaults(func=cmd_migrate)

    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    if hasattr(args, 'func'):
        try:
            args.func(args)
        except ValueError as e:
            die(str(e))
        except Exception as e:
            die(f"Operation failed: {e}")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
