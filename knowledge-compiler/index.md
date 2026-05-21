# 知识编译索引 (Knowledge Compiler Index)

> 自动生成于 2026-05-21 10:28:37 | 版本 v2.0
> 基于 llm-wiki 模式：sources → entities → concepts → syntheses → comparisons → questions

## 📚 目录结构（知识树骨架）

```
wiki/
├── sources/          # 原始资料来源
├── entities/         # 实体档案
├── concepts/         # 技术概念
├── syntheses/        # 综合综述
├── comparisons/      # 对比分析
├── questions/        # 知识问答（中文Q&A）
├── digest/           # 每日速递
├── weekly-digest/    # 每周摘要
├── knowledge-compiler/  # 知识编译输出
│   ├── index.md      # 本索引
│   ├── graph.jsonld  # 机器可读图谱
│   └── stats.json    # 统计数据
└── src/              # mdBook 阅读层
```

## 🔗 交叉引用映射（目录 → 内容页码）

### 实体档案被引用来源

#### Addy Osmani (`entities/addy-osmani.md`)

**被 1 篇来源引用：**
- [Agent Skills - GitHub仓库分析](sources/agent-skills-github.md)

#### AMD (`entities/amd.md`)

**被 6 篇来源引用：**
- [Untitled](sources/nvidia-rubin-platform.md)
- [Chiplet 互连技术 2026：UCIe、HBM4 与封装拐点](sources/chiplet-interconnect-2026.md)
- [EDA 厂商竞逐台积电埃米时代路线图（2026 TSMC Symposium）](sources/eda-vendors-tsmc-2026.md)
- [AMD MI450 vs NVIDIA Rubin 竞争分析](sources/amd-mi450-vs-rubin.md)
- [Intel EMIB-T 与先进封装代工战略](sources/intel-emib-t-advanced-packaging.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)

#### Andrej Karpathy (`entities/andrej-karpathy.md`)

**被 4 篇来源引用：**
- [12-Factor Agents 工程原则深度解析](sources/12-factor-agents-humanlayer.md)
- [Karpathy Agentic Engineering 深度分析](sources/karpathy-agentic-engineering-2026.md)
- [GitHub AI 仓库排名追踪（2026-05-12 快照）](sources/github-ai-ranking-2026-05.md)
- [Karpathy CLAUDE.md 12条规则升级版](sources/karpathy-claude-md-12-rules.md)

#### Anthropic (`entities/anthropic.md`)

**被 12 篇来源引用：**
- [MCP Sampling Loop 技术深度解析](sources/mcp-sampling-loop-deep-dive.md)
- [GitHub Trending Weekly 2026-03-25 — Agent Skills Ecosystem Explosion](sources/github-trending-2026-03-25.md)
- [12-Factor Agents 工程原则深度解析](sources/12-factor-agents-humanlayer.md)
- [Untitled](sources/anthropic-three-agent-harness.md)
- [Stripe Minions Blueprint 架构详解](sources/stripe-minions-blueprint.md)
- [Untitled](sources/anthropic-managed-agents.md)
- [LangChain Terminal Bench 2.0 Harness优化详解](sources/langchain-terminal-bench-20.md)
- [月之暗面 Kimi K2.5 深度分析](sources/moonshot-kimi-k25.md)
- [AMD MI450 vs NVIDIA Rubin 竞争分析](sources/amd-mi450-vs-rubin.md)
- [Karpathy Agentic Engineering 深度分析](sources/karpathy-agentic-engineering-2026.md)
- [GitHub AI 仓库排名追踪（2026-05-12 快照）](sources/github-ai-ranking-2026-05.md)
- [Karpathy CLAUDE.md 12条规则升级版](sources/karpathy-claude-md-12-rules.md)

#### antirez (Salvatore Sanfilippo) (`entities/antirez.md`)

**被 2 篇来源引用：**
- [Harness Verifier Model 训练方法与多 Agent 容错架构深度调研](sources/harness-verifier-training-2026.md)
- [ds4 - GitHub仓库分析](sources/ds4-github.md)

#### DeepSeek (`entities/deepseek.md`)

