# Hermes 多智能体团队交付系统

> 基于 proposal-management 构建的智能协作交付体系

---

## 第1页：系统概述

# Hermes 多智能体团队交付系统

## 核心理念

**从需求到交付，全流程智能协调**

- 提案驱动：每个需求都有生命周期追踪
- 角色分工：Coordinator / PM / Dev 专业协同
- 超时自治：无人响应时自动按最优策略推进
- 交付保障：验收通过才视为完成

## 技术栈

| 组件 | 技术 |
|------|------|
| 协调层 | Hermes AIAgent (小墨) |
| 消息传递 | FastAPI (collab-server, port 9119) |
| 状态存储 | SQLite (state.db) |
| 提案索引 | proposal-index.md |
| 文档管理 | 两层结构：项目 → 提案 |

---

## 第2页：核心角色定义

# 三角色协作模型

## Coordinator（小墨）

**职责**：全流程协调与验收

```
接收诉求 → 澄清需求 → 登记提案 → 协调PM → PRD确认
→ 技术方案确认 → 移交开发 → 验收交付
```

**特点**：
- 最多3轮澄清提问
- 设置超时倒计时自动推进
- 开发完成后承担验收职责

---

## PM（Product Manager）

**职责**：需求分析与PRD输出

**输入**：模糊想法、需求草稿、原始诉求

**输出**：正式 PRD 文档

**工作区**：`~/.hermes/workspace-pm/proposals/`

**交付物**：PRD 文档（中文为主，英文标题/术语可选）

---

## Dev（Developer）

**职责**：技术实现与交付

**输入**：已确认的 PRD + 技术方案

**输出**：完整项目实现

**工作区**：`~/.hermes/workspace-dev/proposals/`

**交付物**：功能完整的可部署项目

---

## 第3页：提案生命周期

# 提案状态流转

```
intake → clarifying → prd_pending_confirmation → approved_for_dev
    ↓                                                ↓
clarifying（最多3轮）                      needs_revision
                                                  ↓
                                           in_dev → in_acceptance → accepted → delivered
```

## 状态说明

| 状态 | 说明 |
|------|------|
| intake | 提案登记，接收原始需求 |
| clarifying | 需求澄清阶段（≤3轮） |
| prd_pending_confirmation | PRD 确认中（5分钟超时） |
| approved_for_dev | 技术方案已确认，等待开发 |
| in_dev | 开发中 |
| in_acceptance | 验收中 |
| needs_revision | 需要返修 |
| accepted | 验收通过 |
| delivered | 已向用户交付 |

---

## 第4页：完整工作流程

# 提案处理流程（9步）

## Step 1：需求接收

**动作**：接收 boss 诉求，最多3轮澄清提问

**聚焦**：目标、范围、约束、验收标准

**输出**：更新提案状态为 `clarifying`

---

## Step 2：提案登记

**动作**：在 proposal-index.md 中创建条目

**ID格式**：`P-YYYYMMDD-XXX`

**输出目录**：`workspace-dev/proposals/<slug>/docs/`

---

## Step 3：路由至 PM

**条件**：需求仍是 idea 或需求草稿

**动作**：移交 PM 产出正式 PRD

**输出**：PRD 保存至 `workspace-pm/proposals/`

---

## Step 4：PRD 确认

**动作**：
1. 向 boss 展示 PRD
2. 启动5分钟倒计时
3. 超时默认通过

**超时处理**：`PRD Confirmation` → `timeout-approved`

---

## Step 5：技术诉求确认

**动作**：
1. 询问技术栈、性能、成本、部署方式
2. 最多3轮追问
3. 启动5分钟倒计时
4. 超时按当前假设推进

---

## Step 6：输出技术方案

**输出**：`technical-solution.v1.md`

**状态更新**：`approved_for_dev`

---

## Step 7：移交开发

**动作**：
1. 拉取最新代码
2. 更新状态为 `in_dev`
3. Dev 在 `workspace-dev/proposals/<slug>/` 输出实现

---

## Step 8：验收审查

**检查项**：

