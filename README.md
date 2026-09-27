# SPICE Model Benchmark

**English** · [简体中文](README.zh-CN.md)

A curated record of MOSFET model integration and ngspice validation using an existing research benchmark. The toolkit runs DC, transient, AC and noise analyses and generates data, plots and verification reports.

## My contribution and provenance

My work in this project was obtaining and importing models, including FreePDK45 and BSIM-family models, running simulations, and organizing the resulting evidence. I did not write the core benchmark implementation or author the third-party device models. The benchmark code comes from the [SJTU-YONGFU-RESEARCH-GRP project](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark); this repository curates a local version together with model files, experiments and results. For a concrete example, see the [FreePDK45 DC analysis and its linked plots/data](experiments/expt_dc/FREEPDK45_MODEL_RESULTS.md). The [contribution and evidence guide](docs/CONTRIBUTION_AND_PROVENANCE.md) separates my role, upstream code and model authorship.

## Start here

**Want to try the benchmark?** Use the bundled FreePDK45 model and the command below. **Want to inspect past work?** Go to the [historical results index](archive/README.md). **Want to adapt a circuit or experiment?** See the [netlist index](netlists/README.md) and [experiment index](experiments/README.md).

Requirements: Python 3.8+ and `ngspice` available on your `PATH`. Run from a clone of this repository:

```bash
git clone https://github.com/ShunHao0626/spice-model-benchmark.git
cd spice-model-benchmark
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
spice-benchmark models/FreePDK45/nom.inc --modes dc --output-dir spice_benchmark_results
```

The command creates `spice_benchmark_results/REPORT.md`, `data/` and `plots/` under the selected output directory. Omit `--modes dc` to run all four analyses. The output directory is ignored by Git.

## Benchmark another model

The default circuits instantiate devices named `NMOS_VTG` and `PMOS_VTG` with FreePDK45 dimensions. Passing a different model file replaces the model include in **copies** of those circuits. Your model must define compatible device names and parameters.

For a different device topology or naming scheme, supply your own circuit files:

```bash
spice-benchmark path/to/model.inc --modes dc \
  --dc-circuit path/to/dc.cir --output-dir my_results
```

Custom circuits are used as written; include the desired model in each custom circuit. The CLI still requires an existing model-file argument. Default circuits are stored in the repository, so use an editable install from a source checkout; a non-editable wheel currently does not bundle them.

## Read the results

A successful process exit means the selected simulations and report generation completed. **It does not mean every verification check passed.** Read the detailed checks and measurements in `REPORT.md` before using a result as evidence. The files under [`archive/`](archive/README.md) are dated outputs from 2025, not results of the current checkout.

A smoke run of all four default modes on this consolidated checkout generated 33 data files, 22 plots and a report. Historical reports include failed and unfinished checks; those scientific outcomes have not been revalidated or repaired here.

## Repository guide

| Location | What you will find |
| --- | --- |
| [`src/spice_model_benchmark/`](src/spice_model_benchmark/) | CLI, ngspice runner, parsers, verification and plotting |
| [`netlists/`](netlists/README.md) | Default FreePDK45 circuits and optional PDK examples |
| [`models/FreePDK45/`](models/FreePDK45/) | Model required by the quick start |
| [`experiments/`](experiments/README.md) | Standalone DC, CV, transient, noise and reliability work |
| [`archive/`](archive/README.md) | Dated reports, data and plots from the source folders |
| [`third_party/`](third_party/README.md) | Separately licensed BSIM model source code |
| [`docs/`](docs/) | Methodology, [contribution and provenance](docs/CONTRIBUTION_AND_PROVENANCE.md), checklist and [source map](docs/SOURCE_MAP.md) |

The benchmark uses simulation-based checks; it does not implement AI/ML parameter extraction. Optional circuits for other PDKs require models that are not bundled. See the [consolidation source map](docs/SOURCE_MAP.md) for what was included or left out.

## License

The benchmark code retains its [MIT license](LICENSE). FreePDK45 and BSIM sources have their own terms; see [third-party notices](docs/THIRD_PARTY.md). The original two local folders were not modified.
