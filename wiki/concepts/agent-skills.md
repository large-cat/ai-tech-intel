# Agent Skills

- **类型**: 概念 / 开源项目 / Agent工程规范
- **提出者**: Addy Osmani (Google Chrome DevTools总监, AngularJS联创)
- **创建时间**: 2026-02-16
- **最后更新**: 2026-05-12

## 一句话定义

**Agent Skills** 是一套将Google二十年工程实践封装成AI可执行技能模块的开源规范，解决AI编程工具"走最短路径、跳过工程纪律"的痛点。

---

## 背景问题

AI编程助手（Claude Code, Cursor, Codex等）能写出功能正确的代码，但在工程层面是"野路子"出身：
- ❌ 不写测试
- ❌ 不做代码审查
- ❌ 不考虑向后兼容
- ❌ 不遵循提交规范
- ❌ 不做安全审计

**根本原因**: AI的目标是"让用户满意"，不是"让代码能上生产"。

---

## 🧬 技术原理深度版

### 为什么需要Agent Skills？

AI编程助手的核心问题是**目标函数错位**：
- AI优化的是"用户即时满意度"（单次对话评分）
- 工程需要的是"长期系统健康度"（可维护性、安全性、可测试性）
- 结果：AI写出"能跑但不敢上生产"的代码

Agent Skills通过**结构化指令注入**修正这个目标函数——把"工程纪律"编码成AI必须遵循的工作流。

### 核心洞察：LLM的"短视"问题

LLM的上下文窗口虽大，但在长任务中表现出**时间折扣**（Temporal Discounting）：
- 前面的决策在后续步骤中被遗忘或覆盖
- 看不到全局架构约束（"这里加个字段"破坏了另一处接口）
- Agent Skills本质是给LLM装上**外部记忆 + 检查清单**（Checklist），防止遗忘

---

## 🔑 SKILL.md 文件规范详解

### 文件结构（OpenClaw AgentSkills规范）

每个 `SKILL.md` 遵循严格的元数据区块 + 指令区块结构：

```yaml
---
# 元数据区块（YAML Front Matter）
name: code-review              # 技能标识符（kebab-case）
description: 代码审查技能     # 一句话描述
version: 1.0.0               # 语义化版本
author: addyosmani           # 作者
tags: [code-quality, security]  # 分类标签
---

# 指令区块（Markdown正文）
## 触发条件
- 当用户要求"审查代码"或"code review"时激活

## 工作流
1. **静态分析**：运行 ESLint/Prettier/类型检查
2. **安全扫描**：检查 SQL注入/XSS/依赖漏洞
3. **架构审查**：验证是否符合项目既定模式
4. **输出格式**：使用标准Code Review模板

## 禁止事项
- ❌ 不要只指出问题而不给修复建议
- ❌ 不要审查测试文件中的测试逻辑（除非明显错误）
- ❌ 不要修改第三方库代码

## 输出模板
```markdown
### 🔴 Critical
- {文件}:{行号} — {问题} → {修复建议}

### 🟡 Warning
...
```
```

### 关键设计原则

| 原则 | 说明 | 反例 |
|------|------|------|
| **明确激活条件** | 什么场景下触发，避免误激活 | "代码相关任务"（太模糊） |
| **确定性输出** | 结构化模板，减少AI自由发挥 | "请给一些建议"（无格式） |
| **否定指令** | 明确禁止的行为清单 | 防止AI"自作聪明" |
| **版本控制** | 技能本身可迭代 | v1.0 → v1.1 新增安全检查项 |
| **原子性** | 一个技能只做一件事 | "代码审查+重构+测试"（过于庞大） |

---

## 🏗️ MCP协议技术实现（Model Context Protocol）

> **来源**：`arxiv.org/pdf/2604.05969`（MCP: JSON-RPC 2.0 Background）

Agent Skills 的底层通信协议是 **MCP（Model Context Protocol）**，由 Anthropic 设计并开源，采用 **JSON-RPC 2.0** 作为传输层规范。

### 协议架构：三层栈

```
┌─────────────────────────────────────┐
│  Application Layer: Agent Skills     │  ← SKILL.md 语义层
├─────────────────────────────────────┤
│  Protocol Layer: MCP Primitives    │  ← Tools / Resources / Prompts
├─────────────────────────────────────┤
│  Transport Layer: JSON-RPC 2.0     │  ← stdio / SSE / HTTP
└─────────────────────────────────────┘
```

### JSON-RPC 2.0 消息格式

所有MCP通信基于JSON-RPC 2.0标准请求/响应：

**请求消息**：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "code_review",
    "arguments": {"file_path": "src/main.js", "strictness": "high"}
  }
}
```

**响应消息**：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [{"type": "text", "text": "### 🔴 Critical..."}]
  }
}
```

