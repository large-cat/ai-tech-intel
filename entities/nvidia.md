# NVIDIA

> 类型：硬件厂商 | 核心产品：GPU、AI加速器 | 最后更新：2026-05-09

## 简介

NVIDIA是全球AI计算基础设施的核心供应商，其GPU架构从Ampere到Hopper、Blackwell，再到即将推出的Rubin和Feynman，持续引领AI训练和推理性能。

## 最新动态

### 2026-03：GTC 2026 重大发布

**Feynman AI架构**
- 首个采用1nm级工艺的AI芯片，预计2028年商用
- 继续使用TSMC作为主要制造伙伴，同时与Intel洽谈代工合作
- 目标：超越所有现有硬件性能

**Rubin平台**
- 2026年下半年上市
- 配备HBM4内存
- 与Vera CPU搭配
- 采用液冷散热（NVL72/NVL8机架标准）
- 目标：大幅降低GPT-5/GPT-6等模型的训练时间

**SRAM架构探索**
- 正在探索基于SRAM的AI推理芯片架构
- 将大型SRAM块置于芯片内部，减少数据移动
- 定位为HBM的补充而非替代（SRAM面积是DRAM的5-10倍）

### 2026-01：VeraRubin供应商确定
- HBM4供应商：三星 + SK海力士（独家）
- Micron未入选（性能不达标）
- VeraRubin配备16颗HBM4芯片，总容量576GB

## 技术栈

| 架构 | 时间 | 工艺 | 内存 |
|------|------|------|------|
| Ampere | 2020 | 7nm | GDDR6X/HBM2 |
| Hopper | 2022 | 4nm | HBM3 |
| Blackwell | 2024 | 4nm | HBM3E |
| Rubin | 2026H2 | 3nm | HBM4 |
| Feynman | 2028 | 1nm级 | HBM4E/HBM5 |

## 关键合作
- **TSMC**：主要代工伙伴
- **三星/SK海力士**：HBM供应商
- **Intel**：潜在代工伙伴（洽谈中）
- **OpenAI**：Stargate项目合作（900K DRAM晶圆/月）

## 相关概念
- [HBM](../concepts/hbm.md)
- [存算一体](../concepts/processing-in-memory.md)
- [Chiplet](../concepts/chiplet.md)
