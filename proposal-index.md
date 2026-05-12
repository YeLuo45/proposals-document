# Proposal Index

> **数据源**: `proposals.csv`（主数据）
> 本文件仅作快速索引，实际数据以 CSV 为准。

---
## 提案总数：187个

### 按状态统计

- **active**: 126
- **in_dev**: 58
- **archived**: 2
- **delivered**: 1

### 按项目统计（Top 15）

- **PRJ-20260418-002**: 40
- **PRJ-20260421-001**: 32
- **PRJ-20260420-002**: 17
- **PRJ-20260419-003**: 13
- **PRJ-20250416-001**: 11
- **PRJ-20260412-008**: 11
- **PRJ-20260428-002**: 8
- **PRJ-20260422-001**: 6
- **PRJ-20260428-001**: 6
- **PRJ-20250416-002**: 6
- **PRJ-20260412-009**: 5
- **PRJ-20260420-001**: 4
- **PRJ-20260419-001**: 3
- **PRJ-20260423-005**: 3
- **PRJ-20260418-004**: 2

---
## CSV 数据文件

| `proposals.csv` | 提案主表（20字段） | 186行 |
| `projects.csv` | 项目主表 | 32行 |
| `project_proposal_mapping.csv` | Project↔Proposal映射 | 186行 |

---
---

### P-20260505-012: future-little-leaders-v3-家庭圈-family-circle

- `Proposal ID`: `P-20260505-012`
- `Title`: future-little-leaders-v3-家庭圈-family-circle
- `Owner`: 小墨
- `Current Status`: `in_dev`
- `PRD Path`: `workspace-pm/proposals/P-20260505-011-prd.md`
- `Project Path`: `/home/hermes/future-little-leaders`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `pending`
- `Last Update`: 2026-05-05
- `Notes`: 家庭成员角色系统 + 任务归属 + 家庭共享任务池 + 宝宝头像优化 + 家庭数据概览；cron P-20260502-017-tech-confirm 重复触发(2026-05-11)，状态已存在，仅记录时间戳

### P-20260502-017: ai-subscription-大模型调用层升级-llm-design-dev

- `Proposal ID`: `P-20260502-017`
- `Title`: ai-subscription-大模型调用层升级-llm-design-dev
- `Owner`: 小墨
- `Current Status`: `in_dev`
- `PRD Path`: `workspace-pm/proposals/P-20260502-017-prd.md`
- `Technical Solution`: (待输出)
- `Test Cases Path`: (待填写)
- `Project Path`: `workspace-dev/ai-subscription/proposals`
- `Acceptance`: -
- `PRD Confirmation`: `timeout-approved`
- `PRD Confirmation Countdown ID`: -
- `Technical Expectations`: timeout-approved
- `Technical Expectations Countdown ID`: -
- `Technical Stack`: `ai SDK + @ai-sdk/openai + @ai-sdk/anthropic + @ai-sdk/google + partial-json + jsonrepair`
- `Technical Expectations Timeout Resolution`: 倒计时到期(2026-05-02)，默认通过处理（cron job P-20260502-017-tech-confirm 执行）
- `Research Direction`: pending
- `Research Direction Countdown ID`: -
- `Deployment URL`: (待部署)
- `Deployment Branch`: (待填写)
- `Last Update`: 2026-05-12
- `Notes`: 状态已存在，无需更新（cron P-20260502-017-tech-confirm 重复触发(2026-05-11)，仅记录时间戳）；再次触发(2026-05-13 cron 2nd)，状态已就绪，无需更新；再次触发(2026-05-14 cron)，状态已就绪，无需更新；再次触发(2026-05-14 cron 2nd)，状态已就绪，无需更新；再次触发(2026-05-15 cron)，状态已就绪，无需更新；再次触发(2026-05-16 cron)，状态已就绪，无需更新；再次触发(2026-05-17 cron)，状态已就绪，无需更新；再次触发(2026-05-19 cron)，状态已就绪，无需更新；再次触发(2026-05-20 cron)，状态已就绪，无需更新；再次触发(2026-05-21 cron)，状态已就绪，无需更新；再次触发(2026-05-22 cron)，状态已就绪，无需更新；再次触发(2026-05-23 cron)，状态已就绪，无需更新；再次触发(2026-05-26 cron)，状态已就绪，无需更新；再次触发(2026-05-27 cron)，状态已就绪，无需更新；再次触发(2026-05-28 cron)，状态已就绪，无需更新 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-05-28 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-05-29 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-05-30 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-05-31 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-06-02 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-06-03 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-06-05 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-06-06 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-06-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-06-17 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-06-18 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-06-19 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-06-19 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-07-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-07-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-07-13 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-07-14 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-07-15 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新

