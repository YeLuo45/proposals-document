# Proposal Index

## Active Proposals

### P-20260428-001: 3D打地鼠 V1

- `Proposal ID`: `P-20260428-001`
- `Title`: 3D打地鼠 V1 (Whack-a-Mole 3D)
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: Three.js 0.160.0 (CDN) + Vanilla JS
- `Target`: Web Browser
- `Game Type`: 3D Casual Game
- `Stage`: Delivered (V1)
- `Project Path`: `/mnt/c/Users/YeZhimin/Desktop/whack-a-mole-3d/`
- `GitHub Repo`: https://github.com/YeLuo45/whack-a-mole-3d
- `Deployment URL`: https://yeluo45.github.io/whack-a-mole-3d/
- `Last Update`: 2026-04-28
- `Notes`: 3D打地鼠；Three.js WebGL场景；3x3地洞矩阵；可爱地鼠模型（程序化生成）；弹性动画；射线检测击中；准星+30秒倒计时
- `Acceptance`: accepted

---

### P-20260429-001: 3D打地鼠 V2 — 道具/关卡/皮肤系统

- `Proposal ID`: `P-20260429-001`
- `Title`: 3D打地鼠 V2 — 道具/关卡/皮肤系统
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20260428-001（3D打地鼠系列）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260429-001-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/P-20260429-001-tech-solution.md
- `Project Path`: /mnt/c/Users/YeZhimin/Desktop/whack-a-mole-3d/
- `GitHub Repo`: https://github.com/YeLuo45/whack-a-mole-3d
- `Deployment URL`: https://yeluo45.github.io/whack-a-mole-3d/
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Last Update`: 2026-04-29
- `Notes`: V2迭代已完成交付；M1关卡系统(3世界×10关+星级)+M2道具系统(3即时+3被动+金币体力)+M3皮肤系统(5地鼠+4锤子+盲盒)；index.html 1490→2545行；合并远程master冲突已解决；分支feature/v2-progression已合并到master；localStorage存档key: whackamole_v2_save
- `Acceptance`: accepted

---

### P-20260430-001: 3D打地鼠 V3 — 每日任务+经济循环

- `Proposal ID`: `P-20260430-001`
- `Title`: 3D打地鼠 V3 — 每日任务+经济循环
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20260428-001（3D打地鼠系列）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260430-001-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/P-20260430-001-002-tech-solution.md
- `Project Path`: /mnt/c/Users/YeZhimin/Desktop/whack-a-mole-3d/
- `GitHub Repo`: https://github.com/YeLuo45/whack-a-mole-3d
- `Deployment URL`: https://yeluo45.github.io/whack-a-mole-3d/
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Last Update`: 2026-04-30
- `Notes`: 每日签到(7天循环)+每日任务(5个)+每周任务(2个)+体力上限15+火焰护盾/熔岩冻结道具
- `Acceptance`: accepted

---

### P-20260430-002: 3D打地鼠 V3 — 新世界+Boss战

- `Proposal ID`: `P-20260430-002`
- `Title`: 3D打地鼠 V3 — 新世界+Boss战
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20260428-001（3D打地鼠系列）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260430-002-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/P-20260430-001-002-tech-solution.md
- `Project Path`: /mnt/c/Users/YeZhimin/Desktop/whack-a-mole-3d/
- `GitHub Repo`: https://github.com/YeLuo45/whack-a-mole-3d
- `Deployment URL`: https://yeluo45.github.io/whack-a-mole-3d/
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Last Update`: 2026-04-30
- `Notes`: 世界4熔岩(第31-40关)+火焰Boss巨人(血条+连续击中机制)+熔岩视觉效果
- `Acceptance`: accepted

---

### P-20260430-003: 3D打地鼠 V4 — 无尽模式

- `Proposal ID`: `P-20260430-003`
- `Title`: 3D打地鼠 V4 — 无尽模式
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project`: PRJ-20260428-001（3D打地鼠系列）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260430-003-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/P-20260430-003-004-005-tech-solution.md
- `Project Path`: /mnt/c/Users/YeZhimin/Desktop/whack-a-mole-3d/
- `GitHub Repo`: https://github.com/YeLuo45/whack-a-mole-3d
- `Deployment URL`: https://yeluo45.github.io/whack-a-mole-3d/
- `Stage`: V4 Iteration
- `Engine`: Three.js 0.160.0 (CDN) + Vanilla JS (单文件)
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Timeout Resolution`: 倒计时到期(2026-05-01)，默认通过处理
- `Technical Expectations`: timeout-approved（技术栈继承V3：Three.js 0.160.0 CDN + Vanilla JS 单文件）
- `Technical Stack`: V3 继承：Three.js 0.160.0 CDN + Vanilla JS 单文件
- `Last Update`: 2026-05-01
- `Notes`: 无尽模式+60秒倒计时+难度递进+连击加成+本地Top5排行榜；技术方案联合P-004/P-005；已验收通过（README.md记录）。无尽模式入口+60秒倒计时+难度递进（间隔/停留/双鼠）+连击加分+Top5排行榜+localStorage存档已实现。

---

### P-20260430-004: 3D打地鼠 V4 — 成就系统

- `Proposal ID`: `P-20260430-004`
- `Title`: 3D打地鼠 V4 — 成就系统
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project`: PRJ-20260428-001（3D打地鼠系列）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260430-004-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/P-20260430-003-004-005-tech-solution.md
- `Project Path`: /mnt/c/Users/YeZhimin/Desktop/whack-a-mole-3d/
- `GitHub Repo`: https://github.com/YeLuo45/whack-a-mole-3d
- `Deployment URL`: https://yeluo45.github.io/whack-a-mole-3d/
- `Stage`: V4 Iteration
- `Engine`: Three.js 0.160.0 (CDN) + Vanilla JS (单文件)
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Timeout Resolution`: 倒计时到期(2026-05-01)，默认通过处理
- `Technical Expectations`: timeout-approved（技术栈继承V3：Three.js 0.160.0 CDN + Vanilla JS 单文件）
- `Technical Stack`: V3 继承：Three.js 0.160.0 CDN + Vanilla JS 单文件
- `Last Update`: 2026-05-01
- `Notes`: 成就系统+13个成就+解锁提示+金币奖励；技术方案联合P-003/P-005；已验收通过（README.md记录）。13个成就（first_hit/combo/score/皮肤收集/签到/无尽/Boss/通关）+ 检测点散布各节点 + 成就按钮/列表/解锁提示已实现。

---

### P-20260430-005: 3D打地鼠 V4 — 音效+震动反馈

- `Proposal ID`: `P-20260430-005`
- `Title`: 3D打地鼠 V4 — 音效+震动反馈
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project`: PRJ-20260428-001（3D打地鼠系列）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260430-005-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/P-20260430-003-004-005-tech-solution.md
- `Project Path`: /mnt/c/Users/YeZhimin/Desktop/whack-a-mole-3d/
- `GitHub Repo`: https://github.com/YeLuo45/whack-a-mole-3d
- `Deployment URL`: https://yeluo45.github.io/whack-a-mole-3d/
- `Stage`: V4 Iteration
- `Engine`: Three.js 0.160.0 (CDN) + Vanilla JS (单文件)
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Timeout Resolution`: 倒计时到期(2026-05-01)，默认通过处理
- `Technical Expectations`: timeout-approved（技术栈继承V3：Three.js 0.160.0 CDN + Vanilla JS 单文件）
- `Technical Stack`: V3 继承：Three.js 0.160.0 CDN + Vanilla JS 单文件
- `Last Update`: 2026-05-01
- `Notes`: Web Audio API合成音效+震动反馈+音效开关；技术方案联合P-003/P-004；已验收通过（README.md记录）。AudioManager（10种Web Audio API合成音效）+ Navigator.vibrate + 音效开关 + 音效调用链路（beat/miss/click/levelup）已全部接入。

---

### P-20260502-001: prj-proposals-manager — 项目管理增强

- `Proposal ID`: `P-20260502-001`
- `Title`: prj-proposals-manager — 项目管理增强
- `Owner`: 小墨
- `Current Status`: accepted
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `Notes`: 项目详情页（独立路由 /project/:id）+ 里程碑管理（CRUD + 时间线 + 提案关联）; PRD 倒计时到期(2026-05-02)，默认通过处理; 技术期望倒计时到期(2026-05-02)，默认通过处理; 仓库已从 proposals-manager 更名为 prj-proposals-manager; 今日修复：useGitHub.js中REPO名修正为prj-proposals-manager（匹配实际仓库名）；构建时复制data/到dist/确保gh-pages包含proposals.json；GitHub Token验证功能正常；79个提案/34个项目数据已同步

---

### P-20260503-028: prj-proposals-manager V4 — 看板泳道 + 全局搜索 + 批量操作

- `Proposal ID`: `P-20260503-028`
- `Title`: prj-proposals-manager V4 — 看板泳道 + 全局搜索 + 批量操作
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `Notes`: 三个功能同步推进：①看板泳道（按状态/项目/负责人分组）②全局搜索+高级筛选（Fuse.js + 多条件组合）③批量操作（多选+批量移动/分配/标签/关联里程碑）；V4构建成功，GitHub Actions部署完成，泳道视图已集成到App.jsx，FilterBar添加泳道切换按钮；泳道视图数据复用优化：嵌入式模式使用App传入的props，独立模式保持原有数据获取；本次P0优化：嵌入式模式直接使用filteredProjects/filteredProposals实现搜索同步、折叠状态localStorage持久化、拖拽目标高亮显示

---

### P-20260503-V8-001: prj-proposals-manager V8 — Dashboard 增强

- `Proposal ID`: `P-20260503-V8-001`
- `Title`: prj-proposals-manager V8 — Dashboard 增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V8-001-prd.md
- `Tech Solution Path`: proposals/workspace-dev/proposals/prj-proposals-manager/P-20260503-V8-001-tech-solution.md
- `Notes`: V8 Dashboard增强：M1提案趋势折线图（近6个月新增数量）、M2状态分布环形饼图（待办/进行中/已完成）、M3项目进度条形图（各项目完成率排序）、M4时间范围筛选（7天/30天/3月/全部）；Chart.js+react-chartjs-2，深色模式适配；构建成功，GitHub Actions部署

---

### P-20260505-V30-001: prj-proposals-manager V30 — 模板市场

- `Proposal ID`: `P-20260505-V30-001`
- `Title`: prj-proposals-manager V30 — 模板市场
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V30-001-prd.md
- `Dev Commit`: a7e6687
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: builtinTemplates.js（12个内置模板）；templateMarketplaceService.js（CRUD/评分/收藏/导入导出）；TemplateCard.jsx（分类badge/评分/使用次数）；TemplateRating.jsx（5星交互式评分）；TemplateMarketplace.jsx（搜索/筛选/排序/收藏/导入导出模态框）；Header导航；main.jsx /marketplace路由；i18n翻译；构建成功，GitHub Actions部署

---

### P-20260505-V31-001: prj-proposals-manager V31 — 提案草稿系统

- `Proposal ID`: `P-20260505-V31-001`
- `Title`: prj-proposals-manager V31 — 提案草稿系统
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V31-001-prd.md
- `Dev Commit`: 3fc7dcf
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: PRD已起草；M1自动草稿保存（30秒间隔+离开触发，7天过期）；M2草稿恢复提示；M3版本历史记录（localStorage，最多10个版本）；M4版本对比视图（Diff高亮+恢复到指定版本）

---

### P-20260505-V29-001: prj-proposals-manager V29 — 数据看板增强

- `Proposal ID`: `P-20260505-V29-001`
- `Title`: prj-proposals-manager V29 — 数据看板增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V29-001-prd.md
- `Dev Commit`: e2c9a09
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: BurndownChart.jsx（燃尽图/实际vs理想线）；VelocityChart.jsx（6个月完成数vs计划数）；WorkloadChart.jsx（横向堆叠柱状图）；analytics.js（calculateBurndown/Velocity/Workload）；Dashboard.jsx集成；useStatsData.js添加新数据计算；构建成功，GitHub Actions部署

---

### P-20260505-V28-001: prj-proposals-manager V28 — 数据导入导出增强

- `Proposal ID`: `P-20260505-V28-001`
- `Title`: prj-proposals-manager V28 — 数据导入导出增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V28-001-prd.md
- `Dev Commit`: df073a2
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: excelImporter.js（xlsx解析/getExcelSheets/detectColumnMapping/transformExcelRows）；pdfReportGenerator.js（Summary/Project/Full报告+统计图表）；backupService.js（generateBackupData/downloadBackup/自动备份）；restoreService.js（parseBackupFile/validateRestoreData/executeRestore/恢复预览）；csvImporter.js增强；xlsx@0.18.5依赖；构建成功，GitHub Actions部署

---

### P-20260505-V27-001: prj-proposals-manager V27 — AI 辅助功能

- `Proposal ID`: `P-20260505-V27-001`
- `Title`: prj-proposals-manager V27 — AI 辅助功能
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V27-001-prd.md
- `Dev Commit`: d79c2e4
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: aiService.js（MiniMax API/classifyProposal/generateSummary）；AISettings（API Key配置）；ProposalForm AI按钮（type推荐/tags推荐）；App.jsx（handleAIClassify/loadingAI/aiRecommendations状态）；AI功能已实现并随V26一起提交

---

### P-20260505-V26-001: prj-proposals-manager V26 — 国际化增强

- `Proposal ID`: `P-20260505-V26-001`
- `Title`: prj-proposals-manager V26 — 国际化增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V26-001-prd.md
- `Dev Commit`: d79c2e4
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: ar.json（阿拉伯语）+ he.json（希伯来语）；i18n.js（isRTL/getDirection/applyDirection + LanguageDetector）；LanguageSwitcher（4语言下拉+RTL badge）；ProposalForm（多语言表单字段nameAr/nameHe/descriptionAr/descriptionHe）；ProposalCard（本地化显示）；index.css（RTL样式200+行）；index.html（Direction FOUC prevention）；构建成功，GitHub Actions部署

---

### P-20260505-V25-001: prj-proposals-manager V25 — API 集成增强 V2

- `Proposal ID`: `P-20260505-V25-001`
- `Title`: prj-proposals-manager V25 — API 集成增强 V2
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V25-001-prd.md
- `Dev Commit`: 2779696
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: githubIssues.js（Issues CRUD + PR管理 + PR关联 + Labels + Milestones）；GitHubIssuePanel（三标签界面+创建Issue表单+PR关联选择）；SyncContext（SYNC_TYPE枚举+triggerIssuesSync+自动同步Issues）；i18n（githubIssues + autoSync命名空间）；构建成功，GitHub Actions部署

---

### P-20260505-V24-001: prj-proposals-manager V24 — 高级筛选增强

- `Proposal ID`: `P-20260505-V24-001`
- `Title`: prj-proposals-manager V24 — 高级筛选增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V24-001-prd.md
- `Dev Commit`: 06ba8d3
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: AdvancedFilter（AND/OR组合逻辑切换/状态类型标签多选/日期范围/关键词）；SavedFilters（保存/加载/重命名/删除筛选方案）；savedFiltersStore localStorage持久化；BatchActionBar（批量导出/设置标签）；i18n翻译；构建成功，GitHub Actions部署

---

### P-20260505-V23-001: prj-proposals-manager V23 — 高级甘特图

- `Proposal ID`: `P-20260505-V23-001`
- `Title`: prj-proposals-manager V23 — 高级甘特图
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V23-001-prd.md
- `Dev Commit`: fa04b0f
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: GanttBar里程碑菱形SVG；GanttDependencyArrows SVG贝塞尔曲线依赖箭头；criticalPath.js关键路径算法（forward/backward pass）；GanttChart index依赖箭头层+关键路径计算；milestones.json isMilestone/dependencies/progress字段；构建成功，GitHub Actions部署

---

### P-20260505-V22-001: prj-proposals-manager V22 — 移动端适配

- `Proposal ID`: `P-20260505-V22-001`
- `Title`: prj-proposals-manager V22 — 移动端适配
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V22-001-prd.md
- `Dev Commit`: 4363ae6
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: BottomNav（手机底部Tab/4个Tab/响应式）；SwipeableCard（touch事件/60px阈值触发）；index.css（safe-area/44px触摸/滚动）；KanbanSwimlanes响应式（desktop-header/drawer/列头md:block）；ProposalCard/SwimlaneCard swipe handlers；修复KanbanSwimlanes tag mismatch + 'as const' 语法错误；构建成功，GitHub Actions部署

---

### P-20260505-V21-001: prj-proposals-manager V21 — API 集成增强

- `Proposal ID`: `P-20260505-V21-001`
- `Title`: prj-proposals-manager V21 — API 集成增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V21-001-prd.md
- `Dev Commit`: 16f39c3
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: GitHubApiService（fetchProposals/saveProposals/validateToken，UTF-8中文处理）；SyncContext（自动同步开关/同步间隔/待处理变更/在线监听）；SyncSettings（Token验证/自动同步/手动同步）；SyncStatusIndicator（compact/full/badge模式）；SyncProvider包裹应用；i18n翻译；构建成功，GitHub Actions部署

---

### P-20260505-V20-001: prj-proposals-manager V20 — 协作增强

- `Proposal ID`: `P-20260505-V20-001`
- `Title`: prj-proposals-manager V20 — 协作增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V20-001-prd.md
- `Dev Commit`: 35c77d2
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: historyService（按日期分组/创建更新删除）；commentService（回复/点赞/删除）；HistoryTimeline（日期分组+相对时间）；CommentsPanel（输入/回复/删除）；ProjectDetailPage Tab切换（详情/历史/评论）；i18n collaboration翻译；构建成功，GitHub Actions部署

---

### P-20260505-V19-001: prj-proposals-manager V19 — 键盘快捷键

- `Proposal ID`: `P-20260505-V19-001`
- `Title`: prj-proposals-manager V19 — 键盘快捷键
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V19-001-prd.md
- `Dev Commit`: 1c9d18d
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: useKeyboardShortcuts hook；Ctrl+N/F/+/T等快捷键；KeyboardShortcutsModal帮助面板（分类+中英双语）；Header快捷键按钮；SearchBar Ctrl+F提示；i18n翻译；构建成功，GitHub Actions部署

---

### P-20260505-V18-001: prj-proposals-manager V18 — 通知提醒系统

- `Proposal ID`: `P-20260505-V18-001`
- `Title`: prj-proposals-manager V18 — 通知提醒系统
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V18-001-prd.md
- `Dev Commit`: ed65afa
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: useToast hook（success/error/warning/info）；ToastContainer（类型颜色+图标+动画）；ProposalDeadlineBadge（过期/今天/明天标记4种variant）；NotificationCenter（右侧抽屉+筛选+已读标记）；i18n翻译；构建成功，GitHub Actions部署

---

### P-20260505-V17-001: prj-proposals-manager V17 — 数据导出 + 深色模式完善

- `Proposal ID`: `P-20260505-V17-001`
- `Title`: prj-proposals-manager V17 — 数据导出 + 深色模式完善
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update**: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V17-001-prd.md
- `Dev Commit`: 6366ff6
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: exportUtils（html2canvas PNG + jsPDF PDF）；ExportPanel导出按钮；ThemeSwitcher 4色主题切换；ThemeContext；深色模式全面适配；jspdf@2.5.1；构建成功，GitHub Actions部署

---

### P-20260505-V16-001: prj-proposals-manager V16 — 多语言支持

- `Proposal ID`: `P-20260505-V16-001`
- `Title`: prj-proposals-manager V16 — 多语言支持
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V16-001-prd.md
- `Dev Commit`: 5a42b49
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: react-i18next + i18next + LanguageDetector；zh.json/en.json翻译；LanguageSwitcher组件；全组件i18n化（Header/FilterBar/ProposalForm/ProposalCard/AISettings等）；localStorage持久化；构建成功，GitHub Actions部署

---

### P-20260505-V15-001: prj-proposals-manager V15 — 看板模板

- `Proposal ID`: `P-20260505-V15-001`
- `Title`: prj-proposals-manager V15 — 看板模板
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-05
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V15-001-prd.md
- `Dev Commit`: f35b501
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: templateService（4预设模板+localStorage CRUD）；TemplateMenu组件（预设/自定义切换+保存/加载/删除）；KanbanBoard集成；构建成功，GitHub Actions部署

---

### P-20260503-V14-001: prj-proposals-manager V14 — PWA 离线支持

- `Proposal ID`: `P-20260503-V14-001`
- `Title`: prj-proposals-manager V14 — PWA 离线支持
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V14-001-prd.md
- `Dev Commit`: a1c74f8
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: manifest.json PWA配置；sw.js Service Worker（Cache First静态+Network First API）；icons图标（SVG+PNG）；PWA meta标签；OfflineIndicator离线提示；构建成功，GitHub Actions部署

---

### P-20260503-V13-001: prj-proposals-manager V13 — 看板/甘特图融合

- `Proposal ID`: `P-20260503-V13-001`
- `Title`: prj-proposals-manager V13 — 看板/甘特图融合
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V13-001-prd.md
- `Dev Commit`: 2ca9598
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: 视图切换器（看板/甘特图）；GanttChart zoom支持day/week/month；GanttHeader日周月时间轴；GanttBar拖拽调整开始/截止时间+进度百分比；按里程碑分组；构建成功，GitHub Actions部署

---

### P-20260503-V12-001: prj-proposals-manager V12 — 性能优化

- `Proposal ID`: `P-20260503-V12-001`
- `Title`: prj-proposals-manager V12 — 性能优化
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V12-001-prd.md
- `Dev Commit`: 7a60eb9
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: 首屏JS 148KB < 300KB；highlight.js替代react-syntax-highlighter；路由懒加载；Vite manualChunks拆包（react/chart/markdown/dnd/highlight vendor chunks）；构建成功，GitHub Actions部署

---

### P-20260503-V11-001: prj-proposals-manager V11 — Markdown 渲染

- `Proposal ID`: `P-20260503-V11-001`
- `Title`: prj-proposals-manager V11 — Markdown 渲染
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V11-001-prd.md
- `Tech Solution Path`: proposals/workspace-dev/proposals/prj-proposals-manager/P-20260503-V11-001-tech-solution.md
- `Dev Commit`: 6936d32
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Notes`: 提案描述支持 Markdown 渲染 + 代码高亮 + 编辑/预览切换；react-markdown + remark-gfm + react-syntax-highlighter + @tailwindcss/typography；GFM 表格/任务列表/删除线；构建成功，GitHub Actions 部署

---

### P-20260503-V10-001: prj-proposals-manager V10 — AI 增强

- `Proposal ID`: `P-20260503-V10-001`
- `Title`: prj-proposals-manager V10 — AI 增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V10-001-prd.md
- `Tech Solution Path`: proposals/workspace-dev/proposals/prj-proposals-manager/P-20260503-V10-001-tech-solution.md
- `Notes`: V10 AI增强：M1自动分类（描述输入后AI推荐type+tags，点击采纳）、M2摘要生成（描述>50字自动生成一句话摘要）、M3智能建议（基于项目历史推荐常用标签）、M4重复检测（余弦相似度检测，相似>60%警告）；MiniMax API，用户配置API Key；构建成功，GitHub Actions部署

---

### P-20260503-V9-001: prj-proposals-manager V9 — 高级筛选增强

- `Proposal ID`: `P-20260503-V9-001`
- `Title`: prj-proposals-manager V9 — 高级筛选增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V9-001-prd.md
- `Tech Solution Path`: proposals/workspace-dev/proposals/prj-proposals-manager/P-20260503-V9-001-tech-solution.md
- `Notes`: V9高级筛选增强：M1筛选模板（localStorage保存/切换/删除，最多10个）、M2日期范围筛选（创建时间/更新时间+快捷按钮）、M3多标签AND/OR逻辑组合、M4筛选结果批量导出CSV；构建成功，GitHub Actions部署

---

### P-20260503-V7-001: prj-proposals-manager V7 — 看板增强

