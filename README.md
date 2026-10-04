# Ultimate AI Mastery

A return to the foundations for rebuilding a deep understanding of artificial intelligence: scientific computing, libraries, neural networks, language models, reasoning, diffusion, flow matching, and world models.

This repository serves two purposes: **a guided notebook curriculum** and **a personal reference book to revisit an idea, derive it, and implement it again**. The target level is advanced master's/research; foundations are reconstructed without assuming they are still fresh.

## Start here

| Need | Entry point |
|---|---|
| Browse all chapters and their objectives | [Detailed curriculum](docs/CURRICULUM.md) |
| Choose a path and understand prerequisites | [Learning paths](docs/LEARNING_PATHS.md) |
| Review a concept or an API | [Reference book index](reference/README.md) |
| Check what “cover everything” means | [Coverage policy](coverage/README.md) and [domain matrix](coverage/DOMAINS.md) |
| Understand exercises and solutions | [Teaching guidelines](docs/PEDAGOGY.md) |
| Find the initial sources | [Annotated reading list](references/READING_LIST.md) |
| See the next concrete work item | [Roadmap](docs/ROADMAP.md) |

## Actual repository status

**NP-01 is available:** [ndarray, shapes, axes, and dtypes](notebooks/numpy/01-ndarray/README.md), with a guided lesson, nine exercises, worked solutions, and a review note. The solution passed all checks in a fresh in-process kernel; [validation details](validation/NP-01.md) record the environment and limitations.

The other 202 curriculum units remain planned. Templates are not completed lessons. A NumPy foundations environment is version-locked; other environments and exhaustive library symbol inventories remain to be established.

Each library has its own in-depth learning path: **NumPy, pandas, Matplotlib, PyTorch, and JAX**. Coverage is not limited to functions used in the AI projects. SciPy, tokenization tools, and related ecosystems will be explicitly added to the scope when a chapter requires them.

## Organization

- `notebooks/`: chapters; each lesson will have adjacent `lesson.ipynb` and `solution.ipynb` files.
- `reference/`: review notes, a concept index, and an API index.
- `coverage/`: domain coverage, followed by public symbol coverage for each version.
- `references/`: readings and the provenance of explanations.
- `templates/`: lesson, solution, and review-note templates.
- `docs/`: progression, prerequisites, teaching guidelines, and roadmap.
- `environments/`: reproducible environment policy.

All repository content is written in English, including explanations, exercises, solutions, reference notes, documentation, metadata, code comments, and docstrings. Experiments prioritize synthetic data and manageable sizes, followed by optional extensions. A miniature reproduction does not promise the performance of a large model.
