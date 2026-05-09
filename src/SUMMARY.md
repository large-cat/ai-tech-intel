# Summary

[知识总图](README.md)

---

# 卷一：今日速递

- [2026年5月9日](digest/2026-05-09.md)

---

# 卷二：AI Agent 工程

## 第0层 · 前置知识

- [RLHF：让模型对齐人类偏好](agent-engineering/prereq/rlhf.md)
- [测试时计算：推理时多想一会](agent-engineering/prereq/test-time-compute.md)

## 第1层 · 根概念

- [Harness 方法论](agent-engineering/harness/README.md)

## 第2层 · 子概念

- [PEV 循环（Plan-Execute-Verify）](agent-engineering/harness/pev-cycle.md)
- [三Agent架构（Anthropic）](agent-engineering/harness/three-agent.md)
- [五层架构（行业共识）](agent-engineering/harness/five-layers.md)
- [Context Engineering](agent-engineering/harness/context-engineering.md)
- [Cognitive Memory > RAG](agent-engineering/harness/cognitive-memory.md)

## 第3层 · 实践案例

- [Anthropic：三Agent + Managed Agents](agent-engineering/practices/anthropic.md)
- [OpenAI：100万行零手写代码](agent-engineering/practices/openai.md)
- [Stripe Minions：确定性×智能体混合](agent-engineering/practices/stripe.md)
- [LangChain：模型不变Harness变](agent-engineering/practices/langchain.md)
- [月之暗面：Agent Swarm 100子Agent](agent-engineering/practices/moonshot.md)

## 第4层 · 工具与协议

- [MCP：模型控制协议](agent-engineering/tools/mcp.md)
- [LangGraph：状态管理图](agent-engineering/tools/langgraph.md)
- [E2B：安全Agent沙箱](agent-engineering/tools/e2b.md)
- [ADK：Google Agent套件](agent-engineering/tools/adk.md)

## 第5层 · 延伸概念

- [Agent Skills](agent-engineering/extended/agent-skills.md)

---

# 卷三：AI 硬件与芯片

## 第0层 · 前置知识

- [冯·诺依曼瓶颈](hardware/prereq/memory-wall.md)

## 第1层 · 根概念

- [存算一体](hardware/pim/README.md)
- [HBM：高带宽内存](hardware/hbm/README.md)
- [Chiplet：芯粒架构](hardware/chiplet/README.md)

## 第2层 · 子概念

### 存算一体的三个方向

- [近存运算（最接近产品化）](hardware/pim/near-memory.md)
- [存内计算（实验室→原型）](hardware/pim/compute-in-memory.md)
- [存内逻辑（早期研究）](hardware/pim/logic-in-memory.md)

### HBM 演进路线

- [HBM3E（当前主流）](hardware/hbm/hbm3e.md)
- [HBM4（2026H2）](hardware/hbm/hbm4.md)
- [HBM4E / HBM5（未来）](hardware/hbm/hbm4e.md)
- [cHBM：定制化HBM](hardware/hbm/chbm.md)

## 第3层 · 竞争格局

- [NVIDIA：Rubin + Feynman](hardware/competition/nvidia.md)
  - [Feynman：1.6nm + 硅光子](hardware/competition/nvidia-feynman.md)
  - [Rubin：HBM4 576GB](hardware/competition/nvidia-rubin.md)
- [AMD MI450：2nm工艺首次反超](hardware/competition/amd.md)
- [内存厂商：SK海力士 + 三星](hardware/competition/memory-vendors.md)

---

# 卷四：大模型厂商

## 闭源阵营

- [Anthropic](vendors/closed/anthropic.md)
- [OpenAI](vendors/closed/openai.md)
- [Google DeepMind](vendors/closed/google.md)

## 开源/中国阵营

- [月之暗面](vendors/open-source/moonshot.md)
- [DeepSeek](vendors/open-source/deepseek.md)
- [Meta](vendors/open-source/meta.md)

---

# 卷五：开源与人物

- [ds4：DeepSeek V4 Flash本地推理引擎](open-source/ds4.md)
- [值得关注的人物](people/README.md)

---

# 附录

- [LLM Wiki 知识库模式](appendix/pattern.md)
- [信息源与方法论](appendix/methodology.md)
- [完整实体索引](appendix/entities-index.md)
- [完整概念索引](appendix/concepts-index.md)
