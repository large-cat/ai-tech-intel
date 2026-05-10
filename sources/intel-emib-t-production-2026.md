# Intel EMIB-T Enters Production Fab Rollout in 2026 — Tom's Hardware

**来源**：Tom's Hardware  
**URL**：https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-t-heads-for-fab-rollout-this-year  
**日期**：2026-02  
**采集时间**：2026-05-10  

---

## 执行摘要

Intel EMIB-T（带TSV的嵌入式多Die互连桥）**预计今年进入生产工厂投产**，这是Intel Foundry在18A工艺良率达到行业标准之前，最快实现AI加速器封装收入的跳板。Intel CFO Dave Zinsner表示正在"接近敲定每年数十亿美元收入的先进封装交易"。

---

## 技术细节：EMIB-T vs 标准EMIB

### 标准EMIB（2017量产）
- 在有机基板腔体内嵌入小硅桥Die
- **跳过TSV**——桥Die简单廉价
- 功率必须通过有机基板绕桥传输（长路径、高电阻）
- 适合Sapphire Rapids和Ponte Vecchio，但**不适合HBM4级加速器**

### EMIB-T（2026投产）
- **加入TSV**——桥Die支持垂直功率传输
- 集成MIM电容（噪声抑制）
- 铜接地网格（信号隔离）
- **45μm凸点间距**，路线图→35μm→25μm
- 能效：约**0.25 pJ/bit**
- UCIe-A接口：**32 Gb/s/pin或更高**
- 支持HBM3/HBM3E/HBM4/**HBM5**
- 封装尺寸可达**120mm×180mm**，支持38+桥接、12+光罩级Die

---

## 性能对标：Intel vs TSMC CoWoS-L

| 指标 | Intel EMIB-T | TSMC CoWoS-L |
|------|-------------|-------------|
| 2026目标 | **8x光罩** | 5.5x光罩 |
| 2027目标 | 12x光罩 | 9.5x光罩 |
| 2028目标 | 12x+光罩 | — |
| 成本 | **低数百美元/芯片** | $900-1,000/Rubin级加速器 |
| 桥Die晶圆利用率 | ~**90%** | ~60%(大中介层) |
| HBM支持 | HBM3→HBM5 | HBM3E→HBM4 |

> 来源：Bernstein分析师估计；Investing.com封装分析

---

## Intel概念封装（2025年12月发布）

Intel展示了概念性2.5D/3D封装设计：
- **16个计算元素**跨8个基Die
- **24个HBM5堆叠**
- **10,296 mm²硅面积**
- 达到**12x光罩尺寸**

对比：TSMC CoWoS-L路线图2027年目标9.5x光罩，Intel目标2028年12x+

---

## 商业意义

1. **Intel Foundry翻身**：2025年外部收入仅$307M vs $10.3B运营亏损
2. **封装是最快切入点**：18A工艺良率2027年前难达行业标准
3. **Terafab项目**：已签约Musk的Terafab（尽管交付现实存疑）
4. **成本优势**：EMIB比CoWoS便宜$500-800/芯片

---

## 原文链接
- https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-t-heads-for-fab-rollout-this-year