*最后更新：2026-05-12*
### P-20260506-001: ai-subscription-智能分类标签系统

- `Proposal ID`: `P-20260506-001`
- `Title`: ai-subscription-智能分类标签系统
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260506-001-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `boss-selected-P0`
- `Technical Expectations`: pending
- `Last Update`: 2026-05-06
- `Notes`: commit 1da65a8 - TagBadge/TagManager/TagFilterSidebar + IndexedDB tags表 + AI生成标签 + 多维筛选

### P-20260506-002: ai-subscription-Readwise-Instapaper同步

- `Proposal ID`: `P-20260506-002`
- `Title`: ai-subscription-Readwise-Instapaper同步
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260506-002-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `boss-selected-P0`
- `Technical Expectations`: pending
- `Last Update`: 2026-05-06
- `Notes`: commit 43b7fa5 - Readwise API同步 + Instapaper一键保存 + syncIndexedDB

### P-20260506-003: ai-subscription-多语言原文翻译

- `Proposal ID`: `P-20260506-003`
- `Title`: ai-subscription-多语言原文翻译
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260506-003-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `boss-selected-P0`
- `Technical Expectations`: pending
- `Last Update`: 2026-05-06
- `Notes`: commit 07ed1acd - 语言检测+翻译按钮+TranslationSettings+translationDB

### P-20260506-004: ai-subscription-知识图谱可视化

- `Proposal ID`: `P-20260506-004`
- `Title`: ai-subscription-知识图谱可视化
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260506-004-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `boss-selected-P1`
- `Technical Expectations`: pending
- `Last Update`: 2026-05-06
- `Notes`: commit 333e42c - AI实体提取+SVG力导向图谱+EntityCard+knowledgeGraphDB

### P-20260506-005: ai-subscription-RSS-Atom输出

- `Proposal ID`: `P-20260506-005`
- `Title`: ai-subscription-RSS-Atom输出
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260506-005-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `boss-selected-P2`
- `Technical Expectations`: pending
- `Last Update`: 2026-05-06
- `Notes`: commit 2300dbe - RSS/Atom生成+publicListDB+PublicListEditor

### P-20260506-006: ai-subscription-邮件组同步

- `Proposal ID`: `P-20260506-006`
- `Title`: ai-subscription-邮件组同步
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260506-006-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `boss-selected-P2`
- `Technical Expectations`: pending
- `Last Update`: 2026-05-06
- `Notes`: commit e294592 - 订阅者管理+邮件模板+批量发送+emailSubscriptionDB

### P-20260506-007: ai-subscription-API开放

- `Proposal ID`: `P-20260506-007`
- `Title`: ai-subscription-API开放
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260506-007-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `boss-selected-P2`
- `Technical Expectations`: pending
- `Last Update`: 2026-05-06
- `Notes`: commit 0572d8b - API Key管理+REST端点+DeveloperPanel+apiDB

### P-20260506-008: ai-subscription-智能摘要增强

- `Proposal ID`: `P-20260506-008`
- `Title`: ai-subscription-智能摘要增强
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260506-008-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `confirmed`
- `Last Update`: 2026-05-06
- `Notes`: commit 3b7d6d3d - summary-schema.ts + aiAdapter.ts结构化摘要生成(summarizeStructured/summarizeStructuredWithFallback)
- `Technical Expectations`: pending
- `Last Update`: 2026-05-06
- `Notes`: 结构化摘要：生成标题+3关键点+情感标签，ArticleCard UI升级，IndexedDB字段扩展

### P-20260506-009: ai-subscription-自动化工作流

- `Proposal ID`: `P-20260506-009`
- `Title`: ai-subscription-自动化工作流
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260506-009-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `confirmed`
- `Last Update`: 2026-05-06
- `Notes`: commit 3b7d6d3d - WorkflowEngine + workflowDB + telegramService + WorkflowList/WorkflowEditor/WorkflowLogs + Settings Tab
- `Technical Expectations`: pending
- `Last Update`: 2026-05-06
- `Notes`: 规则引擎：触发器(keyword/sentiment/source)+动作(add_tag/Telegram/Webhook/星标)，WorkflowEngine异步执行