- 需求一致性（对照 PRD）
- 功能验收（实际操作验证）
- 构建成功（`npm run build`）
- 交付信息完整

**状态更新**：`in_acceptance`

---

## Step 9：交付或返修

**通过**：状态 → `accepted` / `delivered`，向 boss 最终交付

**不通过**：状态 → `needs_revision`，输出结构化返修意见

---

## 第5页：超时自治机制

# 倒计时规则

## PRD 确认超时

**话术**：
> PRD 已整理完成。请确认是否已完善，可以进入下一步。**5分钟内没有回复，按默认通过继续推进。**

**操作**：提问后立即创建 cron job

```python
cron(action='create',
     schedule='2026-04-16T12:43:00+08:00',
     prompt='【倒计时到期】提案 P-YYYYMMDD-XXX PRD确认超时，默认通过处理。',
     name='P-YYYYMMDD-XXX-prd-confirm')
```

---

## 技术诉求确认超时

**话术**：
> 在输出技术方案前，需要确认你的技术诉求。**5分钟内没有回复，按当前假设默认通过。**

---

## 超时处理流程

1. 等待 cron 超时 system event
2. 按默认动作执行
3. 清理对应 cron job
4. 更新提案记录
5. 补写 Timeout Resolution

---

## 第6页：文档管理规范

# 两层结构：项目 → 提案

## 目录结构

```
~/.hermes/workspace-dev/proposals/<project-slug>/
├── docs/
│   ├── index.md              # 文档索引（版本历史）
│   ├── proposal.md           # 原始提案
│   ├── prd.v1.md            # PRD v1
│   ├── prd.v2.md            # PRD v2（如有修订）
│   ├── technical-solution.v1.md  # 技术方案 v1
│   └── technical-solution.v2.md  # 技术方案 v2（如有修订）
└── （项目源码）
```

---

## 文档索引格式（index.md）

```markdown
# P-YYYYMMDD-XXX: <Title> — Documents

## Proposal
| Version | File | Updated |
|---------|------|---------|

## PRD
| Version | File | Updated | Notes |
|---------|------|---------|-------|

## Technical Solution
| Version | File | Updated | Notes |
|---------|------|---------|-------|
```

---

## 提案文档总索引

路径：`~/.hermes/proposals/proposal-docs-index.md`

格式：

```markdown
## P-YYYYMMDD-XXX: <Title>

| Document | Path | Version | Updated |
|----------|------|---------|---------|
| Proposal | `workspace-dev/proposals/<slug>/docs/proposal.md` | - | YYYY-MM-DD |
| PRD | `workspace-dev/proposals/<slug>/docs/prd.v1.md` | v1.0 | YYYY-MM-DD |
```

---

## 第7页：开发交付标准

# Dev 三项硬指标

## 1. 构建成功

```bash
npm run build
# exit code 必须为 0
```

## 2. 输出目录非空

实际列出文件确认：

```bash
ls -la dist/
```

## 3. 核心源文件存在

验证关键文件存在

---

## 功能自测清单

- [ ] 核心逻辑可正常运行
- [ ] 主要功能流程无崩溃
- [ ] 构建无错误
- [ ] 未破坏现有功能

---

## 交付信息格式

```markdown
## 交付报告

**提案ID**: P-XXXXXXXX-XXX

**修改文件**:
- file1.js: 修改内容说明
- file2.js: 修改内容说明

**验证结果**:
- [x] 核心逻辑自测通过
- [x] npm run build 成功
- [x] 控制台无 Error

**如有问题未解决**:
- 已知问题: 描述 | 原因 | 影响范围
```

---

## 第8页：验收规则

# Coordinator 验收检查

## 1. 需求一致性

- [ ] 结果符合 boss 最终确认的需求
- [ ] PRD 有对应实现（逐一核对）
- [ ] 范围没有偷工减料或自行扩大

## 2. 功能验收（必须实际操作）

- [ ] 核心功能亲自操作验证
- [ ] 控制台是否有 Error（warning 可忽略）
- [ ] 改动未破坏其他功能
- [ ] 构建成功

## 3. 交付信息完整性

