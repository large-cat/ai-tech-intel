# Harness Engineering / Harness方法论

> 类型：AI工程方法论 | 热度：🔥 2026年最核心范式 | 最后更新：2026-05-09

## 定义

Harness Engineering（Harness工程）是2026年出现的AI工程新范式，核心是构建一个确定性的"执行环境"来约束和验证概率性的AI输出。

**核心公式**：Agent = Model + Harness

- **模型（Model）**：大脑——推理能力
- **Harness（马具/线束）**：身体+神经系统+规则框架——让模型在真实环境中持续行动、调用工具、完成长任务

## 为什么需要Harness

传统软件开发（SDD）把AI当API调用，但Agent时代面临三大失败：
1. **幻觉逃避测试** —— 传统测试无法覆盖AI的创造性输出
2. **长窗口上下文退化** —— 长时间任务中上下文丢失
3. **会话状态漂移** —— 多轮交互中目标偏离

## 核心框架

### PEV循环（Plan-Execute-Verify）
- 标准SDLC对Agent太慢
- Harness强制Agent：写计划 → 在Sandbox执行 → Verifier模型检查 → 失败则重试
- 无需人工干预

### 三Agent架构（Anthropic）
| Agent | 职责 |
|-------|------|
| Planner | 规划任务、分解步骤 |
| Generator | 执行生成（代码/设计/内容） |
| Evaluator | 评估输出质量，提供反馈 |

### 五层架构（行业共识）
根据OpenAI、Anthropic、LangChain、Stripe的实践提炼：

| 层级 | 名称 | 职责 | 变化频率 |
|------|------|------|----------|
| L1 | **约束层** | 定义Agent能做什么、不能做什么 | 慢 |
| L2 | **上下文层** | 控制模型每一步看到什么（CLAUDE.md等） | 中 |
| L3 | **执行层** | 工具编排、MCP配置、Sandbox管理 | 中 |
| L4 | **验证层** | 检查输出正确性（测试、类型检查、规则） | **快** |
| L5 | **生命周期层** | 健康监控、崩溃恢复、成本控制、人机协同 | 慢 |

**关键设计原则**：
- **验证层（L4）是最高影响层**：结构化验证带来最大可靠性提升（LangChain实验：仅优化Harness，Terminal Bench 2.0从52.8%→66.5%，排名#30→#5）[来源：LangChain Blog, 2026-02; 中文综合报道]
- **成功静默，失败 loud**：通过测试不进入上下文，仅错误信息反馈给Agent
- **动态工具范围**：规划阶段不需要文件写入权限，减少Token消耗和错误（Vercel实验：移除80%工具后任务成功率反而提升）[来源：行业报道, 2026-03]

### 关键组件
- **Contracts**：输入输出约束、验证门、权限边界
- **Cognitive Memory**：超越RAG，存储决策的"为什么"
- **File-backed State**：外部化持久状态，路径可寻址
- **Failure Taxonomy**：命名失败模式驱动恢复

## 行业验证

