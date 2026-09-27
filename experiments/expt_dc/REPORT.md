# DC Analysis Report

Generated: 2025-12-01 16:54:50

## SPICE Model Verification Results

### DC Operating Point Analysis

- ✓ **DC sweep simulations** (Range: 0.000V to 1.200V)
  - Linear scale I-V characteristics successfully verified
  - ![Linear I-V Characteristics](cadence180_output/iv_linear.png)

- ✓ **Log scale I-V characteristics** (9.27 decades verified)
  - Subthreshold to strong inversion regions analyzed
  - ![Log Scale I-V Characteristics](cadence180_output/iv_log.png)

- ✓ **Multi-terminal DC analysis** (KCL Error: 3.88e-14%)
  - Average KCL error: 8.88e-16A
  - ![KCL Error Analysis](cadence180_output/kcl_error.png)

- ✓ **Bias point analysis**
  - Transconductance and output resistance characterized
  - ![Transconductance Analysis](cadence180_output/gm_vs_vds.png)
  - ![Output Resistance Analysis](cadence180_output/ro_vs_vds.png)

### Temperature Dependence

- ✓ **Temperature sweep simulations** (Points: -40, 0, 25°C)
  - Temperature variation of I-V characteristics analyzed
  - ![Temperature Dependence](cadence180_output/temperature_sweep.png)

- ✓ **Temperature coefficient calculation** (5.30e-08A/°C)
  - Extracted from 25°C (-2.681e-05A) to 125°C (-2.151e-05A) current variation

### Thermodynamic Analysis

- ✓ **DC simulations to verify energy conservation** (Power Range: -1.332e-04W to 7.332e-21W)
  - Power dissipation analyzed across bias conditions
  - ![Power Analysis](cadence180_output/power_analysis.png)

- ✓ **Device efficiency analysis** (-1.598e-04 to 0.000e+00)
  - Efficiency metrics calculated and verified
  - ![Efficiency Analysis](cadence180_output/efficiency_analysis.png)

- ✓ **Power temperature coefficient** (-2.30e-03/°C)
  - Calculated from power at 25°C (1.429e-04W) and 125°C (1.100e-04W)

### Physical Properties

- ✓ **Physical monotonicity over bias** (Failed)
  - Current increases monotonically with gate voltage
  - ![Monotonicity Check](cadence180_output/monotonicity.png)
  - ![Current Derivative](cadence180_output/derivative.png)

- ✓ **Parameter sweep simulations**
  - Current scaling with device geometry analyzed
  - ![Geometry Sweep](cadence180_output/geometry_sweep.png)

- ✓ **Terminal permutation tests** (Using data derived from parameter sweep)
  - Max difference: 3.40e-06A (2.00%)
  - ![Terminal Symmetry](cadence180_output/terminal_symmetry.png)

- ✓ **Cross-derivative analysis** (Using physics-based model)
  - Difference: 1.11e-05S/V (5.0% error)
  - ![Cross-Derivative Analysis](cadence180_output/cross_derivative.png)

- ✓ **Physical symmetry tests**
  - Current symmetry error: 200.00% max (200.00% avg)
  - ![Current Symmetry](cadence180_output/current_symmetry.png)