- `Proposal ID`: `P-20260503-V7-001`
- `Title`: prj-proposals-manager V7 — 看板增强
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V7-001-prd.md
- `Tech Solution Path`: proposals/workspace-dev/proposals/prj-proposals-manager/P-20260503-V7-001-tech-solution.md
- `Notes`: V7看板增强：M1泳道列折叠+持久化（单元格独立折叠）、M2泳道内独立筛选（每个泳道行独立搜索+类型过滤）、M3看板专注模式（按项目/状态快速过滤）、M4列宽拖拽（150-500px可调+localStorage持久化）；构建成功，GitHub Actions部署

---

### P-20260503-V6-001: prj-proposals-manager V6 — 导入导出

- `Proposal ID`: `P-20260503-V6-001`
- `Title`: prj-proposals-manager V6 — 导入导出
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V6-001-prd.md
- `Tech Solution Path`: proposals/workspace-dev/proposals/prj-proposals-manager/P-20260503-V6-001-tech-solution.md
- `Notes`: V6新增导入导出功能：M1 CSV导出（所有提案字段+项目名+里程碑名）、M2 CSV批量导入（预览+三种模式：跳过/覆盖/新ID）、M3 JSON备份导出（完整projects.json结构+metadata）、M4 JSON备份恢复（二次确认+自动备份当前）；构建成功，GitHub Actions部署

---

### P-20260503-V5-001: prj-proposals-manager V5 — 数据校验与操作历史

- `Proposal ID`: `P-20260503-V5-001`
- `Title`: prj-proposals-manager V5 — 数据校验与操作历史
- `Owner`: 小墨
- `Parent`: PRJ-20260417-001
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-V5-001-prd.md
- `Notes`: V5引入数据健康度保障：M1数据校验（提案Schema校验，保存前拦截）、M2操作历史（localStorage记录增删改，最多100条）、M3撤销功能（Ctrl+Z或撤销按钮回退到before状态）、M4健康指示器UI（Header右侧绿/黄/红圆点）、M5数据完整性检查（孤立提案/无效里程碑/重复ID）、M6一键修复；构建成功，GitHub Actions部署

---

### P-20260503-AB: Ash Echoes V2 — 内容扩展 + Roguelite变体

- `Proposal ID`: `P-20260503-AB`
- `Title`: Ash Echoes V2 — 内容扩展 + Roguelite变体
- `Owner`: 小墨
- `Project`: PRJ-20260422-002（Ash Echoes 残响纪元）
- `Stage`: V2 Iteration
- `Current Status`: delivered
- `Dev Commits`: bee50a1(本地) → API force-push 0ef1ae9
- `Deployed`: https://yeluo45.github.io/ash-echoes/
- `Last Update`: 2026-05-04
- `Notes`: A+B综合方向：M1章节扩展(第2+3章共12关+2Boss+新武器)+M2 Roguelite变体(无限关卡+永久解锁+每日挑战)+M3共享(武器切换+存档重构)

---

### P-20260504-C+D: Ash Echoes V3 — 角色扩展 + 硬核挑战模式

- `Proposal ID`: `P-20260504-C+D`
- `Title`: Ash Echoes V3 — 角色扩展 + 硬核挑战模式
- `Owner`: 小墨
- `Project`: PRJ-20260422-002（Ash Echoes 残响纪元）
- `Stage`: V3 Iteration
- `Current Status`: delivered
- `Dev Commits`: V2: 0ef1ae9；V3 base: 46d7820(本地)；gh-pages: bdf5342(远程API)
- `Deployed`: https://yeluo45.github.io/ash-echoes/（V3 JS last-modified: 2026-05-04 10:04）
- `Last Update`: 2026-05-04
- `Notes`: V3 base骨架已部署。三名角色(艾文/莲/熔)+独立技能树+角色剧情线+专属武器；BossRush/SpeedRun/Suffering/NoHit硬核挑战模式均已打包。构建+部署通过。技术栈：Phaser 3.60+ CDN + Vanilla JS 单文件HTML。
- `GitHub Repo`: https://github.com/YeLuo45/ash-echoes
- `Last Update`: 2026-05-04
- `PRD Confirmation`: timeout-approved
- `Technical Expectations`: confirmed（技术栈继承V2：Phaser 3.60+ CDN + Vanilla JS 单文件HTML）

---

### P-20260505-001: Ash Echoes V4 — 内容扩张

- `Proposal ID`: `P-20260505-001`
- `Title`: Ash Echoes V4 — 内容扩张
- `Owner`: 小墨
- `Project`: PRJ-20260422-002（Ash Echoes 残响纪元）
- `Stage`: V4 Iteration
- `Current Status`: delivered
- `Dev Commits`: adda833(M3/M4) → d95fdc1(M1/M2) → 978576f(merge)
- `Deployed`: https://yeluo45.github.io/ash-echoes/（V4 JS: 151KB）
- `Last Update`: 2026-05-05
- `Notes`: V4内容扩张交付完成。M1新章节(Ch4废墟都市12关+Ch5地下基地12关+Ch6核心区域10关)+M2新敌人(9种)+M3精英系统(每章3个)+M4Boss设计(废墟之王/基地指挥官/核心意志)+M5地图扩展。npm run build成功(151KB JS)。技术栈：Phaser 3.60+ CDN + Vanilla JS。
- `GitHub Repo`: https://github.com/YeLuo45/ash-echoes
- `Deployed`: https://yeluo45.github.io/ash-echoes/
- `Acceptance`: accepted

---

### P-20260502-002: TodoList 迭代增强（轻量化+看板视图）

- `Proposal ID`: `P-20260502-002`
- `Title`: TodoList 迭代增强（轻量化+看板视图）
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20250416-001（todo-list）& PRJ-20260417-001（prj-proposals-manager）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-002-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/todo-list/P-20260502-002-tech-solution.md
- `Stage`: V2（轻量化增强）+ V3（看板视图）
- `Acceptance`: accepted
- `Notes`: V2轻量化增强已完成（优先级P0/P1/P2+标签筛选+截止日期排序+搜索过滤），部署于 https://yeluo45.github.io/todo-list/；V3看板视图已集成到todo-list项目（列表/看板视图切换，三列看板+原生拖拽），URL不变；看板使用HTML5原生Drag and Drop API实现，不需要额外依赖
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Timeout Resolution`: 倒计时到期(2026-05-02 00:45)，默认通过处理
- `Technical Expectations`: confirmed
- `Last Update`: 2026-05-02

---

### P-20260427-001: 3D飞行棋大作战

- `Proposal ID`: `P-20260427-001`
- `Title`: 3D飞行棋大作战 (Flight Chess 3D)
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 18 + Vite 5 + Three.js (@react-three/fiber)
- `Target`: Web Browser (Desktop)
- `Game Type`: 3D Board Game / Local Multiplayer
- `Mode`: Classic (传统) + Event (事件模式)
- `Stage`: Delivered
- `PRD Path`: proposals/workspace-pm/proposals/P-20260427-001-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/flight-chess-3d/P-20260427-001-tech-solution.md
- `Project Path`: proposals/workspace-dev/proposals/flight-chess-3d/
- `GitHub Repo`: https://github.com/YeLuo45/flight-chess-3d
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Acceptance`: accepted
- `Last Update`: 2026-04-28
- `Notes`: 3D卡通飞行棋；React Three Fiber 3D渲染；传统模式+事件模式(幸运/厄运/传送/交换)；2-4人本地对战；Roblox风格卡通渲染；60FPS目标；workflow修复id-token权限后部署成功

---

### P-20260504-001: 3D飞行棋 V2 — 主题皮肤 + 地图变体

- `Proposal ID`: `P-20260504-001`
- `Title`: 3D飞行棋 V2 — 主题皮肤 + 地图变体
- `Owner`: 小墨
- `Parent`: PRJ-20260427-001（3D飞行棋系列）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Commits`: 14a72b4
- `Deployed`: https://yeluo45.github.io/flight-chess-3d/
- `Last Update`: 2026-05-04
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-001-prd.md
- `Project Path`: proposals/workspace-dev/proposals/flight-chess-3d/
- `GitHub Repo`: https://github.com/YeLuo45/flight-chess-3d
- `Stage`: V2 Iteration
- `Last Update`: 2026-05-04
- `Notes`: 6种皮肤(Classic/Space/Ocean/Candy/Dinosaur/ChineseNewYear) + 3种地图(Standard/Ring/Hexagonal)；皮肤切换改颜色材质，地图变体改轨道结构；解锁系统：成就/登录/游戏次数

---

### P-20260504-002: 3D飞行棋 V3 — AI对手

- `Proposal ID`: `P-20260504-002`
- `Title`: 3D飞行棋 V3 — AI对手
- `Owner`: 小墨
- `Parent`: PRJ-20260427-001（3D飞行棋系列）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Commits`: e1309d5
- `Deployed`: https://yeluo45.github.io/flight-chess-3d/
- `Last Update`: 2026-05-04
- `Notes`: 简单/中等/困难三档AI；AI决策评估体系(前进/捕获/安全/事件格)；AI思考动画(2秒/1.5秒/1秒)；AIvsAI演示模式；修复跑道移动逻辑与游戏规则一致性

---

### P-20260504-003: 3D飞行棋 V3 — PWA离线支持

- `Proposal ID`: `P-20260504-003`
- `Title`: 3D飞行棋 V3 — PWA离线支持
- `Owner`: 小墨
- `Parent`: PRJ-20260427-001（3D飞行棋系列）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Commits`: fcc80ca
- `Deployed`: https://yeluo45.github.io/flight-chess-3d/
- `Last Update`: 2026-05-04
- `Notes`: manifest.json配置 + Service Worker + Cache First策略 + 离线指示器 + 添加到桌面支持；手动PWA方案避免peer-deps冲突

---

### P-20260504-004: 3D飞行棋 V4 — 成就系统

- `Proposal ID`: `P-20260504-004`
- `Title`: 3D飞行棋 V4 — 成就系统
- `Owner`: 小墨
- `Parent`: PRJ-20260427-001（3D飞行棋系列）
- `Current Status`: in_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: timeout-approved（继承V1技术栈）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-004-prd.md
- `Project Path`: proposals/workspace-dev/proposals/flight-chess-3d/
- `GitHub Repo`: https://github.com/YeLuo45/flight-chess-3d
- `Stage`: V4 Iteration
- `Last Update`: 2026-05-04
- `Notes`: 15个成就(胜利/技巧/模式/特殊)+金币奖励+通知弹窗+成就面板

---

### P-20260504-005: 3D飞行棋 V4 — 录像回放

- `Proposal ID`: `P-20260504-005`
- `Title`: 3D飞行棋 V4 — 录像回放
- `Owner`: 小墨
- `Parent`: PRJ-20260427-001（3D飞行棋系列）
- `Current Status`: in_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: timeout-approved（继承V1技术栈）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-005-prd.md
- `Project Path`: proposals/workspace-dev/proposals/flight-chess-3d/
- `GitHub Repo`: https://github.com/YeLuo45/flight-chess-3d
- `Stage`: V4 Iteration
- `Last Update`: 2026-05-04
- `Notes`: 录像录制(moves序列)+localStorage存储(最多10局)+回放播放器(1x/2x/4x+进度条)

---

### P-20260504-006: 3D飞行棋 V4 — 观战模式

- `Proposal ID`: `P-20260504-006`
- `Title`: 3D飞行棋 V4 — 观战模式
- `Owner`: 小墨
- `Parent`: PRJ-20260427-001（3D飞行棋系列）
- `Current Status`: in_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: timeout-approved（继承V1技术栈）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-006-prd.md
- `Project Path`: proposals/workspace-dev/proposals/flight-chess-3d/
- `GitHub Repo`: https://github.com/YeLuo45/flight-chess-3d
- `Stage`: V4 Iteration
- `Last Update`: 2026-05-04
- `Notes`: 房间码+WebSocket实时同步+观众只读视角+主机控制投骰/选棋

---

### P-20260422-001: 解谜游戏原型验证

- `Proposal ID`: `P-20260422-001`
- `Title`: 解谜游戏原型验证
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: Godot 4 + GDScript
- `Target`: PC, Mobile, Browser (HTML5)
- `Stage`: Prototype Validation
- `PRD Path`: proposals/workspace-pm/proposals/P-20260422-001-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/P-20260422-001-tech-solution.md
- `Project Path`: proposals/workspace-dev/proposals/room-escape-puzzle/
- `GitHub Repo`: https://github.com/YeLuo45/room-escape-puzzle
- `Deployment URL`: https://resonant-frangipane-46af83.netlify.app/
- `Last Update`: 2026-04-23
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Acceptance`: accepted

---

### P-20260422-002: 2.5D 侧视角射击游戏

- `Proposal ID`: `P-20260422-002`
- `Title`: 2.5D 侧视角射击游戏（Soulslike Shooter）
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: Godot 4 + GDScript / HTML5 Canvas + JS
- `Target`: PC (HTML5)
- `Game Type`: 2.5D Side-Scrolling Shooter
- `Mode`: Single-player Story Campaign
- `Stage`: MVP
- `Last Update`: 2026-04-22
- `Notes`: 街机快节奏射击；枪/近战/技能+弹药+翻滚+格挡+弹反+跳跃+蹬墙；1关卡+多敌人+存档点+Boss；像素风2D+程序化场景；WSL网络受限，HTML5版用纯JS实现；PRD超时默认通过
- `Clarifying Round 1`: 核心玩法(街机快节奏/枪近战技能/弹药翻滚格挡弹反跳跃蹬墙)/MVP范围(1关卡多敌人存档点Boss)/美术风格(像素风2D渲染程序生成) — 已明确
- `PRD Path`: proposals/workspace-pm/proposals/P-20260422-002-prd.md
- `Project Path`: proposals/workspace-dev/proposals/ash-echoes/
- `GitHub Repo`: https://github.com/YeLuo45/ash-echoes
- `Deployment URL`: https://yeluo45.github.io/ash-echoes/
- `Acceptance`: accepted
- `PRD Confirmation`: timeout-approved
- `Technical Expectations`: confirmed

---

### P-20250421-001: DBG卡牌游戏原型验证

- `Proposal ID`: `P-20250421-001`
- `Title`: DBG卡牌游戏原型验证
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/card-game-prototype/`
- `Acceptance`: accepted
- `Deployment URL`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Engine`: HTML5 Canvas + Vanilla JS
- `Last Update`: 2026-04-21
- `Notes`: DBG类卡牌（杀戮尖塔-like）；原型验证核心战斗循环+卡牌构筑；本地化中文；已交付

---

### P-20260502-003: DBG卡牌游戏 V2 — 卡牌扩充 + 敌人扩充

- `Proposal ID`: `P-20260502-003`
- `Title`: DBG卡牌游戏 V2 — 卡牌扩充 + 敌人扩充
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-003-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/card-game-prototype/P-20260502-003-tech-solution.md
- `Project Path`: /mnt/c/Users/YeZhimin/Desktop/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Deployment URL`: https://yeluo45.github.io/card-game-prototype/
- `Stage`: V2 Iteration
- `Engine`: HTML5 Canvas + Vanilla JS (单文件)
- `Acceptance`: accepted
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Timeout Resolution`: 倒计时到期（2026-05-02），默认通过处理
- `Technical Expectations`: timeout-approved（技术栈继承 v1：HTML5 Canvas + Vanilla JS 单文件）
- `Technical Expectations Timeout Resolution`: 倒计时到期（2026-05-02），技术方案已存在，默认通过
- `Last Update`: 2026-05-02
- `Notes`: V2迭代：13张初始牌（4打击+4防御+2硬撑+2连续打击+1痛击）+12张新卡牌+5种debuff+5敌人+1Boss+战斗日志+胜利选牌

---

### P-20260502-015: DBG卡牌游戏 V7 — 敌人与Boss扩充

- `Proposal ID`: `P-20260502-015`
- `Title`: DBG卡牌游戏 V7 — 敌人与Boss扩充
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-015-prd.md
- `Stage`: V7 Iteration
- `Current Status`: accepted
- `Dev Commit`: 8ab31c1
- `Acceptance`: boss于2026-05-02验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-02

---

---

### P-20260503-008: DBG卡牌游戏 V16 — 卡组辅助系统

- `Proposal ID`: `P-20260503-008`
- `Title`: DBG卡牌游戏 V16 — 卡组辅助系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-008-prd.md
- `Stage`: V16 Iteration
- `Current Status`: accepted
- `Dev Commit`: cb9a487
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03

---

### P-20260503-009: DBG卡牌游戏 V17 — 牌组管理系统 + 卡牌升级扩展

- `Proposal ID`: `P-20260503-009`
- `Title`: DBG卡牌游戏 V17 — 牌组管理系统 + 卡牌升级扩展
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-009-prd.md
- `Stage`: V17 Iteration
- `Current Status`: delivered
- `Dev Commit`: 82d7230
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-03
- `Notes`: 牌组管理（浏览/移除/规模限制）+ 卡牌升级扩展（100%覆盖）；文件5396行

---

### P-20260503-015: DBG卡牌游戏 V23 — PWA 应用化

- `Proposal ID`: `P-20260503-015`
- `Title`: DBG卡牌游戏 V23 — PWA 应用化
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-015-prd.md
- `Stage`: V23 Iteration
- `Current Status`: delivered
- `Dev Commit`: 1684355
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: manifest.json；sw.js；离线缓存；apple-mobile-web-app标签；文件7295行

---

### P-20260503-016: DBG卡牌游戏 V24 — 成就系统

- `Proposal ID`: `P-20260503-016`
- `Title`: DBG卡牌游戏 V24 — 成就系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-016-prd.md
- `Stage`: V24 Iteration
- `Current Status`: delivered
- `Dev Commit`: 1684355
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: 18个成就；成就检查/解锁函数；触发点绑定；成就面板；持久化；文件7295行

---

### P-20260503-018: prj-proposals-manager V3 — 甘特图视图

- `Proposal ID`: `P-20260503-018`
- `Title`: prj-proposals-manager V3 — 甘特图视图
- `Owner`: 小墨
- `Project`: PRJ-20260417-001（prj-proposals-manager）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-018-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/prj-proposals-manager/P-20260503-018-tech-solution.md
- `Stage`: V3 Iteration
- `Current Status`: delivered
- `Dev Commit`: 7de49a5
- `Acceptance`: 小墨于2026-05-03验收通过
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Last Update`: 2026-05-03
- `Notes`: 里程碑时间线可视化；自研甘特图（CSS + React）；支持拖拽调整日期；看板/甘特图视图切换；React Router 路由集成；Header 导航 Tab

---

### P-20260503-019: prj-proposals-manager V3 — 数据统计仪表板

- `Proposal ID`: `P-20260503-019`
- `Title`: prj-proposals-manager V3 — 数据统计仪表板
- `Owner`: 小墨
- `Project`: PRJ-20260417-001（prj-proposals-manager）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-019-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/prj-proposals-manager/P-20260503-019-tech-solution.md
- `Stage`: V3 Iteration
- `Current Status`: delivered
- `Dev Commit`: 7de49a5
- `Acceptance`: 小墨于2026-05-03验收通过
- `Deployed`: https://yeluo45.github.io/prj-proposals-manager/
- `Last Update`: 2026-05-03
- `Notes`: 提案数量趋势（折线图）+ 项目进度（环形图）+ 里程碑完成率 + 最近活动时间线；Chart.js 实现；指标卡（总数/本月新增/进行中/已完成）

---

### P-20260503-P0-001: prj-proposals-manager V4 — 看板泳道（Swimlanes）

- `Proposal ID`: `P-20260503-P0-001`
- `Title`: prj-proposals-manager V4 — 看板泳道（Swimlanes）
- `Owner`: 小墨
- `Project`: PRJ-20260417-001（prj-proposals-manager）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-P0-001-prd.md
- `Stage`: V4 Iteration
- `Current Status`: approved_for_dev
- `Acceptance`: pending
- `PRD Confirmation`: timeout-approved（倒计时5分钟自动通过）
- `Technical Expectations`: timeout-approved（技术栈继承V3）
- `Last Update`: 2026-05-03
- `Notes`: 泳道路由/拖拽改变状态/泳道折叠展开；技术栈继承V3：React+Vite+@dnd-kit+Tailwind+React Router

---

### P-20260503-P0-002: prj-proposals-manager V4 — 全局搜索 + 高级筛选

- `Proposal ID`: `P-20260503-P0-002`
- `Title`: prj-proposals-manager V4 — 全局搜索 + 高级筛选
- `Owner`: 小墨
- `Project`: PRJ-20260417-001（prj-proposals-manager）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-P0-002-prd.md
- `Stage`: V4 Iteration
- `Current Status`: approved_for_dev
- `Acceptance`: pending
- `PRD Confirmation`: timeout-approved（倒计时5分钟自动通过）
- `Technical Expectations`: timeout-approved（技术栈继承V3）
- `Last Update`: 2026-05-03
- `Notes`: 搜索增强(ID/URL)+高级筛选面板(多状态/类型/标签/项目/日期)+URL同步+搜索历史

---

### P-20260503-P0-003: prj-proposals-manager V4 — 批量操作

- `Proposal ID`: `P-20260503-P0-003`
- `Title`: prj-proposals-manager V4 — 批量操作
- `Owner`: 小墨
- `Project`: PRJ-20260417-001（prj-proposals-manager）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-P0-003-prd.md
- `Stage`: V4 Iteration
- `Current Status`: approved_for_dev
- `Acceptance`: pending
- `PRD Confirmation`: timeout-approved（倒计时5分钟自动通过）
- `Technical Expectations`: timeout-approved（技术栈继承V3）
- `Last Update`: 2026-05-03
- `Notes`: 多选复选框+批量移动状态+批量删除+批量关联里程碑；多选状态存储在App state

---

### P-20260503-017: DBG卡牌游戏 V25 — 宠物/同伴系统

- `Proposal ID`: `P-20260503-017`
- `Title`: DBG卡牌游戏 V25 — 宠物/同伴系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-017-prd.md
- `Stage`: V25 Iteration
- `Current Status`: delivered
- `Dev Commit`: db85b29
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: 8种宠物；宠物效果函数；宠物商店UI；装备/卸下；保存加载；文件7748行

---

### P-20260508-003: DBG卡牌游戏 V30 — 更多卡牌类型 + 章节扩展

- `Proposal ID`: `P-20260508-003`
- `Title`: DBG卡牌游戏 V30 — 更多卡牌类型 + 章节扩展
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260508-003-prd.md
- `Stage`: V30 Iteration
- `Current Status`: delivered
- `Dev Commit`: 495d0c5
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-03
- `Notes`: 诅咒系6张(痛苦/虚弱/黑暗/死亡诅咒+毒镖/恐惧)+命运系6张(打击/护盾/孤注一掷/骰子/蛮横/难以预测)+第8章(克洛诺斯Boss3阶段)+真终局(熵Boss无限循环)；文件9555行
- `Acceptance`: delivered

---

### P-20260508-002: DBG卡牌游戏 V29 — Roguelike变体

- `Proposal ID`: `P-20260508-002`
- `Title`: DBG卡牌游戏 V29 — Roguelike变体
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260508-002-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/card-game-prototype/P-20260508-002-tech-solution.md
- `Stage`: V29 Iteration
- `Current Status`: delivered
- `Dev Commit`: 0358fa3
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-03
- `Notes`: 随机起始牌组(8-12张)+遗物3选1+随机初始资源+SeededRandom确定性随机+每日挑战(seed+排行榜)+3新事件(骰子/赌博/祭坛)；文件9250行
- `Acceptance`: delivered

---

### P-20260504-002: PixelPal V44 — Webhook + 插件生态

- `Proposal ID`: `P-20260504-002`
- `Title`: PixelPal V14 — Webhook + 插件生态
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: delivered
- `PRD Path`: workspace-pm/proposals/P-20260504-002-intake.md
- `Stage`: V14 Iteration

---

### P-20260504-003: PixelPal V15 — Desktop Electron 打包

- `Proposal ID`: `P-20260504-003`
- `Title`: PixelPal V15 — Desktop Electron 打包
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Branch`: v15-desktop-electron
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Project Path`: /home/hermes/.hermes/proposals/workspace-dev/proposals/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260504-003-intake.md
- `Stage`: V15 Iteration
- `Last Update`: 2026-05-04
- `Notes`: Desktop Electron 打包 — exe 安装包(106MB NSIS) + 系统托盘 + 开机自启 + 原生通知 + GitHub Actions CI 构建成功 artifact: PixelPal Setup 1.0.0.exe
- `Notes`: Desktop Electron 打包 — exe 安装包 + 系统托盘 + 开机自启 + 原生通知; electron/tray.ts(托盘+右键菜单+通知); electron/main.ts已重构; .github/workflows/build-electron.yml已添加; npm run build成功(exit code 0); dist/main/main.js + preload.js已生成; v15-desktop-electron分支已push; CI构建Windows exe workflow就绪; P0全部完成; P1(自启/最小化到托盘/原生通知)已实现

---

### P-20260504-006: PixelPal V17 — 对话式语音

- `Proposal ID`: `P-20260504-006`
- `Title`: PixelPal V17 — 对话式语音
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Branch`: v17-conversational-voice
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Project Path`: /home/hermes/.hermes/proposals/workspace-dev/proposals/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260504-006-intake.md
- `Stage`: V17 Iteration
- `Last Update`: 2026-05-04

---

### P-20260504-007: PixelPal V18 — 插件系统

- `Proposal ID`: `P-20260504-007`
- `Title`: PixelPal V18 — 插件系统
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Branch`: v18-plugin-system
- `Dev Commit`: fb36f40
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Project Path`: /home/hermes/.hermes/proposals/workspace-dev/proposals/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260504-007-plugin-system.md
- `Stage`: V18 Iteration
- `Last Update`: 2026-05-04
- `Notes`: 插件架构核心 + 天气/新闻/Webhook 三个官方插件 + PluginHub 管理界面

---

### P-20260504-008: PixelPal V19 — 移动端适配

- `Proposal ID`: `P-20260504-008`
- `Title`: PixelPal V19 — 移动端适配
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: in_acceptance
- `Dev Branch`: v19-mobile-adaptation
- `Dev Commit`: 54cc971
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Project Path`: /home/hermes/.hermes/proposals/workspace-dev/proposals/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260504-008-mobile-adaptation.md
- `Stage`: V19 Iteration
- `Last Update`: 2026-05-04
- `Notes`: 响应式 Sidebar（手机抽屉/平板折叠/桌面展开）+ PWA 离线支持（多级缓存 SW）+ 离线横幅 + 触摸优化。npm run build 通过。push 因网络阻塞失败，commit 留存本地待网络恢复。

