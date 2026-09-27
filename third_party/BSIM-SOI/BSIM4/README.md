# BSIM4 4.8.3

**BSIM4 (Berkeley Short-channel IGFET Model) Version 4.8.3**

Released: May 19, 2025

## Description

BSIM4 is a physics-based, accurate, scalable, robust, and predictive MOSFET SPICE model developed by the BSIM Research Group at the University of California, Berkeley. It addresses MOSFET physical effects into the sub-100nm regime and has been used for various technology nodes, including 0.13 µm, 90 nm, 65 nm, 45/40 nm, 23/28 nm, and 22/20 nm.

## Files

### Source Code (25 files)
- `b4.c` - Main BSIM4 model implementation
- `b4acld.c` - AC load functions
- `b4ask.c` - Ask functions
- `b4check.c` - Parameter checking
- `b4cvtest.c` - CV test functions
- `b4del.c` - Delete functions
- `b4dest.c` - Destructor functions
- `b4geo.c` - Geometry functions
- `b4getic.c` - Initial condition functions
- `b4ld.c` - Load functions
- `b4mask.c` - Mask functions
- `b4mdel.c` - Model delete functions
- `b4mpar.c` - Model parameter functions
- `b4noi.c` - Noise functions
- `b4par.c` - Parameter functions
- `b4pzld.c` - Pole-zero load functions
- `b4set.c` - Set functions
- `b4temp.c` - Temperature functions
- `b4trunc.c` - Truncation functions
- `devsup.c` - Device support functions
- `inp2m.c` - Input to model functions
- `inpdomod.c` - Input domain functions
- `inpfindl.c` - Input find functions
- `nevalsrc2.c` - Noise evaluation functions
- `noisean.c` - Noise analysis functions

### Header Files
- `bsim4def.h` - Main definitions header
- `bsim4ext.h` - External definitions header
- `bsim4itf.h` - Interface header

### Build Files
- `makedefs` - Make definitions

### Documentation
- `BSIM4_4.8.3_technical_manual.pdf` - Complete technical manual
- `BSIM4_4.8.3_update_document.pdf` - Update document compared to previous version

### License
- `LICENSE.txt` - License information
- `NOTICE.txt` - Notice file

## Source

Downloaded from: https://www.bsim.berkeley.edu/models/bsim4/

## Usage

BSIM4 is a C-based SPICE model that needs to be compiled and integrated into a SPICE simulator. The model provides comprehensive MOSFET modeling capabilities including:

- Sub-100nm MOSFET effects
- Short-channel effects
- Subthreshold behavior
- Mobility degradation
- Velocity saturation
- Drain-induced barrier lowering (DIBL)
- Hot carrier effects
- Noise modeling
- Self-heating effects
- Gate tunneling current
- Quantum mechanical effects

## Compilation

To compile BSIM4, you typically need to:
1. Include the source files in your SPICE simulator's build system
2. Link against the appropriate SPICE simulator libraries
3. Follow the specific integration instructions for your simulator

## Technology Nodes

BSIM4 has been validated and used for various technology nodes:
- 0.13 µm
- 90 nm
- 65 nm
- 45/40 nm
- 23/28 nm
- 22/20 nm

## Note

This is the latest version of BSIM4 as of May 2025, making it a very recent and up-to-date model for advanced MOSFET simulation.

