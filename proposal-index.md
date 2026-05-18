# Proposal Index

Last updated: 2026-05-18

### P-20260518-001: nanobot-inspired AsyncMessageBus + Channel Adapter

- `Proposal ID`: `P-20260518-001`
- `Title`: nanobot-inspired MessageBus + Channel Adapter 架构重构
- `Owner`: 小墨
- `Current Status`: accepted
- `Project`: hermes-agent-collab
- `Source Design`: nanobot-design (Async MessageBus + Channel Adapters)
- `PRD Path`: workspace-dev/proposals/hermes-agent-collab/docs/P-20260518-001-prd.md
- `Last Update`: 2026-05-18
- `Notes`: Direction A — nanobot-inspired MessageBus refactor. AsyncMessageBus with queue (max 1000), 3x retry + dead-letter, ChannelAdapter pattern (WS/SSE/HTTP). Committed c03f776, pushed.

### P-20260518-012: future-little-leaders V10 V3 M5 Dashboard 补全 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: npm run build:h5 成功，Git commit dc2b28b9，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V10-M5-dashboard.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (dc2b28b9)
- **Features**: 积分总览; 7日收支趋势; 任务趋势柱状图; 技能树进度; 成就进度环; AI建议区块; getDashboardStatsV2

---

### P-20260518-018: future-little-leaders V16 微信小程序特定功能 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: git commit 0f121fe4, push成功; 微信分享卡片+附近发现+反馈
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V16-wx-miniprogram.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (0f121fe4)
- **Features**: wxService; locationService; wx-jssdk; share-card; nearby; feedback; share-poster

---

### P-20260518-017: future-little-leaders V15 儿童社交功能 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: git commit 48bab4e9, push成功; 朋友系统+积分赠送+组队任务+成长PK
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V15-social.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (48bab4e9)
- **Features**: friendStore; challengeStore; friendService; challengeService; 6 social pages; social components

---

### P-20260518-016: future-little-leaders V14 多语言 i18n 支持 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: git commit 4a954aa1, push成功; i18n框架+4语言+settings语言切换
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V14-i18n.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (4a954aa1)
- **Features**: i18n; zh-CN; zh-TW; en; zh-HK; settings language picker; global $t

---

### P-20260518-015: future-little-leaders V13 V4 离线同步深度集成 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: git commit 1d77bb18, push成功; initV4+SyncConflictModal+SyncStore+conflictResolver+Workers D1
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V13-v4-offline-sync-deep-integration.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (1d77bb18)
- **Features**: initV4; appInitializer; SyncConflictModal; SyncStatusBadge; syncStore; conflictResolver; Workers D1 API

---

### P-20260518-014: future-little-leaders V12 积分商城增强 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: git commit a95a9de7, push成功; 35商品+积分商城+兑换记录+排行榜
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V12-reward-shop.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (a95a9de7)
- **Features**: rewardItems(35商品); rewardStore; leaderboardStore; rewardService; reward-shop; reward-detail; exchange-records; leaderboard; LeaderboardItem; reward_items表; exchange_records表

---

### P-20260518-013: future-little-leaders V11 Flow 模板市场 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: git commit 07e3fb0c, push成功; 8 files changed, 1809 insertions(+), 10 deletions(-)
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V11-flow-template-market.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (07e3fb0c)
- **Features**: flowExporter; flowImporter; 5预设模板; flow-templates页面; scheduler服务

---

### P-20260518-010: future-little-leaders V9 成长报告 AI 总结 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: npm run build:h5 成功，Git commit 6c8335da，push 成功；SDK commit d2ed559，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V9-ai-growth-summary.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (6c8335da) + SDK main (d2ed559)
- **Features**: aiSummaryService; buildGrowthStats; 模板回退; FastAPI; AI Summary区域; ai_summary_cache表

---

### P-20260518-007: future-little-leaders V8 Python SDK + 家校互通 (Direction A)

- **Project**: future-little-leaders-sdk-python
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: pip install 成功，from fll_sdk import __version__ 输出 1.0.0，Git push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V8-python-sdk.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: main (3fbafe9)
- **Features**: FLLClient; JWT认证; Pydantic模型; WebhookServer; Cloudflare Worker占位; school_sync示例

---

### P-20260518-005: future-little-leaders V7 家庭通知中枢 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: npm run build:h5 成功，Git commit 74f58f5a，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V7-notification-hub.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (74f58f5a)
- **Features**: 12通道; SQLite持久化; Tab分组; 日期分组; 未读置顶; 渠道偏好设置; notificationStore

---

### P-20260518-002: hermes-agent-collab chatdev-inspired Agent Role System + Phase-Gated Pipeline (Direction A)

- **Project**: hermes-agent-collab
- **Owner**: 小墨
- **Stage**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: docs/P-20260518-002-prd.md
- **Git**: gh-pages (025a728)
- **Features**: AgentRole (ORCHESTRATOR/EXECUTOR/CRITIC/MONITOR/SPECIALIST); ROLE_SYSTEM_PROMPTS; TaskComplexity (SIMPLE/NORMAL/COMPLEX); OrchestrationPhase enum with can_transition_to/next_phase; Agent.system_prompt; Task.complexity/phase/phase_history; evaluate_complexity/get_next_phase helpers; TaskManager.transition_phase/advance_phase; TaskAction.phase_transition; phase-gated set_status/complete/fail/cancel

---

### P-20260518-003: future-little-leaders V6 自进化技能树/成长图谱系统 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: npm run build:h5 成功，Git commit 9753b773，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V6-skill-tree.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (9753b773)
- **Features**: 四棵树(knowledge/habit/social/creative); SVG树状图; 自进化阈值调整; 40+节点; skillTreeStore; 集成achievementStore

---

### P-20260517-035: future-little-leaders V5 可视化任务编排画布 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: npm run build:h5 成功，Git commit d14a0811，push 成功
- **Last Update**: 2026-05-17
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (d14a0811)
- **Features**: 拖拽节点画布; SVG贝塞尔连线; flowStore CRUD; flow-builder/flow-list 页面

---

