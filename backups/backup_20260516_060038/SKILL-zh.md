---
name: prj-proposals-manager
description: 管理从提案受理到交付的全生命周期，协调各Agent或角色协作（协调者 / PM专家 / 开发专家 / 测试专家 / 调研专家）。覆盖受理、澄清、PRD确认、技术评审、测试用例生成、开发交接、验收和交付环节。支持任意Agent平台
version: 2.5.0
author: YeLuo45
license: MIT
metadata:
  hermes:
    tags: [proposal, workflow, lifecycle, project-management, coordinator, pm, dev, test, research]
    homepage: https://yeluo45.github.io/prj-proposals-manager/
    related_skills: [harness-desktop-iteration-workflow, dbg-card-game-workflow, pixel-pal-web-workflow]
---

# 提案管理系统

一个跨平台通用的提案生命周期管理技能，适用于多角色工作流（协调者 / PM / 开发 / 测试专家 / 调研专家）。

## 架构：CSV作为权威数据源

```
+------------------+       +---------------------+       +------------------+
|   CSV 文件        | <--> |  proposal_manager   | -->   |  Markdown 文件   |
| (权威数据源)      |       |  _cli.py           |       | (派生数据)       |
+------------------+       +---------------------+       +------------------+
        |                                                       |
        v                                                       v
+------------------+                                   +------------------+
|  GitHub 远程     | <------------------------------- |  sync-proposals  |
|  (CSV推送)       |                                   |  -to-website.py  |
+------------------+                                   +------------------+
```

**数据流：**
1. 所有变更通过 `proposal_manager_cli.py` 进行（写入CSV）
2. CSV文件是**唯一权威数据源**
3. `sync-proposals-to-website.py` 读取CSV并推送到GitHub
4. LLM根据CSV内容生成/更新Markdown文件

## 快速开始

```bash
# 初始化（首次使用）
python3 scripts/init_proposals_dir.py

# 创建项目（带工作空间初始化）
python3 scripts/proposal_manager_cli.py project add --name "项目名" --git-repo "https://github.com/owner/repo" --init-workspace

# 创建提案
python3 scripts/proposal_manager_cli.py proposal add --title "提案标题" --project-id PRJ-YYYYMMDD-XXX

# 更新提案字段
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --status in_dev
python3 scripts/proposal_manager_cli.py proposal update P-YYYYMMDD-XXX --deployment-url "https://..."

# 更新项目字段
python3 scripts/proposal_manager_cli.py project update PRJ-YYYYMMDD-XXX --name "新名称"

# 查看状态
python3 scripts/proposal_manager_cli.py proposal list --fields id,title,status,project_name
python3 scripts/proposal_manager_cli.py project list --fields id,name,proposal_count

# 同步到GitHub
GITHUB_TOKEN=$GITHUB_TOKEN python3 scripts/sync-proposals-to-website.py

# 备份
bash scripts/backup_proposals.sh
```

## CSV结构（权威数据源）

### projects.csv
```
id,name,proposal_count,git_repo,local_path,description,last_update
PRJ-20260419-007,ai-creator-h5,3,https://github.com/owner/repo,/path/to/local,我的项目,2026-05-15
```

### proposals.csv
```
id,title,owner,status,project_id,project_name,stage,prd_path,tech_solution_path,project_path,
git_repo,deployment_url,deployment_branch,prd_confirmation,tech_expectations,acceptance,
research_direction,last_update,engine,target,game_type,notes
```

### project_proposal_mapping.csv
```
project_id,project_name,project_git_repo,project_local_path,proposal_id,proposal_name,proposal_status
```

## 工作流程

```
Step 1a/1b: 受理 -- 登记提案（从现有代码库或全新）
Step 2: 澄清 -- 最多3轮
Step 3: 必要时转给PM
Step 4: PRD确认关卡
Step 5: 技术诉求关卡（最多3轮）
Step 6: 输出技术方案
Step 6b: 交接给测试专家 -- 生成TDD测试用例
Step 7: 交接给开发（以测试用例为参考）
Step 8: 测试专家基于测试用例执行验收
Step 9: 交付或修订
Step 10: 研究方向（验收后迭代规划）
Step 11: 部署（验收后交付）
Step 12: 网站重建
```