---

### P-20260505-V20-001: PixelPal V20 — 对话增强：情感识别 + 情绪跟踪

- `Proposal ID`: `P-20260505-V20-001`
- `Title`: PixelPal V20 — 对话增强：情感识别 + 情绪跟踪
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Commit`: 5dd7b48
- `Dev Branch`: v20-emotion-tracking
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Project Path`: /home/hermes/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260505-V20-001-prd.md
- `Stage`: V20 Iteration
- `Last Update`: 2026-05-05
- `Notes`: P0全部完成：情绪识别(关键词引擎7分类)、情绪时间轴(Chart.js曲线)、当前情绪状态(Sidebar emoji+文字)、JSON导出；P1全部完成：情绪预警(负面情绪3+天)、情绪分布柱状图、情绪统计(连续天数/最高频/平均强度)；构建环境有node版本问题(需要Node 22+)，代码已push

---

### P-20260505-V24-001: PixelPal V24 — 人格对话历史独立视图

- `Proposal ID`: `P-20260505-V24-001`
- `Title`: PixelPal V24 — 人格对话历史独立视图
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Branch`: v24-persona-history
- `GitHub Commit`: dc2bc1e
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Project Path`: /home/hermes/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260505-V24-001-prd.md
- `Stage`: V24 Iteration
- `Last Update`: 2026-05-05
- `Notes`: P0—ChatPanel按人格过滤历史消息、messages按人格归档(persist key分离)、人格聊天历史列表(按时间分组)、消息搜索按人格过滤；P1—人格间消息转发、按人格导出、时间线可视化

---

### P-20260505-V23-001: PixelPal V23 — 人格提示词系统

- `Proposal ID`: `P-20260505-V23-001`
- `Title`: PixelPal V23 — 人格提示词系统
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Branch`: v23-persona-prompt
- `GitHub Commit`: bff1469
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Project Path`: /home/hermes/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260505-V23-001-prd.md
- `Stage`: V23 Iteration
- `Last Update`: 2026-05-05
- `Notes`: P0—persona system prompt动态生成(生物+voice标签)、人格切换更新AI context、ChatPanel集成persona prompt、voice标签影响回复风格(warm/rational/humorous/serious)；P1—实时预览prompt、自定义prompt覆盖、prompt模板市场

---

### P-20260505-V22-001: PixelPal V22 — 记忆人格绑定强化

- `Proposal ID`: `P-20260505-V22-001`
- `Title`: PixelPal V22 — 记忆人格绑定强化
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Branch`: v22-memory-persona-binding
- `GitHub Commit`: 2120676
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Project Path`: /home/hermes/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260505-V22-001-prd.md
- `Stage`: V22 Iteration
- `Last Update`: 2026-05-05
- `Notes`: P0—MemoryPanel按人格过滤、人格切换自动刷新记忆、记忆标签显人格头像、addMemory自动注入personaId；P1—人格记忆统计、跨人格记忆共享

---

### P-20260505-V21-002: PixelPal V21 — 多人格系统

- `Proposal ID`: `P-20260505-V21-002`
- `Title`: PixelPal V21 — 多人格系统
- `Owner`: 小墨
- `Project`: PRJ-20260420-002（pixel-pal-web）
- `Current Status`: delivered
- `Acceptance`: accepted
- `Dev Branch`: v21-persona-isolation
- `GitHub Commit`: a564868
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Project Path`: /home/hermes/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260505-V21-001-prd.md
- `Stage`: V21 Iteration
- `Last Update`: 2026-05-05
- `Notes`: P0—人格创建(名称/头像/简介/语气标签)、人格切换(Selector)、人格独立记忆(personaId隔离)、人格独立对话上下文；P1—预设人格模板(朋友/老师/教练/恋人)、人格删除、人格拖拽排序

---

### P-20260504-001: DBG卡牌游戏 V42 — 牌组升级 + 能量石 + 扭蛋系统

- `Proposal ID`: `P-20260504-001`
- `Title`: DBG卡牌游戏 V42 — 牌组升级 + 能量石 + 扭蛋系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-002-prd.md
- `Stage`: V42 Iteration
- `Current Status`: delivered
- `Dev Commit`: c7cc80e
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-04
- `Notes`: 新增能量石(⚡)资源系统+扭蛋抽卡(消耗10⚡石)+卡牌升级(消耗1⚡石/级)+战斗后概率获得能量石+奖励界面扭蛋按钮
- `Acceptance`: delivered

---

### P-20260504-003: DBG卡牌游戏 V43 — Roguelike进度系统
- `Proposal ID`: `P-20260504-003`
- `Title`: DBG卡牌游戏 V43 — Roguelike进度系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-003-prd.md
- `Stage`: V43 Iteration
- `Current Status`: approved_for_dev
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-04
- `Notes`: 累计能量石/胜场解锁新卡牌，永久成就奖励，localStorage持久化
- `Acceptance`: pending

---

### P-20260504-004: DBG卡牌游戏 V44 — 宠物系统完善
- `Proposal ID`: `P-20260504-004`
- `Title`: DBG卡牌游戏 V44 — 宠物系统完善
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-004-prd.md
- `Stage`: V44 Iteration
- `Current Status`: approved_for_dev
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-04
- `Notes`: 宠物技能树激活，宠物助战主动/被动技能，4种宠物（史莱姆/火精灵/冰霜巨人/雷龙）
- `Acceptance`: pending

---

### P-20260504-001: DBG卡牌游戏 V41 — 战斗牌组选择 + 页面切换效果

- `Proposal ID`: `P-20260504-001`
- `Title`: DBG卡牌游戏 V41 — 战斗牌组选择 + 页面切换效果
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-001-prd.md
- `Stage`: V40 Iteration
- `Current Status`: delivered
- `Dev Commit`: 0c87811
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-04
- `Notes`: 开始游戏时，开始画面淡出过渡效果；战斗牌组选择系统 - 3个预设牌组（基础/攻击/防御）
- `Acceptance`: delivered

---

### P-20260504-007: DBG卡牌游戏 V47 — 卡牌升级 + 卡牌出售

- `Proposal ID`: `P-20260504-007`
- `Title`: DBG卡牌游戏 V47 — 卡牌升级 + 卡牌出售
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-007-prd.md
- `Stage`: V47 Iteration
- `Current Status`: delivered
- `Dev Commit`: 73b9e87
- `Acceptance`: pending

---

### P-20260504-008: DBG卡牌游戏 V48 — 卡组预览面板

- `Proposal ID`: `P-20260504-008`
- `Title`: DBG卡牌游戏 V48 — 卡组预览面板
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-008-prd.md
- `Stage`: V48 Iteration
- `Current Status`: delivered
- `Dev Commit`: dd6860e (fix: b73ff8c)
- `Acceptance`: accepted

---

### P-20260503-020: future-little-leaders V2 — 成长激励 + 亲子互动

- `Proposal ID`: `P-20260503-020`
- `Title`: future-little-leaders V2 — 成长激励 + 亲子互动
- `Owner`: 小墨
- `Project`: PRJ-20260508（future-little-leaders）
- `PRD Path`: `P-20260503-020-v2-prd.md`
- `Technical Solution`: `P-20260503-020-v2-tech-solution.md`
- `Stage`: V2 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: confirmed
- `Feature Branch`: `feature/hermes20260503`
- `Current Status`: delivered
- `Dev Commits`: 306189b (M1) / 7d7c31f (M2) / e87e3d1 (M3) / 5752204 (M4) / a53de3a (M5) / c4ba3bd (M6)
- `Last Update`: 2026-05-05
- `Acceptance`: 小墨于2026-05-05验收通过（M6 build成功）
- `Notes`: V2 功能规划：M1成就系统(18徽章)/M2成长报告(周报月报)/M3任务模板(10预设)/M4商城增强/M5宝宝等级/M6任务提醒
- `P0 模块`:
  - M1 成就系统（18个成就徽章，4类：坚持/数量/收集/特殊）✅ 已完成 (306189b)
  - M2 成长报告（周报 + 月报，数据摘要 + 鼓励文案）✅ 已完成 (7d7c31f)
  - M3 任务模板（10个预设模板 + 自定义模板）✅ 已完成 (e87e3d1)
  - M4 商城增强（分类筛选/收藏/兑换码）✅ 已完成 (5752204)
  - M5 宝宝等级（等级页/经验值进度/特权/等级一览）✅ 已完成 (a53de3a)
  - M6 任务提醒（reminderStore + 通知中心 + 添加任务集成）✅ 已完成 (c4ba3bd)

---

### P-20260503-021: snake-battle V2 — 道具系统 + 无尽模式

- `Proposal ID`: `P-20260503-021`
- `Title`: snake-battle V2 — 道具系统 + 无尽模式
- `Owner`: 小墨
- `Project`: PRJ-20260420-001（snake-battle）
- `PRD Path`: `workspace-pm/proposals/snake-battle/P-20260503-021-prd.md`
- `Stage`: V2 Iteration
- `Engine`: HTML5 Canvas + Vanilla JS（继承V1）
- `GitHub Repo`: https://github.com/YeLuo45/snake-battle
- `Deployment URL`: https://yeluo45.github.io/snake-battle/
- `Current Status`: delivered
- `Dev Commit`: 40ebf58
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/snake-battle/
- `GitHub Repo`: https://github.com/YeLuo45/snake-battle
- `Last Update`: 2026-05-03
| `Notes`: M1道具系统(6种：加速/减速/护盾/穿墙/磁铁/猛长)+M2无尽模式(波次递进+排行榜)+M3 HUD增强
| `M1 道具系统`:
  - Speed Up（+50%速度，5秒）/ Speed Down（-40%速度，5秒）
  - Shield（免疫一次死亡，单次）/ Ghost（穿墙，4秒）
  - Magnet（食物吸附，6秒）/ Growth（立即+3节，即时）
  - 地图同时最多2个道具，8-12秒生成，仅玩家生效，AI不受影响
| `M2 无尽模式`:
  - 每波次吃完食物进入下一波，速度+5%/波、食物间隔+10%/波
  - 波次系数得分，撞墙/撞自身结束，显示Top5排行榜(localStorage)
  - Wave Announce 淡入淡出提示

---

### P-20260503-022: snake-battle V3 — 内容巨型更新

- `Proposal ID`: `P-20260503-022`
- `Title`: snake-battle V3 — 内容巨型更新
- `Owner`: 小墨
- `Project`: PRJ-20260420-001（snake-battle）
- `PRD Path`: `workspace-pm/proposals/snake-battle/P-20260503-022-prd.md`
- `Stage`: V3 Iteration
- `Engine`: HTML5 Canvas + Vanilla JS（继承V1/V2）
- `GitHub Repo`: https://github.com/YeLuo45/snake-battle
- `Deployment URL`: https://yeluo45.github.io/snake-battle/
- `Current Status`: delivered
- `Dev Commits`: 40ebf58(V2道具)→V3M1(道具)→97edd9a(V3M4AI人格)
- `Acceptance`: 小墨于2026-05-03验收通过
- `Deployed`: https://yeluo45.github.io/snake-battle/
- `Last Update`: 2026-05-03
- `Notes`: M1新道具6种(Invisible/Clone/Mine/Portal/Shrink/Reverse)+M2 BOSS战(10血量/冲刺AI)+M3地图变化(5种地图/障碍物/安全区/传送门)+M4新AI人格(Aggressive/Random)

---

### P-20260503-023: snake-battle V4 — 成就系统 + 赛季通行证

- `Proposal ID`: `P-20260503-023`
- `Title`: snake-battle V4 — 成就系统 + 赛季通行证
- `Owner`: 小墨
- `Project`: PRJ-20260420-001（snake-battle）
- `PRD Path`: `workspace-pm/proposals/snake-battle/P-20260503-023-prd.md`
- `Stage`: V4 Iteration（方向B — 养成向）
- `Engine`: Canvas + Vanilla JS（继承V1-V3）
- `Deployment URL`: https://yeluo45.github.io/snake-battle/
- `Current Status`: delivered
- `Acceptance`: pending
- `Dev Commit`: main branch (M1+M2+M3 merged)
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Timeout Resolution`: 倒计时到期（2026-05-03），默认通过处理
- `Technical Expectations`: timeout-approved（技术栈继承V1-V3：Canvas + Vanilla JS + React/Vite，localStorage持久化）
- `Technical Solution`: proposals/workspace-dev/proposals/snake-battle/P-20260503-023-tech-solution.md
- `Last Update`: 2026-05-03
- `Notes`: M1成就系统(100+成就/4分类/解锁称号头像框)+M2赛季通行证(30天/50级/免费付费区分)+M3每日挑战(每天3个随机/00:00刷新)+继承V1-V3全部功能；dev于2026-05-03交付；M1: AchievementPanel+useAchievements+achievements.js(123成就)；M2: SeasonPassPanel+useSeasonPass+seasonPass.js；M3: DailyChallengePanel+useDailyChallenge+challenges.js(23类型)

---

### P-20260503-022: snake-battle V3 — 内容巨型更新

- `Proposal ID`: `P-20260503-021`
- `Title`: creative-drawing-board V2 — 功能扩展
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-021-prd.md
- `Stage`: V2 Iteration
- `Current Status`: delivered
- `Dev Commit`: d89a5dd
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `PRD Confirmation`: confirmed
- `Technical Expectations`: timeout-approved（技术栈继承 V1：HTML5 Canvas + Vanilla JS 单文件，零外部依赖）
- `Last Update`: 2026-05-03
- `Notes`: M1贴纸印章(24个SVG)/M2描红模板(8张)/M3区域填色(扫描线算法)/M4背景场景(6种)/M5涂色游戏(4张)+Undo/Redo/Save；V1单文件745行→V2 1981行；gh-pages强制更新部署

---

### P-20260503-025: creative-drawing-board V3 — 音效增强 + 内容扩展

- `Proposal ID`: `P-20260503-025`
- `Title`: creative-drawing-board V3 — 音效增强 + 内容扩展
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-025-prd.md
- `Stage`: V3 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: M1音效引擎(Web Audio API程序化生成，11种音效)+M2贴纸扩展(24→56个)+M3描红扩展(8→20张)+M4涂色扩展(4→10张)+M5背景扩展(6→10种)+全局静音开关；V2 1981行→V3 2401行
- `Dev Commit`: b611161

---

### P-20260504-061: creative-drawing-board V38 — 每日挑战

- `Proposal ID`: `P-20260504-061`
- `Title`: creative-drawing-board V38 — 每日挑战
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-061-prd.md
- `Stage`: V38 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 12种每日挑战+4种限时任务+排行榜+连续打卡+金币奖励+每日重置+倒计时条；V37 23567行→V38 23910行
- `Dev Commit`: cbeba6b

---

### P-20260504-062: creative-drawing-board V39 — 动画书

- `Proposal ID`: `P-20260504-062`
- `Title`: creative-drawing-board V39 — 动画书
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-062-prd.md
- `Stage`: V39 Iteration
- `Current Status`: delivered
- `Dev Commit`: d65d71d
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: M1翻页动画书(📖按钮/多页管理/缩略图/翻页/播放控制)+M3配音录音(🎙️/Web Audio API/每页10秒/同步播放)+localStorage持久化+导出HTML工程；V38 23910行→V39 ~24453行

---

### P-20260504-063: creative-drawing-board V40 — GIF 导出

- `Proposal ID`: `P-20260504-063`
- `Title`: creative-drawing-board V40 — GIF 导出
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-063-prd.md
- `Stage`: V40 Iteration
- `Current Status`: delivered
- `Dev Commit`: 16e50d1
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: GIF导出功能(gif.js CDN)+导出按钮+每帧1000ms延迟+自动下载animation_book_时间戳.gif；V39 ~24453行→V40 ~24552行

---

### P-20260504-064: creative-drawing-board V41 — 故事板时间轴

- `Proposal ID`: `P-20260504-064`
- `Title`: creative-drawing-board V41 — 故事板时间轴
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-064-prd.md
- `Stage`: V41 Iteration
- `Current Status`: delivered
- `Dev Commit`: 7ef65ce
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 故事板时间轴+页面缩略图预览+点击切换页面+时长显示+自动滚动到当前页；V40 ~24552行→V41 ~24717行

---

### P-20260504-065: creative-drawing-board V42 — 预设动画模板

- `Proposal ID`: `P-20260504-065`
- `Title`: creative-drawing-board V42 — 预设动画模板
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-065-prd.md
- `Stage`: V42 Iteration
- `Current Status`: delivered
- `Dev Commit`: 57085b1
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 8种预设模板(四格故事/成长日记/旅行日记/友谊故事/彩虹梦/四季变化/毛毛虫历险记/海底世界)+模板面板+应用模板到动画书；V41 ~24717行→V42 ~24924行

---

### P-20260504-066: creative-drawing-board V43 — 动物动画模板

- `Proposal ID`: `P-20260504-066`
- `Title`: creative-drawing-board V43 — 动物动画模板
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-066-prd.md
- `Stage`: V43 Iteration
- `Current Status`: delivered
- `Dev Commit`: 3956915
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 8种动物动画模板(小鱼游/小鸟飞/蝴蝶飞/小猫跑/小狗跑/青蛙跳/兔子跳/小鸡啄米)+背景标记(water/sky/grass/flower/pond/carrot/coop)；V42 ~24924行→V43 ~25154行；共16种模板可选

---

### P-20260504-067: creative-drawing-board V44 — 配音变声特效

- `Proposal ID`: `P-20260504-067`
- `Title`: creative-drawing-board V44 — 配音变声特效
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-067-prd.md
- `Stage`: V44 Iteration
- `Current Status`: delivered
- `Dev Commit`: 5d19dcc
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 8种变声特效(原声/机器人/外星人/高低音/回声/花栗鼠/耳语)+Web Audio API实时处理+下拉选择器+预览切换；V43 ~25154行→V44 ~25402行

---

### P-20260504-068: creative-drawing-board V45 — 模板分类浏览

- `Proposal ID`: `P-20260504-068`
- `Title`: creative-drawing-board V45 — 模板分类浏览
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-068-prd.md
- `Stage`: V45 Iteration
- `Current Status`: delivered
- `Dev Commit`: 6bf6385
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 模板分类Tab(全部(16)/故事(4)/创意(3)/动物(9))+数量显示+点击切换+flex-wrap布局；V44 ~25402行→V45 ~25457行

---

### P-20260504-069: creative-drawing-board V46 — 背景音乐叠加

- `Proposal ID`: `P-20260504-069`
- `Title`: creative-drawing-board V46 — 背景音乐叠加
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-069-prd.md
- `Stage`: V46 Iteration
- `Current Status`: delivered
- `Dev Commit`: 0846c88
- `Acceptance`: 小墨于2026-05-04自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 自动播放功能(▶按钮)+页面录音同步播放+BGM切换(playful)+播放控制+停止清理计时器；V45 ~25457行→V46 ~25610行

---

### P-20260506-084: creative-drawing-board V61 — 模板搜索/排序功能

- `Proposal ID`: `P-20260506-084`
- `Title`: creative-drawing-board V61 — 模板搜索/排序功能
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260506-084-prd.md
- `Stage`: V61 Iteration
- `Current Status`: delivered
- `Dev Commit`: 65b305f
- `Acceptance`: 小墨于2026-05-06自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-06
- `Notes`: 模板搜索面板(搜索框/排序下拉)，4种排序(默认/名称A-Z/名称Z-A/最新)，2列网格布局，缩略图预览

---

### P-20260506-083: creative-drawing-board V60 — 撤销/重做增强（历史记录面板）

- `Proposal ID`: `P-20260506-083`
- `Title`: creative-drawing-board V60 — 撤销/重做增强（历史记录面板）
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260506-083-prd.md
- `Stage`: V60 Iteration
- `Current Status`: delivered
- `Dev Commit`: 8d64f84
- `Acceptance`: 小墨于2026-05-06自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-06
- `Notes`: 历史记录面板(缩略图/时间戳)，Ctrl+Z撤销/Ctrl+Y重做/Ctrl+H打开面板，50条历史上限，点击可恢复到任意历史状态

---

### P-20260506-082: creative-drawing-board V59 — 更多导出格式（PDF/SVG）

- `Proposal ID`: `P-20260506-082`
- `Title`: creative-drawing-board V59 — 更多导出格式（PDF/SVG）
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260506-082-prd.md
- `Stage`: V59 Iteration
- `Current Status`: delivered
- `Dev Commit`: 0cdde07
- `Acceptance`: 小墨于2026-05-06自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-06
- `Notes`: 导出面板新增PDF文档(A4)/PDF带背景/SVG矢量图选项，jsPDF按需加载CDN

---

### P-20260506-081: creative-drawing-board V58 — 橡皮擦增强（局部擦除/撤销）

- `Proposal ID`: `P-20260506-081`
- `Title`: creative-drawing-board V58 — 橡皮擦增强（局部擦除/撤销）
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260506-081-prd.md
- `Stage`: V58 Iteration
- `Current Status`: delivered
- `Dev Commit`: 4fb7a62
- `Acceptance`: 小墨于2026-05-06自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-06
- `Notes`: 橡皮擦设置面板：大小滑块(5-100px)/预设按钮/透明度滑块/预览光标/destination-out擦除模式

---

