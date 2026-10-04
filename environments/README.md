# Reproducible environments

## Available: NumPy foundations

- Runtime validated: CPython 3.12.14, Linux x86_64, CPU.
- NumPy 2.3.5 and Matplotlib 3.10.8.
- [Direct dependencies](numpy-foundations.in).
- [Exact installed dependency versions](numpy-foundations-py312-linux.lock.txt), including transitive dependencies.
- [Setup instructions](../notebooks/numpy/01-ndarray/README.md) and [validation evidence](../validation/NP-01.md).

The lock records package versions, not wheel hashes or the OS image. It is a tested Linux/Python 3.12 environment, not a claim of bit-identical execution on every platform. Run `pip check` after installation. A browser notebook UI is not included; use an existing Jupyter installation or editor with the registered kernel.

## Still planned

A broader scientific computing environment including pandas, plus independent PyTorch and JAX environments. No versions for those future environments are declared validated. Documentation links using `stable` or `latest` remain entry points, not dependency locks.

Do not install or modify system drivers from a notebook. Add GPU profiles only after verification on target hardware. Record the versions actually executed, rather than assuming the latest version.

For each experiment: seed when randomness is used, data provenance/license, execution command, versions, hardware, observed duration, and peak memory if measured. Exact numerical reproducibility can vary by hardware, backend, and operation; document tolerances. Large datasets and weights stay out of Git, with explicit download instructions.
