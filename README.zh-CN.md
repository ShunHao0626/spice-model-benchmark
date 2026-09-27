# SPICE 模型基准测试

[English](README.md) · **简体中文**

本仓库整理了基于现有研究基准程序完成的 MOSFET 模型导入与 ngspice 仿真验证工作。工具可运行直流、瞬态、交流和噪声分析，并生成数据、图表和验证报告。

## 我的贡献与项目来源

我在这项工作中主要负责获取及导入模型，包括 FreePDK45、Sky130、GF180 和 BSIM 系列等；运行仿真并整理结果证据。这里列举的模型并非全部。基准程序的核心实现及第三方器件模型并非由我编写。基准代码来自 [SJTU-YONGFU-RESEARCH-GRP 项目](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark)；本仓库整理了本地版本及相应的模型文件、实验和结果。具体案例见[附带图表及数据的 FreePDK45 直流报告](experiments/expt_dc/FREEPDK45_MODEL_RESULTS.md)和 [Sky130 历史输出](experiments/expt_dc/sky130_output/)。[贡献与证据说明](docs/CONTRIBUTION_AND_PROVENANCE.md)逐项说明这些模型在仓库中目前有哪些材料。

## 从这里开始

**想先跑通主程序？** 使用仓库自带的 FreePDK45 模型和下方命令。**想查看以往工作？** 阅读[历史结果索引](archive/README.md)。**想修改电路或实验？** 阅读[网表索引](netlists/README.md)和[实验索引](experiments/README.md)。

要求 Python 3.8+，并确保 `ngspice` 位于 `PATH`。请从本仓库的克隆目录运行：

```bash
git clone https://github.com/ShunHao0626/spice-model-benchmark.git
cd spice-model-benchmark
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
spice-benchmark models/FreePDK45/nom.inc --modes dc --output-dir spice_benchmark_results
```

运行后，指定的输出目录下会有 `REPORT.md`、`data/` 和 `plots/`。去掉 `--modes dc` 即运行全部四类分析。该输出目录已加入 Git 忽略规则。

## 具体能得到什么结果？

程序将数值仿真数据保存到 `data/`，图表保存到 `plots/`，并在 `REPORT.md` 汇总测量值及验证检查。下表列出相应模型、电路和分析成功完成时可以得到的结果类型。

| 分析类型 | 可以查看的结果 | 历史运行中的图表示例 |
| --- | --- | --- |
| **DC 直流** | 漏极电流随漏极／栅极电压变化的 I–V 曲线、温度扫描、器件各端电流平衡；报告可给出电流范围、KCL 误差、功率和温度相关数值。 | [I–V 特性](archive/sjtu-results-2025-08/plots/dc_iv_characteristics.png) |
| **AC 交流** | 栅电容随偏置变化、S 参数幅值／相位随频率变化、非准静态相位响应和电荷守恒数据；报告可给出电容及 S 参数范围、相位差和电荷误差。 | [电容分量](archive/sjtu-results-2025-08/plots/ac_cv_components.png) |
| **瞬态** | 栅极／漏极或输入／输出电压波形、开关电流、随时间变化的功率和能量；报告可给出上升时间、传播或级联延迟、峰值与平均开关功率。 | [开关响应](archive/sjtu-results-2025-08/plots/trans_switching_response.png) |
| **噪声** | 热噪声、闪烁噪声（1/f）和散粒噪声频谱，以及可用时的温度或偏置扫描；报告可给出噪声底、1/f 指数、拐角频率和温度依赖性。 | [噪声分量](archive/sjtu-results-2025-08/plots/noise_components.png) |

如需同时查看图表、原始文件和报告中的测量值，可阅读 [2025 年 8 月的历史报告](archive/sjtu-results-2025-08/REPORT.md)及其 [`data/` 目录](archive/sjtu-results-2025-08/data/)；模型专属的直流案例见 [FreePDK45 报告](experiments/expt_dc/FREEPDK45_MODEL_RESULTS.md)和[所引用的输出文件](experiments/expt_dc/freepdk45_output/)。这些是历史结果，其数值及通过／失败状态不代表其他模型或新运行也会得到相同结论。

## 测试其他模型

默认电路使用名为 `NMOS_VTG` 和 `PMOS_VTG` 的器件，以及 FreePDK45 的器件尺寸。传入其他模型文件时，程序会在**复制出的默认电路**中替换模型引用。新模型必须提供兼容的器件名称和参数。

如果器件结构或名称不同，请提供自己的电路文件：

```bash
spice-benchmark path/to/model.inc --modes dc \
  --dc-circuit path/to/dc.cir --output-dir my_results
```

自定义电路会按原样使用；请在每个自定义电路里写好模型引用。命令行仍要求传入一个存在的模型文件。默认电路保存在仓库中，因此请从源码目录进行可编辑安装；当前普通 wheel 安装不会打包这些电路。

## 如何看结果

进程成功退出，表示所选仿真和报告生成已完成，**不代表每项验证指标都通过**。引用结果前，请查看 `REPORT.md` 中的详细检查与测量值。[`archive/`](archive/README.md) 中是 2025 年的历史输出，不是当前代码的运行结果。

在这个合并后的仓库中，四种默认模式的一次冒烟运行生成了 33 个数据文件、22 张图和一份报告。历史报告含有失败及未完成项目；这里没有重新验证或修复这些科研结论。

## 仓库导航

| 位置 | 内容 |
| --- | --- |
| [`src/spice_model_benchmark/`](src/spice_model_benchmark/) | 命令行入口、ngspice 调度、数据解析、验证与绘图 |
| [`netlists/`](netlists/README.md) | 默认 FreePDK45 电路及可选 PDK 示例 |
| [`models/FreePDK45/`](models/FreePDK45/) | 快速开始所需模型 |
| [`experiments/`](experiments/README.md) | 独立的 DC、CV、瞬态、噪声和可靠性实验 |
| [`archive/`](archive/README.md) | 原始目录中的历史报告、数据和图表 |
| [`third_party/`](third_party/README.md) | 采用独立许可的 BSIM 模型源码 |
| [`docs/`](docs/) | 方法、[贡献与来源说明](docs/CONTRIBUTION_AND_PROVENANCE.md)、检查清单和[合并来源说明](docs/SOURCE_MAP.md) |

本项目使用仿真结果进行检查，目前不包含 AI/ML 参数提取实现。其他 PDK 的可选电路需要另行取得模型。具体纳入及排除的内容见[合并来源说明](docs/SOURCE_MAP.md)。

## 许可

基准测试代码保留原有的 [MIT 许可](LICENSE)。FreePDK45 和 BSIM 源码适用各自的条款，详见[第三方说明](docs/THIRD_PARTY.md)。原始的两个本地目录没有改动。
