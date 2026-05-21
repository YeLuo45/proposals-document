# Proposal Index

Last updated: 2026-05-16 23:45:00

## Active Proposals

### PENDING CONFIRMATION

#### P-20260522-001: 调度器可视化

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (7fb1412)
- **Last Update**: 2026-05-22
- **PRD Path**: workspace-pm/proposals/P-20260522-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (7fb1412)
- **Views**: SchedulerView.vue
- **API**:
  - GET/POST /api/scheduler/jobs — 任务CRUD
  - PUT/DELETE /api/scheduler/jobs/:id — 更新/删除
  - POST /api/scheduler/jobs/:id/toggle — 启用/禁用
  - POST /api/scheduler/jobs/:id/run — 手动触发
  - GET /api/scheduler/history — 执行历史
- **Tables**: scheduled_jobs, scheduled_job_history

### PENDING CONFIRMATION

#### P-20260521-002: Pipeline 步骤细分

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (dbee051)
- **Last Update**: 2026-05-21
- **PRD Path**: workspace-pm/proposals/P-20260521-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (dbee051)
- **Views**: PipelineStages.vue
- **API**:
  - GET/POST /api/pipeline-stages/templates — 模板CRUD
  - GET /api/pipeline-stages/templates/default — 默认模板
  - POST /api/pipeline-stages/pipelines/:id/stages — 添加Stage
  - GET /api/pipeline-stages/pipelines/:id/stages — 列表
  - PUT /api/pipeline-stages/stages/:id — 更新Stage
  - DELETE /api/pipeline-stages/stages/:id — 删除
  - POST /api/pipeline-stages/stages/reorder — 拖拽排序
- **Tables**: pipeline_templates, pipeline_stages_v2

### PENDING CONFIRMATION

#### P-20260521-001: GitHub Actions 集成

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (984bfb9)
- **Last Update**: 2026-05-21
- **PRD Path**: workspace-pm/proposals/P-20260521-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (984bfb9)
- **Views**: GitHubActions.vue
- **API**:
  - GET /api/github/actions/workflows?repoId= — 列表 Workflows
  - POST /api/github/actions/workflows/:workflowId/run — 触发
  - GET /api/github/actions/runs?repoId= — Runs 列表
  - GET /api/github/actions/runs/:runId — Run 详情 + Jobs + Steps
  - GET /api/github/actions/jobs/:jobId — Job 详情
  - GET /api/github/actions/logs/:jobId/:stepNumber — Step 日志
- **Tables**: github_actions_configs, action_runs

### PENDING CONFIRMATION

#### P-20260520-002: 通知系统 UI

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (eea97fc)
- **Last Update**: 2026-05-20
- **PRD Path**: workspace-pm/proposals/P-20260520-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (eea97fc)
- **Views**:
  - NotificationSettings.vue: 5个Tab (Telegram/Email/Webhook/事件订阅/历史)
- **API**:
  - GET/PUT /api/settings/email — Email 配置
  - POST /api/settings/email/test — 测试邮件
  - GET/PUT /api/settings/webhook — Webhook 配置
  - POST /api/settings/webhook/test — 测试 Webhook
- **Notes**:
  - Settings.vue 简化为链接入口
  - 完整通知渠道配置 UI

### PENDING CONFIRMATION

#### P-20260520-001: UI 界面增强

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (6873691)
- **Last Update**: 2026-05-20
- **PRD Path**: workspace-pm/proposals/P-20260520-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (6873691)
- **Views**:
  - PipelineKanban.vue: 四列看板 (pending/running/success/failed) + 详情弹窗
  - BatchPanel.vue: 批量列表 + 创建表单 + pause/resume/cancel
  - DeployTargets.vue: 目标CRUD + 类型表单 (githubPages/vps/s3/script) + 连接测试
- **Router**: /pipelines /batch /deploy-targets
- **Nav**: App.vue 侧边栏新增导航项

### PENDING CONFIRMATION

#### P-20260519-002: 部署目标管理增强

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (7c7a545)
- **Last Update**: 2026-05-19
- **PRD Path**: workspace-pm/proposals/P-20260519-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (7c7a545)
- **API**:
  - GET/POST /api/deploy/targets — 列表/创建
  - GET/PUT/DELETE /api/deploy/targets/:id — 详情/更新/删除
  - POST /api/deploy/targets/:id/test — 测试连接
  - POST /api/deploy/:targetId/run — 执行部署
  - POST /api/deploy/:targetId/rollback — 回滚
  - POST /api/deploy/multi — 多目标部署
  - GET /api/deploy/:targetId/snapshots — 可用快照
  - GET /api/deploy/rollback/history — 回滚历史
- **Notes**:
  - deploy_targets / deploy_history / rollback_history 表
  - 4种部署器: githubPages / vps(ssh2) / s3(@aws-sdk) / script
  - RollbackManager: backup/restore

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (1b81129)
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-002-prd.md
- **Tech Solution**: workspace-dev/proposals/github-repo-manager/P-20260518-002-tech-solution.md
- **Direction**: A
- **Mode**: 无人值守模式（自动确认、自动验收、自动迭代）
- **Git**: 本地 master 已 commit (1b81129)
- **API**:
  - GET /api/pipeline-history (列表+分页)
  - GET /api/pipeline-history/stats (统计)
  - GET /api/pipeline-history/kanban (看板)
  - GET /api/pipeline-history/:id (详情)
  - POST /api/pipeline-history/cleanup
- **Notes**:
  - server/db/init.js: pipeline_history + pipeline_stages 表
  - server/services/pipelineHistory.js: 历史记录服务
  - server/routes/pipelineHistory.js: API 路由
  - server/services/pipelineOrchestrator.js: 集成历史钩子

### PENDING CONFIRMATION

