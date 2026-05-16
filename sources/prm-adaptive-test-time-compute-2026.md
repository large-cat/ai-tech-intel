# PRM 训练数据构建与 Test-Time Compute 自适应预算分配深度调研

> 来源汇总：arXiv 2506.00027 (PRM Generalization), arXiv 2505.15960 (FoVer), arXiv 2602.01070 (Adaptive TTC), arXiv 2604.14853 (Solve-then-Learn), arXiv 2601.04700 (PRISM), arXiv 2601.07182 (PRPO), OpenReview df3p10k2kq / o0k034W6vx (Discriminative PRM), arXiv 2509.21154 (PRM-GRPO), emergentmind.com PRM overview, Zylos.ai RL posttraining guide。
> 调研日期：2026-05-16

---

## 一、PRM 训练数据构建：从人工标注到自动合成

### 1.1 核心挑战

PRM（Process Reward Model）需要 **步骤级标签**（step-level labels）来评估推理链中每一步的正确性。传统方法依赖：
- **人工标注**：成本高、规模受限（OpenAI 的 PRM 用了数千人时）。
- **采样标注**：用 LLM 多次采样后通过结果一致性推断步骤标签，需要大量 LLM 调用。

**关键问题**：
- PRM 训练数据的质量直接决定 PRM 的泛化能力。
- 步骤级标注的噪声会导致 PRM 在训练时过拟合到特定错误模式。
- 领域迁移时，PRM 在训练领域外的表现可能大幅下降。

---

### 1.2 自动步骤级标注方法

#### 方法 A：蒙特卡洛 rollout（MC-PRM）

**原理**：对推理链的每个前缀进行大量随机 rollout，用最终结果的准确率作为该步骤的奖励信号。

**公式**：
```
R(s_t) = E[Outcome | prefix = s_0...s_t]
```

**优势**：无需人工标注，可大规模生成。
**局限**：
- 计算成本高（每个步骤需要多次 rollout）。
- 早期步骤的 rollout 方差大，信号稀疏。
- 存在 **credit assignment 模糊**：一个步骤的正确性可能被后续步骤的错误掩盖。

#### 方法 B：自动步骤级标注框架（ASLAF）

**论文**：arXiv 2506.00027 ("From Mathematical Reasoning to Code: Generalization of PRMs", 2025-05)

**核心发现**：
- PRM 在数学数据集上训练的模型，在代码生成任务上表现 **可比于专门在代码上训练的 PRM** —— 显示跨领域泛化能力。
- 训练数据的 **多样性** 比 **领域匹配** 更重要。
- 梯度分析显示 PRM 倾向于选择具有相似底层模式的响应。

**标注策略**：
1. 使用 **结果验证器**（unit test / exact match）自动判断最终答案是否正确。
2. 对于正确轨迹，所有步骤标记为正。
3. 对于错误轨迹，用 **最短前缀差异法** 定位第一个错误步骤：比较错误轨迹与正确轨迹的步骤前缀，第一个分叉点即为错误步骤。
4. 通过 **Best-of-N** 采样生成足够的正负样本对。

#### 方法 C：形式化验证标注（FoVer）

**论文**：FoVer — arXiv 2505.15960 (2025-05, 多版本更新至 2026-04)

**核心创新**：
- 对形式化推理任务（逻辑、定理证明），用 **Z3 / Isabelle** 等自动定理证明器标注步骤级错误标签。
- **完全自动化**：无需人工标注，无需额外 LLM 调用。
- 构建的数据集在 **12 个推理 benchmark** 上验证，包括非形式化任务（NLI, BBH）。

**实验结果**：
- 在 FoVer 数据上微调的 PRM，不仅在数学/逻辑任务上提升，在 **NLI 和 BBH**（与训练任务差异很大的任务）上也显著改进。
- 证明 PRM 可以从形式化验证数据中学习，泛化到自然语言推理任务。

#### 方法 D：无步骤标签学习判别式 PRM

**论文**：OpenReview df3p10k2kq / o0k034W6vx (ICLR 2026)