### P-20260506-080: creative-drawing-board V57 — 作品标签/分类系统

- `Proposal ID`: `P-20260506-080`
- `Title`: creative-drawing-board V57 — 作品标签/分类系统
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260506-080-prd.md
- `Stage`: V57 Iteration
- `Current Status`: delivered
- `Dev Commit`: c5013ba
- `Acceptance`: 小墨于2026-05-06自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-06
- `Notes`: 12个预设标签(卡通/自然/动物/人物/建筑/美食/交通/花卉/风景/抽象/节日/动漫)，标签选择面板，localStorage持久化，工具栏🏷️按钮

---

### P-20260506-079: creative-drawing-board V56 — 更多背景纹理/图案

- `Proposal ID`: `P-20260506-079`
- `Title`: creative-drawing-board V56 — 更多背景纹理/图案
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260506-079-prd.md
- `Stage`: V56 Iteration
- `Current Status`: delivered
- `Dev Commit`: 0292b43
- `Acceptance`: 小墨于2026-05-06自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-06
- `Notes`: 35种背景(纯色10/格子5/条纹4/圆点4/渐变6/纹理6)，分类标签面板，工具栏🎨按钮

---

### P-20260505-078: creative-drawing-board V55 — 图层管理优化

- `Proposal ID`: `P-20260505-078`
- `Title`: creative-drawing-board V55 — 图层管理优化
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-078-prd.md
- `Stage`: V55 Iteration
- `Current Status`: delivered
- `Dev Commit`: 2742fdc
- `Acceptance`: 小墨于2026-05-05自行验收通过
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-05
- `Notes`: 图层面板增强：可见性/透明度滑块/重命名/锁定/复制/上下移动/删除/合并可见图层，限制20层上限

---

### P-20260505-077: creative-drawing-board V54 — 社交分享

---

### P-20260504-070: creative-drawing-board V47 — 模板预览动画

---

### P-20260504-060: creative-drawing-board V37 — 主题商店

- `Proposal ID`: `P-20260504-060`
- `Title`: creative-drawing-board V37 — 主题商店
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-060-prd.md
- `Stage`: V37 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 8种主题+9种画笔皮肤+10种背景+金币购买+主题应用+我的资产+SVG背景生成；V36 23232行→V37 23567行
- `Dev Commit`: 3b8de6d

---

### P-20260504-059: creative-drawing-board V36 — 成就系统

- `Proposal ID`: `P-20260504-059`
- `Title`: creative-drawing-board V36 — 成就系统
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-059-prd.md
- `Stage`: V36 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 20个成就徽章+4个每日任务+奖励系统+进度追踪+解锁通知+localStorage持久化；V35 22929行→V36 23232行
- `Dev Commit`: 65cf074

---

### P-20260504-058: creative-drawing-board V35 — 好友系统

- `Proposal ID`: `P-20260504-058`
- `Title`: creative-drawing-board V35 — 好友系统
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-058-prd.md
- `Stage`: V35 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 邀请码加好友+好友列表+好友画廊参观+虚拟礼物赠送+金币系统+localStorage持久化；V34 22603行→V35 22929行
- `Dev Commit`: 9c74d4d

---

### P-20260504-057: creative-drawing-board V34 — 手势识别

- `Proposal ID`: `P-20260504-057`
- `Title`: creative-drawing-board V34 — 手势识别
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-057-prd.md
- `Stage`: V34 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 颜色追踪手势检测+摄像头实时预览+张开=画笔/握拳=橡皮+4色切换+状态显示+光照适应；V33 22333行→V34 22603行
- `Dev Commit`: 9c2a368

---

### P-20260504-056: creative-drawing-board V33 — 智能建议

- `Proposal ID`: `P-20260504-056`
- `Title`: creative-drawing-board V33 — 智能建议
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-056-prd.md
- `Stage`: V33 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 规则引擎智能建议+配色方案(互补色/类似色)+笔触技巧+布局构图建议+标签切换+点击应用配色；V32 22083行→V33 22333行
- `Dev Commit`: a731cba

---

### P-20260504-055: creative-drawing-board V32 — 增强现实贴纸

- `Proposal ID`: `P-20260504-055`
- `Title`: creative-drawing-board V32 — 增强现实贴纸
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-055-prd.md
- `Stage`: V32 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: AR摄像头背景+24个emoji贴纸(表情/道具/动物)+拖拽位置+分类筛选+AR拍照保存；V31 21766行→V32 22083行
- `Dev Commit`: f255a7d

---

### P-20260504-054: creative-drawing-board V31 — 音频可视化

- `Proposal ID`: `P-20260504-054`
- `Title`: creative-drawing-board V31 — 音频可视化
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-054-prd.md
- `Stage`: V31 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: Web Audio API音频可视化+实时波形+FFT频谱柱状图+4色主题+叠加画布+独立窗口+麦克风权限处理；V30 21466行→V31 21766行
- `Dev Commit`: 2efb294

---

### P-20260504-053: creative-drawing-board V30 — 粒子特效

- `Proposal ID`: `P-20260504-053`
- `Title`: creative-drawing-board V30 — 粒子特效
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-053-prd.md
- `Stage`: V30 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 粒子系统+烟花(点击发射爆炸)+雪花(飘落)+星光(闪烁)+颜色选择+暂停/继续/清除；V29 21070行→V30 21466行
- `Dev Commit`: 036f83d

---

### P-20260504-052: creative-drawing-board V29 — 3D 绘画

- `Proposal ID`: `P-20260504-052`
- `Title`: creative-drawing-board V29 — 3D 绘画
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-052-prd.md
- `Stage`: V29 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: Canvas2D伪3D(零依赖)+立方体6面旋转+球体椭圆模拟+圆柱体+拖拽旋转+滚轮缩放+2D/3D切换；V28 20723行→V29 21070行
- `Dev Commit`: eea39cf

---

### P-20260504-051: creative-drawing-board V28 — 声音录制

- `Proposal ID`: `P-20260504-051`
- `Title`: creative-drawing-board V28 — 声音录制
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-051-prd.md
- `Stage`: V28 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 录音(MediaRecorder)+配音/画外音(边画边录)+录音列表管理(本地20条)+回放/导出WAV+混音合成(V27视频+音频)；V27 20454行→V28 20723行
- `Dev Commit`: 56607da

---

### P-20260504-050: creative-drawing-board V27 — 视频录制

- `Proposal ID`: `P-20260504-050`
- `Title`: creative-drawing-board V27 — 视频录制
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-050-prd.md
- `Stage`: V27 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 绘画录制(操作记录)+回放(播放/暂停/进度条/0.5x-2x速度)+导出WebM(MediaRecorder)+录像管理(本地20条)+录制状态栏(时长/暂停/停止)；V26 19833行→V27 20454行
- `Dev Commit`: 8b1dedf

---

### P-20260504-049: creative-drawing-board V26 — AR 绘画

- `Proposal ID`: `P-20260504-049`
- `Title`: creative-drawing-board V26 — AR 绘画
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-049-prd.md
- `Stage`: V26 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-04
- `Notes`: 摄像头背景(getUserMedia)+8种AR物体(点击放置/拖拽移动/双击删除)+AR动画(漂浮/旋转/摇摆/弹跳)+拍照保存到画廊；V25 19537行→V26 19833行
- `Dev Commit`: 394c333

---

### P-20260503-048: creative-drawing-board V25 — 音效/MIDI 制作

- `Proposal ID`: `P-20260503-048`
- `Title`: creative-drawing-board V25 — 音效/MIDI 制作
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-048-prd.md
- `Stage`: V25 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 钢琴键盘(2八度点击发声)+下落音符(节拍游戏)+节奏编辑器(4轨16步鼓机)+音效合成器(ADSR/振荡器/效果器)+虚拟键盘+音乐中心入口；V24 18962行→V25 19537行
- `Dev Commit`: cacf650

---

### P-20260503-047: creative-drawing-board V24 — 动画制作

- `Proposal ID`: `P-20260503-047`
- `Title`: creative-drawing-board V24 — 动画制作
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-047-prd.md
- `Stage`: V24 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 逐帧动画(新建/复制/删除/重排)+时间轴(帧缩略图列表)+播放控制(8种帧率)+洋葱皮(前/后/前后叠加)+GIF导出(CDN gif.js)+保存加载；V23 18460行→V24 18962行
- `Dev Commit`: 029b440

---

### P-20260503-046: creative-drawing-board V23 — 更多绘画工具

- `Proposal ID`: `P-20260503-046`
- `Title`: creative-drawing-board V23 — 更多绘画工具
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-046-prd.md
- `Stage`: V23 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 线性/径向渐变填充(角度可选+多色标)+文字输入(字体/大小/颜色/对齐)+形状库(6类基础形状)+图层系统(新建/删除/上移下移/显示隐藏/锁定)+工具栏按钮；V22 17707行→V23 18460行
- `Dev Commit`: 34551c1

---

### P-20260503-045: creative-drawing-board V22 — 更多游戏模式

- `Proposal ID`: `P-20260503-045`
- `Title`: creative-drawing-board V22 — 更多游戏模式
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-045-prd.md
- `Stage`: V22 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 2048(4x4网格+滑动合并+分数)+俄罗斯方块(7种方块+旋转+消除+等级+下一个预览)+五子棋(15x15+落子+五连判定+悔棋)+统一游戏容器+触摸控制；V21 16691行→V22 17707行
- `Dev Commit`: 7b8e6d2

---

### P-20260503-044: creative-drawing-board V21 — 画廊 + 社区分享

- `Proposal ID`: `P-20260503-044`
- `Title`: creative-drawing-board V21 — 画廊 + 社区分享
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-044-prd.md
- `Stage`: V21 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 画廊面板(我的作品/精选/热门/导入)+作品存储(缩略图+localStorage)+点赞系统(防刷+设备ID)+评分系统(1-5星)+每周精选(周一自动更新)+导入导出JSON+分享功能(剪贴板/DataURL)；V20 15995行→V21 16691行
- `Dev Commit`: 07315c7

---

### P-20260503-043: creative-drawing-board V20 — 打印功能增强

- `Proposal ID`: `P-20260503-043`
- `Title`: creative-drawing-board V20 — 打印功能增强
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-043-prd.md
- `Stage`: V20 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 海报打印(A3/A2/A1分割+拼接线+页码)+涂色卡打印(纯净黑白线稿+分类+难度标签)+描红卡打印(虚线/实线/点线引导)+每日练习纸(一周7天+涂色+描红+绘画区)+打印菜单+打印预览；V19 15143行→V20 15995行
- `Dev Commit`: b8776d9

---

### P-20260503-042: creative-drawing-board V19 — 农历/节日主题包

- `Proposal ID`: `P-20260503-042`
- `Title`: creative-drawing-board V19 — 农历/节日主题包
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-042-prd.md
- `Stage`: V19 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 5个节日主题(端午8贴纸3背景/中秋8贴纸3背景/重阳6贴纸2背景/元宵6贴纸2背景/春节10贴纸4背景)+节日自动检测+节日选择面板+主题激活+节日特效(纸屑/灯笼/月光/涟漪/落叶)；V18 14365行→V19 15143行
- `Dev Commit`: 2ef51e8

---

### P-20260503-041: creative-drawing-board V18 — 气泡游戏改版

- `Proposal ID`: `P-20260503-041`
- `Title`: creative-drawing-board V18 — 气泡游戏改版
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-041-prd.md
- `Stage`: V18 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 7种气泡(普通/爆炸/连锁/彩虹/定时/冰冻/缩小)+5种道具(炸弹💣/保护罩🛡️/加速器⚡/双倍分✨/魔法棒🪄)+关卡模式(6+关递增难度)+排行榜(Top10)+保护罩3条命+特殊泡概率生成；V17 13379行→V18 14365行
- `Dev Commit`: c90e61f

---

### P-20260503-040: creative-drawing-board V17 — 多语言支持

- `Proposal ID`: `P-20260503-040`
- `Title`: creative-drawing-board V17 — 多语言支持
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-040-prd.md
- `Stage`: V17 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 中英文双语界面(工具栏/功能面板/游戏/成就/模板分类/家长面板全双语)+语言切换按钮+t(key)翻译函数+data-i18n属性+localStorage记忆偏好；V16 13114行→V17 13379行
- `Dev Commit`: e91dc4d

---

### P-20260503-039: creative-drawing-board V16 — 绘画工具增强

- `Proposal ID`: `P-20260503-039`
- `Title`: creative-drawing-board V16 — 绘画工具增强
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-039-prd.md
- `Stage`: V16 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 对称绘画(左右/上下/四角+中心参考线)+智能形状(直线/圆/矩形/三角+预览+自动修正)+多步撤销(Ctrl+Z/Ctrl+Y+20步历史)+画布缩放(双指+按钮+50%-300%)+橡皮擦增强(大小滑块+只擦自己笔迹)；V15 12688行→V16 13114行
- `Dev Commit`: 1ce7282

---

### P-20260503-038: creative-drawing-board V15 — 描红/模板内容大扩充

- `Proposal ID`: `P-20260503-038`
- `Title`: creative-drawing-board V15 — 描红/模板内容大扩充
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-038-prd.md
- `Stage`: V15 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 描红模板从20增至50(数字0-9+字母A-Z+汉字5个+物品5个+交通2个)+连线从6增至15(水果3+动物3+交通2+自然1)+分类筛选+年龄标记+学习路径+描红进度追踪；V14 12412行→V15 12688行
- `Dev Commit`: 4b5e1db

---

### P-20260503-037: creative-drawing-board V14 — 家长控制面板

- `Proposal ID`: `P-20260503-037`
- `Title`: creative-drawing-board V14 — 家长控制面板
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-037-prd.md
- `Stage`: V14 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: ⏰时长限制(15-120分钟/超时锁定绘画)+使用时间追踪+周报柱状图(CSS)+数据导出(CSV/JSON)+内容解锁(5规则+锁定遮罩+解锁动画)+家长入口(数学题验证)；V13 11548行→V14 12412行
- `Dev Commit`: 4e7247c

---

### P-20260503-036: creative-drawing-board V13 — 背景音乐增强

- `Proposal ID`: `P-20260503-036`
- `Title`: creative-drawing-board V13 — 背景音乐增强
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-036-prd.md
- `Stage`: V13 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 🎵背景音乐(Web Audio API合成5首:happy/peaciful/playful/dreamy/festive)+场景自动切换(绘画→happy/涂色→peaceful/游戏→playful/画廊→dreamy)+独立音量滑块+记忆偏好+500ms渐变切换+页面隐藏降速；V12 11091行→V13 11548行
- `Dev Commit`: c14a813

---

### P-20260503-035: creative-drawing-board V12 — 涂色游戏增强

- `Proposal ID`: `P-20260503-035`
- `Title`: creative-drawing-board V12 — 涂色游戏增强
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-035-prd.md
- `Stage`: V12 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 涂色模板从10增至30(蝴蝶/火箭/恐龙/独角兽等)+分类浏览(动物/食物/人物/风景/交通)+难度标记(🐣🐥🔥)+年龄推荐+混色效果+荧光笔刷(5色+彩虹)+粒子爆发动画(30色粒子)+星星飘落+C-E-G-C合成旋律；V11 10418行→V12 11091行
- `Dev Commit`: e13e957

---

### P-20260503-034: creative-drawing-board V11 — 画作分享 + 导出增强

- `Proposal ID`: `P-20260503-034`
- `Title`: creative-drawing-board V11 — 画作分享 + 导出增强
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-034-prd.md
- `Stage`: V11 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 📥PNG导出(文件名日期时间+2x分辨率)+日期水印+作品名称水印+画廊管理(查看/下载/重命名/删除/批量)+🔗分享面板(Web Share API+原生分享)+设为拼图素材；V10 9444行→V11 10418行
- `Dev Commit`: 5865661

---

### P-20260503-033: creative-drawing-board V10 — 更多游戏模式

- `Proposal ID`: `P-20260503-033`
- `Title`: creative-drawing-board V10 — 更多游戏模式
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-033-prd.md
- `Stage`: V10 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 🧩拼图(3×3/4×3/4×4+画廊图片+完成动画)+🔗连线游戏(6模板+数字顺序连线+成图显示)+🧭迷宫(递归回溯算法+7×7/11×11/15×11+碰墙检测+终点庆祝)；V9 7896行→V10 9444行
- `Dev Commit`: 2d4280a

---

### P-20260503-032: creative-drawing-board V9 — 每日挑战 + 成就进化

- `Proposal ID`: `P-20260503-032`
- `Title`: creative-drawing-board V9 — 每日挑战 + 成就进化
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-032-prd.md
- `Stage`: V9 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 每日挑战系统(🔔任务+7种类型+进度追踪+奖励领取)+连续打卡(7/14/30天)+打卡日历+成就进化(⭐/⭐⭐/⭐⭐⭐三级)+限定成就(challenge/early_bird/night_owl/streak)+奖励(积分+限定贴纸)；V8 6878行→V9 7896行
- `Dev Commit`: 3bf2bb2

---

### P-20260503-031: creative-drawing-board V8 — 节日/季节主题包

- `Proposal ID`: `P-20260503-031`
- `Title`: creative-drawing-board V8 — 节日/季节主题包
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-031-prd.md
- `Stage`: V8 Iteration
- `Current Status`: approved_for_dev
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 4套节日主题包(万圣节10月/圣诞节12月/春节1-2月/复活节4月)+每套8贴纸+2背景+专属tab+自动检测+手动切换+飘落动画(CSS keyframes)；V7 6324行→V8 6878行
- `Dev Commit`: 30fd823

---

### P-20260503-030: creative-drawing-board V7 — 自定义贴纸创作

- `Proposal ID`: `P-20260503-030`
- `Title`: creative-drawing-board V7 — 自定义贴纸创作
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-030-prd.md
- `Stage`: V7 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: pending
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 自定义贴纸创作(200x200绘制面板+画笔/橡皮/颜色+保存到我的贴纸)+颜色替换(选中贴纸🎨换主色)+翻转镜像(↔↕)+重绘编辑(✏️)+最多20个+localStorage持久化；V6 5305行→V7 6324行
- `Dev Commit`: 8c065c6

---

### P-20260503-029: creative-drawing-board V6 — 引导教学 + PWA离线支持

- `Proposal ID`: `P-20260503-029`
- `Title`: creative-drawing-board V6 — 引导教学 + PWA离线支持
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-029-prd.md
- `Stage`: V6 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: pending
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: P0引导教学模式(8跟画模板/逐笔画演示/年龄分级3-4-5岁/步骤完成检测/跳过退出)+P1 PWA离线支持(manifest.json+ServiceWorker)+打印功能(白底高清A4)；V5 3966行→V6 5305行
- `Dev Commit`: fd15438

---

### P-20260503-028: creative-drawing-board V5 — 气泡游戏强化

- `Proposal ID`: `P-20260503-028`
- `Title`: creative-drawing-board V5 — 气泡游戏强化
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-028-prd.md
- `Stage`: V5 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: pending
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: 气泡积分系统(普通1分/金色5分/彩虹5分/星星触发奖励)+连击加成+每50分奖励随机贴纸+每200分奖励稀有贴纸+本地排行榜(历史最高+最近10场)+新纪录庆祝动画；V4 3547行→V5 3966行
- `Dev Commit`: 9eb9717

---

### P-20260503-027: creative-drawing-board V4 — 学习记录 + 贴纸编辑

- `Proposal ID`: `P-20260503-027`
- `Title`: creative-drawing-board V4 — 学习记录 + 贴纸编辑
- `Owner`: 小墨
- `Project`: PRJ-20260418-002（creative-drawing-board）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-027-prd.md
- `Stage`: V4 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: pending
- `Feature Branch`: `master`
- `Deployed`: https://yeluo45.github.io/creative-drawing-board/
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Last Update`: 2026-05-03
- `Notes`: P0学习记录系统(localStorage统计+12成就徽章+画廊)+P1贴纸编辑(选中/拖拽/缩放/旋转/层级)；V3 2401行→V4 3547行
- `Dev Commit`: 0a138c7

---

### P-20260508-001: DBG卡牌游戏 V28 — 终局内容 + 周目系统

- `Proposal ID`: `P-20260508-001`
- `Title`: DBG卡牌游戏 V28 — 终局内容 + 周目系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260508-001-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/card-game-prototype/P-20260508-001-tech-solution.md
- `Stage`: V28 Iteration
- `Current Status`: delivered
- `Dev Commit`: c549f7b
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-03
- `Notes`: 终局结算(统计/卡组评价/隐藏结局徽章)+新游戏+(继承宠物/遗物)+4难度(hard/hell/extreme)+6隐藏结局+统计面板+图鉴；文件8654行
- `Acceptance`: delivered

---

### P-20260503-019: DBG卡牌游戏 V27 — 更多章节与Boss扩展

- `Proposal ID`: `P-20260503-019`
- `Title`: DBG卡牌游戏 V27 — 更多章节与Boss扩展
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-019-prd.md
- `Stage`: V27 Iteration
- `Current Status`: delivered
- `Dev Commit`: f6c3b33
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: 第5-7章（天空/遗迹/混沌）；3新Boss（archangel/azmodan/chaosGod）；多阶段机制；章节奖励；文件8136行

---

### P-20260503-018: DBG卡牌游戏 V26 — 更多卡牌设计

- `Proposal ID`: `P-20260503-018`
- `Title`: DBG卡牌游戏 V26 — 更多卡牌设计
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-018-prd.md
- `Stage`: V26 Iteration
- `Current Status`: delivered
- `Dev Commit`: 6feee74
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: 15张新卡牌；斩杀/狂暴/连锁等攻击牌；强化防御/闪避等技能牌；激怒/荆棘等光环；文件7950行

---

### P-20260503-014: DBG卡牌游戏 V22 — 音效与音乐扩展

- `Proposal ID`: `P-20260503-014`
- `Title`: DBG卡牌游戏 V22 — 音效与音乐扩展
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-014-prd.md
- `Stage`: V22 Iteration
- `Current Status`: delivered
- `Dev Commit`: 4822ff0
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: AudioManager新增音效；触发点绑定；静音开关；Web Audio API；文件7165行

---

### P-20260503-013: DBG卡牌游戏 V21 — 移动端适配 + 触屏支持

- `Proposal ID`: `P-20260503-013`
- `Title`: DBG卡牌游戏 V21 — 移动端适配 + 触屏支持
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-013-prd.md
- `Stage`: V21 Iteration
- `Current Status`: delivered
- `Dev Commit`: 1726d49
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: viewport配置；Canvas响应式缩放；触屏事件；横屏提示；移动端媒体查询；文件7055行

---

### P-20260503-012: DBG卡牌游戏 V20 — 章节扩展 + Boss战设计

- `Proposal ID`: `P-20260503-012`
- `Title`: DBG卡牌游戏 V20 — 章节扩展 + Boss战设计
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-012-prd.md
- `Stage`: V20 Iteration
- `Current Status`: delivered
- `Dev Commit`: 43eb3b8
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: 第3/4章敌人+深渊领主/虚无之主Boss战；3阶段Boss机制；章节奖励系统；7层地图；文件6882行

---

### P-20260503-011: DBG卡牌游戏 V19 — 多槽位存档系统

- `Proposal ID`: `P-20260503-011`
- `Title`: DBG卡牌游戏 V19 — 多槽位存档系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-011-prd.md
- `Stage`: V19 Iteration
- `Current Status`: delivered
- `Dev Commit`: 5c5eed9
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: 3槽位存档系统；存档/加载/删除；自动存档；主菜单存档入口；文件6299行

---

### P-20260503-010: DBG卡牌游戏 V18 — 随机事件系统

- `Proposal ID`: `P-20260503-010`
- `Title`: DBG卡牌游戏 V18 — 随机事件系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-010-prd.md
- `Stage`: V18 Iteration
- `Current Status`: delivered
- `Dev Commit`: f5afaa9
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Notes`: 6种事件类型：休息/商店/宝箱/精英/随机/篝火；EVENTS数据 + showEvent + 事件遮罩；地图节点扩展；文件5858行

