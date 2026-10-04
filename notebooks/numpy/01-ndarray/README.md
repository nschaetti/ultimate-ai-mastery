# NP-01 — The ndarray: shapes, axes, and dtypes

[Lesson](lesson.ipynb) · [Worked solutions](solution.ipynb) · [Review note](../../../reference/numpy/ndarray-shapes-axes-dtypes.md) · [Validation evidence](../../../validation/NP-01.md)

This chapter rebuilds the array mental model through explanations, equations, worked examples, nine coding exercises, progressive hints, independent checks, two diagnostic figures, and a final image preprocessing exercise.

## Study workflow

1. Open `lesson.ipynb` and run the setup cell in the pinned environment.
2. Predict shapes and values before running worked examples.
3. Replace each exercise's `NotImplementedError`, then run its check cell.
4. Use hints only when needed; consult the adjacent solution for reasoning and common mistakes.
5. Reconstruct the review note from memory, then compare.

The incomplete learner notebook is intentionally not a successful “Run All” notebook. `solution.ipynb` is the complete executable version and retains compact outputs, including two figures, for reading on GitHub. Neither notebook downloads data or uses a GPU.

## Local environment

Validated on **CPython 3.12.14, Linux x86_64**, with NumPy **2.3.5** and Matplotlib **3.10.8**. The lock includes execution and notebook-validation dependencies. It does not install a browser UI; use an existing Jupyter or notebook-capable editor.

From the repository root:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r environments/numpy-foundations-py312-linux.lock.txt
.venv/bin/python -m pip check
.venv/bin/python -m ipykernel install --user --name uam-numpy --display-name "Ultimate AI Mastery — NumPy"
```

Select that kernel in your notebook editor. The notebook checks the NumPy and Matplotlib versions. Other operating systems or Python versions may work, but were not validated by this run. The versioned NumPy documentation covers the 2.3 release series, while the runtime lock selects patch 2.3.5.

## Reproduce validation

```bash
.venv/bin/python tools/validate_np01.py
```

The validator starts a fresh in-process IPython kernel inside the newly launched Python process, executes every solution cell without allowing errors, verifies all nine checks and both figure outputs, and updates `solution.ipynb` and `validation/NP-01.json`. It needs no network sockets. `--engine jupyter` selects a separate kernel over local IPC; that mode could not run in the validation environment because socket creation is restricted. `--output /tmp/np01-solution.ipynb` writes the executed notebook elsewhere; the JSON evidence still updates in the repository. The human-readable report summarizes the recorded run and must be reviewed when evidence changes.

The reported wall time includes kernel startup and rendering. Peak memory describes the Python process on Linux, including the validator for in-process execution, not just array storage. This is a small correctness experiment, not a performance benchmark.

## Exercise map

| ID | Task | Main failure caught |
|---|---|---|
| E01 | Inspect array metadata | Confusing first-axis length and total size |
| E02 | Build row and column shapes | Treating a vector transpose as a column |
| E03 | Derive reduction shapes | Keeping the axes meant to be reduced |
| E04 | Compute sensor means | Averaging channels instead of batch/time |
| E05 | Permute image layout | Reshaping into the right shape but wrong values |
| E06 | Choose signed integer storage | Missing inclusive limits or sign requirements |
| E07 | Normalize uint8 data | Integer division, wrong dtype, or input mutation |
| E08 | Compare precision paths | Expecting widening to restore lost information |
| E09 | Compose preprocessing | Mixing statistics, dtype, or layout contracts |

API coverage is recorded in the [chapter ledger](../../../coverage/numpy/2.3.5-NP-01.json). It is a curated lesson-level record, not an exhaustive NumPy symbol inventory.
