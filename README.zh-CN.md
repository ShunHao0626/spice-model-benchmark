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