**错误消息**：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {"code": -32602, "message": "Invalid params", "data": {"field": "strictness"}}
}
```

标准错误码（继承JSON-RPC 2.0）：
| 错误码 | 含义 | MCP场景 |
|--------|------|---------|
| `-32700` | Parse Error | JSON格式错误 |
| `-32600` | Invalid Request | 缺少jsonrpc/version字段 |
| `-32601` | Method Not Found | 调用了未注册的Tool |
| `-32602` | Invalid Params | 参数类型/必填校验失败 |
| `-32603` | Internal Error | Tool执行异常崩溃 |
| `-32000` | MCP Server Error | 服务端自定义错误 |

### MCP Primitives：三大核心原语

#### 1. Tools（工具）—— 可执行函数

Tools 是 Agent 可调用的**确定性函数**，签名必须显式声明：

```json
{
  "name": "run_linter",
  "description": "对指定文件运行静态分析",
  "inputSchema": {
    "type": "object",
    "properties": {
      "file_path": {"type": "string", "description": "相对路径"},
      "linter_type": {"type": "string", "enum": ["eslint", "prettier", "tsc"]}
    },
    "required": ["file_path", "linter_type"]
  }
}
```

Tool 执行四阶段生命周期：
```
Client Request → Server Validate(inputSchema) → Execute → Client Receive(result)
```

关键约束：
- **Schema 严格校验**：输入必须匹配 `inputSchema`（JSON Schema Draft 7）
- **超时控制**：默认 30s，可配置
- **幂等性**：同一输入应产生相同输出（推荐但非强制）

#### 2. Resources（资源）—— 只读上下文

Resources 提供**结构化只读数据**，不执行副作用：

```json
{
  "uri": "file:///project/src/main.js",
  "mimeType": "text/javascript",
  "text": "// 文件内容...",
  "metadata": {"size": 2048, "last_modified": "2026-05-01T12:00:00Z"}
}
```

Resource vs Tool 的本质区别：
| 维度 | Tool | Resource |
|------|------|----------|
| 副作用 | ✅ 可执行任意操作 | ❌ 只读 |
| 输入 | 需参数（inputSchema） | 仅需URI |
| 返回 | 结构化结果 | 原始内容 + 元数据 |
| 缓存 | 不可缓存 | 可订阅变更（Resource Updated通知） |
| 典型用例 | 运行测试、部署、发送消息 | 读取文件、查询数据库、获取配置 |

#### 3. Prompts（提示模板）—— 预定义指令

Prompts 是**可复用的对话模板**，支持插值：

```json
{
  "name": "code_review_prompt",
  "description": "结构化代码审查模板",
  "arguments": [
    {"name": "file_path", "required": true},
    {"name": "language", "required": false, "default": "typescript"}
  ],
  "messages": [
    {
      "role": "user",
      "content": {
        "type": "text",
        "text": "请审查以下 {{language}} 代码文件：{{file_path}}"
      }
    }
  ]
}
```

### MCP连接生命周期（4阶段）

```
[1] 初始化 (Initialize)
    └─→ Client 发送 initialize 请求（protocolVersion, capabilities, clientInfo）
    └─→ Server 返回支持的能力集
    └─→ 握手完成 → 进入 Operation 阶段

[2] 运行 (Operation)
    └─→ 工具调用、资源读取、提示填充、采样请求循环发生
    └─→ 支持并发请求（id字段区分）

[3] 通知 (Notification)
    └─→ 单向消息（无id字段），如 progress/cancel/resource_updated
    └─→ 客户端可发 `notifications/cancel` 中止长时操作

[4] 关闭 (Close)
    └─→ 优雅关闭：发送 `notifications/closed`
    └─→ 异常断开：Transport层检测连接丢失
