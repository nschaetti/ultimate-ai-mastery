# Reproducible environments

Status: to be established. No set of versions has yet been installed and validated for the curriculum. The reading list's `stable` and `latest` links are entry points, not dependency locks.

Plan a scientific computing/NumPy/pandas/Matplotlib environment, a PyTorch environment, and a JAX environment, each with an identifiable Jupyter kernel. This allows their acceleration requirements to be managed independently. Do not install or modify system drivers from a notebook.

Before the first validated chapter, create dependency files and exact locks; test imports and a representative CPU operation. Add GPU profiles only after verification on the target hardware. Chapters must record the versions actually executed, not the version assumed to be the latest.

For each experiment: seed, data provenance/license, execution command, versions, hardware, observed duration, and peak memory if measured. Exact numerical reproducibility can vary by hardware, backend, and operation; document tolerances. Large datasets and weights stay out of Git. Their download must be explicit.