### Step 1a: 从现有代码库登记

当需求是从现有GitHub仓库克隆并登记为提案时（而非从零构建）：

1. 克隆仓库到 `$DEV_OUTPUT_DIR/<项目名>/proposals/` 或本地复制

2. 对于设计文档项目（`*-design`），使用直接 `cp -r` + 网站补丁工作流（绕过sync脚本）

### Step 1b: 从零登记新提案

1. 读取 `$PROPOSALS_ROOT/proposal-index.md` 确定下一个ID
2. 将 `$TEMPLATES_DIR/request-intake-template.md` 复制到 `$PROPOSALS_ROOT/P-YYYYMMDD-XXX.md`
3. 填写基本信息和原始需求
4. 在 `proposal-index.md` 的 Active Proposals 下添加条目，状态为 `intake`
5. 在 `$PROPOSAL_DOCS_INDEX` 中为此提案添加条目
6. 创建 `$DEV_OUTPUT_DIR/<项目名>/proposals/docs/index.md` 并写入初始索引结构

### Step 2: 澄清需求

- 向需求方最多进行3轮澄清提问，聚焦于：目标、范围、约束、验收标准
- 在提案文件中的 Clarification 部分记录每轮问答
- 3轮后或需求已清晰时，记录最终假设
- 将状态更新为 `clarifying`

### Step 3: 转给PM

如果需求只是一个想法或粗略草稿，转交给PM角色生成PRD。

- PM将PRD保存到 `$PM_OUTPUT_DIR/<项目名>/YYYY-MM-DD-prd.md`
- PM同时将PRD复制到 `$DEV_OUTPUT_DIR/<项目名>/proposals/docs/prd.v1.md`
- PM交付后更新 `proposal-index.md` 中的 PRD Path

### Step 4: PRD确认关卡

PM返回PRD后：

1. 向需求方展示PRD并请求确认
2. 启动确认倒计时（建议：5分钟）
3. 在 "PRD Confirmation Countdown ID" 中记录倒计时引用

如果确认：将 PRD Confirmation 设为 `confirmed`，取消倒计时，然后立即将状态更新为 `approved_for_dev` 并启动开发。

如果超时：将 PRD Confirmation 设为 `timeout-approved`，在 "Timeout Resolution" 中记录，然后立即将状态更新为 `approved_for_dev` 并启动开发。

### Step 5: 技术诉求关卡

输出技术方案前：

1. 向需求方了解：技术栈、性能、成本、部署方式、可维护性、依赖约束
2. 最多3轮提问
3. 启动确认倒计时（与Step 4相同机制）
4. 在 "Technical Expectations Countdown ID" 中记录

如果确认：将 Technical Expectations 设为 `confirmed`，立即编写技术方案并将状态更新为 `approved_for_dev`。

如果超时：将 Technical Expectations 设为 `timeout-approved`，按当前假设继续，立即编写技术方案并将状态更新为 `approved_for_dev`。

### Step 6: 技术方案

- 将技术方案输出到 `$PROPOSALS_ROOT/P-YYYYMMDD-XXX-tech-solution.md`
- 同时复制到 `$DEV_OUTPUT_DIR/<项目名>/proposals/docs/technical-solution.v1.md`
- 将状态更新为 `approved_for_dev`

### Step 6b: TDD测试用例生成

技术方案输出后，交接给测试专家基于TDD原则生成测试用例：

1. 协调者将任务转给测试专家，附带：PRD文档、技术方案文档、项目背景

2. 测试专家输出测试用例到 `$TEST_OUTPUT_DIR/<项目名>/YYYY-MM-DD-test-cases.md`
   - 测试用例必须可追溯到PRD需求
   - 包含测试用例ID、描述、前置条件、步骤、预期结果
   - 覆盖正常路径和边界情况
   - 将测试用例复制到 `$DEV_OUTPUT_DIR/<项目名>/proposals/docs/test-cases.v1.md`

