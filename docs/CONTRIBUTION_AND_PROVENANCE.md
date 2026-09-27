# Contribution and provenance / 贡献与来源

## English

### My role

I obtained and imported MOSFET model files, including FreePDK45, Sky130, GF180 and members of the BSIM family, configured the model inputs for the benchmark and standalone experiments, ran simulations, and organized the resulting reports, data and plots. These names are examples, not an exhaustive inventory. This repository presents that integration and validation workflow as my project contribution. I do not claim authorship of the core benchmark code or the third-party device models.

### Where the code and models came from

- **Benchmark code:** The `src/spice_model_benchmark/` implementation derives from the [SJTU-YONGFU-RESEARCH-GRP benchmark](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark). This repository consolidates a local snapshot and includes integration fixes; consult the upstream project for its current development history.
- **Device models:** The included FreePDK45 and BSIM files are third-party material; see [third-party notices](THIRD_PARTY.md). Sky130 and GF180 PDK files are not distributed here. Importing a model does not imply creating it.
- **Local consolidation:** The [source map](SOURCE_MAP.md) records how two local folders were combined and which files were retained.

### Inspectable example

| Step | Evidence in this repository |
| --- | --- |
| Model input | [`models/FreePDK45/nom.inc`](../models/FreePDK45/nom.inc) |
| Experiment setup | [`experiments/expt_dc/dc_analysis.cir`](../experiments/expt_dc/dc_analysis.cir) and [`dc_analyzer.py`](../experiments/expt_dc/dc_analyzer.py) |
| Report | [FreePDK45 DC analysis](../experiments/expt_dc/FREEPDK45_MODEL_RESULTS.md) |
| Archived outputs | [`experiments/expt_dc/freepdk45_output/`](../experiments/expt_dc/freepdk45_output/) contains the report's linked plots and data |

The FreePDK45 report records a December 2025 run. Its cross-derivative and symmetry sections include identified fallback calculations; these should not be described as wholly ngspice-derived validation. Other dated reports in [`archive/`](../archive/README.md) document historical runs and sometimes failed checks. The included BSIM files establish model availability, but this repository does not yet provide a complete, individually indexed BSIM run-to-result trail. Do not infer that every archived result is solely my work.

### Other named model work and current evidence

| Model family | What is available here | Limit |
| --- | --- | --- |
| Sky130 | [DC circuit](../netlists/sky130_dc_circuit.cir), [CV circuit](../experiments/expt_cv/cv_mos_sky130.cir), and [37 archived DC output files](../experiments/expt_dc/sky130_output/) copied from the original local folder | The Sky130 PDK and a complete run log are not bundled; these outputs have not been rerun or independently validated in this checkout. The folder includes explicitly named physics/derived fallback files. |
| GF180 | [DC circuit](../netlists/gf180_dc_circuit.cir) referring to a GF180 model | The GF180 PDK and a matched result set are not bundled, so this circuit alone is not evidence of a successful run. |
| BSIM family | [Imported model sources](../third_party/README.md) | A complete model-to-run-to-result index is not yet available. |

This table describes what a reader can inspect in this repository. It does not limit the broader model work described above.

## 简体中文

### 我的工作

我负责获取及导入 MOSFET 模型文件，包括 FreePDK45、Sky130、GF180 和 BSIM 系列中的模型；配置基准程序及独立实验所需的模型输入，运行仿真，并整理报告、数据和图表。这些名称只是举例，并非全部模型。本仓库用这些材料展示我的模型集成与验证工作。我不将基准程序核心代码或第三方器件模型标为自己编写。

### 代码与模型来源

- **基准代码：** `src/spice_model_benchmark/` 源于 [SJTU-YONGFU-RESEARCH-GRP 的基准项目](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark)。本仓库整理的是一个本地版本，并包含模型集成相关修正；最新开发历史请以上游仓库为准。
- **器件模型：** 仓库收录的 FreePDK45 与 BSIM 文件属于第三方材料，相关条款见[第三方说明](THIRD_PARTY.md)。Sky130 与 GF180 PDK 文件未在此发布。导入模型不代表编写模型。
- **本地整理：** [来源映射](SOURCE_MAP.md)说明两个本地目录如何合并，以及纳入了哪些文件。

### 可查看的案例

| 步骤 | 仓库中的证据 |
| --- | --- |
| 模型输入 | [`models/FreePDK45/nom.inc`](../models/FreePDK45/nom.inc) |
| 实验设置 | [`experiments/expt_dc/dc_analysis.cir`](../experiments/expt_dc/dc_analysis.cir) 与 [`dc_analyzer.py`](../experiments/expt_dc/dc_analyzer.py) |
| 报告 | [FreePDK45 直流分析](../experiments/expt_dc/FREEPDK45_MODEL_RESULTS.md) |
| 历史输出 | [`experiments/expt_dc/freepdk45_output/`](../experiments/expt_dc/freepdk45_output/) 包含报告引用的数据与图表 |

FreePDK45 报告记录了 2025 年 12 月的运行结果。其中交叉导数与对称性部分含有已标明的备用计算，不能把整份报告描述为完全由 ngspice 仿真得到的验证结果。[`archive/`](../archive/README.md)中的其他历史报告有些包含未通过的检查。仓库提供了 BSIM 模型文件，但尚未为每次 BSIM 运行建立完整的模型到结果索引，也不能据此将所有历史输出都归为我个人完成。

### 其他模型工作与当前证据

| 模型系列 | 仓库中可查看的材料 | 当前限制 |
| --- | --- | --- |
| Sky130 | [直流电路](../netlists/sky130_dc_circuit.cir)、[CV 电路](../experiments/expt_cv/cv_mos_sky130.cir)及从原始本地目录复制的 [37 个直流历史输出文件](../experiments/expt_dc/sky130_output/) | 未收录 Sky130 PDK 和完整运行日志；这些输出没有在当前仓库重新运行或独立验证。目录中含有明确命名的物理模型及衍生备用数据。 |
| GF180 | 引用了 GF180 模型的[直流电路](../netlists/gf180_dc_circuit.cir) | 未收录 GF180 PDK 和对应结果；仅有电路文件不能证明仿真已成功运行。 |
| BSIM 系列 | [已导入的模型源码](../third_party/README.md) | 尚无完整的模型、运行与结果对应索引。 |

此表只说明读者目前能在本仓库直接查看的材料，不限定上述模型工作范围。
