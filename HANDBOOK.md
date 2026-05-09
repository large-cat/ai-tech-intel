# 🧭 AI Tech Intel 概念图谱

> **知识编译**视角的知识库导航。不是按文件或日期组织，而是按概念的层级、依赖和递进关系组织。
>
> 每条学习路径标注：⭐难度（1-5）、⏱️预计阅读时间、📋前置概念。

---

## 如何使用这本手册

**场景1：从零学习一个领域**
> 选一个分支，从"前置知识"开始，沿着箭头方向逐层深入。

**场景2：查一个具体概念**
> 在图谱中找到该概念，看它的前置（需要先懂什么）和后续（学完后可以深入什么）。

**场景3：快速了解全貌**
> 看根概念的一句话定义，不需要深入子概念。

---

## 图谱总览

```
                    ┌─────────────────────────────────────┐
                    │     🤖 AI 技术情报 知识总图            │
                    └──────────────┬────────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
   ┌────▼────┐              ┌──────▼──────┐           ┌──────▼──────┐
   │ 分支1   │              │   分支2     │           │   分支3     │
   │ AI Agent│              │ AI 硬件     │           │ 大模型      │
   │ 工程    │              │ 基础设施    │           │ 技术        │
   └────┬────┘              └──────┬──────┘           └──────┬──────┘
        │                          │                       │
   ┌────▼────┐              ┌──────▼──────┐           ┌──────▼──────┐
   │ 分支4   │              │   分支5     │           │   分支6     │
   │ 开源    │              │ 学习资源    │           │ 每日情报    │
   │ 生态    │              │ 与方法      │           │ 速递        │
   └─────────┘              └─────────────┘           └─────────────┘
```

---

# 分支1：AI Agent 工程

> 2026年最核心范式。Agent = Model + Harness，环境比模型更重要。

## 🔷 学习路径：从零到深入

### 第0层：前置知识（必须先懂）

| 概念 | 一句话 | ⭐ | ⏱️ | 页面 |
|------|--------|---|---|------|
| **RLHF** | 让模型对齐人类偏好的训练方法 | ⭐⭐ | 10min | [concepts/rlhf.md](concepts/rlhf.md) |
| **测试时计算** | 推理时"多想一会"，不只看模型大小 | ⭐⭐ | 10min | [concepts/test-time-compute.md](concepts/test-time-compute.md) |

### 第1层：根概念

| 概念 | 一句话 | ⭐ | ⏱️ | 前置 | 页面 |
|------|--------|---|---|------|------|
| **Harness 方法论** | 围绕LLM构建确定性执行环境，约束概率性输出 | ⭐⭐⭐ | 20min | RLHF + 测试时计算 | [concepts/harness-methodology.md](concepts/harness-methodology.md) |

**学完这一层，你能回答**：
- 为什么2026年大家都在谈Harness？
- Agent = Model + Harness 是什么意思？
- PEV循环（Plan-Execute-Verify）怎么工作？
- 五层架构中哪一层影响最大？

### 第2层：子概念（深入Harness）

**从 Harness 方法论延伸出来的子方向**：

```
Harness 方法论
    │
    ├──▶ PEV 循环（Plan-Execute-Verify）
    │       └── 标准SDLC对Agent太慢 → 写计划→执行→验证→重试
    │
    ├──▶ 三Agent架构（Anthropic）
    │       └── Planner + Generator + Evaluator 分离
    │
    ├──▶ 五层架构（行业共识）
    │       └── L1约束 → L2上下文 → L3执行 → L4验证 → L5生命周期
    │
    ├──▶ Context Engineering
    │       └── 不是写好一条Prompt，而是设计动态系统来组装上下文
    │
    └──▶ Cognitive Memory > RAG
            └── 存储"为什么"而不仅是"是什么"
```

### 第3层：实践案例（谁在怎么做）

**学完根概念后，看各家具体怎么落地**：