#### P-20260518-001: Webhook 外部触发 + GitHub Webhook 事件订阅

### PENDING CONFIRMATION

#### P-20260516-003: MessageBus 事件驱动重构 + 无人值守模式

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (8efea95)
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260516-003-prd.md
- **Tech Solution**: workspace-dev/proposals/github-repo-manager/P-20260516-003-tech-solution.md
- **Direction**: A (MessageBus 事件驱动重构)
- **Mode**: 无人值守模式（自动确认、自动验收、自动迭代）
- **Git**: 本地 master 已 commit (8efea95)，push 阻塞（HTTP 408），tree 已创建 (ef8fe36)
- **阻塞**: 网络阻塞 git push，API 方式 tree 已创建但 commit 创建超时
- **API**: GET/PUT /api/settings/telegram, POST /api/settings/telegram/test
- **Notes**: 
  - npm run build: ✅
  - Telegram Bot API 封装: ✅
  - 多渠道通知 (Email + Telegram): ✅
  - 统一 send() 入口: ✅
  - GitHub push: 网络不稳定，commit 已保存待重试

### IN DEV

#### P-20260419-001: Proposal Request Intake

- **Project**: temple-run
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-04-19

#### P-20260419-005: PRD: Hermes Agent 团队协作增强

- **Project**: hermes-agent-collab
- **Owner**: 
- **Stage**: ### Phase 1: 基础框架（1-2 周）
- **Acceptance**: 
- **Last Update**: 2026-04-19

#### P-20260422-001: PRD — 解谜游戏：房间逃脱

- **Project**: room-escape-puzzle
- **Owner**: 
- **Stage**: **5个关卡**
- **Acceptance**: 
- **Last Update**: 2026-04-22

#### P-20260422-003: 

- **Project**: match3-puzzle
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260422-005: 

- **Project**: little-garden
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260426-001: 

- **Project**: preschool-puzzle
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260427-001: PRD - 3D飞行棋（Flight Chess 3D）

- **Project**: flight-chess-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-04-27

#### P-20260429-001: PRD — 3D打地鼠 V2: 道具/关卡/皮肤系统

- **Project**: whack-a-mole-3d
- **Owner**: 
- **Stage**: | 内容 | 周期 |
- **Acceptance**: 
- **Last Update**: 2026-04-29

#### P-20260430-001: P-20260430-001: 3D打地鼠 V3 — 每日任务+经济循环

- **Project**: whack-a-mole-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-04-30

#### P-20260430-002: P-20260430-002: 3D打地鼠 V3 — 新世界+Boss战

- **Project**: whack-a-mole-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-04-30

#### P-20260502-001: Proposal Intake — P-20260502-001

- **Project**: ai-novel-assistant
- **Owner**: 
- **Stage**: | 交付物 |
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-003: Intake — P-20260502-003

- **Project**: ai-novel-assistant
- **Owner**: 
- **Stage**: | 内容 | 交付物 |
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-004: Harness Desktop v3 - PRD

- **Project**: flight-chess-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-007: Proposal Intake — P-20260502-007

- **Project**: game-1024
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-008: Proposal Intake — P-20260502-008

- **Project**: game-1024
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-017: PRD: ai-subscription — 大模型调用层升级 (llm-design-dev)

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: | 内容 | 产出 |
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260503-020: PRD: DBG卡牌游戏 V38 — 新手教程 + 卡牌使用率追踪

- **Project**: todolist
- **Owner**: 
- **Stage**: | 时机 | 内容 |
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-028: PRD: creative-drawing-board V5 — 气泡游戏强化

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-038: PRD: creative-drawing-board V15 — 描红/模板内容大扩充

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-039: PRD: creative-drawing-board V16 — 绘画工具增强

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260503-040: PRD: creative-drawing-board V17 — 多语言支持

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260503-041: PRD: creative-drawing-board V18 — 气泡游戏改版

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260503-042: PRD: creative-drawing-board V19 — 农历/节日主题包

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260503-043: PRD: creative-drawing-board V20 — 打印功能增强

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260503-044: PRD: creative-drawing-board V21 — 画廊 + 社区分享

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260503-045: PRD: creative-drawing-board V22 — 更多游戏模式

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260503-046: PRD: creative-drawing-board V23 — 更多绘画工具

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260503-047: PRD: creative-drawing-board V24 — 动画制作

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260503-048: PRD: creative-drawing-board V25 — 音效/MIDI 制作

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-049: PRD: creative-drawing-board V26 — AR 绘画

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-050: PRD: creative-drawing-board V27 — 视频录制

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-051: PRD: creative-drawing-board V28 — 声音录制

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-052: PRD: creative-drawing-board V29 — 3D 绘画（简化版）

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-053: PRD: creative-drawing-board V30 — 粒子特效

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-054: PRD: creative-drawing-board V31 — 音频可视化

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-055: PRD: creative-drawing-board V32 — 增强现实贴纸

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-056: PRD: creative-drawing-board V33 — 智能建议

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-057: PRD: creative-drawing-board V34 — 手势识别

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-058: PRD: creative-drawing-board V35 — 好友系统

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-059: PRD: creative-drawing-board V36 — 成就系统

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-060: PRD: creative-drawing-board V37 — 主题商店

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-061: PRD: creative-drawing-board V38 — 每日挑战

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-3009: 

- **Project**: future-little-leaders
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3032: 

- **Project**: flight-chess-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3040: 

- **Project**: flight-chess-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3041: 

- **Project**: flight-chess-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3043: 

- **Project**: flight-chess-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3054: 

- **Project**: ai-novel-assistant
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3096: 

