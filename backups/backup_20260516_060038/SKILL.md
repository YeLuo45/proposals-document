---
name: prj-proposals-manager
description: Manage proposal lifecycle from intake to delivery across coordinating agents or roles (Coordinator / PM / Dev / Test Expert / Research Analyst). Covers intake, clarification, PRD confirmation, technical review, test case generation, development handoff, acceptance, and delivery. Works with any agent platform (Cursor, Hermes, OpenClaw, etc.)
version: 2.5.0
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

### Branch Data Comparison (2026-05-15)
| Branch | projects | has prjUrl |
|--------|----------|------------|
| master | 45 | 37 |
| gh-pages | 45 | 37 |

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

## CSV Schema (Source of Truth)

### projects.csv
```
id,name,proposal_count,git_repo,local_path,prj_url,description,last_update
PRJ-20260419-007,ai-creator-h5,3,https://github.com/owner/repo,/path/to/local,https://owner.github.io/ai-creator-h5,My project,2026-05-15
```
- `prj_url`: GitHub Pages deployment URL inferred from `git_repo` (e.g., `https://yeluo45.github.io/repo-name`). Only set for `github.com/YeLuo45/*` repos. Format: `https://yeluo45.github.io/{repo}` or `https://yeluo45.github.io/{repo}/` for repos requiring trailing slash.

### proposals.csv
```
id,title,owner,status,project_id,project_name,stage,prd_path,tech_solution_path,project_path,
git_repo,prj_url,deployment_branch,prd_confirmation,tech_expectations,acceptance,
research_direction,last_update,engine,target,game_type,notes
```
- `prj_url`: GitHub Pages deployment URL, same inference logic as projects.csv