**被 5 篇来源引用：**
- [月之暗面 Kimi K2.5 深度分析](sources/moonshot-kimi-k25.md)
- [ds4 - GitHub仓库分析](sources/ds4-github.md)
- [PRM 训练数据构建与 Test-Time Compute 自适应预算分配深度调研](sources/prm-adaptive-test-time-compute-2026.md)
- [小红书 AI 战略深度追踪](sources/xiaohongshu-ai-strategy-2026.md)
- [GitHub AI 仓库排名追踪（2026-05-12 快照）](sources/github-ai-ranking-2026-05.md)

#### Google DeepMind (`entities/google-deepmind.md`)

**被 14 篇来源引用：**
- [MCP Sampling Loop 技术深度解析](sources/mcp-sampling-loop-deep-dive.md)
- [台积电 CoWoS 产能目标上调（2026-2027）](sources/tsmc-cowos-capacity-2026-2027.md)
- [Chiplet 互连技术 2026：UCIe、HBM4 与封装拐点](sources/chiplet-interconnect-2026.md)
- [EDA 厂商竞逐台积电埃米时代路线图（2026 TSMC Symposium）](sources/eda-vendors-tsmc-2026.md)
- [近存计算（Near-Memory Computing）商业化全景 2026](sources/near-memory-computing-commercialization.md)
- [LangChain Terminal Bench 2.0 Harness优化详解](sources/langchain-terminal-bench-20.md)
- [AMD MI450 vs NVIDIA Rubin 竞争分析](sources/amd-mi450-vs-rubin.md)
- [Harness Engineering: 从 Prompt → Context → Harness 的认知升级](sources/harness-engineering-huxiu-2026-03-13.md)
- [Karpathy Agentic Engineering 深度分析](sources/karpathy-agentic-engineering-2026.md)
- [小红书 AI 战略深度追踪](sources/xiaohongshu-ai-strategy-2026.md)
- [Intel EMIB-T 与先进封装代工战略](sources/intel-emib-t-advanced-packaging.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)
- [GitHub AI 仓库排名追踪（2026-05-12 快照）](sources/github-ai-ranking-2026-05.md)
- [Karpathy CLAUDE.md 12条规则升级版](sources/karpathy-claude-md-12-rules.md)

#### Intel (`entities/intel.md`)

