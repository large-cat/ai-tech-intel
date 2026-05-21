# 闭源 vs 开源/中国模型厂商对比

> 对比类型：商业模式与技术路线
> 更新时间：2026-05
> 触发条件：新模型发布、license变更、市场份额变化

## 核心差异矩阵

| 维度 | 闭源阵营 (Anthropic/OpenAI/Google) | 开源/中国阵营 (Meta/DeepSeek/月之暗面) |
|------|--------------------------------------|----------------------------------------|
| **商业模式** | API订阅 + 企业授权 | 开源模型 + 云服务/API |
| **license** | 专有/限制性 | Apache/MIT/Modified MIT |
| **训练数据** | 不公开 | 部分公开或完全公开 |
| **推理成本** | 高（垄断定价） | 低（竞争驱动） |
| **生态控制** | 强（平台锁定） | 弱（去中心化） |
| **中国市场** | 受限/合规成本高 | 本土优势 |

## 具体厂商对比

### Anthropic vs 月之暗面

| 指标 | Anthropic | 月之暗面 (Moonshot) |
|------|-----------|---------------------|
| 旗舰模型 | Claude 4 | Kimi K2.5 |
| Agent能力 | Managed Agents (三Agent) | Agent Swarm (100子Agent) |
| 工具调用 | 复杂编排 | 1500+工具调用/轮 |
| 训练方法 | RLHF + Constitutional AI | PARL (Process-Adaptive RL) |
| License | 专有 | Modified MIT |
| 中国市场 | 不可用 | 本土部署 |

来源：[[anthropic-managed-agents]]、[[moonshot-kimi-k25]]

### OpenAI vs DeepSeek

| 指标 | OpenAI | DeepSeek |
|------|--------|----------|
| 旗舰模型 | GPT-5 / o4 | DeepSeek-V4 / R2 |
| 开源策略 | GPT-OSS-120B（部分） | 全开源 |
| 本地推理 | 有限支持 | ds4引擎（Flash推理） |
| 推理成本 | $$$ | $ |
| 架构 | MoE (117B总量/5.1B激活) | Dense/MoE混合 |

来源：[[karpathy-agentic-engineering-2026]]、[[ds4-github]]

## 2026年关键变量

1. **OpenAI开源动摇**：GPT-OSS-120B开源是否意味着闭源商业模式承压？
2. **中国厂商出海**：月之暗面、DeepSeek的海外扩张能力
3. **License博弈**：Modified MIT vs Apache 2.0的生态吸引力

---

*本对比基于 [[sources/moonshot-kimi-k25]]、[[sources/amd-mi450-vs-rubin]]（类比逻辑）等综合。*