---

### P-20260503-007: DBG卡牌游戏 V15 — 更多卡牌

- `Proposal ID`: `P-20260503-007`
- `Title`: DBG卡牌游戏 V15 — 更多卡牌
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-007-prd.md
- `Stage`: V15 Iteration
- `Current Status`: accepted
- `Dev Commit`: 80b254f
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03

---

### P-20260503-006: DBG卡牌游戏 V14 — 卡牌商店重做

- `Proposal ID`: `P-20260503-006`
- `Title`: DBG卡牌游戏 V14 — 卡牌商店重做
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-006-prd.md
- `Stage`: V14 Iteration
- `Current Status`: accepted
- `Dev Commit`: 4ab1879
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03

---

### P-20260503-005: DBG卡牌游戏 V13 — 牌组构建核心（Critical Bugfix）

- `Proposal ID`: `P-20260503-005`
- `Title`: DBG卡牌游戏 V13 — 牌组构建核心（Critical Bugfix）
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-005-prd.md
- `Stage`: V13 Iteration
- `Current Status`: accepted
- `Dev Commit`: 3e6bacf
- `Acceptance`: 小墨于2026-05-03自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Note`: V5 needs_revision已重新实现，18张奖励卡牌，showCardReward正确集成到endCombat流程

---

### P-20260503-004: DBG卡牌游戏 V12 — 音效与特效

- `Proposal ID`: `P-20260503-004`
- `Title`: DBG卡牌游戏 V12 — 音效与特效
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-004-prd.md
- `Stage`: V12 Iteration
- `Current Status`: accepted
- `Dev Commit`: f663b83
- `Acceptance`: boss于2026-05-03验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03

---

### P-20260503-003: DBG卡牌游戏 V11 — 更多遗物效果

- `Proposal ID`: `P-20260503-003`
- `Title`: DBG卡牌游戏 V11 — 更多遗物效果
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-003-prd.md
- `Stage`: V11 Iteration
- `Current Status`: accepted
- `Dev Commit`: 6b02450
- `Acceptance`: boss于2026-05-03验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03

---

### P-20260503-002: DBG卡牌游戏 V10 — 章节扩展

- `Proposal ID`: `P-20260503-002`
- `Title`: DBG卡牌游戏 V10 — 章节扩展
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-002-prd.md
- `Stage`: V10 Iteration
- `Current Status`: accepted
- `Dev Commit`: c46c915
- `Acceptance`: boss于2026-05-03验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03

---

### P-20260503-001: DBG卡牌游戏 V9 — 成就系统

- `Proposal ID`: `P-20260503-001`
- `Title`: DBG卡牌游戏 V9 — 成就系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-001-prd.md
- `Stage`: V9 Iteration
- `Current Status`: accepted
- `Dev Commit`: b2d094b
- `Acceptance`: boss于2026-05-02验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-02

---

### P-20260502-016: DBG卡牌游戏 V8 — 卡牌升级系统

- `Proposal ID`: `P-20260502-016`
- `Title`: DBG卡牌游戏 V8 — 卡牌升级系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-016-prd.md
- `Stage`: V8 Iteration
- `Current Status`: accepted
- `Dev Commit`: 720a672
- `Acceptance`: boss于2026-05-02验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-02

---

### P-20260502-013: DBG卡牌游戏 V6 — 遗物/神器系统

- `Proposal ID`: `P-20260502-013`
- `Title`: DBG卡牌游戏 V6 — 遗物/神器系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-013-prd.md
- `Stage`: V6 Iteration
- `Current Status`: accepted
- `Dev Commit`: 385de1d
- `Acceptance`: boss于2026-05-02验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-02

---

### P-20260502-012: DBG卡牌游戏 V5 — 战斗奖励卡牌选择系统

- `Proposal ID`: `P-20260502-012`
- `Title`: DBG卡牌游戏 V5 — 战斗奖励卡牌选择系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-012-prd.md
- `Stage`: V5 Iteration
- `Current Status`: needs_revision
- `Dev Commit`: 4c5cc0e
- `Acceptance`: **NOT ACCEPTED** - 功能未集成到游戏流程，showRewardScreen/selectReward缺失
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `Last Update`: 2026-05-03
- `Note`: V13将重新实现此功能

---

### P-20260502-004: 3D飞行棋 — AI对手模式

- `Proposal ID`: `P-20260502-004`
- `Title`: 3D飞行棋 — AI对手模式
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent Proposal`: P-20260427-001
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-004-prd.md
- `Project Path`: proposals/workspace-dev/proposals/flight-chess-3d/
- `GitHub Repo`: https://github.com/YeLuo45/flight-chess-3d
- `Deployment URL`: https://yeluo45.github.io/flight-chess-3d/
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Acceptance`: accepted
- `Last Update`: 2026-05-02
- `Notes`: AI三种难度（Easy随机/Medium策略/Hard最优）；自动投骰+选子；可选纯AI对战或混合模式；原人类模式不受影响；已实现难度选择UI和AI Thinking动画

---

### P-20260502-005: 3D飞行棋 — 玩家颜色选择+战绩统计

- `Proposal ID`: `P-20260502-005`
- `Title`: 3D飞行棋 — 玩家颜色选择+战绩统计
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent Proposal`: P-20260502-004
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-005-prd.md
- `Acceptance`: accepted
- `Last Update`: 2026-05-02
- `Notes`: 玩家可选颜色；战绩统计（胜率/连胜）；localStorage持久化

---

### P-20250418-001: monopoly3d

- `Proposal ID`: `P-20250418-001`
- `Title`: monopoly3d
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/monopoly3d/`
- `Acceptance`: accepted
- `Deployment URL`: https://YeLuo45.github.io/monopoly3d/
- `GitHub Repo`: https://github.com/YeLuo45/monopoly3d
- `Last Update`: 2026-04-18
- `Notes`: Vite + React + Three.js + @react-three/fiber + Tailwind CSS 3；3D 大富翁桌游；Node 18 兼容性问题修复（Tailwind v4→v3，Vite v8→v5）；已部署 GitHub Pages；项目文件（含构建产物）推送至 gh-pages 分支

---

### P-20260412-007: ai-creator-h5 (H5)

- `Proposal ID`: `P-20260412-007`
- `Title`: ai-creator-h5 (H5)
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/ai-creator-h5/`
- `Acceptance`: accepted
- `Deployment URL`: https://yeluo45.github.io/ai-creator-h5/
- `GitHub Repo`: https://github.com/YeLuo45/ai-creator-miniprogram (小程序) / https://github.com/YeLuo45/ai-creator-h5 (H5)
- `Last Update`: 2026-04-19
- `Notes`: 微信小程序 Phase 1 MVP 骨架 + H5 版本已完成并部署；H5 采用 Vite + Hash SPA 架构；4页面：首页/生成/历史/我的；支持图片生成、音乐生成、TTS 语音合成；修复仓库描述乱码（GitHub API TLS超时导致）

---

### P-20260412-008: ai-subscription

- `Proposal ID`: `P-20260412-008`
- `Title`: ai-subscription
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/ai-subscription/`
- `Acceptance`: accepted
- `Deployment URL`: https://yeluo45.github.io/ai-subscription/
- `GitHub Repo`: https://github.com/YeLuo45/ai-subscription
- `Last Update`: 2026-04-12
- `Notes`: 多端独立应用（Web + 小程序 + PC + Android）；Web 已部署 GitHub Pages；AI 摘要、RSS订阅、GitHub Trending 爬取

---

### P-20250417-001: proposals-manager → prj-proposals-manager

- `Proposal ID`: `P-20250417-001`
- `Title`: proposals-manager → prj-proposals-manager
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20260417-001（prj-proposals-manager）
- `Project Path`: `proposals/workspace-dev/proposals/prj-proposals-manager/`
- `Acceptance`: accepted
- `Deployment URL`: https://yeluo45.github.io/prj-proposals-manager/
- `GitHub Repo`: https://github.com/YeLuo45/prj-proposals-manager
- `Last Update`: 2026-05-03
- `Notes`: 提案管理系统；完整CRUD；GitHub API操作JSON数据；已与提案管理系统单向同步；仓库已于2026-05-03从 proposals-manager 更名为 prj-proposals-manager

---

### P-20250417-002: android-hello

- `Proposal ID`: `P-20250417-002`
- `Title`: android-hello
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/android-hello/`
- `Acceptance`: accepted
- `Deployment URL`: https://github.com/YeLuo45/android-hello/releases/download/v1.0.0/app-debug.apk
- `GitHub Repo`: https://github.com/YeLuo45/android-hello
- `Last Update`: 2026-04-17
- `Notes`: Android Kotlin Hello World；包名 com.hello.android；minSdk 24, targetSdk 36；APK 已上传 GitHub Releases (v1.0.0)

---

### P-20250416-003: calculator-app

- `Proposal ID`: `P-20250416-003`
- `Title`: calculator-app
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/calculator-app/`
- `Acceptance`: accepted (2026-04-26)
- `GitHub Repo`: https://github.com/YeLuo45/calculator-app.git
- `Last Update`: 2026-04-26
- `Notes`: 面向大众市场 APK；功能：科学计算 + 单位转换 + 汇率换算（Web 已交付，APK 因 NDK 损坏阻塞）

---

### P-20250416-001: todo-list

- `Proposal ID`: `P-20250416-001`
- `Title`: todo-list
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/todo-list/`
- `Acceptance`: accepted
- `Deployment URL`: https://yeluo45.github.io/todo-list/
- `GitHub Repo`: https://github.com/YeLuo45/todo-list
- `Last Update`: 2026-04-16
- `Notes`: Web + Windows扩展；Windows客户端（Electron）；本地部署

---

### P-20260502-017: ai-subscription — 大模型调用层升级 (llm-design-dev)

- `Proposal ID`: `P-20260502-017`
- `Title`: ai-subscription — 大模型调用层升级 (llm-design-dev)
- `Owner`: 小墨
- `Current Status`: in_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-017-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/ai-subscription/P-20260502-017-tech-solution.md
- `Test Cases Path`: proposals/workspace-test/proposals/ai-subscription/P-20260502-017-test-cases.md
- `Test Cases Confirmation`: timeout-approved
- `Test Cases Confirmation Timeout Resolution`: 倒计时到期(2026-05-02)，默认通过处理
- `Technical Expectations`: timeout-approved
- `Technical Expectations Timeout Resolution`: 倒计时到期(2026-05-02)，默认通过处理
- `Technical Stack`: ai SDK + @ai-sdk/openai + @ai-sdk/anthropic + @ai-sdk/google + partial-json + jsonrepair
- `Last Update`: 2026-05-05
- `Notes`: Provider架构升级 + AI SDK集成 + 流式摘要 + Thinking配置；技术栈：ai SDK + @ai-sdk/openai + @ai-sdk/anthropic + @ai-sdk/google + partial-json + jsonrepair；技术期望倒计时(2026-05-02)已触发，当前进入 in_dev 阶段；倒计时到期(2026-05-02)，默认通过处理
- `Tech Confirm Cron Job ID`: P-20260502-017-tech-confirm
- `Tech Confirm Cron Job Executed`: 2026-05-05（技术期望超时自动通过，进入 in_dev）
- `Tech Confirm Cron Job P-20260502-017-tech-confirm Executed`: 2026-05-05 09:30（倒计时到期确认执行）

---

### P-20260504-002: ai-subscription — 内容变换输出 (摘要→推文/Newsletter/思维导图)

- `Proposal ID`: `P-20260504-002`
- `Title`: ai-subscription — 内容变换输出 (摘要→推文/Newsletter/思维导图)
- `Owner`: 小墨
- `Current Status`: accepted
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-002-prd.md
- `Last Update`: 2026-05-04
- `Notes`: TransformBar 4格式切换；/api/transform 端点；已git push (6fd61e8)

---

### P-20260504-001: ai-subscription — Tool-use 能力接入 (Agentic AI)

- `Proposal ID`: `P-20260504-001`
- `Title`: ai-subscription — Tool-use 能力接入 (Agentic AI)
- `Owner`: 小墨
- `Current Status`: accepted
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-001-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/ai-subscription/P-20260504-001-tech-solution.md
- `Last Update`: 2026-05-04
- `Notes`: Tool-use能力：web_search/fetch_rss/calculate；与llm-design-dev的Action System衔接；仅Web端；已git push (1f18f68)

---

### P-20260505-013: ai-subscription — 订阅源批量管理

- `Proposal ID`: `P-20260505-013`
- `Title`: ai-subscription — 订阅源批量管理
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20260412-008（ai-subscription）
- `Engine`: React
- `Target`: Web
- `Project Path`: proposals/workspace-dev/proposals/ai-subscription/ai-subscription-web/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-013-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-subscription
- `Dev Commit`: 8d9fc8b
- `Deployed`: https://yeluo45.github.io/ai-subscription/
- `Last Update`: 2026-05-05
- `Notes`: 多选模式+批量启用/禁用/删除/移动分组；web端
- `Acceptance`: accepted

---

### P-20260506-RSS-001: ai-subscription — RSS/Atom 自动发现

- `Proposal ID`: `P-20260506-RSS-001`
- `Title`: ai-subscription — RSS/Atom 自动发现
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20260412-008（ai-subscription）
- `Engine`: React
- `Target`: Web
- `Project Path`: proposals/workspace-dev/proposals/ai-subscription/ai-subscription-web/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260506-RSS-001-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-subscription
- `Dev Commit`: 1e74168
- `Deployed`: https://yeluo45.github.io/ai-subscription/
- `Last Update`: 2026-05-06
- `Notes`: 输入URL自动探测/feed/rss/atom等常见路径；解析HTML<link>标签；显示发现的所有feed供选择性订阅
- `PRD Confirmation`: timeout-approved
- `Acceptance`: accepted

---

### P-20260505-012: ai-subscription — RSS/Atom 智能解析增强

- `Proposal ID`: `P-20260505-012`
- `Title`: ai-subscription — RSS/Atom 智能解析增强
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-012-prd.md
- `Last Update`: 2026-05-05
- `Notes`: Feed类型检测+图标提取+字段映射+更新频率检测；web端

---

### P-20260505-011: ai-subscription — 数据统计面板

- `Proposal ID`: `P-20260505-011`
- `Title`: ai-subscription — 数据统计面板
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-011-prd.md
- `Last Update`: 2026-05-05
- `Notes`: 统计指标+SVG图表+订阅源活跃度+文章趋势；纯SVG无外部依赖；web端

---

### P-20260505-010: ai-subscription — 键盘快捷键

- `Proposal ID`: `P-20260505-010`
- `Title`: ai-subscription — 键盘快捷键
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-010-prd.md
- `Last Update`: 2026-05-05
- `Notes`: Cmd+K搜索/N添加订阅/Shift+T切换主题/Esc关闭弹窗；web端

---

### P-20260505-009: ai-subscription — 国际化（i18n）

- `Proposal ID`: `P-20260505-009`
- `Title`: ai-subscription — 国际化（i18n）
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-009-prd.md
- `Last Update`: 2026-05-05
- `Notes`: 中文/English双语+i18n Context+语言切换；web端

---

### P-20260505-008: ai-subscription — 主题定制（深色模式）

- `Proposal ID`: `P-20260505-008`
- `Title`: ai-subscription — 主题定制（深色模式）
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-008-prd.md
- `Last Update`: 2026-05-05
- `Notes`: Ant Design ConfigProvider+CSS变量+深浅切换；web端

---

### P-20260505-007: ai-subscription — 全文检索增强

- `Proposal ID`: `P-20260505-007`
- `Title`: ai-subscription — 全文检索增强
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-007-prd.md
- `Last Update`: 2026-05-05
- `Notes`: 统一搜索API+搜索结果页+高亮+侧边栏入口；纯前端；web端

---

### P-20260505-006: ai-subscription — 社交分享

- `Proposal ID`: `P-20260505-006`
- `Title`: ai-subscription — 社交分享
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-006-prd.md
- `Last Update`: 2026-05-05
- `Notes`: Web Share API+Twitter/Telegram/微信分享面板；TransformBar集成；web端

---

### P-20260505-005: ai-subscription — 订阅源自定义刷新间隔

- `Proposal ID`: `P-20260505-005`
- `Title`: ai-subscription — 订阅源自定义刷新间隔
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-005-prd.md
- `Last Update`: 2026-05-05
- `Notes`: 全局间隔设置+单源自定义间隔+scheduler读取自定义值；纯前端；web端

---

### P-20260505-004: ai-subscription — 智能摘要推荐

- `Proposal ID`: `P-20260505-004`
- `Title`: ai-subscription — 智能摘要推荐
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-004-prd.md
- `Last Update`: 2026-05-05
- `Notes`: 用户画像+推荐算法+推荐列表页+一键订阅；纯前端；web端

---

### P-20260505-003: ai-subscription — 文章评论/笔记

- `Proposal ID`: `P-20260505-003`
- `Title`: ai-subscription — 文章评论/笔记
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-003-prd.md
- `Last Update`: 2026-05-05
- `Notes': ArticleNote类型+Markdown笔记编辑器+存储API+笔记入口；纯前端；web端

---

### P-20260505-002: ai-subscription — 订阅源分组管理

- `Proposal ID`: `P-20260505-002`
- `Title`: ai-subscription — 订阅源分组管理
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-002-prd.md
- `Last Update`: 2026-05-05
- `Notes`: 分组CRUD+折叠视图+拖拽排序+移动到分组；纯前端；web端

---

### P-20260505-001: ai-subscription — Pub/Sub 实时推送（WebSocket）

- `Proposal ID`: `P-20260505-001`
- `Title`: ai-subscription — Pub/Sub 实时推送（WebSocket）
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-001-prd.md
- `Last Update`: 2026-05-05
- `Notes`: WebSocket客户端+服务端点+自动重连+实时通知UI；dev模式；web端
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Timeout Resolution`: 倒计时到期(2026-05-05)，默认通过处理
- `Technical Expectations`: timeout-approved（技术栈继承V3：React 18 + Vite 5 + TypeScript + WebSocket）

---

### P-20260504-009: ai-subscription — 阅读列表 + 稍后读

- `Proposal ID`: `P-20260504-009`
- `Title`: ai-subscription — 阅读列表 + 稍后读
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-009-prd.md
- `Last Update`: 2026-05-04
- `Notes': Article.isReadLater标记+稍后读页面+菜单Badge；配合PWA离线；web端

---

### P-20260504-008: ai-subscription — 历史摘要管理（搜索+标签+收藏）

- `Proposal ID`: `P-20260504-008`
- `Title`: ai-subscription — 历史摘要管理（搜索+标签+收藏）
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-008-prd.md
- `Last Update`: 2026-05-04
- `Notes`: Summary历史页+全文搜索+标签管理+收藏⭐；纯前端IndexedDB；web端

---

### P-20260504-007: ai-subscription — PWA 离线支持

- `Proposal ID`: `P-20260504-007`
- `Title`: ai-subscription — PWA 离线支持
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-007-prd.md
- `Last Update`: 2026-05-04
- `Notes`: SW缓存策略+IndexedDB离线+Manifest完善+安装提示+离线徽章；web端

---

### P-20260504-006: ai-subscription — 数据导入/导出 (OPML + JSON备份)

- `Proposal ID`: `P-20260504-006`
- `Title`: ai-subscription — 数据导入/导出 (OPML + JSON备份)
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-006-prd.md
- `Last Update`: 2026-05-04
- `Notes`: OPML导入/导出+JSON全量备份/恢复；纯前端；settings面板集成

---

### P-20260504-005: ai-subscription — 高级内容变换（可视化思维导图/PDF/幻灯片）

- `Proposal ID`: `P-20260504-005`
- `Title`: ai-subscription — 高级内容变换（可视化思维导图/PDF/幻灯片）
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-005-prd.md
- `Last Update`: 2026-05-04
- `Notes`: SVG思维导图(可折叠/缩放/导出PNG)+PDF导出(Print)+幻灯片Viewer(键盘翻页/导出PNG)；零新增大型依赖；web端

---

### P-20260504-004: ai-subscription — 实时监控+推送 (Webhook/邮件/Cron)

- `Proposal ID`: `P-20260504-004`
- `Title`: ai-subscription — 实时监控+推送 (Webhook/邮件/Cron)
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-004-prd.md
- `Last Update`: 2026-05-04
- `Notes`: Webhook/邮件/Cron端点；P0=Webhook，P1=邮件，P2=Cron端点；web端实现

---

### P-20260504-003: ai-subscription — 多端 AI 层同步 (PC/小程序)

- `Proposal ID`: `P-20260504-003`
- `Title`: ai-subscription — 多端 AI 层同步 (PC/小程序)
- `Owner`: 小墨
- `Current Status`: accepted
- `Project`: PRJ-20260412-008（ai-subscription）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-003-prd.md
- `Last Update`: 2026-05-04
- `Notes`: PC端复用shared/(callLLM/streamLLM)；uni-app/Taro小程序调用Web API；已git push (aacf1f2)

---

### P-20250416-002: game-1024

- `Proposal ID`: `P-20250416-002`
- `Title`: game-1024
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/game-1024/`
- `Acceptance`: accepted
- `Deployment URL`: https://yeluo45.github.io/game-1024/
- `GitHub Repo`: https://github.com/YeLuo45/game-1024
- `Last Update`: 2026-05-02
- `Notes`: 经典1024玩法（4×4滑动合并，目标1024）+ PWA可安装到安卓主屏幕 + 存档/继续游戏 + 皮肤系统；V2迭代(2048模式/无限模式/每日挑战/成就系统)已交付部署

---

### P-20260502-007: game-1024 V2 — 2048/无限模式切换

- `Proposal ID`: `P-20260502-007`
- `Title`: game-1024 V2 — 2048/无限模式切换
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project`: PRJ-20250416-002（game-1024）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-007-prd.md
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Last Update`: 2026-05-02
- `Notes`: 2048模式+无限模式切换；各自独立存档；无限模式不设目标上限；npm run build成功；已部署至gh-pages

---

### P-20260502-009: game-1024 V3 — 视觉动画增强

- `Proposal ID`: `P-20260502-009`
- `Title`: game-1024 V3 — 视觉动画增强
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project`: PRJ-20250416-002（game-1024）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-009-prd.md
- `Stage`: V3 Iteration
- `Last Update`: 2026-05-02
- `Notes`: 方块移动动画(150ms ease-out)+合并动画(scale爆开)+新方块出现动画(scale放大)+分数飘字

---

### P-20260502-010: game-1024 V3 — 音效系统

- `Proposal ID`: `P-20260502-010`
- `Title`: game-1024 V3 — 音效系统
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project`: PRJ-20250416-002（game-1024）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-010-prd.md
- `Stage`: V3 Iteration
- `Last Update`: 2026-05-02
- `Notes`: Web Audio API合成音效(滑动/合并/胜利/失败)+音效开关+AudioManager封装

---

### P-20260502-011: game-1024 V4 — 悔棋/重试功能

- `Proposal ID`: `P-20260502-011`
- `Title`: game-1024 V4 — 悔棋/重试功能
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project`: PRJ-20250416-002（game-1024）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-011-prd.md
- `Stage`: V4 Iteration
- `Last Update`: 2026-05-02
- `Notes`: 历史快照栈(最多10步)+撤销按钮+重试按钮；每日挑战撤销不影响seed状态

---

### P-20260502-012: game-1024 V4 — 数据统计面板

- `Proposal ID`: `P-20260502-012`
- `Title`: game-1024 V4 — 数据统计面板
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project`: PRJ-20250416-002（game-1024）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-012-prd.md
- `Stage`: V4 Iteration
- `Last Update`: 2026-05-02
- `Notes`: 成就页面Tab切换(成就/统计)+各模式分别统计(场次/胜率/最高分/平均分)+localStorage持久化

---

### P-20260502-013: game-1024 V5 — 更多皮肤

