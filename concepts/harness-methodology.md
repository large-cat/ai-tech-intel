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