"
### P-20260506-010: PixelPal-V23-移动端PWA适配

- `Proposal ID`: `P-20260506-010`
- `Title`: PixelPal-V23-移动端PWA适配
- `Owner`: 小墨
- `Current Status`: `in_dev`
- `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260506-001.md`
- `Project Path`: `/home/hermes/pixel-pal-web`
- `Project`: `PRJ-20260420-002`
- `Acceptance`: pending
- `PRD Confirmation`: `confirmed`
- `Last Update`: 2026-05-06
- `Notes`: V23 移动端适配 - manifest/theme-color/sw路径/Drawer优化/消息长按菜单/触摸优化

### P-20260507-001: PixelPal-V41-协作模式深化

- `Proposal ID`: `P-20260507-001`
- `Title`: PixelPal-V41-协作模式深化
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: accepted
- `Project Path`: `/home/hermes/pixel-pal-web`
- `Project`: `PRJ-20260420-002`
- `Last Update`: 2026-05-07
- `Notes`: V41协作模式深化完成：CollaborationChat+TaskBreakdown+ResultSummary+CollaborationControls，3-tab集成（分工/对话/汇总），commit 45c7883。注意：npm run build在本地exit 2（既有TS错误），但GitHub Actions用vite build正常通过。

### P-20260507-002: PixelPal-Settings-版本信息显示

- `Proposal ID`: `P-20260507-002`
- `Title`: PixelPal-Settings-版本信息显示
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260507-002.md`
- `Project Path`: `/home/hermes/pixel-pal-web`
- `Project`: `PRJ-20260420-002`
- `Last Update`: 2026-05-07
- `Notes`: 设置页VersionInfo组件显示版本+构建时间，vite.config.ts define注入；commit cc0c1d5

### P-20260507-003: PixelPal-V42-协作系统深度化

- `Proposal ID`: `P-20260507-003`
- `Title`: PixelPal-V42-协作系统深度化
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260507-003.md`
- `Project Path`: `/home/hermes/pixel-pal-web`
- `Project`: `PRJ-20260420-002`
- `Last Update`: 2026-05-07
- `Notes`: V42协作系统深度化完成：CollabHistory(10条历史)+CollabHistoryDetail(详情)+store持久化+4-tab集成；commit cc0c1d5

### P-20260507-006: AI Creator H5 - API额度管理

- `Proposal ID`: `P-20260507-006`
- `Title`: AI Creator H5 - API额度管理
- `Owner`: 小墨
- `Current Status`: `active`
- `Acceptance`: `active`
- `PRD Path`: `workspace-pm/proposals/P-20260507-006-prd.md`
- `Project Path`: `/home/hermes/ai-creator-h5`
- `Project`: `PRJ-20260419-007`
- `Last Update`: 2026-05-07
- `Notes`: API额度管理完成：usageService.js(用量追踪/成本估算/预警)+额度卡片+弹窗面板+每月1日自动重置；commit f1febad，部署到 https://yeluo45.github.io/ai-creator-h5/

### P-20260508-001: AI Creator H5 - 创作者中心

- `Proposal ID`: `P-20260508-001`
- `Title`: AI Creator H5 - 创作者中心
- `Owner`: 小墨
- `Current Status`: `active`
- `Acceptance`: `active`
- `PRD Path`: `workspace-pm/proposals/P-20260508-001-prd.md`
- `Project Path`: `/home/hermes/ai-creator-h5`
- `Project`: `PRJ-20260419-007`
- `Last Update`: 2026-05-08
- `Notes`: 创作者中心完成：creator.html(作品集/资料/分享)+creatorService.js(核心服务)+Canvas分享卡片；commit a5d4923，部署到 https://yeluo45.github.io/ai-creator-h5/

### P-20260508-002: AI Creator H5 - PWA离线支持增强

- `Proposal ID`: `P-20260508-002`
- `Title`: AI Creator H5 - PWA离线支持增强
- `Owner`: 小墨
- `Current Status`: `active`
- `Acceptance`: `active`
- `PRD Path`: `workspace-pm/proposals/P-20260508-002-prd.md`
- `Project Path`: `/home/hermes/ai-creator-h5`
- `Project`: `PRJ-20260419-007`
- `Last Update`: 2026-05-08
- `Notes`: PWA离线支持增强完成：SW v1.6.0缓存更新+全局离线状态栏+生成页离线禁用+版本更新toast；commit caccf7a，部署到 https://yeluo45.github.io/ai-creator-h5/

