# proposals-document

提案管理系统 — 提案文档与版本管理。

## 目录结构

```
proposals-document/
├── proposal-index.md          # 提案总索引
├── proposal-docs-index.md      # 提案文档索引（PRD + 技术方案）
├── proposals/                  # 原始提案文件
│   ├── P-YYYYMMDD-XXX.md
│   └── P-YYYYMMDD-XXX-tech-solution.md
├── templates/                  # 提案模板
│   ├── request-intake-template.md
│   ├── proposal-status-template.md
│   └── acceptance-checklist-template.md
└── project-docs/               # 各项目的版本化文档
    └── <project-slug>/
        └── docs/
            ├── index.md         # 项目文档索引
            ├── proposal.md      # 原始提案
            ├── prd.vN.md       # PRD（版本化）
            └── technical-solution.vN.md  # 技术方案（版本化）
```

## 文档管理规范

- PRD 和技术方案采用版本化管理（v1, v2, ...）
- 每个项目 `docs/index.md` 记录当前版本和历史版本
- `proposal-docs-index.md` 是全局文档索引

## 相关链接

- 提案管理系统：[YeLuo45/proposals-manager](https://github.com/YeLuo45/proposals-manager)
- 部署地址：https://yeluo45.github.io/proposals-manager/
