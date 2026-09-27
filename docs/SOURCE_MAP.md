# Consolidation source map

The new repository was assembled from two local folders without copying either folder's `.git` history or altering the source folders.

| New location | Source |
| --- | --- |
| `src/spice_model_benchmark/`, `examples/`, `netlists/`, `docs/` | `spice_model_benchmark_old` working tree (November 2025 generation) |
| `models/FreePDK45/` | `spice_model_benchmark_old/models/FreePDK45/` |
| `experiments/` | Selected scripts, circuits, and instructions from `spice_model_benchmark_old/sandbox/` |
| `experiments/expt_dc/freepdk45_output/` | Data and plots referenced by the FreePDK45 DC report, from `spice_model_benchmark_old/sandbox/expt_dc/freepdk45_output/` |
| `archive/reference-results-2025-05/` | `spice_model_benchmark_old/reference_results/` |
| `archive/results-2025-06/` | `spice_model_benchmark_old/results/` |
| `archive/sjtu-results-2025-08/` | `SJTU/results/` |
| `third_party/` | BSIM-BULK, BSIM-CMG, BSIM-SOI, and BSIM3 source from `SJTU/` |

The old working tree contained local modifications relative to its Git commit; this consolidation used the files present on disk. The `SJTU/spice_model_benchmark/` directory was a partial checkout with its own benchmark `src/` and `netlists/` absent from the working tree, so its duplicate benchmark code was not used. Its historical results were retained under `archive/`. Personal absolute checkout paths in copied Markdown reports and notes were normalized to `<original-checkout>`.

To keep the repository practical and suitable for public access, the following were not copied: the 14 GB PDK tree, the 1.7 GB model tree other than FreePDK45, vendor-specific Cadence and Synopsys examples, nested Git repositories, virtual environments, logs, most experiment-generated output, duplicate PDFs, PDK-specific `.spiceinit` files, and the top-level paper PDFs in `SJTU/`. These remain in the original local folders. Some optional netlists in `netlists/` reference PDKs that are not bundled and require the user to obtain those PDKs independently.

The consolidated code also repairs the default-circuit path and connects the CLI model argument to the copied default netlists. It does not claim that all historical verification failures have been resolved.
