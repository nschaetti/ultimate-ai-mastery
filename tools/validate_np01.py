"""Execute NP-01 solutions in a fresh kernel and record validation evidence."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys
import time
from datetime import datetime, timezone

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from ipykernel.inprocess.manager import InProcessKernelManager
from IPython.utils.capture import capture_output


def main():
    """Validate the chapter and write an executed solution and evidence report."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=None,
                        help="Executed solution path; defaults to the repository solution.")
    parser.add_argument("--engine", choices=("inprocess", "jupyter"), default="inprocess",
                        help="Fresh in-process kernel, or separate Jupyter kernel via IPC.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    chapter = root / "notebooks/numpy/01-ndarray"
    lesson = nbformat.read(chapter / "lesson.ipynb", as_version=4)
    solution = nbformat.read(chapter / "solution.ipynb", as_version=4)
    for notebook in (lesson, solution):
        nbformat.validate(notebook)
    learner_ids = [c.id for c in lesson.cells if "exercise" in c.metadata.get("tags", [])]
    solution_ids = [c.id for c in solution.cells if "solution" in c.metadata.get("tags", [])]
    assert learner_ids == solution_ids and len(learner_ids) == 9
    check_ids = [c.id for c in solution.cells if "check" in c.metadata.get("tags", [])]
    assert check_ids == [f"{eid}-check" for eid in learner_ids]
    source_hash = hashlib.sha256(json.dumps(
        [(c.id, c.cell_type, c.source) for c in solution.cells],
        ensure_ascii=False, separators=(",", ":"),
    ).encode()).hexdigest()
    for c in solution.cells:
        if c.cell_type == "code":
            c.outputs = []
            c.execution_count = None
    original_count = len(solution.cells)
    solution.cells.append(nbformat.v4.new_code_cell(
        "import json, resource, sys\n"
        "print(json.dumps({'kernel_executable': sys.executable, "
        "'kernel_peak_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}))",
        id="validation-resource-probe",
    ))
    started = time.perf_counter()
    if args.engine == "jupyter":
        # Use this environment's Python, never an unrelated installed kernel.
        manager = KernelManager(kernel_name="python3", transport="ipc")
        manager.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
        client = NotebookClient(solution, km=manager, timeout=120, allow_errors=False,
                                resources={"metadata": {"path": str(chapter)}})
        client.execute()
    else:
        # The CLI runs in a new process; the shell starts with no notebook state.
        manager = InProcessKernelManager()
        manager.start_kernel()
        shell = manager.kernel.shell
        try:
            for c in solution.cells:
                if c.cell_type != "code":
                    continue
                with capture_output() as captured:
                    result = shell.run_cell(c.source, store_history=True)
                result.raise_error()
                c.execution_count = shell.execution_count - 1
                c.outputs = []
                for name, content in (("stdout", captured.stdout), ("stderr", captured.stderr)):
                    if content:
                        c.outputs.append(nbformat.v4.new_output("stream", name=name, text=content))
                for rich in captured.outputs:
                    c.outputs.append(nbformat.v4.new_output(
                        "display_data", data=rich.data, metadata=rich.metadata))
        finally:
            manager.shutdown_kernel()
    elapsed = time.perf_counter() - started
    resource_text = "".join(o.get("text", "") for o in solution.cells[-1].outputs)
    resource_data = json.loads(resource_text)
    assert Path(resource_data["kernel_executable"]).absolute() == Path(sys.executable).absolute()
    solution.cells = solution.cells[:original_count]
    code_cells = [c for c in solution.cells if c.cell_type == "code"]
    assert all(c.execution_count is not None for c in code_cells)
    png_count = sum("image/png" in o.get("data", {}) for c in code_cells for o in c.outputs)
    assert png_count == 2, f"Expected two embedded figures, got {png_count}"
    assert not any(o.output_type == "error" for c in code_cells for o in c.outputs)
    solution.metadata.uam.status = "validated"
    output = args.output or chapter / "solution.ipynb"
    output.parent.mkdir(parents=True, exist_ok=True)
    nbformat.validate(solution)
    nbformat.write(solution, output)
    evidence = {
        "unit_id": "NP-01", "status": "passed",
        "validated_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(), "platform": platform.platform(),
        "machine": platform.machine(), "device": "CPU",
        "packages": {name: importlib.metadata.version(name) for name in
                     ("numpy", "matplotlib", "nbformat", "nbclient", "ipykernel")},
        "lock_sha256": hashlib.sha256((root / "environments/numpy-foundations-py312-linux.lock.txt").read_bytes()).hexdigest(),
        "solution_source_sha256": source_hash,
        "code_cells_executed": len(code_cells), "exercise_checks_passed": len(check_ids),
        "embedded_figures": png_count, "wall_seconds_including_kernel_start": round(elapsed, 3),
        "kernel_peak_rss_mib": round(resource_data["kernel_peak_rss_kib"] / 1024, 2),
        "memory_measurement": "Linux resource.ru_maxrss; includes imports and rendering and, for inprocess, the validator itself",
        "execution_engine": args.engine,
        "execution_limitations": "Separate Jupyter socket transport unavailable in the validation environment; in-process kernel checks cell execution, not a browser front end" if args.engine == "inprocess" else None,
        "command": f"python tools/validate_np01.py --engine {args.engine}",
        "learner_notebook": "Schema and exercise alignment validated; intentionally incomplete, not executed as a completed lesson",
    }
    evidence_path = root / "validation/NP-01.json"
    evidence_path.write_text(json.dumps(evidence, indent=2) + "\n")
    print(json.dumps(evidence, indent=2))


if __name__ == "__main__":
    main()