3. 更新追踪：更新 `proposal-index.md` 中的 Test Cases Path，状态更新为 `in_tdd_test`

### Step 7: 交接给开发

- 将状态更新为 `in_dev`
- 如果目录不存在，开发创建 `$DEV_OUTPUT_DIR/<项目名>/proposals/docs/`
- 开发将项目产出保存到 `$DEV_OUTPUT_DIR/<项目名>/proposals/`
- 更新 `proposal-index.md` 中的 Project Path

### Step 8: 测试专家验收（基于TDD）

开发报告完成后，测试专家基于测试用例执行验收：

需求一致性：
- 符合需求方确认的需求
- 与PRD对齐
- 无范围蔓延或偷工减料

测试用例执行：
- 执行 `test-cases.vN.md` 中的每个测试用例
- 记录每个测试用例的通过/失败状态
- 记录任何偏差或失败

功能验证（必须实际操作，不能只截图）：
- 核心功能端到端正常工作
- 控制台/日志无Error（warning可忽略）
- 现有功能未被破坏
- 构建成功

验收期间将状态更新为 `in_test_acceptance`。

如果所有测试用例通过：进入Step 9（交付）

如果任何测试用例失败：将状态更新为 `test_failed`，输出结构化返修意见。

### Step 9: 交付或修订

如果所有测试用例通过：将状态更新为 `accepted`，进入Step 10（研究方向）

如果未通过验收：将状态更新为 `needs_revision`，输出结构化返修意见。

### Step 10: 研究方向（验收后迭代规划）

验收通过后（状态变为 `accepted` 或 `delivered`）：

1. 协调者询问需求方："基于本次交付，你希望进入下一个迭代方向探索，还是先维护当前版本？"
2. 启动5分钟确认倒计时，创建cron job
3. 在 "Research Direction Countdown ID" 中记录倒计时引用

如果需求方确认方向：将 Research Direction 设为 `confirmed`，立即将任务转给PM生成下一个迭代PRD。

如果超时：将 Research Direction 设为 `timeout-approved`，协调者自主决策，立即将任务转给PM生成下一个迭代PRD。

### Step 11: 部署（验收后交付）

验收完成后（状态变为 `accepted`），协调者处理部署：

1. 确定部署目标：GitHub Pages 或 Cloudflare Pages
2. 创建部署分支
3. 准备部署（确保package-lock.json已提交，运行 `npm run build`）
4. 推送到远程
5. 触发部署
6. 验证部署
7. 更新提案：状态设为 `deployed`，记录 Deployment URL 和 Deployment Branch
8. 同步到proposals-manager网站 + hermes-agent

### Step 12: 网站重建

- 使用 `proposal-sync-website` skill 更新 YeLuo45/prj-proposals-manager 中的 `data/proposals.json`
- 同步后重建网站：从GitHub API下载更新的 `proposals.json` 到 `public/data/proposals.json`，然后 `npm run build` 并gh-pages deploy

## 开发交付质量检查

验收前必须验证三项硬指标：

1. 构建exit code：必须为0
2. 输出目录非空：列出核心文件确认
3. 核心源码/服务文件存在：验证关键文件存在

### 接管触发条件

满足任一条件时，协调者应直接从开发手中接管：
- 开发连续2次交付不合格
- 开发session被API/配额错误中断
- 开发session异常短（< 30秒）却声称完成
- 修复方法简单且明确

### 修复记录

协调者直接修复问题时，记录到：
1. 项目memory文件（如 `MEMORY.md`）的相关章节
2. 每日日志（如 `memory/YYYY-MM-DD.md`）
3. 提案的 Notes 或 Main Fixes Applied 字段

## 索引条目模板

添加到 `proposal-index.md` 时：

### P-YYYYMMDD-XXX: <标题>