| 厂商/组织 | 实践 | 关键数据 | 难度 | 页面 |
|-----------|------|----------|------|------|
| **Anthropic** | 三Agent Harness + Managed Agents | p50 TTFT↓60% | ⭐⭐⭐⭐ | [entities/anthropic.md](entities/anthropic.md) |
| **OpenAI** | 100万行生产代码，零手写 | 100万行 | ⭐⭐⭐ | [entities/openai.md](entities/openai.md) |
| **Stripe** | Minions Blueprint：确定性×智能体混合 | 1300+ PR/周 | ⭐⭐⭐⭐ | [sources/stripe-minions-blueprint.md](sources/stripe-minions-blueprint.md) |
| **LangChain** | 仅优化Harness，Terminal Bench剧变 | 52.8%→66.5% | ⭐⭐⭐ | [sources/langchain-terminal-bench-20.md](sources/langchain-terminal-bench-20.md) |
| **月之暗面** | Agent Swarm 100子Agent并行 | SWE-Bench 76.8% | ⭐⭐⭐⭐ | [entities/moonshot.md](entities/moonshot.md) |

### 第4层：工具与协议

**理解了架构后，看具体用什么工具实现**：

| 工具 | 定位 | 热度 |
|------|------|------|
| **MCP** | 模型控制协议，Agent工具访问标准 | 🔥 月下载9700万+ |
| **LangGraph** | 状态管理图，Agent工作流编排 | ⭐⭐⭐ |
| **E2B** | 安全Agent沙箱，隔离执行环境 | ⭐⭐⭐ |
| **ADK** | Google Agent开发套件 | ⭐⭐ |

### 第5层：延伸概念

| 概念 | 与Harness的关系 | ⭐ | 页面 |
|------|----------------|----|------|
| **Agent Skills** | 具体编程技能的实现（Addy Osmani项目） | ⭐⭐⭐ | [concepts/agent-skills.md](concepts/agent-skills.md) |

---

# 分支2：AI 硬件与芯片

> 模型性能受限于内存带宽，而非算力。存储和计算的物理距离是核心瓶颈。

## 🔷 学习路径

### 第0层：前置知识

