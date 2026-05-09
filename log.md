# 知识库操作日志

## 格式
`[YYYY-MM-DD] action | description`

---

## 2026-05-09

### [2026-05-09] setup | GitHub仓库集成完成
**仓库**：https://github.com/large-cat/ai-tech-intel
**配置：**
- SSH Deploy Key（ed25519），仅 `ai-tech-intel` 仓库有写权限
- Remote: `git@github-ai-tech-intel:large-cat/ai-tech-intel.git`
- 首次推送：22个文件已上传到master分支

**定时任务更新：**
- 早上8点调研 → 自动 `git add wiki/` → `git commit` → `git push`
- 晚上8点调研(US) → 同上，commit信息带 `(US)` 标记
- 早上9:30微信推送 → 消息附带GitHub链接（可直接点击查看完整版）

---

### [2026-05-09] update | 定时任务调整为一天两调研+统一推送
**原因**：用户要求覆盖美国时段（美东8点对应北京时间20点）

**新定时任务配置：**
1. `AI Tech Intel Research` — 0 8 * * * (北京时间早上8点)
2. `AI Tech Intel Research (US)` — 0 20 * * * (北京时间晚上8点，对应美东早上8点)
3. `AI Tech Intel Push` — 30 9 * * * (北京时间早上9:30，统一推送)

**逻辑：**
- 早上8点调研亚洲/欧洲时段更新
- 晚上8点调研美国时段更新（美东白天发布的内容）
- 两次结果合并到同一篇 weekly-digest/YYYY-MM-DD.md
- 第二天早上9:30统一推送到微信

---

### [2026-05-09] update | 扩展监控范围+新增概念页面
**用户偏好更新：**
- 排除来源：CSDN（质量不稳定）
- 新增监控：前沿博客、GitHub项目、行业大佬动态

**新增概念页面：**
- `concepts/agent-skills.md` — Addy Osmani的AI编程Agent技能库 (29K+ stars)
- `concepts/ds4.md` — antirez的DeepSeek V4 Flash专用推理引擎 (Metal-only, 2-bit量化)
- `concepts/llm-wiki-pattern.md` — Karpathy的LLM Wiki知识管理模式

**新增监控目标：**
**GitHub项目：**
- addyosmani/agent-skills — Agent技能库
- antirez/ds4 — 本地专用推理引擎
- Pratiyush/llm-wiki — LLM Wiki实现
- ruvnet/Ruflo — Agent编排平台
- bytedance/deer-flow — 字节SuperAgent
- virattt/dexter — 金融研究Agent

**行业大佬：**
- Andrej Karpathy — Eureka Labs, LLM Wiki
- Addy Osmani — agent-skills, Chrome DevTools AI
- swyx — Latent Space, AI Engineer
- Simon Willison — Datasette, LLM工具
- Andrew Ng — DeepLearning.AI

**社区：**
- Hacker News AI热帖
- Reddit r/MachineLearning
- Twitter/X AI圈

**定时任务更新：**
- 更新 `~/.openclaw/cron/jobs.json`
- 加入前沿项目/人物监控prompt

---

## 2026-05-09

### [2026-05-09] init | 知识库初始化
- 创建wiki目录结构
- 创建CLAUDE.md (schema)
- 创建index.md
- 设定每日自动调研任务
- 监控目标：Anthropic/OpenAI/Google/月之暗面/DeepSeek/NVIDIA/三星/SK海力士
- 重点技术：Harness方法论、存算一体/近存运算
