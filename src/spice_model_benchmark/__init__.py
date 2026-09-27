"""SPICE model benchmark package and convenience entry point."""

from pathlib import Path
from typing import List, Optional, Union
import re

from .data_reader import DataReader
from .logger import Logger
from .mosfet_simulation import MOSFETSimulation
from .plot_generator import PlotGenerator
from .simulation_runner import SimulationRunner
from .verification_manager import VerificationManager

__version__ = "1.0.0"
__all__ = [
    "MOSFETSimulation", "Logger", "SimulationRunner", "DataReader",
    "PlotGenerator", "VerificationManager", "benchmark_spice_model",
]

_MODES = ("dc", "transient", "ac", "noise")
_INCLUDE = re.compile(r"^\s*\.inc(?:lude)?\s+.*$", re.IGNORECASE | re.MULTILINE)


def _prepare_default_circuit(template: Path, model_file: Path, target: Path) -> Path:
    """Make a copy of a bundled circuit with the selected model included."""
    circuit = template.read_text(encoding="utf-8")
    if not _INCLUDE.search(circuit):
        raise ValueError(f"No model include directive found in {template}")
    if "\n" in str(model_file) or "\r" in str(model_file) or '"' in str(model_file):
        raise ValueError("Model path contains a character unsupported by SPICE includes")
    circuit = _INCLUDE.sub(lambda _: f'.inc "{model_file}"', circuit, count=1)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(circuit, encoding="utf-8")
    return target


def benchmark_spice_model(
    model_file: Union[str, Path],
    output_dir: Union[str, Path] = "spice_benchmark_results",
    modes: Optional[List[str]] = None,
    dpi: int = 300,
    log_level: str = "INFO",
    dc_circuit: Optional[Union[str, Path]] = None,
    transient_circuit: Optional[Union[str, Path]] = None,
    noise_circuit: Optional[Union[str, Path]] = None,
    ac_circuit: Optional[Union[str, Path]] = None,
) -> bool:
    """Run the selected analyses with default or caller-provided SPICE circuits.

    Default circuits are copied into the output directory with their model include
    replaced by ``model_file``. Custom circuits are used as supplied; put the
    desired model include in each custom circuit.
    """
    model_path = Path(model_file).expanduser().resolve()
    if not model_path.is_file():
        raise FileNotFoundError(f"SPICE model file not found: {model_path}")

    selected = list(_MODES) if modes is None or modes == ["all"] else list(modes)
    if not selected or any(mode not in _MODES for mode in selected):
        raise ValueError(f"modes must contain one or more of: {', '.join(_MODES)}")

    output_path = Path(output_dir).expanduser().resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    templates = Path(__file__).resolve().parents[2] / "netlists"
    custom = {
        "dc": dc_circuit, "transient": transient_circuit,
        "ac": ac_circuit, "noise": noise_circuit,
    }
    circuits = {}
    for mode in selected:
        if custom[mode] is not None:
            circuit = Path(custom[mode]).expanduser().resolve()
            if not circuit.is_file():
                raise FileNotFoundError(f"Custom {mode} circuit not found: {circuit}")
        else:
            template = templates / f"freepdk45_{mode}_circuit.cir"
            if not template.is_file():
                raise FileNotFoundError(f"Default {mode} circuit not found: {template}")
            circuit = _prepare_default_circuit(
                template, model_path, output_path / "_netlists" / template.name
            )
        circuits[mode] = str(circuit)

    simulation = MOSFETSimulation(
        dc_circuit_file=circuits.get("dc"),
        transient_circuit_file=circuits.get("transient"),
        ac_circuit_file=circuits.get("ac"),
        noise_circuit_file=circuits.get("noise"),
        output_dir=str(output_path),
        dpi=dpi,
        log_level=log_level,
    )
    return simulation.run(modes=selected)
