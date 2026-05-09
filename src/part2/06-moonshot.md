# 月之暗面：Agent Swarm 100子Agent并行

> Kimi K2.5的核心差异化：不是"模型+Agent wrapper"，而是模型本身为Agent Swarm优化。

{{#include ../../sources/moonshot-kimi-k25.md}}

---

**关键数据**：
- Agent Swarm：最多100个子Agent并行
- 并行工具调用：1500次/任务
- SWE-Bench Verified：76.8%
- API价格：输入$0.6/M，输出$3/M（比OpenAI低一个数量级）
- License：Modified MIT（限制大型云平台直接转售）