- **Project**: preschool-puzzle
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260505-005: PRD: ai-stock-simulation 多策略对比

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-006: P-20260505-006 策略参数优化面板 PRD

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-007: P-20260505-007 真实K线数据对接 PRD

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-008: P-20260505-008: 回测报告导出增强

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-009: P-20260505-009: 持仓/交易历史持久化

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-010: PRD: ai-subscription — 键盘快捷键

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-011: PRDV3 — 家庭圈（Family Circle）

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-012: PRD: ai-subscription — RSS/Atom 智能解析增强

- **Project**: future-little-leaders
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260506-010: 

- **Project**: pixel-pal-web
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

### ACTIVE

#### P-20260517-005: PRD: Tower-Baby-Guard V6 — 音效系统 + BOSS战强化

- **Project**: tower-baby-guard
- **Owner**: 小墨
- **Stage**: DELIVERED — audio system + BOSS health bar + phases + screen shake
- **Acceptance**: delivered
- **Last Update**: 2026-05-17
- **PRD Confirmation**: auto-approved (unattended mode)
- **Technical Expectations**: auto-approved (unattended mode)
- **Notes**: 借鉴 nanobot 音效+BOSS战 | 无人值守模式 | Godot 4 GDScript | DELIVERED + PUSHED

#### P-20260517-006: PRD: Tower-Baby-Guard V7 — 多关卡世界系统

- **Project**: tower-baby-guard
- **Owner**: 小墨
- **Stage**: DELIVERED — world select + 9 scenes + world progression + 3 world mechanics
- **Acceptance**: delivered
- **Last Update**: 2026-05-17
- **PRD Confirmation**: auto-approved (unattended mode)
- **Technical Expectations**: auto-approved (unattended mode)
- **Notes**: 借鉴 trading-agents 多世界扩展 | 无人值守模式 | Godot 4 GDScript | DELIVERED + PUSHED

#### P-20260517-007: PRD: Tower-Baby-Guard V8 — 天气系统 + 动态环境

- **Project**: tower-baby-guard
- **Owner**: 小墨
- **Stage**: DELIVERED — 5 weather types + dynamic particles + weather mechanics
- **Acceptance**: delivered
- **Last Update**: 2026-05-17
- **PRD Confirmation**: auto-approved (unattended mode)
- **Technical Expectations**: auto-approved (unattended mode)
- **Notes**: 借鉴 trading-agents 动态天气 | 无人值守模式 | Godot 4 GDScript | DELIVERED + PUSHED

#### P-20260517-008: PRD: Tower-Baby-Guard V9 — 无尽模式 + 每日挑战 + 录像回放

- **Project**: tower-baby-guard
- **Owner**: 小墨
- **Stage**: DELIVERED — endless waves + daily challenge + replay system
- **Acceptance**: delivered
- **Last Update**: 2026-05-17
- **PRD Confirmation**: auto-approved (unattended mode)
- **Technical Expectations**: auto-approved (unattended mode)
- **Notes**: 借鉴 nanobot roguelike+录像 | 无人值守模式 | Godot 4 GDScript | DELIVERED + PUSHED

#### P-20260517-004: PRD: Tower-Baby-Guard V5 — YAML Level Editor + Story System

- **Project**: tower-baby-guard
- **Owner**: 小墨
- **Stage**: DELIVERED — level select + 3 JSON levels + story vignettes + special events
- **Acceptance**: delivered
- **Last Update**: 2026-05-17
- **PRD Confirmation**: auto-approved (unattended mode)
- **Technical Expectations**: auto-approved (unattended mode)
- **Notes**: 借鉴 ChatDev YAML workflow | 无人值守模式 | Godot 4 GDScript | DELIVERED + PUSHED

#### P-20260517-003: PRD: Tower-Baby-Guard V4 — Persistence + Achievement System

#### P-20260517-002: PRD: Tower-Baby-Guard V3 — Tower Upgrade System

- **Project**: tower-baby-guard
- **Owner**: 小墨
- **Stage**: DELIVERED — 15 upgrades (3 per tower) + upgrade panel + sell value
- **Acceptance**: delivered
- **Last Update**: 2026-05-17
- **PRD Confirmation**: auto-approved (unattended mode)
- **Technical Expectations**: auto-approved (unattended mode)
- **Notes**: 借鉴 nanobot 技能市场模式 | 无人值守模式 | Godot 4 GDScript | DELIVERED + PUSHED

#### P-20260517-001: PRD: Tower-Baby-Guard V2 — Tower Collaboration System

- **Project**: tower-baby-guard
- **Owner**: 小墨
- **Stage**: DELIVERED — 8 combos implemented + alliance system + combo meter + alliance range UI
- **Acceptance**: delivered
- **Last Update**: 2026-05-17
- **PRD Confirmation**: auto-approved (unattended mode)
- **Technical Expectations**: auto-approved (unattended mode)
- **Notes**: 借鉴 trading-agents 多智能体协作架构 | 无人值守模式 | Godot 4 GDScript | DELIVERED + PUSHED

#### P-20250416-001:

- **Project**: todolist
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250416-002: 

- **Project**: game-1024
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250416-003: PRD: React Native 安卓计算器

- **Project**: calculator-app
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-04-16

#### P-20250417-001: 

- **Project**: prj-proposals-manager
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250417-002: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250418-001: 

- **Project**: monopoly3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250418-003: 

- **Project**: harness-desktop
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250418-004: 

- **Project**: future-little-leaders
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250418-005: 

- **Project**: todo-app
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250419-002: 

- **Project**: tank-battle
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250420-001: 

- **Project**: snake-battle
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250421-002: 

- **Project**: ai-novel-assistant
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20250421-003: 

- **Project**: personalClaw
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260412-008: 

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260412-009: 

- **Project**: ai-stock-simulation
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260419-003: 别踩白块（Web + PWA）— 需求概述

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-04-19

