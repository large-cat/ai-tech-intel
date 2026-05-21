# 半导体与AI硬件趋势综述

> 综合类型：硬件技术综述
> 覆盖实体：NVIDIA, AMD, Intel, 三星, SK海力士, Micron, TSMC
> 覆盖概念：HBM, Chiplet, 存算一体, 先进封装
> 更新策略：新架构发布/产能数据触发更新

## 三大硬件拐点

### 拐点1：HBM4量产（2026H2）

| 厂商 | 状态 | 关键参数 |
|------|------|---------|
| 三星 | 已官宣出货 | 16-Hi堆叠，64GB/堆栈 |
| Micron | 已官宣出货 | 12-Hi堆叠 |
| SK海力士 | 未官宣（62%份额） | 供应格局生变 |

来源：[[samsung-micron-hbm4-shipping-2026]]

### 拐点2：先进封装市场翻倍

- 2026年先进封装市场达 **$50B**
- Intel EMIB-T投产，CoWoS产能扩张
- UCIe联盟达120+成员

来源：[[intel-emib-t-production-2026]]、[[ai-packaging-50b-market-2026]]

### 拐点3：存算一体从实验室到产品

| 方向 | 成熟度 | 代表产品/项目 |
|------|--------|--------------|
| 近存运算 | ⭐⭐⭐⭐ 产品化前夜 | Samsung AxPIM, SK海力士 AiM |
| 存内计算 | ⭐⭐⭐ 原型验证 | 多家学术/初创 |
| 存内逻辑 | ⭐⭐ 早期研究 | 实验室阶段 |

来源：[[near-memory-computing-commercialization]]

## NVIDIA vs AMD 路线对比

| 维度 | NVIDIA Rubin | AMD MI450 |
|------|---------------|-----------|
| 工艺 | 3nm | 2nm（首次反超） |
| HBM容量 | 576GB（16颗HBM4） | 432GB |
| 发布时间 | 2026H2 | 2027 |
| 特殊设计 | 硅光子互连 | 标准互连 |

来源：[[amd-mi450-vs-rubin]]、[[nvidia-rubin-platform]]

## 产能瓶颈：被低估的变量

TSMC CoWoS产能从2026年的 **38万片/月** 计划扩至2027年的 **60万片/月**，但需求可能超过80万片/月。

这意味着：先进封装的产能瓶颈可能成为比芯片架构更重要的竞争壁垒。

来源：[[tsmc-cowos-capacity-2026-2027]]

---

*本综述基于 [[sources/nvidia-feynman-gtc2026]]、[[sources/hbm4-5-roadmap-2026]]、[[sources/chiplet-interconnect-2026]] 等来源。*
