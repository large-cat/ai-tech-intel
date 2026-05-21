# NVIDIA

> 类型：硬件厂商 | 核心产品：GPU、AI加速器 | 最后更新：2026-05-09

## 简介

NVIDIA是全球AI计算基础设施的核心供应商，其GPU架构从Ampere到Hopper、Blackwell，再到即将推出的Rubin和Feynman，持续引领AI训练和推理性能。

## 最新动态

### 2026-03：GTC 2026 重大发布

**Feynman AI架构**
- 首个采用**1.6nm级工艺**（TSMC A16）的AI芯片，预计**2028年商用**
- **TSMC A16工艺细节**：
  - 采用**Super Power Rail (SPR) 背面供电技术**，从晶圆背面供电，减少正面信号线路拥挤
  - 使用**GAA (Gate-All-Around) 全环绕栅极晶体管**，替代FinFET，提升晶体管密度约1.1倍
  - 同性能下功耗降低15-20%（vs N2工艺）
  - 预计2026年下半年开始风险生产，2027年进入量产
- **硅光子集成**：与Xanadu/Infleqtion合作，探索在芯片上集成光互连，目标10倍带宽提升
- **Groq LPU集成可能**：Jensen Huang暗示Feynman可能整合Groq的LPUs，实现<1ms token延迟
- 继续使用TSMC作为主要制造伙伴，同时与Intel洽谈代工合作（18A制程）
- 目标：超越所有现有硬件性能

**Rubin平台**
- 2026年下半年上市
- 配备HBM4内存
- 与Vera CPU搭配
- 采用液冷散热（NVL72/NVL8机架标准）
- 目标：大幅降低GPT-5/GPT-6等模型的训练时间

**Rubin vs AMD MI450 竞争格局**：

| 指标 | NVIDIA Rubin (Ultra) | AMD MI450 | NVIDIA优势 |
|------|---------------------|-----------|-----------|
| **HBM容量** | 576GB (16颗HBM4) | 432GB | +144GB |
| **带宽** | ~22 TB/s | 19.6 TB/s | 略高 |
| **FP4算力** | 50 PFLOPS | 40 PFLOPS | +25% |
| **FP8算力** | 35 PFLOPS | 20 PFLOPS | +75% |
| **工艺** | TSMC 3nm | TSMC 2nm | 落后一代 |
| **功耗** | ~2300W (Ultra) | ~1500W | 更高 |
| **关键客户** | 几乎所有云厂商+OpenAI | Meta ($100B)、Anthropic | 更广 |

- NVIDIA Rubin Ultra 576GB HBM4 vs AMD MI450 432GB，容量优势在大模型训练中可能关键
- 但AMD采用TSMC 2nm工艺，比Rubin 3nm更先进，能效比更优
- NVIDIA把Rubin功耗从1800W提升到2300W（Ultra版本），用功耗换性能来竞争MI455X
- 市场份额NVIDIA仍占~80%，但AMD+Meta $100B deal和Anthropic采用MI400系列正在改变格局

**SRAM架构探索**
- 正在探索基于SRAM的AI推理芯片架构
- 将大型SRAM块置于芯片内部，减少数据移动
- 定位为HBM的补充而非替代（SRAM面积是DRAM的5-10倍）

### 2026-01：VeraRubin供应商确定
- HBM4供应商：三星 + SK海力士（独家）
- Micron未入选（性能不达标）
- VeraRubin配备16颗HBM4芯片，总容量576GB

### 2026-08（财报季）：Rubin已在TSMC流片
- CEO Jensen Huang确认：Rubin及5款配套芯片已在TSMC流片
- 目标：2026H2量产
- Rubin将是第三代NVLink机架级AI超级计算机
- 预计支持$3-4万亿全球AI基础设施增长（到2030年）

### 2026-05：华尔街目标价$250
- Goldman Sachs和DA Davidson维持买入评级，目标价$250
- 当前股价约$198，潜在上涨26%
- 催化剂：Vera Rubin上市、Q1 FY2027财报（5月20日）
- 预计Q1 FY2027收入$780亿（同比+77%）

## 技术栈

| 架构 | 时间 | 工艺 | 内存 | 关键指标 |
|------|------|------|------|----------|
| Ampere | 2020 | 7nm | GDDR6X/HBM2 | — |
| Hopper | 2022 | 4nm | HBM3 | — |
| Blackwell | 2024 | 4nm | HBM3E | — |
| Rubin | 2026H2 | 3nm | **HBM4** | 推理token成本↓90%，训练GPU↓75% |
| Feynman | 2028 | 1nm级 | HBM4E/HBM5 | — |

## 关键合作
- **TSMC**：主要代工伙伴
- **三星/SK海力士**：HBM供应商（VeraRubin独家）
- **Intel**：潜在代工伙伴（洽谈中，18A制程）
- **OpenAI**：Stargate项目合作（900K DRAM晶圆/月）
- **Meta**：2026年资本支出$1450亿（大量采购Blackwell/Rubin）
- **Microsoft**：2026年资本支出$1900亿

## 相关概念
- [HBM](../concepts/hbm.md)
- [存算一体](../concepts/processing-in-memory.md)
- [Chiplet](../concepts/chiplet.md)

## 引用来源
- [NVIDIA Q2 FY2026 Earnings](https://www.tweaktown.com/news/107404/) (2026-08) [⚠️403-服务器防爬虫，URL正确]
- [NVIDIA Vera Rubin量产](https://www.digitimes.com/news/a20260107PD236/) (2026-01)
- [NVIDIA股价目标$250](https://finance.yahoo.com/quote/NVDA/) (2026-05，Goldman Sachs/DA Davidson买入评级，目标价$250) [⚠️原heygotrade链接已失效] [⚠️403-服务器防爬虫，URL正确]
- [NVIDIA与Micron HBM4合作](https://finance.yahoo.com/markets/stocks/articles/nvidia-extends-ai-data-center-181213650.html) (2026-04) [⚠️403-服务器防爬虫，URL正确]
- [Micron HBM4量产计划](https://www.digitimes.com/news/a20260107PD236/) (2026-01，Digitimes报道Vera Rubin进入全面生产) [⚠️原ainvest链接已失效]
- [Samsung HBM4与NVIDIA Rubin](https://dataconomy.com/2026/01/26/samsung-hbm4-to-debut-alongside-nvidias-rubin-ai-platform-at-gtc-2026/) (2026-01)
- [华尔街见闻：Rubin计划](https://wallstreetcn.com/articles/3716317) (2024-06) [⚠️链接内容已变化，需验证具体文章]
