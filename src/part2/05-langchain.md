# LangChain：模型不变，Harness变，结果剧变

> LangChain的对照实验证明了"Harness > 模型"：固定Claude 3.5 Sonnet，仅优化Harness，SWE-Bench从52.8%→66.5%。

{{#include ../../sources/langchain-terminal-bench-20.md}}

---

**核心洞察**：
- Reasoning Sandwich：规划用最高深度，实现用中等，验证再用最高
- LoopDetectionMiddleware：N次编辑后自动提示"重新考虑方法"
- Trace Analyzer Skill：从失败traces自动学习，类似boosting
- **模型-specific Harness tuning**：Claude的Harness不能直接套到GPT上
