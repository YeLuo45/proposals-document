# Proposals Directory

本目录用于管理跨 Agent 的需求闭环。

## 目录结构

```
proposals/
├── proposal-index.md          # 提案索引
├── README.md                  # 本文件
└── templates/                 # 模板目录
    ├── request-intake-template.md      # 提案登记模板
    ├── proposal-status-template.md     # 状态跟踪模板
    └── acceptance-checklist-template.md # 验收清单模板
```

## 提案ID格式

`P-YYYYMMDD-XXX` — 按日顺序编号，零填充

## 提案状态

```
intake → clarifying → prd_pending_confirmation → approved_for_dev
→ in_dev → in_acceptance → accepted → delivered
                                                    ↓
                                            needs_revision → in_dev
```

## 工作流程

1. 登记提案（intake）
2. 需求澄清（clarifying）
3. PRD 确认（prd_pending_confirmation）
4. 技术方案（approved_for_dev）
5. 开发（in_dev）
6. 验收（in_acceptance）
7. 交付（delivered）

## 相关目录

- PM 产物：`~/.hermes/proposals/workspace-pm/proposals`
- Dev 产物：`~/.hermes/proposals/workspace-dev/proposals`

---

*由小墨（main）Agent 管理*
