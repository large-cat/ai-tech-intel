# RLHF 新变体深度解析：Online DPO / IPO / KTO

> 来源：[鹤啸九天 RLHF原理及进化](https://wqw547243068.github.io/rlhf) | [arxiv:2509.11298](https://arxiv.org/pdf/2509.11298) — 对齐方法统一框架 | [OpenReview: Online IPO](https://openreview.net/pdf?id=G1R8Ns8n38) | [港中文 EEPO](https://wqw547243068.github.io/rlhf)  
> 关联概念：[[RLHF]], [[DPO]], [[PPO]], [[GRPO]], [[HALO]]  
> 日期：2026-05-15（综合多源分析）

---

## 背景：为什么需要 DPO 的替代品

### PPO-RLHF 的核心问题

传统 RLHF 三阶段流程（SFT → RM 训练 → PPO 优化）存在三个痛点：

1. **训练不稳定**：PPO 的 clip ratio、GAE、Critic 网络同时优化，超参敏感
2. **需要奖励模型**：RM 训练需要大量偏好数据，且 RM 本身可能过拟合
3. **计算成本高**：PPO 需要在线采样（rollout），每步都要生成完整回答

### DPO 的革命性简化

2023年提出的 **Direct Preference Optimization (DPO)** 将 RLHF 简化为一个**单阶段、无需奖励模型**的对比学习损失：

```
L_DPO = -log σ(β * [(log π(y_w|x) - log π_ref(y_w|x)) - (log π(y_l|x) - log π_ref(y_l|x))])
```

**本质**：带参考模型的对比学习。用偏好数据直接优化策略，完全跳过 RL 循环。

**效果**：训练快、稳定，但存在过拟合风险（尤其当 β 调参不当时）。

---

## 变体1：IPO（Identity Preference Optimization）

### 核心动机

DPO 在偏好数据上容易**过拟合**——当策略和参考模型的差距过大时，DPO 损失会变得极端，导致策略坍缩到只生成 preferred 回答。

### 数学改进

IPO 在 DPO 基础上添加了**正则化项**，将损失从 log-sigmoid 改为平方损失：

```
L_IPO = E[(log π(y_w|x) - log π_ref(y_w|x) - log π(y_l|x) + log π_ref(y_l|x) - τ)^2]
```

其中 τ 是一个目标 margin 超参数。

**关键差异**：
- DPO：push preferred 回答概率上升、rejected 下降（无上限，可能过度优化）
- IPO：将偏好差距约束在一个目标范围内（平方损失自带正则化效果）

### Online IPO

2024-2025年发展的 **Online IPO** 将离线偏好数据改为在线采样：

```
L_online_IPO = E_{(y,y')~π_θ}[p*(y>y') * ((r_θ(y) - r_θ(y')) - 1/2)^2 
                              + p*(y'>y) * ((r_θ(y') - r_θ(y)) - 1/2)^2]
```

**流程**：
1. 策略模型生成一对回答 (y, y')
2. 奖励模型或人类判断哪个更好
3. 直接用 IPO 损失更新策略

**优势**：策略始终更新自己的采样分布，数据更"新鲜"，减少分布偏移。

---

## 变体2：KTO（Kahneman-Tversky Optimization）

### 理论基础：前景理论

KTO 基于 **Kahneman-Tversky 前景理论**（Prospect Theory）——人类以有偏见但定义明确的方式感知随机变量，例如著名的**损失厌恶**（loss aversion）。

### 核心创新：从 Pairwise 到 Pointwise

DPO/IPO 都需要**成对偏好数据**（y_w vs y_l），而 KTO 只需要**二元信号**（这个回答好 / 不好）：

```
L_KTO = E[λ_y * (1 - σ(β * (r_θ(x,y) - r_ref(x,y))))]
```

其中 λ_y 根据 y 是"好"还是"坏"调整权重（体现损失厌恶：坏样本惩罚更重）。

**三种数据需求对比**：

| 方法 | 数据形式 | 标注成本 |
|------|---------|---------|
| PPO-RLHF | 成对偏好 + 奖励分数 | 高 |
| DPO | 成对偏好（chosen/rejected）| 中 |
| IPO | 成对偏好 + margin 控制 | 中 |
| **KTO** | **单样本二元标签（好/坏）** | **低** |

### HALO 框架

KTO 属于 **HALO（Human-Aware Loss Functions）** 家族——将人类感知偏见显式编码进损失函数。

> "没有一个 HALO 普遍优越；最佳损失取决于最适合给定设置的归纳偏差。"

实验结果（7B 模型）：
- DPO（β=0.01）MT Bench 分数最高
- KTO 表现接近 DPO
- IPO 效果不如基础模型（当 β 调参不当时）

---

## 变体3：Online DPO

### 核心机制

Online DPO 将 DPO 从**离线**（固定偏好数据集）改为**在线**（策略自己生成数据）：

```
1. 策略模型 π_θ 生成回答 y
2. 奖励模型打分 r(y) 或人类判断
3. 将 (x, y, r(y)) 加入动态数据集
4. 用 DPO 损失更新 π_θ
5. 重复
```

**与 PPO 的区别**：
- PPO：在线采样 + RL 优化（策略梯度、优势估计、Critic）
- Online DPO：在线采样 + 对比损失（无需 Critic，无需优势估计）

### Samplers-in-Online-DPO (2025)

2025年新工作发现，Online DPO 的**采样策略**（如何从策略中采样训练数据）对效果影响巨大：

| 采样策略 | 核心思想 | 效果 |
|---------|---------|------|
| Best-of-N | 从 N 个样本中选奖励最高的 | 简单有效 |
| Rejection Sampling | 只保留高于阈值的样本 | 减少噪声 |
| Diverse Sampling | 最大化样本间多样性 | 改善泛化 |
| Self-Critique | 模型自己评估样本质量 | 无需外部 RM |

---

## 统一框架：所有对齐方法的分类

根据 [arxiv:2509.11298](https://arxiv.org/pdf/2509.11298)，所有偏好优化方法可以按以下维度分类：

### 按数据粒度

| 粒度 | 方法 |
|------|------|
| **Token-level** | TDPO, RTO |
| **Pairwise** | DPO, IPO, KTO, BCO, WPO, SimPO, ORPO, cDPO, rDPO, f-DPO, alpha-DPO, CPO, R-DPO |
| **Listwise** | ListNet, ListMLE, LambdaRank, RankNet, RRHF, SLiC-HF |
| **Group** | GRPO, RLOO, WPO |
| **Trajectory** | PPO-RLHF, ReMax |

### 按是否可约化（Reducible）

**可约化**（有闭式解，无需迭代优化）：
- DPO（基准）
- SPPO, Nash-MD, INPO, DNO, APO, RSO, XPO, cDPO, rDPO

**不可约化**（需要迭代，通常基于 RL）：
- GRPO, RLOO, WPO, KTO, BCO, RTO, PPO-RLHF, ReMax

### 按等价类

| 等价类 | 方法 | 共同哈希 |
|--------|------|---------|
| DPO 等价 | DPO, SPPO, Nash-MD, INPO, DNO, APO, RSO, XPO, cDPO, rDPO | 509dff3aee |
| SimPO/ORPO 等价 | SimPO, ORPO | dce2a41b55 |
| IPO 等价 | IPO, IPO-MD | e5ddaf1ff7 |

---

## 2025 新进展：EEPO（熵保持偏好优化）

### 问题：GRPO 的熵坍缩

GRPO（Group Relative Policy Optimization）在可验证奖励任务（数学、代码）上表现优异，但存在**熵快速坍缩**问题——策略迅速收敛到少数几个固定解法，丧失探索能力。

### EEPO 方案

港中文 2025年10月提出的 **EEPO（Entropy-Enhanced Preference Optimization）**：

1. **自适应触发**：只有当熵低于阈值时才启用，避免干扰正常探索
2. **互补损失**：更强惩罚"高概率"token，定向压制主导模式
3. **轻量高效**：只对 rollout 模型做一步更新，每轮从 policy 同步，遗忘仅当次生效

**效果**（相对 GRPO 提升）：
- Qwen2.5-3B：+24.3%
- Llama3.2-3B-Instruct：+33.0%
- Qwen3-8B-Base：+10.4%

**核心洞察**：只修改采样过程而不改变目标函数，通过"采样-然后-遗忘"打断自我强化循环。

---

## 实践选择指南

| 场景 | 推荐方法 | 理由 |
|------|---------|------|
| 有大量成对偏好数据 | DPO | 简单、稳定、效果好 |
| 偏好数据有限，怕过拟合 | IPO | 平方损失自带正则化 |
| 只有二元反馈（好/坏） | KTO | 数据需求最低 |
| 需要在线更新、实时反馈 | Online DPO / Online IPO | 数据新鲜，减少分布偏移 |
| 数学/代码等可验证任务 | GRPO + EEPO | 规则奖励 + 熵保持 |
| 追求理论统一性 | 统一框架（arxiv:2509.11298） | 根据归纳偏差选择等价类 |

---

## 与 Harness 方法论的关系

在 Agent 训练/推理框架（Harness）中，RLHF 变体的选择直接影响：

1. **Verifier 训练**：Online DPO/IPO 可用于训练 Verifier（判断 Agent 输出是否正确）
2. **Test-Time Compute**：KTO 的低数据需求适合快速微调特定任务的 Agent
3. **Self-Improvement Loop**：Online 方法天然支持 Agent 的自我迭代（生成 → 评估 → 更新）

---

## 引用

- [鹤啸九天：RLHF 原理及进化](https://wqw547243068.github.io/rlhf) — 中文最系统的 RLHF 教程，含 DPO/IPO/KTO 完整推导
- [arxiv:2509.11298](https://arxiv.org/pdf/2509.11298) — "A Unified Framework for Preference Optimization"，所有方法的等价类分类
- [OpenReview: Online IPO](https://openreview.net/pdf?id=G1R8Ns8n38) — Online IPO 的完整数学推导和实现细节
- [KTO: Model Alignment as Prospect Theoretic Optimization](https://arxiv.org/abs/2402.01306) — KTO 原始论文
- [DPO: Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — DPO 原始论文（2023）
- [EEPO 技术解读](https://wqw547243068.github.io/rlhf) — 港中文 2025，熵保持偏好优化