### P-20260517-034: future-little-leaders V4 离线优先 + 多设备同步 (Direction A)

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: npm run build:h5 成功，Git commit face16f9，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V4-offline-sync.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (face16f9)
- **Features**: sql.js SQLite; Delta Sync Engine; E2E 加密架构; V4 PRD; 修复 add-task.vue 重复声明; 修复 family-dashboard.vue 缺少 </style>

---

Last updated: 2026-05-18

- **Project**: future-little-leaders
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: npm run build:h5 成功，Git commit face16f9，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-dev/proposals/future-little-leaders/PRD-V4-offline-sync.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: feature/hermes20260503 (face16f9)
- **Features**: sql.js SQLite; Delta Sync Engine; E2E 加密架构; V4 PRD; 修复 add-task.vue 重复声明; 修复 family-dashboard.vue 缺少 </style>

---

Last updated: 2026-05-16 23:45:00

### P-20260517-037: ai-creator-h5 API开放平台 (Direction D)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit e5fab2c，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-037-prd.md
- **Direction**: D
- **Mode**: 无人值守模式
- **Git**: 已推送 origin/main (e5fab2c)
- **Features**: API开放平台; API Key管理; 接口文档; services/apiService.js; pages/api.html

---

### P-20260517-036: ai-creator-h5 实时协作 (Direction C)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 1eff031，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-036-prd.md
- **Direction**: C
- **Mode**: 无人值守模式
- **Git**: 已推送 origin/main (1eff031)
- **Features**: 实时协作; 分享链接; 评论系统; services/collabService.js; pages/shared.html

---

### P-20260517-035: ai-creator-h5 AI角色专业化 (Direction B)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit a8f4321，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-035-prd.md
- **Direction**: B
- **Mode**: 无人值守模式
- **Git**: 已推送 origin/main (a8f4321)
- **Features**: AI角色专业化; 插画师/音乐人/配音师/设计师; services/roleService.js; pages/roles.html

---

### P-20260517-034: ai-creator-h5 创作质量评估 (Direction A)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 067933c，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-034-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 已推送 origin/main (067933c)
- **Features**: 0-100质量分; 维度评分; 优化建议; services/qualityService.js

---

### P-20260517-033: ai-creator-h5 端到端加密 (Direction F)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 7d7da2e，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-033-prd.md
- **Direction**: F
- **Mode**: 无人值守模式
- **Git**: 已推送 origin/main (7d7da2e)
- **Features**: E2E加密; AES-256-GCM; Web Crypto API; 隐私模式; services/cryptoService.js

---

### P-20260517-032: ai-creator-h5 跨平台桌面端 (Direction E)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 39295b7，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-032-prd.md
- **Direction**: E
- **Mode**: 无人值守模式
- **Git**: 已推送 origin/main (39295b7)
- **Features**: Tauri 2桌面端; src-tauri/; package.json tauri脚本

---

### P-20260517-031: ai-creator-h5 PWA离线优先增强 (Direction D)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit a1bc35b，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-031-prd.md
- **Direction**: D
- **Mode**: 无人值守模式
- **Git**: 已推送 origin/main (a1bc35b)
- **Features**: Offline-First; 离线队列; IndexedDB; 缓存管理; services/offlineQueue.js

---

### P-20260517-030: ai-creator-h5 记忆系统 (Direction C)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 984f7e6，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-030-prd.md
- **Direction**: C
- **Mode**: 无人值守模式
- **Git**: 已推送 origin/main (984f7e6)
- **Features**: Dream Memory; IndexedDB存储; 偏好分析; 智能推荐; pages/memory.html; services/memoryService.js

---

### P-20260517-029: ai-creator-h5 多渠道分享 (Direction B)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit ab247d1，push 成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-029-prd.md
- **Direction**: B
- **Mode**: 无人值守模式
- **Git**: 已推送 origin/main (ab247d1)
- **Features**: 微信/Twitter/Telegram/短链分享; pages/share.html; services/shareService.js

---

### P-20260517-028: ai-creator-h5 工具系统生态 (Direction A)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit e2c3572，构建成功
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-028-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 main 已 commit (e2c3572)
- **Features**: nanobot-design Tool System; 5内置工具; pages/tools.html; services/toolRegistry.js

---

## Active Proposals

### PENDING CONFIRMATION

#### P-20260607-001: 部署时间线

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (2306885)
- **Last Update**: 2026-06-07
- **PRD Path**: workspace-pm/proposals/P-20260607-001-prd.md
- **Direction**: B
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (2306885)
- **Features**: 甘特图可视化 / 日/周/月视图 / 统计概览 / 仓库排行 / 里程碑追踪

### PENDING CONFIRMATION

#### P-20260606-001: 部署回滚增强

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (2f478da)
- **Last Update**: 2026-06-06
- **PRD Path**: workspace-pm/proposals/P-20260606-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (2f478da)
- **Features**: 快照管理 / 两版本对比 / 一键回滚 / 回滚历史 / 影响分析

### PENDING CONFIRMATION

#### P-20260605-001: 审计日志

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (ebbc6af)
- **Last Update**: 2026-06-05
- **PRD Path**: workspace-pm/proposals/P-20260605-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (ebbc6af)
- **Features**: 操作日志 / 登录历史 / 统计概览 / CSV+JSON导出 / 变更前后对比

### PENDING CONFIRMATION

#### P-20260605-002: Compliance Report 合规报告

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (94196b3)
- **Last Update**: 2026-06-05
- **PRD Path**: workspace-pm/proposals/P-20260605-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (94196b3)
- **Views**: ComplianceReportView.vue
- **Features**: GDPR/SOC2/PCI-DSS/ISO27001报告 / 多格式导出 / 合规状态概览

### PENDING CONFIRMATION

#### P-20260605-003: Notification Center 统一通知中心

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (3fff871)
- **Last Update**: 2026-06-05
- **PRD Path**: workspace-pm/proposals/P-20260605-003-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (3fff871)
- **Views**: NotificationCenterView.vue
- **Features**: 通知聚合 / 未读数 / 快速操作 / 偏好设置 / 免打扰时段

### PENDING CONFIRMATION

#### P-20260606-001: Data Export & Report Generation 数据导出

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (2b95c9b)
- **Last Update**: 2026-06-06
- **PRD Path**: workspace-pm/proposals/P-20260606-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (2b95c9b)
- **Views**: DataExportView.vue
- **Features**: CSV/JSON/Excel导出 / 模板 / 定时任务 / 历史记录

