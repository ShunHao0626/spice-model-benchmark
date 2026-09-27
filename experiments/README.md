# Standalone experiments / 独立实验

These scripts are exploratory work kept separate from the main `spice-benchmark` CLI. They may need manual setup or models that are not bundled. 这些脚本是独立探索工作，不属于主命令行流程；部分实验需要手动配置或另行取得模型。

| Folder | Topic / 主题 |
| --- | --- |
| [`expt_dc/`](expt_dc/) | DC analysis and model comparisons / 直流分析与模型比较 |
| [`expt_cv/`](expt_cv/) | Capacitance–voltage experiments / 电容–电压实验 |
| [`expt_tran/`](expt_tran/) | Transient and switching experiments / 瞬态与开关实验 |
| [`expt_noise/`](expt_noise/) | Noise analysis / 噪声分析 |
| [`expt_rel/`](expt_rel/) | Reliability and environment studies / 可靠性与环境实验 |

For an evidence-backed example, open the [FreePDK45 DC report](expt_dc/FREEPDK45_MODEL_RESULTS.md) and its linked `freepdk45_output/` files. Some cross-derivative and symmetry outputs use fallback calculations, as disclosed in the report. Most other generated experiment outputs remain in the original local folders.

可从附有 `freepdk45_output/` 数据和图表的 [FreePDK45 直流报告](expt_dc/FREEPDK45_MODEL_RESULTS.md)开始查看。部分交叉导数与对称性结果使用备用计算，报告中已有标注。其他大多数实验输出仍保存在原始本地目录。

The [Sky130 DC output archive](expt_dc/sky130_output/) is also included. Its PDK and full run log are not bundled, so treat these as historical data rather than a validated current run. 另收录 [Sky130 直流历史输出](expt_dc/sky130_output/)；由于没有附带 PDK 和完整运行日志，应将其视为历史数据，而非当前环境中已验证的运行结果。