| 概念 | 一句话 | ⭐ | ⏱️ | 页面 |
|------|--------|---|---|------|
| **冯·诺依曼瓶颈** | 数据在CPU和内存之间搬运消耗60%+系统能耗 | ⭐ | 5min | [concepts/processing-in-memory.md](concepts/processing-in-memory.md#问题内存墙-memory-wall) |

### 第1层：根概念

| 概念 | 一句话 | ⭐ | ⏱️ | 前置 | 页面 |
|------|--------|---|---|------|------|
| **存算一体 (PIM)** | 在内存里做计算，突破冯·诺依曼瓶颈 | ⭐⭐⭐ | 20min | 冯·诺依曼瓶颈 | [concepts/processing-in-memory.md](concepts/processing-in-memory.md) |
| **HBM** | 高带宽内存，AI推理的带宽瓶颈 | ⭐⭐ | 15min | — | [concepts/hbm.md](concepts/hbm.md) |
| **Chiplet** | 芯粒架构，后摩尔时代的模块化设计 | ⭐⭐ | 15min | — | [concepts/chiplet.md](concepts/chiplet.md) |

### 第2层：子概念

**存算一体的三个子方向**（递进关系：从近到远）：

```
存算一体（总概念）
    │
    ├──▶ 近存运算 (Near-Memory Computing)
    │       └── 逻辑层紧邻DRAM/HBM，最接近产品化
    │       └── 代表：NVIDIA HBM4、SK海力士 cHBM、Google 3D-DRAM
    │
    ├──▶ 存内计算 (Compute-in-Memory)
    │       └── 在内存位单元内执行运算，实验室→原型阶段
    │       └── 代表：SRAM-CIM（边缘AI）、ReRAM-CIM（Stanford/清华）
    │
    └──▶ 存内逻辑 (Logic-in-Memory)
            └── 在存储单元内嵌入布尔逻辑，早期研究
            └── 代表：高校为主
```

**HBM 的演进路线**：

```
HBM 技术
    │
    ├──▶ HBM3E（当前主流，2024-2025）
    │
    ├──▶ HBM4（2026H2，NVIDIA Rubin/AMD MI450主力）
    │       └── cHBM：定制化HBM，在base die集成计算逻辑
    │
    └──▶ HBM4E / HBM5（2027-2028，NVIDIA Feynman）
```

### 第3层：硬件竞争格局

**理解了概念后，看各家产品怎么落地**：

| 厂商 | 产品 | 关键规格 | 定位 | 页面 |
|------|------|----------|------|------|
| **NVIDIA** | Rubin (2026H2) | HBM4 576GB / 3nm / 50 PFLOPS FP4 | 训练主力 | [entities/nvidia.md](entities/nvidia.md) |
| **NVIDIA** | Feynman (2028) | 1.6nm / 硅光子 / GAA | 下一代 | [sources/nvidia-feynman-gtc2026.md](sources/nvidia-feynman-gtc2026.md) |
| **AMD** | MI450 (2026H2) | HBM4 432GB / **2nm** / 40 PFLOPS FP4 | 训练竞争 | [entities/amd.md](entities/amd.md) |
| **SK海力士** | cHBM / AiMX / CuD | Stream DQ架构，推理吞吐~7×提升 | 内存+计算 | [entities/sk-hynix.md](entities/sk-hynix.md) |
| **三星** | HBM4E / HCB键合 | 16Gbps/pin，HCB散热降低20%+ | 追赶者 | [entities/samsung.md](entities/samsung.md) |

**竞争关键点**：
- [AMD MI450 vs NVIDIA Rubin 详细对比](sources/amd-mi450-vs-rubin.md)

---

# 分支3：大模型厂商

> 各家的技术路线、模型矩阵、最新动态。

## 🔷 按阵营组织

### 闭源阵营

| 厂商 | 定位 | 最新动态 | 深度分析 |
|------|------|----------|----------|
| **Anthropic** | Harness Engineering领导者，可靠性优先 | Claude 3.7 / Opus 4.7 / Managed Agents | [entities/anthropic.md](entities/anthropic.md) |
| **OpenAI** | 规模+开源并重 | GPT-OSS-120B开源 / o4-mini / 100万行AI代码 | [entities/openai.md](entities/openai.md) |
| **Google DeepMind** | 多语言+长上下文 | Gemini 3.1 Pro/Flash / 1M context | [entities/google-deepmind.md](entities/google-deepmind.md) |

### 开源/中国阵营

| 厂商 | 定位 | 最新动态 | 深度分析 |
|------|------|----------|----------|
| **月之暗面** | Agent Swarm + 价格屠夫 | Kimi K2.5 / 100子Agent / Modified MIT | [entities/moonshot.md](entities/moonshot.md) |
| **DeepSeek** | 推理效率极致 | R2 / $0.27/M input / MIT license | [entities/deepseek.md](entities/deepseek.md) |
| **Meta** | 开源+基础设施 | Llama 4 / $1450亿 capex | [entities/meta.md](entities/meta.md) |

---

# 分支4：开源生态

| 项目 | 作者 | 定位 | 页面 |
|------|------|------|------|
| **ds4** | antirez (Redis作者) | DeepSeek V4 Flash本地推理引擎，C语言零依赖 | [concepts/ds4.md](concepts/ds4.md) |
| **agent-skills** | Addy Osmani | AI编程Agent工程技能库 | [concepts/agent-skills.md](concepts/agent-skills.md) |
| **llm-wiki** | Pratiyush | 本知识库的模式参考实现 | [concepts/llm-wiki-pattern.md](concepts/llm-wiki-pattern.md) |

---

# 分支5：学习资源与方法

| 资源 | 用途 |
|------|------|
| [LLM Wiki 模式](concepts/llm-wiki-pattern.md) | 本知识库的组织方法论 |
| [ABOUT.md](ABOUT.md) | 项目背景、信息源优先级、使用方法 |
| [index.md](index.md) | 机器可读的结构化索引 |

---

# 分支6：每日情报速递

| 日期 | 核心信号 |
|------|----------|
| [2026-05-09](weekly-digest/2026-05-09.md) | Harness成为核心范式 / NVIDIA GTC双架构 / 存算一体产品前夜 |

---

## 附录：概念依赖图（纯文本版）

```
冯·诺依曼瓶颈
    │
    ├──▶ 存算一体
    │       ├──▶ 近存运算 ──▶ HBM ──▶ cHBM ──▶ SK海力士/NVIDIA产品
    │       ├──▶ 存内计算 ──▶ SRAM-CIM / ReRAM-CIM
    │       └──▶ 存内逻辑（早期）
    │
    └──▶ Chiplet（并行解决路径）

RLHF + 测试时计算
    │
    ├──▶ Harness 方法论
    │       ├──▶ PEV循环
    │       ├──▶ 三Agent架构 ──▶ Anthropic实践
    │       ├──▶ 五层架构
    │       ├──▶ Context Engineering
    │       └──▶ Cognitive Memory
    │
    └──▶ Agent Skills ──▶ agent-skills项目
```

---

*最后更新：2026-05-09*  
*设计原则：每个概念标明位置（层级）、依赖（前置/后续）、深度（⭐）、时间（⏱️）*
