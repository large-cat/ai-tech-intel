# DS4 - DeepSeek V4 Flash专用推理引擎

- **类型**: 概念 / 开源项目 / 本地推理
- **作者**: Salvatore Sanfilippo (antirez, Redis创始人)
- **创建时间**: 2026-05-07
- **最后更新**: 2026-05-09

## 一句话定义

**ds4** 是Redis创始人antirez为DeepSeek V4 Flash模型从零编写的专用本地推理引擎，采用"一模型一引擎"的激进路线，Metal-only、2-bit非对称量化、KV缓存磁盘化，目标是让本地推理从"能跑"走向"产品级"。

---

## 核心设计

### 三大关键技术

| 技术 | 原理 | 效果 |
|------|------|------|
| **非对称2-bit量化** | MoE Router层用IQ2_XXS/Q2_K，其他层保持Q8 | 大幅压缩体积，编码场景性能可接受 |
| **KV缓存磁盘化** | 将KV状态写入SSD，下次请求匹配token前缀直接加载 | 跳过prefill，Claude Code式25K初始提示首次后瞬间恢复 |
| **内置API兼容层** | /v1/chat/completions (OpenAI) + /v1/messages (Anthropic) | 直接接入opencode/Pi/Claude Code |

### 工程哲学

> "本地推理领域有很多优秀项目，但新模型不断发布，注意力立刻被下一个模型吸走。这个项目刻意走一条窄路：一次赌一个模型，官方logits验证，长上下文测试，足够的Agent集成来确认它真的能用。"
> — antirez

**与通用框架的对比**

| 维度 | llama.cpp/MLX | ds4 |
|------|---------------|-----|
| 定位 | 万能框架（一个框架跑所有模型） | 专用引擎（一个模型一个优化） |
| 体积 | 几百MB+ | 68MB |
| 代码量 | 几十万行 | 几千行 |
| 优化深度 | 通用抽象 = 妥协 | 针对性优化 = 极致 |
| 维护模型数 | 数百个 | 1个（当前是V4 Flash） |

---

## 关键数据

| 指标 | 数据 |
|------|------|
| 二进制体积 | ~68MB |
| 内存需求 | 128GB+ (Mac Studio级别) |
| 上下文支持 | 最高1M tokens (26GB内存) |
| 量化方案 | 2-bit非对称 (Router) + Q8 (其他) |
| 推理后端 | Metal-only (未来可能CUDA) |
| AI辅助开发 | GPT 5.5 "strong assistance" |

---

## 技术洞察

### "一模型一引擎"路线的意义

1. **本地AI从"玩具"到"工作站"**
   - 配合Mac Studio + 128GB RAM + ds4 + Claude Code = 完全私有的准前沿AI工作站

2. **对通用框架的挑战**
   - 如果每个明星模型都值得一个专用引擎，通用框架的价值在哪里？
   - 可能答案：通用框架跑实验，专用引擎跑生产

3. **AI辅助开发的标杆案例**
   - antirez公开承认："开发有GPT 5.5的强力协助"
   - 从fork llama.cpp到从零写ds4，仅两周
   - "如果你不接受AI协助开发的代码，这个软件不适合你"

### 潜在风险

- **模型过时风险** — V4 Flash过气后，ds4可能需重写
- **硬件锁定** — Metal-only，CUDA/Linux用户暂无法使用
- **维护可持续性** — 个人项目，长期维护不确定

---

## 与Harness/Agent Skills的关联

- ds4是**Agent的执行环境** — 让本地Agent（Claude Code/opencode）有可靠的推理后端
- Agent Skills是**Agent的行为规范** — 让Agent在编码时遵循工程纪律
- 两者结合 = 本地私有 + 工程级可靠的AI开发环境

---

## 相关页面

- [entities/antirez.md](../entities/antirez.md) — 作者详情
- [entities/deepseek.md](../entities/deepseek.md) — DeepSeek厂商页
- [concepts/processing-in-memory.md](processing-in-memory.md) — 存算一体（量化技术相关）
- [sources/ds4-github.md](../sources/ds4-github.md) — 仓库分析

## 外部链接

- GitHub: https://github.com/antirez/ds4
- HN讨论: https://news.ycombinator.com/item?id=48050751