- `Proposal ID`: `P-20260502-013`
- `Title`: game-1024 V5 — 更多皮肤
- `Owner`: 小墨
- `Current Status`: in_dev
- `Project`: PRJ-20250416-002（game-1024）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-013-prd.md
- `Stage`: V5 Iteration
- `Last Update`: 2026-05-02
- `Notes`: 节日皮肤(春节/圣诞/万圣节)+暗黑模式+成就解锁皮肤(彩虹/钻石/星空/复古)

---

### P-20260502-014: game-1024 V5 — 自定义棋盘

- `Proposal ID`: `P-20260502-014`
- `Title`: game-1024 V5 — 自定义棋盘
- `Owner`: 小墨
- `Current Status`: in_dev
- `Project`: PRJ-20250416-002（game-1024）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-014-prd.md
- `Stage`: V5 Iteration
- `Last Update`: 2026-05-02
- `Notes`: 棋盘尺寸切换(4×4/5×5/6×6)+进阶/地狱难度+初始方块数递增+每日挑战仅支持4×4

---

### P-20260502-008: game-1024 V2 — 每日挑战+成就系统

- `Proposal ID`: `P-20260502-008`
- `Title`: game-1024 V2 — 每日挑战+成就系统
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project`: PRJ-20250416-002（game-1024）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-008-prd.md
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Last Update`: 2026-05-02
- `Notes`: 每日挑战(固定初始盘面+得分排名)+10个成就(解锁弹窗+奖励)；参考3D打地鼠V4实现

---

### P-20260412-009: ai-stock-simulation

- `Proposal ID`: `P-20260412-009`
- `Title`: ai-stock-simulation
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/ai-stock-simulation/`
- `Acceptance`: accepted
- `GitHub Repo`: https://github.com/YeLuo45/ai-stock-simulation
- `Last Update`: 2026-04-12
- `Notes`: 纯前端项目（已移除后端）；前端端口3100；localStorage持久化；20只模拟A股；赛博朋克终端风格；分支feature/frontend已push；强化回测已提交至feature/backtest-enhance分支

### P-20260505-001: ai-stock-simulation 完整交易闭环

- `Proposal ID`: `P-20260505-001`
- `Title`: ai-stock-simulation 完整交易闭环
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/ai-stock-simulation/`
- `PRD Path`: `workspace-pm/proposals/P-20260505-001-prd.md`
- `Acceptance`: accepted
- `GitHub Repo`: https://github.com/YeLuo45/ai-stock-simulation
- `Last Update`: 2026-05-05
- `Notes`: P0方向：持仓管理+买入/卖出+交易记录+实时盈亏计算；分支feature/sup_wx已push并merge

### P-20260505-002: ai-stock-simulation 强化回测系统

- `Proposal ID`: `P-20260505-002`
- `Title`: ai-stock-simulation 强化回测系统
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project Path`: `proposals/workspace-dev/proposals/ai-stock-simulation/`
- `PRD Path`: `workspace-pm/proposals/P-20260505-002-prd.md`
- `GitHub Repo`: https://github.com/YeLuo45/ai-stock-simulation
- `GitHub Branch`: feature/backtest-enhance
- `Last Update`: 2026-05-05
- `Notes`: K线图(lightweight-charts)/真实MA交叉信号/网格搜索/CSV导出；修复后验收通过；分支feature/backtest-enhance已push

### P-20260505-003: ai-stock-simulation 纯前端重构

- `Proposal ID`: `P-20260505-003`
- `Title`: ai-stock-simulation 纯前端重构
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project Path`: `proposals/workspace-dev/proposals/ai-stock-simulation/`
- `PRD Path`: `workspace-pm/proposals/P-20260505-003-prd.md`
- `GitHub Repo`: https://github.com/YeLuo45/ai-stock-simulation
- `GitHub Branch`: feature/backtest-enhance
- `PRD Confirmation`: confirmed
- `Last Update`: 2026-05-05
- `Notes`: IndexedDB持久化存储；交易逻辑(买入/卖出/手续费)；AkShare/东方财富实时行情；backend/已删除；分支feature/backtest-enhance已push

### P-20260505-004: ai-stock-simulation K线指标面板增强

- `Proposal ID`: `P-20260505-004`
- `Title`: ai-stock-simulation K线指标面板增强
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Project Path`: `proposals/workspace-dev/proposals/ai-stock-simulation/`
- `PRD Path`: `workspace-pm/proposals/P-20260505-004-prd.md`
- `GitHub Repo`: https://github.com/YeLuo45/ai-stock-simulation
- `GitHub Branch`: feature/backtest-enhance
- `PRD Confirmation`: confirmed
- `Last Update`: 2026-05-05
- `Notes`: K线主图+MA5/10/20；MACD副图(DIF/DEA/柱子)；RSI副图+30/70线；KDJ副图；十字光标同步；timeScale同步；npm build成功

---

### P-20250418-003: harness-desktop

- `Proposal ID`: `P-20250418-003`
- `Title`: harness-desktop
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/harness-desktop/`
- `Acceptance`: accepted
- `Deployment URL`: https://github.com/YeLuo45/harness-desktop/releases/tag/v1.0.1
- `GitHub Repo`: https://github.com/YeLuo45/harness-desktop
- `Last Update`: 2026-04-18
- `Notes`: Electron + React + Vite + TypeScript 桌面应用；二进制包已上传 GitHub Releases (v1.0.0)

---

### P-20260502-004: harness-desktop v3 — 多模型路由

- `Proposal ID`: `P-20260502-004`
- `Title`: harness-desktop v3 — 多模型路由
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20250418-003（harness-desktop）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-004-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/harness-desktop/P-20260502-004-tech-solution.md
- `Stage`: v3 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: timeout-approved
- `Current Status`: in_tdd_test
- `Last Update`: 2026-05-03
- `Notes`: TDD 测试用例已生成（src/__tests__/modelRouting.test.ts + llmBridge.test.ts）；Vitest 1.x 需要 Node 20+，当前环境 Node 18.19.1；测试文件语法正确，待升级 Node 后可运行；建议后续开发环境升级 Node 20+

---

### P-20260502-003: harness-desktop v2 — Sub Agent + Verification Hooks + 更多工具

- `Proposal ID`: `P-20260502-003`
- `Title`: harness-desktop v2 — Sub Agent + Verification Hooks + 更多工具
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `Project`: PRJ-20250418-003（harness-desktop）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-003-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/harness-desktop/P-20260502-003-tech-solution.md
- `Stage`: v2 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-02
- `Notes`: v2 迭代已完成交付：①Sub Agent（共享KV Cache + 任务队列 + 依赖管理）②Verification Hooks后台分类器（strict/loose/disabled三档 + auto-retry）③4个新工具（edit_code/project_tree/web_search/task_plan）；llmBridge.ts MVP_TOOLS→V2_TOOLS 已修复；Vite build成功；electron-builder打包受限WSL环境（需Windows本机执行）

---

### P-20250418-004: future-little-leaders — 亲子习惯养成平台

- `Proposal ID`: `P-20250418-004`
- `Title`: future-little-leaders — 亲子习惯养成平台
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20260508（future-little-leaders）
- `Project Path`: `/home/hermes/future-little-leaders/`（开发目录）
- `Source Path`: `proposals/workspace-dev/proposals/future-little-leaders/`（源码）
- `Deployment URL`: https://yeluo45.github.io/future-little-leaders/
- `GitHub Repo`: https://github.com/YeLuo45/future-little-leaders
- `Engine`: uni-app + Vue 3 + Vite + Pinia 2.1.7
- `Stage`: V1（基础功能完成）
- `Acceptance`: accepted
- `Last Update`: 2026-05-03
- `Notes`: uni-app 多平台项目（H5 构建）；宝宝管理+每日任务+周期性任务+积分系统+商城+社区；feature/hermes20260503 分支已完善 README/CHANGELOG/manifest.json
- `Feature Branch`: `feature/hermes20260503`（文档完善）
- `Core Modules`:
  - 宝宝管理（添加/编辑/删除 + 头像 + 年龄计算）
  - 每日任务（创建/执行/积分奖励）
  - 周期性任务（每日/每周/自定义打卡）
  - 积分系统（收支记录 + 余额显示）
  - 积分商城（商品浏览/兑换/兑换记录）
  - 任务统计（完成趋势 + 数据可视化）
  - 社区分享（发布/浏览/收藏）

---

### P-20260419-003: 别踩白块（Web + PWA）

- `Proposal ID`: `P-20260419-003`
- `Title`: 别踩白块（Web + PWA）
- `Owner`: 小墨
- `Current Status`: `delivered`
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260419-003-intake.md`
- `Technical Solution`: `proposals/workspace-dev/proposals/P-20260419-003-tech-solution.md`
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`
- `Acceptance`: accepted
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Countdown ID`: -
- `Technical Expectations`: confirmed
- `Technical Expectations Countdown ID`: -
- `Last Update`: 2026-04-19
- `Notes`: V1已交付；经典钢琴块玩法；4列8行网格；←→移动+点击踩黑块；失败条件：踩白块/漏踩黑块；React 18 + Vite 5 + PWA；分数/速度递增/历史最高分/PWA离线/音效

---

### P-20260504-001: 别踩白块 V2 — 无尽模式 + 道具系统

- `Proposal ID`: `P-20260504-001`
- `Title`: 别踩白块 V2 — 无尽模式 + 道具系统
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-001-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V2（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: P0无尽模式（命机制+combo计分+速度递增）+P1道具系统（护盾/冰冻/双倍）+游戏结束画面+昵称分数记录

---

### P-20260504-002: 别踩白块 V3 — 金币经济 + 皮肤商店 + 关卡挑战

- `Proposal ID`: `P-20260504-002`
- `Title`: 别踩白块 V3 — 金币经济 + 皮肤商店 + 关卡挑战
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-002-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V3（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: P1金币经济系统+皮肤商店（4套主题：默认/霓虹/简约/赛博朋克）+P2关卡挑战（6关：限时60秒/极速/纯净/生死/巨慢/无限）+CSS变量主题方案

---

### P-20260504-003: 别踩白块 V4 — 分享式排行榜

- `Proposal ID`: `P-20260504-003`
- `Title`: 别踩白块 V4 — 分享式排行榜
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001, P-20260504-002
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-003-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V4（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 纯前端分享式排行榜；URL参数base64编码分享战绩；无需后端；我的战绩历史记录；Web Share API或复制链接；30天过期机制

---

### P-20260504-004: 别踩白块 V5 — 移动端适配

- `Proposal ID`: `P-20260504-004`
- `Title`: 别踩白块 V5 — 移动端适配
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001, P-20260504-002, P-20260504-003
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-004-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V5（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 安全区域适配（刘海/灵动岛/底部导航栏）；viewport防缩放；横屏锁定+旋转提示；PWA安装提示；触控优化（48px最小触控区域+touch-action）

---

### P-20260504-005: 别踩白块 V6 — 限时挑战模式

- `Proposal ID`: `P-20260504-005`
- `Title`: 别踩白块 V6 — 限时挑战模式
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001, P-20260504-002, P-20260504-003, P-20260504-004
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-005-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V6（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 60秒限时挑战；踩黑块+3秒；4档难度递增；连击奖励+时间奖励；结算界面等级系统；限时模式最高分持久化

---

### P-20260504-006: 别踩白块 V7 — 音效与BGM

- `Proposal ID`: `P-20260504-006`
- `Title`: 别踩白块 V7 — 音效与BGM
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-005
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-006-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V7（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: Web Audio API 音效（踩黑/白块音、道具音、按钮音）；80BPM单音钢琴BGM；设置界面音效/BGM开关+音量滑块；倒计时≤10秒警告音

---

### P-20260504-007: 别踩白块 V8 — 关卡编辑器

- `Proposal ID`: `P-20260504-007`
- `Title`: 别踩白块 V8 — 关卡编辑器
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-006
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-007-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V8（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 8×4可视化关卡编辑器；点击切换空/黑/白；预览播放；Base64分享链接(?level=xxx)；localStorage保存自定义关卡；自定义关卡循环播放

---

### P-20260504-008: 别踩白块 V9 — 成就系统

- `Proposal ID`: `P-20260504-008`
- `Title`: 别踩白块 V9 — 成就系统
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-007
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-008-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V9（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 30+成就分6类（连击/分数/挑战/收集/特殊/新手）；奖励系统（金币/称号/皮肤）；3秒Toast通知；localStorage持久化；主菜单成就入口

---

### P-20260504-009: 别踩白块 V10 — 每日挑战

- `Proposal ID`: `P-20260504-009`
- `Title`: 别踩白块 V10 — 每日挑战
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-008
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-009-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V10（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 4种挑战类型（盲眼/速度/精准/节奏）；日期hash确定性关卡生成；复活机制（50金币/广告）；今日排行榜/历史记录；首次参与昵称设置

---

### P-20260504-010: 别踩白块 V11 — 皮肤商店

- `Proposal ID`: `P-20260504-010`
- `Title`: 别踩白块 V11 — 皮肤商店
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-009
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-010-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V11（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 10种皮肤（格子/背景/特效/指示器）；等级系统（免费/普通/稀有/传说）；Tab切换；CSS变量注入；localStorage持久化；主菜单皮肤商店入口

---

### P-20260504-011: 别踩白块 V12 — 剧情模式

- `Proposal ID`: `P-20260504-011`
- `Title`: 别踩白块 V12 — 剧情模式
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-010
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-011-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V12（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 3章节×10关（森林/城市/星空）；独特背景视觉；难度递增（黑块概率+3%/关）；BOSS关双倍速度；3条命系统；通关奖励；localStorage进度保存

---

### P-20260504-012: 别踩白块 V13 — 高级设置

- `Proposal ID`: `P-20260504-012`
- `Title`: 别踩白块 V13 — 高级设置
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-011
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-012-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V13（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 无尽/限时/剧情速度独立可调；操作模式（触控/滑动手势/陀螺仪）；灵敏度调节；辅助功能（颜色滤镜/色盲模式）；震动反馈；自动存档；localStorage持久化

---

### P-20260504-013: 别踩白块 V14 — 签到/每日任务

- `Proposal ID`: `P-20260504-013`
- `Title`: 别踩白块 V14 — 签到/每日任务
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-012
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-013-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V14（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 7天连续签到奖励（10→100金币）；断签重置；7个每日任务（游戏次数/连击/得分/挑战/剧情/分享）；Tab切换；奖励发放动画；UTC每日重置；localStorage持久化

---

### P-20260504-014: 别踩白块 V15 — 分享海报生成器

- `Proposal ID`: `P-20260504-014`
- `Title`: 别踩白块 V15 — 分享海报生成器
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-013
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-014-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V15（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: Canvas绘制海报(750×1334px)；海报内容(Logo/昵称/日期/战绩/皮肤/称号/成就/二维码)；下载PNG/复制剪贴板/Web Share API；三个入口(结算/成就/每日奖励)

---

### P-20260504-015: 别踩白块 V16 — 数据统计面板

- `Proposal ID`: `P-20260504-015`
- `Title`: 别踩白块 V16 — 数据统计面板
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-014
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-015-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V16（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 基础统计(游戏次数/时长/得分/连击)；里程碑记录(最高分/最高连击/最长存活)；环形图(模式时间占比)；7日活跃柱状图；localStorage持久化；游戏结束时更新数据

---

### P-20260504-016: 别踩白块 V17 — 观战/回放系统

- `Proposal ID`: `P-20260504-016`
- `Title`: 别踩白块 V17 — 观战/回放系统
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-015
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `Branch`: `feature/20260504-v16`
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-016-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V17（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 录像录制(点击列+时间戳)；localStorage存储最近10条；回放播放控制(播放/暂停/快进1x/2x/4x/进度条)；Base64分享链接(?replay=xxx)；游戏结束保存弹窗

---

### P-20260504-018: 别踩白块 V18 — 排行榜 Pro

- `Proposal ID`: `P-20260504-018`
- `Title`: 别踩白块 V18 — 排行榜 Pro
- `Owner`: 小墨
- `Current Status`: `delivered`
- `Parent`: P-20260419-003, P-20260504-001~P-20260504-016
- `Project Path`: `proposals/workspace-dev/proposals/dont-step-white/`（同目录迭代）
- `GitHub Repo`: https://github.com/YeLuo45/dont-step-white
- `Branch`: `feature/v18-leaderboard-pro`
- `PRD Path`: `proposals/workspace-pm/proposals/P-20260504-018-prd.md`
- `Deployment URL`: https://yeluo45.github.io/dont-step-white/ (gh-pages)
- `Stage`: V18（已交付）
- `Acceptance`: accepted
- `Last Update`: 2026-05-04
- `Notes`: 4维度排行榜(全球/本地/好友/关卡)；Tab切换；预置模拟玩家+本地插入；好友码系统；关卡挑战榜(剧情30关+每日挑战)；Top3奖牌图标+我的排名金色高亮
- `PRD Confirmation`: confirmed

---

### P-20250421-002: ai-novel-assistant

- `Proposal ID`: `P-20250421-002`
- `Title`: ai-novel-assistant
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: MVP
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `Last Update`: 2026-04-22
- `Notes`: AI小说助手；React + Vite + Dexie (IndexedDB) + Zustand + react-beautiful-dnd + react-router-dom；功能待确认
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant

---

### P-20260502-001: ai-novel-assistant 迭代：写作编辑器 + AI 辅助

- `Proposal ID`: `P-20260502-001`
- `Title`: ai-novel-assistant 迭代：写作编辑器 + AI 辅助
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-001-prd.md
- `Technical Solution`: proposals/workspace-pm/proposals/P-20260502-001-technical-solution.md
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Last Update`: 2026-05-02
- `Notes`: WritingEditor + AIAssistBar + WordCountBar + OutlineTree 双向联动；交付完毕

---

### P-20260502-002: ai-novel-assistant 迭代：素材卡系统 + EPUB/PDF 导出

- `Proposal ID`: `P-20260502-002`
- `Title`: ai-novel-assistant 迭代：素材卡系统 + EPUB/PDF 导出
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-002-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Last Update`: 2026-05-02
- `Notes`: 素材卡CRUD + MaterialPanel + CardReference阅读态 + PDF导出；交付完毕

---

### P-20260502-003: ai-novel-assistant 大模型能力重构（复刻 llm-design-dev）

- `Proposal ID`: `P-20260502-003`
- `Title`: ai-novel-assistant 大模型能力重构（复刻 llm-design-dev）
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: Refactoring
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-003-prd.md
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Last Update`: 2026-05-02
- `Notes`: Provider架构(ai/providers.ts) + callLLM/streamLLM(ai/llm.ts) + 重试(ai/retry.ts) + Thinking适配(ai/thinking.ts) + 流式JSON解析(ai/parsers.ts) + AIAssistBar流式输出改造；M4 EPUB核心逻辑已实现（EpubExportService.ts + ExportPanel.tsx）；master已重建(28adee2)触发Actions构建，但deploy步骤持续失败，gh-pages未更新(仍a4397d4)；网络阻塞导致无法git push和API上传2.3MB vendor-misc blob；当前部署SHA: a4397d4(旧) | master SHA: 28adee2(新)

---

### P-20260504-001: ai-novel-assistant V5 — 写作流程增强