**核心突破**：
- 传统 PRM 需要昂贵的步骤级标签。
- 提出 **从隐式信号学习过程奖励** —— 不依赖显式步骤标签。
- 方法：利用 policy 模型自身的隐藏状态（hidden states）提取过程级信用分配信号，无需额外 reward model。
- 另一路线（Cui et al., 2025）：通过 outcome-level 信号的隐式传播推断步骤质量。

---

### 1.3 PRM 训练数据质量的关键因子

| 因子 | 影响 | 最佳实践 |
|------|------|---------|
| **数据多样性** | 高多样性 > 领域匹配 | 混合数学、代码、逻辑、科学推理数据 |
| **标签准确性** | 噪声标签导致 PRM 过拟合 | 使用形式化验证器或强 outcome verifier |
| **步骤粒度** | 过细增加噪声，过粗丢失信号 | 按语义单元分段（如一个数学变换、一行代码） |
| **正负比例** | 严重不平衡影响校准 | 通过采样控制正负比例在 1:2 到 1:3 |
| **模型规模** | PRM 规模存在收益递减 | 7B-13B PRM 通常足够，更大模型边际收益递减 |

**论文支持**：arXiv 2506.00027 的系统分析表明，PRM 性能随规模增加呈现 **diminishing returns**，模型大小与计算成本的平衡至关重要。

---

## 二、PRM + RLHF 联合训练框架

### 2.1 PRM 与 PPO/GRPO 的结合难点

**核心矛盾**：
- GRPO（Group Relative Policy Optimization）消除了 PPO 中的 critic model 和 GAE，大幅简化训练。
- 但 GRPO 原本为 outcome-level reward 设计，如何接入 step-level 的 PRM 信号？

**已知实现**（截至 2026-05）：
- Shao et al. (2024) DeepSeekMath：修改 GRPO 以支持 step-level rewards。
- Yang et al. (2025)：PRM + GRPO 在 RLHF 中的应用。
- Feng et al. (2025)：PRM + GRPO 的另一种实现。
- **但这些都是特例** —— GRPO 与 PRM 的广泛结合仍需要算法层面的修改。

---

### 2.2 PRPO：Process Relative Policy Optimization

**论文**：PRPO — arXiv:2601.07182v3 (上海大学/中科大/复旦, 2026-02)

**核心创新**：在无 critic 框架中统一 outcome reward 和 process reward。

**方法**：
1. **语义分段**：根据语义线索将推理序列分段（segmentation）。
2. **PRM 分数归一化**：将 PRM 的步骤级分数转换为 token-level advantages。
3. **分布对齐**：通过 location-parameter shift 将 process advantages 的分布与 outcome advantages 对齐。
4. **组合信号**：最终 advantage = outcome advantage + aligned process advantage。

**关键机制**：
- **防截断（Anti-Truncation）**：纯 PRM 可能导致早期低奖励 token 驱动策略生成截断输出。PRPO 通过分布对齐避免此问题。
- **Length Penalty**：长度超过 1024 时施加惩罚，防止无意义扩展。

**实验结果**：
- Qwen2.5-Math-1.5B 在 MATH500 上：GRPO 61.2% → PRPO 64.4%（+3.2%）。
- PRPO + PRM-Avg 联合使用可达 66.0%。
- 在 AMC2023 和 AIME2024 上也有显著提升。

---

### 2.3 PRISM：统一的后训练框架

**论文**：PRISM — arXiv:2601.04700v2 (2026-01)

**设计目标**：解决无明确可验证奖励任务的后训练问题（如创意写作、开放式对话）。

**架构**：
- **PRM 作为质量评估器**：用 PRM 评估生成质量，替代传统的 outcome reward。
- **与 GRPO 结合**：PRM 提供 process-level 反馈，GRPO 进行策略优化。
- **使用 GenPRM-7B** 作为过程奖励模型。

**实验**：
- 在 MATH、GSM-8k、Minerva-Math 上对比 GRPO with Ground-Truth、INTUITOR、PRISM。
- 对于代码推理，在 LiveCodeBench 上评估 Python 代码生成。