- Proposal ID: P-YYYYMMDD-XXX
- Title: <标题>
- Owner: <协调者>
- Current Status: <状态>
- PRD Path: （PM填写）
- Technical Solution: （待填写）
- Test Cases Path: （测试专家填写）
- Project Path: （开发填写）
- Acceptance: -
- PRD Confirmation: pending
- PRD Confirmation Countdown ID: -
- Technical Expectations: pending
- Technical Expectations Countdown ID: -
- Research Direction: pending
- Research Direction Countdown ID: -
- Deployment URL: （部署后填写）
- Deployment Branch: （部署后填写）
- Last Update: YYYY-MM-DD
- Notes:

## 提案状态（统一）

```
intake -> clarifying -> prd_pending_confirmation -> approved_for_dev -> in_tdd_test -> in_dev -> in_test_acceptance -> accepted -> deploying -> deployed
                                                                                   |                              |
                                                                         needs_revision -> in_dev              test_failed -> in_dev
```

## 脚本说明

| 脚本 | 用途 |
|------|------|
| init_proposals_dir.py | 初始化/修复提案目录结构 |
| proposal_manager_cli.py | 项目和提案的增删改查（所有CSV操作必须通过此脚本） |
| edit_proposal.py | 遗留的字段编辑器（建议使用cli.py） |
| sync-proposals-to-website.py | 读取CSV，推送到GitHub，生成网站JSON |
| backup_proposals.sh | 备份所有提案系统数据 |
| rollback_proposals.sh | 回滚：全量回滚、项目回滚、提案回滚 |

## 备份与回滚

### 备份

```bash
# 创建备份（保留最近10个备份）
bash scripts/backup_proposals.sh

# 备份存储位置: ~/.hermes/proposals/backups/
```

### 回滚

```bash
# 列出可用备份
bash scripts/rollback_proposals.sh list

# 验证备份完整性
bash scripts/rollback_proposals.sh verify proposals_backup_YYYYMMDD_HHMMSS.tar.gz

# 全量回滚（到最新备份）
bash scripts/rollback_proposals.sh full

# 全量回滚到指定备份（N=1为最新，N=2为第二新）
bash scripts/rollback_proposals.sh full 3

# 回滚指定项目
bash scripts/rollback_proposals.sh project PRJ-YYYYMMDD-XXX

# 回滚指定提案
bash scripts/rollback_proposals.sh proposal P-YYYYMMDD-XXX
```

### 回滚行为

| 命令 | 恢复内容 |
|------|----------|
| `full N` | 从备份N恢复所有CSV和Markdown文件 |
| `project <id> N` | projects.csv条目 + 相关提案 + mapping |
| `proposal <id> N` | proposals.csv中单个提案 + mapping |

**安全机制：**
- 全量回滚前：创建当前状态的紧急备份
- 项目/提案回滚前：创建紧急备份
- 所有操作需要输入 `yes` 确认

## 配置

| 变量 | 值 | 说明 |
|------|-----|------|
| PROPOSALS_ROOT | ~/.hermes/proposals | 存放CSV和Markdown文件的根目录 |
| DEV_OUTPUT_DIR | ~/.hermes/proposals/workspace-dev/<项目>/proposals | 开发工作空间 |
| PM_OUTPUT_DIR | ~/.hermes/proposals/workspace-pm/<项目>/proposals | PM工作空间 |
| TEST_OUTPUT_DIR | ~/.hermes/proposals/workspace-test/<项目>/proposals | 测试工作空间 |
| RESEARCH_OUTPUT_DIR | ~/.hermes/proposals/workspace-research/<项目>/proposals | 调研工作空间 |

## 数据规则

1. **CSV是权威数据源** - 所有变更必须通过 `proposal_manager_cli.py`
2. **Markdown文件是派生数据** - 由LLM根据CSV内容生成/更新
3. **GitHub CSV合并到本地** - 远程CSV中的新条目会合并到本地CSV
4. **CSV始终推送到GitHub** - 任何变更后，sync脚本将CSV文件推送到GitHub

