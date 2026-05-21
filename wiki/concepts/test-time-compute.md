# Test-Time Compute（测试时计算扩展）

**类型**：推理范式 / 模型性能优化策略  
**别名**：Inference-Time Compute / 推理时计算  
**核心思想**：**推理时多"想"一会，比训练更大模型更划算**

---

## 🧬 技术原理深度版

### 核心洞察：Scaling Law 的两个维度

传统 Scaling Law 只关注**训练时扩展**（Train-Time Scaling）：
$$L(N, D) \propto \frac{1}{N^{0.34}} + \frac{1}{D^{0.28}}$$
其中 $N$ = 模型参数，$D$ = 训练token数。

测试时计算扩展（Test-Time Scaling）发现：
- 固定模型 $N$，增加推理时计算量 $C_{test}$（更多推理步骤/验证/搜索）
- 性能提升曲线与训练更大模型相当，但**成本更低**

**关键公式**（来源：`arxiv.org/pdf/2505.18065`）：
$$P(\text{correct}) = f(C_{test}) \approx \frac{C_{test}^\alpha}{C_{test}^\alpha + C_0^\alpha}$$
其中 $\alpha \approx 0.3-0.5$（任务相关），$C_0$ 为饱和常数。

### OpenAI的验证

- **o1模型**：推理时生成"思维链"（Chain-of-Thought），多步验证
- **o3/o4**：进一步增加推理步骤，性能持续提升
- **关键发现**：测试时计算扩展的"性价比"高于训练时扩展

---

## 🏛️ 发展时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 2022 | Chain-of-Thought Prompting论文：让模型"一步步想" | arxiv.org |
| 2023 | "Let's Verify Step by Step"：逐步验证提升数学推理 | OpenAI |
| 2024-09 | **OpenAI o1-preview发布**，测试时计算扩展首次产品化 | OpenAI |
| 2024-12 | **o3发布**，ARC-AGI基准突破，证明扩展极限远未到达 | OpenAI |
| 2025-01 | **o3-mini发布**，低成本推理模型，普及测试时计算 | OpenAI |
| 2025-04 | **Google Gemini 2.5 Flash Thinking**发布，跟进测试时计算 | Google |
| 2025-06 | **DeepSeek-R1**证明纯RL也能获得推理能力（无需人类思维链） | DeepSeek |
| 2026-04 | **o4-mini发布**，测试时计算进一步成本优化 | OpenAI |
| 2026-04 | **月之暗面K2.5**跟进推理增强，测试时计算成为行业标配 | Moonshot |

---

## 🔑 技术方法深度版

### 1. Chain-of-Thought（CoT）基础版

**原理**：在Prompt中加入"Let's think step by step"，强制模型生成中间推理步骤。

**数学本质**：
$$P(y|x) = \sum_{r} P(y|r, x) P(r|x)$$
其中 $r$ 是推理路径（reasoning path），通过显式生成 $r$ 将联合分布分解。

**成本**：低（仅需Prompt修改，不增加推理次数）
**效果**：中等提升（GSM8K +15-20%）

---

### 2. Self-Consistency（自一致性）

**原理**：多次采样生成多个CoT路径，选多数答案（投票机制）。

**数学**：
$$\hat{y} = \arg\max_y \sum_{i=1}^{K} \mathbb{1}[y_i = y]$$
其中 $K$ = 采样次数（通常 5-40），$y_i$ = 第 $i$ 次采样的最终答案。

**成本**：中（$K$ 次独立推理）
**效果**：稳定提升（数学推理 +10-15%，比单路CoT更鲁棒）

---

### 3. Best-of-N 搜索

**原理**：生成 $N$ 个完整回答，用**验证器（Verifier）**打分，选最高分。

**数学**：
$$\hat{y} = \arg\max_{i \in [1,N]} V(x, y_i)$$
其中 $V(\cdot)$ 是验证器模型（ORM - Outcome Reward Model）。

**验证器训练**：
$$\mathcal{L}_{ORM} = -\mathbb{E}_{(x, y, c) \sim D} [c \log \sigma(V(x, y)) + (1-c) \log(1 - \sigma(V(x, y)))]$$
其中 $c \in \{0, 1\}$ 是二元正确标签。

**成本**：高（$N$ 次完整推理 + 验证器推理）
**效果**：大幅提升（AIME 2024: 基线 12% → Best-of-64: 83%）

---

### 4. Process Reward Model（PRM，过程奖励模型）

**原理**：不仅验证最终答案，还**奖励每一步的正确性**。

**数学**：
$$R_{PRM} = \sum_{t=1}^{T} r_t(s_t)$$
其中 $s_t$ 是第 $t$ 步状态，$r_t(s_t)$ 是该步的奖励（由PRM预测）。

