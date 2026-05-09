# Agent Skills

- **类型**: 概念 / 开源项目 / Agent工程规范
- **提出者**: Addy Osmani (Google Chrome DevTools总监, AngularJS联创)
- **创建时间**: 2026-02-16
- **最后更新**: 2026-05-09

## 一句话定义

**Agent Skills** 是一套将Google二十年工程实践封装成AI可执行技能模块的开源规范，解决AI编程工具"走最短路径、跳过工程纪律"的痛点。

---

## 背景问题

AI编程助手（Claude Code, Cursor, Codex等）能写出功能正确的代码，但在工程层面是"野路子"出身：
- ❌ 不写测试
- ❌ 不做代码审查
- ❌ 不考虑向后兼容
- ❌ 不遵循提交规范
- ❌ 不做安全审计

**根本原因**: AI的目标是"让用户满意"，不是"让代码能上生产"。

---

## 核心设计

### SKILL.md 文件规范

每个技能是一个结构化的Markdown文件，定义AI在特定工程场景下应遵循的工作流：

```
skills/
├── code-review/
│   └── SKILL.md          ← 代码审查技能
├── testing/
│   └── SKILL.md          ← 测试策略技能
├── refactoring/
│   └── SKILL.md          ← 重构技能
├── documentation/
│   └── SKILL.md          ← 文档编写技能
├── security/
│   └── SKILL.md          ← 安全审计技能
└── deprecation/
    └── SKILL.md          ← 弃用迁移技能
```

### 关键原则

1. **先写规格再写代码** — PRD/规格文档是强制前置步骤
2. **测试即证明** — 每个功能必须有对应测试
3. **安全审查内嵌** — 安全不是可选项
4. **向后兼容保证** — API变更需有迁移路径

---

## 生态系统

### 支持的工具
- Claude Code
- Cursor
- Windsurf
- Codex CLI
- GitHub Copilot Chat

### 衍生项目
- **skillsjars.com** — Maven Central上的技能包分发
- **community skills** — 社区贡献的技能库扩展

---

## 关键数据

| 指标 | 数据 |
|------|------|
| GitHub Stars | 29K+ (2026-05-09) |
| 日增Stars | ~629/天 |
| 开源时间 | 2026-02-16 |
| 当前版本 | v0.6.0 |
| 许可 | MIT |

---

## 技术洞察

### 为什么这是一个信号？

1. **工程化拐点** — AI编程从"demo级"走向"生产级"的标志
2. **标准化尝试** — 类似当年ESLint/Prettier对JS生态的规范化作用
3. **人机协作新范式** — 人类定纪律，AI执行纪律，而非人类逐行审查

### 与Harness方法论的关系

Agent Skills是**Harness的具象化实现**之一：
- Harness = 抽象架构概念（Planner-Generator-Evaluator）
- Agent Skills = 可落地的工程实践规范（SKILL.md文件集）

### 潜在挑战

- **过度约束风险** — 严格规范可能降低AI的创造性解决问题的能力
- **维护负担** — 技能文件本身需要随技术演进更新
- **工具碎片化** — 不同AI IDE的技能格式不完全兼容

---

## 相关页面

- [entities/addy-osmani.md](../entities/addy-osmani.md) — 项目作者
- [concepts/harness-methodology.md](harness-methodology.md) — Harness方法论
- [sources/agent-skills-github.md](../sources/agent-skills-github.md) — 仓库分析

## 外部链接

- GitHub: https://github.com/addyosmani/agent-skills
- Maven Central: https://skillsjars.com
