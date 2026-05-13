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
- `Notes`: 家庭成员角色系统 + 任务归属 + 家庭共享任务池 + 宝宝头像优化 + 家庭数据概览；cron P-20260502-017-tech-confirm 重复触发(2026-05-11)，状态已存在，仅记录时间戳；再次触发(2027-05-13 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新

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
- `Last Update`: 2026-05-13
再次触发(2026-09-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-10-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-11-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2027-01-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2027-02-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2027-03-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2027-04-12 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2027-05-13 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-05-13 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新-13 cron P-20260502-017-tech-confirm 08:10)，状态已就绪，无需更新；再次触发(2027-05-13 cron P-20260502-017-tech-confirm 08:45)，状态已就绪，无需更新；再次触发(2026-05-13 06:00 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-05-14 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新；再次触发(2026-05-14 10:05 cron P-20260502-017-tech-confirm)，状态已就绪，无需更新

*最后更新：2026-05-14*

### P-20260513-001: AstrBot-Plugin-Marketplace

- `Proposal ID`: `P-20260513-001`
- `Title`: AstrBot-Plugin-Marketplace
- `Owner`: 小墨
- `Current Status`: `in_acceptance`
- `PRD Path`: `workspace-pm/proposals/P-20260513-001-prd.md`
- `Technical Solution`: `workspace-pm/proposals/P-20260513-001-prd.md#技术方案`
- `Project Path`: `/home/hermes/workspace-dev/proposals/astrbot-design/`
- `Acceptance`: `pending`
- `PRD Confirmation`: `confirmed` (boss selected: a/b = 轻量GitHub方案 + 必选签名)
- `Technical Expectations`: `confirmed`
- `Technical Stack`: 轻量方案（GitHub JSON + Actions），Ed25519 签名
- `Last Update`: 2026-05-13
- `Notes`: 已交付：18文件，docs构建成功，git push成功。Phase 1 MVP：插件列表/搜索/安装/卸载/更新，签名必选，安全扫描

### P-20260513-002: AstrBot-Multi-Agent-Collaboration

- `Proposal ID`: `P-20260513-002`
- `Title`: AstrBot-Multi-Agent-Collaboration
- `Owner`: 小墨
- `Current Status`: `in_acceptance`
- `PRD Path`: `workspace-pm/proposals/P-20260513-002-prd.md`
- `Technical Solution`: `workspace-pm/proposals/P-20260513-002-prd.md#技术方案`
- `Project Path`: `/home/hermes/workspace-dev/proposals/astrbot-design/`
- `Acceptance`: `pending`
- `PRD Confirmation`: `confirmed` (boss selected: b=async event-driven)
- `Technical Expectations`: `confirmed`
- `Technical Stack`: asyncio + Queue 事件驱动架构
- `Last Update`: 2026-05-13
- `Notes`: 已交付：13文件，Python语法验证通过，git push成功。MessageQueue/ContextPool/Agent基类/内置Teams/Dashboard/API

### P-20260513-003: AstrBot-Knowledge-Base-Enhancements

- `Proposal ID`: `P-20260513-003`
- `Title`: AstrBot-Knowledge-Base-Enhancements
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260513-003-prd.md`
- `Technical Solution`: `workspace-pm/proposals/P-20260513-003-prd.md#技术方案`
- `Project Path`: `/home/hermes/workspace-dev/proposals/astrbot-design/`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `confirmed` (boss selected: a/b = 本地模型 + LRU缓存)
- `Technical Stack`: sentence-transformers + FAISS + BM25 + Cross-Encoder + LRU
- `Last Update`: 2026-05-13
- `Notes`: 已交付：14文件，Python语法验证通过，git push成功。Hybrid Search/Reranker/Query Expander/Notion-Obsidian-Confluence/Episodic Memory

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

### P-20260512-007: 项目提案管理-导出收藏列表

- `Proposal ID`: `P-20260512-007`
- `Title`: 项目提案管理-导出收藏列表
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `Project Path`: `/home/hermes/workspace-dev/proposals/prj-proposals-manager`
- `Project`: `prj-proposals-manager`
- `Last Update`: 2026-05-12
- `Notes`: 收藏视图支持导出CSV（含项目信息+置顶状态+收藏时间）；commit 91513fa，GitHub Pages已部署

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
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-012-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Last Update`: 2026-05-12
 - `Notes`: commit 8b4b8010 - shared/lib/ai/cost-alert/(types+storage+notifier+alert-service+index)；CostAlertPanel.tsx；Browser Notification+面板通知；每日/周/月阈值+4级状态；routeAndCall后自动触发

### P-20260512-013: ai-subscription-文章Panel集成PipelineUI

 - `Proposal ID`: `P-20260512-013`
 - `Title`: ai-subscription-文章Panel集成PipelineUI
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-013-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Last Update`: 2026-05-12
 - `Notes`: commit 1be74a1a - ArticleDetail.tsx改造(AI处理按钮+PipelineUI集成+流式处理)；ArticleProcessResult.tsx；localStorage持久化

### P-20260512-014: ai-subscription-多语言推送支持（Telegram/Email/WebPush）

 - `Proposal ID`: `P-20260512-014`
 - `Title`: ai-subscription-多语言推送支持（Telegram/Email/WebPush）
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-014-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Last Update`: 2026-05-12
 - `Notes`: commit 2c7aad05 - shared/lib/ai/push-channel/(types+storage+telegram-sender+email-sender+webpush-sender+channel-service+index)；PushChannelPanel.tsx；Telegram/Email/WebPush三渠道+模板变量

### P-20260512-015: ai-subscription-订阅源智能分类（AI自动打标签）

 - `Proposal ID`: `P-20260512-015`
 - `Title`: ai-subscription-订阅源智能分类（AI自动打标签）
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-015-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Last Update`: 2026-05-12
 - `Notes`: commit beb728a2 - shared/lib/ai/feed-category/(types+storage+feed-analyzer+tag-recommender+feed-category-service+index)；FeedCategoryPanel.tsx；RSS AI分析+标签推荐+标签库

### P-20260512-016: ai-subscription-智能订阅源推荐（基于阅读历史）

 - `Proposal ID`: `P-20260512-016`
 - `Title`: ai-subscription-智能订阅源推荐（基于阅读历史）
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-016-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Last Update`: 2026-05-12
 - `Notes`: commit 915addea - shared/lib/ai/feed-recommend/(types+storage+interest-analyzer+similarity-engine+recommend-service+index)；FeedRecommendPanel.tsx；兴趣向量+余弦相似度+推荐理由

### P-20260512-017: ai-subscription-离线支持（Service Worker + 本地缓存）

 - `Proposal ID`: `P-20260512-017`
 - `Title`: ai-subscription-离线支持（Service Worker + 本地缓存）
 - `Owner`: 小墨
 - `Current Status`: `accepted`
 - `Acceptance`: `accepted`
 - `PRD Path`: `workspace-pm/proposals/P-20260512-017-prd.md`
 - `Project Path`: `/home/hermes/ai-subscription`
 - `Last Update`: 2026-05-12
 - `Notes`: commit cd97e833 - shared/lib/ai/offline/(types+cache-manager+sync-service+index)；web/sw.ts；OfflineIndicator.tsx；Service Worker注册+IndexedDB缓存+网络状态监听

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
### P-20260513-004: card-game-prototype V62 — Roguelike 完整体验

- `Proposal ID`: `P-20260513-004`
- `Title`: card-game-prototype V62 — Roguelike 完整体验
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260513-004-prd.md`
- `Project Path`: `/home/hermes/card-game-prototype`
- `Acceptance`: `accepted`
- `Last Update`: 2026-05-13
- `Notes`: commit 50aa412 - relics-loader.js(8遗物)+elite-loader.js(5精英+2Boss+章节节点)；V62代码已push，需验收

### P-20260513-007: card-game-prototype V63 — Meta进度 & 成就系统

- `Proposal ID`: `P-20260513-007`
- `Title`: card-game-prototype V63 — Meta进度 & 成就系统
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `Last Update`: 2026-05-13
- `Notes`: V63已部署到 https://yeluo45.github.io/card-game-prototype/

### P-20260513-008: card-game-prototype V64 — 战斗系统深化

- `Proposal ID`: `P-20260513-008`
- `Title`: card-game-prototype V64 — 战斗系统深化
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260513-008-prd.md`
- `Project Path`: `/home/hermes/card-game-prototype`
- `Acceptance`: `accepted`
- `Last Update`: 2026-05-13
- `Notes`: V64已部署到 https://yeluo45.github.io/card-game-prototype/ — 状态效果(虚弱/易伤/中毒/燃烧/力量)/新卡牌(fireball等)/手牌上限10张/能量检查

### P-20260513-009: card-game-prototype V65 — 敌人AI行为系统

- `Proposal ID`: `P-20260513-009`
- `Title`: card-game-prototype V65 — 敌人AI行为系统
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260513-009-prd.md`
- `Project Path`: `/home/hermes/card-game-prototype`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `pending`
- `Last Update`: 2026-05-14
- `Notes`: V65已部署到 https://yeluo45.github.io/card-game-prototype/ — EnemyAI类(5种策略)/Boss第二阶段/精英敌人标识/enemy-ai.js(5,644字节)

### P-20260514-001: card-game-prototype V66 — 视觉与音效系统

- `Proposal ID`: `P-20260514-001`
- `Title`: card-game-prototype V66 — 视觉与音效系统
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260514-001-prd.md`
- `Project Path`: `/home/hermes/card-game-prototype`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `pending`
- `Last Update`: 2026-05-14
- `Notes`: V66已部署到 https://yeluo45.github.io/card-game-prototype/ — 伤害飘字(damageFloat)+卡牌飞行动画(card-fly-to-enemy)+状态pulse(statusPulse)+AudioManager(Web Audio API)+敌人攻击闪红

### P-20260514-002: card-game-prototype V67 — 卡牌与遗物扩充

- `Proposal ID`: `P-20260514-002`
- `Title`: card-game-prototype V67 — 卡牌与遗物扩充
- `Owner`: 小墨
- `Current Status`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260514-002-prd.md`
- `Project Path`: `/home/hermes/card-game-prototype`
- `Acceptance`: `pending`
- `PRD Confirmation`: `pending`
- `Technical Expectations`: `pending`
- `Last Update`: 2026-05-14
- `Notes`: 新增15-20张卡牌(雷霆一击/吸血之刃等)+6个遗物(锈铁戒指/燃烧之核等)+稀有度分级(普通/稀有/传奇)+特殊词缀(lifesteal/critical/burn等)

### P-20260514-003: card-game-prototype V68 — 自动化测试用例覆盖

- `Proposal ID`: `P-20260514-003`
- `Title`: card-game-prototype V68 — 自动化测试用例覆盖
- `Owner`: 小墨
- `Current Status`: `approved_for_dev`
- `PRD Path`: `workspace-pm/proposals/P-20260514-003-prd.md`
- `Project Path`: `/home/hermes/card-game-prototype`
- `Acceptance`: `pending`
- `Technical Expectations`: `pending`
- `Last Update`: 2026-05-14
- `Notes`: Jest单元测试(card-effects/relic-effects/damage/status-effects)+Puppeteer E2E(battle-flow/ui-render)，覆盖率>80%

### P-20260513-005: GitHub Repo Manager V2 — 核心闭环真实化

- `Proposal ID`: `P-20260513-005`
- `Title`: GitHub Repo Manager V2 — 核心闭环真实化
- `Owner`: 小墨
- `Current Status`: `approved_for_dev`
- `PRD Path`: `workspace-pm/proposals/P-20260513-005-prd.md`
- `Project Path`: `/home/hermes/github-repo-manager`
- `Acceptance`: `pending`
- `Last Update`: 2026-05-13
- `Notes`: Build/Deploy/Scheduler 已实现但未充分验证；A1超时保护缺失、A3任务持久化缺失；Windows exe 打包需在 Windows 主机进行

### P-20260513-002: card-game-prototype V61 — 卡包市场 / 远程加载

- `Proposal ID`: `P-20260513-001`
- `Title`: card-game-prototype V60 — 卡牌插件系统
- `Owner`: 小墨
- `Current Status`: `approved_for_dev`
- `PRD Path`: `workspace-pm/proposals/P-20260513-001-prd.md`
- `Tech Solution Path`: `workspace-dev/proposals/card-game-prototype/P-20260513-001-tech-solution.md`
- `Project Path`: `/home/hermes/card-game-prototype`
- `Acceptance`: `pending`
- `PRD Confirmation`: `timeout-approved`
- `Technical Expectations`: `timeout-approved`
- `Timeout Resolution`: Q1=轻量方案（GitHub JSON + Actions），Q2=插件签名必选
- `Last Update`: 2026-05-13
- `Notes`: PRD确认超时(5min)，默认通过处理；技术诉求超时(5min)，默认通过：轻量方案（GitHub JSON + Actions），插件签名必选。现有已accepted状态为前置版本V60已完成交付，本次为新迭代提案记录。

### P-20260513-003: GitHub Repo Manager — 定时拉取 + 自动构建部署系统

- `Proposal ID`: `P-20260513-003`
- `Title`: GitHub Repo Manager — 定时拉取 + 自动构建部署系统
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260513-003-prd.md`
- `Project Path`: `/home/hermes/github-repo-manager`
- `Technical Expectations`: `timeout-approved`
- `Technical Stack`: `Vue 3 + Vite + Node.js (Express) + Electron + SQLite (better-sqlite3) + simple-git`
- `Technical Expectations Timeout Resolution`: 倒计时到期(2026-05-13)，按已确认技术栈默认通过
- `Delivery Notes`: dev subagent 超时(600s)，项目骨架已创建；main 修复 server/db/init.js electron require 问题；重建 better-sqlite3 兼容 Node 20；Vite build 成功；Electron Windows exe 需在 Windows 主机构建
- `Last Update`: 2026-05-13
- `Notes`: commit ed43353 + ff58a2c；Vue 3 + Node.js + Electron 项目骨架；Express + SQLite 后端(修复 electron 耦合)；Electron 主进程 + 托盘；npm run dev 正常

### P-20260513-002: Agent 记忆系统 — 跨 Session LLM 决策记忆

- `Proposal ID`: `P-20260513-002`
- `Title`: Agent 记忆系统 — 跨 Session LLM 决策记忆
- `Owner`: 小墨
- `Current Status`: `approved_for_dev`
- `PRD Path`: `workspace-pm/proposals/P-20260513-002-prd.md`
- `Tech Solution Path`: `workspace-dev/proposals/P-20260513-002-tech-solution.md`
- `Project Path`: (待分配)
- `Acceptance`: pending
- `PRD Confirmation`: `timeout-approved`
- `Technical Expectations`: `timeout-approved`
- `Technical Stack`: `asyncio + Queue（异步事件驱动）`
- `Timeout Resolution`: `Q=async event-driven（asyncio + Queue）`
- `Last Update`: 2026-05-13
- `Notes`: PRD 确认超时(2026-05-13 09:39)，按默认通过处理；Q=async event-driven（asyncio + Queue）；技术方案已输出

### P-20260514-001: PixelPal V98 — Agent 专业分工体系深化

- `Proposal ID`: `P-20260514-001`
- `Title`: PixelPal V98 — Agent 专业分工体系深化
- `Owner`: 小墨
- `Current Status`: `in_acceptance`
- `PRD Path`: `workspace-pm/proposals/P-20260514-001-prd.md`
- `Project Path`: `/home/hermes/pixel-pal-web`
- `Project`: `PRJ-20260420-002`
- `Acceptance`: pending
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `pending`
- `Last Update`: 2026-05-14
- `Notes`: dev交付完成，commit e8a270d，v98-agent-role-system分支，build成功(✓ 3.3s)；RoleSystem文件在src/services/agents/roleSystem/；init.ts/agentBus.ts/orchestratorAgent.ts已更新；待主Agent验收

### P-20260514-002: PixelPal V99 — Agent 自我进化与学习系统

- `Proposal ID`: `P-20260514-002`
- `Title`: PixelPal V99 — Agent 自我进化与学习系统
- `Owner`: 小墨
- `Current Status`: `approved_for_dev`
- `PRD Path`: `workspace-pm/proposals/P-20260514-002-prd.md`
- `Project Path`: `/home/hermes/pixel-pal-web`
- `Project`: `PRJ-20260420-002`
- `Acceptance`: pending
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: pending
- `Last Update`: 2026-05-14
- `Notes`: V98的自然延伸；ExecutionHistory执行追踪 + FailureCaseLibrary失败归因 + PromptEvolutionEngine动态优化 + AgentSelectionStrategy成功率选择 + AdaptiveThreshold学习型阈值

### P-20260513-006: ai-novel-assistant V23 — 一键三版本规划流程

- `Proposal ID`: `P-20260513-006`
- `Title`: ai-novel-assistant V23 — 一键三版本规划流程
- `Owner`: 小墨
- `Current Status`: `delivered`
- `PRD Path`: `workspace-pm/proposals/P-20260513-006-prd.md`
- `Project Path`: `/home/hermes/ai-novel-assistant`
- `Acceptance`: `delivered`
- `Last Update`: 2026-05-14
- `Notes`: V23完成，commit 53d1405，master分支；CreateProjectModal扩展字段 + VersionGeneratorPage三版本生成 + VersionSelector选择UI + RelationshipGraph关系图 + 数据模型扩展；build成功；GitHub Actions部署中

### P-20260514-001: prj-proposals-manager-个人数据仪表盘

- `Proposal ID`: `P-20260514-001`
- `Title`: prj-proposals-manager-个人数据仪表盘
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260514-001-prd.md`
- `Project Path`: `/home/hermes/workspace-dev/proposals/prj-proposals-manager`
- `Project`: `prj-proposals-manager`
- `Last Update`: 2026-05-13
- `Notes`: Dashboard视图新增：4统计卡片（总提案/Active/in_dev/本月新增）+项目分布饼图+月度趋势折线图+最近活跃提案列表+快捷入口；commit ae95401，GitHub Pages已部署

### P-20260514-002: trending-dashboard-社交协作功能

- `Proposal ID`: `P-20260514-002`
- `Title`: trending-dashboard 社交协作功能
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260514-002-prd.md`
- `Project`: `trending-dashboard`
- `Last Update`: 2026-05-14
- `Notes`: 社交协作功能已完成（收藏夹/精选分享/作者关注）；commit de95798 via API；GitHub Pages 已部署

### P-20260514-005: trending-dashboard-数据增强

- `Proposal ID`: `P-20260514-005`
- `Title`: trending-dashboard 数据增强
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260514-005-prd.md`
- `Project`: `trending-dashboard`
- `Last Update`: 2026-05-14
- `Notes`: 数据增强已完成（RisingBadge / SortControls / ProjectDetailPanel）；commit 2726406；GitHub Pages 已部署

### P-20260514-006: trending-dashboard-个性化智能

- `Proposal ID`: `P-20260514-006`
- `Title`: trending-dashboard 个性化智能
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260514-006-prd.md`
- `Project`: `trending-dashboard`
- `Last Update`: 2026-05-14
- `Notes`: 个性化智能已完成（RecommendationsPanel / TopicTrackingPanel / ReportsPanel）；commit 2a1ef15；GitHub Pages 已部署

### P-20260514-007: trending-dashboard-社交深化

- `Proposal ID`: `P-20260514-007`
- `Title`: trending-dashboard 社交深化
- `Owner`: 小墨
- `Current Status`: `approved_for_dev`
- `PRD Path`: `workspace-pm/proposals/P-20260514-007-prd.md`
- `Project`: `trending-dashboard`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `timeout-approved`
- `Last Update`: 2026-05-14
- `Description`: 评论系统 + 分享海报 + 通知提醒

### P-20260514-003: ai-subscription-Multi-Agent Pipeline架构升级

- `Proposal ID`: `P-20260514-003`
- `Title`: ai-subscription-Multi-Agent Pipeline架构升级
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260514-001-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Project`: `ai-subscription`
- `PRD Confirmation`: `timeout-approved`
- `Technical Expectations`: `timeout-approved`
- `Last Update`: 2026-05-14
- `Notes`: 交付完成；commit 36e1e371；MessageBus+ContextPool+6 Agent类+content-pipeline-team；并行执行tagger+translator；CriticAgent评分+降级；PipelineUI critic展示；修复pre-existing CostAlertService导出bug；build成功(22.5s)

### P-20260514-004: ai-subscription-Pipeline Dashboard可视化

- `Proposal ID`: `P-20260514-004`
- `Title`: ai-subscription-Pipeline Dashboard可视化
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260514-004-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Project`: `ai-subscription`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `confirmed`
- `Last Update`: 2026-05-14
- `Notes`: 交付完成；commit 181c7be6；5个新组件：AgentNodeCard+MessageFlow+ContextViewer+CriticTimeline+PipelineDashboard；ArticleDetail添加Dashboard入口按钮；build成功

### P-20260514-005: ai-subscription-自定义Agent注册机制

- `Proposal ID`: `P-20260514-005`
- `Title`: ai-subscription-自定义Agent注册机制
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `PRD Path`: `workspace-pm/proposals/P-20260514-005-prd.md`
- `Project Path`: `/home/hermes/ai-subscription`
- `Project`: `ai-subscription`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `confirmed`
- `Last Update`: 2026-05-14
- `Notes`: 交付完成；commit ee4ef6ec；AgentRegistry单例+IndexedDB持久化；AgentRegistrationPanel注册面板（表单+测试+列表）；CoordinatorAgent集成registry调度；build成功(23.5s)

### P-20260514-006: ai-subscription-条件路由

- `Proposal ID`: `P-20260514-006`
- `Title`: ai-subscription-条件路由
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `confirmed`
- `Last Update`: 2026-05-14
- `Notes`: 交付完成；commit b496af33；Conditional Routing路由条件（minContentLength/maxContentLength/requiresVision/preference）；RouterModelInfo增强；findModelForTask评分路由；routeTaskWithConditions；build成功(23.8s)

### P-20260514-007: ai-subscription-订阅源智能分类

- `Proposal ID`: `P-20260514-007`
- `Title`: ai-subscription-订阅源智能分类
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `confirmed`
- `Last Update`: 2026-05-14
- `Notes`: 交付完成；commit 78cf0677；集成 feed-category 模块到订阅流程；scheduler.ts 自动触发AI分类；FeedList.tsx增加智能分类菜单和FeedCategoryPanel；build成功(21s)

### P-20260514-008: ai-subscription-智能订阅源推荐

- `Proposal ID`: `P-20260514-008`
- `Title`: ai-subscription-智能订阅源推荐
- `Owner`: 小墨
- `Current Status`: `accepted`
- `Acceptance`: `accepted`
- `PRD Confirmation`: `confirmed`
- `Technical Expectations`: `confirmed`
- `Last Update`: 2026-05-14
- `Notes`: 交付完成；commit fc08a7d8；集成已有feed-recommend模块（similarity-engine+interest-analyzer+recommend-service）；FeedList.tsx导航集成FeedRecommendPanel；build成功(19.4s)