### project_proposal_mapping.csv
```
project_id,project_name,project_git_repo,project_local_path,proposal_id,proposal_name,proposal_status
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

2. For design document projects (`*-design`), use direct `cp -r` + website patch workflow (bypass sync script)

### Step 1b: Register New Proposal from Scratch

1. Read `$PROPOSALS_ROOT/proposal-index.md` to determine next ID
2. Copy `$TEMPLATES_DIR/request-intake-template.md` to `$PROPOSALS_ROOT/P-YYYYMMDD-XXX.md`
3. Fill in basic info and original requirements
4. Add entry under Active Proposals in `proposal-index.md`, status = `intake`
5. Add entry for this proposal in `$PROPOSAL_DOCS_INDEX`
6. Create `$DEV_OUTPUT_DIR/<project-name>/proposals/docs/index.md` and write initial index structure

### Step 2: Clarify Requirements

- Ask up to 3 rounds of clarifying questions to the requester, focusing on: goals, scope, constraints, acceptance criteria
- Record each Q&A round in the Clarification section of the proposal file
- After 3 rounds or when requirements are clear, record final assumptions
- Update status to `clarifying`

### Step 3: Transfer to PM

If the requirement is just an idea or rough draft, transfer to PM role to generate PRD.

- PM saves PRD to `$PM_OUTPUT_DIR/<project-name>/YYYY-MM-DD-prd.md`
- PM also copies PRD to `$DEV_OUTPUT_DIR/<project-name>/proposals/docs/prd.v1.md`
- After PM delivery, update PRD Path in `proposal-index.md`

### Step 4: PRD Confirmation Gate

After PM returns PRD:

1. Show PRD to requester and request confirmation
2. Start confirmation countdown (recommended: 5 minutes)
3. Record countdown reference in "PRD Confirmation Countdown ID"

If confirmed: Set PRD Confirmation to `confirmed`, cancel countdown, immediately update status to `approved_for_dev` and start development.

If timeout: Set PRD Confirmation to `timeout-approved`, record in "Timeout Resolution", immediately update status to `approved_for_dev` and start development.

### Step 5: Technical Expectations Gate

Before outputting technical solution:

1. Understand from requester: tech stack, performance, cost, deployment method, maintainability, dependency constraints
2. Up to 3 rounds of questions
3. Start confirmation countdown (same mechanism as Step 4)
4. Record in "Technical Expectations Countdown ID"

If confirmed: Set Technical Expectations to `confirmed`, immediately write technical solution and update status to `approved_for_dev`.

If timeout: Set Technical Expectations to `timeout-approved`, proceed with current assumptions, immediately write technical solution and update status to `approved_for_dev`.

### Step 6: Technical Solution

- Output technical solution to `$PROPOSALS_ROOT/P-YYYYMMDD-XXX-tech-solution.md`
- Also copy to `$DEV_OUTPUT_DIR/<project-name>/proposals/docs/technical-solution.v1.md`
- Update status to `approved_for_dev`

### Step 6b: TDD Test Case Generation

After technical solution output, transfer to Test Expert to generate test cases based on TDD principles:

1. Coordinator transfers task to Test Expert with: PRD document, technical solution document, project background

2. Test Expert outputs test cases to `$TEST_OUTPUT_DIR/<project-name>/YYYY-MM-DD-test-cases.md`
   - Test cases must be traceable to PRD requirements
   - Include: test case ID, description, preconditions, steps, expected results
   - Cover normal paths and edge cases
   - Copy test cases to `$DEV_OUTPUT_DIR/<project-name>/proposals/docs/test-cases.v1.md`

3. Update tracking: Update Test Cases Path in `proposal-index.md`, update status to `in_tdd_test`

### Step 7: Handoff to Development

- Update status to `in_dev`
- If directory doesn't exist, Dev creates `$DEV_OUTPUT_DIR/<project-name>/proposals/docs/`
- Dev saves project output to `$DEV_OUTPUT_DIR/<project-name>/proposals/`
- Update Project Path in `proposal-index.md`

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

Functional verification (must实际操作, not just screenshots):
- Core functionality works end-to-end
- No Error in console/logs (warnings OK)
- Existing functionality not broken
- Build succeeds

Update status to `in_test_acceptance` during acceptance.

If all test cases pass: Proceed to Step 9 (deliver)

If any test case fails: Update status to `test_failed`, output structured revision feedback.

### Step 9: Deliver or Revise

If all test cases pass: Update status to `accepted`, proceed to Step 10 (research direction)

If acceptance failed: Update status to `needs_revision`, output structured revision feedback.

### Step 10: Research Direction (Post-Acceptance Iteration Planning)

After acceptance passes (status becomes `accepted` or `delivered`):

1. Coordinator asks requester: "Based on this delivery, do you want to explore the next iteration direction, or maintain the current version first?"
2. Start 5-minute confirmation countdown, create cron job
3. Record countdown reference in "Research Direction Countdown ID"

If requester confirms direction: Set Research Direction to `confirmed`, immediately transfer task to PM to generate next iteration PRD.

If timeout: Set Research Direction to `timeout-approved`, Coordinator decides autonomously, immediately transfer task to PM to generate next iteration PRD.

### Step 11: Deploy (Post-Acceptance Delivery)

After acceptance (status becomes `accepted`):

1. Determine deployment target: GitHub Pages or Cloudflare Pages
2. Create deployment branch
3. Prepare deployment (ensure package-lock.json is committed, run `npm run build`)
4. Push to remote
5. Trigger deployment
6. Verify deployment
7. Update proposal: Set status to `deployed`, record Deployment URL and Deployment Branch
8. Sync to proposals-manager website + hermes-agent

### Step 12: Website Rebuild

- Use `proposal-sync-website` skill to update `data/proposals.json` in YeLuo45/prj-proposals-manager
- After sync, rebuild website: Download updated `proposals.json` from GitHub API to `public/data/proposals.json`, then `npm run build` and gh-pages deploy

## Development Delivery Quality Checks

Three hard指标的 must be verified before acceptance:

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

## Confusion: Proposal System ≠ GitHub Repositories

**The proposal system contains a curated subset of projects — it does NOT auto-sync all GitHub repositories.**

- `projects.csv` has 45 projects (curated subset)
- GitHub has 60+ `*-design` repos that are NOT in the proposal system
- Adding a GitHub repo does NOT automatically add it to the proposal system
- To add a project: use `proposal_manager_cli.py project add --name "..." --git-repo "..."`

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
    --prd-path "workspace-pm/my-project/proposals/docs/prd.v1.md" \
    --deployment-url "https://owner.github.io/my-project" \
    --notes "Fixed critical bug"

# Update project fields
python3 scripts/proposal_manager_cli.py project update <id> \
    --name "New Name" \
    --git-repo "https://github.com/owner/new-repo"
```

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
| references/data-model.md | CSV structure and field validation |
| references/data-recovery.md | Recovering from data corruption |
| references/data-structure-gotchas.md | CSV-JSON field alignment + frontend field name debugging |
| references/website-sync.md | GitHub sync architecture |
| references/sync-script-pitfalls.md | Sync script known issues |
| references/vite-cache-issue.md | Vite build cache issue |
