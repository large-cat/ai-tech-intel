# MCP Sampling Loop 技术深度解析

> 来源：[MCP Survey Paper (preprints.org)](https://www.preprints.org/manuscript/202504.0245/download/final_file) | [极客时间 MCP & A2A 前沿实战](https://time.geekbang.org/column/article/888095) | [阿里云 MCP 详解](https://developer.aliyun.com/article/1659874) | [JavaGuide MCP](https://javaguide.cn/ai/agent/mcp.html)  
> 关联概念：[[Model Context Protocol]], [[Agent Skills]], [[Human-in-the-loop]], [[12-Factor Agents]]  
> 日期：2026-05-15（综合多源分析）

---

## 什么是 Sampling Loop

MCP 的 **Sampling（采样）** 原语是 MCP 双向通信架构中最被低估、但最具 Agentic 潜力的机制。它允许 **Server 主动向 Client 发起请求**，要求 Client 端的 LLM 执行推理生成——本质上实现了"AI 调用 AI"的递归循环。

> 类比：如果 Tools 是模型调用外部世界的"输出接口"，Sampling 就是外部世界调用模型的"输入接口"。

---

## 协议级工作流程

### 四阶段结构化流程

```
1. Server Initiates Request
   └── 通过 sampling/createMessage 发送请求
   └── 包含：message context、model preferences（cost/latency/capabilities）、
       sampling parameters（temperature/token limits/stop sequences）

2. Client Review and Approval（Human-in-the-loop）
   └── 用户审核、调整或批准 proposed message
   └── 维持人类监督和安全性

3. Model Execution and Completion Generation
   └── Client 调用选定的 LLM 生成 completion
   └── 考虑 sampling parameters 控制响应变异性和特异性

4. Return and Handling of Completions
   └── 结构化响应返回 Server
   └── 包含：使用的模型名称、终止原因、输出内容（text/multimodal）
```

### JSON 请求/响应格式

**请求（Server → Client）**：
```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "当前目录下有哪些文件？"
        }
      }
    ],
    "systemPrompt": "你是一名文件系统助手。",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7,
    "stopSequences": ["\n\n"]
  }
}
```

**响应（Client → Server）**：
```json
{
  "model": "claude-3-sonnet-20240229",
  "stopReason": "endTurn",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "当前目录包含以下文件：\n1. README.md\n2. src/main.py\n3. config.yaml"
  }
}
```

---

## 为什么需要 Sampling

### 问题定义

传统 MCP 架构中，所有推理由 Client（AI 应用）发起，Server 被动响应。但存在一类场景：**Server 在执行任务过程中需要 LLM 的推理能力来完成子任务**。

**典型场景**：
- 代码分析 Server 需要 LLM 解释一段复杂代码的功能
- 数据处理 Server 需要 LLM 生成自然语言摘要
- 多 Agent 协作时，一个 Agent（作为 Server）需要另一个 Agent 的推理输出
- 构建自循环 Agent：Server 发现需要进一步推理时，Sampling 请求模型产出结果，继续后续操作

### 双向性的核心体现

MCP 协议 10 大功能场景中，**由 Server 主动发起**的请求只有三类：
1. `sampling/createMessage` — 请求 LLM 生成内容
2. `roots/list` — 请求工作根目录信息
3. `elicitation/create` — 请求用户输入或决策

Sampling 是其中唯一能调用 LLM 推理能力的服务端发起请求。

---

## Human-in-the-Loop 安全设计

### 为什么 Anthropic 强调谨慎使用

> "Anthropic 强调应谨慎使用这一机制，始终保持人类在环监督，以避免 AI 代理失控循环调用模型。"

**风险**：
- **递归失控**：Agent A 调用 Server，Server 通过 Sampling 调用 Agent B，Agent B 又触发 Server... 形成无限循环
- **成本黑洞**：每次 Sampling 都消耗 token，失控循环可能产生巨额费用
- **责任模糊**：谁为 Agent 的 Agent 的决策负责？

### 安全机制

1. **用户确认**：Client 必须允许用户 review/adjust/approve proposed message
2. **模型偏好协商**：Server 可以表达偏好（更智能/更快/更便宜），但最终决定权在 Client 和用户手中
3. **可选支持**：Sampling 并非所有 MCP Server 均支持，需依赖客户端实现
4. **上下文边界**：通过 `includeContext` 字段控制上下文范围（`none` | `thisServer` | `allServers`）

---

## 与 12-Factor Agents 的映射

MCP Sampling Loop 直接支撑 **12-Factor Agents** 的多个原则：

| 12-Factor 原则 | Sampling Loop 的支撑 |
|----------------|----------------------|
| **#5 Own your context window** | Sampling 明确控制 `includeContext`，Server 只能获取授权的上下文 |
| **#6 Own the interaction model** | Human-in-the-loop 强制用户保持控制权 |
| **#7 Own the contact surface area** | Server 不能直接接触 LLM，必须通过 Client 代理 |
| **#10 Instrument everything** | Sampling 请求和响应都是结构化 JSON，可完整追踪 |

---

## 与 Harness 方法论的关系

在 Harness（Agent 编排系统）框架中，Sampling Loop 对应以下组件：

- **Reasoning Sandwich**：Sampling 请求就是"让模型做推理"的层
- **LoopDetectionMiddleware**：必须检测 Sampling 触发的递归循环，防止失控
- **Trace Analyzer Skill**：所有 Sampling 调用必须进入可观测链路
- **MCP Integration**：Stripe Minions Blueprint 的 400+ MCP Server 中，Sampling 是高级 Server（如代码分析、数据处理）的标配能力

---

## 实际应用场景

### 场景1：智能代码审查 Agent

```
用户提交 PR → Agent 调用代码分析 MCP Server
                     ↓
              Server 发现复杂算法需要解释
                     ↓
              Server 发起 sampling/createMessage
                     ↓
              Client 展示请求给用户，用户批准
                     ↓
              LLM 生成算法解释
                     ↓
              Server 将解释整合进审查报告
                     ↓
              Agent 输出最终 PR 审查意见
```

### 场景2：多 Agent 协作（Research Agent + Writing Agent）

```
Research Agent（作为 Server）收集资料后
        ↓
发现需要生成一段总结性文字
        ↓
通过 Sampling 请求 Writing Agent（Client 端 LLM）
        ↓
Writing Agent 生成内容，经用户确认后返回
        ↓
Research Agent 整合进最终报告
```

### 场景3：Self-Healing 系统

```
监控 Server 检测到异常日志
        ↓
通过 Sampling 请求 LLM 诊断根因
        ↓
LLM 返回可能的根因分析
        ↓
Server 自动触发修复工具
        ↓
循环验证直到恢复正常
```

---

## 技术实现要点

### 客户端支持状态

| 客户端 | Sampling 支持 | 备注 |
|--------|--------------|------|
| Claude Desktop | ✅ 完整支持 | Anthropic 原生实现 |
| Cursor | ⚠️ 部分支持 | 通过插件扩展 |
| Continue.dev | ✅ 支持 | 开源实现 |
| 自建 Client | 需自行实现 | 参考 MCP SDK |

### 模型偏好协商

Server 可以在请求中表达偏好，但最终由 Client 决定：

```json
{
  "modelPreferences": {
    "hints": ["claude-3-opus", "gpt-4"],
    "costPriority": 0.3,
    "speedPriority": 0.7,
    "intelligencePriority": 0.5
  }
}
```

**优先级说明**：
- `costPriority`：成本敏感（适合批量处理）
- `speedPriority`：延迟敏感（适合实时交互）
- `intelligencePriority`：质量敏感（适合复杂推理）

---

## 与 A2A (Agent-to-Agent) 协议的对比

| 维度 | MCP Sampling | Google A2A |
|------|-------------|------------|
| **发起方** | Server → Client（单向） | Agent ↔ Agent（双向） |
| **安全模型** | Client 控制，用户确认 | 任务委托 + 能力发现 |
| **适用场景** | 工具级调用 | 服务级协作 |
| **生态成熟度** | 1万+ MCP Server | 早期，Google 主导 |
| **标准化程度** | JSON-RPC 2.0，严格 Schema | 基于 HTTP/JSON，较灵活 |

**互补关系**：MCP 解决"模型与工具的连接"，A2A 解决"Agent 与 Agent 的协作"。Sampling 是 MCP 向 Agent 级协作迈出的关键一步。

---

## 引用

- [A Survey of the Model Context Protocol (MCP)](https://www.preprints.org/manuscript/202504.0245/download/final_file) — 2025年4月预印本，含 Sampling 机制完整流程图
- [极客时间：人在环路——通过Sampling机制实现人机互动](https://time.geekbang.org/column/article/888095) — 中文深度讲解
- [阿里云 MCP 详解](https://developer.aliyun.com/article/1659874) — 含 Sampling 请求/响应 JSON 示例
- [JavaGuide MCP](https://javaguide.cn/ai/agent/mcp.html) — 2026年5月最新更新，含 Sampling 与其他原语的对比
- [MCP官方文档](https://modelcontextprotocol.io) — `sampling/createMessage` 规范