---

### 2.4 PRM-GRPO 训练的关键工程要点

根据 Zylos.ai 2026-04 的行业总结：

**生产 Agent 训练的最佳实践**：
1. **起步用 ORM + Outcome Reward Shaping**：开始用 outcome reward model + 部分信用奖励（如格式正确、中间步骤部分完成）。
2. **轨迹 >10 轮时引入轻量 PRM**：短轨迹（<10 步）ORM 足够；长轨迹需要 PRM 提供中间信号。
3. **GenRM 仅在高预算场景使用**：GenRM（生成式 reward model）需要大量数据和计算，仅在能负担得起时使用。
4. **PRM 的奖励黑客风险**：PRM 特别容易被 hack（Cui et al., 2025）。需要：
   - 定期用 held-out 数据验证 PRM 的校准度。
   - 监控 PRM 分数分布，防止 collapse 到 narrow band。
   - 使用 RewardBench 2 进行跨领域验证。

---

## 三、Test-Time Compute 自适应预算分配

### 3.1 问题形式化

**核心问题**：给定有限的推理预算，哪些输入值得更多计算？哪些可以廉价回答？

**数学形式化**（Solve-then-Learn, arXiv 2604.14853）：
- **约束优化问题**：最大化期望准确率，受限于平均计算预算。
- 每个实例（instance）的最优计算量不同 —— 简单问题需要少算，复杂问题需要多算。

---

### 3.2 Solve-then-Learn 两阶段框架

**论文**：Adaptive Test-Time Compute Allocation — arXiv 2604.14853 (2026-04)

**阶段一：Solve（求解）**
1. **拉格朗日松弛**：将全局预算约束分解为每个实例的子问题。
2. **闭式 Oracle 动作**：每个实例有 closed-form 的最优动作，权衡准确率与成本。
3. **单调性保证**：证明诱导成本在对偶变量上单调，可通过二分搜索精确命中目标预算。

**阶段二：Learn（学习）**
1. 训练轻量级分类器预测 Oracle 动作。
2. 输入特征仅需廉价特征（如 prompt 长度、问题类型、模型置信度）。
3. **遗憾界**：学习策略的任务级遗憾被 imitation error × worst-case per-instance gap 所界定。

**实验结果**（MATH / GSM8K，DeepSeek-V3 / GPT-4o-mini / Qwen2.5-7B）：
- 相比均匀分配和启发式分配，**最高提升 12.8% 相对准确率**（MATH 上）。
- 跟踪拉格朗日 Oracle 上界，imitation accuracy >91%。

---

### 3.3 PRM 引导的自适应推理框架

**论文**："What If We Allocate Test-Time Compute Adaptively?" — arXiv 2602.01070v4 (2026-02 → 2026-04)

**核心设计**：将推理视为 **迭代轨迹生成与选择**。

**每轮迭代**：
1. **高层规划**（可选）：生成解题计划。
2. **工具选择 + 计算策略 + 探索参数**：动态选择推理工具和计算预算。
3. **候选轨迹生成**：基于当前策略生成推理步骤。
4. **PRM 作为统一控制信号**：
   - **迭代内**：步骤级 PRM 分数聚合指导生成过程中的剪枝和扩展。
   - **跨迭代**：聚合轨迹奖励用于选择最终响应。

**效率特征**：
- 使用理论 FLOPs 和 **计算强度指标**（惩罚浪费的生成和工具开销）。
- 验证引导的分配将计算集中在 **高效用推理路径** 上。

**实验结果**：
- 在 MATH-500 上大幅超越直接 test-time scaling。
- 在 AIME24 和 AMO-Bench 等 harder benchmark 上提升数倍（several-fold improvements）。

---

### 3.4 自适应 Test-Time Compute 方法对比