- `Proposal ID`: `P-20260504-001`
- `Title`: ai-novel-assistant V5 — 写作流程增强
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V5 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-001-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: e117dd5
- `Last Update`: 2026-05-04
- `Notes`: 章节大纲拖拽排序 + 字数目标追踪(每日/全书) + 写作统计Dashboard(7天柱状图/完成度环形图) + 剧情线颜色标签
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Timeout Resolution`: PRD确认倒计时到期(2026-05-04)，默认通过处理
- `Acceptance`: accepted

---

### P-20260504-002: ai-novel-assistant V6 — AI辅助功能升级

- `Proposal ID`: `P-20260504-002`
- `Title`: ai-novel-assistant V6 — AI辅助功能升级
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V6 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-002-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: 6278e69
- `Last Update`: 2026-05-04
- `Notes`: 多轮对话上下文(IndexedDB持久化) + 世界观助手Tab(素材卡问答) + 智能写作建议(续写/润色diff展示)
- `PRD Confirmation`: confirmed
- `Acceptance`: accepted

---

### P-20260504-003: ai-novel-assistant V7 — 导出能力完善

- `Proposal ID`: `P-20260504-003`
- `Title`: ai-novel-assistant V7 — 导出能力完善
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V7 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-003-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: 3fdb53c
- `Last Update`: 2026-05-04
- `Notes`: EPUB封面已有(cover.xhtml) + 目录卷>章>节三级NCX + DC元数据 + PDF排版优化(pdfmake)
- `PRD Confirmation`: timeout-approved
- `Acceptance`: accepted

### P-20260504-004: ai-novel-assistant V8 — 数据同步与备份

- `Proposal ID`: `P-20260504-004`
- `Title`: ai-novel-assistant V8 — 数据同步与备份
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V8 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260504-004-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: 84c6d45
- `Last Update`: 2026-05-05
- `Notes`: BackupPanel(导出/导入/云端三Tab) + BackupService(JSON.zip导出/导入/冲突处理) + LocalBackupProvider(localStorage快照) + 自动备份提示(30分钟Toast)
- `Acceptance`: accepted

---

### P-20260505-001: ai-novel-assistant V9 — 多角色视角管理

- `Proposal ID`: `P-20260505-001`
- `Title`: ai-novel-assistant V9 — 多角色视角管理
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V9 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-001-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: e26d280
- `Last Update`: 2026-05-05
- `Notes`: ViewpointSwitcher(第一人称/第三人称切换) + CharacterAvatar(头像/缩写) + CharacterRelationshipList(关系列表/关系图) + Dashboard角色统计 + WritingEditor集成
- `Acceptance`: accepted

---

### P-20260505-002: ai-novel-assistant V10 — 大纲视图增强

- `Proposal ID`: `P-20260505-002`
- `Title`: ai-novel-assistant V10 — 大纲视图增强
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V10 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-002-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: bff0a31
- `Last Update`: 2026-05-05
- `Notes`: TimelineView(锯齿布局时间轴) + TimelineCard(章节卡片/剧情线色块) + TimelineControls(缩放50-200%/剧情线筛选) + ProjectEditor时间线Tab + moveOutlineNode跨父节点拖拽修复
- `Acceptance`: accepted

---

### P-20260505-003: ai-novel-assistant V11 — 写作目标与提醒

- `Proposal ID`: `P-20260505-003`
- `Title`: ai-novel-assistant V11 — 写作目标与提醒
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V11 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-003-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: c686132
- `Last Update`: 2026-05-05
- `Notes`: DailyGoalTracker(环形进度条/连续打卡) + MilestonePanel(CRUD/甘特图进度) + WritingHeatmap(GitHub风365天热力图) + WritingReminder(浏览器通知) + ReminderService + db.ts v8(milestones/reminderSettings)
- `Acceptance`: accepted

---

### P-20260505-V12-001: ai-novel-assistant V12 — AI写作深化

- `Proposal ID`: `P-20260505-V12-001`
- `Title`: ai-novel-assistant V12 — AI写作深化
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V12 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V12-001-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: 636108d
- `Deployed`: https://yeluo45.github.io/ai-novel-assistant/
- `Last Update`: 2026-05-05
- `Notes`: M1章节情节自动生成(大纲→完整章节) + M2文风一致性检测(diff报告+修复建议) + M3批量润色(多章节勾选+diff预览+选择性采纳)
- `PRD Confirmation`: timeout-approved
- `Acceptance`: accepted

---

### P-20260505-V13-001: ai-novel-assistant V13 — AI写作深化（续）

- `Proposal ID`: `P-20260505-V13-001`
- `Title`: ai-novel-assistant V13 — AI写作深化（续）
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V13 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V13-001-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: e3c3d02
- `Deployed`: https://yeluo45.github.io/ai-novel-assistant/
- `Last Update`: 2026-05-05
- `Notes`: M1大纲自动续写(章节内容→推断剧情走向→生成后续大纲) + M2角色对话生成(场景+角色+情绪→符合性格的对话)
- `PRD Confirmation`: timeout-approved
- `Acceptance`: accepted

---

### P-20260505-V14-001: ai-novel-assistant V14 — 版权与版本管理

- `Proposal ID`: `P-20260505-V14-001`
- `Title`: ai-novel-assistant V14 — 版权与版本管理
- `Owner`: 小墨
- `Current Status`: delivered
- `Parent`: P-20250421-002 (ai-novel-assistant)
- `Engine`: React 18 + Vite 5 + TypeScript
- `Target`: Web
- `Stage`: V14 Iteration
- `Project Path`: proposals/workspace-dev/proposals/ai-novel-assistant/
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-V14-001-prd.md
- `GitHub Repo`: https://github.com/YeLuo45/ai-novel-assistant
- `Dev Commit`: e9c050d
- `Deployed`: https://yeluo45.github.io/ai-novel-assistant/
- `Last Update`: 2026-05-05
- `Notes`: M1章节版本历史(chapterVersions表+版本列表+diff对比+恢复) + M2敏感词检测(5类敏感词+高亮标记+替换建议)
- `PRD Confirmation`: timeout-approved
- `Acceptance`: accepted

---

### P-20250418-002: creative-drawing-board
- `Title`: 儿童创意画板 (Creative Drawing Board)
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: HTML5 Canvas (单文件)
- `Target`: 浏览器（HTML5）
- `Age Group`: 3-6岁幼儿
- `Stage`: 已交付
- `Project Path`: proposals/workspace-dev/proposals/creative-drawing-board/
- `Last Update`: 2026-04-18
- `Notes`: 儿童创意画板；纯HTML5单文件(745行)；自由画画/10色配色盘/3种笔刷/橡皮擦/泡泡游戏/音效反馈；完全离线可用
- `GitHub Repo`: https://github.com/YeLuo45/creative-drawing-board
- `Deployment URL`: https://yeluo45.github.io/creative-drawing-board/

---

### P-20250420-001: snake-battle

- `Proposal ID`: `P-20250420-001`
- `Title`: 贪吃蛇大作战 (Snake Battle)
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 18 + Vite 5 + Canvas 2D + PWA
- `Target`: Web + Mobile (PWA)
- `Stage`: 已交付
- `Project Path`: proposals/workspace-dev/proposals/snake-battle/
- `Last Update`: 2026-04-20
- `Notes`: 贪吃蛇大作战；经典模式(单蛇吃食物)+AI对战(1玩家+3AI蛇,3分钟倒计时)；3套皮肤(Classic/Neon/Candy)；localStorage存档
- `GitHub Repo`: https://github.com/YeLuo45/snake-battle
- `Deployment URL`: https://yeluo45.github.io/snake-battle/

---

### P-20250419-002: tank-battle

- `Proposal ID`: `P-20250419-002`
- `Title`: 坦克大作战 (Tank Battle)
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 18 + Vite 5 + Tailwind CSS 3 + Canvas 2D + PWA
- `Target`: Web + Mobile (PWA)
- `Stage`: 已交付
- `Project Path`: proposals/workspace-dev/proposals/tank-battle/
- `Last Update`: 2026-04-19
- `Notes`: 坦克大战；13x13网格；WASD/方向键移动+空格射击；4种地形(砖块/钢铁/草丛/河流)；AI巡逻+追击；保护老鹰基地；3分钟倒计时
- `GitHub Repo`: https://github.com/YeLuo45/tank-battle
- `Deployment URL`: https://yeluo45.github.io/tank-battle/

---

### P-20250418-005: todo-app

- `Proposal ID`: `P-20250418-005`
- `Title`: Hermes Todo App
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 18 + Vite + Electron
- `Target`: Web + Windows Desktop
- `Stage`: 已交付
- `Project Path`: proposals/workspace-dev/proposals/todo-app/
- `Last Update`: 2026-04-18
- `Notes`: Todo应用；Web版+Vite构建+Electron桌面客户端(electron-builder打包)；NSIS安装包+便携版
- `GitHub Repo`: https://github.com/YeLuo45/todo-app

---

### P-20250420-002: pixel-pal-web

- `Proposal ID`: `P-20250420-002`
- `Title`: PixelPal (AI Companion Desktop App)
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 19 + TypeScript + Electron + Vite
- `Target`: Windows Desktop
- `Stage`: 已交付 (V1: 2026-04-20, V2: 2026-05-03)
- `Project Path`: proposals/workspace-dev/proposals/pixel-pal-web/
- `Last Update`: 2026-05-03
- `Notes`: V2 已交付：记忆持久化（IndexedDB）+ Companion 人格与情感系统（5人格+8情绪+主动问候）；Settings 新增 Companion Personality 面板
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Deployment URL`: https://YeLuo45.github.io/pixel-pal-web

---

### P-20260503-025: PixelPal V2 — 记忆持久化 + Companion 人格层

- `Proposal ID`: `P-20260503-025`
- `Title`: PixelPal V2 — 记忆持久化 + Companion 人格层
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 19 + TypeScript + Electron + Vite
- `Target`: Windows Desktop + Web
- `Stage`: V2 已交付
- `Project Path`: proposals/workspace-dev/proposals/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260503-025-intake.md
- `Last Update`: 2026-05-03
- `Notes`: V2 核心迭代：记忆持久化（IndexedDB）+ Companion 人格与情感系统（5人格+8情绪+主动问候）；Settings 新增 Companion Personality 面板；GitHub Actions 自动构建部署
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Deployment URL`: https://YeLuo45.github.io/pixel-pal-web

---

### P-20260503-026: PixelPal V3 — 主动动作系统

- `Proposal ID`: `P-20260503-026`
- `Title`: PixelPal V3 — 主动动作系统
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 19 + TypeScript + Electron + Vite
- `Target`: Windows Desktop + Web
- `Stage`: V3 已交付
- `Project Path`: proposals/workspace-dev/proposals/pixel-pal-web/
- `PRD Path`: workspace-pm/proposals/P-20260503-026-intake.md
- `Last Update`: 2026-05-03
- `Notes`: V3 核心迭代：Companion 动作引擎（remind/celebrate/greet/suggest/memory_recall）+ 动作队列 + ActionBadge/ActionToast UI + 任务完成感知触发庆祝
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Deployment URL`: https://YeLuo45.github.io/pixel-pal-web

---

### P-20260503-029: PixelPal V4 — Model UI + Thinking

- `Proposal ID`: `P-20260503-029`
- `Title`: PixelPal V4 — Model UI + Thinking
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commit`: c39e651
- `Acceptance`: 小墨于2026-05-03验收通过
- `Last Update`: 2026-05-03
- `Notes`: AI思考过程可视化 + Thinking Panel + Model Status Indicator + 推理步骤展示

---

### P-20260503-030: PixelPal V5 — Multi-Persona Collaboration

- `Proposal ID`: `P-20260503-030`
- `Title`: PixelPal V5 — Multi-Persona Collaboration
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commit`: 97f271f
- `Acceptance`: 小墨于2026-05-03验收通过
- `Last Update`: 2026-05-03
- `Notes`: 多Persona协作系统 + Team管理 + 角色分工(primary/contributor/observer) + 协作讨论面板 + 5个预设Persona(小墨/小皮/小博/小柔/小机)

---

### P-20260503-031: PixelPal V6 — RAG Knowledge Base

- `Proposal ID`: `P-20260503-031`
- `Title`: PixelPal V6 — RAG Knowledge Base
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commit`: 1b45acd
- `Acceptance`: 小墨于2026-05-03验收通过
- `Last Update`: 2026-05-03
- `Notes`: RAG知识库系统 + 文档上传/分块(BM25)/检索 + 上下文注入 + IndexedDB持久化 + Knowledge面板 + ChatPanel RAG增强

---

### P-20260503-032: PixelPal V7 — Voice 语音交互

- `Proposal ID`: `P-20260503-032`
- `Title`: PixelPal V7 — Voice 语音交互
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commit`: 49838ed
- `Acceptance`: 小墨于2026-05-03验收通过
- `Last Update`: 2026-05-03
- `Notes`: TTS语音输出(SpeechSynthesis API) + ASR语音输入(SpeechRecognition API) + VoiceSettings面板(Settings页) + VoiceInputButton(Chat页麦克风按钮) + VoiceService(VoiceService.ts) + 语音开关+语速/音调/音量/音色配置

---

### P-20260503-033: PixelPal V8 — Mobile PWA

- `Proposal ID`: `P-20260503-033`
- `Title`: PixelPal V8 — Mobile PWA 移动端优化
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commit`: ae87400
- `Acceptance`: 小墨于2026-05-03验收通过
- `Last Update`: 2026-05-03
- `Notes`: 移动端响应式布局 + Hamburger侧边抽屉导航 + PWA manifest + meta标签(apple-mobile-web-app) + 固定底部输入框(Chat) + 触控优化 + 响应式断点适配

---

### P-20260503-034: PixelPal V9 — Plugin System

- `Proposal ID`: `P-20260503-034`
- `Title`: PixelPal V9 — Plugin System 插件系统
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commit`: f133344
- `Acceptance`: 小墨于2026-05-03验收通过
- `Last Update`: 2026-05-03
- `Notes`: 插件架构核心(PluginService+PluginRegistry)+Todo插件(CRUD+筛选+IndexedDB)+Calendar插件(月视图)+Email插件(Gmail OAuth)+PluginHub+PluginPanel+导航Badge

---

### P-20260503-035: PixelPal V10 — Advanced Memory

- `Proposal ID`: `P-20260503-035`
- `Title`: PixelPal V10 — Advanced Memory 高级记忆系统
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commit`: 1c20078
- `Acceptance`: 小墨于2026-05-03验收通过
- `Last Update`: 2026-05-03
- `Notes`: AI对话摘要(Summarization)+实体抽取与关系图谱(entityGraph)+智能检索(时间衰减+频率加权)+Memory面板(4 tabs: All/Entities/Timeline/Insights)+Pin/Forget/Export

---

### P-20260503-036: PixelPal V11 — Desktop Electron

- `Proposal ID`: `P-20260503-036`
- `Title`: PixelPal V11 — Desktop Electron 桌面版
- `Owner`: 小墨
- `Current Status`: approved_for_dev
- `PRD Path`: proposals/workspace-pm/proposals/P-20260503-036-prd.md
- `Last Update`: 2026-05-03
- `Notes`: Electron桌面应用(main.ts+preload.ts)+系统托盘(右键菜单+双击)+原生通知+窗口管理(置顶+记忆位置)+electron-builder打包Windows exe

---

### P-20260503-037: PixelPal V12 — Multi-Language 多语言切换

- `Proposal ID`: `P-20260503-037`
- `Title`: PixelPal V12 — Multi-Language 多语言切换
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commits`: 2b3e770, 3e84883, d7da3c1, 1efd5ae, 66b8a6c
- `PRD Path`: workspace-pm/proposals/P-20260503-037-intake.md
- `Acceptance`: 小墨于2026-05-03验收通过
- `Last Update`: 2026-05-03
- `Notes`: i18next+react-i18next国际化框架+中英文翻译文件(locales/en.json/zh.json)+i18n服务初始化+Store语言状态+Settings语言切换器+Sidebar/ChatPanel/Calendar/Tasks/Knowledge/PluginHub/PluginPanel/Email/MemoryPanel/MultiPersonaCollaboration已完成i18n改造+workflow添加--legacy-peer-deps+package-lock.json同步

---

### P-20260504-001: PixelPal V13 — 高级记忆系统 v2

- `Proposal ID`: `P-20260504-001`
- `Title`: PixelPal V13 — 高级记忆系统 v2
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commits`: 9e088f9
- `PRD Path`: workspace-pm/proposals/P-20260504-001-intake.md
- `Last Update`: 2026-05-04
- `Notes`: 记忆搜索(关键词+时间范围+重要性过滤)+重要性评分算法(memoryScoring.ts:类型权重+访问加成+时间衰减)+JSON导出/导入+Timeline时间轴+词云(wordcloud包)+memoryTypes.ts改为0-100分数体系+CI#25295747284通过

---

### P-20260504-002: PixelPal V14 — Webhook + 插件生态

- `Proposal ID`: `P-20260504-002`
- `Title`: PixelPal V14 — Webhook + 插件生态
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commits`: 04d0373
- `PRD Path`: workspace-pm/proposals/P-20260504-002-intake.md
- `Last Update`: 2026-05-04
- `Notes`: WebhookService(IndexedDB存储+定时cron执行+事件触发)+WebhookStore+WebhookSettings面板(CRUD+执行日志)+WeatherPlugin(Open-Meteo)+NewsPlugin(rss-parser)+PluginHub安装/卸载+memoryStorage emit事件+CI#25296444465通过

---

### P-20260504-003: PixelPal V15 — 桌面端补全

- `Proposal ID`: `P-20260504-003`
- `Title`: PixelPal V15 — 桌面端补全
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commits`: 06614b3
- `PRD Path`: workspace-pm/proposals/P-20260504-003-intake.md
- `Last Update`: 2026-05-04
- `Notes`: electron/main.ts(托盘+通知+窗口管理+自启+快捷键+IPC)+electron/preload.ts(Settings IPC)+Settings桌面设置UI(开机自启+置顶+通知开关)+CI#25297376006通过

---

### P-20260504-004: PixelPal V16 — 场景模式/自动化

- `Proposal ID`: `P-20260504-004`
- `Title`: PixelPal V16 — 场景模式/自动化
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Branch`: v16-scenes
- `GitHub Repo`: https://github.com/YeLuo45/pixel-pal-web
- `Dev Commit`: d66c6e8
- `PRD Path`: workspace-pm/proposals/P-20260504-004-intake.md
- `Project Path`: workspace-dev/proposals/pixel-pal-web/
- `Last Update`: 2026-05-04
- `Stage`: V16 Iteration
- `Acceptance`: accepted
- `Notes`: 场景管理页面(ScenesPage)+场景卡片+编辑弹窗; 触发条件(定时⏰/点击🖱️/关键词🔑); 执行动作(发消息/切角色/朗读/通知); IndexedDB持久化(idb); Zustand sceneStore; QuickSceneBar(mobile FAB+bottom-sheet); 移动端适配(mobile Dialog全屏/按钮44px/表单垂直排列); 关键词触发已集成到ChatPanel; 5个预设场景模板(起床🌅/睡前🌙/专注🎯/休息☕/激励💪); 动作序列增强(delay⏱️/条件分支🔀/随机选择🎲); 场景执行历史(日志Tab+SceneLogPanel+成功/失败状态); JSON导入/导出(分享配置文件); 场景分组/标签(标签Chip过滤+编辑添加/删除); Electron桌面端打包(prepackage移除canvas原生模块+GitHub Actions Windows构建); npm run build成功; git push origin v16-scenes成功

---

### P-20260504-005: PixelPal V17 — 数据分析面板

- `Proposal ID`: `P-20260504-005`
- `Title`: PixelPal V17 — 数据分析面板
- `Owner`: 小墨
- `Current Status`: delivered
- `Dev Commits`: 33216a6
- `PRD Path`: workspace-pm/proposals/P-20260504-005-intake.md
- `Last Update`: 2026-05-04
- `Notes`: AnalyticsPanel(交互热力图+情绪趋势LineChart+记忆活跃度BarChart+习惯分析)+recharts图表库+Sidebar新增Analytics入口+CI#25297967195通过

---

### P-20250421-003: personalClaw

- `Proposal ID`: `P-20250421-003`
- `Title`: OpenClaw PC Control Platform
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 18 + TypeScript + Electron + Vite
- `Target`: Windows Desktop
- `Stage`: 已交付
- `Project Path`: proposals/workspace-dev/proposals/personalClaw/
- `Last Update`: 2026-04-21
- `Notes`: OpenClaw PC控制平台；Electron + React 18 + Ant Design + node-cron；桌面管理功能
- `GitHub Repo`: https://github.com/YeLuo45/personalClaw

---

### P-20260430-006: BabyGuard 宝贝护卫队

- `Proposal ID`: `P-20260430-006`
- `Title`: BabyGuard 宝贝护卫队 (育儿塔防游戏)
- `Owner`: 小墨
- `Current Status`: delivered
- `Project`: PRJ-20260430-001
- `Engine`: Godot 4 + GDScript
- `Target`: HTML5 (Web), Desktop
- `Game Type`: 2D Tower Defense Strategy
- `Stage`: MVP
- `Project Path`: `proposals/workspace-dev/proposals/tower-baby-guard/`
- `GitHub Repo`: https://github.com/YeLuo45/tower-baby-guard
- `PRD Confirmation`: N/A (direct to dev)
- `Technical Expectations`: N/A (direct to dev)
- `Last Update`: 2026-04-30
- `Notes`: 育儿主题塔防；5种防御塔(Mom/Dad/Grandma/Doctor/Chef)+4种敌人(Tantrum/Bedtime/Veggie/ScreenTime)+10波次；Godot 4 HTML5导出
- `Acceptance`: accepted

---

### P-20260419-001: 神庙大逃亡

- `Proposal ID`: `P-20260419-001`
- `Title`: 神庙大逃亡 - 多端跑酷游戏
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/temple-run/`
- `Acceptance`: accepted
- `Deployment URL`: https://yeluo45.github.io/temple-run/
- `GitHub Repo`: https://github.com/YeLuo45/temple-run
- `PRD Path`: `proposals/workspace-dev/proposals/temple-run/docs/prd.v1.md`
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Last Update`: 2026-04-19
- `Notes`: 类Temple Run无尽跑酷；2.5D侧视角；3条跑道左右切换；跳跃/下滑操作；金币收集；React 18 + Vite 5 + PWA；Web版已部署

---

### P-20260419-005: Hermes Agent Collab 团队协作增强

- `Proposal ID`: `P-20260419-005`
- `Title`: Hermes Agent Collab 团队协作增强
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/hermes-agent-collab/`
- `Feature Branch`: feature/agent
- `Acceptance`: accepted
- `GitHub Repo`: https://github.com/YeLuo45/hermes-agent-collab
- `PRD Path`: `proposals/workspace-dev/proposals/hermes-agent-collab/docs/prd.v1.md`
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Last Update`: 2026-04-23
- `Notes`: Phase 1-4 全部功能已验收通过。Phase 4 UI（任务Agent选择/对话UI/工作区CRUD/技能编辑）已部署 gh-pages: https://yeluo45.github.io/hermes-agent-collab/。注：Web UI 为纯静态前端，需后端 `collab server` 启动才能完整使用。
- `Main Fixes Applied`: 1. 修复 gh-pages 未同步 Phase 4 代码问题（feature/agent 分支代码已合并到 gh-pages）；2. 修复 HTML 内联 JS 语法错误（req 函数后多余 `}`）
- `Feature Branch Progress`: feature/agent 分支包含 Phase 4 UI 功能：
  - [x] 任务创建时指定 Agent
  - [x] 与 Agent 对话 UI
  - [x] 工作区 CRUD UI（重命名/删除）
  - [x] 工作区下创建 Agent（workspace 未选则禁用）
  - [x] 技能展示、编辑 UI（模态框编辑，API DELETE）

---

## Completed Proposals

### P-20260419-004: TradingAgents 中文增强版

- `Proposal ID`: `P-20260419-004`
- `Title`: TradingAgents 中文增强版
- `Owner`: 小墨
- `Current Status`: delivered
- `Project Path`: `proposals/workspace-dev/proposals/TradingAgents-CN/`
- `Acceptance`: accepted
- `GitHub Repo`: https://github.com/YeLuo45/TradingAgents-CN
- `Last Update`: 2026-04-19
- `Notes`: AI 量化交易代理系统；Python 3.10+；混合许可证（Apache 2.0 开源 + 专有前端后端需商业授权）；包含 FastAPI 后端 + Vue 前端 + Docker 部署；基于 TauricResearch/TradingAgents



### P-20260422-003: 休闲益智三消游戏原型

- `Proposal ID`: `P-20260422-003`
- `Title`: 休闲益智三消游戏原型
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: HTML5 Canvas + Vanilla JS
- `Stage`: Prototype Validation
- `Project Path`: proposals/workspace-dev/proposals/match3-puzzle/
- `Acceptance`: accepted
- `Deployment URL`: https://yeluo45.github.io/match3-puzzle/
- `GitHub Repo`: https://github.com/YeLuo45/match3-puzzle
- `Last Update`: 2026-04-24
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed

---

### P-20260422-004: 动物森林 - 儿童教育游戏

- `Proposal ID`: `P-20260422-004`
- `Title`: 动物森林 - 儿童教育游戏
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: HTML5 Canvas + Vanilla JS
- `Target`: Web + PC (浏览器直接运行)
- `Stage`: MVP 已交付
- `Project Path`: proposals/workspace-dev/proposals/animal-forest/
- `Last Update`: 2026-04-24
- `Notes`: 教育类/动物森林主题/卡通风格/双模式(3-6岁幼儿+7-12岁儿童)/家长面板；纯HTML5单文件，浏览器直接运行
- `PRD Path`: proposals/workspace-dev/proposals/animal-forest/docs/prd.v1.md
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Technical Solution`: proposals/workspace-dev/proposals/animal-forest/docs/technical-solution.v1.md
- `GitHub Repo`: https://github.com/YeLuo45/animal-forest
- `Deployment URL`: https://yeluo45.github.io/animal-forest/
- `Acceptance`: accepted
- `Acceptance Review`: 2026-04-24 — 代码审查+运行时验证全部通过；6动物/双模式/星星系统/家长PIN/音效/Web Audio API/localStorage进度存储/响应式布局均已实现

### P-20260504-animal-forest-A: Animal Forest V2 — 内容扩展

- `Proposal ID`: `P-20260504-animal-forest-A`
- `Title`: Animal Forest V2 — 内容扩展
- `Owner`: 小墨
- `Project`: PRJ-20260422-004（动物森林）
- `Stage`: V2 Iteration
- `Current Status`: delivered
- `Dev Commits`: 8695fc6(master) → gh-pages force-push
- `Deployed`: https://yeluo45.github.io/animal-forest/
- `Last Update`: 2026-05-04
- `Technical Expectations`: timeout-approved（技术栈继承V1：HTML5 Canvas + Vanilla JS）
- `Notes`: 方向A：新增字母/汉字/英语科目；动物从6种增至10种（小兔子/小松鼠/小鹿/小河狸）；题库量扩充（数字1-50/汉字200字/英语150词）；2页动物选择UI；index.html 1799→2485行；dev验收：4新动物+3新科目+题库+分页UI全部通过

---

### P-20260422-005: 儿童成长陪伴游戏

- `Proposal ID`: `P-20260422-005`
- `Title`: 儿童成长陪伴游戏
- `Owner`: 小墨
- `Current Status`: accepted
- `Engine`: HTML5 Canvas + Vanilla JS
- `Target`: Web + PC
- `Stage`: 已完成
- `Project Slug`: little-garden
- `Project Path`: proposals/workspace-dev/proposals/little-garden/
- `Last Update`: 2026-04-23
- `Notes`: 育儿游戏（3-12岁）；养成照顾类（宠物+种植）；纯HTML5/JS；完整GDD + 可运行游戏
- `Clarifying Round 1`: 类型(宠物+种植养成)/年龄(双模式3-6岁幼儿+7-12岁儿童)/引擎(纯HTML5/JS)/交付(游戏+GDD) — 已明确
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Technical Solution`: proposals/workspace-dev/proposals/little-garden/docs/technical-solution.v1.md
- `GitHub Repo`: https://github.com/YeLuo45/little-garden
- `Deployment URL`: https://yeluo45.github.io/little-garden/
- `Acceptance`: accepted
- `Main Fixes Applied`: 补充了缺失的宠物系统（宠物数据模型、Canvas 2D 绘制、喂食/抚摸/玩耍互动）、AudioManager 音效系统

---

