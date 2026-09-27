# Circuit netlists / 电路网表

The CLI uses the four `freepdk45_*_circuit.cir` files as templates for DC, transient, AC and noise analyses. It copies a selected template into the output directory and replaces its model include with the model path you pass. 命令行以四个 `freepdk45_*_circuit.cir` 文件为模板，复制后再将模型引用替换为用户传入的路径。

The shorter `dc_circuit.cir`, `transient_circuit.cir`, `ac_circuit.cir` and `noise_circuit.cir` are retained from the earlier layout and reference the bundled FreePDK45 model. Other named circuits (Sky130, GF180, IHP) are examples requiring PDK files that are not included here. 其他以 Sky130、GF180、IHP 命名的示例电路需要仓库未附带的 PDK。
