# project_proposal_mapping.csv Schema Change Log

## Current Structure (2026-05-16+)

```
project_id,project_name,proposal_id,proposal_name
```

4 fields — no redundancy with projects.csv or proposals.csv.

## Historical Structure (pre-2026-05-16)

```
project_id,project_name,project_git_repo,project_local_path,proposal_id,proposal_name,proposal_status
```

7 fields — three fields were removed as redundant:
- `project_git_repo` — already in projects.csv
- `project_local_path` — already in projects.csv
- `proposal_status` — already in proposals.csv

## Scripts That Must Be Updated on Schema Change

When changing project_proposal_mapping.csv structure, these files must be updated in sync:

| File | What to Update |
|------|----------------|
| `scripts/proposal_manager_cli.py` | MAPPING_CSV_HEADERS constant + any mapping write/read logic |
| `scripts/sync-proposals-to-website.py` | Docstring comment at top |
| `scripts/pull-proposals-from-github.py` | mapping_headers + mapping_rows dict construction |
| `scripts/init_proposals_dir.py` | CSV_FILES dict entry |
| `SKILL.md` | CSV Schema section |
| `SKILL-zh.md` | CSV Schema section |
| `references/csv-structure-recovery.md` | Structure reference |
| `references/data-model.md` | This file / schema change log |

## Data Migration Command

```python
import csv

old_csv = "/path/to/project_proposal_mapping.csv"
new_csv = "/path/to/project_proposal_mapping.csv.new"
backup = old_csv + ".bak_before_field_removal"

with open(old_csv, 'r', encoding='utf-8') as f:
    content = f.read()
with open(backup, 'w', encoding='utf-8') as f:
    f.write(content)

NEW_HEADERS = ['project_id', 'project_name', 'proposal_id', 'proposal_name']

with open(old_csv, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open(new_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=NEW_HEADERS, extrasaction='ignore')
    writer.writeheader()
    for row in rows:
        writer.writerow({k: row.get(k, '') for k in NEW_HEADERS})
```

## Verification

After migration, verify row count is unchanged:
```bash
wc -l old.csv new.csv   # counts must match
```