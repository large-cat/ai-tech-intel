# 2026年AI行业趋势综合综述

> 综合类型：年度趋势综述
> 覆盖实体：Anthropic, OpenAI, Google DeepMind, NVIDIA, AMD, 月之暗面, DeepSeek, Meta
> 覆盖概念：Harness方法论, 存算一体, HBM, Chiplet, Agent Skills, RLHF
> 更新策略：每月补充新信号，季度重写核心判断

## 核心判断

2026年AI行业的核心矛盾已经从**"谁的模型更强"**转向**"谁的Harness（Agent编排系统）更稳"**。这一范式转移同时被 Anthropic、OpenAI、Stripe、LangChain 验证。

### 范式转移的三重证据

| 证据来源 | 核心发现 | 来源链接 |
|---------|---------|---------|
| Anthropic | 三Agent架构（Plan-Execute-Verify）成为生产标准 | [[anthropic-three-agent-harness]] |
| OpenAI | 100万行生产代码零手写，GPT-OSS-120B开源 | [[openai-100m-lines]] |
| Stripe | Minions Blueprint：确定性×智能体混合，400+MCP | [[stripe-minions-blueprint]] |
| LangChain | Terminal Bench 2.0：模型不变Harness变 | [[langchain-terminal-bench]] |

## 两大技术主线

### 主线一：Agent工程化（软件层）

**从"会写代码的AI"到"会管理AI的工程师"**

- **Harness方法论**成为2026年核心范式，类比2010年代的DevOps
- **MCP协议**（Model Context Protocol）标准化Agent互操作
- **Agent Skills**生态爆发，GitHub上相关仓库前100名中Agent框架占比显著

### 主线二：存算一体（硬件层）

**从"更快GPU"到"重新设计内存墙"**

- HBM4进入量产，三星/Micron同时官宣出货
- Intel EMIB-T投产，先进封装市场翻倍至$50B
- 近存运算（Near-Memory Computing）最接近产品化

## 竞争格局变化

### 闭源阵营
- Anthropic：三Agent + Managed Agents，企业级Harness
- OpenAI：GPT-OSS-120B开源，MoE架构117B总量/5.1B激活参数
- Google：Gemini多模态，TPU v6

### 开源/中国阵营
- 月之暗面：Kimi K2.5，Agent Swarm 100子Agent，PARL训练
- DeepSeek：ds4本地推理引擎，V4 Flash
- Meta：Llama系列持续开源

## 待回答问题

- [ ] OpenAI开源策略是否会动摇闭源商业模式？
- [ ] HBM4产能瓶颈是否成为比芯片架构更重要的竞争壁垒？
- [ ] Agent Skills标准化何时到达临界点？

---

*本综述随新来源自动更新。关联来源见 [[知识编译索引]]。*
