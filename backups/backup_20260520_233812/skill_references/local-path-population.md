# local_path Population Workflow

## Overview

`local_path` in `projects.csv` should be a filesystem path to the local development directory, NOT a URL. The canonical root is:

```
/home/hermes/.hermes/proposals/workspace-dev/proposals/{project-name}
```

This directory contains **symlinks** to actual project locations, not the actual projects.

## Symlink Strategy

Rather than storing raw paths like `/home/hermes/{repo}`, create symlinks under `workspace-dev/proposals/` that point to the actual locations. This centralizes all local project references.

## Source Locations (search order)

When populating `local_path` for a project in `projects.csv`:

1. `/home/hermes/.hermes/proposals/workspace-dev/proposals/{repo}` — already symlinked
2. `/home/hermes/workspace-dev/proposals/{repo}` — development workspace (many untracked dirs live here)
3. `/home/hermes/{repo}` — direct project directories (e.g., `harness-desktop`, `monopoly3d`)
4. `/home/hermes/opensource/{repo}` — especially for `*-design` VitePress doc sites
5. `/home/hermes/projects/{repo}` — additional projects

## Python Population Script

```python
import csv, os

with open('projects.csv', 'r', encoding='utf-8') as f:
    projects = list(csv.reader(f))

header = projects[0]
lp_idx = header.index('local_path')
gr_idx = header.index('git_repo')

wp_dev = '/home/hermes/.hermes/proposals/workspace-dev/proposals'
os.makedirs(wp_dev, exist_ok=True)

ws_dev = '/home/hermes/workspace-dev/proposals'
home = '/home/hermes'
opensource = '/home/hermes/opensource'
projects_dir = '/home/hermes/projects'

updated = []
for row in projects[1:]:
    if row[lp_idx]:  # skip already filled
        continue
    repo_name = row[gr_idx].split('/')[-1] if row[gr_idx] else ''
    alt = row[1]

    # Try all source locations
    src = None
    for base in [ws_dev, home, opensource, projects_dir]:
        for name in [repo_name, alt]:
            p = f'{base}/{name}'
            if os.path.isdir(p) and not os.path.islink(p):
                src = p
                break
        if src:
            break

    if src:
        target = f'{wp_dev}/{os.path.basename(src)}'
        if not os.path.exists(target):
            os.symlink(src, target)
        row[lp_idx] = target
        updated.append((row[0], row[1], target))

with open('projects.csv', 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(projects)

print(f'Updated {len(updated)} rows')
```

## Key Insight

The `*-design` projects (VitePress documentation sites) are stored under `/home/hermes/opensource/`, not directly under `/home/hermes/`. When a project has `git_repo: https://github.com/YeLuo45/ohmypi-design`, the local path is `/home/hermes/opensource/ohmypi-design`, which symlinks to `workspace-dev/proposals/ohmypi-design`.

## Untracked Directories

`/home/hermes/.hermes/proposals/workspace-dev/proposals/` may contain directories not yet in `projects.csv`. Before creating symlinks, check if the project already exists in CSV. Untracked but GitHub-hosted projects should be added to CSV with new `PRJ-YYYYMMDD-NNN` IDs before linking.

Known untracked (2026-05-16): `dsw-debug`, `dsw-deploy`, `dsw-fresh`, `dsw-new-deploy`, `shared`, `todo-ghpages`, `calculator-app.bak.*` — these are tools/temp/backup dirs, not projects to track.

## After Editing CSV

After any CSV edit, run sync to push to GitHub:
```bash
cd /home/hermes/.hermes/skills/prj-proposals-manager
GITHUB_TOKEN=$(gh auth token) python3 scripts/sync-proposals-to-website.py
```

## Common Pitfalls

1. **Using raw `/home/hermes/{repo}` paths** instead of symlinks — breaks the centralized reference pattern
2. **Forgetting to create symlink** — `local_path` points to non-existent directory
3. **Wrong directory name** — some repos use alternate names (e.g., `todo-list` in filesystem vs `todolist` in git_repo)
4. **CRLF in CSV** — always run `sed -i 's/\r$//' projects.csv proposals.csv` after execute_code writes
5. **Forgetting `workspace-dev/` prefix** — the correct path is `workspace-dev/`, NOT `workplace-dev/` (persistent typo)
6. **Symlink already exists as real directory** — if `workspace-dev/proposals/{repo}` is already a real dir (not symlink), don't try to `os.symlink(src, target)` — just set `local_path` to that path directly

7. **Broken symlink (points to non-existent path)** — a symlink can exist but point to a path that doesn't exist. This is silently broken and worse than no symlink. **Always verify symlink target actually exists** with `readlink -f` + `test -e`:
   ```bash
   # WRONG: just checking symlink exists
   ls -la workspace-dev/proposals/openspec-design  # shows symlink, looks OK

   # CORRECT: verify target also exists
   test -e "$(readlink -f workspace-dev/proposals/openspec-design)" && echo OK || echo BROKEN
   ```
   Real case (2026-05-20): `openspec-design` symlink pointed to `/home/hermes/projects/openspec-design` (non-existent), while CSV correctly had `/home/hermes/opensource/OpenSpec`. Both symlink and CSV must be checked independently.

## Migration Verification Checklist

When migrating `/home/hermes/projects/` entries to `workspace-dev/proposals/` symlinks:

```
for each project:
  1. Check if /home/hermes/projects/{name} EXISTS (real dir or broken symlink)
  2. Check if workspace-dev/proposals/{name} EXISTS as symlink
  3. If symlink exists: verify readlink target == CSV local_path field
  4. If symlink missing: create symlink to correct source path
  5. If symlink target != CSV local_path: fix symlink AND CSV
  6. Verify target path actually exists (test -e)
  7. Update last_update in CSV if any field changed
```

**Critical**: Do NOT trust a symlink's mere existence — `ls -la` shows the symlink even if the target is dead. Always `readlink` + `test -e`.