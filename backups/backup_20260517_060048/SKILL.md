---
name: prj-proposals-manager
description: Manage proposal lifecycle from intake to delivery across coordinating agents or roles (Coordinator / PM / Dev / Test Expert / Research Analyst). Covers intake, clarification, PRD confirmation, technical review, test case generation, development handoff, acceptance, and delivery. Works with any agent platform (Cursor, Hermes, OpenClaw, etc.)
version: 3.1.0
author: YeLuo45
license: MIT
metadata:
  hermes:
    tags: [proposal, workflow, lifecycle, project-management, coordinator, pm, dev, test, research]
    homepage: https://yeluo45.github.io/prj-proposals-manager/
    related_skills: [harness-desktop-iteration-workflow, dbg-card-game-workflow, pixel-pal-web-workflow]
---

# Proposal Management

A platform-agnostic skill for managing proposal lifecycles across multi-role workflows (Coordinator / PM / Dev / Test Expert / Research Analyst). Covers intake, clarification, PRD confirmation, technical review, test case generation, development handoff, acceptance, and delivery.

## Architecture: CSV as Source of Truth

```
+------------------+       +---------------------+       +------------------+
|   CSV Files      | <--> |  proposal_manager   | -->   |  Markdown Files  |
| (source of truth)|       |  _cli.py            |       | (derived)        |
+------------------+       +---------------------+       +------------------+
        |                                                       |
        v                                                       v
+------------------+                                   +------------------+
|  Local CSVs      |                                   |  GitHub JSON     |
|  (not on GitHub) | <------- pull-proposals -------- |  (proposals.json)|
+------------------+       (GitHub is JSON format)    +------------------+
                                    ^
                                    |
                          +------------------+
                          |  sync-proposals  |
                          |  -to-website.py  |
                          +------------------+
                          (CSV -> JSON push)
```

**Data Flow:**
1. All changes are made via `proposal_manager_cli.py` (writes to CSV)
2. CSV files are the **sole source of truth**
3. `sync-proposals-to-website.py` reads CSV and pushes to GitHub (pushes to `gh-pages` branch)
4. LLM generates/updates markdown files (`proposal-index.md`, `proposal-docs-index.md`, `project-index.md`) from CSV content

## CRITICAL: GitHub Pages Serves from gh-pages Branch

**The website `https://yeluo45.github.io/prj-proposals-manager/` reads from the `gh-pages` branch, NOT `master`.**

- `sync-proposals-to-website.py` pushes to `gh-pages` branch by default
- The `master` branch may have different content (used for development/source)
- After running sync, always verify via `curl https://yeluo45.github.io/prj-proposals-manager/data/proposals.json` or `curl https://raw.githubusercontent.com/YeLuo45/prj-proposals-manager/gh-pages/data/proposals.json`
- The raw GitHub API (`api.github.com`) defaults to `master` branch — use `?ref=gh-pages` to target the deployed branch

## Quick Start

```bash
# Initialize (first-time use)
python3 scripts/init_proposals_dir.py

# Create a project (with local workspace initialization)
python3 scripts/proposal_manager_cli.py project add --name "ProjectName" --git-repo "https://github.com/owner/repo" --init-workspace

# Create a proposal (local project path auto-determined)
python3 scripts/proposal_manager_cli.py proposal add --title "ProposalTitle" --project-id PRJ-YYYYMMDD-XXX

# Update proposal fields
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --status in_dev
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --deployment-url "https://..."

# Update project fields
python3 scripts/proposal_manager_cli.py project update PRJ-YYYYMMDD-XXX --name "NewName"

# View status
python3 scripts/proposal_manager_cli.py proposal list --fields id,title,status,project_name
python3 scripts/proposal_manager_cli.py project list --fields id,name,proposal_count

# Sync to website (CSV -> GitHub)
GITHUB_TOKEN=$GITHUB_TOKEN python3 scripts/sync-proposals-to-website.py

# Backup
bash scripts/backup_proposals.sh
```

## Operation Modes

### Default Mode (Interactive)

When user confirmation is required, present options A/B/C/D and wait for single-letter response:
- Options presented in brackets: `[A] Option A  [B] Option B  [C] Option C  [D] Continue`
- User responds with single letter (case-insensitive)
- Timeouts trigger the first option as default

### Unattended Mode (Fully Automated)

For continuous iteration without user present. Enabled when requester/boss specifies "unattended" or "auto" when initiating a proposal.

**How to Enter:**
- Boss/Requester declares intent: "I want to run this in unattended mode" or "--unattended" when submitting proposal
- Recorded in proposal's `notes` field as `mode: unattended`
- Once entered, all subsequent iterations for this project remain in unattended mode automatically

**Characteristics:**
- Creates a 5-minute countdown cron job when iteration options are presented
- Auto-selects first option (A) when cron fires if no user response
- Never stalls on confirmation gates
- Unattended mode persists across iterations — once set, stays set for this project

**Propagation:**
- When a new iteration proposal is created under an unattended-mode project, it inherits unattended mode
- Unattended mode is NOT cleared on delivery — it continues until boss explicitly exits

**When triggered:**
- On delivery: Presents A/B/C/D options briefly (10 seconds for boss to override), then auto-selects A via cron — **no waiting for user input**
- On PRD/tech expectations confirmation: Auto-approves and proceeds after 5-minute timeout
- On iteration completion: **Immediately begin next iteration with direction A** — do NOT block waiting for confirmation
- Never asks clarifying questions in unattended mode