```

### Transport层实现

| 传输方式 | 方向 | 适用场景 | 协议细节 |
|----------|------|----------|----------|
| **stdio** | Client→Server单向 | 本地子进程（最常见） | 子进程标准输入输出，JSON-RPC消息以换行符分隔 |
| **SSE** | Server→Client单向 | 远程HTTP推送 | `Content-Type: text/event-stream`，JSON-RPC消息封装在SSE data字段 |
| **HTTP** | 请求/响应双向 | RESTful集成 | POST请求体携带JSON-RPC消息，SSE流回传响应 |

---

## 🏗️ ACP/A2A 协议对比（多Agent通信）

当单Agent不够用时，需要多Agent协作协议。

### ACP（Anthropic Agent Communication Protocol）

Anthropic提出的**轻量级Agent间通信标准**：

```json
{
  "message_type": "task_request",
  "from_agent": "planner",
  "to_agent": "coder",
  "task": {
    "id": "task-001",
    "description": "实现用户认证中间件",
    "dependencies": [],
    "deliverables": ["src/auth.ts", "tests/auth.test.ts"]
  },
  "context": {
    "parent_task": "build-api-server",
    "constraints": ["使用JWT", "支持刷新令牌"]
  }
}
```

特点：
- **无中心协调器**：Agent间直接通信
- **任务粒度高**：支持子任务拆分、依赖声明
- **上下文传递**：parent_task 保证全局一致性

### A2A（Google Agent-to-Agent Protocol）

Google在2026年4月发布的**结构化Agent互操作协议**（比ACP更正式）：

核心概念：
| 概念 | 说明 |
|------|------|
| **Agent Card** | 每个Agent发布能力清单（类似OpenAPI Spec） |
| **Task** | 工作单元，有生命周期（submitted → working → input_required → completed/failed） |
| **Artifact** | 任务产出物（文件、数据、结构化结果） |
| **Message** | Agent间对话流，支持多轮协商 |

Agent Card示例：
```json
{
  "agent_name": "frontend_builder",
  "version": "1.0.0",
  "capabilities": ["react", "typescript", "css_modules"],
  "input_schema": {"project_type": "string", "design_url": "string?"},
  "output_schema": {"deliverables": ["file_path"], "build_commands": ["string"]},
  "endpoint": "https://agents.example.com/frontend/invoke"
}
```

A2A vs MCP 的关系：
- **MCP**：Agent ↔ 工具/资源（"我有什么能力"）
- **A2A**：Agent ↔ Agent（"你能帮我做什么"）
- **互补**：MCP解决"工具调用"，A2A解决"任务协作"

### 三协议定位对比

| 协议 | 层级 | 通信对象 | 核心问题 | 状态（2026） |
|------|------|----------|----------|-------------|
| **MCP** | 工具层 | Agent ↔ Tool/Resource | "我能调用什么功能？" | **已开源**，生态成熟 |
| **ACP** | 任务层 | Agent ↔ Agent | "谁能帮我做这个子任务？" | Anthropic内部使用 |
| **A2A** | 协作层 | Agent ↔ Agent | "多Agent如何协同完成复杂任务？" | Google发布，待验证 |

---

## 🚀 生态与工具链

### OpenClaw AgentSkills（本机运行）

OpenClaw是第一个原生支持Agent Skills的运行时：
- **运行时选择**：用户对话 → 匹配SKILL.md → 加载上下文 → AI按工作流执行
- **本地工具链**：通过MCP stdio传输层调用本地工具（git, npm, docker, curl）
- **文件系统代理**：AI通过MCP Resources安全读取/写入文件（URI白名单控制）

### Anthropic MCP SDK

官方SDK支持多语言：
- **TypeScript SDK**：`@anthropic-ai/mcp`，提供 `Client` 和 `Server` 类
- **Python SDK**：`mcp-python`，异步 asyncio 架构
- **核心API**：
  - `client.list_tools()` → 返回可用Tool清单
  - `client.call_tool(name, arguments)` → 执行Tool
  - `client.read_resource(uri)` → 读取Resource
  - `client.get_prompt(name, arguments)` → 获取Prompt模板

### Stripe Minions Blueprint（确定性×智能体混合架构）

Stripe在2026年3月发布的**生产级Agent架构**（来源：`sources/modern-harness-blueprint-2026.md`）：

```
┌─────────────────────────────────────────────────┐
│  Minion（确定性Agent）                           │
│  ├── 400+ MCP Tools（测试、部署、监控、审计）      │
│  ├── 200+ 服务并行执行                            │
│  ├── 循环：计划 → 执行 → 验证 → 失败则重试        │
│  └── 总运行时间：90分钟（完全自主，无人值守）       │
└─────────────────────────────────────────────────┘
```

关键实现细节：
- **Harness约束**：所有MCP Tool调用必须有Schema约束 + 超时控制
- **验证器（Verifier）**：独立LLM实例审查Minion输出，不通过则回滚
- **沙箱隔离**：每个Minion在独立Docker容器中运行，文件系统隔离
- **审计日志**：每次Tool调用记录输入/输出/耗时，用于事后分析

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| GitHub Stars | 29K+ (2026-05-09) | GitHub仓库实时数据 |
| 日增Stars | ~629/天 | GitHub统计估算 [来源：github.com/addyosmani/agent-skills] |
| MCP协议版本 | 2025-03-26（JSON-RPC 2.0） | Anthropic官方 |
| OpenClaw AgentSkills | 30+内置技能 | OpenClaw仓库 |
| Minions Blueprint工具数 | 400+ MCP Tools | Stripe Engineering Blog |
| Minions并行服务数 | 200+ | Stripe Engineering Blog |
| Minion单次运行时长 | 90分钟（无人值守） | Stripe Engineering Blog |
| A2A协议发布 | 2026-04 | Google Cloud Blog |
| Agent Card标准 | 基于JSON Schema | Google A2A Spec |

---

## 🔗 相关页面
- [concepts/harness-methodology.md](harness-methodology.md) — Harness Engineering（确定性约束）
- [entities/addy-osmani.md](../entities/addy-osmani.md) — 项目作者
- [entities/anthropic.md](../entities/anthropic.md) — MCP/ACP协议设计者
- [entities/google-deepmind.md](../entities/google-deepmind.md) — A2A协议发布者
- [entities/stripe.md](../entities/stripe.md) — Minions Blueprint
- [entities/openclaw.md](../entities/openclaw.md) — OpenClaw运行时
- [GitHub 仓库](https://github.com/addyosmani/agent-skills) — 实时数据

---

*最后更新：2026-05-12*  
*信息来源：Anthropic MCP Spec (arxiv.org/pdf/2604.05969), Google A2A Protocol, Stripe Engineering Blog, OpenClaw AgentSkills规范, Addy Osmani博客*