### PENDING CONFIRMATION

#### P-20260606-002: Environment Health Matrix 环境健康矩阵

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (9ddcadb)
- **Last Update**: 2026-06-06
- **PRD Path**: workspace-pm/proposals/P-20260606-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (9ddcadb)
- **Views**: EnvironmentHealthView.vue
- **Features**: 多环境矩阵 / 五维评分 / 趋势图 / 问题汇总 / 依赖关系

### PENDING CONFIRMATION

#### P-20260607-001: Onboarding Wizard 新用户入门向导

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (ffd68b3)
- **Last Update**: 2026-06-07
- **PRD Path**: workspace-pm/proposals/P-20260607-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (ffd68b3)
- **Views**: OnboardingWizard.vue
- **Features**: 5步向导 / GitHub连接 / 仓库添加 / 环境配置 / Pipeline创建

### PENDING CONFIRMATION

#### P-20260604-001: 批量操作增强

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (20024f4)
- **Last Update**: 2026-06-04
- **PRD Path**: workspace-pm/proposals/P-20260604-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (20024f4)
- **Features**: 批量选择(多选/全选/反选) / 批量编辑/删除 / CSV导入 / 模板应用 / 导出

### PENDING CONFIRMATION

#### P-20260603-001: Webhook 可视化调试

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (1489a9c)
- **Last Update**: 2026-06-03
- **PRD Path**: workspace-pm/proposals/P-20260603-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (1489a9c)
- **Features**: 请求模拟 / 响应查看 / 响应对比 / 模板库 / cURL生成

### PENDING CONFIRMATION

#### P-20260602-001: API 密钥管理增强

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (e34d0a6)
- **Last Update**: 2026-06-02
- **PRD Path**: workspace-pm/proposals/P-20260602-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (e34d0a6)
- **Features**: 密钥轮换 / 访问日志 / 权限分级 / 过期提醒

### PENDING CONFIRMATION

#### P-20260603-002: Deployment Timeline 部署时间线

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (a888bb0)
- **Last Update**: 2026-06-03
- **PRD Path**: workspace-pm/proposals/P-20260603-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (a888bb0)
- **Views**: DeploymentTimelineView.vue
- **Features**: 部署时间线 / 趋势统计 / 环境对比 / 成功失败回滚颜色标注

### PENDING CONFIRMATION

#### P-20260604-001: Cost Analysis Dashboard 成本分析

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (5c79408)
- **Last Update**: 2026-06-04
- **PRD Path**: workspace-pm/proposals/P-20260604-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (5c79408)
- **Views**: CostAnalysisView.vue
- **Features**: 成本分解 / 趋势预测 / 仓库分布 / 环境分类 / 资源类型

### PENDING CONFIRMATION

#### P-20260604-002: Security Audit Log 安全审计

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (6f57d70)
- **Last Update**: 2026-06-04
- **PRD Path**: workspace-pm/proposals/P-20260604-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (6f57d70)
- **Views**: SecurityAuditView.vue
- **Features**: 安全事件审计 / 异常检测 / 趋势统计 / 合规报告

### PENDING CONFIRMATION

#### P-20260602-002: Repository Insights 仓库洞察

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (c2efa36)
- **Last Update**: 2026-06-02
- **PRD Path**: workspace-pm/proposals/P-20260602-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (c2efa36)
- **Views**: RepoInsightsView.vue
- **Features**: 代码质量评分 / 依赖关系图 / 热力图 / 贡献者分析 / 健康预警

### PENDING CONFIRMATION

#### P-20260601-001: 自定义工作流编排

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (6604a32)
- **Last Update**: 2026-06-01
- **PRD Path**: workspace-pm/proposals/P-20260601-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (6604a32)
- **Features**: 可视化编辑器 / 节点拖拽 / 连线 / 执行引擎 / 3内置模板

### PENDING CONFIRMATION

#### P-20260601-002: Pipeline Dependency Graph + API Keys

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (77be614)
- **Last Update**: 2026-06-01
- **PRD Path**: workspace-pm/proposals/P-20260601-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (77be614, f118b99, 304d066, 627e522)
- **Views**: PipelineGraphView.vue, WorkflowCanvasView.vue
- **Features**: 依赖图可视化 / 节点拖拽 / 连线 / API密钥管理

### PENDING CONFIRMATION

#### P-20260531-001: 国际化 (i18n)

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (38dee42)
- **Last Update**: 2026-05-31
- **PRD Path**: workspace-pm/proposals/P-20260531-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (38dee42)
- **Features**: 中英文切换 / 语言选择器 / 翻译文件

### PENDING CONFIRMATION

#### P-20260530-001: 定时任务可视化编辑器

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (8222211)
- **Last Update**: 2026-05-30
- **PRD Path**: workspace-pm/proposals/P-20260530-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (8222211)
- **Views**: SchedulerEditorView.vue
- **Features**: Cron模板 / 分步输入 / 执行历史 / 任务链

### PENDING CONFIRMATION

#### P-20260530-002: Webhook Event Simulator

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (b91ce42)
- **Last Update**: 2026-05-30
- **PRD Path**: workspace-pm/proposals/P-20260530-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (b91ce42)
- **Views**: WebhookSimulatorView.vue
- **Features**: Push/PR/Tag/Release事件模拟 / 历史记录 / 响应预览

### PENDING CONFIRMATION

#### P-20260529-001: 部署预览环境

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (d9810e0)
- **Last Update**: 2026-05-29
- **PRD Path**: workspace-pm/proposals/P-20260529-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (d9810e0)
- **Views**: PreviewEnvironmentsView.vue
- **Features**: 环境CRUD / 自动过期 / 快照管理 / 资源限制

### PENDING CONFIRMATION

#### P-20260528-002: 移动端适配

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (1b16a77)
- **Last Update**: 2026-05-28
- **PRD Path**: workspace-pm/proposals/P-20260528-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (1b16a77)
- **Features**: 响应式布局 / 底部Tab栏 / FAB / PWA manifest

### PENDING CONFIRMATION