### P-20260508-003: PixelPal V50 — Linear Dark Mode 大重构

- `Proposal ID`: `P-20260508-003`
- `Title`: PixelPal V50 — Linear Dark Mode 大重构
- `Owner`: 小墨
- `Current Status`: `active`
- `Acceptance`: `active`
- `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260508-001.md`
- `Project Path`: `/home/hermes/pixel-pal-web`
- `Project`: `PRJ-20260420-002`
- `Last Update`: 2026-05-08
- `Notes`: 基于 Linear.app 设计系统全面重构 UI：#08090a/#0f1011/#191a1b 深色层次 + 品牌indigo #5e6ad2 + accent violet #7170ff + Inter Variable 字体 + 侧边栏/ChatPanel/Settings 全深色化；commit c961502，部署到 https://YeLuo45.github.io/pixel-pal-web；GitHub PR#16 已合并

### P-20260508-004: PixelPal V51 — MiniMax 清新浅色主题

- `Proposal ID`: `P-20260508-004`
- `Title`: PixelPal V51 — MiniMax 清新浅色主题
- `Owner`: 小墨
- `Current Status`: `active`
- `Acceptance`: `active`
- `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260508-002.md`
- `Project Path`: `/home/hermes/pixel-pal-web`
- `Project`: `PRJ-20260420-002`
- `Last Update`: 2026-05-08
- `Notes`: 新增 MiniMax 浅色主题与 V50 深色并存：DM Sans+Outfit字体 / 品牌蓝#1456f0 / 纯白主背景+浅灰次级 / Near Black文字+Gray次级 / Settings主题切换UI(Dark/Light/MiniMax/System)；commit d79449f，PR#17 已合并

### P-20260512-001: 项目提案管理-收藏项目功能

- `Proposal ID`: `P-20260512-001`
- `Title`: 项目提案管理-收藏项目功能
- `Owner`: 小墨
- `Current Status`: `approved_for_dev`
- `PRD Path`: `workspace-pm/proposals/P-20260512-001-prd.md`
- `Tech Solution Path`: `workspace-dev/proposals/prj-proposals-manager/P-20260512-001-tech-solution.md`
- `Project Path`: `/home/hermes/workspace-dev/proposals/prj-proposals-manager`
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `Last Update`: 2026-05-12
- `Notes`: 新增收藏项目功能，星标按钮，收藏数据存储到GitHub仓库data/favorites.json；commit 6d3b4c4，GitHub Pages已部署

### P-20260512-002: 项目提案管理-收藏列表独立视图

- `Proposal ID`: `P-20260512-002`
- `Title`: 项目提案管理-收藏列表独立视图
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `Tech Solution Path`: `workspace-dev/proposals/prj-proposals-manager/P-20260512-002-tech-solution.md`
- `Project Path`: `/home/hermes/workspace-dev/proposals/prj-proposals-manager`
- `Project`: `prj-proposals-manager`
- `Last Update`: 2026-05-12
- `Notes`: 收藏视图快速访问已收藏项目，Header添加星标入口和数量badge；commit 335fdf1，GitHub Pages已部署

### P-20260512-003: 项目提案管理-收藏项目排序

- `Proposal ID`: `P-20260512-003`
- `Title`: 项目提案管理-收藏项目排序
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `Tech Solution Path`: `workspace-dev/proposals/prj-proposals-manager/P-20260512-003-tech-solution.md`
- `Project Path`: `/home/hermes/workspace-dev/proposals/prj-proposals-manager`
- `Project`: `prj-proposals-manager`
- `Last Update`: 2026-05-12
- `Notes`: 收藏视图按最近收藏时间倒序排列；commit 9d2bdc7，GitHub Pages已部署

### P-20260512-004: 项目提案管理-收藏数据本地缓存

- `Proposal ID`: `P-20260512-004`
- `Title`: 项目提案管理-收藏数据本地缓存
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `Tech Solution Path`: `workspace-dev/proposals/prj-proposals-manager/P-20260512-004-tech-solution.md`
- `Project Path`: `/home/hermes/workspace-dev/proposals/prj-proposals-manager`
- `Project`: `prj-proposals-manager`
- `Last Update`: 2026-05-12
- `Notes`: useFavorites添加localStorage缓存层（5分钟TTL）；commit 4e46611，GitHub Pages已部署