## 工作空间初始化

使用 `--init-workspace` 创建项目时，脚本会创建：

```
workspace-dev/<项目>/proposals/
workspace-dev/<项目>/proposals/docs/index.md

workspace-pm/<项目>/proposals/
workspace-pm/<项目>/proposals/docs/index.md

workspace-test/<项目>/proposals/
workspace-test/<项目>/proposals/docs/index.md

workspace-research/<项目>/proposals/
workspace-research/<项目>/proposals/docs/index.md
```

每个 `docs/index.md` 包含Proposal、PRD、Technical Solution和Test Cases的版本追踪表。

## 通过CLI编辑字段

所有CSV字段都可通过 `proposal_manager_cli.py` 更新：

```bash
# 更新提案字段
python3 scripts/proposal_manager_cli.py proposal update <id> \
    --status in_dev \
    --prd-path "workspace-pm/my-project/proposals/docs/prd.v1.md" \
    --deployment-url "https://owner.github.io/my-project" \
    --notes "已修复关键bug"

# 更新项目字段
python3 scripts/proposal_manager_cli.py project update <id> \
    --name "新名称" \
    --git-repo "https://github.com/owner/new-repo"
```

## 重要说明

### 路径发现

Hermes环境：
- `~/.hermes/proposals/` 是实际的提案根目录 -- 而非 `~/proposals/`
- 主索引文件是 `proposal-docs-index.md`（而非 `proposal-index.md`）

OpenClaw环境（Windows/WSL）：
- 提案根目录：`~/.openclaw/workspace/proposals/`
- 主索引文件是 `proposal-index.md`
- PM输出：`~/.openclaw/workspace-pm/proposals/`
- 开发输出：`~/.openclaw/workspace-dev/proposals/`

### 关键：execute_code文件写入会移除所有换行符

通过execute_code写回 `proposal-index.md` 时，整个文件会变成单行。始终在用于 `proposal-index.md` 之前先备份。

安全做法：
1. 写回前先 `cp proposal-index.md proposal-index.md.bak`
2. 或先写到 `/tmp/` 验证内容正确后再覆盖
3. 永远不要在execute_code中直接覆盖 `proposal-index.md`

### 处理重复的Cron超时事件

处理cron超时事件时：
1. 首先检查 `proposal-index.md`，看状态是否已被之前的相同cron事件更新过
2. 如果 PRD Confirmation 或 Technical Expectations 已显示 `timeout-approved`，不要再更新
3. 同一个cron事件可能多次到达；幂等性至关重要
4. 同时检查 `proposals.csv` -- 提案可能在 `proposal-index.md` 中但不在CSV中

### CSV重复预防

通过patch工具向 `proposals.csv` 添加新条目时：
1. 首先验证ID不存在
2. old_string使用唯一上下文
3. 如果不小心创建了重复，立即移除

## 模板

此skill期望在 `$TEMPLATES_DIR/` 中有三个模板：

| 模板 | 用途 |
|------|------|
| request-intake-template.md | 初始提案登记，含澄清字段和确认关卡 |
| proposal-status-template.md | 状态追踪，含关联资源、确认关卡和返修意见 |
| acceptance-checklist-template.md | 结构化验收评审，含功能/质量/交付检查项 |

## 已知问题

| 问题 | 参考文档 |
|------|----------|
| sync-proposals-to-website.py 分组逻辑陷阱 | references/sync-script-pitfalls.md |
| Vite build后bundle不更新 | references/vite-cache-issue.md |

## 参考文档

| 文档 | 说明 |
|------|------|
| references/data-model.md | CSV结构和字段验证 |
| references/data-recovery.md | 数据损坏恢复 |
| references/data-structure-gotchas.md | CSV-JSON字段对齐 |
| references/website-sync.md | GitHub同步架构 |
| references/sync-script-pitfalls.md | Sync脚本已知问题 |
| references/vite-cache-issue.md | Vite构建缓存问题 |