#### P-20260528-001: AI 异常检测

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (c1e2172)
- **Last Update**: 2026-05-28
- **PRD Path**: workspace-pm/proposals/P-20260528-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (c1e2172)
- **Views**: AnomalyDetectionView.vue
- **Features**: 4种检测模型 / Critical/Warning/Info / 阈值配置 / 修复建议

### PENDING CONFIRMATION

#### P-20260527-002: GitOps 集成

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (11e6616)
- **Last Update**: 2026-05-27
- **PRD Path**: workspace-pm/proposals/P-20260527-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (11e6616)
- **Views**: GitOpsView.vue
- **Features**: 声明式配置 / YAML+JSON解析 / Webhook自动同步 / 配置历史

### PENDING CONFIRMATION

#### P-20260527-001: 通知渠道扩展

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (c014115)
- **Last Update**: 2026-05-27
- **PRD Path**: workspace-pm/proposals/P-20260527-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (c014115)
- **Views**: NotificationSettingsView.vue
- **Features**: Slack/Discord / 4内置模板 / 规则引擎 / 变量替换

### PENDING CONFIRMATION

#### P-20260527-003: Activity Timeline 活动时间线

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (ef27ca4)
- **Last Update**: 2026-05-27
- **PRD Path**: workspace-pm/proposals/P-20260527-003-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (ef27ca4)
- **Views**: ActivityTimelineView.vue
- **Features**: 仓库活跃度排行 / 操作时间线 / 事件聚合 / 统计卡片

### PENDING CONFIRMATION

#### P-20260527-004: 导入导出配置备份系统

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (6692d2b)
- **Last Update**: 2026-05-27
- **PRD Path**: workspace-pm/proposals/P-20260527-004-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (6692d2b)
- **Views**: BackupView.vue
- **Features**: 整机配置导出JSON / 选择性合并导入 / credentials加密 / 备份历史

### PENDING CONFIRMATION

#### P-20260526-002: Pipeline 模板市场

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (6a0afbb)
- **Last Update**: 2026-05-26
- **PRD Path**: workspace-pm/proposals/P-20260526-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (6a0afbb)
- **Views**: PipelineTemplatesView.vue
- **Features**: 5内置模板 / CRUD / 评分 / 一键应用到仓库

### PENDING CONFIRMATION

#### P-20260526-001: SSH 终端集成

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (6a17003)
- **Last Update**: 2026-05-26
- **PRD Path**: workspace-pm/proposals/P-20260526-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (6a17003)
- **Views**: SSHTerminalView.vue
- **Features**: SSH连接 / xterm.js终端 / 命令执行 / 密码或密钥认证

### PENDING CONFIRMATION

#### P-20260525-002: 日志聚合搜索

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (c145202)
- **Last Update**: 2026-05-25
- **PRD Path**: workspace-pm/proposals/P-20260525-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (c145202)
- **Views**: LogSearchView.vue
- **Features**: 多源聚合 / 全文搜索 / 过滤器 / 实时流 / 分页

### PENDING CONFIRMATION

#### P-20260525-001: 统计分析仪表盘

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (d8bd304)
- **Last Update**: 2026-05-25
- **PRD Path**: workspace-pm/proposals/P-20260525-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (d8bd304)
- **Views**: StatsDashboard.vue
- **Features**: 总览卡片 / 趋势图 / 分布图 / 仓库排行 / 正在运行

### PENDING CONFIRMATION

#### P-20260525-002: 日志聚合搜索

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (c145202)
- **Last Update**: 2026-05-25
- **PRD Path**: workspace-pm/proposals/P-20260525-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (c145202)
- **Views**: LogSearchView.vue
- **Router**: /logs/search
- **API**:
  - GET /api/logs/search — 多源搜索
  - GET /api/logs/stats — 日志统计
  - GET /api/logs/stream/:repoId — SSE实时流
- **Features**: 多源搜索 / 过滤器 / 实时流 / 分页

### DELIVERED

#### P-20260525-001: 统计分析仪表盘

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (d8bd304)
- **Last Update**: 2026-05-25
- **PRD Path**: workspace-pm/proposals/P-20260525-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (d8bd304)
- **Views**: StatsDashboard.vue
- **Router**: /stats
- **API**:
  - GET /api/stats/overview — 总览统计
  - GET /api/stats/pipeline-trend — Pipeline趋势
  - GET /api/stats/deploy-trend — 部署趋势
  - GET /api/stats/repo-ranking — 仓库排行
  - GET /api/stats/active-runs — 正在运行
- **Features**: 总览卡片 / 趋势图 / 分布图 / 仓库排行 / 正在运行

### PENDING CONFIRMATION

#### P-20260524-002: 多环境配置

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (fd01602)
- **Last Update**: 2026-05-24
- **PRD Path**: workspace-pm/proposals/P-20260524-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (fd01602)
- **Views**: EnvConfigView.vue
- **Features**: 环境CRUD / 变量管理 / 切换active / 敏感加密 / ${VAR}解析

### PENDING CONFIRMATION

#### P-20260524-001: Webhook 触发记录

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (ac3300b)
- **Last Update**: 2026-05-24
- **PRD Path**: workspace-pm/proposals/P-20260524-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (ac3300b)
- **Views**: WebhookEventsLog.vue
- **Features**: 事件列表 / 按仓库/类型/状态筛选 / 详情弹窗 / 统计面板

### PENDING CONFIRMATION

#### P-20260523-002: 凭证安全管理

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (05d2eaf)
- **Last Update**: 2026-05-23
- **PRD Path**: workspace-pm/proposals/P-20260523-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (05d2eaf)
- **Views**: CredentialsView.vue
- **Features**: AES-256-GCM加密 / CRUD / 按仓配置 / 测试验证

### PENDING CONFIRMATION

#### P-20260523-001: 部署回滚 UI

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (86c7a76)
- **Last Update**: 2026-05-23
- **PRD Path**: workspace-pm/proposals/P-20260523-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (86c7a76)
- **Views**: RollbackView.vue
- **Features**: 目标选择 / 快照列表 / 一键回滚 / 二次确认 / 回滚历史

### PENDING CONFIRMATION

