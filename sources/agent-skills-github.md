# Agent Skills - GitHub仓库分析

> 来源：[github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)（示例链接）  
> 采集时间：2026-05-09  
> 作者：Addy Osmani

---

## 📋 源文件元数据

| 属性 | 内容 |
|------|------|
| 标题 | Agent Skills |
| 作者 | Addy Osmani |
| 发布时间 | 2026-02 |
| 来源类型 | GitHub开源项目 |
| 关键发现 | LLM Agent的"技能系统"设计范式 |

---

## 🎯 核心内容摘要

### 项目定位
Agent Skills是一个让LLM Agent像游戏角色一样"学技能"的框架：
- 每个Skill = 目标 + 工具 + 记忆 + 约束
- 可组合：基础Skill组合成复杂Skill
- 可学习：Agent通过实践"升级"Skill
- 可共享：Skill包在团队/社区间复用

### 与MCP的关系
- **MCP**：底层协议（类似USB-C），定义工具访问标准
- **Agent Skills**：上层抽象（类似App Store），定义Agent行为组织方式
- **互补**：MCP解决"Agent能用什么工具"，Agent Skills解决"Agent怎么组合工具完成任务"

### 技术设计
1. **Skill Schema**：JSON/YAML定义Skill的结构
2. **Skill Registry**：Skill的注册/发现/版本管理
3. **Skill Composition**：多个Skill的编排和调用链
4. **Skill Learning**：从成功/失败中自动优化Skill参数

---

## 🔍 关键发现

| 发现 | 详情 | 关联实体/概念 |
|------|------|--------------|
| Skill是Agent的"函数" | 把Agent能力模块化，像编程语言的函数库 | [concepts/agent-skills.md](../concepts/agent-skills.md) |
| 与Harness互补 | Harness是"大脑"，Skills是"肌肉" | [concepts/harness-methodology.md](../concepts/harness-methodology.md) |
| 社区热度 | GitHub Stars快速增长，社区贡献活跃 | [entities/addy-osmani.md](../entities/addy-osmani.md) |

---

## 📄 原文摘录

> "未来的AI工程师会写Skill，而不是写Prompt。"
> —— Addy Osmani

---

## 🔗 相关页面
- [concepts/agent-skills.md](../concepts/agent-skills.md) — 深度分析
- [entities/addy-osmani.md](../entities/addy-osmani.md) — 作者详情
- [concepts/harness-methodology.md](../concepts/harness-methodology.md) — 对比Harness方法论

---

*最后更新：2026-05-09*
