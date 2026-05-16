# Harness Verifier Model 训练方法与多 Agent 容错架构深度调研

> 来源汇总：arXiv 2603.18886 (Principia/J1), arXiv 2511.07833 (MURPHY), arXiv 2601.17223 (VPRM), arXiv 2605.05737 (ReFlect), arXiv 2503.13657 (MAST), arXiv 2601.05755 (VIGIL), arXiv 2604.13630 (SafeHarness), 以及 Tian Pan / Redis / 51CTO / Preprints.org 等社区分析。
> 调研日期：2026-05-16

---

## 一、Verifier Model 的三种训练范式

### 1.1 On-Policy Judge/Verifier 训练（J1 / Principia 框架）

**论文**：Principia — arXiv:2603.18886 (Meta FAIR, 2026-03)

核心发现：训练一个"严格的 LLM-as-Verifier"最有效的方法不是离线监督学习，而是 **on-policy 强化学习**。

**训练配方**：
1. **数据构建**：构建 Principia 数据集 —— 要求模型推导数学对象（非数值/MCQA），输出必须是结构化数学表达式。
2. **LLM-as-Judge**：使用 Qwen3-235B / o3 等强模型做初始评判，但发现即使强模型在复杂推导上也犯错。
3. **On-Policy Judge Training**：
   - 用 RLVR（RL with Verifiable Rewards）训练独立的 Judge 模型
   - Judge 的奖励来自 **ground-truth formal verification**（如 Lean/Isabelle 形式化验证）
   - 关键：Judge 必须在与被评估的推理轨迹 **同一分布** 的数据上训练（on-policy），否则存在严重的 distribution shift
4. **Test-Time Scaling**：训练好的 Judge 可通过 aggregation（多数投票 / 加权聚合）在推理时扩展计算，提升验证准确率。

**关键结论**：
- On-policy 训练比 off-policy SFT 提升显著 —— Judge 在分布外数据上的判断准确率差距可达 15-20%。
- Verifier 与被验证模型的 **能力对齐** 很重要：用弱 verifier 评判强 policy 会出现 "transfer gap"，导致验证信号失效。

---

### 1.2 多轮反馈驱动的 Verifier 训练（MURPHY）

**论文**：MURPHY — arXiv:2511.07833v3 (CMU/Industry, 2025-11 → 2026-02)

**问题**：传统 GRPO 只优化单轮结果，对需要迭代决策的 Agent 任务效果差。

**核心创新**：
- **Feedback-Conditioned Rollout Tree**：每轮 rollout 后，将执行反馈（编译错误、测试失败、运行时异常）编码为结构化信号，输入到下一轮生成中。
- **Trajectory-Level Credit Assignment**：在多轮轨迹中用类似 PPO 的 advantage 估计，给每个决策步骤分配信用。
- **Pruning**：剪掉明显错误的分支，降低多轮优化的计算成本。
- **独立 Verifier 模型**：训练一个专门的 verifier 评估每轮中间结果的可修复性（plausibility），决定是否继续迭代或回退。

**实验结果**：
- 在代码生成 benchmark 上，MURPHY 比 compute-matched GRPO 基线提升 **8% absolute pass@1**。
- 独立 verifier 能识别 "有修复价值的错误" vs "根本性方向错误"，减少无效迭代。

---

### 1.3 可验证过程奖励模型（VPRM）

**论文**：VPRM — arXiv:2601.17223 (UCL / 医学证据综合领域, 2026-01)

**核心问题**：传统 PRM 用神经网络评判中间步骤，存在 opacity、reward hacking、bias 风险。

**解决方案**：
- **确定性规则验证器替代神经网络**：在医学证据偏倚评估领域，中间推理步骤可通过 guideline-defined criteria 和 rule-based decision paths 进行程序化验证。
- **VPRM 框架**：每一步的中间推理都经过确定性规则检查，而非神经网络打分。
- 奖励信号来自 **可验证的规则满足度**（rule compliance），而非 learned reward model 的预测。

**实验结果**：
- VPRM 比 SOTA 模型提升 **20% F1**。
- 比纯结果级可验证奖励（Outcome Reward）提升 **6.5%**。
- 步骤级决策与最终标签的一致性（coherence）显著优于神经 PRM。

**启示**：在有明确规则/形式化规范的领域（数学证明、代码编译、医学指南），**规则验证器 > 神经网络验证器**。

---

### 1.4 Verifier 训练方法总结对比

