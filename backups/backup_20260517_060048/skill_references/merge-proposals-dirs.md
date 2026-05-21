# Proposal Directory Merge Workflow

## Context

`/home/hermes/proposals` was an older location, while `/home/hermes/.hermes/proposals` is the canonical workspace (per `PROPOSALS_ROOT` config). On 2026-05-16, the older directory was merged into the canonical one then removed.

## Merge Procedure

```python
import os, shutil

src = '/home/hermes/proposals'
dst = '/home/hermes/.hermes/proposals'

# 1. Root .md files (skip proposal-index.md which already exists)
for f in os.listdir(src):
    if not f.endswith('.md') or f == 'proposal-index.md':
        continue
    src_path = f'{src}/{f}'
    dst_path = f'{dst}/{f}'
    if not os.path.exists(dst_path):
        shutil.copy2(src_path, dst_path)

# 2. workspace-pm/proposals (merge, skip dirs and existing files)
src_pm = f'{src}/workspace-pm/proposals'
dst_pm = f'{dst}/workspace-pm/proposals'
os.makedirs(dst_pm, exist_ok=True)
for f in os.listdir(src_pm):
    src_path = f'{src_pm}/{f}'
    if os.path.isdir(src_path):
        continue  # skip subdirs (e.g., "P19")
    dst_path = f'{dst_pm}/{f}'
    if not os.path.exists(dst_path):
        shutil.copy2(src_path, dst_path)

# 3. prj-proposals
src_prj = f'{src}/prj-proposals'
dst_prj = f'{dst}/prj-proposals'
os.makedirs(dst_prj, exist_ok=True)
for f in os.listdir(src_prj):
    if os.path.isdir(f'{src_prj}/{f}'):
        continue
    if not os.path.exists(f'{dst_prj}/{f}'):
        shutil.copy2(f'{src_prj}/{f}', f'{dst_prj}/{f}')

# 4. workspace-dev/proposals — symlink from canonical location
# (already done via local_path population; just verify)

# 5. Remove old directory
shutil.rmtree(src)
```

## What Gets Merged

| Location | What | Notes |
|----------|------|-------|
| Root `.md` | PRJ-YYYYMMDD-XXX.md files | Skip `proposal-index.md` (already canonical) |
| `workspace-pm/proposals/` | PRD and proposal markdown files | Skip subdirectories and existing files |
| `prj-proposals/` | Project-level documents | Merge new files only |
| `workspace-dev/proposals/` | Actual project directories | **Don't merge — use symlinks instead** (see local-path-population.md) |

## Verification

After merge:
```bash
# Check root md count (should be ~20)
ls /home/hermes/.hermes/proposals/*.md | wc -l

# Check workspace-pm count
ls /home/hermes/.hermes/proposals/workspace-pm/proposals/ | wc -l

# Verify old dir removed
ls /home/hermes/proposals  # should fail
```

## Post-Merge Sync

Always run sync after merge:
```bash
cd /home/hermes/.hermes/skills/prj-proposals-manager
GITHUB_TOKEN=$(gh auth token) python3 scripts/sync-proposals-to-website.py
```