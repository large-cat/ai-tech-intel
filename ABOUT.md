# 📘 关于 AI Tech Intel

> 本知识库是怎么运作的、追踪什么、怎么使用。

---

## 这是什么

**AI Tech Intel** 是一个每日自动维护的 AI 前沿技术情报知识库。核心目标：

- **追踪信号**：谁在发布什么、什么技术正在从论文走向产品、什么方法论被多家公司独立验证
- **建立关联**：某个厂商的动作和某个技术概念的关系是什么
- **持续更新**：知识随时间增长，不是一次性调研报告

---

## 追踪范围

### 🧠 模型与软件

| 厂商 | 追踪重点 |
|------|----------|
| **Anthropic** | Claude模型、Harness Engineering、三Agent架构 |
| **OpenAI** | GPT/o系列、Harness方法论、开源策略、Stargate |
| **Google DeepMind** | Gemini、TPU、Agent框架 |
| **月之暗面** | Kimi系列、长上下文、MoE、Agent Swarm |
| **DeepSeek** | 推理效率、开源模型、低价策略 |
| **Meta** | Llama系列、AI基础设施投入 |

### ⚡ 硬件与基础设施

| 厂商 | 追踪重点 |
|------|----------|
| **NVIDIA** | GPU架构（Rubin/Feynman）、CUDA生态、HBM策略 |
| **AMD** | MI系列GPU、ROCm、与NVIDIA竞争 |
| **三星** | HBM、存算一体、制程 |
| **SK海力士** | HBM霸主地位、cHBM/AiMX存算一体 |
| **Intel** | Gaudi加速器、代工合作 |

### 🛠️ 开源项目与工具

| 项目 | 作者 | 意义 |
|------|------|------|
| [agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani | AI编程Agent技能库 |
| [ds4](https://github.com/antirez/ds4) | antirez (Redis作者) | DeepSeek V4 Flash本地推理引擎 |
| [llm-wiki](https://github.com/Pratiyush/llm-wiki) | Pratiyush | 本知识库的模式参考 |

### 👤 行业大佬博客

| 人物 | 关注点 |
|------|--------|
| **Andrej Karpathy** | AI教育、LLM工具、Agent架构 |
| **Addy Osmani** | Chrome性能、AI Agent工程 |
| **Simon Willison** | LLM工具、Datasette、实用主义 |
| **swyx** | AI工程、Latent Space播客 |
| **Andrew Ng** | DeepLearning.AI、AI应用落地 |

---

## 信息源优先级

**优先使用：**
- 厂商官方博客（Anthropic Engineering、OpenAI Blog、Google DeepMind Blog）
- arxiv.org 论文
- IEEE 技术文献
- 知名科技媒体（The Next Platform、Tom's Hardware、Wccftech）
- 行业大佬个人博客
- GitHub Release / README

**不使用：**
- CSDN（信息质量不稳定）
- 未经验证的自媒体

---

## 知识库结构

本知识库采用 **Karpathy LLM Wiki 模式** —— 增量式维护的结构化知识库：

| 目录 | 用途 | 给谁看 |
|------|------|--------|
| `entities/` | 厂商/人物/产品的档案卡片 | 人类 / AI |
| `concepts/` | 技术概念的深度分析文章 | 人类 / AI |
| `sources/` | 单篇源文件的摘要（含关键数据和引用） | 人类 / AI |
| `weekly-digest/` | 每日重点摘要（执行摘要 + Top信号） | 人类 |
| `index.md` | 结构化索引，机器可读 | AI |
| `HANDBOOK.md` | 按主题组织的知识导航 | 人类 |
| `ABOUT.md` | 本文件，项目背景 | 人类 |

**核心设计原则**：
- **增量式维护** — 知识随时间增长，每次查询不从零推导
- **结构化页面** — 实体 + 概念 + 源文件，三层互相引用
- **来源可追溯** — 每个结论都标注来源，可下钻验证

---

## 更新节奏

| 时间（北京时间） | 动作 |
|------------------|------|
| 08:00 | 调研亚洲/欧洲时段更新 |
| 20:00 | 调研美国时段更新 |
| 09:30 | 微信推送当日简报 |

---

## 技术重点方向

1. **Harness方法论** — LLM Agent的工程化框架，2026年最核心范式
2. **存算一体 / 近存运算** — 突破冯·诺依曼瓶颈，从论文走向产品
3. **HBM与内存技术** — AI推理的带宽瓶颈，HBM4/4E演进
4. **Chiplet与先进封装** — 后摩尔时代的架构创新
5. **Agent Skills / Agent框架** — 新工具、新协议、新范式

---

## 怎么使用这个知识库

**快速浏览**：打开 [HANDBOOK.md](HANDBOOK.md)，按主题找到你关心的内容。

**追踪某个公司**：去 `entities/` 目录找到对应文件，看时间线和最新动态。

**了解某个技术**：去 `concepts/` 目录找到对应文件，看深度分析。

**看今天发生了什么**：打开 `weekly-digest/最新日期.md`。

**验证某个数据点**：去 `sources/` 目录找对应的源文件摘要，看原始来源。

**让AI帮你查**：给AI看 `index.md`，它有完整的结构化索引。

---

*最后更新：2026-05-09*