**CRITICAL — iteration completion triggers next iteration immediately:**
```python
# When a proposal is marked "delivered" in unattended mode:
# 1. Present direction options (A/B/C/D) briefly
# 2. Immediately proceed with direction A (do NOT wait for response)
# 3. Create next proposal PRD + tech-solution
# 4. Implement + commit (even if push is blocked)
# 5. Present next round of options
# Loop until boss explicitly says "stop" or "exit unattended mode"
```

**Why this matters**: Unattended mode is for **continuous iteration** — the point is to keep working without stalls. If push is blocked by network, the code is still committed locally. When network recovers, push resumes. The key is: never pause the iteration loop waiting for user input when in unattended mode.

**Critical — unattended means IMMEDIATE auto-selection:**
- On delivery, the 5 options (A-E) are informational (boss can override by saying B/C/D/E)
- If boss responds with a single letter (A/B/C/D/E), treat as direction confirmation and continue
- The cron job auto-selects A only if boss has not responded after 5 minutes
- **Do NOT wait for boss to confirm before starting next iteration** — if unattended mode is active, immediately begin the next iteration with direction A after delivering the current one

**Implementation — Unattended Auto-Select:**
```python
# Instead of waiting for user input, create countdown cron:
cronjob(action='create', name=f"unattended-{proposal_id}", 
        prompt=f"Auto-select iteration direction A for P-{proposal_id}", 
        schedule='5m', 
        deliver='local')
# Immediately proceed with direction A — don't wait
```

**Usage:**
```bash
# Boss declares when initiating proposal
"我要无人值守模式跑这个项目" or "run in unattended mode"

# Recorded in proposal notes field:
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --notes "mode: unattended"
```

## CSV Schema (Source of Truth)

