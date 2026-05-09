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

### 关键组件
- **Contracts**：输入输出约束、验证门、权限边界
- **Cognitive Memory**：超越RAG，存储决策的"为什么"
- **File-backed State**：外部化持久状态，路径可寻址
- **Failure Taxonomy**：命名失败模式驱动恢复

## 行业验证

| 公司/组织 | 实践 |
|-----------|------|
| **Anthropic** | 三Agent Harness、Managed Agents、Claude Code |
| **OpenAI** | 团队用Harness Engineering交付100万行生产代码 |
| **Stripe** | Minions体系每周合并1300+ AI编写的PR |
| **LangChain** | 仅优化Harness，Terminal Bench 2.0得分从52.8%→66.5% |

## 工具生态
- **LangGraph**：状态管理图
- **E2B**：安全Agent沙箱
- **ADK**：Google Agent开发套件
- **MCP**：模型控制协议（月下载9700万+）

## 关键洞察

> "在AI Agent时代，模型本身不再是瓶颈，围绕模型的外部系统设计才是决定性能的关键杠杆。"

- 模型不变，Harness变，结果剧变
- 环境比模型更重要
- 需要定期Lint：清理随模型升级而过时的workaround

## 相关实体
- [Anthropic](../entities/anthropic.md)
- [OpenAI](../entities/openai.md)