#### P-20260419-004: 

- **Project**: TradingAgents-CN
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260424-001: 

- **Project**: OpenMAIC
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260424-002: P-20260424-002: Hermes 协作服务器消息转发机制重构

- **Project**: hermes-agent-collab
- **Owner**: 
- **Stage**: | 内容 | 交付物 |
- **Acceptance**: 
- **Last Update**: 2026-04-24

#### P-20260430-003: P-20260430-003: 3D打地鼠 V4 — 无尽模式

- **Project**: whack-a-mole-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-04-30

#### P-20260430-004: P-20260430-004: 3D打地鼠 V4 — 成就系统

- **Project**: whack-a-mole-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-04-30

#### P-20260430-005: P-20260430-005: 3D打地鼠 V4 — 音效+震动反馈

- **Project**: whack-a-mole-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-04-30

#### P-20260430-006: 

- **Project**: tower-baby-guard
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260430-007: 

- **Project**: doc-editor
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260502-002: Intake — P-20260502-002

- **Project**: ai-novel-assistant
- **Owner**: 
- **Stage**: | 交付物 |
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-005: PRD - 3D飞行棋 AI对战 迭代功能

- **Project**: flight-chess-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-009: PRD — P-20260502-009

- **Project**: game-1024
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-010: PRD — P-20260502-010

- **Project**: game-1024
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-011: PRD — P-20260502-011

- **Project**: game-1024
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-012: PRD — P-20260502-012

- **Project**: todolist
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-013: PRD — P-20260502-013

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-014: 

- **Project**: todolist
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260502-015: P-20260502-015: DBG卡牌游戏 V7 — 敌人与Boss扩充

- **Project**: todolist
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-016: P-20260502-016: DBG卡牌游戏 V8 — 卡牌升级系统

- **Project**: todolist
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260502-019: 

- **Project**: todolist
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260503-001: P-20260503-001: DBG卡牌游戏 V9 — 成就系统

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260503-002: P-20260503-002: DBG卡牌游戏 V10 — 章节扩展

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-02

#### P-20260503-003: P-20260503-003: DBG卡牌游戏 V11 — 更多遗物效果

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-004: P-20260503-004: DBG卡牌游戏 V12 — 音效与特效

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-005: P-20260503-005: DBG卡牌游戏 V13 — 牌组构建核心（Critical Bugfix）

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-006: P-20260503-006: DBG卡牌游戏 V14 — 卡牌商店重做

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-007: P-20260503-007: DBG卡牌游戏 V15 — 更多卡牌

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-008: P-20260503-008: DBG卡牌游戏 V16 — 卡组辅助系统

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-009: PRD — DBG卡牌游戏 V17 — 牌组管理系统 + 卡牌升级扩展

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-010: PRD — DBG卡牌游戏 V18 — 随机事件系统

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-011: PRD — DBG卡牌游戏 V19 — 多槽位存档系统

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-012: PRD — DBG卡牌游戏 V20 — 章节扩展 + Boss 战设计

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-013: PRD — DBG卡牌游戏 V21 — 移动端适配 + 触屏支持

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-014: PRD — DBG卡牌游戏 V22 — 音效与音乐扩展

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-015: PRD — DBG卡牌游戏 V23 — PWA 应用化

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-016: PRD — DBG卡牌游戏 V24 — 成就系统

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-017: PRD — DBG卡牌游戏 V25 — 宠物/同伴系统

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-018: PRD — P-20260503-018: prj-proposals-manager V3 — 甘特图视图

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: | 交付物 | 说明 |
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-019: PRD — P-20260503-019: prj-proposals-manager V3 — 数据统计仪表板

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: | 交付物 | 说明 |
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-021: PRD: DBG卡牌游戏 V39 — Combo系统 + BossRush + 宠物技能树

- **Project**: snake-battle
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-022: P-20260503-022 PRD — 战斗奖励系统 + 卡牌升级

- **Project**: snake-battle
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-023: 

- **Project**: snake-battle
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260503-024: 

- **Project**: todolist
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260503-025: P-20260503-025: PixelPal V2 — 记忆持久化 + Companion 人格层

- **Project**: todolist
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-026: PRD: 技能版本管理系统

- **Project**: prj-proposals-manager
- **Owner**: 
- **Stage**: 
- **PRD**: workspace-pm/proposals/PRJ-20260417-001/P-20260503-026.md
- **Project Path**: /home/hermes/.hermes/proposals/workspace-dev/proposals/prj-proposals-manager
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260503-027: PRD: creative-drawing-board V4 — 学习记录 + 贴纸编辑

- **Project**: todolist
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-03

#### P-20260504-004: P-20260504-004: PixelPal V16 — 场景模式/自动化

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-009: PRD: ai-subscription — 阅读列表 + 稍后读

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260517-005: PRD: 卡牌DBG V22 — 多策略敌人AI辩论系统

- **Project**: card-game-prototype
- **Owner**: 小墨
- **Stage**: approved_for_dev
- **Acceptance**: 
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-005-prd.md
- **Direction**: A
- **Mode**: 无人值守模式

#### P-20260504-010: P-20260504-010 PRD: 遗物系统扩展

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-011: P-20260504-011 PRD: 卡牌升级系统扩展

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-012: P-20260504-012 PRD: UI优化 — 卡牌动画、战斗特效、界面布局改进

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-013: P-20260504-013 PRD: 章节Boss战后商店

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-014: P-20260504-014 PRD: 战斗后牌组构建系统

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-015: P-20260504-015 PRD: 卡牌融合系统

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-016: P-20260504-016 PRD: 宠物进化系统

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-018: P-20260504-018 PRD: 流派套装效果系统

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-062: PRD: creative-drawing-board V39 — 动画书

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-063: PRD: creative-drawing-board V40 — GIF 导出

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-064: PRD: creative-drawing-board V41 — 故事板时间轴

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-065: PRD: creative-drawing-board V42 — 预设动画模板

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-066: PRD: creative-drawing-board V43 — 更多动物动画模板

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-067: PRD: creative-drawing-board V44 — 配音变声特效

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-04

