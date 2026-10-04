# Initial annotated reading list

Entry points accessed on **October 4, 2026**. This list starts the curriculum; it is neither exhaustive nor a certification that the papers have been read in full. Future lessons will add precise references near claims, sections to read, and the versions used. The `stable`/`latest` indexes change over time: they must be replaced or accompanied by fixed references in the inventories.

## Libraries — official documentation

| Source | Intended use | Reading guidance |
|---|---|---|
| [NumPy reference](https://numpy.org/doc/stable/reference/index.html) | NP and API inventory | Start with ndarray, dtypes, and ufuncs; then work through topic-based routines and subpackages. |
| [PyTorch documentation](https://docs.pytorch.org/docs/stable/index.html) | PT and model implementations | Connect tensor, autograd, and module APIs to exercises; inventory specialized components separately. |
| [JAX API reference](https://docs.jax.dev/en/latest/jax.html) | JX and functional transformations | Start with arrays, transformations, and pytrees; deepen coverage of lax, sharding, export, and extensions in the relevant chapters. |
| [Matplotlib API](https://matplotlib.org/stable/api/index.html) | MPL and diagnostics | Read the object-oriented interfaces, then artists and specialized modules; connect each figure to its object model. |
| [pandas API reference](https://pandas.pydata.org/docs/reference/index.html) | PD and data preparation | Structure the inventory around Series, DataFrame, Index, accessors, windows, IO, and extensions. |

## Starting papers — primary sources

| Reference | Block | Reading question |
|---|---|---|
| Vaswani et al., 2017 — [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | ATT | How do attention, positions, feed-forward networks, and residual connections fit together? Reconstruct the block's dimensions. |
| Ouyang et al., 2022 — [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) | FB | Which data and objectives distinguish SFT, reward modeling, and policy optimization? |
| Rafailov et al., 2023 — [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | FB | Which assumptions allow the preference objective to be reformulated? |
| DeepSeek-AI et al., 2025 — [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | RSN | Distinguish reported recipes, the authors' evaluations, and what our small experiment can test. |
| Ho et al., 2020 — [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | DIFF | Connect the forward process, reverse process, and denoising target. |
| Lipman et al., 2022 — [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | FLOW | Why can a velocity field be learned from conditional paths? |
| Hafner et al., 2023 — [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) | WM | Separate dynamics learning, imagination, and behavior learning. |
| Assran et al., 2023 — [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243) | JEPA | Identify the predicted targets, masking, and representation learning mechanisms. |

The years above refer to the first arXiv version, not necessarily the year of conference or journal publication. Before reproducing a method, choose a specific revision and check the authors' code. Detailed section references are not provided until the corresponding full text has been studied.

## Readings to add

Chapter-specific bibliographies for autograd, contrastive learning, distillation, attention variants, RL, VAEs, score matching, rectified flows, video world models, and video/action JEPA variants will be established as those chapters are written. Their absence here does not exclude them from the curriculum.

## NP-01 — versioned chapter sources

NP-01 uses the NumPy 2.3 documentation and executes against NumPy 2.3.5. Its [lesson](../notebooks/numpy/01-ndarray/lesson.ipynb) links each explanation to the relevant API page and closes with essential and further readings. The [review note](../reference/numpy/ndarray-shapes-axes-dtypes.md) retains the principal sources for quick consultation. The global `stable` index above is not the version lock for this chapter.