**PRM训练目标**：
$$\mathcal{L}_{PRM} = -\sum_{t} \mathbb{E}_{(x, s_t, c_t)} [c_t \log \sigma(\phi(s_t)) + (1-c_t) \log(1 - \sigma(\phi(s_t)))]$$
其中 $\phi(s_t)$ 是PRM对步骤 $t$ 正确性的logit预测，$c_t \in \{0, 1\}$ 是人工标注的步骤级标签。

**关键洞察**：
- ORM（Outcome RM）只能告诉你"最终对不对"
- PRM能告诉你"第3步错了，从那里重试"
- **PRM指导的搜索** = Beam Search + 步骤级剪枝

**成本**：最高（需要大量步骤级人工标注训练PRM）
**效果**：最佳（AIME 2024: 基线 12% → PRM+BeamSearch: 90%+）

---

### 5. Tree-of-Thought（ToT）

**原理**：多路径并行探索，每步评估后保留Top-k最有希望的分支。

**算法**（来源：`arxiv.org/abs/2305.10601`）：
```
1. 生成候选步骤（Branching Factor = b）
2. 对每个候选，PRM打分
3. 保留 Top-k 最高分候选
4. 对每个保留候选，递归生成下一步
5. 到达终止条件时，选全局最高分的完整路径
```

**复杂度**：$O(b \cdot k \cdot d)$，其中 $d$ = 推理深度。

**与PRM结合**：ToT用PRM作为启发函数指导Beam Search，类似AlphaGo的MCTS。

---

### 6. 验证器类型对比

| 验证器 | 监督粒度 | 训练成本 | 推理成本 | 效果 |
|--------|----------|----------|----------|------|
| **ORM** | 结果级（对/错） | 低 | 每回答1次 | 中 |
| **PRM** | 步骤级（每步对/错） | **高**（需步骤标注） | 每步1次 | **最高** |
| **LLM-as-Judge** | 文本级（自然语言评分） | 无（零样本） | 每回答1次 | 中（不稳定） |

---

## 🚀 核心争议

### 1. "思考"vs"背诵"
- **支持方**：测试时计算让模型真正"推理"，而非 memorization
- **质疑方**：可能只是更长的 pattern matching，没有真正的抽象推理
- **证据**：o3在ARC-AGI上达到87.5%（接近人类），但分布外泛化仍有限

### 2. 成本与延迟
- **o1/o3**：推理时间从几秒延长到几分钟
- **API定价**：o4-mini $1.10/$4.40 per 1M tokens vs GPT-4.5 $75/$150
- **权衡**：用户愿意为更好答案等更久吗？
- **经济学**：测试时计算成本比训练同性能大模型低 **10-100倍**

### 3. 可解释性
- **优势**：思维链让模型"展示工作过程"，可审计
- **局限**：模型可能"编造"思维链（看起来合理但实际错误）
- **伪造检测**：训练PRM时加入"思维链一致性"作为辅助任务

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| o1 vs GPT-4o数学提升 | AIME 2024: 12% → 83% | OpenAI |
| o3 ARC-AGI | 87.5%（接近人类水平） | OpenAI |
| 测试时计算成本优势 | 比训练同性能大模型低10-100倍 | 论文估计 [来源：arxiv.org/pdf/2505.18065] |
| o4-mini定价 | $1.10/$4.40 per 1M tokens | OpenAI |
| Self-Consistency K值 | 5-40次采样（成本与K线性） | 论文实践 |
| PRM步骤标注成本 | ~$50K/1000题（人工逐步验证） | OpenAI "Let's Verify Step by Step" |
| Best-of-64效果 | AIME 2024: 12% → 83% | OpenAI o1技术报告 |
| PRM+BeamSearch效果 | AIME 2024: 12% → 90%+ | OpenAI o1技术报告 |

---

## 🔗 相关页面
- [entities/openai.md](../entities/openai.md) — o系列模型
- [entities/deepseek.md](../entities/deepseek.md) — R1推理模型
- [entities/moonshot.md](../entities/moonshot.md) — K2.5推理
- [entities/google-deepmind.md](../entities/google-deepmind.md) — Gemini Thinking
- [concepts/rlhf.md](rlhf.md) — PRM训练依赖RLHF技术

---

*最后更新：2026-05-12*  
*信息来源：OpenAI o1/o3技术报告, "Let's Verify Step by Step" (arxiv.org), DeepSeek-R1论文, "Reward Model Generalization for Compute-Aware Test-Time Reasoning" (arxiv.org/pdf/2505.18065), Google Gemini 2.5 Flash Thinking*