### P-20260512-005: 项目提案管理-收藏批量管理

- `Proposal ID`: `P-20260512-005`
- `Title`: 项目提案管理-收藏批量管理
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `Project Path`: `/home/hermes/workspace-dev/proposals/prj-proposals-manager`
- `Project`: `prj-proposals-manager`
- `Last Update`: 2026-05-12
- `Notes`: 收藏视图支持多选模式和批量删除；commit fdad67c，GitHub Pages已部署

### P-20260512-006: 项目提案管理-收藏项目置顶

- `Proposal ID`: `P-20260512-006`
- `Title`: 项目提案管理-收藏项目置顶
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `Project Path`: `/home/hermes/workspace-dev/proposals/prj-proposals-manager`
- `Project`: `prj-proposals-manager`
- `Last Update`: 2026-05-12
- `Notes`: 收藏项目支持置顶功能（📌置顶/📍取消）；commit ba01f1c，GitHub Pages已部署

### P-20260509-001: PixelPal V64 — Agent执行循环闭环

- `Proposal ID`: `P-20260509-001`
- `Title`: PixelPal V64 — Agent执行循环闭环
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: accepted
- `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-004.md`
- `Project Path`: `/home/hermes/pixel-pal-web`
- `Project`: `PRJ-20260420-002`
- `PRD Confirmation`: confirmed
- `Last Update`: 2026-05-09
- `Notes`: V64 agentExecutor: LLM任务分解+步骤执行+回调；AgentPanel绑定executor；TaskQueue IndexedDB持久化恢复；Sidebar导航已接入；build ✓, master已push ✓

### P-20260509-002: PixelPal V66 — Plan用户确认执行系统

 - `Proposal ID`: `P-20260509-002`
 - `Title`: PixelPal V65 — Plan用户确认执行系统
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Notes`: V66 Plan系统：usePlanExecution hook bridge planStore↔agentExecutor；PlanView完整UI（步骤/风险/进度/确认）；ChatPanel关键词触发+createPlanFromTask集成；build ✓, master已push ✓
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-005.md`
 - `Last Update`: 2026-05-09

### P-20260509-005: PixelPal V67 — Agent记忆上下文增强

 - `Proposal ID`: `P-20260509-005`
 - `Title`: PixelPal V67 — Agent记忆上下文增强
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-005.md`
 - `Last Update`: 2026-05-09
 - `Notes`: 基于MessageHistory的会话级记忆上下文；AgentExecutor注入相关记忆到LLM提示词；UI显示记忆状态；自动提取任务结果

### P-20260509-006: PixelPal V68 — 双插件系统统一

 - `Proposal ID`: `P-20260509-006`
 - `Title`: PixelPal V68 — 双插件系统统一
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-006.md`
 - `Last Update`: 2026-05-09
 - `Notes`: 统一PluginService和pluginRegistry为一站式UnifiedPluginService；迁移现有工具；标记旧接口deprecated；保持向后兼容

### P-20260509-007: PixelPal V69 — Telegram/Feishu平台适配

 - `Proposal ID`: `P-20260509-007`
 - `Title`: PixelPal V69 — Telegram/Feishu平台适配
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-007.md`
 - `Last Update`: 2026-05-09
 - `Notes`: 平台适配层；PlatformAdapter接口+Web/Telegram/Feishu实现；agentEngine跨平台复用；骨架实现，环境变量配置

### P-20260509-008: PixelPal V70 — 语音情感→行为联动

 - `Proposal ID`: `P-20260509-008`
 - `Title`: PixelPal V70 — 语音情感→行为联动
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-008.md`
 - `Last Update`: 2026-05-09
 - `Notes`: 情绪-行为映射表；EmotionBehaviorEngine引擎（冷却+阈值）；配置开关；与AgentExecutor解耦，接口预留

### P-20260509-009: PixelPal V71 — 场景感知自动化

 - `Proposal ID`: `P-20260509-009`
 - `Title`: PixelPal V71 — 场景感知自动化
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-009.md`
 - `Last Update`: 2026-05-09
 - `Notes`: 时间场景+用户状态检测；SceneAwarenessEngine；组合场景响应映射；recordAction/recordError接口；与Agent/Memory解耦

### P-20260509-010: PixelPal V72 — Agent跨会话持久化记忆

 - `Proposal ID`: `P-20260509-010`
 - `Title`: PixelPal V72 — Agent跨会话持久化记忆
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-010.md`
 - `Last Update`: 2026-05-09
 - `Notes`: MemoryStorage持久化服务；MemoryManager.enablePersistence()；agentMemory IndexedDB表；记忆跨会话保留；过期自动清理