#### P-20260504-068: PRD: creative-drawing-board V45 — 模板分类浏览

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260504-069: PRD: creative-drawing-board V46 — 背景音乐叠加

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260504-3001: 

- **Project**: ai-novel-assistant
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3024: 

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3027: 

- **Project**: dont-step-white
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3035: 

- **Project**: flight-chess-3d
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3046: 

- **Project**: TradingAgents-CN
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260504-3055: 

- **Project**: hermes-agent-collab
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260505-001: PRD: Monopoly3D 核心体验打磨

- **Project**: ai-stock-simulation
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-002: PRD: ai-stock-simulation 强化回测系统

- **Project**: ai-stock-simulation
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-003: PRD: Monopoly3D AI 对手智能化

- **Project**: ai-stock-simulation
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-004: PRD: Monopoly3D 完整资源包

- **Project**: ai-stock-simulation
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-013: PRD: ai-subscription — 订阅源批量管理

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-014: PRD: android-hello V2.1.0 — 单元测试

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-015: PRD: android-hello V2.2.0 — Compose Navigation 多页面

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-016: PRD: android-hello V2.3.0 — Room 数据持久化

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-017: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260505-078: P-20260505-078: creative-drawing-board V55 — 图层管理优化

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260506-001: PRD: PixelPal V20 — 智能体(Agent)框架

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: | 内容 | 交付物 |
- **Acceptance**: 
- **Last Update**: 2026-05-06

#### P-20260506-002: PRD: PixelPal V21 情感计算引擎 v2

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-06

#### P-20260506-003: Intake: PixelPal V22 — 深度个性化学习系统

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: | 内容 | 验收方式 |
- **Acceptance**: 
- **Last Update**: 2026-05-06

#### P-20260506-004: P-20260506-004 真实K线数据对接 PRD

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-06

#### P-20260506-005: P-20260506-005 回测报告导出增强 PRD

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-06

#### P-20260506-006: P-20260506-006 持仓/交易历史持久化 PRD

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-06

#### P-20260506-007: PRD: ai-subscription API 开放

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-06

#### P-20260506-008: PRD: ai-subscription 智能摘要增强

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-06

#### P-20260506-009: PRD: ai-subscription 自动化工作流

- **Project**: ai-subscription
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-06

#### P-20260506-018: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260506-019: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260506-020: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260506-021: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260506-022: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260506-023: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260506-079: P-20260506-079: creative-drawing-board V56 — 更多背景纹理/图案

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260506-080: P-20260506-080: creative-drawing-board V57 — 作品标签/分类系统

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260506-081: P-20260506-081: creative-drawing-board V58 — 橡皮擦增强（局部擦除/撤销）

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260506-082: P-20260506-082: creative-drawing-board V59 — 更多导出格式（PDF/SVG）

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260506-083: P-20260506-083: creative-drawing-board V60 — 撤销/重做增强（历史记录面板）

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260506-084: P-20260506-084: creative-drawing-board V61 — 模板搜索/排序功能

- **Project**: creative-drawing-board
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260507-001: PRD: AI Novel Assistant 结构化大纲系统

- **Project**: pixel-pal-web
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-07

#### P-20260507-002: P-20260507-002: 真实K线数据 - Yahoo Finance API 对接

- **Project**: pixel-pal-web
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-07

#### P-20260507-003: PRD: PixelPal V42 — 协作系统深度化

- **Project**: pixel-pal-web
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-07

#### P-20260507-024: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260507-025: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260507-026: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260507-027: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260507-028: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260507-029: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260507-030: 

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260508-003: P-20260508-003: AI对手自进化引擎

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260508-005: P-20260508-005: 多人模式增强 — 实时对战/观战/录像

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260508-006: P-20260508-006: 新功能构思

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260509-001: P6: 轨迹系统 (Trajectory System)

- **Project**: trading-agents-design
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260509-003: PRD: android-hello V3.10.0 深色模式优化

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260509-004: PRD: 策略市场/跟单系统

- **Project**: android-hello
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260509-008: PRD: android-hello V3.16.0 性能优化

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-10

#### P-20260509-009: P-20260509-009: 地图编辑器升级 — 可视化编辑 + 特殊格子

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260509-010: 

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260509-011: PRD: 策略进化 ↔ 模拟交易联动

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260509-012: 

- **Project**: card-game-prototype
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260509-024: P-20260509-024 PRD — 持仓分析面板（Position Analytics）

- **Project**: ai-stock-simulation
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260511-001: 

- **Project**: astrbot-design
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260511-002: 

- **Project**: autoagent-design
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260511-003: 

- **Project**: bmad-method-design
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260511-004: 

- **Project**: chatdev-design
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260511-005: 

- **Project**: deepcode-design
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260511-006: 

- **Project**: deepseek-coder-design
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260513-003: P-20260513-003: GitHub Repo Manager — 定时拉取 + 自动构建部署系统

- **Project**: github-repo-manager
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-13

### ARCHIVED

#### P-20260504-070: PRD: creative-drawing-board V47 — 模板预览动画

- **Project**: temple-run
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-077: P-20260505-077: creative-drawing-board V54 — 社交分享

- **Project**: prj-proposals-manager
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-05

#### P-20260505-081: 

- **Project**: temple-run
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 

#### P-20260507-006: P-20260507-006: AI Creator H5 - API额度管理

- **Project**: ai-creator-h5
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-07

