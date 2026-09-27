# BSIM3 3.3.0

**BSIM3 (Berkeley Short-channel IGFET Model) Version 3.3.0**

Released: July 29, 2005

## Description

BSIM3 is a physics-based, accurate, scalable, robust, and predictive MOSFET SPICE model developed by the BSIM Research Group at the University of California, Berkeley. It has been widely adopted by semiconductor and IC design companies worldwide for device modeling and CMOS IC design.

## Files

### Source Code
- `b3.c` - Main BSIM3 model implementation
- `b3acld.c` - AC load functions
- `b3ask.c` - Ask functions
- `b3check.c` - Parameter checking
- `b3cvtest.c` - CV test functions
- `b3del.c` - Delete functions
- `b3dest.c` - Destructor functions
- `b3getic.c` - Initial condition functions
- `b3ld.c` - Load functions
- `b3mask.c` - Mask functions
- `b3mdel.c` - Model delete functions
- `b3mpar.c` - Model parameter functions
- `b3noi.c` - Noise functions
- `b3par.c` - Parameter functions
- `b3pzld.c` - Pole-zero load functions
- `b3set.c` - Set functions
- `b3temp.c` - Temperature functions
- `b3trunc.c` - Truncation functions

### Header Files
- `bsim3def.h` - Main definitions header
- `bsim3itf.h` - Interface header

### Documentation
- `B330_Enhancement.pdf` - Enhancement documentation
- `bugfix_330.txt` - Bug fixes for version 3.3.0
- `Mod_doc/` - Model documentation directory
- `test/` - Test cases and examples

### Build Files
- `makedefs` - Make definitions
- `B3TERMS_OF_USE` - Terms of use

## Source

Downloaded from: https://www.bsim.berkeley.edu/models/bsim3/

## Usage

BSIM3 is a C-based SPICE model that needs to be compiled and integrated into a SPICE simulator. The model provides comprehensive MOSFET modeling capabilities including:

- Short-channel effects
- Subthreshold behavior
- Mobility degradation
- Velocity saturation
- Drain-induced barrier lowering (DIBL)
- Hot carrier effects
- Noise modeling

## Compilation

To compile BSIM3, you typically need to:
1. Include the source files in your SPICE simulator's build system
2. Link against the appropriate SPICE simulator libraries
3. Follow the specific integration instructions for your simulator

## Test Cases

The `test/` directory contains various test cases and examples demonstrating BSIM3 functionality, including:
- DC characteristics
- AC analysis
- Transient analysis
- Noise analysis
- Model parameter extraction

## Note

This is a legacy version of BSIM3. For newer applications, consider using BSIM4, BSIM-BULK, or other more recent BSIM models.