### P-20260509-011: PixelPal V73 — EmotionBehaviorEngine与AgentExecutor集成

 - `Proposal ID`: `P-20260509-011`
 - `Title`: PixelPal V73 — EmotionBehaviorEngine与AgentExecutor集成
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-011.md`
 - `Last Update`: 2026-05-09
 - `Notes`: EmotionContextInjector；AgentExecutor注入情感上下文到LLM提示词；任务完成后自动发送情感响应；platformAdapter hook

### P-20260509-012: PixelPal V74 — SceneAwarenessEngine与AgentExecutor集成

 - `Proposal ID`: `P-20260509-012`
 - `Title`: PixelPal V74 — SceneAwarenessEngine与AgentExecutor集成
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-012.md`
 - `Last Update`: 2026-05-09
 - `Notes`: SceneContextInjector；AgentExecutor注入场景上下文到LLM提示词；任务完成后自动发送场景响应；与情感上下文平行

### P-20260509-013: PixelPal V75 — UI层recordAction/recordError集成

 - `Proposal ID`: `P-20260509-013`
 - `Title`: PixelPal V75 — UI层recordAction/recordError集成
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-013.md`
 - `Last Update`: 2026-05-09
 - `Notes`: useSceneAwareness hook；ChatPanel/AgentPanel集成recordAction/recordError；场景响应Toast；全局事件节流

### P-20260509-014: PixelPal V76 — Telegram/Feishu真实API对接

 - `Proposal ID`: `P-20260509-014`
 - `Title`: PixelPal V76 — Telegram/Feishu真实API对接
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-014.md`
 - `Last Update`: 2026-05-09
 - `Notes`: Telegram long polling+sendMessage实现；Feishu OAuth2 token+sendMessage实现；.env.example更新；需要bot token和app credentials

### P-20260509-015: PixelPal 下一阶段 — 多Agent协作架构

 - `Proposal ID`: `P-20260509-015`
 - `Title`: PixelPal 下一阶段 — 多Agent协作架构
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-015.md`
 - `Last Update`: 2026-05-09
 - `Notes`: AgentRegistry注册表；AgentBus消息总线；Orchestrator/Coordinator/Executor/Reviewer四种Agent类型；复用V64-V74基础设施

### P-20260509-016: PixelPal 多Agent实际协作流程实现

 - `Proposal ID`: `P-20260509-016`
 - `Title`: PixelPal 多Agent实际协作流程实现
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-016.md`
 - `Last Update`: 2026-05-09
 - `Notes`: OrchestratorAgent任务分解分发；ExecutorAgent执行；ReviewerAgent审查；init.ts初始化入口；完整消息协作流程

### P-20260509-017: PixelPal 多Agent与V64 AgentExecutor合并

 - `Proposal ID`: `P-20260509-017`
 - `Title`: PixelPal 多Agent与V64 AgentExecutor合并
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-017.md`
 - `Last Update`: 2026-05-09
 - `Notes`: ExecutorAgent调用V64 agentExecutor；init.ts初始化入口；避免循环依赖；Orchestrator→Executor→AgentExecutor完整调用链

### P-20260509-018: PixelPal 多Agent任务触发入口

 - `Proposal ID`: `P-20260509-018`
 - `Title`: PixelPal 多Agent任务触发入口
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-018.md`
 - `Last Update`: 2026-05-09
 - `Notes`: useMultiAgentTrigger hook；/multi和/single命令；自动关键词检测；ChatPanel集成；系统消息显示协作状态

### P-20260509-019: PixelPal 多Agent结果可视化展示

 - `Proposal ID`: `P-20260509-019`
 - `Title`: PixelPal 多Agent结果可视化展示
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-019.md`
 - `Last Update`: 2026-05-09
 - `Notes`: MultiAgentStatus组件（任务列表+进度条）；MultiAgentPanel浮动按钮；任务状态颜色区分；右下角固定位置

### P-20260509-020: PixelPal 个性化推荐系统

 - `Proposal ID`: `P-20260509-020`
 - `Title`: PixelPal 个性化推荐系统
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-020.md`
 - `Last Update`: 2026-05-09
 - `Notes`: PreferenceEngine偏好提取；RecommendationEngine推荐生成；RecommendationPanel组件；基于历史交互的个性化推荐