#### P-20260522-002: 仓库分组增强

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (220f1df)
- **Last Update**: 2026-05-22
- **PRD Path**: workspace-pm/proposals/P-20260522-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (220f1df)
- **Views**: GroupManager.vue
- **API**:
  - GET/POST /api/groups — 分组CRUD
  - GET /api/groups/:id — 分组详情(含成员)
  - PUT/DELETE /api/groups/:id — 更新/删除
  - PUT /api/groups/reorder — 拖拽排序
  - POST /api/groups/:id/batch-action — 组级别批量操作
- **Tables**: groups (新增description/last_activity字段)

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

### DELIVERED

#### P-20260522-002: 仓库分组增强

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (220f1df)
- **Last Update**: 2026-05-22
- **PRD Path**: workspace-pm/proposals/P-20260522-002-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (220f1df)
- **Views**: GroupManager.vue
- **Router**: /groups
- **API**:
  - GET/POST /api/groups — 列表/创建
  - GET /api/groups/:id — 分组详情(含成员)
  - PUT /api/groups/:id — 更新分组
  - DELETE /api/groups/:id — 删除分组
  - PUT /api/groups/reorder — 拖拽排序
  - POST /api/groups/:id/repos — 添加仓库到分组
  - DELETE /api/groups/:id/repos/:repoId — 从分组移除
  - POST /api/groups/:id/batch-action — 组级别批量操作
- **Tables**: groups (新增description/last_activity字段)
- **Files**:
  - server/db/init.js: groups表字段扩展
  - server/routes/groups.js: API路由
  - server/services/groupsService.js: 业务逻辑
  - src/views/GroupManager.vue: 分组管理UI
  - src/router.js: /groups路由
  - src/App.vue: 分组导航

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

- **Project**: github-repo-manager
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 代码已提交本地 master (704ecfa)
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260518-001-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Git**: 本地 master 已 commit (704ecfa)
- **Files**:
  - server/routes/webhook.js: Webhook接收端点 (trigger + generic)
  - server/services/webhookTrigger.js: 事件处理逻辑
  - server/routes/credentials.js: 凭证管理CRUD
  - server/services/credentialService.js: AES-256-GCM加密
  - src/views/WebhookSettings.vue: Webhook配置UI
  - src/views/WebhookEventsLog.vue: 事件日志UI
  - src/views/CredentialsView.vue: 凭证管理UI
  - src/views/RollbackView.vue: 回滚历史UI
- **API**:
  - POST /api/webhook/trigger — GitHub Webhook触发
  - POST /api/webhook/generic — 通用Webhook
  - GET/POST /api/webhook/events — 事件日志
  - GET/PUT/DELETE /api/settings/webhook/:id — Webhook配置
  - GET/POST/PUT/DELETE /api/credentials — 凭证CRUD
- **Tables**: webhook_events, webhook_secrets, credentials
- **Notes**: electron-builder下载Electron卡住，Vite构建成功(75s)，但完整包未生成

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

#### P-20260518-004: TodoList V31 — 离线优先架构（Zustand 统一状态管理）

- **Project**: TodoList
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 构建成功，GitHub Actions 部署成功，curl 验证 200 OK
- **Last Update**: 2026-05-18
- **Git**: main (7d35b0c)
- **Features**: Zustand 统一状态管理，12+ localStorage 调用迁移到 store，离线状态栏 OfflineBanner，migrateFromLegacy 数据迁移
- **Deploy**: https://yeluo45.github.io/todo-list/?v=31

#### P-20260518-005: TodoList V32 — 离线优先深化（SharedWorker + OPFS + 冲突解决）

- **Project**: TodoList
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 构建成功，GitHub Actions 部署成功，curl 验证 200 OK
- **Last Update**: 2026-05-18
- **Git**: main (028845f)
- **Features**: SharedWorker 跨标签页同步，OPFS 大文件存储，ConflictModal 冲突解决弹窗
- **Deploy**: https://yeluo45.github.io/todo-list/?v=32

#### P-20260518-006: TodoList V33 — 离线优先深化round2（集成 + OPFS存储层）

- **Project**: TodoList
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 构建成功，GitHub Actions 部署成功，curl 验证 200 OK
- **Last Update**: 2026-05-18
- **Git**: main (7d295cd)
- **Features**: App.jsx 集成 useSyncWorker，ConflictModal 冲突解决流程，storage.js 统一存储层（OPFS自动切换）
- **Deploy**: https://yeluo45.github.io/todo-list/?v=33

#### P-20260518-007: TodoList V36 — 离线优先深化round5（冲突自动合并策略）

- **Project**: TodoList
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 构建成功，GitHub Actions 部署成功，curl 验证 200 OK
- **Last Update**: 2026-05-18
- **Git**: main (5d4d10c)
- **Features**: syncWorker autoMerge() 自动合并策略，冲突检测（updatedAt比对），subtasks 去重
- **Deploy**: https://yeluo45.github.io/todo-list/?v=36

#### P-20260518-008: TodoList V37 — 离线优先深化round6（OPFS迁移进度Toast）

- **Project**: TodoList
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: 构建成功，GitHub Actions 部署成功，curl 验证 200 OK
- **Last Update**: 2026-05-18
- **Git**: main (ec2f063)
- **Features**: storage.js migrateToOPFS 分批进度回调，App.jsx OPFS 迁移进度 Toast + 样式
- **Deploy**: https://yeluo45.github.io/todo-list/?v=37

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

#### P-20260517-008: PRD: 卡牌DBG V25 — 成就系统+统计追踪

- **Project**: card-game-prototype
- **Owner**: 小墨
- **Stage**: approved_for_dev
- **Acceptance**: 
- **Last Update**: 2026-05-17
- **PRD Path**: workspace-pm/proposals/P-20260517-008-prd.md
- **Direction**: A
- **Mode**: 无人值守模式

#### P-20260517-007: PRD: 卡牌DBG V24 — 更多卡牌类型(POWER/CURSE/TREASURE)

#### P-20260517-006: PRD: 卡牌DBG V23 — 随机事件+商人系统

#### P-20260517-005: PRD: 卡牌DBG V22 — 多策略敌人AI辩论系统

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

#### P-20260517-014: PRD: ai-subscription 测试体系建设 — Vitest 单元测试 + 集成测试

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-014-prd.md
- **Reference**: 前置: P-20260517-013 UI/UX 打磨
- **Notes**: bf030bb2 - Vitest配置(vite.config.ts test{}) + 8个测试文件(cryptoService/sanitize/offline/engine/EmptyState/OfflineIndicator/ThemeSwitcher/setup)。构建 24.70s（需NODE_ENV=development）。无人值守完成。