#### P-20260508-001: P-20260508-001: 玩家数据持久化 & 跨会话成长系统

- **Project**: ai-creator-h5
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-08

#### P-20260516-001: ai-creator-h5 V2 - 视觉设计升级

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **Notes**: 暗色主题 + 橙青品牌色渐变 + glass-morphism + 卡片动效，部署至 https://yeluo45.github.io/ai-creator-h5/

#### P-20260516-002: ai-creator-h5 V3 - 架构增强（Zustand + 离线缓存）

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **Notes**: Zustand 统一状态管理 + persist middleware 替代散装 localStorage + 离线状态检测 + 历史记录持久化。Commit 04adadd，部署 https://yeluo45.github.io/ai-creator-h5/

#### P-20260516-003: ai-creator-h5 V4 - 多模型选择 + 提示词模板库

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **Notes**: 模型选择器（图片image-01/02，音乐music-2.6/02，语音speech-01/02）+ 提示词模板库（3类各3模板）+ Tab过滤。Commit 7222b79，部署 https://yeluo45.github.io/ai-creator-h5/

#### P-20260516-004: ai-creator-h5 V5 - 用户偏好记忆 + 模型使用统计

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **Notes**: lastSelectedModel 偏好持久化 + modelUsage 统计 + "我的"页统计展示 + 生成成功自动 increment。Commit bb196a1，部署 https://yeluo45.github.io/ai-creator-h5/

#### P-20260516-005: ai-creator-h5 V6 - API额度管理 + 成本统计

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **Notes**: MODEL_COST 配置 + bar 可视化 + 累计消耗估算。Commit 1dcde2a，部署 https://yeluo45.github.io/ai-creator-h5/

#### P-20260516-006: ai-creator-h5 V7 - 收藏夹/专辑管理

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **Notes**: albums/favorites 数据模型 + 收藏弹窗 + 专辑 CRUD UI + 专辑展开查看收藏。Commit 137748d7，部署 https://yeluo45.github.io/ai-creator-h5/

#### P-20260516-007: ai-creator-h5 V8 - 批量操作 + 社区分享

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **Notes**: 批量选择/删除/收藏 + 分享按钮（复制base64到剪贴板）。Commit 05a2242，部署 https://yeluo45.github.io/ai-creator-h5/

#### P-20260508-002: P-20260508-002: 创意工坊 & 社区生态

- **Project**: ai-creator-h5
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-09

#### P-20260512-003: PRD: AI智能工作流引擎

- **Project**: cultivation-simulator
- **Owner**: 
- **Stage**: 
- **Acceptance**: 
- **Last Update**: 2026-05-12

#### P-20260516-001: PRD: 多渠道消息总线重构 (V101)

- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/pixel-pal-web/P-20260516-001-prd.md
- **Reference**: nanobot-design (HKUDS/nanobot, ~3,510 lines, multi-channel AI assistant)

#### P-20260516-002: PRD: 插件化订阅源架构（PluginRegistry + PluginMarketplace）

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-001-prd.md
- **Reference**: nanobot-design (tool system), astrbot (plugin-marketplace with Ed25519 signature)
- **Notes**: c55cc672 - 9 files, 1499 insertions. Build: 22.79s. Zero new deps (Web Crypto API).

#### P-20260516-003: PRD: creative-drawing-board V54 — 本地持久化 + 版本历史

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-16
- **Last Update**: 2026-05-16
- **Dev Commit**: 7cc2c23 (1071行)
- **Lines**: 36,699 → 37,770 (+1,071)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=54
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-003-prd.md

#### P-20260516-004: ai-novel-assistant V31 — 离线优先存储 + 版本历史

- **Project**: ai-novel-assistant
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: pending
- **Last Update**: 2026-05-16
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-004-prd.md
- **Reference**: thunderbolt-design (offline-first), ChapterVersion model (existing)
- **Unattended**: true

#### P-20260516-005: ai-novel-assistant V32 — 写作工具系统生态

- **Project**: ai-novel-assistant
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: pending
- **Last Update**: 2026-05-16
- **Reference**: chatdev-design (role system + task complexity routing)
- **Unattended**: true
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-005-prd.md

#### P-20260516-006: ai-novel-assistant V33 — AI 角色专业化分工

- **Project**: ai-novel-assistant
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: pending
- **Last Update**: 2026-05-16
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-006-prd.md
- **Reference**: chatdev-design (role system + task complexity routing)
- **Unattended**: true

#### P-20260516-003: PRD: 插件市场后端服务

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-002-prd.md
- **Reference**: 前置: P-20260516-002 插件化订阅源架构
- **Notes**: ab2670be - 18 files, 3050 insertions. 前端构建 22.42s，后端 tsc 编译通过。无人值守模式完成。

#### P-20260516-005: PRD: creative-drawing-board V55 — 可扩展工具/印章系统

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: approved_for_dev
- **Acceptance**: pending
- **Last Update**: 2026-05-16
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-005-prd.md
- **Reference**: nanobot-design (tool system + PluginRegistry), thunderbolt-design (component registry)
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true

#### P-20260517-001: PRD: 多渠道 Adapter 扩展 — Telegram + Discord (V102)

- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/pixel-pal-web/P-20260516-002-prd.md
- **Reference**: nanobot-design (multi-channel: Telegram/Discord)

---

- **Proposal ID**: P-20260517-002
- **Title**: Plan Review Gate
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/pixel-pal-web/P-20260517-002-prd.md
- **Reference**: deepcode-design/workflow-architecture.md §3.2 PlanReviewRuntime

---

- **Proposal ID**: P-20260518-001
- **Title**: Loop Detection System
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/pixel-pal-web/P-20260518-001-prd.md
- **Reference**: nanobot/nanobot/agent/loop.py (max_iterations=20)
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
|- **Unattended**: true
|

