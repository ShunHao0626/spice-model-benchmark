# BSIM-CMG 112.0.0

**BSIM-CMG (Common Multi-Gate) Model Version 112.0.0**

Released: December 26, 2024

## Description

BSIM-CMG is a compact model designed for common multi-gate field-effect transistors (FETs), including double-, triple-, and all-around-gate FinFETs. This model provides physical surface-potential-based formulations for both intrinsic and extrinsic models with finite body doping.

## Files

- `bsimcmg.va` - Main Verilog-A model file
- `bsimcmg_body.include` - Body effect calculations
- `bsimcmg_checking.include` - Parameter checking routines
- `bsimcmg_initialization.include` - Model initialization
- `bsimcmg_macros.include` - Macro definitions
- `bsimcmg_noise.include` - Noise modeling
- `bsimcmg_parameters.include` - Parameter definitions
- `bsimcmg_variables.include` - Variable declarations

## Documentation

- `BSIM-CMG_112.0.0_Technical_Manual.pdf` - Complete technical manual
- `BSIM-CMG_112.0.0_Updates.pdf` - Release notes and updates

## License

See `LICENSE.txt` for licensing information.

## Source

Downloaded from: https://www.bsim.berkeley.edu/models/bsimcmg/

## Usage

Include the main model file `bsimcmg.va` in your SPICE simulator. The model supports various multi-gate transistor configurations and is compatible with most commercial SPICE simulators.

For detailed usage instructions, refer to the technical manual.