#### P-20260517-027: PRD: ai-subscription API 开放平台 — 第三方集成 + Webhook 事件订阅 + 开放 API

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-027-prd.md
- **Reference**: 前置: P-20260517-026 高级个性化
- **Notes**: 54cdea19 - ApiPlatform.tsx(Webhook/API Key/集成) + server/routes/platform.ts + 导航集成。构建 30.39s。无人值守完成。

#### P-20260517-026: PRD: ai-subscription 高级个性化 — 主题定制 + 布局自定义 + Widget 小部件

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-026-prd.md
- **Reference**: 前置: P-20260517-025 数据导出增强
- **Notes**: b1525bbe - PersonalizationPanel.tsx(主题/布局/Widget管理) + usePersonalization hook + theme.css + Settings集成。构建 27.68s。无人值守完成。

#### P-20260517-025: PRD: ai-subscription 数据导出增强 — OPML 导出 + JSON 备份 + 订阅源迁移工具

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-025-prd.md
- **Reference**: 前置: P-20260517-024 高级探索
- **Notes**: 214317c1 - export.ts(OPML/JSON导出) + Settings.tsx(导出/导入管理UI)。构建 27.50s。无人值守完成。

#### P-20260517-024: PRD: ai-subscription 高级探索 — AI Agent 编排 + 自定义工作流画布 + 可视化流程设计

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-024-prd.md
- **Reference**: 前置: P-20260517-023 社区功能
- **Notes**: e170f1b8 - Explorer.tsx(高级探索页面) + Agent Registry + Workflow Canvas + Pipeline Visualizer + 导航集成。构建 26.66s。无人值守完成。

#### P-20260517-023: PRD: ai-subscription 社区功能 — 公开订阅列表 + 分享功能 + 用户个人主页

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-023-prd.md
- **Reference**: 前置: P-20260517-022 用户体验优化
- **Notes**: 0c963b00 - Community.tsx(发现/我的列表/我的订阅) + communityDB.ts + types/community.ts + 导航集成。构建 30.41s。无人值守完成。

#### P-20260517-022: PRD: ai-subscription 用户体验优化 — 快捷键增强 + 键盘导航 + 全局搜索优化

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-022-prd.md
- **Reference**: 前置: P-20260517-021 智能推荐
- **Notes**: 473af794 - useKeyboardShortcuts增强 + useGlobalSearch(模糊搜索/防抖/键盘导航) + useListNavigation + 快捷键帮助面板。构建 23.90s。无人值守完成。

#### P-20260517-021: PRD: ai-subscription 智能推荐增强 — 个性化推荐 + 相似文章推荐

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-021-prd.md
- **Reference**: 前置: P-20260517-020 性能深化
- **Notes**: d30d1369 - Recommend.tsx页面 + recommendationService.ts(相似度计算) + 导航集成。构建 27.75s。无人值守完成。

#### P-20260517-020: PRD: ai-subscription 性能深化 — 代码分割优化 + Service Worker 缓存策略 + CDN 加速

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-020-prd.md
- **Reference**: 前置: P-20260517-019 国际化扩展
- **Notes**: 7e1f6392 - vendor-ml独立chunk(6MB) + vendor-charts + vendor-i18n + sw.js缓存策略v3(CDN_CACHE)。构建 29.04s。无人值守完成。

#### P-20260517-019: PRD: ai-subscription 国际化扩展 — 多语言支持 + RTL 布局适配

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-019-prd.md
- **Reference**: 前置: P-20260517-018 高级安全
- **Notes**: 669148b8 - 6个新语言文件(th/vi/id/de/fr/es) + LanguageSwitcher 8语言选项 + i18n/index.tsx支持所有 locales。构建 30.87s。无人值守完成。

#### P-20260517-018: PRD: ai-subscription 高级安全功能 — E2E 加密传输 + MCP 鉴权增强 + 敏感操作二次验证

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-018-prd.md
- **Reference**: 前置: P-20260517-017 数据可视化
- **Notes**: 25922451 - cryptoService增强(AES-GCM加密) + SensitiveConfirmModal(敏感操作二次验证) + MCP鉴权增强(Bearer Token)。构建 30.79s。无人值守完成。

#### P-20260517-017: PRD: ai-subscription 数据可视化增强 — 阅读趋势图表 + 健康度仪表盘 + 阅读统计

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-017-prd.md
- **Reference**: 前置: P-20260517-016 高级功能
- **Notes**: f4ffaae3 - ReadingTrendChart(7天折线图/纯SVG) + HealthDashboard(环形图/健康度评分) + ReadingTimeStats(热力图) + AnalyticsDashboard(整合三个组件)。构建 25.43s。无人值守完成。

#### P-20260517-016: PRD: ai-subscription 高级功能探索 — AI Agent 自动化 + 对话式交互

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-016-prd.md
- **Reference**: 前置: P-20260517-015 部署优化
- **Notes**: 55bdbeb1 - AIAssistantPanel(Ant Design Drawer聊天界面) + chatService(自然语言查询/订阅统计/内容推荐/摘要生成) + localStorage持久化(ai-subscription-chat-history)。构建 25.43s。无人值守完成。

#### P-20260517-015: PRD: ai-subscription 部署优化 — CI/CD + 版本管理

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-015-prd.md
- **Reference**: 前置: P-20260517-014 测试体系
- **Notes**: 73c1575c - GitHub Actions CI(.github/workflows/ci.yml npm ci/test/build) + Deploy(deploy.yml peaceiris/actions-gh-pages) + CHANGELOG.md。构建 28.47s。无人值守完成。

#### P-20260517-013: PRD: ai-subscription UI/UX 打磨 — 暗色模式 + 动画 + 空状态页面

