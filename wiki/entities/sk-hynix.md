# SK海力士 (SK hynix)

> 类型：硬件厂商 | 核心产品：HBM、DRAM、NAND | 最后更新：2026-05-09

## 简介

SK海力士是全球HBM（高带宽内存）市场的领导者，在AI内存基础设施中占据核心地位。截至2025年Q3，SK海力士占据HBM市场53%的份额（收入计）/ 62%（出货量计）。

## 最新动态

### 2026-05：产能扩张
- 2026年投资基础设施：**比之前宣布的增加4倍以上**
- M15X工厂预计2027年中期投入使用
- 与三星一起和OpenAI签署意向书：供应90万片DRAM晶圆/月（支持Stargate项目）

### 2026-03：GTC 2026
- 主题展台"Spotlight on AI Memory"
- 展示与NVIDIA的联合产品：液冷eSSD、DGX Spark（搭载LPDDR5X）
- HBM4、HBM3E、SOCAMM2全线产品

### 2026-01：CES 2026
**AI System Demo Zone展示：**
- **cHBM (Custom HBM)**：客户定制化HBM，将GPU/ASIC功能集成到HBM基板
  - **核心技术"Stream DQ Architecture"**：在HBM base die上实现定制计算逻辑，将部分GPU/ASIC功能（HBM PHY、内存控制器、甚至处理逻辑）集成到HBM基板
  - **性能提升**：SK海力士称cHBM可将最大推理吞吐提升约**7倍**（vs传统HBM）
  - **客户扩展**：Google/Amazon/Microsoft等超大规模云厂商也计划从2027年起定制自己的HBM（"他们有自己的Workload"）
- **AiMX**：基于GDDR6-AiM芯片的LLM专用加速器卡
- **CuD (Compute-using-DRAM)**：在DRAM单元内执行简单计算
- **CMM-Ax**：CXL内存模块+计算能力集成
- **Data-aware CSD**：可感知/分析/执行处理的计算存储驱动器

## 产品线

| 产品 | 状态 | 特点 |
|------|------|------|
| HBM3E | 量产中 | 当前主流 |
| HBM4 | 2026年Q1开始供货 | 第六代，NVIDIA VeraRubin主力供应 |
| HBM4E | 开发中 | 速度提升 |
| LPDDR6 | 展示阶段 | 端侧AI优化 |
| 321层QLC NAND | 展示阶段 | 2Tb容量，AI数据中心eSSD |

## NVIDIA供应关系
- 2025年Q2以来SK海力士超越三星，DRAM收入市场份额第一（38%）
- HBM市场份额高达**64%**（2025年Q2）
- NVIDIA VeraRubin独家HBM4供应商（与三星共享）
- 计划2026年产能基本售罄

## 技术路线
- **Full Stack AI Memory Creator**战略
- 从HBM到LPDDR到QLC NAND，覆盖AI数据中心全栈
- 重点推进PIM/CuD等存算一体技术

## 相关概念
- [HBM](../concepts/hbm.md)
- [存算一体](../concepts/processing-in-memory.md)