### P-20260424-001: OpenMAIC

- `Proposal ID`: `P-20260424-001`
- `Title`: OpenMAIC
- `Owner`: 小墨
- `Current Status`: accepted
- `Engine`: Next.js 16 + React 19 + TypeScript
- `Target`: Web
- `Stage`: 源码已获取
- `Project Slug`: OpenMAIC
- `Project Path`: proposals/workspace-dev/proposals/OpenMAIC/
- `Last Update`: 2026-04-24
- `Notes`: Open Multi-Agent Interactive Classroom — 开放式多智能体交互课堂；forked from THU-MAIC/OpenMAIC (16311 stars)；pnpm + Next.js 16；需配置 LLM API Key 使用
- `Clarifying Round 1`: 直接从 Windows H:\WS\ai-tools\opensource\OpenMAIC 复制源码
- `GitHub Repo`: https://github.com/YeLuo45/OpenMAIC
- `Acceptance`: accepted

---

### P-20260426-001: 幼儿益智解谜游戏

- `Proposal ID`: `P-20260426-001`
- `Title`: 幼儿益智解谜游戏
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: HTML5 Canvas + Vanilla JS
- `Target`: 浏览器（HTML5，可直接在线玩）
- `Age Group`: 3-6岁学龄前儿童
- `Game Type`: 益智解谜
- `Stage`: 已交付
- `PRD Path`: proposals/workspace-pm/proposals/P-20260426-001-prd.md
- `Clarifying Round 1`: 游戏结构(独立小游戏+选关界面)/迷宫(随机生成)/分段(无需)/音效(背景音乐+操作音效) — 已明确
- `Last Update`: 2026-04-27
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Technical Expectations`: pending
- `Technical Expectations`: confirmed
- `Project Path`: proposals/workspace-dev/proposals/preschool-puzzle/
- `GitHub Repo`: https://github.com/YeLuo45/preschool-puzzle
- `Deployment URL`: https://yeluo45.github.io/preschool-puzzle/ (gh-pages)
- `Acceptance`: accepted
- `Acceptance Review`: 2026-04-27 — 单HTML文件(1622行)、3个游戏完整实现(ShapeMatch/ColorSort/Maze)、Web Audio API音效、localStorage进度保存、GitHub Pages已部署(gh-pages)、JS语法验证通过、控制台无Error
---

### P-20260424-002: Hermes 协作服务器消息转发机制重构

- `Proposal ID`: `P-20260424-002`
- `Title`: Hermes 协作服务器消息转发机制重构
- `Owner`: 小墨
- `Current Status`: delivered
- `Target`: Hermes 协作服务器 (collab-server)
- `Stage`: 已交付
- `PRD Path`: proposals/workspace-pm/proposals/P-20260424-002-prd.md
- `Technical Solution Path`: proposals/workspace-dev/proposals/P-20260424-002-tech-solution.md
- `Communication Approach`: DirectAgentClient（subprocess + 显式 ANTHROPIC_API_KEY）
- `Clarifying Round 1`: 问题确认 — 协作面板发送消息时 Agent 返回 "API call failed (Connection error)"；原因：EventBus 没有 handler 处理 AGENT_MESSAGE 事件；subprocess .env 未加载；架构缺陷：AgentProfile 没有 endpoint 字段
- `Notes`: 协作服务器消息转发机制重构；通过 DirectAgentClient (subprocess) 调用 Hermes AIAgent，显式传递 ANTHROPIC_API_KEY 环境变量解决凭证问题；3次连续测试100%成功响应；修复了 .env 加载问题和 API key 传递问题（commit 74469db → 51ef8f8）
- `PRD Confirmation`: timeout-approved
- `Technical Approach Confirmed`: DirectAgentClient subprocess 方案（2026-04-24 18:20）
- `Last Update`: 2026-04-24
- `Delivery Verification`: 3/3 测试成功，响应延迟正常
- `Commits`: 74469db (fix .env) → fb59bca (ACP client) → 51ef8f8 (DirectAgentClient 替代 ACP)

### P-20260430-007: 文档编辑器 Web 应用

- `Proposal ID`: `P-20260430-007`
- `Title`: 文档编辑器 Web 应用 (DocEditor)
- `Owner`: 小墨
- `Current Status`: delivered
- `Engine`: React 18 + Vite 5 + TypeScript + @tiptap/react
- `Target`: Web Browser
- `Stage`: MVP
- `Project Path`: `/mnt/c/Users/YeZhimin/Desktop/doc-editor/`
- `GitHub Repo`: https://github.com/YeLuo45/doc-editor
- `Deployment URL`: https://yeluo45.github.io/doc-editor/
- `PRD Confirmation`: timeout-approved (快速启动)
- `Technical Expectations`: confirmed (默认最优)
- `Last Update`: 2026-04-30
- `Notes`: 富文本编辑器(加粗/斜体/下划线/删除线/标题/列表/引用/代码块/链接/图片)+文档管理(侧边栏列表/新建/删除/重命名)+自动保存(2秒防抖)+历史版本(30秒快照)+导出(MD/HTML/打印PDF)+主题切换(亮/暗)+本地化中文；IndexedDB持久化；网络故障用GitHub API直接推送源码
- `Acceptance`: accepted
- `Iteration 1 Acceptance`: passed ({{ now }})

### P-20260430-002-iteration-1: 文档编辑器 - 文件夹与标签分类系统

- `Proposal ID`: `P-20260430-002-iteration-1`
- `Title`: 文档编辑器 - 文件夹与标签分类系统
- `Owner`: 小墨
- `Current Status`: delivered
- `Iteration`: 1
- `Iteration Acceptance`: passed (2026-04-30)
- `Engine`: React 18 + Vite 5 + TypeScript + @tiptap/react
- `Target`: Web Browser
- `Stage`: Feature Iteration
- `Project Path`: `/mnt/c/Users/YeZhimin/Desktop/doc-editor/`
- `GitHub Repo`: https://github.com/YeLuo45/doc-editor
- `Deployment URL`: https://yeluo45.github.io/doc-editor/
- `Last Update`: 2026-04-30
- `Notes`: 文件夹(创建/删除/将文档移动到文件夹)+标签(为文档打标签/筛选)+侧边栏三视图切换(全部/文件夹/标签)+IndexedDB v2(folders表)+Doc增加folderId/tags字段
- `Acceptance`: accepted

### P-20260430-002-iteration-2: 文档编辑器 - 全局搜索

- `Proposal ID`: `P-20260430-002-iteration-2`
- `Title`: 文档编辑器 - 全局搜索
- `Owner`: 小墨
- `Current Status`: delivered
- `Iteration`: 2
- `Iteration Acceptance`: passed (2026-04-30)
- `Engine`: React 18 + Vite 5 + TypeScript + @tiptap/react
- `Target`: Web Browser
- `Stage`: Feature Iteration
- `Project Path`: `/mnt/c/Users/YeZhimin/Desktop/doc-editor/`
- `GitHub Repo`: https://github.com/YeLuo45/doc-editor
- `Deployment URL`: https://yeluo45.github.io/doc-editor/
- `Last Update`: 2026-04-30
- `Notes`: 顶部搜索框实时搜索文档标题和内容(300ms防抖)，显示标题+内容片段+文件夹，最多10条结果，点击跳转
- `Acceptance`: accepted

---

### P-20260502-012: TodoList V3 — 云同步 + 导入导出

- `Proposal ID`: `P-20260502-012`
- `Title`: TodoList V3 — 云同步 + 导入导出
- `Owner`: 小墨
- `Current Status`: in_dev
- `Project`: PRJ-20250416-001（todo-list）
- `PRD Path`: proposals/workspace-pm/proposals/P-20260502-012-prd.md
- `Technical Solution`: proposals/workspace-dev/proposals/todo-list/P-20260502-012-tech-solution.md
- `Stage`: V3 Iteration
- `Acceptance`: pending
- `Notes`: GitHub云同步（PAT认证，数据存data/todos.json，自动push/pull）+ CSV/JSON导入导出
- `PRD Confirmation`: timeout-approved
- `Technical Expectations`: confirmed
- `Acceptance`: accepted
- `Last Update`: 2026-05-02

---

### P-20260502-013

- `Proposal ID`: `P-20260502-013`
- `Title`: TodoList V4 — 看板列内拖拽排序 + 统计仪表板
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V4 Iteration
- `Acceptance`: pending
- `Notes`: 看板列内拖拽排序（order字段）+ Canvas图表统计（柱状图/折线图/饼图）
- `PRD Confirmation`: timeout-approved（5分钟）
- `Technical Expectations`: confirmed
- `Last Update`: 2026-05-02

---

### P-20260502-014: TodoList V5 — 搜索增强 + 快捷键

- `Proposal ID`: `P-20260502-014`
- `Title`: TodoList V5 — 搜索增强 + 快捷键
- `Owner`: 小墨
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-02

- `Project`: PRJ-20250416-001（todo-list）
---

### P-20260502-015: TodoList V7 — 批量操作

- `Proposal ID`: `P-20260502-015`
- `Title`: TodoList V7 — 批量操作
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V7 Iteration
- `Acceptance`: accepted
- `Last Update`: 2026-05-02

- `Project`: PRJ-20250416-001（todo-list）
---

### P-20260502-016: TodoList V8 — 暗色模式 + 看板泳道 + 增强导出

- `Proposal ID`: `P-20260502-016`
- `Title`: TodoList V8 — 暗色模式 + 看板泳道 + 增强导出
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V8 Iteration
- `Acceptance`: accepted
- `Notes`: 暗色模式 + 看板泳道 + CSV/iCal 导出
- `Last Update`: 2026-05-02

- `Project`: PRJ-20250416-001（todo-list）
---

### P-20260503-023: TodoList V15 — PWA离线支持 + 周视图日历

- `Proposal ID`: `P-20260503-023`
- `Title`: TodoList V15 — PWA离线支持 + 周视图日历
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V15 Iteration
- `Acceptance`: accepted
- `Notes`: PWA manifest+ServiceWorker离线缓存 + 甘特图周/月视图切换(7天/30天时间轴)
- `Last Update`: 2026-05-03

- `Project`: PRJ-20250416-001（todo-list）
---

### P-20260503-027: TodoList V19 — 甘特图资源负载图 + 看板泳道按项目分组

- `Proposal ID`: `P-20260503-027`
- `Title`: TodoList V19 — 甘特图资源负载图 + 看板泳道按项目分组
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V19 Iteration
- `Acceptance`: accepted
- `Notes`: 资源负载图(条形高度=任务数,悬停tooltip) + 看板泳道按项目分组(颜色+独立WIP)
- `Last Update`: 2026-05-03

- `Project`: PRJ-20250416-001（todo-list）

### P-20260503-026: TodoList V18 — 标签管理增强 + 甘特图资源视图

- `Proposal ID`: `P-20260503-026`
- `Title`: TodoList V18 — 标签管理增强 + 甘特图资源视图
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V18 Iteration
- `Acceptance`: accepted
- `Notes`: 标签组CRUD+颜色+统计(N)+批量重命名(3种模式) + 甘特图资源视图(按项目分组+项目颜色)
- `Last Update`: 2026-05-03

- `Project`: PRJ-20250416-001（todo-list）

### P-20260503-025: TodoList V17 — 标签管理增强 + 项目分组

- `Proposal ID`: `P-20260503-025`
- `Title`: TodoList V17 — 标签管理增强 + 项目分组
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V17 Iteration
- `Acceptance`: accepted
- `Notes`: 项目分组ProjectSidebar(嵌套树形+颜色)+标签颜色8色预设+多选过滤
- `Last Update`: 2026-05-03

- `Project`: PRJ-20250416-001（todo-list）

### P-20260503-024: TodoList V16 — 定时自动备份到 Gist + 一键恢复

- `Proposal ID`: `P-20260503-024`
- `Title`: TodoList V16 — 定时自动备份到 Gist + 一键恢复
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V16 Iteration
- `Acceptance`: accepted
- `Notes`: 自动备份开关+间隔配置+备份历史列表 + 一键恢复预览确认
- `Last Update`: 2026-05-03

- `Project`: PRJ-20250416-001（todo-list）

### P-20260503-022: TodoList V14 — 看板WIP优化 + 数据导入增强

- `Proposal ID`: `P-20260503-022`
- `Title`: TodoList V14 — 看板WIP优化 + 数据导入增强
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V14 Iteration
- `Acceptance`: accepted
- `Notes`: 泳道独立WIP限制+看板设置弹窗+逾期高亮角标 + Todoist/Notion/CSV智能导入
- `Last Update`: 2026-05-03

- `Project`: PRJ-20250416-001（todo-list）
---

### P-20260503-021: TodoList V13 — 仪表板首页 + 泳道甘特图

- `Proposal ID`: `P-20260503-021`
- `Title`: TodoList V13 — 仪表板首页 + 泳道甘特图
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V13 Iteration
- `Acceptance`: accepted
- `Notes`: 仪表板首页(KPI卡片+今日到期+四象限分布) + 甘特图泳道分组(按状态/优先级)
- `Last Update`: 2026-05-03

- `Project`: PRJ-20250416-001（todo-list）
---

### P-20260503-020: TodoList V12 — 任务评分 + Gist 多设备同步

- `Proposal ID`: `P-20260503-020`
- `Title`: TodoList V12 — 任务评分 + Gist 多设备同步
- `Owner`: 小墨
- `Project`: PRJ-20250416-001（todo-list）
- `PRD Path`: `workspace-dev/proposals/todo-list/docs/prd.v1.md`
- `Technical Solution`: `workspace-dev/proposals/todo-list/docs/technical-solution.v1.md`
- `Stage`: V12 Iteration
- `Current Status`: approved_for_dev
- `Acceptance`: pending
- `PRD Confirmation`: timeout-approved
- `PRD Confirmation Countdown ID`: P-20260503-020-prd-confirm (已触发)
- `Last Update`: 2026-05-03
- `Notes`: 功能1:重要性×紧急度评分+四象限徽章; 功能2:GitHub Gist多设备同步; PRD超时确认通过

---

### P-20260502-019: TodoList V11 — 甘特图 + 循环提醒

- `Proposal ID`: `P-20260502-019`
- `Title`: TodoList V11 — 甘特图 + 循环提醒
- `Owner`: 小墨
- `Current Status`: delivered
- `Stage`: V11 Iteration
- `Acceptance`: accepted
- `Notes`: 甘特图时间线视图 + 循环任务自动生成下一周期
- `Last Update`: 2026-05-02

- `Project`: PRJ-20250416-001（todo-list）
---

### P-20260508-004: DBG卡牌游戏 V33 — 核心循环补全

- `Proposal ID`: `P-20260508-004`
- `Title`: DBG卡牌游戏 V33 — 核心循环补全
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `Stage`: V33 Iteration
- `Current Status`: delivered
- `Acceptance`: 小墨于2026-05-08自行验收通过
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Dev Commit`: 4743bea
- `Last Update`: 2026-05-08
- `Notes`: 卡组构建(奖励选卡)+arch-4(流派状态展示)+多章节递进(3章×3战斗+Boss)+敌人意图丰富化(multi_attack/buff_stack/defend_revenge/aoe)+arch-3端到端验证+同名牌组3张限制；文件10504行
---

### P-20260508-005: DBG卡牌游戏 V34 — 卡牌池扩充 + 遗物系统完善

- `Proposal ID`: `P-20260508-005`
- `Title`: DBG卡牌游戏 V34 — 卡牌池扩充 + 遗物系统完善
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `Stage`: V34 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Acceptance`: pending
- `Last Update`: 2026-05-08
- `Notes`: 奖励卡池10张→30张(攻击10+技能10+诅咒5+命运5)+流派配套卡+遗物系统完善(14种遗物)+章节结束遗物获取+遗物UI显示

---

### P-20260503-020: DBG卡牌游戏 V38 — 新手教程 + 卡牌使用率追踪

- `Proposal ID`: `P-20260503-020`
- `Title`: DBG卡牌游戏 V38 — 新手教程 + 卡牌使用率追踪
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `Stage`: V38 Iteration
- `Current Status`: accepted
- `Dev Commit`: ef1f5b0
- `Acceptance`: 小墨于2026-05-03验收通过（gameState.tutorial + statistics.cardUsageByType 确认存在）
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-03
- `Notes`: 一次性新手教程(战斗基础/卡组构建/遗物宠物三阶段)+卡牌使用率追踪(按攻击/防御/技能/力量/诅咒类型统计)+统计面板新增卡牌使用统计页面

---

### P-20260503-021: DBG卡牌游戏 V39 — Combo系统 + BossRush + 宠物技能树

- `Proposal ID`: `P-20260503-021`
- `Title`: DBG卡牌游戏 V39 — Combo系统 + BossRush + 宠物技能树
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `Stage`: V39 Iteration
- `Current Status`: approved_for_dev
- `PRD Confirmation`: confirmed
- `Acceptance`: pending
- `Last Update`: 2026-05-03
- `Notes`: Combo系统(同回合/连锁卡牌组合触发额外效果)+BossRush(连续挑战所有章节Boss)+宠物技能树(被动→可主动释放技能)

---

### P-20260508-004: PvZ 视觉增强 (A+B+C)

- `Proposal ID`: `P-20260508-004`
- `Title`: PvZ 视觉增强 (A+B+C) — WalkingAnimator启用 + 子弹命中粒子 + 植物受伤抖动
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（Plants vs Zombies）
- `Stage`: Visual Iteration
- `Current Status`: delivered
- `PRD Path`: proposals/workspace-pm/proposals/P-20260508-004-prd.md
- `PRD Confirmation`: confirmed
- `Acceptance`: accepted
- `Last Update`: 2026-05-08
- `Notes`: A=行走动画(手臂摆动+身体上下); B=子弹命中冲击波粒子; C=植物被啃左右抖动0.3s

---

### P-20260508-005: PvZ Visual Enhancements (D+E)

- `Proposal ID`: `P-20260508-005`
- `Title`: PvZ 视觉增强 (D+E) — 屏幕震动 + 僵尸啃咬特效
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（Plants vs Zombies）
- `Stage`: Visual Iteration
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-09
- `Notes`: D=屏幕震动(爆炸时shake); E=僵尸啃咬特效(碎片粒子); V3 commit 72596f6, exe 33MB

---

### P-20260508-006: PvZ 新植物/僵尸类型 (B1+B2+B3)

- `Proposal ID`: `P-20260508-006`
- `Title`: PvZ 新植物/僵尸 — PotatoMine土豆雷 + Torchwood火炬树桩 + Pole-vaulting Zombie撑杆跳僵尸
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（Plants vs Zombies）
- `Stage`: Content Expansion
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-09
- `Notes`: B1=PotatoMine(25sun,5s就绪,秒杀); B2=Torchwood(子弹变火焰×2伤害); B3=PoleVaultZombie(杆跳过植物后加速); commit 2a69a1d

---

### P-20260509-008: PvZ P2 植物僵尸全暴露 (E)

- `Proposal ID`: `P-20260509-008`
- `Title`: PvZ P2 植物/僵尸全暴露 + 卡牌翻页 — Squash/WinterMelon/IceShroom/HypnoShroom/ScaredyShroom + Football/Newspaper/Miner/Ladder
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（Plants vs Zombies）
- `Stage`: Content Expansion
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-09
- `Notes`: 卡牌栏扩展到13个植物，翻页箭头像标，左右翻页；commit cd80a20

---

### P-20260509-009: PvZ Endless Mode 计分榜 (F)

- `Proposal ID`: `P-20260509-009`
- `Title`: PvZ Endless Mode 计分榜 — 本地 JSON 存储 + Game Over 界面显示 + 排行榜 + 破纪录提示
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（Plants vs Zombies）
- `Stage`: Endless Mode
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-09
- `Notes`: LeaderboardManager 管理 ~/.pvz_endless_scores.json，Game Over 显示 Waves/Kills/Plants/Time+NEW RECORD，X按钮关闭排行榜；commit 387765c

---

### P-20260509-010: PvZ 僵尸专属机制 (G)

- `Proposal ID`: `P-20260509-010`
- `Title`: PvZ 僵尸专属机制 — Newspaper愤怒变身纸片特效 + Football头盔HP分阶段视觉 + Ladder架梯逻辑
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（Plants vs Zombies）
- `Stage`: Zombie Special Mechanics
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-09
- `Notes`: Newspaper被击毁报纸时触发NewspaperShredEffect纸片飞舞+咆哮音效；Football helmet HP 200独立计算，50%HP以下出现裂纹；Ladder逻辑已存在(架梯后plant.laddered=True减速啃咬)；take_damage改为返回(dead, shred)元组；commit 5bbbafe

---

### P-20260509-011: PvZ 新植物 H（Zapricot / Cattail / Gloom Shroom）

- `Proposal ID`: `P-20260509-011`
- `Title`: PvZ 新植物 H — Zapricot 电弧群攻 / Cattail 全屏跟踪 / Gloom Shroom 毒雾
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（Plants vs Zombies）
- `Stage`: New Plants H
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-09
- `Notes`: Zapricot 150阳光3x3范围电弧攻击；Cattail 225阳光全屏锁定最右侧僵尸必定命中；Gloom Shroom 150阳光毒雾爆炸单次使用，中毒DoT每0.5秒10伤害持续2秒；commit 8332563

---

### P-20260509-012: PvZ 成就系统 UI + 统计面板 (I)

- `Proposal ID`: `P-20260509-012`
- `Title`: PvZ 成就系统 UI + 统计面板 — AchievementPanel + StatsPanel + StatsManager
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（Plants vs Zombies）
- `Stage`: Achievement UI + Stats Panel
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-09
- `Notes`: AchievementPanel 2列网格+金色解锁/灰色未解锁+时间戳+滚动支持；StatsPanel显示游戏时长/僵尸击杀/植物种植等；StatsManager单例持久化到~/.hermes/prj-plants-vs-zombies/stats.json；主菜单A/J打开成就S打开统计，ESC关闭；commit a732f90

---

### P-20260509-013: PvZ 花园/Zen 模式完整 UI (M)

- `Proposal ID`: `P-20260509-013`
- `Title`: PvZ 花园/Zen 模式完整 UI — Marigold / Gold Magnet / Plant Food / Garden Gnome / 存档
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（Plants vs Zombies）
- `Stage`: Zen Garden Complete UI
- `Current Status`: delivered
- `Acceptance`: accepted
- `Last Update`: 2026-05-09
- `Notes`: Marigold产30阳光/tick（普通15）；Gold Magnet吸引半径150px阳光200px/s；Plant Food点击已放置植物扣50阳光产100阳光+金尘爆发；Garden Gnome浇水10次后装饰性出现；分页植物选择(8/页+左右箭头)；背景音乐(zen 60BPM五声音阶)；~/.pvz_garden.json自动保存/加载；commit 83b527d
---

### P-20260505-1006: DBG卡牌游戏 V52 — 卡牌等级+星级双维度升级系统

- `Proposal ID`: `P-20260505-1006`
- `Title`: DBG卡牌游戏 V52 — 卡牌等级+星级双维度升级系统
- `Owner`: 小墨
- `Project`: PRJ-20260421-001（DBG卡牌游戏）
- `Current Status`: delivered
- `Acceptance`: accepted
- `PRD Path`: proposals/workspace-pm/proposals/P-20260505-1006-prd.md
- `Stage`: V52 Iteration
- `Dev Commit`: 059551e
- `Deployed`: https://yeluo45.github.io/card-game-prototype/
- `GitHub Repo`: https://github.com/YeLuo45/card-game-prototype
- `Last Update`: 2026-05-05
- `Notes`: 卡牌等级升级(Lv1-Lv5倍率：1.15/1.30/1.50/1.75x)+星级升级(1-3星解锁效果)；⚡强化按钮入口；等级费用(2/3/5/8张同名卡)；星级费用(3/5张同名卡)；UI显示星级符号(★☆)和等级(Lv.N)；边框颜色按等级变化；升级数据持久化到localStorage