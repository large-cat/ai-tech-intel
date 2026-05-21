# Google DeepMind

**类型**：模型厂商 / 科技巨头AI部门  
**总部**：英国伦敦（DeepMind）+ 美国加州（Google Brain）  
**关键人物**：Demis Hassabis（CEO, 2024诺奖得主）, Jeff Dean（Google首席科学家）, Oriol Vinyals, Koray Kavukcuoglu

---

## 🏛️ 时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 2010 | DeepMind在伦敦成立，由Demis Hassabis等人创立 | deepmind.com |
| 2014 | 被Google以4亿英镑收购 | Google官方 |
| 2016-03 | AlphaGo击败李世石，AI里程碑事件 | Nature |
| 2017-10 | AlphaZero：自我对弈学习围棋/国际象棋/将棋 | Science |
| 2018-12 | AlphaFold诞生，蛋白质结构预测突破 | CASP12 |
| 2021 | Google Brain发布Switch Transformer（1.6T参数MoE） | arxiv.org |
| 2022-04 | PaLM（540B参数）发布，few-shot学习里程碑 | arxiv.org |
| 2022-07 | AlphaFold2开源，预测2亿+蛋白质结构 | Nature |
| 2023-03 | Google Brain + DeepMind合并为Google DeepMind | Google官方 |
| 2023-12 | Gemini 1.0发布，原生多模态（文本+图像+音频+视频） | deepmind.google |
| 2024-02 | Gemini 1.5 Pro发布，100万token上下文窗口 | deepmind.google |
| 2024-12 | Gemini 2.0 Flash发布，速度最快的一代 | deepmind.google |
| 2025-01 | AlphaFold3发布，预测所有生物分子结构 | Nature |
| 2025-03 | Gemini 2.5 Pro发布，推理能力大幅提升 | deepmind.google |
| 2025-04 | **Gemini 2.5 Ultra发布**，多模态+推理双冠王 | deepmind.google |
| 2026-02 | **Willow量子芯片发布**，5分钟完成超算10^25年的计算 | Google博客 |
| 2026-04 | Gemini 2.5 Flash更新，TPU v6p大规模部署 | deepmind.google |

---

## 🔑 关键模型矩阵

| 系列 | 定位 | 特点 | 最新版本 | 开源状态 |
|------|------|------|----------|----------|
| Gemini | 通用多模态 | 原生多模态架构 | Gemini 2.5 Ultra | 闭源（API） |
| AlphaFold | 科学计算 | 蛋白质/分子结构预测 | AlphaFold3 | **开源** |
| Gemma | 开源模型 | 轻量可部署 | Gemma 3 27B | **开源** |

---

## 🚀 核心技术路线

### 1. 原生多模态（Native Multimodality）
- **与GPT-4o的差异**：Gemini从训练阶段就是多模态，而非后期拼接
- **2.5 Ultra能力**：文本+图像+音频+视频统一推理，视频理解业界领先
- **关键突破**：2024年Gemini 1.5 Pro实现100万token上下文，2025年扩展至200万

### 2. AlphaFold系列（科学AI）
- **AlphaFold2（2021）**：蛋白质结构预测，开源，预测2亿+结构
- **AlphaFold3（2025）**：扩展到DNA/RNA/小分子/蛋白质复合物
- **社会影响**：被190个国家/地区的200万+研究人员使用
- **2024诺奖**：Demis Hassabis和John Jumper获诺贝尔化学奖

### 3. TPU（张量处理单元）
- **TPU v5p**：2023年发布，用于Gemini 1.0训练
- **TPU v6e/v6p**：2025-2026年部署，能效比大幅提升
- **与NVIDIA竞争**：Google自用为主，云服务器对外提供
- **Willow量子芯片**：2026年2月发布，用于量子计算纠错

### 4. Gemini 2.5 Ultra 技术亮点
- **MMLU**：87.8%（多模态理解）
- **MMMU**：75.6%（大学级多模态推理）
- **Video Understanding**：长视频（1小时+）内容理解业界最强
- **Context Window**：200万token（约3000页PDF）

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| AlphaFold使用国家 | 190+ | DeepMind官方 |
| AlphaFold预测结构 | 2亿+蛋白质 | DeepMind官方 |
| Gemini API开发者 | 数百万 | Google官方 |
| Gemma下载量 | 数千万 | Hugging Face/Kaggle |
| Willow量子芯片 | 105个物理量子比特 | Google博客 |

---

## 🔗 相关页面
- [concepts/harness-methodology.md](../concepts/harness-methodology.md) — 对比Google Agent策略
- [concepts/test-time-compute.md](../concepts/test-time-compute.md) — 测试时计算扩展
- [concepts/processing-in-memory.md](../concepts/processing-in-memory.md) — Google 3D-DRAM chiplet专利
- [weekly-digest/2026-05-09.md](../weekly-digest/2026-05-09.md) — 首日记录

---

*最后更新：2026-05-09*  
*信息来源：deepmind.google、Google博客、Nature、arxiv.org*