---

- **Proposal ID**: P-20260518-002
- **Title**: Checkpoint + Progress Tracker
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/pixel-pal-web/P-20260518-002-prd.md
- **Reference**: deepcode-design/workflow-architecture.md §3.3 PlanningCheckpointCallback

#### P-20260518-003: Provider 极速接入

- **Proposal ID**: P-20260518-003
- **Title**: Provider 极速接入
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/pixel-pal-web/P-20260518-003-prd.md
- **Reference**: nanobot README "adding a new LLM provider now takes just 2 simple steps"
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true

|#### P-20260519-001: Memory Persistence V2

- **Proposal ID**: P-20260519-001
- **Title**: Memory Persistence V2
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-19
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/pixel-pal-web/P-20260519-001-prd.md
- **Reference**: nanobot memory store pattern + V105 CheckpointManager
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true

#### P-20260519-002: Skill Chaining

- **Proposal ID**: P-20260519-002
- **Title**: Skill Chaining
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-19
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/pixel-pal-web/P-20260519-002-prd.md
- **Reference**: nanobot skill framework pattern
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true


#### P-20260517-003: PRD: doc-editor V2 — 多 Agent 文档协作系统 + 无人值守模式
|
|- **Project**: doc-editor
|- **Owner**: 小墨
|- **Stage**: approved_for_dev
|- **Acceptance**: pending
|- **Last Update**: 2026-05-17
|- **PRD Path**: /home/hermes/.hermes/proposals/PRJ-20260517-003-doc-editor-v2-multi-agent.md
|- **Reference**: trading-agents-design (13 Agent 协作), nanobot-design (MessageBus + AgentLoop)
|- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
|- **Unattended**: true
|
|#### P-20260516-004: PRD: 离线优先 + 多设备同步

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-16
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-003-prd.md
- **Reference**: thunderbolt (offline-first + PowerSync), 前置: P-20260516-002
- **Notes**: 1bdead4f - 8 files, 1293 insertions. 前端构建 21.83s。SyncEngine + OfflineQueue + GitHub Gist适配器。无人值守模式完成。

#### P-20260516-006: PRD: creative-drawing-board V56 — 家长控制台（使用统计/作品管理）

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-16
- **Last Update**: 2026-05-16
- **Dev Commit**: 735a51f (949行)
- **Lines**: 38,086 → 39,035 (+949)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=56
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-006-prd.md
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true

#### P-20260516-007: PRD: creative-drawing-board V57 — AI 辅助绘画增强

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-16
- **Last Update**: 2026-05-16
- **Dev Commit**: 64e0427 (对称辅助已存在，笔画补全/智能填心见V58)
- **Lines**: 39,035 (行数未变，代码已存在于早期版本)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=57
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260516-007-prd.md
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true

#### P-20260517-002: PRD: creative-drawing-board V58 — 笔画补全 + 智能填色

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-17
- **Last Update**: 2026-05-17
- **Dev Commit**: cde4999 (285行)
- **Lines**: 39,035 → 39,318 (+283)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=58
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-001-prd.md
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true

#### P-20260517-003: PRD: creative-drawing-board V59 — 协作绘画（实时同步）

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: approved_for_dev
- **Acceptance**: pending
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-002-prd.md
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true

#### P-20260517-004: PRD: MCP Client 集成 — 扩展 AI 工具生态

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-002-prd.md
- **Reference**: nanobot-design (MCP tool system), thunderbolt-design (扩展工具生态)
- **Notes**: 62f37169 - 7 files, 1451 insertions. 构建 26.91s。零新增依赖，自实现 MCP JSON-RPC over stdio。无人值守完成。

#### P-20260517-005: PRD: MCP 工具生态扩展 — 接入真实 MCP 服务器

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-003-prd.md
- **Reference**: 前置: P-20260517-004 MCP Client 核心
- **Notes**: a0e4e737 - MCP 服务器模板（GitHub/Brave Search/Slack/Filesystem）+ 工具调用历史。构建 29.69s。无人值守完成。

#### P-20260517-006: PRD: AI 原生工具调用 — MCP 工具增强内容分析

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-006-prd.md
- **Reference**: 前置: P-20260517-005 MCP 工具生态扩展
- **Notes**: b06a2fbf - MCP AI 适配器（callMCPTool/enhanceWithMCP）+ GitHub/Brave Search 增强 + MCPEnhancePanel + GitHub Trending 推荐。构建 29.44s。无人值守完成。

#### P-20260517-012: PRD: ai-subscription PWA 增强 — 桌面通知 + 离线能力 + 快捷方式

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-012-prd.md
- **Reference**: 前置: P-20260517-011 安全加固
- **Notes**: d2425dfa - manifest.json/icons(192/512) + notify()桌面通知 + isOnline()离线检测 + InstallBanner(beforeinstallprompt)。构建 4.24s。无人值守完成。

#### P-20260517-011: PRD: ai-subscription 安全加固 — E2E 加密 + MCP 鉴权 + 日志脱敏

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-011-prd.md
- **Reference**: 前置: P-20260517-010 性能优化
- **Notes**: ed59fe62 - AES-GCM E2E加密(cryptoService) + MCP Bearer Token鉴权(Authorization头) + 日志脱敏(sanitize.ts) + secureCopy(30s清空)。构建 35.66s。无人值守完成。

#### P-20260517-010: PRD: ai-subscription 性能优化 — Bundle 拆包 + 懒加载 + Service Worker 缓存

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-010-prd.md
- **Reference**: 前置: P-20260517-009 多语言 i18n
- **Notes**: 2faec6ad - manualChunks拆包(vendor-react/ai-sdk/antd/utils) + React.lazy懒加载MCPServerPanel/AnalyticsDashboard + 自定义sw.js缓存。构建 29.70s。无人值守完成。

