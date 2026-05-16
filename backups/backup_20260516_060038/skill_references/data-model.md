# Data Model & CSV Reference

## Index Files

**重要变更：2026-05-05 起，数据以 CSV 为结构化存储，markdown 仅作轻量快速索引。**

| File | Purpose | Format |
|------|---------|--------|
| `~/.hermes/proposals/proposals.csv` | 提案主数据（20字段，含 project_id 外键） | CSV |
| `~/.hermes/proposals/projects.csv` | 项目主数据（id, name, proposal_count, git_repo） | CSV |
| `~/.hermes/proposals/project_proposal_mapping.csv` | Project↔Proposal 映射关系 | CSV |
| `~/.hermes/proposals/proposal-index.md` | 提案快速索引（仅含统计摘要，指向 CSV） | Markdown |
| `~/.hermes/proposals/project-index.md` | 项目快速索引（仅含清单和统计，指向 CSV） | Markdown |

### CSV Fields

**proposals.csv**：id, title, owner, status, project_id, project_name, stage, prd_path, tech_solution_path, project_path, git_repo, **prj_url**, deployment_branch, prd_confirmation, tech_expectations, acceptance, research_direction, last_update, engine, target, game_type, notes (22 fields)

**projects.csv**：id, name, proposal_count, git_repo, local_path, **prj_url**, description, last_update (8 fields)

**project_proposal_mapping.csv**：project_id, project_name, project_git_repo, project_local_path, proposal_id, proposal_name, proposal_status

### Relationships

- `project-index.md` 和 `proposal-index.md` 共同构成完整的"项目-提案"双视角索引
- `project_proposal_mapping.csv` 同步维护
- 写入前全部字段自动校验，校验失败则中断，不写入

## Validation Rules

| 字段 | 校验内容 |
|------|---------|
| `id` | 格式 `PRJ-YYYYMMDD-XXX` 或 `P-YYYYMMDD-XXX`，自动判重 |
| `project_id` | 外键必须已存在于 `projects.csv` |
| `status` | 必须在有效枚举值内 |
| `git_repo` | 必须以 `http://` `https://` 或 `git@` 开头（可空） |
| `prj_url` | 同上（可空，从 git_repo 推断） |
| `prd_confirmation` | 枚举：`pending`, `confirmed`, `timeout-approved`, `rejected`, 空 |
| `tech_expectations` | 同上 |
| `acceptance` | 枚举：`pending`, `accepted`, `rejected`, 空 |
| `game_type` | 枚举：休闲/策略/卡牌/RPG/消除/塔防/模拟/动作/射击 |
| 必填 | `id`, `title`, `project_id`, `status` 不能为空 |

## Data Write Rules

- 新增时自动填充 `last_update` 为当天日期
- 新增提案时自动继承所属项目的 `git_repo`
- 新增/删除提案时自动更新对应项目的 `proposal_count`
- `project_proposal_mapping.csv` 同步维护
- 写入前全部字段自动校验，校验失败则中断，不写入

## Duplicate Columns

**CSV rewrite operations can produce duplicate columns if not explicitly deduplicated.**

Symptom: `projects.csv` header shows `prj_url,prj_url` (two identical column names). The CSV appears to read fine but `csv.DictReader` silently drops the second occurrence, so the actual data mapping is wrong.

**When rewriting CSV programmatically (e.g., in sync scripts or data fixes):**
```python
# WRONG: csv.DictReader + csv.DictWriter can silently drop duplicate columns
rows = list(csv.DictReader(content.splitlines()))
writer = csv.DictWriter(f, fieldnames=fieldnames)  # fieldnames may have dupes

# CORRECT: Explicitly deduplicate columns before writing
seen = set()
new_fieldnames = []
for fn in fieldnames:
    if fn in seen:
        continue  # skip duplicate
    seen.add(fn)
    new_fieldnames.append(fn)
writer = csv.DictWriter(f, fieldnames=new_fieldnames)
```

**Detection:**
```bash
# Count occurrences of 'prj_url' in header
awk -F',' 'NR==1 {print gsub(/prj_url/, "")}' projects.csv
# If result > 1, duplicate exists
```