### projects.csv — 8-Field Structure (STRICT)
```
id,name,proposal_count,git_repo,local_path,prj_url,description,last_update
PRJ-20260516-001,my-project,3,https://github.com/YeLuo45/repo,,https://yeluo45.github.io/repo/,My project,2026-05-16
```
- `id` MUST be `PRJ-YYYYMMDD-NNN` — never bare repo names. Non-compliant IDs must be renumbered on correction day.
- `local_path` MUST be empty or a filesystem path — NEVER a URL. Use `prj_url` for GitHub Pages URLs.
- `prj_url`: Deployment URL — GitHub Pages, Cloudflare Pages, Netlify, or other hosting platforms. Format varies: `https://yeluo45.github.io/{repo}/` for GitHub Pages, or direct domain for Cloudflare/Netlify. Only set for YeLuo45/* repos with deployment enabled.

proposals.csv — 20-Field Structure (STRICT)
```
id,title,owner,status,project_id,project_name,stage,prd_path,tech_solution_path,project_path,deployment_branch,prd_confirmation,tech_expectations,acceptance,research_direction,last_update,engine,target,game_type,notes
P-20260505-001,PRD: Monopoly3D 核心体验打磨,,active,PRJ-20260412-009,Monopoly3D,intake,workspace-pm/proposals/PRJ-20260412-009/P-20260505-001-prd.md,,/home/hermes/workspace-dev/proposals/monopoly3d,gh-pages,,,,,,2026-05-05,,,,
```

### project_proposal_mapping.csv
```
project_id,project_name,proposal_id,proposal_name
```

## Workflow: Proposal Lifecycle

```
Step 1a/1b: Intake -- Register proposal (from existing codebase or new)
Step 2: Clarify -- Up to 3 rounds
Step 3: Transfer to PM if needed
Step 4: PRD confirmation gate
Step 5: Technical expectations gate (up to 3 rounds)
Step 6: Output technical solution
Step 6b: Handoff to Test Expert -- Generate TDD test cases
Step 7: Handoff to Dev (with test cases as reference)
Step 8: Test Expert acceptance based on test cases
Step 9: Deliver or revise
Step 10: Research direction (post-acceptance iteration planning)
Step 11: Deploy (post-acceptance delivery)
Step 12: Website rebuild
```

### Step 1a: Register from Existing Codebase

When the requirement is to clone an existing GitHub repo and register as proposal (vs building from scratch):

1. Clone repo to `$DEV_OUTPUT_DIR/<project-name>/proposals/` or copy locally

2. For design document projects (`*-design`), follow Step 1b as normal proposal

### Step 1b: Register New Proposal from Scratch

1. Use `proposal_manager_cli.py` to determine next PRJ_ID and P-ID:
   ```bash
   # Generate next project ID
   python3 scripts/proposal_manager_cli.py project next-id

   # Generate next proposal ID for a project
   python3 scripts/proposal_manager_cli.py proposal next-id PRJ-YYYYMMDD-XXX
   ```
2. Create a feature branch for this proposal (if project has remote repo):
   ```bash
   cd $DEV_PROPOSALS/<project-name>
   git checkout -b feature/P-YYYYMMDD-XXX
   ```
3. Copy `$TEMPLATES_DIR/request-intake-template.md` to `$PM_PROPOSALS/PRJ-YYYYMMDD-XXX/P-YYYYMMDD-XXX.md`
4. Fill in basic info and original requirements
5. Add entry for this project in `$PROJECTS_CSV` (projects.csv)
6. Add entry for this proposal in `$PROPOSAL_DOCS_INDEX`
7. Create project directory structure:
   ```bash
   mkdir -p $DEV_PROPOSALS/<project-name>/docs
   mkdir -p $PM_PROPOSALS/PRJ-YYYYMMDD-XXX
   ```

### Step 2: Clarify Requirements

- Ask up to 3 rounds of clarifying questions to the requester, focusing on: goals, scope, constraints, acceptance criteria
- Record each Q&A round in the Clarification section of the proposal file
- After 3 rounds or when requirements are clear, record final assumptions
- Update status to `clarifying`:
  ```bash
  python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --status clarifying
  ```

### Step 3: Transfer to PM

If the requirement is just an idea or rough draft, transfer to PM role to generate PRD.

- PM saves PRD to `$PM_PROPOSALS/PRJ-YYYYMMDD-XXX/YYYY-MM-DD-prd.md`
- PM also copies PRD to `$DEV_PROPOSALS/<project-name>/docs/prd.v1.md`
- Update PRD Path in proposals.csv:
  ```bash
  python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --prd-path "$PM_PROPOSALS/PRJ-YYYYMMDD-XXX/YYYY-MM-DD-prd.md"
  ```

### Step 4: PRD Confirmation Gate

After PM returns PRD:

1. Show PRD to requester and request confirmation
2. Start confirmation countdown (recommended: 5 minutes)
3. Record countdown reference in "PRD Confirmation Countdown ID"

If confirmed: Set PRD Confirmation to `confirmed`, cancel countdown, immediately update status to `approved_for_dev` and start development.
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --prd-confirmation confirmed --status approved_for_dev
```

If timeout: Set PRD Confirmation to `timeout-approved`, record in "Timeout Resolution", immediately update status to `approved_for_dev` and start development.
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --prd-confirmation timeout-approved --status approved_for_dev
```

### Step 5: Technical Expectations Gate

Before outputting technical solution:

1. Understand from requester: tech stack, performance, cost, deployment method, maintainability, dependency constraints
2. Up to 3 rounds of questions
3. Start confirmation countdown (same mechanism as Step 4)
4. Record in "Technical Expectations Countdown ID"

If confirmed: Set Technical Expectations to `confirmed`, immediately write technical solution and update status to `approved_for_dev`.
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --tech-expectations confirmed --status approved_for_dev
```

If timeout: Set Technical Expectations to `timeout-approved`, proceed with current assumptions, immediately write technical solution and update status to `approved_for_dev`.
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --tech-expectations timeout-approved --status approved_for_dev
```

### Step 6: Technical Solution

- Output technical solution to `$PROPOSALS_ROOT/P-YYYYMMDD-XXX-tech-solution.md`
- Also copy to `$DEV_PROPOSALS/<project-name>/docs/technical-solution.v1.md`
- Update tech_solution_path and status:
  ```bash
  python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --tech-solution-path "$PROPOSALS_ROOT/P-YYYYMMDD-XXX-tech-solution.md" --status approved_for_dev
  ```

### Step 6b: TDD Test Case Generation

After technical solution output, transfer to Test Expert to generate test cases based on TDD principles:

1. Coordinator transfers task to Test Expert with: PRD document, technical solution document, project background

2. Test Expert outputs test cases to `$TEST_OUTPUT_DIR/<project-name>/YYYY-MM-DD-test-cases.md`
   - Test cases must be traceable to PRD requirements
   - Include: test case ID, description, preconditions, steps, expected results
   - Cover normal paths and edge cases
   - Copy test cases to `$DEV_OUTPUT_DIR/<project-name>/proposals/docs/test-cases.v1.md`

3. Update tracking: Update Test Cases Path and status:
  ```bash
  python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --test-cases-path "$TEST_PROPOSALS/<project-name>/YYYY-MM-DD-test-cases.md" --status in_tdd_test
  ```

### Step 7: Handoff to Development

- Update status to `in_dev`:
  ```bash
  python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --status in_dev
  ```
- Update project_path:
  ```bash
  python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --project-path "$DEV_PROPOSALS/<project-name>"
  ```
- If directory doesn't exist, Dev creates `$DEV_PROPOSALS/<project-name>/docs/`

### Step 8: Test Expert Acceptance (Based on TDD)

After Dev reports completion, Test Expert executes acceptance based on test cases:

Requirements consistency:
- Conforms to confirmed requirements from requester
- Aligned with PRD
- No scope creep or cut corners

Test case execution:
- Execute each test case in `test-cases.vN.md`
- Record pass/fail status for each test case
- Record any deviations or failures

Functional verification (must actually operate, not just screenshots):
- Core functionality works end-to-end
- No Error in console/logs (warnings OK)
- Existing functionality not broken
- Build succeeds

Update status to `in_test_acceptance` during acceptance.
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --status in_test_acceptance
```

If all test cases pass: Proceed to Step 9 (deliver)

If any test case fails: Update status to `test_failed`, output structured revision feedback.
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --status test_failed
```

### Step 9: Deliver or Revise

If all test cases pass: Update status to `accepted`, proceed to Step 10 (research direction).
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --status accepted
```

If acceptance failed: Update status to `needs_revision`, output structured revision feedback.
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --status needs_revision
```

### Step 10: Research Direction (Post-Acceptance Iteration Planning)

After acceptance passes (status becomes `accepted` or `delivered`):

1. Coordinator asks requester: "Based on this delivery, do you want to explore the next iteration direction, or maintain the current version first?"
2. Start 5-minute confirmation countdown, create cron job
3. Record countdown reference in "Research Direction Countdown ID"

If confirmed: Set Research Direction to `confirmed`, immediately transfer task to PM to generate next iteration PRD.
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --research-direction confirmed
```

If timeout: Set Research Direction to `timeout-approved`, Coordinator decides autonomously, immediately transfer task to PM to generate next iteration PRD.
```bash
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --research-direction timeout-approved
```

### Step 11: Deploy (Post-Acceptance Delivery)

After acceptance (status becomes `accepted`):

1. Determine deployment target: GitHub Pages or Cloudflare Pages
2. Create deployment branch
3. Prepare deployment (ensure package-lock.json is committed, run `npm run build`)
4. Push to remote
5. Trigger deployment
6. Verify deployment
7. Update proposal: Set status to `deployed`, record Deployment URL and Deployment Branch:
   ```bash
   python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --status deployed --deployment-url "https://..." --deployment-branch gh-pages
   ```
8. Sync to proposals-manager website + hermes-agent

### Step 12: Website Rebuild

- Use `proposal-sync-website` skill to update `data/proposals.json` in YeLuo45/prj-proposals-manager
- After sync, rebuild website: Download updated `proposals.json` from GitHub API to `public/data/proposals.json`, then `npm run build` and gh-pages deploy

## Development Delivery Quality Checks

Three hard criteria must be verified before acceptance:

1. Build exit code: Must be 0
2. Output directory non-empty: List core files to confirm
3. Core source/service files exist: Verify key files exist

### Takeover Trigger Conditions

Coordinator should take over directly from Dev when any condition is met:
- Dev delivers unqualified 2 consecutive times
- Dev session interrupted by API/quota error
- Dev session abnormally short (<30s) yet claims completion
- Fix method is simple and clear

### Fix Record

When Coordinator directly fixes issues, record to:
1. Project memory file (e.g., `MEMORY.md`) relevant sections
2. Daily log (e.g., `memory/YYYY-MM-DD.md`)
3. Proposal's Notes or Main Fixes Applied fields

## Index Entry Template

When adding to `proposal-index.md`:

### P-YYYYMMDD-XXX: <Title>

- Proposal ID: P-YYYYMMDD-XXX
- Title: <Title>
- Owner: <Coordinator>
- Current Status: <Status>
- PRD Path: (filled by PM)
- Technical Solution: (to be filled)
- Test Cases Path: (filled by Test Expert)
- Project Path: (filled by Dev)
- Acceptance: -
- PRD Confirmation: pending
- PRD Confirmation Countdown ID: -
- Technical Expectations: pending
- Technical Expectations Countdown ID: -
- Research Direction: pending
- Research Direction Countdown ID: -
- Deployment URL: (filled after deploy)
- Deployment Branch: (filled after deploy)
- Last Update: YYYY-MM-DD
- Notes:

## Scripts

| Script | Purpose |
|--------|---------|
| init_proposals_dir.py | Initialize/repair proposals directory structure |
| proposal_manager_cli.py | CRUD for projects and proposals (ALL CSV operations go through here) |
| edit_proposal.py | Legacy field editor for markdown+CSV (use cli.py for new work) |
| sync-proposals-to-website.py | Read CSV, push to GitHub, generate website JSON |
| pull-proposals-from-github.py | Pull GitHub proposals.json and convert to local CSV |
| backup_proposals.sh | Backup all proposal system data |
| rollback_proposals.sh | Rollback: full system, per-project, or per-proposal from backups |
| sync-pm-to-dev.py | Sync accepted PRD/tech/test files from workspace-pm to workspace-dev |
| generate-spec.py | Generate OpenSpec SPEC — from proposal (`<project_id>`) or init for existing project (`--init <project_name>`, `--init --all`) |

## Backup and Rollback

### Backup

```bash
# Create backup (keeps last 10 backups)
bash scripts/backup_proposals.sh

# Backup is stored in: ~/.hermes/proposals/backups/
```

### Rollback

```bash
# List available backups
bash scripts/rollback_proposals.sh list

# Verify backup integrity
bash scripts/rollback_proposals.sh verify proposals_backup_YYYYMMDD_HHMMSS.tar.gz

# Full system rollback (to latest backup)
bash scripts/rollback_proposals.sh full

# Full system rollback to specific backup (N=1 is latest, N=2 is second-latest)
bash scripts/rollback_proposals.sh full 3

# Rollback specific project
bash scripts/rollback_proposals.sh project PRJ-YYYYMMDD-XXX

# Rollback specific proposal
bash scripts/rollback_proposals.sh proposal P-YYYYMMDD-XXX
```

### Rollback Behavior

| Command | Data Restored |
|---------|--------------|
| `full N` | All CSV + markdown files from backup N |
| `project <id> N` | projects.csv entry + related proposals + mapping |
| `proposal <id> N` | Single proposal in proposals.csv + mapping |

**Safety:**
- Before full rollback: creates emergency backup of current state
- Before proposal/project rollback: creates emergency backup
- All operations require `yes` confirmation

## CSV Field Fillability Analysis

proposals.csv has 20 fields (22 → 20 after removing git_repo/prj_url on 2026-05-16). Not all are equal — knowing what CAN vs CANNOT be back-filled from .md files is critical:

| Field | Source | Can Back-Fill? |
|-------|--------|----------------|
| `title` | .md `# 标题` or filename | ✅ Yes — 148/211 filled |
| `owner` | .md content (owner/负责人) | ❌ No — .md files didn't include this |
| `stage` | .md content (stage/阶段) | ⚠️ Partial — 13/211 (only a few .md had this) |
| `last_update` | .md git log or file mtime | ✅ Yes — 148/211 (172 untracked by git → file mtime fallback) |
| `prd_path`, `tech_solution_path`, `project_path` | Project dir structure | ⚠️ Partial — needs path inference |
| `deployment_branch` | Workflow field | ⚠️ From projects.csv join (gh-pages default) |
| `prd_confirmation`, `tech_expectations`, `acceptance`, `research_direction`, `engine`, `target`, `game_type`, `notes` | Workflow fields | ❌ No — human-filled workflow state |

**Why most fields are empty:** `sync-proposals-to-website.py` reads from GitHub's `proposals.json` (source: YeLuo45's personal access token API), which only contains core fields (id, project_id, etc.). Extended fields exist only in local `.md` files under `workspace-pm/proposals/`. On 2026-05-16, `git_repo` and `prj_url` were removed from proposals.csv because they already exist in `projects.csv` (see `references/proposals-csv-schema-change-log.md`).

**Back-filling workflow:**
1. Loose `.md` files (344 files at `workspace-pm/proposals/` root, not in project subdirs) are the primary content source
2. Match loose `.md` to CSV rows by extracting `P-YYYYMMDD-NNN` prefix from filename
3. For `last_update`: try `git log --format=%ai` first; if file is untracked, use `os.path.getmtime()` as fallback
4. Write ALL 22 fields explicitly — omitting `last_update` in fieldnames list causes it to be dropped

**IMPORTANT — execute_code DictWriter drops fields:**
When using Python `csv.DictWriter(f, fieldnames=ALL_FIELDS)` after loading with `csv.DictReader`, the written CSV will only include the exact `fieldnames` specified. If `last_update` is in the data but not in `fieldnames`, it silently disappears. Always list all 20 fields explicitly.

**`git log` returns empty on untracked files:**
The `workspace-pm/proposals/` directory has 172+ `.md` files that are NOT tracked by git. Running `git log --format=%ai -- <file>` on these returns nothing. Always fallback to `os.path.getmtime()` for `last_update` on untracked files. The pattern:
```python
r = subprocess.run(['git', 'log', '-1', '--format=%ai', '--', fpath], capture_output=True, ...)
if r.returncode == 0 and r.stdout.strip():
    last_update = r.stdout.strip()[:10]
else:
    last_update = datetime.fromtimestamp(os.path.getmtime(fpath)).strftime('%Y-%m-%d')
```

## Configuration

| Variable | Value | Description |
|----------|-------|-------------|
| PROPOSALS_ROOT | ~/.hermes/proposals | Directory holding CSV and markdown files |
| DEV_OUTPUT_DIR | ~/.hermes/proposals/workspace-dev/<project>/proposals | Dev workspace |
| PM_OUTPUT_DIR | ~/.hermes/proposals/workspace-pm/<project>/proposals | PM workspace |
| TEST_OUTPUT_DIR | ~/.hermes/proposals/workspace-test/<project>/proposals | Test workspace |
| RESEARCH_OUTPUT_DIR | ~/.hermes/proposals/workspace-research/<project>/proposals | Research workspace |

## Data Rules

1. **CSV is the source of truth** - All changes MUST go through `proposal_manager_cli.py`
2. **Markdown files are derived** - Generated/updated by LLM from CSV content
3. **GitHub remote is JSON, NOT CSV** - Remote `data/` has `proposals.json`, `todos.json`, `milestones.json`. CSV files do NOT exist on GitHub and were never successfully pushed there.
4. **Recovery from GitHub** - Use `pull-proposals-from-github.py` to pull from `proposals.json` (GitHub's canonical format) and convert to local CSV. For historical recovery, check GitHub commit history (e.g., `?path=data/proposals.json&since=YYYY-MM-DD`) to find specific versions.
5. **CSV duplicate column prevention** - When reading CSV and rewriting (e.g., in sync script), always explicitly deduplicate columns. Duplicate `prj_url` columns corrupt the CSV. See `references/data-model.md#duplicate-columns`.
6. **projects.csv `local_path` field may contain URLs** - Historical entries have `local_path` = `https://yeluo45.github.io/{repo}` instead of filesystem paths. The `prj_url` field (added 2026-05-15) is correct for GitHub Pages URLs. Always preserve 8-field structure: `id,name,proposal_count,git_repo,local_path,prj_url,description,last_update`.
7. **PrjUrl inference: .git suffix must be stripped** - If `git_repo` ends with `.git`, remove it before inferring `prj_url`.
8. **prjId format is PRJ-YYYYMMDD-NNN** — Non-compliant IDs (bare repo names like `hermes-agent-design`, `cultivation-simulator`, `github-repo-manager`) must be renumbered. The correct format is `PRJ-YYYYMMDD-NNN` where NNN starts at 001 per day. After any manual CSV edit that changes project IDs, regenerate proposals.json and re-sync via sync script — never leave CSV and JSON out of sync.
    - **Renumbering procedure**: Generate new IDs using next available sequence for the creation date (e.g., if `PRJ-20260515-013` is the highest on 2026-05-15, use `PRJ-20260516-001` onwards). Update `projects.csv` id column and all `proposals.csv` `project_id` references. Re-sync.
9. **All 69 projects (as of 2026-05-16) have local_path filled** — Symlinks in `workspace-dev/proposals/` point to real development directories. Projects with no local clone have `local_path` pointing to `workspace-dev/proposals/{repo}` (the real dir exists there even if no explicit symlink was created).
10. **workspace-dev/proposals is the canonical local path root** — Symlinks in `/home/hermes/.hermes/proposals/workspace-dev/proposals/` point to actual project directories. Source locations searched (in order):
1. `/home/hermes/.hermes/proposals/workspace-dev/proposals/{repo}` — already symlinked
2. `/home/hermes/workspace-dev/proposals/{repo}` — development workspace (many untracked dirs live here)
3. `/home/hermes/{repo}` — direct project directories (e.g., `harness-desktop`, `monopoly3d`)
4. `/home/hermes/opensource/{repo}` — especially for `*-design` VitePress doc sites
5. `/home/hermes/projects/{repo}` — additional projects
    - `/home/hermes/projects/{repo}` — additional projects
    **NOTE**: The correct path is `workspace-dev/`, NOT `workplace-dev/` (this was a persistent typo corrected 2026-05-16).

### workspace-pm/proposals Has TWO Kinds of Content

The `workspace-pm/proposals/` directory is NOT purely a tree of project subdirs — it contains BOTH:

1. **Project subdirs** (13 dirs as of 2026-05-16): e.g., `PRJ-20250416-001/`, `ai-stock-simulation/`, `snake-battle/`
   - These hold properly organized `.md` files per project
   
2. **Loose `.md` files at root** (346 files as of 2026-05-16): e.g., `P-20260505-001-prd.md`, `P-20260505-002-prd.md`
   - These are NOT in project subdirs
   - They ARE indexed by `proposal-docs-index.md` and proposals.csv
   - When back-filling CSV from .md files, scan BOTH locations

```python
# CORRECT: scan both locations
base = 'workspace-pm/proposals'
loose_files = [f for f in os.listdir(base) if f.endswith('.md') and f.startswith('P-')]
subdir_files = []
for d in os.listdir(base):
    if os.path.isdir(os.path.join(base, d)):
        subdir_files += [os.path.join(d, f) for f in os.listdir(os.path.join(base, d)) if f.endswith('.md')]
```

Always create symlinks here, don't reference raw `/home/hermes/{repo}` paths in `local_path`.
    **NOTE**: The correct path is `workspace-dev/`, NOT `workplace-dev/` (this was a persistent typo corrected 2026-05-16).

## Proposal States

Use these exact names across all roles:

```
intake -> clarifying -> prd_pending_confirmation -> approved_for_dev -> in_tdd_test -> in_dev -> in_test_acceptance -> accepted -> deploying -> deployed
                                                                                   |                              |
                                                                         needs_revision -> in_dev              test_failed -> in_dev
```

## Workspace Initialization

When creating a project with `--init-workspace`, the script creates:

```
workspace-dev/<project>/proposals/
workspace-dev/<project>/proposals/docs/index.md

workspace-pm/<project>/proposals/
workspace-pm/<project>/proposals/docs/index.md

workspace-test/<project>/proposals/
workspace-test/<project>/proposals/docs/index.md

workspace-research/<project>/proposals/
workspace-research/<project>/proposals/docs/index.md
```

Each `docs/index.md` contains a version tracking table for Proposal, PRD, Technical Solution, and Test Cases.

## Field Editing via CLI

All CSV fields can be updated via `proposal_manager_cli.py`:

```bash
# Update proposal fields
python3 scripts/proposal_manager_cli.py proposal update <id> \
    --status in_dev \
    --title "PRD: Feature Name" \
    --owner boss \
    --project-id PRJ-20260516-001 \
    --stage intake \
    --prd-path "workspace-pm/proposals/PRJ-20260516-001/my-proposal-prd.md" \
    --tech-solution-path "workspace-pm/proposals/PRJ-20260516-001/my-proposal-tech.md" \
    --project-path "/home/hermes/workspace-dev/proposals/my-project" \
    --deployment-url "https://yeluo45.github.io/my-project/" \
    --deployment-branch gh-pages \
    --prd-confirmation confirmed \
    --tech-expectations confirmed \
    --acceptance passed \
    --research-direction "Expand to mobile" \
    --engine Unity \
    --target "iOS,Android" \
    --game-type RPG \
    --notes "Fixed critical bug"

# Update project fields
python3 scripts/proposal_manager_cli.py project update <id> \
    --name "New Name" \
    --git-repo "https://github.com/YeLuo45/new-repo" \
    --local-path "/home/hermes/workspace-dev/proposals/new-repo" \
    --description "Project description"
```

### Post-Acceptance: Sync PRD/Tech to Dev Workspace

After a proposal is accepted, PRD and technical solution files should be synced to the corresponding project in `workspace-dev/proposals/` so they are included when the project syncs to its remote repository:

```bash
python3 scripts/sync-pm-to-dev.py <project_id> [--dry-run]

# Examples
python3 scripts/sync-pm-to-dev.py PRJ-20260422-001          # sync ai-novel-assistant
python3 scripts/sync-pm-to-dev.py PRJ-20260516-001 --dry-run  # preview only
```

This copies PRD (files with `prd` in name), technical solution files, and test case/spec files from:
`workspace-pm/proposals/{project_id}/` → `workspace-dev/proposals/{project_name}/`

Test files are identified by keywords: `test`, `spec`, `test-case` in the filename.

### Post-Acceptance: Generate OpenSpec SPEC

After acceptance, generate OpenSpec-compliant SPEC files from the accepted proposal's PRD and technical solution:

```bash
python3 scripts/generate-spec.py <project_id> [--dry-run]

# Examples
python3 scripts/generate-spec.py PRJ-20260422-001          # generate SPEC for ai-novel-assistant
python3 scripts/generate-spec.py PRJ-20260516-001 --dry-run  # preview only
```

This reads PRD and tech-solution from `workspace-pm/proposals/{project_id}/` and generates:

```
workspace-dev/proposals/{project_name}/SPEC/
├── proposal.md        # Why/What/Capabilities/Impact (from PRD)
├── spec.md           # Requirements + GHERKIN scenarios
├── design.md         # Context/Goals/Decisions/Risks (from tech solution)
├── tasks.md          # Implementation checklist
└── .openspec.yaml    # Metadata (schema, project, created date)
```

OpenSpec reference: https://github.com/YeLuo45/OpenSpec (schemas/spec-driven/templates/)

### Initialize SPEC for Existing Projects

For projects without proposals (legacy projects), initialize OpenSpec SPEC from existing project files (README.md, existing SPEC.md):

```bash
# Initialize SPEC for a single project (by project name)
python3 scripts/generate-spec.py --init <project_name>
python3 scripts/generate-spec.py --init todolist                      # by project name
python3 scripts/generate-spec.py --init ai-stock-simulation --name "AlphaTrader"  # with display name

# Initialize SPEC for ALL projects without SPEC
python3 scripts/generate-spec.py --init --all
python3 scripts/generate-spec.py --init --all --dry-run               # preview only
```

This reads from:
- `workspace-dev/proposals/{project_name}/README.md` (project description, features, tech stack)
- `workspace-dev/proposals/{project_name}/SPEC.md` (if exists)
- Falls back to template content if no sources found

## Important Notes

### Path Discovery

Hermes environment:
- `~/.hermes/proposals/` is the actual proposals root -- not `~/proposals/`
- Primary index file is `proposal-docs-index.md` (not `proposal-index.md`)

OpenClaw environment (Windows/WSL):
- Proposals root: `~/.openclaw/workspace/proposals/`
- Primary index file is `proposal-index.md`
- PM output: `~/.openclaw/workspace-pm/proposals/`
- Dev output: `~/.openclaw/workspace-dev/proposals/`

### Critical: execute_code file write removes all line breaks

When writing back `proposal-index.md` via execute_code, the entire file becomes one line. Always backup before writing to `proposal-index.md`.

Safe approach:
1. Before writing back, `cp proposal-index.md proposal-index.md.bak`
2. Or write to `/tmp/` first, verify content, then overwrite
3. Never directly overwrite `proposal-index.md` in execute_code

### GITHUB_TOKEN Must Be Exported

When running sync/pull scripts that need GitHub authentication:
- **WRONG**: `GITHUB_TOKEN=$GITHUB_TOKEN python3 script.py` (subshell doesn't inherit)
- **CORRECT**: `export GITHUB_TOKEN=$(gh auth token) && python3 script.py`
- Or: `GITHUB_TOKEN=$(gh auth token) python3 script.py` (command substitution works inline)

### GitHub Actions Build Cache Pitfalls

**`cache: ''` DOES NOT disable caching** — it enables npm's own cache:

```yaml
# WRONG — this ENABLES npm cache
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: ''   # This is NOT empty; npm uses its own cache strategy
```

**Correct approach — truly disable caching:**

```yaml
# Option 1: explicitly use npm cache
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'

# Option 2: remove cache line entirely (no caching at all)
- uses: actions/setup-node@v4
  with:
    node-version: '20'
```

**Even with no explicit cache, Actions may reuse old node_modules/build artifacts.** If GitHub Pages shows stale JS after successful deploy:

1. Check deployed JS: `curl -s https://yeluo45.github.io/prj-proposals-manager/assets/index-*.js | tr ';' '\n' | grep -i "fe\.prjUrl"`
2. If JS is stale (shows `fe.githubPages||fe.url` instead of `fe.prjUrl||fe.githubPages||fe.url`):
   - Verify source code is correct: `curl -s https://raw.githubusercontent.com/YeLuo45/prj-proposals-manager/master/src/components/ProjectCard.jsx | grep prjUrl`
   - The Actions build is not recompiling — likely reusing cached build artifacts
3. **Recovery via REST API** (when `git push --force` is blocked):
   - Download correct file from a known-good commit: `curl -s https://raw.githubusercontent.com/YeLuo45/prj-proposals-manager/{good-sha}/src/components/ProjectCard.jsx -o /tmp/ProjectCard.jsx`
   - Get current SHA: `curl -s -X GET -H "Authorization: Bearer $GH_TOKEN" "https://api.github.com/repos/{owner}/{repo}/contents/src/components/ProjectCard.jsx"`
   - Push via REST API: `PUT /repos/{owner}/{repo}/contents/src/components/ProjectCard.jsx` with base64-encoded content and current SHA
   - This avoids needing `git push --force`

**NEVER push compiled JS assets to source files** — if you download a compiled `.js` from GitHub Pages and push it as `ProjectCard.jsx`, you corrupt the source with compiled code. Always keep source (`.jsx`, `.tsx`) and build (`dist/`) artifacts separate.

### WSL GitHub API Reliability

WSL network to GitHub API is unreliable (timeouts, 403, 409). Patterns that work:
- Direct `curl` with `--max-time 20` often succeeds where `gh api` times out
- Always get current SHA before PUT: `curl -s --max-time 20 -X GET "https://api.github.com/repos/.../contents/...?ref=gh-pages"`
- For large payloads (>100KB), `gh api` is more reliable than raw `curl`
- If PUT returns 409 Conflict, the SHA has changed — re-fetch SHA and retry
- Network may recover after 10-30s sleep; script logic should handle this

**Branch targeting for sync:**
- `sync-proposals-to-website.py` defaults to pushing `gh-pages` branch (GitHub Pages source)
- But if the script reports success without actually updating gh-pages, verify: `curl https://raw.githubusercontent.com/YeLuo45/prj-proposals-manager/gh-pages/data/proposals.json`
- If gh-pages is stale but master is updated, use REST API to manually sync: `PUT /repos/{owner}/{repo}/contents/data/proposals.json?ref=gh-pages` with correct SHA

### Handling Duplicate Cron Timeout Events

When processing cron timeout events:
1. First check `proposal-index.md` to see if status was already updated by a previous identical cron event
2. If PRD Confirmation or Technical Expectations already shows `timeout-approved`, do not update again
3. The same cron event may arrive multiple times; idempotency is critical
4. Also check `proposals.csv` -- proposal may be in `proposal-index.md` but not in CSV
5. **CRITICAL: Check actual field values, not just status** -- a cron may say "PRD确认超时" but `prd_confirmation` might already be `confirmed`. The cron prompt describes what was *intended* to timeout, but the data at cron-firing time controls what actually needs updating. Always compare the actual CSV field values against what the cron says should be updated.

**Confusing state pattern to watch for**: When `prd_confirmation=confirmed` but cron says "PRD确认超时", this means either:
- The cron was created with wrong parameters, OR
- The PRD was confirmed between cron creation and cron firing
In this case, the cron should still update status to `approved_for_dev` if not already done, but should NOT re-confirm fields that are already confirmed.

### CSV Duplicate Prevention

When adding new entries to `proposals.csv` via patch tool:
1. First verify ID doesn't exist
2. Use unique context for `old_string`
3. If accidentally created duplicate, immediately remove it

## Templates

This skill expects three templates in `$TEMPLATES_DIR/`:

| Template | Purpose |
|----------|---------|
| request-intake-template.md | Initial proposal registration, includes clarification fields and confirmation gates |
| proposal-status-template.md | Status tracking, includes associated resources, confirmation gates, and revision feedback |
| acceptance-checklist-template.md | Structured acceptance review, includes functionality/quality/delivery checklist |

## Known Issues

| Issue | Reference |
|-------|-----------|
| sync-proposals-to-website.py grouping logic trap | references/sync-script-pitfalls.md |
| references/vite-cache-issue.md | Vite build cache issue |
| references/bash-pitfalls.md | bash scripting pitfalls: `((var++))` with `set -e`, cp -r hangs, quote spacing |
| CSV structure corruption (execute_code/patch bypass CLI) | references/csv-structure-recovery.md |

## Critical: Website Frontend Field Names vs CSV Field Names

**The website UI (`ProjectCard.jsx`) reads specific JSON field names.**

| CSV field | JSON field | Website "访问" button reads |
|-----------|-----------|---------------------------|
| `prj_url` | `prjUrl` | `prjUrl` ✅ (primary) |
| `git_repo` | `gitRepo` | `gitRepo` ✅ (fallback for "访问", also used for "仓库" button) |
| `local_path` | `localPath` | `localPath` ✅ (used elsewhere) |

**How "访问" button works (after 2026-05-15 fix):**
```jsx
{(project.prjUrl || project.gitRepo) && (
  <button onClick={() => window.open(project.prjUrl || project.gitRepo, '_blank')}>
    访问
  </button>
)}
```
- **Primary**: `prjUrl` (GitHub Pages deployment URL)
- **Fallback**: `gitRepo` (GitHub repository URL)
- **"仓库" button**: always uses `gitRepo`

**Debug pattern — when JSON data is correct but UI doesn't show "访问":**
1. Check website source: `curl -s https://raw.githubusercontent.com/YeLuo45/prj-proposals-manager/master/src/components/ProjectCard.jsx | grep -n "prjUrl"`
2. Verify deployed JSON: `curl -s https://raw.githubusercontent.com/YeLuo45/prj-proposals-manager/gh-pages/data/proposals.json` (bypasses Pages CDN)
3. Fix ProjectCard.jsx, push to master, GitHub Actions auto-rebuilds
4. If rebuild didn't update dist/asset hash, manually trigger: `gh workflow run "Deploy to GitHub Pages"`

**GitHub Pages deployment is SLOW to update after sync:**
- Even after sync script succeeds, GitHub Pages CDN can take 1-2 minutes to reflect changes
- Always use `raw.githubusercontent.com` for immediate verification instead of `yeluo45.github.io`
- If raw.githubusercontent shows correct data but Pages doesn't, wait 60s and retry

**REST API push may corrupt JSON on large payloads (>100KB):**
- Always verify JSON validity locally: `python3 -c "import json; json.load(open('proposals.json'))"`
- If GitHub reports "Unterminated string" error, the JSON was corrupted during upload
- Retry the push — the file on GitHub may still be the old valid version
- For large files, prefer the sync script (`sync-proposals-to-website.py`) over raw REST API calls

## References

| Document | Description |
|----------|-------------|
| references/data-model.md | CSV structure, field validation, common data quality issues (historical `local_path` URL corruption, `.git` suffix, 8-field enforcement) |
| references/proposals-csv-schema-change-log.md | Schema evolution for proposals.csv (22→20 fields, git_repo/prj_url removed 2026-05-16) |
| references/csv-schema-change-log.md | Schema evolution for project_proposal_mapping.csv (7→4 fields) |
| references/local-path-population.md | How to populate `local_path` for projects — symlink strategy, source location search order, Python script |
| references/merge-proposals-dirs.md | Merging `/home/hermes/proposals` into `/home/hermes/.hermes/proposals` — procedure, what to merge vs symlink, post-merge sync |
| references/data-recovery.md | Recovering from data corruption |
| references/data-structure-gotchas.md | CSV-JSON field alignment + frontend field name debugging |
| references/website-sync.md | GitHub sync architecture |
| references/sync-script-pitfalls.md | Sync script known issues |
| references/vite-cache-issue.md | Vite build cache issue |