**被 9 篇来源引用：**
- [HBM4/5 路线图与产业格局重构（2026-2027）](sources/hbm4-5-roadmap-2026.md)
- [Chiplet 互连技术 2026：UCIe、HBM4 与封装拐点](sources/chiplet-interconnect-2026.md)
- [Applied Materials 收购 ASMPT NEXX（面板级先进封装沉积设备）](sources/applied-materials-nexx-acquisition-2026-05-03.md)
- [近存计算（Near-Memory Computing）商业化全景 2026](sources/near-memory-computing-commercialization.md)
- [Intel EMIB-T Enters Production Fab Rollout in 2026 — Tom's Hardware](sources/intel-emib-t-production-2026.md)
- [小红书 AI 战略深度追踪](sources/xiaohongshu-ai-strategy-2026.md)
- [Intel EMIB-T 与先进封装代工战略](sources/intel-emib-t-advanced-packaging.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)

#### LangChain (`entities/langchain.md`)

**被 5 篇来源引用：**
- [Blueprint for a Modern Agentic Harness in 2026 (Gist Summary)](sources/modern-harness-blueprint-2026.md)
- [LangChain Terminal Bench 2.0 Harness优化详解](sources/langchain-terminal-bench-20.md)
- [Harness Engineering: 从 Prompt → Context → Harness 的认知升级](sources/harness-engineering-huxiu-2026-03-13.md)
- [Karpathy Agentic Engineering 深度分析](sources/karpathy-agentic-engineering-2026.md)
- [GitHub AI 仓库排名追踪（2026-05-12 快照）](sources/github-ai-ranking-2026-05.md)

#### Meta AI (`entities/meta.md`)

**被 5 篇来源引用：**
- [台积电 CoWoS 产能目标上调（2026-2027）](sources/tsmc-cowos-capacity-2026-2027.md)
- [Harness Verifier Model 训练方法与多 Agent 容错架构深度调研](sources/harness-verifier-training-2026.md)
- [月之暗面 Kimi K2.5 深度分析](sources/moonshot-kimi-k25.md)
- [AMD MI450 vs NVIDIA Rubin 竞争分析](sources/amd-mi450-vs-rubin.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)

#### Micron (`entities/micron.md`)

**被 4 篇来源引用：**
- [HBM4/5 路线图与产业格局重构（2026-2027）](sources/hbm4-5-roadmap-2026.md)
- [Samsung and Micron Start Shipping HBM4 — The Register](sources/samsung-micron-hbm4-shipping-2026.md)
- [Applied Materials 收购 ASMPT NEXX（面板级先进封装沉积设备）](sources/applied-materials-nexx-acquisition-2026-05-03.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)

#### 月之暗面 (Moonshot AI) (`entities/moonshot.md`)

**被 2 篇来源引用：**
- [月之暗面 Kimi K2.5 深度分析](sources/moonshot-kimi-k25.md)
- [GitHub AI 仓库排名追踪（2026-05-12 快照）](sources/github-ai-ranking-2026-05.md)

#### NVIDIA (`entities/nvidia.md`)

**被 11 篇来源引用：**
- [HBM4/5 路线图与产业格局重构（2026-2027）](sources/hbm4-5-roadmap-2026.md)
- [Samsung and Micron Start Shipping HBM4 — The Register](sources/samsung-micron-hbm4-shipping-2026.md)
- [台积电 CoWoS 产能目标上调（2026-2027）](sources/tsmc-cowos-capacity-2026-2027.md)
- [Untitled](sources/nvidia-rubin-platform.md)
- [Chiplet 互连技术 2026：UCIe、HBM4 与封装拐点](sources/chiplet-interconnect-2026.md)
- [EDA 厂商竞逐台积电埃米时代路线图（2026 TSMC Symposium）](sources/eda-vendors-tsmc-2026.md)
- [近存计算（Near-Memory Computing）商业化全景 2026](sources/near-memory-computing-commercialization.md)
- [Untitled](sources/nvidia-feynman-gtc2026.md)
- [AMD MI450 vs NVIDIA Rubin 竞争分析](sources/amd-mi450-vs-rubin.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)

#### OpenAI (`entities/openai.md`)

**被 14 篇来源引用：**
- [MCP Sampling Loop 技术深度解析](sources/mcp-sampling-loop-deep-dive.md)
- [Untitled](sources/nvidia-rubin-platform.md)
- [Untitled](sources/anthropic-three-agent-harness.md)
- [Stripe Minions Blueprint 架构详解](sources/stripe-minions-blueprint.md)
- [Untitled](sources/nvidia-feynman-gtc2026.md)
- [LangChain Terminal Bench 2.0 Harness优化详解](sources/langchain-terminal-bench-20.md)
- [Harness Verifier Model 训练方法与多 Agent 容错架构深度调研](sources/harness-verifier-training-2026.md)
- [月之暗面 Kimi K2.5 深度分析](sources/moonshot-kimi-k25.md)
- [AMD MI450 vs NVIDIA Rubin 竞争分析](sources/amd-mi450-vs-rubin.md)
- [PRM 训练数据构建与 Test-Time Compute 自适应预算分配深度调研](sources/prm-adaptive-test-time-compute-2026.md)
- [Harness Engineering: 从 Prompt → Context → Harness 的认知升级](sources/harness-engineering-huxiu-2026-03-13.md)
- [小红书 AI 战略深度追踪](sources/xiaohongshu-ai-strategy-2026.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)
- [GitHub AI 仓库排名追踪（2026-05-12 快照）](sources/github-ai-ranking-2026-05.md)

#### Pratiyush (`entities/pratiyush.md`)

**被 1 篇来源引用：**
- [ds4 - GitHub仓库分析](sources/ds4-github.md)

#### 三星 (Samsung Electronics) (`entities/samsung.md`)

**被 8 篇来源引用：**
- [HBM4/5 路线图与产业格局重构（2026-2027）](sources/hbm4-5-roadmap-2026.md)
- [Samsung and Micron Start Shipping HBM4 — The Register](sources/samsung-micron-hbm4-shipping-2026.md)
- [Untitled](sources/nvidia-rubin-platform.md)
- [Chiplet 互连技术 2026：UCIe、HBM4 与封装拐点](sources/chiplet-interconnect-2026.md)
- [Applied Materials 收购 ASMPT NEXX（面板级先进封装沉积设备）](sources/applied-materials-nexx-acquisition-2026-05-03.md)
- [近存计算（Near-Memory Computing）商业化全景 2026](sources/near-memory-computing-commercialization.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)

#### SK海力士 (SK hynix) (`entities/sk-hynix.md`)

**被 8 篇来源引用：**
- [HBM4/5 路线图与产业格局重构（2026-2027）](sources/hbm4-5-roadmap-2026.md)
- [Samsung and Micron Start Shipping HBM4 — The Register](sources/samsung-micron-hbm4-shipping-2026.md)
- [Untitled](sources/nvidia-rubin-platform.md)
- [Applied Materials 收购 ASMPT NEXX（面板级先进封装沉积设备）](sources/applied-materials-nexx-acquisition-2026-05-03.md)
- [Untitled](sources/sk-hynix-ces2026.md)
- [近存计算（Near-Memory Computing）商业化全景 2026](sources/near-memory-computing-commercialization.md)
- [Intel EMIB-T 与先进封装代工战略](sources/intel-emib-t-advanced-packaging.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)

#### Stripe (`entities/stripe.md`)

**被 4 篇来源引用：**
- [MCP Sampling Loop 技术深度解析](sources/mcp-sampling-loop-deep-dive.md)
- [Stripe Minions Blueprint 架构详解](sources/stripe-minions-blueprint.md)
- [Harness Engineering: 从 Prompt → Context → Harness 的认知升级](sources/harness-engineering-huxiu-2026-03-13.md)
- [Karpathy Agentic Engineering 深度分析](sources/karpathy-agentic-engineering-2026.md)

#### TSMC (`entities/tsmc.md`)

**被 9 篇来源引用：**
- [HBM4/5 路线图与产业格局重构（2026-2027）](sources/hbm4-5-roadmap-2026.md)
- [台积电 CoWoS 产能目标上调（2026-2027）](sources/tsmc-cowos-capacity-2026-2027.md)
- [Chiplet 互连技术 2026：UCIe、HBM4 与封装拐点](sources/chiplet-interconnect-2026.md)
- [EDA 厂商竞逐台积电埃米时代路线图（2026 TSMC Symposium）](sources/eda-vendors-tsmc-2026.md)
- [AI Chip Packaging Constraints Create $50B Market — AOL Finance](sources/ai-packaging-50b-market-2026.md)
- [Intel EMIB-T Enters Production Fab Rollout in 2026 — Tom's Hardware](sources/intel-emib-t-production-2026.md)
- [AMD MI450 vs NVIDIA Rubin 竞争分析](sources/amd-mi450-vs-rubin.md)
- [Intel EMIB-T 与先进封装代工战略](sources/intel-emib-t-advanced-packaging.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)

---
### 技术概念被引用来源

#### 先进封装（Advanced Packaging） (`concepts/advanced-packaging.md`)

**被 9 篇来源引用：**
- [HBM4/5 路线图与产业格局重构（2026-2027）](sources/hbm4-5-roadmap-2026.md)
- [台积电 CoWoS 产能目标上调（2026-2027）](sources/tsmc-cowos-capacity-2026-2027.md)
- [Chiplet 互连技术 2026：UCIe、HBM4 与封装拐点](sources/chiplet-interconnect-2026.md)
- [EDA 厂商竞逐台积电埃米时代路线图（2026 TSMC Symposium）](sources/eda-vendors-tsmc-2026.md)
- [Applied Materials 收购 ASMPT NEXX（面板级先进封装沉积设备）](sources/applied-materials-nexx-acquisition-2026-05-03.md)
- [AI Chip Packaging Constraints Create $50B Market — AOL Finance](sources/ai-packaging-50b-market-2026.md)
- [Intel EMIB-T Enters Production Fab Rollout in 2026 — Tom's Hardware](sources/intel-emib-t-production-2026.md)
- [Intel EMIB-T 与先进封装代工战略](sources/intel-emib-t-advanced-packaging.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)

#### Agent Skills (`concepts/agent-skills.md`)

**被 8 篇来源引用：**
- [MCP Sampling Loop 技术深度解析](sources/mcp-sampling-loop-deep-dive.md)
- [GitHub Trending Weekly 2026-03-25 — Agent Skills Ecosystem Explosion](sources/github-trending-2026-03-25.md)
- [12-Factor Agents 工程原则深度解析](sources/12-factor-agents-humanlayer.md)
- [Blueprint for a Modern Agentic Harness in 2026 (Gist Summary)](sources/modern-harness-blueprint-2026.md)
- [Agent Skills - GitHub仓库分析](sources/agent-skills-github.md)
- [小红书 AI 战略深度追踪](sources/xiaohongshu-ai-strategy-2026.md)
- [GitHub AI 仓库排名追踪（2026-05-12 快照）](sources/github-ai-ranking-2026-05.md)
- [Karpathy CLAUDE.md 12条规则升级版](sources/karpathy-claude-md-12-rules.md)

#### Chiplet（芯粒） (`concepts/chiplet.md`)

**被 6 篇来源引用：**
- [Chiplet 互连技术 2026：UCIe、HBM4 与封装拐点](sources/chiplet-interconnect-2026.md)
- [EDA 厂商竞逐台积电埃米时代路线图（2026 TSMC Symposium）](sources/eda-vendors-tsmc-2026.md)
- [Applied Materials 收购 ASMPT NEXX（面板级先进封装沉积设备）](sources/applied-materials-nexx-acquisition-2026-05-03.md)
- [Untitled](sources/nvidia-feynman-gtc2026.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)

#### DS4 - DeepSeek V4 Flash专用推理引擎 (`concepts/ds4.md`)

**被 1 篇来源引用：**
- [ds4 - GitHub仓库分析](sources/ds4-github.md)

#### Harness Engineering / Harness方法论 (`concepts/harness-methodology.md`)

**被 16 篇来源引用：**
- [MCP Sampling Loop 技术深度解析](sources/mcp-sampling-loop-deep-dive.md)
- [GitHub Trending Weekly 2026-03-25 — Agent Skills Ecosystem Explosion](sources/github-trending-2026-03-25.md)
- [12-Factor Agents 工程原则深度解析](sources/12-factor-agents-humanlayer.md)
- [Untitled](sources/anthropic-three-agent-harness.md)
- [Blueprint for a Modern Agentic Harness in 2026 (Gist Summary)](sources/modern-harness-blueprint-2026.md)
- [Stripe Minions Blueprint 架构详解](sources/stripe-minions-blueprint.md)
- [Untitled](sources/anthropic-managed-agents.md)
- [Agent Skills - GitHub仓库分析](sources/agent-skills-github.md)
- [RLHF 新变体深度解析：Online DPO / IPO / KTO](sources/rlhf-online-dpo-ipo-kto.md)
- [LangChain Terminal Bench 2.0 Harness优化详解](sources/langchain-terminal-bench-20.md)
- [Harness Verifier Model 训练方法与多 Agent 容错架构深度调研](sources/harness-verifier-training-2026.md)
- [月之暗面 Kimi K2.5 深度分析](sources/moonshot-kimi-k25.md)
- [Harness Engineering: 从 Prompt → Context → Harness 的认知升级](sources/harness-engineering-huxiu-2026-03-13.md)
- [Karpathy Agentic Engineering 深度分析](sources/karpathy-agentic-engineering-2026.md)
- [小红书 AI 战略深度追踪](sources/xiaohongshu-ai-strategy-2026.md)
- [GitHub AI 仓库排名追踪（2026-05-12 快照）](sources/github-ai-ranking-2026-05.md)

#### HBM（高带宽内存） (`concepts/hbm.md`)

**被 13 篇来源引用：**
- [HBM4/5 路线图与产业格局重构（2026-2027）](sources/hbm4-5-roadmap-2026.md)
- [台积电 CoWoS 产能目标上调（2026-2027）](sources/tsmc-cowos-capacity-2026-2027.md)
- [Untitled](sources/nvidia-rubin-platform.md)
- [Chiplet 互连技术 2026：UCIe、HBM4 与封装拐点](sources/chiplet-interconnect-2026.md)
- [Applied Materials 收购 ASMPT NEXX（面板级先进封装沉积设备）](sources/applied-materials-nexx-acquisition-2026-05-03.md)
- [Untitled](sources/sk-hynix-ces2026.md)
- [AI Chip Packaging Constraints Create $50B Market — AOL Finance](sources/ai-packaging-50b-market-2026.md)
- [近存计算（Near-Memory Computing）商业化全景 2026](sources/near-memory-computing-commercialization.md)
- [Untitled](sources/nvidia-feynman-gtc2026.md)
- [AMD MI450 vs NVIDIA Rubin 竞争分析](sources/amd-mi450-vs-rubin.md)
- [ds4 - GitHub仓库分析](sources/ds4-github.md)
- [Intel EMIB-T 与先进封装代工战略](sources/intel-emib-t-advanced-packaging.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)

#### LLM Wiki (Karpathy Pattern) (`concepts/llm-wiki-pattern.md`)

*暂无来源引用 — 待完善*

#### Near-Memory Computing（近存计算） (`concepts/near-memory-computing.md`)

**被 4 篇来源引用：**
- [Untitled](sources/sk-hynix-ces2026.md)
- [近存计算（Near-Memory Computing）商业化全景 2026](sources/near-memory-computing-commercialization.md)
- [Chiplet Interconnect Ecosystem 2026 Inflection Point — PatSnap Eureka Analysis](sources/patsnap-chiplet-ecosystem-2026.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)

#### 存算一体 / Processing-in-Memory (PIM) (`concepts/processing-in-memory.md`)

**被 3 篇来源引用：**
- [Untitled](sources/sk-hynix-ces2026.md)
- [近存计算（Near-Memory Computing）商业化全景 2026](sources/near-memory-computing-commercialization.md)
- [存内计算（PIM）商业化障碍与工业界路线图深度调研](sources/pim-commercialization-industrial-roadmap-2026.md)

#### RLHF（人类反馈强化学习） (`concepts/rlhf.md`)

**被 3 篇来源引用：**
- [RLHF 新变体深度解析：Online DPO / IPO / KTO](sources/rlhf-online-dpo-ipo-kto.md)
- [Harness Verifier Model 训练方法与多 Agent 容错架构深度调研](sources/harness-verifier-training-2026.md)
- [PRM 训练数据构建与 Test-Time Compute 自适应预算分配深度调研](sources/prm-adaptive-test-time-compute-2026.md)

#### Test-Time Compute（测试时计算扩展） (`concepts/test-time-compute.md`)

**被 3 篇来源引用：**
- [RLHF 新变体深度解析：Online DPO / IPO / KTO](sources/rlhf-online-dpo-ipo-kto.md)
- [Harness Verifier Model 训练方法与多 Agent 容错架构深度调研](sources/harness-verifier-training-2026.md)
- [PRM 训练数据构建与 Test-Time Compute 自适应预算分配深度调研](sources/prm-adaptive-test-time-compute-2026.md)

---
## 📊 统计概览

| 类别 | 数量 | 被引用次数 |
|------|------|------------|
| 实体 (entities) | 19 | 124 |
| 概念 (concepts) | 11 | 66 |
| 来源 (sources) | 35 | — |
| 交叉引用 | — | 190 |

---
## 🧭 如何使用本索引

1. **查找实体/概念**：上方按字母排序的实体和概念列表
2. **追溯来源**：每个实体/概念下方列出引用它的 sources/ 文件
3. **发现空白**：标记为「暂无来源引用」的条目 = 知识缺口，可通过提问触发补充
4. **机器查询**：读取 `graph.jsonld` 获取结构化数据

---
*本索引随知识库增长自动更新。运行 `python3 scripts/knowledge_compiler.py` 重新编译。*