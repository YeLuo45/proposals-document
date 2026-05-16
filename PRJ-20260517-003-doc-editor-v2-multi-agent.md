# PRD: doc-editor V2 — 多 Agent 文档协作系统

## 1. 概述

### 项目信息
- **Project**: doc-editor V2 — 多 Agent 文档协作系统
- **参考架构**: trading-agents-design (13 Agent 协作) + nanobot-design (MessageBus + AgentLoop)
- **提案ID**: P-20260517-002
- **迭代模式**: 无人值守（自动确认、自动验收、自动迭代）

### 核心目标
将文档编辑器从单人工具升级为多角色 AI 协作平台，支持自动化的文档编辑→审查→发布全流程。

---

## 2. 架构概览

```
┌─────────────────────────────────────────────────────────────────┐
│                        doc-editor Multi-Agent System              │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────┐ │
│  │ Editor Agent│  │Reviewer Agent│  │Researcher   │  │ Manager │ │
│  │ (内容编辑)   │  │(质量审查)   │  │  Agent      │  │  Agent  │ │
│  │             │  │             │  │(信息检索)   │  │(协调调度)│ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └────┬────┘ │
│         │               │               │               │       │
│         └───────────────┼───────────────┼───────────────┘       │
│                         ↓               ↓                       │
│              ┌─────────────────────┐                           │
│              │     MessageBus      │  (异步消息路由)            │
│              │  (nanobot-style)    │                           │
│              └──────────┬──────────┘                           │
│                         ↓                                       │
│              ┌─────────────────────┐                           │
│              │   AgentLoop         │  (会话管理+上下文构建)      │
│              │  + AgentRunner     │                           │
│              └──────────┬──────────┘                           │
│                         ↓                                       │
│              ┌─────────────────────┐                           │
│              │   Tool Registry     │  (插件式工具系统)          │
│              └─────────────────────┘                           │
├─────────────────────────────────────────────────────────────────┤
│                    IndexedDB + ContextPool                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Agent 定义

### 3.1 Editor Agent
- **职责**: 文档内容编辑、排版优化、格式调整
- **工具**: read_file, write_file, format_doc, translate
- **触发**: 用户编辑请求 / Manager 分派

### 3.2 Reviewer Agent
- **职责**: 语法检查、风格一致性、内容逻辑审查
- **工具**: grammar_check, style_check, consistency_check
- **输出**: 审查报告 + 修改建议

### 3.3 Researcher Agent
- **职责**: 信息收集、引用查找、资料整理
- **工具**: web_search, web_fetch, cite_reference
- **输出**: 相关资料摘要

### 3.4 Manager Agent
- **职责**: 协调多 Agent 工作流、状态管理、任务调度
- **核心**: 状态机驱动、DAG 任务编排
- **工具**: orchestrator, state_machine, retry_handler

---

## 4. 消息协议

```typescript
interface AgentMessage {
  id: string;              // 消息唯一ID
  sender: AgentType;       // 发送者
  receiver: AgentType | 'broadcast';  // 接收者
  type: MessageType;        // REQUEST | RESPONSE | ERROR | APPROVAL
  payload: any;            // 消息内容
  timestamp: number;
  requiresApproval?: boolean;  // 是否需要人工确认
  conversationId?: string;     // 关联的会话ID
  parentId?: string;           // 父消息ID（线程）
}

enum AgentType {
  EDITOR = 'editor',
  REVIEWER = 'reviewer',
  RESEARCHER = 'researcher',
  MANAGER = 'manager'
}

enum MessageType {
  EDIT_REQUEST = 'EDIT_REQUEST',
  REVIEW_REQUEST = 'REVIEW_REQUEST',
  RESEARCH_REQUEST = 'RESEARCH_REQUEST',
  ORCHESTRATE = 'ORCHESTRATE',
  APPROVAL_REQUEST = 'APPROVAL_REQUEST',
  APPROVAL_RESPONSE = 'APPROVAL_RESPONSE',
  ERROR = 'ERROR'
}
```

---

## 5. 状态机

```
DRAFT → IN_REVIEW → REVISED → APPROVED → PUBLISHED
  ↓         ↓          ↓         ↓
  └─────────┴──────────┴─────────┴──→ REJECTED → DRAFT
                                         (需要修订)