### P-20260509-021: PixelPal 多Agent任务状态与sessionStorage同步

 - `Proposal ID`: `P-20260509-021`
 - `Title`: PixelPal 多Agent任务状态与sessionStorage同步
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-021.md`
 - `Last Update`: 2026-05-09
 - `Notes`: MultiAgentStore统一存储；OrchestratorAgent任务状态同步；ExecutorAgent任务状态同步；MultiAgentPanel实时读取

### P-20260509-022: PixelPal 个性化推荐与ChatPanel集成

 - `Proposal ID`: `P-20260509-022`
 - `Title`: PixelPal 个性化推荐与ChatPanel集成
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: accepted
 - `Project Path`: `/home/hermes/pixel-pal-web`
 - `Project`: `PRJ-20260420-002`
 - `PRD Path`: `/home/hermes/prj-proposals/PRJ-20260509-022.md`
 - `Last Update`: 2026-05-09
 - `Notes`: ChatPanel导入RecommendationPanel；用户消息触发偏好提取；推荐面板显示；点击推荐触发action

### P-20260512-001: ai-subscription-多模型路由智能分发

 - `Proposal ID`: `P-20260512-001`
 - `Title`: ai-subscription-多模型路由智能分发
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-001-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Acceptance`: `accepted`
 - `PRD Confirmation`: `boss-selected-A`
 - `Technical Expectations`: pending
 - `Last Update`: 2026-05-12
 - `Notes`: commit 0398a5eb - 模型注册表(providers-ai-subscription.ts) + 路由规则引擎(router.ts) + 统一调用接口(llm-router.ts)；翻译→Gemini Flash，摘要→Claude Sonnet，标签→GPT-4o，图谱→Gemini Pro；commit 897c9906 - 现有服务接入路由层(tagService/useTranslation/useKnowledgeGraph改用routeAndCall)；commit 380d2432 - 多Agent协作流水线(pipeline/types+agents+director+pipeline+index)

### P-20260512-002: ai-subscription-多Agent协作处理流水线

 - `Proposal ID`: `P-20260512-002`
 - `Title`: ai-subscription-多Agent协作处理流水线
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-002-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Acceptance`: `accepted`
 - `PRD Confirmation`: `boss-selected-A`
 - `Technical Expectations`: pending
 - `Last Update`: 2026-05-12
 - `Notes`: commit 380d2432 - pipeline/types.ts+agents.ts+director.ts+pipeline.ts+index.ts；ExtractorAgent(standard-summary)+SummarizerAgent(structured-summary)+TaggerAgent(tag-generation)+TranslatorAgent(translation)；AsyncGenerator流式输出

### P-20260512-004: ai-subscription-AI智能工作流引擎（Push策略决策）

 - `Proposal ID`: `P-20260512-004`
 - `Title`: ai-subscription-AI智能工作流引擎（Push策略决策）
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-003-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Acceptance`: `accepted`
 - `PRD Confirmation`: `boss-selected-A`
 - `Technical Expectations`: pending
 - `Last Update`: 2026-05-12
 - `Notes`: commit 37175219 - push-strategy-types.ts+push-strategy-aggregator.ts；PushStrategyAgent(aggregateContent)+UserContext(quietHours)+generatePushStrategy；复用routeAndCall(taskType:'push-strategy')

### P-20260512-005: ai-subscription-对话式内容管理

 - `Proposal ID`: `P-20260512-005`
 - `Title`: ai-subscription-对话式内容管理
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-005-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Acceptance`: `accepted`
 - `PRD Confirmation`: `boss-selected-A`
 - `Technical Expectations`: pending
 - `Last Update`: 2026-05-12
 - `Notes`: commit 5e8cdf93 - conversation/types.ts+intent-parser.ts+operations.ts+conversation-manager.ts+index.ts；Intent解析(add_source/delete_source/search_articles等14种)+regex fallback+Confirmation流程；复用routeAndCall(taskType:'intent-classification')+Gemini 2.0 Flash

### P-20260512-006: ai-subscription-本地推理增强（端侧小模型处理）

 - `Proposal ID`: `P-20260512-006`
 - `Title`: ai-subscription-本地推理增强（端侧小模型处理）
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-006-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Acceptance`: `accepted`
 - `PRD Confirmation`: `boss-selected-A`
 - `Technical Expectations`: pending
 - `Last Update`: 2026-05-12
 - `Notes`: commit 0ad0aadb - local-inference/types.ts+hardware-detector.ts+model-registry.ts+inference-manager.ts+index.ts；LocalClassifier(关键词分类<5ms)+硬件检测(WebGPU/WASM)+inferWithFallback云端降级；intent-parser已集成本地推理

