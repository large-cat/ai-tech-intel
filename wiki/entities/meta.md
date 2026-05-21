# Meta AI

**类型**：科技巨头AI部门  
**总部**：美国加州Menlo Park  
**关键人物**：Mark Zuckerberg（CEO）, Yann LeCun（首席AI科学家）, Joelle Pineau（VP AI Research）

---

## 🏛️ 时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 2013 | Yann LeCun加入Facebook（后Meta），创立FAIR（Facebook AI Research） | Meta官方 |
| 2016 | PyTorch开源发布，成为最流行的深度学习框架之一 | pytorch.org |
| 2019 | RoBERTa发布，BERT优化版本，多项NLP任务SOTA | arxiv.org |
| 2022 | OPT-175B发布，开源大模型先驱，与GPT-3对标 | arxiv.org |
| 2023-02 | LLaMA 1发布（65B参数），但"泄露"式开源引发争议 | arxiv.org |
| 2023-07 | LLaMA 2发布，真正开源商用，2万亿token训练 | ai.meta.com |
| 2024-04 | LLaMA 3发布（70B/400B参数），训练数据15万亿token | ai.meta.com |
| 2024-07 | Llama 3.1 405B发布，最大开源模型，对标GPT-4o | ai.meta.com |
| 2024-12 | **Ray-Ban Meta智能眼镜AI功能升级**，多模态Agent | Meta Connect |
| 2025-04 | **LLaMA 4发布**（405B参数），MMLU 88.2%，真正对标GPT-4o/Claude 3.5 | ai.meta.com |
| 2025-06 | **Meta AI内置到WhatsApp/Instagram/Facebook**，覆盖30亿+用户 | Meta官方 |
| 2025-09 | **Llama 4 Scout / Maverick发布**，多模态+工具调用 | ai.meta.com |
| 2026-01 | **Meta AI月活突破7亿**，成为全球最大AI产品之一 | Meta财报 |
| 2026-03 | Llama 4 Behemoth训练中（预计2T+参数），训练集群16万GPU | 供应链消息 |

---

## 🔑 关键模型矩阵

| 系列 | 定位 | 规模 | 特点 | 开源状态 |
|------|------|------|------|----------|
| LLaMA | 开源旗舰 | 405B (LLaMA 4) | 高性能、可商用 | **开源** |
| Llama Scout | 轻量多模态 | 17B | 端侧部署、工具调用 | **开源** |
| Llama Maverick | 中端多模态 | 400B | 平衡性能与效率 | **开源** |
| Llama Behemoth | 实验级 | 2T+（预计） | 研究前沿 | 待定 |

---

## 🚀 核心技术路线

### 1. 开源战略（Open Source AI）
- **Zuckerberg立场**："开源AI是未来的操作系统"
- **商业模式**：模型免费 → 云服务收费（AWS/Azure/ GCP部署）+ 广告变现
- **与OpenAI差异**：Meta走"开放生态"路线，OpenAI走"API变现"路线
- **社区影响**：Hugging Face上Llama系列下载量破亿，衍生模型数千个

### 2. LLaMA 4 技术亮点
- **MMLU**：88.2%（405B版本），与GPT-4、Claude 3.5相当
- **架构**：Dense Transformer（非MoE），15万亿token训练数据
- **多模态**：原生图像+文本理解，非后期拼接
- **工具调用**：内置function calling，支持外部API
- **HellaSwag**：95.3%（常识推理）

### 3. 端侧AI（On-Device AI）
- **Ray-Ban Meta眼镜**：多模态Agent，语音+视觉+实时翻译
- **Llama Scout（17B）**：专为手机/眼镜优化
- **与Apple竞争**：Meta的"AI眼镜" vs Apple Vision Pro

### 4. 算力基础设施
- **训练集群**：16万GPU（2026年，用于Behemoth训练）
- **与NVIDIA关系**：深度绑定，但也在探索自研芯片
- **能源消耗**：2025年宣布100亿美元数据中心投资

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| Meta AI月活用户 | 7亿+（2026年1月） | Meta财报 |
| LLaMA系列下载量 | 1亿+（Hugging Face） | Hugging Face |
| 训练数据规模 | 15万亿token（LLaMA 3/4） | ai.meta.com |
| GPU集群规模 | 16万（2026年Behemoth训练） | 供应链 |
| 开源模型衍生数量 | 数千个 | Hugging Face |

---

## 🔗 相关页面
- [concepts/harness-methodology.md](../concepts/harness-methodology.md) — Meta Agent策略
- [concepts/test-time-compute.md](../concepts/test-time-compute.md) — 推理技术对比
- [weekly-digest/2026-05-09.md](../weekly-digest/2026-05-09.md) — 首日记录

---

*最后更新：2026-05-09*  
*信息来源：ai.meta.com、Meta财报、arxiv.org、Hugging Face*