```

### 状态转换规则
| 当前状态 | 事件 | 下一状态 | 触发者 |
|---------|------|---------|--------|
| DRAFT | 用户提交 | IN_REVIEW | Manager |
| IN_REVIEW | 审查完成 | REVISED | Reviewer |
| REVISED | 作者确认 | APPROVED | Manager |
| APPROVED | 发布请求 | PUBLISHED | Manager |
| * | 审查发现问题 | REJECTED | Reviewer |

---

## 6. 无人值守模式

### 6.1 自动确认
- `requiresApproval: false` 的消息自动放行
- 审查通过（评分 ≥ 0.8）自动进入下一阶段
- 失败重试 3 次，3 次失败后降级处理

### 6.2 自动验收
- Manager Agent 自动执行验收检查
- 检查项：内容完整性、格式规范性、无错误信息
- 验收通过自动推送 GitHub

### 6.3 自动迭代
- 检测到 REJECTED 状态，自动返回 DRAFT
- 自动通知相关 Agent 进行修订
- 迭代次数上限：10 次，超限告警

---

## 7. 工具系统 (Tool Registry)

### 7.1 内置工具

| 工具 | 功能 | Agent |
|------|------|-------|
| `read_file` | 读取文档内容 | Editor/Researcher |
| `write_file` | 写入文档内容 | Editor |
| `format_doc` | 格式化文档 | Editor |
| `grammar_check` | 语法检查 | Reviewer |
| `style_check` | 风格检查 | Reviewer |
| `web_search` | 网络搜索 | Researcher |
| `web_fetch` | 获取网页内容 | Researcher |
| `cite_reference` | 引用生成 | Researcher |
| `orchestrator` | 任务编排 | Manager |
| `state_machine` | 状态管理 | Manager |

### 7.2 工具注册机制
```typescript
class ToolRegistry {
  private tools: Map<string, BaseTool>;

  discover_tools() {
    // 自动扫描 tools/ 目录
    // 加载内置工具 + 自定义工具
  }

  register(tool: BaseTool) { /* ... */ }
  execute(name: string, args: dict): Promise<string>
  get_definitions(): ToolDefinition[]
}
```

---

## 8. 技术方案

### 8.1 目录结构
```
src/
├── agents/
│   ├── types.ts           # Agent 类型定义
│   ├── messageBus.ts      # MessageBus 实现
│   ├── agentLoop.ts       # AgentLoop 核心
│   ├── agentRunner.ts     # AgentRunner 执行器
│   ├── context.ts         # Context 构建
│   ├── registry.ts        # Agent 注册表
│   ├── editor/
│   │   └── index.ts       # Editor Agent
│   ├── reviewer/
│   │   └── index.ts       # Reviewer Agent
│   ├── researcher/
│   │   └── index.ts       # Researcher Agent
│   └── manager/
│       └── index.ts       # Manager Agent（状态机驱动）
├── tools/
│   ├── base.ts            # BaseTool 抽象类
│   ├── registry.ts        # ToolRegistry
│   ├── filesystem.ts      # read_file/write_file
│   ├── formatter.ts       # format_doc
│   ├── grammar.ts         # grammar_check
│   ├── search.ts          # web_search/web_fetch
│   └── index.ts           # 工具导出
├── store/
│   ├── contextPool.ts     # 共享状态存储
│   └── conversationStore.ts
├── i18n.ts
└── App.tsx
```

### 8.2 依赖更新
```json
{
  "dependencies": {
    "@tiptap/react": "^2.2.4",
    "uuid": "^9.0.1"
  },
  "devDependencies": {
    "@types/uuid": "^9.0.8"
  }
}
```

### 8.3 MessageBus 实现（nanobot-style async queue）
```typescript
class MessageBus {
  private queue: AsyncQueue<AgentMessage>;
  private subscribers: Map<AgentType, Handler[]>;

  async publish(message: AgentMessage): Promise<void>
  subscribe(agent: AgentType, handler: Handler): void
  unsubscribe(agent: AgentType, handler: Handler): void
}
```

---

## 9. 无人值守工作流

```
用户输入编辑请求
       ↓
Manager Agent 接收
       ↓
消息入 MessageBus
       ↓
并行分派给 Editor/Reviewer/Researcher
       ↓
Editor 执行内容编辑
Reviewer 执行质量审查
Researcher 收集相关信息
       ↓
结果汇聚到 Manager
       ↓
[无人值守模式]
  ├─ 评分 ≥ 0.8 → 自动通过
  ├─ 评分 < 0.8 → 修订后重试（最多3次）
  └─ 重试失败 → 降级处理 + 告警
       ↓
自动构建 + 自动部署
       ↓
状态更新 PUBLISHED
```

---

## 10. 验收标准

- [ ] MessageBus 异步消息传递正常
- [ ] 4 个 Agent 角色正确注册和调度
- [ ] 状态机 DRAFT→PUBLISHED 全流程贯通
- [ ] 无人值守模式下自动通过率 ≥ 80%
- [ ] `npm run build` 通过，dist 生成
- [ ] GitHub Pages 部署成功
- [ ] 与现有文档管理功能（文件夹/标签/搜索）兼容

---

## 11. 迭代计划

| Phase | 内容 | 交付物 |
|-------|------|--------|
| Phase 1 | 核心框架：MessageBus + AgentLoop + AgentRegistry | 消息通信正常 |
| Phase 2 | Manager Agent：状态机 + DAG 编排 | 工作流驱动 |
| Phase 3 | Editor + Reviewer + Researcher Agent | 协作编辑 |
| Phase 4 | ToolRegistry + 内置工具 | 可扩展工具 |
| Phase 5 | 无人值守模式 + 自动部署 | 全自动化 |