| 方法 | 核心机制 | 需要训练？ | 开销 | 适用场景 |
|------|---------|-----------|------|---------|
| **Solve-then-Learn** | 拉格朗日松弛 + 轻量分类器 | 是（离线） | 低（实时分类） | 批量部署，预算严格约束 |
| **PRM 引导动态分配** | PRM 分数驱动剪枝/扩展 | 是（PRM） | 中（每步 PRM 评估） | 复杂推理，需要细粒度控制 |
| **Best-of-N** | 采样 N 次取最好 | 否 | 高（N× 计算） | 资源充足，简单实现 |
| **MCTS** | 蒙特卡洛树搜索 | 可选 | 最高 | 资源极充足，复杂决策空间 |
| **长度惩罚启发式** | 根据 prompt 特征估计难度 | 否 | 极低 | 快速部署，粗略分配 |

**论文支持**：arXiv 2506.00027 的分析表明，MCTS 在计算资源充足时最有效，Best-of-N 是资源受限时的实用替代。

---

## 四、关键洞察与工程建议

### 4.1 PRM 数据构建最佳实践

1. **优先形式化验证**：在可用形式化验证的领域（数学、逻辑、代码），用 Z3/Isabelle/单元测试自动标注，避免人工成本和噪声。
2. **多样性 > 领域匹配**：PRM 的泛化能力主要来自训练数据的多样性，而非与目标任务领域匹配。
3. **控制标签噪声**：步骤级标签的噪声会直接导致 PRM 过拟合。使用强 verifier（如编译器、定理证明器）确保标签质量。
4. **规模适度**：7B-13B 的 PRM 通常足够。更大模型边际收益递减，且增加推理成本。
5. **无标签替代方案**：如果步骤标注成本过高，考虑判别式 PRM（从隐式信号学习）或隐藏状态信用分配方法。

### 4.2 PRM + RL 联合训练要点

1. **PRPO > 简单 PRM 平均**：PRPO 的分布对齐机制解决了 PRM 单独使用时的截断问题。
2. **ORM 起步，PRM 增强**：生产环境建议先用 ORM + outcome shaping 建立基线，轨迹长度超过 10 步时引入 PRM。
3. **防 reward hacking**：PRM 比 ORM 更容易被 hack。需要持续监控 PRM 校准度和分数分布。
4. **GRPO 需修改以支持 PRM**：标准 GRPO 不支持 step-level reward。需要使用 PRPO、PRISM 或修改版 GRPO。

### 4.3 Test-Time Compute 预算分配策略

1. **非均匀分配 > 均匀分配**：简单问题少算、复杂问题多算，相比均匀采样显著提升效率。
2. **离线训练分类器成本低**：Solve-then-Learn 的轻量分类器在推理时开销极低，适合高并发部署。
3. **PRM 动态控制 > 固定策略**：PRM 引导的动态剪枝/扩展在复杂推理上效果最佳，但每步需要 PRM 评估。
4. **理论保证很重要**：拉格朗日松弛提供了预算精确的数学保证，避免实际部署中预算超支。

---

## 五、引用源

1. PRM Generalization — arXiv 2506.00027 (Yudong Wang et al., 2025-05)
2. FoVer — arXiv 2505.15960 (Ryo Kamoi, 2025-05, v3 2026-04)
3. "What If We Allocate Test-Time Compute Adaptively?" — arXiv 2602.01070v4 (Ahsan Bilal, 2026-02)
4. Solve-then-Learn — arXiv 2604.14853 (Zhiyuan Zhai, 2026-04)
5. PRISM — arXiv 2601.04700v2 (2026-01)
6. PRPO — arXiv 2601.07182v3 (Ruiyi Ding et al., 2026-02)
7. Discriminative PRM without Step Labels — OpenReview df3p10k2kq / o0k034W6vx (ICLR 2026)
8. PRM-GRPO — arXiv 2509.21154 (2025-09)
9. "Process Reward Models: A Survey" — emergentmind.com (2026)
10. "RL Posttraining for Tool-Using Agents" — Zylos.ai (2026-04)
11. RewardBench 2 — bestaiweb.ai (2026-03)
12. Hidden States Credit Assignment — arXiv 2604.23318 (2026-04)
