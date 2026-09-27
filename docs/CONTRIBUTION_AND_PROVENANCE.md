# Contribution and provenance / 贡献与来源

## English

### My role

I obtained and imported MOSFET model files, including FreePDK45 and members of the BSIM family, configured the model inputs for the benchmark and standalone experiments, ran simulations, and organized the resulting reports, data and plots. This repository presents that integration and validation workflow as my project contribution. I do not claim authorship of the core benchmark code or the third-party device models.

### Where the code and models came from

- **Benchmark code:** The `src/spice_model_benchmark/` implementation derives from the [SJTU-YONGFU-RESEARCH-GRP benchmark](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark). This repository consolidates a local snapshot and includes integration fixes; consult the upstream project for its current development history.
- **Device models:** FreePDK45 and BSIM files are third-party material. Their accompanying terms are summarized in [third-party notices](THIRD_PARTY.md). Importing a model does not imply creating it.
- **Local consolidation:** The [source map](SOURCE_MAP.md) records how two local folders were combined and which files were retained.

### Inspectable example

| Step | Evidence in this repository |
| --- | --- |
| Model input | [`models/FreePDK45/nom.inc`](../models/FreePDK45/nom.inc) |
| Experiment setup | [`experiments/expt_dc/dc_analysis.cir`](../experiments/expt_dc/dc_analysis.cir) and [`dc_analyzer.py`](../experiments/expt_dc/dc_analyzer.py) |
| Report | [FreePDK45 DC analysis](../experiments/expt_dc/FREEPDK45_MODEL_RESULTS.md) |
| Archived outputs | [`experiments/expt_dc/freepdk45_output/`](../experiments/expt_dc/freepdk45_output/) contains the report's linked plots and data |

The FreePDK45 report records a December 2025 run. Its cross-derivative and symmetry sections include identified fallback calculations; these should not be described as wholly ngspice-derived validation. Other dated reports in [`archive/`](../archive/README.md) document historical runs and sometimes failed checks. The included BSIM files establish model availability, but this repository does not yet provide a complete, individually indexed BSIM run-to-result trail. Do not infer that every archived result is solely my work.

## 简体中文

### 我的工作

我负责获取及导入 MOSFET 模型文件，包括 FreePDK45 和 BSIM 系列中的模型；配置基准程序及独立实验所需的模型输入，运行仿真，并整理报告、数据和图表。本仓库用这些材料展示我的模型集成与验证工作。我不将基准程序核心代码或第三方器件模型标为自己编写。

### 代码与模型来源

- **基准代码：** `src/spice_model_benchmark/` 源于 [SJTU-YONGFU-RESEARCH-GRP 的基准项目](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark)。本仓库整理的是一个本地版本，并包含模型集成相关修正；最新开发历史请以上游仓库为准。
- **器件模型：** FreePDK45 与 BSIM 文件属于第三方材料，相关条款见[第三方说明](THIRD_PARTY.md)。导入模型不代表编写模型。
- **本地整理：** [来源映射](SOURCE_MAP.md)说明两个本地目录如何合并，以及纳入了哪些文件。

### 可查看的案例

| 步骤 | 仓库中的证据 |
| --- | --- |
| 模型输入 | [`models/FreePDK45/nom.inc`](../models/FreePDK45/nom.inc) |
| 实验设置 | [`experiments/expt_dc/dc_analysis.cir`](../experiments/expt_dc/dc_analysis.cir) 与 [`dc_analyzer.py`](../experiments/expt_dc/dc_analyzer.py) |
| 报告 | [FreePDK45 直流分析](../experiments/expt_dc/FREEPDK45_MODEL_RESULTS.md) |
| 历史输出 | [`experiments/expt_dc/freepdk45_output/`](../experiments/expt_dc/freepdk45_output/) 包含报告引用的数据与图表 |

FreePDK45 报告记录了 2025 年 12 月的运行结果。其中交叉导数与对称性部分含有已标明的备用计算，不能把整份报告描述为完全由 ngspice 仿真得到的验证结果。[`archive/`](../archive/README.md)中的其他历史报告有些包含未通过的检查。仓库提供了 BSIM 模型文件，但尚未为每次 BSIM 运行建立完整的模型到结果索引，也不能据此将所有历史输出都归为我个人完成。
