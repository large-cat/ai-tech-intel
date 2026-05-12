# RLHF（人类反馈强化学习）

**类型**：训练方法 / 对齐技术  
**全称**：Reinforcement Learning from Human Feedback  
**核心作用**：让LLM"学会"人类的偏好和价值观

---

## 🧬 技术原理深度版

### 三步流程

1. **预训练（Pre-training）**：海量文本自监督学习，模型学会语言规律
2. **SFT（Supervised Fine-Tuning）**：人类编写的"理想回答"训练，模型学会格式
3. **RLHF**：人类比较两个回答哪个更好 → 训练Reward Model → 用PPO算法优化策略

### 为什么需要RLHF？

- **SFT的局限**：人类标注成本高，模型只是"模仿"而非"理解"偏好
- **RLHF的突破**：让模型主动学习"什么回答人类更喜欢"
- **应用**：减少有害输出、提升 helpfulness、对齐人类价值观

---

## 🏛️ 发展时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 2017 | OpenAI首次提出RLHF概念，用于游戏和机器人 | OpenAI博客 |
| 2020 | "Learning to Summarize from Human Feedback"论文 | arxiv.org |
| 2022-03 | InstructGPT发布，RLHF首次用于LLM对齐 | OpenAI论文 |
| 2022-11 | ChatGPT发布，RLHF成为行业标配 | OpenAI |
| 2023 | Claude、Llama 2等全面采用RLHF | 各厂商 |
| 2024 | **DPO（Direct Preference Optimization）**兴起，简化RLHF流程 | arxiv.org |
| 2025 | **RLAIF（AI Feedback）**：用AI替代人类标注，降低成本 | Google/Anthropic |
| 2026 | **DeepSeek-R1纯RL路线**：无需SFT，直接用RL训练推理能力 | DeepSeek |

---

## 🔑 关键变体方法深度版

### 1. PPO-RLHF（经典路线）

**完整流程**：
```
SFT模型（π_SFT） → 人类比较数据 → 训练Reward Model（r_θ） → PPO优化 → RLHF模型（π_RL）
```

**Reward Model训练**：
给定偏好对 $(x, y_w, y_l)$（$y_w$ = 人类偏好的回答，$y_l$ = 较差的回答）：
$$\mathcal{L}_R(r_\theta, D) = -\mathbb{E}_{(x, y_w, y_l) \sim D} \left[ \log \sigma\left( r_\theta(x, y_w) - r_\theta(x, y_l) \right) \right]$$
其中 $\sigma$ 是sigmoid函数。$r_\theta(x, y)$ 输出标量奖励值。

**PPO优化目标**：
$$\mathcal{L}^{CLIP}(\theta) = \mathbb{E}_t \left[ \min\left( r_t(\theta) \hat{A}_t, \text{clip}\left(r_t(\theta), 1-\epsilon, 1+\epsilon\right) \hat{A}_t \right) \right]$$
其中：
- $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{old}}(a_t|s_t)}$：新旧策略概率比
- $\hat{A}_t$：优势函数估计（GAE - Generalized Advantage Estimation）
- $\epsilon = 0.2$：裁剪阈值，防止策略突变

**KL散度约束**：
为了防止RL模型偏离SFT模型太远，加入KL惩罚：
$$\mathcal{L}_{total} = \mathcal{L}^{CLIP} - \beta \cdot \mathbb{E}\left[ \text{KL}(\pi_\theta \| \pi_{SFT}) \right]$$
其中 $\beta$ 是KL系数（通常 0.01-0.1）。

**PPO的超参数**：
| 参数 | 典型值 | 作用 |
|------|--------|------|
| $\epsilon$ (clip) | 0.2 | 限制策略更新幅度 |
| $\beta$ (KL coef) | 0.01-0.1 | 防止RL模型偏离SFT太远 |
| $\gamma$ (discount) | 0.99 | 未来奖励折扣因子 |
| $\lambda$ (GAE) | 0.95 | GAE权衡参数 |
| learning rate | 1e-6 ~ 1e-5 | 极小的学习率防止崩溃 |
| batch size | 64-512 | 每个PPO batch的样本数 |

---

### 2. DPO（Direct Preference Optimization）

**核心洞察**：PPO需要训练Reward Model + 4个模型（Policy、Reference、Reward、Value），DPO证明可以直接从偏好数据优化策略，**无需显式Reward Model**。

**数学推导**：

从Bradley-Terry偏好模型出发：
$$P(y_w \succ y_l | x) = \sigma\left( r^*(x, y_w) - r^*(x, y_l) \right)$$

隐式Reward Model（由策略和参考模型导出）：
$$r(x, y) = \beta \log \frac{\pi_\theta(y|x)}{\pi_{ref}(y|x)}$$

**DPO损失函数**：
$$\mathcal{L}_{DPO}(\pi_\theta; \pi_{ref}) = -\mathbb{E}_{(x, y_w, y_l) \sim D} \left[ \log \sigma\left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)} \right) \right]$$

