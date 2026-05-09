# Test-Time Compute（测试时计算扩展）

**类型**：推理范式 / 模型性能优化策略  
**别名**：Inference-Time Compute / 推理时计算  
**核心思想**：**推理时多"想"一会，比训练更大模型更划算**

---

## 🧬 技术原理

### 核心洞察
传统 Scaling Law：
- **训练时扩展**：更大模型 + 更多数据 → 更好性能（但成本指数增长）
- **测试时扩展**：相同模型，推理时投入更多计算（多步思考、验证、搜索）→ 更好性能

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

## 🔑 技术方法

| 方法 | 原理 | 成本 | 效果 |
|------|------|------|------|
| **Chain-of-Thought** | 模型生成中间推理步骤 | 低（仅需Prompt） | 中等提升 |
| **Self-Consistency** | 多次采样，选多数答案 | 中（3-10次推理） | 稳定提升 |
| **Tree-of-Thought** | 多路径探索，评估后选择 | 高（分支搜索） | 大幅提示 |
| **Verifier/ORM** | 训练验证模型，筛选正确路径 | 高（需额外模型） | 精准提升 |
| **Process Reward Model** | 奖励每一步的正确性 | 高（细粒度标注） | 最佳效果 |

---

## 🚀 核心争议

### 1. "思考"vs"背诵"
- **支持方**：测试时计算让模型真正"推理"，而非 memorization
- **质疑方**：可能只是更长的 pattern matching，没有真正的抽象推理

### 2. 成本与延迟
- **o1/o3**：推理时间从几秒延长到几分钟
- **API定价**：o4-mini $1.10/$4.40 per 1M tokens vs GPT-4.5 $75/$150
- **权衡**：用户愿意为更好答案等更久吗？

### 3. 可解释性
- **优势**：思维链让模型"展示工作过程"，可审计
- **局限**：模型可能"编造"思维链（看起来合理但实际错误）

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| o1 vs GPT-4o数学提升 | AIME 2024: 12% → 83% | OpenAI |
| o3 ARC-AGI | 87.5%（接近人类水平） | OpenAI |
| 测试时计算成本 | 比训练同性能大模型低10-100倍 | 论文估计 |
| o4-mini定价 | $1.10/$4.40 per 1M tokens | OpenAI |

---

## 🔗 相关页面
- [entities/openai.md](../entities/openai.md) — o系列模型
- [entities/deepseek.md](../entities/deepseek.md) — R1推理模型
- [entities/moonshot.md](../entities/moonshot.md) — K2.5推理
- [entities/google-deepmind.md](../entities/google-deepmind.md) — Gemini Thinking

---

*最后更新：2026-05-09*  
*信息来源：OpenAI/Google/DeepSeek论文、arxiv.org*