| 方法 | 核心机制 | 适用场景 | 优势 | 局限 |
|------|---------|---------|------|------|
| **On-Policy RL Judge** (Principia) | RLVR 训练 LLM-as-Judge，奖励来自形式化验证 | 数学/科学推导 | 分布对齐，可扩展 test-time compute | 需要形式化 ground truth |
| **Feedback-Conditioned Multi-Turn** (MURPHY) | 执行反馈编码 + 轨迹级信用分配 | 代码生成 / Agent 迭代任务 | 利用真实执行信号，减少幻觉 | 需要多轮交互环境 |
| **Rule-Based VPRM** | 确定性规则检查中间步骤 | 规则明确领域（医学/合规） | 零幻觉、可解释、零训练成本 | 仅适用于可规则化领域 |
| **Self-Play Verifier** (SPELL) | 同一模型扮演生成者和验证者 | 通用推理 | 无需额外训练数据 | 存在自我确认偏差 |

---

## 二、多 Agent Harness 的失败模式分类与自动恢复

### 2.1 MAST 失败模式分类法（14 类）

**论文**：MAST — arXiv:2503.13657 (NeurIPS 2025 D&B)

对 1,600 条执行轨迹、7 个框架（MetaGPT, ChatDev, HyperAgent, AppWorld, AG2, Magentic-One, OpenManus）的实证分析：

**整体失败率：41% - 87%**（每个框架都如此）。

**Top 3 失败模式**：
1. **Step Repetition (15.7%)**：Agent 在无意义地重复相同步骤，没有进展。
2. **Reasoning-Action Mismatch (13.2%)**：推理说要做 A，实际执行了 B。
3. **Unaware of Termination (12.4%)**：任务已完成但 Agent 不停止，继续无效操作。

**三大类别**：

**A. Inter-Agent Misalignment (37%)**
- Context Collapse：一个 Agent 的输出超出另一个的上下文窗口，关键状态被静默丢弃。
- Format Mismatches：A 产出 YAML，B 期望 JSON，无验证步骤。
- Conflicting Resource Ownership：两个 Agent 写入同一位置，产生竞态条件。
- Natural Language Ambiguity："处理订单"对不同 Agent 含义不同。

**B. Task Verification and Termination (21%)**
- Premature Termination (6.2%)：Agent 在任务未完成时标记完成。
- Incomplete Verification (8.2%)：验证步骤存在但检查了错误的内容。
- Incorrect Verification (9.1%)：Verifier 本身对正确性判断错误。

**C. Error Compounding and Conformity Bias**
- Hallucination Propagation：一个 Agent 的幻觉被下游 Agent 当作事实传递。
- Conformity Bias：当 Agent A 做出自信断言，其他 Agent 倾向于附和而非质疑。
- Monoculture Problem：用同一模型做规划和验证，验证器与规划器有相同盲点。

**关键发现**：
- 有显式 verifier 的系统（MetaGPT, ChatDev）失败率显著更低。
- 添加高层目标验证（objective verification）可提升 **+15.6%** 成功率。
- LLM-as-Judge 与人类专家的一致性达 **94%**。

---

### 2.2 ReFlect：结构化 Harness 的 Level 3 方案

**论文**：ReFlect — arXiv:2605.05737 (2026-05)

将推理范式分为 4 个层级：

| 层级 | 范式 | 状态位置 | 错误检测 | 恢复动作 |
|------|------|---------|---------|---------|
| **Level 0** | CoT 单轮生成 | token 轨迹 | 无 | 无 |
| **Level 1** | ReAct / ToT | 文本级 + 环境观察 | 启发式 | 搜索树分支 |
| **Level 2** | Self-Refine / CRITIC | LLM 自身评判 | LLM 调用 | 文本重写 |
| **Level 3** | **ReFlect (本工作)** | **外部结构化状态** | **确定性检查器** | **程序化干预** |

**ReFlect 的 Heavyweight 设计**：
1. **假设追踪（Assumption Tracking）**：将假设作为一等对象，带依赖链接。假设被撤回时，依赖它的所有元素级联标记/撤回。
2. **不确定性估计**：由四个归一化信号合成：(a) 未验证假设比例，(b) 未解决冲突密度，(c) 低置信度证据比例，(d) 被阻塞目标比例。
3. **状态提取**：轻量级独立 LLM 调用从自由文本输出中提取结构化元素（证据、假设、决策、冲突）。
4. **编译视图（Compile View）**：根据当前模式（Execute/Verify/Recover）构造不同形态的 prompt，改变基础 LLM 的行为。
5. **四大操作符**：Inspect（结构化诊断）、Recover（持久化恢复表示）、Transform（靶向干预）、Stabilize（固化成功恢复）。

**实验**：在 70B 模型上评估，轻量版（shape classifier + tool registry）为 headline result，重量版在完整 pilot study 上评估。

---

### 2.3 VIGIL：Verify-Before-Commit 范式

**论文**：VIGIL — arXiv:2601.05755 (2026-01)

针对工具流注入攻击（Tool Stream Injection）提出的防御架构：

**两大系统性漏洞**：
1. **Alignment-Driven Vulnerability**：强推理模型因严格对齐训练，反而更容易将注入的恶意规则视为权威约束。
2. **Static Defense Fragility**：plan-then-execute 范式在环境非确定性时切断反馈循环。