其中：
- $\pi_\theta$：正在训练的策略模型
- $\pi_{ref}$：固定的参考模型（通常是SFT模型）
- $\beta$：温度系数（控制与参考模型的偏离程度，越大越接近参考模型）
- $D$：偏好数据集

**DPO vs PPO 对比**：

| 维度 | PPO | DPO |
|------|-----|-----|
| 模型数量 | 4个（Policy + Reference + Reward + Value） | **2个**（Policy + Reference） |
| 训练流程 | 分阶段（先训Reward Model，再PPO） | **端到端**（一步完成） |
| 训练速度 | 慢（需要在线采样+价值估计） | **快2-3倍**（离线直接优化） |
| 稳定性 | 需调参（学习率、KL系数敏感） | 较稳定 |
| 效果 | 上限高（显式奖励信号） | 略低于PPO上限（隐式奖励） |
| 代表模型 | GPT-4、Claude 3 | Llama 2、Mistral |

---

### 3. GRPO（Group Relative Policy Optimization）

**来源**：DeepSeek-R1 / DeepSeekMath 论文

**核心创新**：PPO需要训练**价值模型（Value Model）**来估计优势函数，GRPO用**组内对比**替代价值模型，大幅减少显存和计算开销。

**GRPO工作流程**：

1. 对同一问题 $x$，从当前策略采样 $G$ 个回答：$\{y_1, y_2, ..., y_G\}$
2. 用Reward Model给每个回答打分：$\{r_1, r_2, ..., r_G\}$
3. 计算组内相对优势（无需价值模型）：
   $$\hat{A}_i = \frac{r_i - \text{mean}(\{r_j\})}{\text{std}(\{r_j\})}$$
4. 使用PPO-clip优化策略：
   $$\mathcal{L}_{GRPO} = \frac{1}{G} \sum_{i=1}^{G} \min\left( r_i(\theta) \hat{A}_i, \text{clip}(r_i(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_i \right) - \beta \cdot \text{KL}(\pi_\theta \| \pi_{ref})$$

**GRPO优势**：
| 对比项 | PPO | GRPO |
|--------|-----|------|
| 价值模型 | ❌ 需要（训练成本高） | ✅ **不需要** |
| 显存占用 | 大（4个模型加载） | **小**（2个模型） |
| 采样效率 | 每样本独立采样 | **组采样**（G个回答共享同一prompt） |
| 训练速度 | 慢 | **快**（减少价值模型前向/反向传播） |
| 适用场景 | 通用对齐 | **推理训练**（数学/代码） |

**DeepSeek-R1的关键突破**：
- **完全跳过SFT**，直接从基础模型开始GRPO训练
- 结果：推理能力（数学/代码）直接涌现
- 代价：通用对话能力需后续SFT补充（R1-Zero → R1）

---

### 4. RLAIF（AI Feedback替代人类）

**原理**：用AI（而非人类）生成偏好标注，降低成本。

Google的Constitutional AI方法：
1. 让AI生成回答
2. 让AI根据"宪法原则"（Constitution）自我批评
3. 用AI生成的批评作为偏好信号训练DPO

**成本降低**：70%+（无需人工标注员）
**局限**：AI反馈质量取决于基础模型能力（Garbage in, garbage out）

---

### 5. 多模态RLHF

**Gemini 2.5**：图像+文本+视频的联合偏好学习
**挑战**：多模态偏好标注更复杂，成本更高
**解决**：RLAIF扩展——用多模态模型自动生成跨模态偏好对

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| InstructGPT人类标注成本 | 数百万美元 | OpenAI论文 |
| DPO训练时间 | 比PPO快2-3倍 | 论文 [来源：arxiv.org/abs/2305.18290] |
| R1纯RL训练成本 | 远低于传统RLHF | DeepSeek |
| RLAIF降低标注成本 | 70%+ | Google论文 |
| GRPO显存节省 | ~50%（去掉价值模型） | DeepSeek-R1论文 |
| GRPO组大小G | 4-16 | DeepSeekMath实践 |
| PPO裁剪阈值ε | 0.2 | 标准值 |
| DPO温度系数β | 0.1-0.5 | 论文实践 |

---

## 🔗 相关页面
- [entities/openai.md](../entities/openai.md) — InstructGPT/ChatGPT
- [entities/deepseek.md](../entities/deepseek.md) — R1纯RL路线
- [entities/anthropic.md](../entities/anthropic.md) — Constitutional AI
- [concepts/harness-methodology.md](harness-methodology.md) — Agent对齐
- [concepts/test-time-compute.md](test-time-compute.md) — PRM依赖RLHF训练

---

*最后更新：2026-05-12*  
*信息来源：OpenAI InstructGPT论文, DeepSeek-R1论文, "Direct Preference Optimization" (arxiv.org/abs/2305.18290), "DeepSeekMath" (arxiv.org), Google Constitutional AI*