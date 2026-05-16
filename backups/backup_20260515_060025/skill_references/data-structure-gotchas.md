# prj-proposals-manager 数据结构坑点

## 两套数据源的对齐问题

### CSV 侧（结构化存储）

| 文件 | 主键格式 | 说明 |
|------|---------|------|
| `proposals.csv` | `P-YYYYMMDD-XXX` | `project_id` 是 `PRJ-YYYYMMDD-XXX` |
| `projects.csv` | `PRJ-YYYYMMDD-XXX` | `name` 是纯英文项目名 |
| `project_proposal_mapping.csv` | `PRJ-YYYYMMDD-XXX` ↔ `P-YYYYMMDD-XXX` | 关联表 |

**关键字段名对应：**

| 正确字段 | 错误字段（易混淆） |
|---------|------------------|
| `project_id` (PRJ-*) | `projectId`（camelCase，JS/JSON 侧） |
| `project_name` (英文) | `name`（项目自己的 name vs 提案自己的 name） |

### Website JSON 侧（v2 树格式）

```json
{
  "version": 2,
  "projects": [
    {
      "id": "PRJ-20260510-001",       // 来自 projects.csv id
      "name": "ai-subscription",       // 来自 projects.csv name（英文）
      "description": "...",
      "url": "https://...",            // 来自 proposals.csv deployment_url
      "gitRepo": "https://github.com/...",
      "proposals": [
        {
          "id": "P-20260510-001",      // 提案自己的 id
          "name": "some feature",       // 提案自己的 name
          "projectId": "PRJ-20260510-001",
          "projectName": "ai-subscription",
          ...
        }
      ]
    }
  ]
}
```

### 常见坑

#### 坑1：同步脚本分组 key 用错字段

同步脚本 `sync-proposals-to-website.py` 中，若分组逻辑使用 `project_id` 匹配 `projects.csv`，但 CSV 中 `project_id` 格式与 `projects.csv` 的 `id` 格式不匹配，就会把提案自己的 `P-*` id 当作项目 id，产生大量垃圾项目（如 `p-20260509-002`）。

**正确做法**：按 `project_name` 分组，因为 `projects.csv` 的 `name` 字段与 `proposals.csv` 的 `project_name` 字段值一致（都是英文项目名）。

#### 坑2：project.name 混入中文

`projects.csv` 的 `name` 应该是英文。若同步脚本从提案 title 提取项目名，会混入中文。

#### 坑3：url/gitRepo 在项目层级缺失

`proposals.csv` 的 `deployment_url` 和 `git_repo` 是提案级字段。同步到网站 JSON 时，需要**提升**到 project 层级（取该项目的第一个非空值），因为项目卡片（SwimlaneRow）需要展示。

#### 坑4：ProjectDetailPage 和 KanbanView 数据流不一致

- `ProjectDetailPage` → 有 `ProjectInfo` 组件（支持编辑 url/gitRepo）
- `KanbanSwimlanes/SwimlaneRow` → 项目头部**没有** url/gitRepo 展示，也没有编辑入口

这是组件间的不一致：同一个数据在两个视图中的可见性不同。

## 验证检查

同步后用以下命令验证数据质量：

```bash
# 检查垃圾 p-* 项目数量
cat data/proposals.json | python3 -c "
import json, sys
data = json.load(sys.stdin)
garbage = [p for p in data['projects'] if p['id'].startswith('p-')]
print('Garbage projects:', len(garbage))
print('Total projects:', len(data['projects']))
"

# 检查 url/gitRepo 非空率
cat data/proposals.json | python3 -c "
import json, sys
data = json.load(sys.stdin)
has_url = sum(1 for p in data['projects'] if p.get('url'))
has_git = sum(1 for p in data['projects'] if p.get('gitRepo'))
print(f'Has url: {has_url}/{len(data[\"projects\"])}')
print(f'Has gitRepo: {has_git}/{len(data[\"projects\"])}')
"
```