- **Project**: ai-subscription
- **Owner**: 小墨
- **Stage**: accepted
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-013-prd.md
- **Reference**: 前置: P-20260517-012 PWA 增强
- **Notes**: 1fef7781 - 暗色模式(ThemeSwitcher亮/暗/跟随系统) + CSS过渡动画(200ms) + EmptyState(6场景纯SVG插图) + SkeletonBlock(纯CSS shimmer)。构建 3.92s。无人值守完成。

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

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: ✅ 2026-05-17
- **Last Update**: 2026-05-17
- **Dev Commit**: 67d89ad (+9行)
- **Lines**: 42,196 → 42,205 (+9)
- **Deployed**: GitHub Actions CI: Build Tauri App (run 25986912054) ✅ SUCCESS
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-011-prd.md
- **Notes**: Tauri v2 构建链路打通 - GitHub Actions CI (windows-latest) 自动构建，产出 NSIS/MSI 安装包。修复了 FilePath API 变更、base64 依赖、async/await edition 问题。
- **Artifacts**: nsis/msi bundles via GitHub Release (draft)
- **Unattended**: true

#### P-20260517-012: UI布局重构 - 分组折叠式工具栏

- **Project**: creative-drawing-board
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-17
- **Dev Commit**: 147eae8 (+294行)
- **Lines**: 42,205 → 42,349 (+144)
- **Deployed**: ✅ master push SUCCESS
- **PRD Path**: ~/.hermes/proposals/workspace-pm/proposals/P-20260517-012-prd.md
- **Notes**: 分组折叠式工具栏 - 6个功能分组（core/drawing/material/media/settings/special），核心工具组常驻展开，间距从6px增加到12px
- **Unattended**: true

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

### P-20260518-001: ai-creator-h5 AI创作工作流编排器 (Direction A iter3)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 478e240，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-001-prd.md
- **Direction**: A (iteration 3)
- **Mode**: 无人值守模式
- **Git**: main (478e240)
- **Features**: 可视化节点编排; 执行引擎; 模板管理; 画布缩放/平移; 无新增依赖

### P-20260518-002: ai-creator-h5 AI角色组合协作系统 V2 (Direction B iter2)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit fdee205+7769028，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-002-prd.md
- **Direction**: B (iteration 2)
- **Mode**: 无人值守模式
- **Git**: main (fdee205, 7769028)
- **Features**: 多角色组合协作; 并行创作; 角色预设管理; 协作状态实时显示; 6种角色

### P-20260518-003: ai-creator-h5 AI创作工作流编排器 v2 (Direction A iter4)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 7feeed3+069147d，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-003-prd.md
- **Direction**: A (iteration 4)
- **Mode**: 无人值守模式
- **Git**: main (7feeed3, 069147d)
- **Features**: 日志面板; 版本管理; 执行结果预览; 状态徽章; 进度条; 快捷键; 撤销; 连接线状态

### P-20260518-013: preschool-puzzle 道具强化与套装收集 V7 (Direction A)

- **Project**: preschool-puzzle
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-013-prd.md
- **Direction**: A (iter 6)
- **Mode**: 无人值守模式
- **Source Design**: nanobot-design (ToolRegistry)
- **Features**: 道具强化; _plus版效果增强; shield计数; all游戏同步
- **Git**: main (80b6a5a)

### P-20260518-014: preschool-puzzle 道具套装收集 V8 (Direction A - A3)

- **Project**: preschool-puzzle
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-014-prd.md
- **Direction**: A (iter 7)
- **Mode**: 无人值守模式
- **Source Design**: nanobot-design
- **Features**: 6套装; shape_master; time_controller; shield_king; color_expert; maze_master; all_plus; all_plus升级为9道具
- **Git**: main (4bac5e6)

### P-20260518-012: preschool-puzzle 新道具开发与效果增强 V6 (Direction A)

- **Project**: preschool-puzzle
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-012-prd.md
- **Direction**: A (iter 5)
- **Mode**: 无人值守模式
- **Source Design**: nanobot-design (ToolRegistry)
- **Features**: 4新道具; 减速沙漏; 双倍积分; 护盾; 答案之书; 全游戏通用效果
- **Git**: main (4153cb0)

### P-20260518-011: preschool-puzzle 成就徽章与道具套装 V5 (Direction A)

- **Project**: preschool-puzzle
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-011-prd.md
- **Direction**: A (iter 4)
- **Mode**: 无人值守模式
- **Source Design**: nanobot-design (ToolRegistry)
- **Features**: 成就系统; 道具套装; 升级券; 8成就徽章
- **Git**: main (c8f7fdf)

### P-20260518-010: preschool-puzzle 星辰商店与限时道具 V4 (Direction A)

- **Project**: preschool-puzzle
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-010-prd.md
- **Direction**: A (iter 3)
- **Mode**: 无人值守模式
- **Source Design**: nanobot-design (ToolRegistry)
- **Features**: 每日签到奖励; 扭蛋系统; 道具升级; 价格调整
- **Git**: main (26f8aa7)

### P-20260518-009: preschool-puzzle 道具效果集成 V3 (Direction A)

- **Project**: preschool-puzzle
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-009-prd.md
- **Direction**: A (iter 2)
- **Mode**: 无人值守模式
- **Source Design**: nanobot-design (ToolRegistry)
- **Features**: shape_hint效果; time_pause效果; color_magnifier效果; sort_assist效果; map_fragment效果; wall_soften效果
- **Git**: main (8cd4e51)

### P-20260518-008: preschool-puzzle 道具系统 V2 (Direction A)

- **Project**: preschool-puzzle
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: git push 成功 (fb9c349), npm run build 无错, 商店按钮+星星显示正常, 6道具注册表, localStorage 持久化
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-008-prd.md
- **Direction**: A
- **Mode**: 无人值守模式
- **Source Design**: nanobot-design (ToolRegistry)
- **Git**: main (fb9c349)
- **Features**: 星星经济; ToolRegistry道具注册表; ItemShop商店; 6个道具; localStorage持久化

---

### P-20260518-003: hermes-agent-collab thunderbolt-inspired SQLite WAL Backend + Dual-Storage Factory (Direction B)

- **Project**: hermes-agent-collab
- **Owner**: 小墨
- **Stage**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: docs/P-20260518-003-prd.md
- **Git**: gh-pages (e11f7be)
- **Features**: StorageBackend ABC; SQLiteStore (WAL mode, thread-local connections, crash recovery); get_storage_backend() factory; append_event/list_events; events table schema; JsonFileStore subclasses StorageBackend; WAL pragmas (journal_mode=WAL, synchronous=NORMAL, busy_timeout=5000)