### P-20260512-007: ai-subscription-成本监控面板

 - `Proposal ID`: `P-20260512-007`
 - `Title`: ai-subscription-成本监控面板
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-007-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Acceptance`: `accepted`
 - `PRD Confirmation`: `boss-selected-A`
 - `Technical Expectations`: pending
 - `Last Update`: 2026-05-12
 - `Notes`: commit 45e45561 - cost-tracker/types.ts+storage.ts+calculator.ts+aggregator.ts；CostRecord(IndexedDB)+PRICING_TABLE(GPT-4o/Claude/Gemini)+aggregateRecords+getDailyCosts；routeAndCall自动记录成本

### P-20260512-008: ai-subscription-Pipeline UI集成（流式输出）

 - `Proposal ID`: `P-20260512-008`
 - `Title`: ai-subscription-Pipeline UI集成（流式输出）
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-008-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Acceptance`: `accepted`
 - `PRD Confirmation`: `boss-selected-A`
 - `Technical Expectations`: pending
 - `Last Update`: 2026-05-12
 - `Notes`: commit 9851fa0e - components/pipeline/PipelineUI.tsx+StageOutput.tsx+index.ts；PipelineUI(AsyncGenerator消费)+StageOutput(流式文本)+4阶段状态(pending/running/done/error)；push超时，待手动push

### P-20260512-009: ai-subscription-聚合推送持久化（Redis队列+定时发送）

 - `Proposal ID`: `P-20260512-009`
 - `Title`: ai-subscription-聚合推送持久化（Redis队列+定时发送）
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-009-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Last Update`: 2026-05-12
 - `Notes`: commit 581675ba - shared/lib/ai/push-queue/(types+storage-adapter+aggregation-service+scheduler+index)；web/src/services/push-queue/PushQueuePanel.tsx；IndexedDB持久化+setInterval定时调度+存储抽象层

### P-20260512-010: ai-subscription-对话历史持久化

 - `Proposal ID`: `P-20260512-010`
 - `Title`: ai-subscription-对话历史持久化
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-010-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Last Update`: 2026-05-12
 - `Notes`: commit 25111253 - shared/lib/ai/conversation-history/(types+storage+index)；conversation-manager.ts改造(依赖注入storage)；IndexedDB持久化+多会话管理+搜索

### P-20260512-011: ai-subscription-本地模型加载（WebLLM/Transformers.js）

 - `Proposal ID`: `P-20260512-011`
 - `Title`: ai-subscription-本地模型加载（WebLLM/Transformers.js）
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-011-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Last Update`: 2026-05-12
 - `Notes`: commit 6de46553 - shared/lib/ai/local-model/(types+model-registry+model-manager+index)；@mlc-ai/web-llm包；Qwen2-0.5B推理；inference-manager.ts改造(真实模型→关键词→云端三级降级)

### P-20260512-012: ai-subscription-成本告警系统（预算阈值+通知）

 - `Proposal ID`: `P-20260512-012`
 - `Title`: ai-subscription-成本告警系统（预算阈值+通知）
 - `Owner`: 小墨
 - `Current Status`: `approved_for_dev`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-012-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Acceptance`: pending
 - `PRD Confirmation`: `boss-selected-A`
 - `Technical Expectations`: pending
 - `Last Update`: 2026-05-12
 - `Notes`: 成本告警系统（阈值+通知+历史）

### P-20260512-003: 成就系统大改版

- `Proposal ID`: `P-20260512-002`
- `Title`: 成就系统大改版
- `Owner`: 小墨
- `Current Status`: active
- `PRD Path`: workspace-pm/proposals/P-20260512-002-prd.md
- `Project Path`: /home/hermes/cultivation-simulator
- `Acceptance`: pending
- `PRD Confirmation`: pending
- `Technical Expectations`: pending
- `Last Update`: 2026-05-12
- `Notes`: V28成就系统重制：30+成就/稀有度/赛季挑战/头像框气泡

### P-20260508-004: PixelPal V51 — MiniMax 清新浅色主题