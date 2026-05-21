# AI Tech Intel 知识问答系统

> 基于 llm-wiki 知识编译的中文 Q&A
> 覆盖领域：Agent工程、半导体硬件、模型厂商、开源生态
> 更新策略：新来源触发补充，用户提问驱动扩展

## 问答导航

### Agent 工程
- [什么是 Harness 方法论？](qa-harness-methodology.md)
- [Anthropic 的三Agent架构是什么？](qa-three-agent.md)
- [MCP 协议解决了什么问题？](qa-mcp-protocol.md)
- [Agent Skills 和 Function Calling 有什么区别？](qa-agent-skills.md)
- [Stripe Minions Blueprint 的核心创新是什么？](qa-stripe-minions.md)

### 半导体与硬件
- [HBM4 相比 HBM3E 有什么升级？](qa-hbm4-upgrade.md)
- [存算一体有哪三个方向？哪个最接近产品化？](qa-pim-directions.md)
- [AMD MI450 为什么能首次在工艺上反超 NVIDIA？](qa-amd-mi450.md)
- [先进封装市场为什么能在2026年翻倍到$50B？](qa-advanced-packaging.md)

### 模型厂商
- [2026年闭源和开源阵营的核心分歧是什么？](qa-closed-vs-open.md)
- [月之暗面 Kimi K2.5 的 Agent Swarm 有什么特别？](qa-kimi-k25.md)
- [OpenAI 开源 GPT-OSS-120B 意味着什么？](qa-openai-oss.md)
- [DeepSeek ds4 是什么？为什么重要？](qa-deepseek-ds4.md)

### 综合趋势
- [2026年AI行业的核心范式转移是什么？](qa-2026-paradigm.md)
- [Karpathy 的 CLAUDE.md 12条规则解决了什么问题？](qa-karpathy-rules.md)
- [RLHF 的新变体（DPO/IPO/KTO）各有什么优劣？](qa-rlhf-variants.md)

---

## 如何提问

如果你有问题不在列表中，可以直接提问。系统会：
1. 搜索现有知识库中的相关来源
2. 基于 [[知识编译索引]] 定位相关实体和概念
3. 生成回答并记录到本问答系统
4. 如果发现知识缺口，自动创建调研任务

---

*本问答系统基于 knowledge-compiler/graph.jsonld 和 190条交叉引用构建。*