| 公司/组织 | 实践 | 关键数据 |
|-----------|------|----------|
| **Anthropic** | 三Agent Harness、Managed Agents、Claude Code | p50 TTFT↓60%，p95 TTFT↓90%+ |
| **OpenAI** | 团队用Harness Engineering交付100万行生产代码 | 零手写代码 |
| **Stripe** | Minions体系每周合并1300+ AI编写的PR | 持续运行 | [来源：行业报道](https://www.mindstudio.ai/blog/what-is-ai-agent-harness-stripe-minions/) (2026-03)，基于Stripe 2025年初披露]
| **LangChain** | 仅优化Harness，Terminal Bench 2.0得分从52.8%→66.5% | 排名#30→#5 |

### Stripe Minions Blueprint：确定性×智能体混合架构

Stripe内部自研的Agent编排框架，源于对Goose（Block/Square开源coding agent）的深度fork，解决"AI写代码不稳定"的核心问题。

**核心创新：Blueprints = 确定性节点 + 智能体节点**

| 节点类型 | 示例 | 特点 |
|----------|------|------|
| **确定性节点（Deterministic）** | git commit、lint、测试、创建分支、推送PR | 硬编码步骤，100%可预测 |
| **智能体节点（Agentic）** | "实现任务描述"、"修复CI失败" | AI自主决策，输出不确定 |

**状态机设计**：交替运行确定性代码节点和自由流动的Agent节点。例如：创建分支（确定）→ 写代码（Agent）→ 运行测试（确定）→ 修复失败（Agent）→ 推送PR（确定）。

**关键子系统：**
- **上下文工程（Context Engineering）**：规则按子目录条件应用，不是全局System Prompt。例如"只在infra/目录启用lint规则"，节省Token并减少误判。
- **Devbox**：10秒启动的隔离开发环境，Agent在此沙箱中运行，与生产隔离。
- **MCP工具网络**：内部"Toolshed"服务器连接400+ MCP工具，Agent按需调用。
- **并行化**：同一Blueprint可在200+服务上同时运行。
- **多Agent协调**：不同Agent专精不同任务类别（前端、后端、安全审计），中央编排器分配任务。
- **人类审查红线**：AI只有提交权，没有合并权。所有PR需人类审查后才合并。

### LangChain Terminal Bench 2.0：Harness优化的"对照实验"

LangChain为验证"Harness>模型"所做的对照实验，被Hugging Face Philipp Schmid称为"2026年最重要的验证"。

**实验设计**：固定模型（Claude 3.5 Sonnet），仅优化Harness，在SWE-Bench Terminal 2.0上测试。

**优化维度与结果**：

| 优化维度 | 具体措施 | 效果 |
|----------|----------|------|
| **System Prompts** | 结构化规划指令、Reasoning Sandwich（xhigh规划→high实现→xhigh验证） | 基线提升 |
| **工具设计** | LocalContextMiddleware（自动映射工作目录和工具位置）、LoopDetectionMiddleware（追踪每文件编辑次数，N次后注入"重新考虑你的方法"） | 减少死循环 |
| **Middleware层** | Trace Analyzer Skill：自动从LangSmith traces分析错误模式，类似boosting——失败案例自动反馈到Harness | 持续提升 |
| **自验证循环** | 时间预算警告、测试要求提示、输出验证 | 减少幻觉 |

**关键发现**：
- **模型-specific Harness tuning**：不同模型需要不同的Harness优化。Claude的Harness不能直接套到GPT上。
- **Reasoning Sandwich**：规划用最高推理深度，实现用中等，验证再用最高——避免"想太多做太少"或"做太快想太少"。
- **开源承诺**：公开了traces数据集和Deep Agents代码。

**基础设施**：Harbor + Daytona 编排Sandbox运行，支持大规模并行评估。

## 工具生态
- **LangGraph**：状态管理图
- **E2B**：安全Agent沙箱
- **ADK**：Google Agent开发套件
- **MCP**：模型控制协议（月下载9700万+）[来源：Anthropic官方及arxiv 2604.05969等多篇论文引用，2026年初数据]

## 关键洞察

> "在AI Agent时代，模型本身不再是瓶颈，围绕模型的外部系统设计才是决定性能的关键杠杆。"

- 模型不变，Harness变，结果剧变
- 环境比模型更重要
- 需要定期Lint：清理随模型升级而过时的workaround
- **Context Anxiety**：模型接近上下文上限时倾向于提前结束任务，Harness需处理

## 相关实体
- [Anthropic](../entities/anthropic.md)
- [OpenAI](../entities/openai.md)

## 引用来源
- [OpenAI: Harness Engineering](https://openai.com/index/harness-engineering/) (2026-02)
- [Anthropic Engineering: Managed Agents](https://www.anthropic.com/engineering/managed-agents) (2026-04)
- [Anthropic Research: Trustworthy Agents](https://www.anthropic.com/research/trustworthy-agents) (2026-04)
- [Harness Engineering: What Every AI Engineer Needs](https://ai.gopubby.com/harness-engineering-what-every-ai-engineer-needs-to-know-in-2026-0ab649e5686a) (2026-04)
- [Harness五层架构详解](https://cozypet.github.io/five-layers-harness/v2.html) (2026-04)
- ~~[从Harness Engineering到本地智能](https://juejin.cn/post/7629339148294209551)~~ (2026-04) [⚠️内容不符：实际为端脑科技硬件产品软文，非Harness技术详解]
- [Mitchell Hashimoto: My AI Adoption Journey](https://mitchellh.com/writing) (2026-02)
- [ThoughtWorks: Harness Engineering框架](https://martinfowler.com/) (2026)