- [ ] 提供文件路径
- [ ] 提供启动/访问方式
- [ ] 提供验证说明或截图

## 4. 质量检查

- [ ] 无明显缺失
- [ ] 无明显冲突
- [ ] 已知限制已说明

---

## 验收结果

**不通过** → 输出结构化返修意见：

```markdown
## 返修意见

- **问题**: <description>
- **影响**: <what is affected>
- **期望修复**: <how to fix and verify>
```

**通过** → 状态 → `accepted` / `delivered`，向 boss 最终交付

---

## 第9页：多智能体协作架构

# Hermes 协作层架构

## 组件关系

```
┌─────────────────────────────────────────────────────┐
│                    Boss (用户)                      │
└─────────────────────┬───────────────────────────────┘
                      │ 诉求/确认
                      ↓
┌─────────────────────────────────────────────────────┐
│           Hermes Gateway (消息分发)                 │
│              ~/.hermes/gateway/                     │
└─────────────────────┬───────────────────────────────┘
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
    ┌──────────┐ ┌─────────┐ ┌──────────┐
    │   小墨   │ │   PM    │ │   Dev    │
    │(Main/Coor)│ │(子Agent) │ │(子Agent) │
    └────┬─────┘ └────┬────┘ └────┬─────┘
         │            │           │
         └────────────┴───────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│        Collab Server (FastAPI, port 9119)           │
│     消息转发 / Agent 注册 / 任务状态管理             │
└─────────────────────────────────────────────────────┘
```

---

## Collab CLI 命令

```bash
collab monitor health    # 系统健康
collab monitor events   # 最近事件
collab monitor stats    # 统计信息
collab agent list       # Agent 列表
collab task list        # 任务列表
collab workspace list   # 工作空间列表
```

---

## 子Agent 消息转发流程

1. collab-server 接收消息
2. 通过 subprocess 调用 AIAgent
3. 传递 api_key（设置 ANTHROPIC_API_KEY 环境变量）
4. AIAgent 处理并返回结果

---

## 第10页：接管与修复机制

# 接管触发条件

满足任一条件，Coordinator 直接接管：

- Dev 连续2次交付不合格
- Dev session 被 API 错误中断
- Dev session 异常短（< 30秒宣告完成）
- 构建问题明确且修复简单

---

## 修复沉淀规则

Coordinator 直接修复的问题，必须同步记录到：

1. `MEMORY.md` 的"重要经验"或"技术决策底线"节
2. 当日 `memory/YYYY-MM-DD.md`
3. 对应提案的 `Notes` 或 `Main Fixes Applied` 字段

---

## 第11页：关键配置文件

# 环境配置

## 路径变量

| 变量 | 值 |
|------|-----|
| `PROPOSALS_ROOT` | `~/.hermes/proposals` |
| `TEMPLATES_DIR` | `~/.hermes/proposals/templates` |
| `PM_OUTPUT_DIR` | `~/.hermes/workspace-pm/proposals` |
| `DEV_OUTPUT_DIR` | `~/.hermes/workspace-dev/proposals` |
| `COORDINATOR` | 小墨 |
| `REQUESTER` | boss |

---

## 提案ID格式

- 项目ID：`PRJ-YYYYMMDD-XXX`
- 提案ID：`P-YYYYMMDD-XXX`

---

## 提案索引位置

`~/.hermes/proposals/proposal-index.md`

包含所有提案的当前状态、路径、确认超时等信息。

---

## 第12页：总结

# Hermes 多智能体交付系统特点

## 智能协调

- 提案全生命周期追踪
- 最多3轮澄清机制
- 超时自动按最优策略推进

## 专业分工

- Coordinator：协调与验收
- PM：需求分析与 PRD
- Dev：技术实现

## 交付保障

- 三项硬指标验证
- 功能实际验收
- 结构化返修流程

## 文档规范

- 两层结构（项目→提案）
- 版本化管理
- 统一索引追踪

---

## 适用场景

- 软件开发项目
- 产品需求交付
- 多角色协作流程
- 需要明确交付标准的项目

---

**谢谢观看**

*基于 proposal-management 构建 | Hermes AIAgent 驱动*