---

### P-20260518-005: hermes-agent-collab ruflo-inspired Hook/Plugin Architecture + Built-in Metrics Plugins (Direction D)

- **Project**: hermes-agent-collab
- **Owner**: 小墨
- **Stage**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: docs/P-20260518-005-prd.md
- **Git**: gh-pages (1bb5599)
- **Features**: HookEvent enum (17 lifecycle events); Plugin dataclass; PluginRegistry (subscribe/emit/enable/disable); global + workspace registries; TaskMetricsPlugin + AgentMetricsPlugin; hook emissions in agent_registry/task_manager/skill_system/orchestration_manager

---

### P-20260518-006: hermes-agent-collab generic-agent Multi-Agent Collaboration Protocol (Direction E)

- **Project**: hermes-agent-collab
- **Owner**: 小墨
- **Stage**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: docs/P-20260518-006-prd.md
- **Git**: gh-pages (9ad4329)
- **Features**: MessageType (9 types); AgentMessage/AgentSession/DelegationPolicy/TaskDistribution/CapabilityMatchResult; MultiAgentProtocol (send/ack/session/distribute/match/timeout); find_by_capability(); for_messages/for_sessions; 7 new HookEvents

---

### P-20260518-007: hermes-agent-collab REST API + SSE Real-time Events Layer (Direction F)

- **Project**: hermes-agent-collab
- **Owner**: 小墨
- **Stage**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: docs/P-20260518-007-prd.md
- **Git**: gh-pages (ab02550)
- **Features**: MessageSendRequest/SessionCreateRequest/DistributionCreateRequest models; orchestration lifecycle endpoints; MultiAgentProtocol REST (send/ack/session/distribute/match); plugin/hook management endpoints; SSE streams with workspace scoping + event filtering + cursor

---

### P-20260518-004: hermes-agent-collab deepcode-inspired TaskRouter + Complexity-Gated Decomposition (Direction C)

- **Project**: hermes-agent-collab
- **Owner**: 小墨
- **Stage**: accepted
- **Last Update**: 2026-05-18
- **PRD Path**: docs/P-20260518-004-prd.md
- **Git**: gh-pages (01989c8)
- **Features**: TaskRouter class (route based on TaskComplexity); SIMPLE (1 SubTask, no LLM); NORMAL (2-4 SubTasks via LLM); COMPLEX (4-8 SubTasks + CriticReview quality gates); _llm_decompose with fallback; OrchestrationManager.decompose_task() delegates to TaskRouter

---

### P-20260518-004: ai-creator-h5 AI创作工作流编排器 v3 (Direction A iter5)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit d8c04ce+ca19af4，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-004-prd.md
- **Direction**: A (iteration 5)
- **Mode**: 无人值守模式
- **Git**: main (d8c04ce, ca19af4)
### P-20260518-005: ai-creator-h5 AI创作工作流编排器 v4 (Direction A iter6)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit b44383e，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-005-prd.md
- **Direction**: A (iteration 6)
- **Mode**: 无人值守模式
- **Git**: main (b44383e)
- **Features**: AI智能推荐; 模板市场; 6个精选模板; 收藏/评分; 分类筛选; 导出JSON
### P-20260518-006: ai-creator-h5 AI创作工作流编排器 v5 (Direction A iter7)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit a304c9e，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-006-prd.md
- **Direction**: A (iteration 7)
- **Mode**: 无人值守模式
- **Git**: main (a304c9e)
- **Features**: 执行监控面板; 实时状态栏; 节点耗时统计; 性能排行; 执行历史; 重新执行
### P-20260518-007: ai-creator-h5 AI创作工作流编排器 v6 (Direction A iter8)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 7f28787，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-007-prd.md
- **Direction**: A (iteration 8)
- **Mode**: 无人值守模式
- **Git**: main (7f28787)
- **Features**: 版本历史追踪; 版本对比; 差异高亮; 回滚; 分支创建/切换/合并/删除
### P-20260518-008: ai-creator-h5 AI创作工作流编排器 v7 (Direction A iter9)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 02ecc5d，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-008-prd.md
- **Direction**: A (iteration 9)
- **Mode**: 无人值守模式
- **Git**: main (02ecc5d)
- **Features**: 分享链接; 权限管理; 在线用户指示; 节点锁定; 审计日志; BroadcastChannel跨标签页协作
### P-20260518-009: ai-creator-h5 AI创作工作流编排器 v8 (Direction A iter10)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit d2f3693，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-009-prd.md
- **Direction**: A (iteration 10)
- **Mode**: 无人值守模式
- **Git**: main (d2f3693)
- **Features**: 插件市场; 自定义节点; 节点构建器; 沙箱执行器; 3个官方插件; 数据转换/字符串处理/数学计算
### P-20260518-010: ai-creator-h5 AI创作工作流编排器 v9 (Direction A iter11)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 577c10e，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-010-prd.md
- **Direction**: A (iteration 11)
- **Mode**: 无人值守模式
- **Git**: main (577c10e)
- **Features**: 自然语言生成工作流; 智能节点推荐; 意图路由节点; 对话式编辑; 5个预设模板
### P-20260518-011: ai-creator-h5 AI创作工作流编排器 v10 (Direction A iter12)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 548f61d，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-011-prd.md
- **Direction**: A (iteration 12)
- **Mode**: 无人值守模式
- **Git**: main (548f61d)
- **Features**: 多格式导出; 代码生成(JS/Python); 定时调度; 触发器管理; 执行报告; 浏览器通知
### P-20260518-012: ai-creator-h5 AI创作工作流编排器 v11 (Direction A iter13)

- **Project**: ai-creator-h5
- **Owner**: 小墨
- **Stage**: delivered
- **Acceptance**: Git commit 602809a，push 成功
- **Last Update**: 2026-05-18
- **PRD Path**: workspace-pm/proposals/P-20260518-012-prd.md
- **Direction**: A (iteration 13)
- **Mode**: 无人值守模式
- **Git**: main (602809a)
- **Features**: 断点调试; 变量监察面板; 执行轨迹; 条件断点; 时间旅行; 单步执行
