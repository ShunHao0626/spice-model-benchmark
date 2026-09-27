# SPICE Model Benchmark

A research-oriented ngspice benchmark for MOSFET models. It runs DC, transient, AC, and noise circuits, reads their outputs, produces plots, and writes a verification report.

This repository consolidates two local research folders: the later Python benchmark implementation from `spice_model_benchmark_old` and the distinct BSIM model sources and August 2025 results from `SJTU`. The original folders were not modified. See [source map](docs/SOURCE_MAP.md) for exactly what was included.

## Quick start

Requirements: Python 3.8+ and `ngspice` on your `PATH`.

```bash
git clone https://github.com/ShunHao0626/spice-model-benchmark.git
cd spice-model-benchmark
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
spice-benchmark models/FreePDK45/nom.inc --modes dc --output-dir spice_benchmark_results
```

The report is written to `spice_benchmark_results/REPORT.md`, with raw data under `data/` and plots under `plots/`. Run all four modes by omitting `--modes`.

The bundled default circuits use the FreePDK45 `NMOS_VTG` and `PMOS_VTG` device names and dimensions. Passing another model file replaces the model include in copies of those circuits; that model must define compatible device names. For a different topology or naming scheme, pass your own circuit files using `--dc-circuit`, `--transient-circuit`, `--ac-circuit`, and/or `--noise-circuit`. Custom circuits are used as provided and should include their model explicitly.

The command-line implementation expects a source checkout because the default netlists live at repository level. A non-editable wheel installation does not bundle these netlists.

## Layout

| Path | Purpose |
| --- | --- |
| `src/spice_model_benchmark/` | Python package: simulation, parsing, verification, plots, CLI |
| `netlists/` | Default FreePDK45 circuits and examples for other PDKs |
| `models/FreePDK45/` | Redistributable model needed for the quick start |
| `experiments/` | Selected independent DC, CV, noise, reliability, and transient experiment code |
| `archive/` | Historical outputs from May, June, and August 2025; not current test results |
| `third_party/` | Separately licensed BSIM model source code |
| `docs/` | Benchmark notes, methodology, and source map |

## Status

All four default modes were smoke-tested together on the consolidated checkout with ngspice: the run generated 33 data files, 22 plots, and a report. Execution success does not mean every verification criterion passed. The archived reports have not been revalidated as a complete suite. Historical reports contain some failed or incomplete checks; read their detailed sections before citing a result. This is a benchmark and experiment collection, not an AI/ML parameter extractor.

## License and sources

The benchmark's top-level code retains its original [MIT license](LICENSE). Files in `models/FreePDK45/` and `third_party/` retain their own license notices; the MIT license does not replace those terms. See [third-party sources](docs/THIRD_PARTY.md).
