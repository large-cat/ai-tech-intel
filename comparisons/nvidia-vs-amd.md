# NVIDIA vs AMD 硬件平台对比

> 对比类型：GPU/加速器架构
> 更新时间：2026-05
> 触发条件：新架构发布、benchmark数据、市场份额变化

## 当前世代对比

| 维度 | NVIDIA Rubin | AMD MI450 |
|------|-------------|-----------|
| **工艺节点** | 3nm (TSMC) | 2nm (TSMC) — 首次反超 |
| **HBM配置** | 16颗HBM4，576GB | 12颗HBM4，432GB |
| **总带宽** | ~4.5 TB/s | ~3.5 TB/s |
| **特殊技术** | 硅光子互连 | 标准互连 |
| **散热方案** | 标准液冷 | 标准液冷 |
| **发布时间** | 2026 H2 | 2027 |
| **Meta订单** | $100B量级 | — |

来源：[[nvidia-rubin-platform]]、[[amd-mi450-vs-rubin]]

## 下一代前瞻

### NVIDIA Feynman (1.6nm)
- 硅光子全面集成
- 功耗降低30%
- 与Intel洽谈代工分散TSMC风险

来源：[[nvidia-feynman-gtc2026]]

### AMD MI500+（推测）
- 若2nm成功，MI500可能继续工艺领先
- 需要软件生态突破（ROCm vs CUDA差距）

## 软件生态差距

| 维度 | NVIDIA CUDA | AMD ROCm |
|------|-------------|----------|
| **开发者数量** | 400万+ | ~50万 |
| **框架支持** | 全生态 | PyTorch/TensorFlow主流 |
| **库成熟度** | cuDNN/cuBLAS生态完善 | MIOpen追赶中 |
| **云服务可用性** | 全平台 | AWS/Azure部分 |

**结论**：AMD硬件参数首次反超，但软件生态差距仍是最大壁垒。

---

*本对比基于 [[sources/amd-mi450-vs-rubin]]、[[sources/nvidia-feynman-gtc2026]]。*