**VIGIL 架构**：
1. **动态约束合成**：基于用户意图建立信任根（root of trust）。
2. **感知净化（Perception Sanitization）**：中和对抗性输入。
3. **推测性推理（Speculative Reasoning）**：探索潜在执行路径。
4. **运行时验证器**：在提交前严格验证暂定轨迹。
5. **自适应回溯（Adaptive Backtracking）**：当验证失败时回退并修正。

**核心原则**：将 **推理探索** 与 **不可逆动作** 解耦。

---

### 2.4 社区最佳实践（Tian Pan / Redis / 51CTO）

**快速失败与恢复设计原则**：
1. **结构化通信协议**：Agent 间用 JSON-RPC / Protobuf 通信，而非自然语言。每条消息在边界处做 schema 验证。
2. **资源所有权规则**：一个 Agent 拥有一个资源。共享状态通过显式共享内存层路由。
3. **独立 Judge Agent**：验证必须与生成解耦。生产内容的 Agent 不应是验证者 —— 否则会产生循环推理。
4. **检查点持久化**：在有意义步骤持久化状态，故障时从检查点恢复而非从头开始。
5. **可观测性**：为每次 Agent 调用、工具调用、Agent 间消息使用 correlation ID。记录结构化 trace（Agent 身份、输入输出、工具调用、token 消耗、延迟、每步成功/失败状态）。
6. **Prompt 作为可靠性杠杆**：在生产 prompt 上构建模拟，逐步观察 Agent 行为。这比单元测试更早暴露失败模式。
7. **为删除而建**：保持架构高度模块化。2024 年需要复杂手工管道的能力，2026 年可能一个 prompt 就能完成。过度固化的逻辑会成为系统进化的障碍。

**故障恢复策略分类**（PALADIN / SHIELDA）：
| 故障类型 | 恢复策略 |
|---------|---------|
| 网络超时 | Retry with backoff |
| Schema 错误 | Alternative tool substitution |
| 权限拒绝 | Graceful degradation |
| 执行异常 | 分类后路由到对应 handler |
| 配额耗尽 | 降级到低成本模型 |
| 依赖失败 | 切换备用服务 |

**关键结论**：Harness 异常处理设计解释的性能方差 > 模型尺寸 —— 这直接颠覆了 "模型能力决定一切" 的隐含假设。

---

## 三、关键洞察与工程建议

### 3.1 Verifier 设计的黄金法则

1. **能力对齐**：Verifier 不应比被验证模型弱太多。弱 verifier 评判强 policy 会产生系统性漏判。
2. **分布对齐**：Verifier 必须在 on-policy 数据上训练，否则面临严重分布偏移。
3. **规则优先**：在可规则化的领域（数学、代码、医学指南），确定性规则验证器 > 神经网络验证器。
4. **独立上下文**：Verifier 必须有独立的上下文窗口和评分标准，不能与生成者共享上下文。
5. **可验证性闭环**：Verifier 的评判标准本身必须是可验证的（形式化验证 / 单元测试 / 规则检查），否则 verifier 也会被 hack。

### 3.2 多 Agent Harness 的设计原则

1. **从单 Agent 开始**：先用单 Agent 架构建立基线，只在并行化收益明确时才增加 Agent。
2. **每层边界都验证**：用 schema check 验证 LLM 输出后再传递给下游。
3. **不同模型做验证**：规划和验证用不同模型（或至少不同参数规模/训练数据），避免 monoculture problem。
4. **故障分类先行**：Harness 必须在涉及模型恢复前对故障类型进行分类（可重试 vs 不可重试，认证错误 vs 配额耗尽）。
5. **Agent 间传递异常类型**：多 Agent 部署中，harness 间的接口必须传递异常类型（type, severity, recoverability），否则故障遏制在结构上不可能实现。

---

## 四、引用源

1. Principia — arXiv:2603.18886 (Meta FAIR, 2026-03)
2. MURPHY — arXiv:2511.07833v3 (CMU, 2025-11)
3. VPRM — arXiv:2601.17223 (UCL, 2026-01)
4. ReFlect — arXiv:2605.05737 (2026-05)
5. MAST — arXiv:2503.13657 (NeurIPS 2025)
6. VIGIL — arXiv:2601.05755 (2026-01)
7. SafeHarness — arXiv:2604.13630 (2026-04)
8. Tian Pan — "Why Multi-Agent LLM Systems Fail" (2025-10)
9. Redis Blog — "Why Multi-Agent LLM Systems Fail & How to Fix Them" (2026-04)
10. 51CTO — "Agent Harness 核心价值" (2026-03)
11. Preprints.org — "Agent Harness for LLM Agents: A Survey" (2026-04)
12. Christopher Meiklejohn — "Getting Up to Speed on Multi-Agent Systems, Part 4" (2026-04)