#### P-20260517-009: PRD: ai-subscription 多语言 i18n 完善 — zh/en 翻译补全 + 语言检测

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-009-prd.md
- **Reference**: 前置: P-20260517-008 数据分析增强
- **Notes**: 37ef19e7 - zh.json/en.json完整翻译 + LanguageSwitcher + I18nProvider + useTranslation hook。构建 19.84s。无人值守完成。

#### P-20260517-008: PRD: ai-subscription 数据分析增强 — 订阅源健康度 + 阅读趋势可视化

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-008-prd.md
- **Reference**: 前置: P-20260517-007 工作流自动化
- **Notes**: ad84cd81 - AnalyticsDashboard + TrendChart(纯SVG) + analytics服务。构建 21.79s。无人值守完成。

#### P-20260517-007: PRD: 高级工作流自动化 — 条件触发器 + Webhook 事件驱动

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-007-prd.md
- **Reference**: 前置: P-20260517-006 MCP AI 工具调用
- **Notes**: 627d30b8 - 工作流引擎核心（types/engine/executor/scheduler）+ Webhook接收端点 + WorkflowListPanel。构建 24.68s。无人值守完成。

#### P-20260517-003: PRD: creative-drawing-board V59 — 协作绘画（实时同步）

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-17
- **Last Update**: 2026-05-17
- **Dev Commit**: 82ff30e (829行)
- **Lines**: 39,318 → 40,147 (+829)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=59
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-002-prd.md
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true

#### P-20260517-005: PRD: creative-drawing-board V60 — 云同步（账号体系）

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-17
- **Last Update**: 2026-05-17
- **Dev Commit**: 9e4ae16 (~920行)
- **Lines**: 40,147 → 41,066 (+919)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=60
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-003-prd.md
- **Notes**: 无人值守模式 - 自动确认+自动验收+自动迭代
- **Unattended**: true

#### P-20260517-006: PRD: creative-drawing-board V61 — Tauri 多平台打包

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-17
- **Last Update**: 2026-05-17
- **Dev Commit**: e5b4575 (15 files, +1,447行)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=61
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-006-prd.md
- **Notes**: Tauri v2 脚手架完成 - src-tauri/Rust项目/tauri.conf.json/Cargo配置/原生命令(fs/dialog/notification/clipboard)
- **Unattended**: true

#### P-20260517-007: PRD: creative-drawing-board V62 — Tauri 原生集成

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-17
- **Last Update**: 2026-05-17
- **Dev Commit**: de12c08 (+101行)
- **Lines**: 41,066 → 41,167 (+101)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=62
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-007-prd.md
- **Notes**: Tauri原生集成 - isTauri检测/tauriSaveFile/tauriCopyImage/tauriNotify/同步完成系统通知/复制图片按钮
- **Unattended**: true

#### P-20260517-008: PRD: creative-drawing-board V63 — 主题商店 + 高级画笔

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-17
- **Last Update**: 2026-05-17
- **Dev Commit**: 61d2ee5 (+352行)
- **Lines**: 41,167 → 41,519 (+352)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=63
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-008-prd.md
- **Notes**: 主题商店+高级画笔 - 6主题(3免费3付费)/6画笔(3免费3付费)/购买确认弹窗/主题应用/画笔切换
- **Unattended**: true

#### P-20260517-009: PRD: creative-drawing-board V64 — 动画帧编辑

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-17
- **Last Update**: 2026-05-17
- **Dev Commit**: 809c23a (+397行)
- **Lines**: 41,519 → 41,916 (+397)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=64
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-009-prd.md
- **Notes**: 动画帧编辑 - 时间轴/播放控制/FPS调节/帧增删复制/导出PNG序列/底部固定按钮
- **Unattended**: true

#### P-20260517-010: PRD: creative-drawing-board V65 — 社交分享

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-17
- **Last Update**: 2026-05-17
- **Dev Commit**: 66771ed (+280行)
- **Lines**: 41,916 → 42,196 (+280)
- **Deployed**: https://yeluo45.github.io/creative-drawing-board/?v=65
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-010-prd.md
- **Notes**: 社交分享 - 二维码/分享链接(URL编码)/Twitter/Facebook/微信二维码/加载分享作品
- **Unattended**: true

#### P-20260517-011: PRD: creative-drawing-board V66 — Tauri 构建发布

#### P-20260519-003: V109 More Channel Adapters

- **Proposal ID**: P-20260519-003
- **Title**: V109 More Channel Adapters
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-19


#### P-20260519-004: V110 Channel Adapter Phase 2

- **Proposal ID**: P-20260519-004
- **Title**: V110 Channel Adapter Phase 2
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-19


#### P-20260519-005: V111 More Channel Adapters 2

- **Proposal ID**: P-20260519-005
- **Title**: V111 More Channel Adapters 2
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-19


#### P-20260519-006: V112 Channel Adapter Phase 2-2

- **Proposal ID**: P-20260519-006
- **Title**: V112 Channel Adapter Phase 2-2
- **Type**: feature
- **Project**: pixel-pal-web
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-19


#### P-20260517-011: PRD: Tower-Baby-Guard V12 — 好友借租 + 商店扭蛋系统

- **Project**: tower-baby-guard
- **Owner**: 小墨
- **Stage**: DELIVERED — friend rental + gacha shop system
- **Acceptance**: delivered
- **Last Update**: 2026-05-17
- **PRD Confirmation**: auto-approved (unattended mode)
- **Technical Expectations**: auto-approved (unattended mode)
- **Notes**: 借鉴 trading-agents 协作思路 + nanobot 扭蛋 | 无人值守模式 | Godot 4 GDScript | DELIVERED + PUSHED
