# Detailed curriculum

**NP-01 is validated** and available in the [chapter guide](../notebooks/numpy/01-ndarray/README.md); all other units are **planned**, not yet written. Each row is a learning unit that may require several notebooks. Stable identifiers will connect prerequisites, exercises, reference notes, and inventories. Specialized chapters remain in scope even when their implementation comes later.

The five library blocks are independent, in-depth learning paths. This curriculum organizes the material; only a versioned public API inventory can demonstrate exhaustive API coverage.

## FND — Scientific practice and Python

**Block prerequisites:** None; initial diagnostic.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| FND-01 | Environments and notebooks | Start from a fresh kernel, identify dependencies, and recognize hidden state. |
| FND-02 | Scientific Python | Master iterators, generators, context managers, functions, classes, and protocols used by scientific libraries. |
| FND-03 | Numerical testing | Compare exactness, tolerances, invariants, and property-based tests. |
| FND-04 | Reproducibility | Distinguish random seeds, determinism, and statistical variability. |
| FND-05 | Measurement and debugging | Measure time and memory without confusing compilation, transfers, and computation. |
| FND-06 | Reading a paper | Extract assumptions, objectives, protocols, and differences between the paper and its code. |

## NP — NumPy — mastering the library

**Block prerequisites:** FND; MATH as needed for each topic.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| [NP-01](../notebooks/numpy/01-ndarray/README.md) | The ndarray model — validated | Explain shape, ndim, size, axes, dtype, and memory representation. |
| NP-02 | Creation and conversion | Choose constructors, conversions, and array creation routines according to the required guarantees. |
| NP-03 | Types and promotion | Predict promotion, casting, overflow, and numerical precision. |
| NP-04 | Indexing and selection | Compare slicing, advanced indexing, masks, take, and updates. |
| NP-05 | Views, copies, and strides | Predict shared memory, contiguity, and the cost of a transformation. |
| NP-06 | Broadcasting and shapes | Derive compatible shapes and detect plausible but incorrect results. |
| NP-07 | Ufuncs and reductions | Use out, where, axes, reduce, accumulate, and floating-point error handling. |
| NP-08 | Assembly and organization | Compare reshape, transpose, stacking, splitting, repetition, and padding. |
| NP-09 | Mathematics, logic, and sets | Choose elementary, complex, bitwise, logical, and set operations. |
| NP-10 | Sorting, searching, and statistics | Analyze axes, stability, quantiles, histograms, NaN, and statistical conventions. |
| NP-11 | Linear algebra and contractions | Connect solve, decompositions, norms, matmul, tensordot, and einsum to their equations. |
| NP-12 | Random number generation | Use Generator, BitGenerator, distributions, and reproducible independent streams. |
| NP-13 | Fourier transforms and windows | Connect spectra, frequencies, normalization, symmetries, and windowing. |
| NP-14 | Polynomials and fitting | Compare polynomial bases, evaluation, differentiation, fitting, and conditioning. |
| NP-15 | Strings, dates, and structured arrays | Handle non-floating-point data and understand its limitations. |
| NP-16 | Masked arrays and extended domains | Compare masks, missing values, and functions with complex-valued domains. |
| NP-17 | Input/output and memmap | Choose formats, load data partially, and explain persistence and representation. |
| NP-18 | Typing, testing, and configuration | Use annotations, numerical assertions, options, and diagnostics. |
| NP-19 | Interoperability and extensions | Study array protocols, DLPack, F2PY, the C-API landscape, and Array API compatibility. |
| NP-20 | Specialized API audit | Reconcile all documented public sections and symbols in the selected version with their lessons. |

## PD — pandas — mastering the library

**Block prerequisites:** NP: arrays, types, and indexing.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| PD-01 | Series, DataFrame, and Index | Explain named axes, alignment, and differences from an ndarray. |
| PD-02 | Construction, types, and conversion | Choose nullable, categorical, and extension types. |
| PD-03 | Indexing and mutation | Master loc, iloc, filtering, alignment, and the selected version's copy semantics. |
| PD-04 | Missing values | Compare sentinels, propagation, detection, and imputation strategies. |
| PD-05 | Computation and statistics | Distinguish vectorized operations, apply, aggregation, and implicit alignment. |
| PD-06 | GroupBy | Build split-apply-combine operations, transform, filter, and multiple aggregations. |
| PD-07 | Joins and concatenation | Detect unexpected cardinality, missing keys, and duplicated rows. |
| PD-08 | Reshaping and MultiIndex | Move between long and wide formats using pivot, melt, stack, and unstack. |
| PD-09 | Text and categories | Use str and cat accessors, regular expressions, and ordered categories. |
| PD-10 | Time and time zones | Distinguish Timestamp, Timedelta, Period, resampling, and localization. |
| PD-11 | Windows | Compare rolling, expanding, and exponentially weighted operations. |
| PD-12 | Input/output | Review reading and writing interfaces and their optional dependencies. |
| PD-13 | Visualization and Styler | Separate graphical analysis, formatting, and table export. |
| PD-14 | Performance and memory | Measure the cost of types, indexes, and operations on large tables. |
| PD-15 | Extensions, options, and testing | Understand ExtensionArray, options, sparse objects, and pandas assertions. |
| PD-16 | API audit and migrations | Inventory methods, accessors, attributes, and version changes. |

## MPL — Matplotlib — mastering the library

**Block prerequisites:** NP: arrays; elementary statistics.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| MPL-01 | Figure, Axes, Axis, and Artist | Build a plot using the object-oriented API and explain the role of pyplot. |
| MPL-02 | Lines, markers, and errors | Choose Line2D, styles, error bars, and uncertainty representations. |
| MPL-03 | Statistical plots | Compare histograms, bar charts, scatter plots, boxplots, and violin plots. |
| MPL-04 | Images, grids, and contours | Choose imshow, pcolormesh, contour, and interpolation according to the data. |
| MPL-05 | Colors and normalization | Connect colormaps, norms, colorbars, and the perception of values. |
| MPL-06 | Axes, scales, and ticks | Control limits, scales, locators, formatters, units, and dates. |
| MPL-07 | Text and annotations | Configure fonts, mathtext, legends, annotations, and typography in exported figures. |
| MPL-08 | Figure layout | Master subplots, mosaics, GridSpec, and layout engines. |
| MPL-09 | Transformations and geometry | Move between data, axes, and figure coordinates; use paths and patches. |
| MPL-10 | Collections and specialized plots | Explain collections, triangulated plots, vector fields, and projections. |
| MPL-11 | Styles and configuration | Build a reproducible style using rcParams and local contexts. |
| MPL-12 | Animation and events | Update artists and handle events, widgets, and animation export. |
| MPL-13 | Backends and export | Distinguish interactive, raster, and vector output; choose DPI and formats. |
| MPL-14 | Toolkits | Explore mplot3d, axes_grid1, and axisartist and their limitations. |
| MPL-15 | Low-level API and audit | Map specialized modules, transformations, rendering, and remaining public APIs. |

## MATH — Mathematics for reconstructing models

**Block prerequisites:** NP in parallel.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| MATH-01 | Vectors, matrices, and spaces | Connect bases, projections, rank, and changes of coordinates. |
| MATH-02 | Decompositions and conditioning | Interpret eigenvalues, SVD, and the stability of a numerical solution. |
| MATH-03 | Differential calculus | Derive gradients, Jacobians, Hessians, and the chain rule with explicit dimensions. |
| MATH-04 | Probability | Work with conditioning, independence, Bayes' rule, and marginalization. |
| MATH-05 | Estimation and Monte Carlo | Compare bias, variance, intervals, and approximations of expectations. |
| MATH-06 | Information and likelihood | Derive log-likelihood, entropy, cross-entropy, and KL divergence. |
| MATH-07 | Optimization | Compare SGD, momentum, adaptive methods, and constraints. |
| MATH-08 | Elementary variational methods | Derive an ELBO and distinguish an approximation from an exact objective. |
| MATH-09 | ODEs, SDEs, and transport | Connect vector fields, numerical integration, and evolving densities. |

## PT — PyTorch — mastering the library

**Block prerequisites:** NP; MATH: derivatives for autograd.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| PT-01 | Tensors and devices | Master creation, types, devices, conversions, and shared memory. |
| PT-02 | Indexing and operations | Review Tensor operations, broadcasting, reductions, and mutation. |
| PT-03 | Autograd | Explain graphs, leaf tensors, accumulation, detach, and gradient contexts. |
| PT-04 | Advanced derivatives | Construct JVPs, VJPs, Hessians, and custom differentiable operations. |
| PT-05 | Modules and parameters | Understand nn.Module, buffers, parameters, hooks, and state_dict. |
| PT-06 | Layers and functional operations | Map nn and nn.functional, initializations, activations, and losses. |
| PT-07 | Optimizers and schedules | Examine state, parameter groups, zero_grad, and scheduling. |
| PT-08 | Data and parallel loading | Master Dataset, IterableDataset, DataLoader, collate, and workers. |
| PT-09 | Randomness and distributions | Compare sampling, reparameterization, RNG, and determinism. |
| PT-10 | Algebra, FFT, and specialized formats | Explore linalg, fft, sparse, quantized, and nested tensors as available in the selected version. |
| PT-11 | Precision and memory | Measure AMP, checkpointing, transfers, and tensor memory consumption. |
| PT-12 | Functional programming | Use torch.func for per-example gradients and vectorized transformations. |
| PT-13 | Compilation and export | Study compile, export, graph breaks, dynamic shapes, and legacy tools. |
| PT-14 | Profiling and benchmarking | Locate a bottleneck without confusing asynchronous execution with measured time. |
| PT-15 | Distributed computing | Understand collectives, DDP, sharding, and distributed checkpointing. |
| PT-16 | Serialization and deployment | Manage checkpoints, loading, interoperability, and export formats. |
| PT-17 | Backends and extensions | Explore accelerators, operator libraries, and C++/CUDA extensions. |
| PT-18 | Testing and module audit | Reconcile testing, utils, and all remaining public APIs with the inventory. |

## JX — JAX — mastering the library

**Block prerequisites:** NP; MATH: derivatives.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| JX-01 | Arrays and jax.numpy | Compare semantics, types, devices, immutability, and functional updates. |
| JX-02 | Pytrees and state | Represent parameters and state without hidden mutations. |
| JX-03 | Explicit randomness | Manage keys, split, distributions, and independent draws. |
| JX-04 | Differentiation | Compare grad, value_and_grad, jacfwd, jacrev, jvp, and vjp. |
| JX-05 | Compilation and tracing | Explain jit, static values, specialization, and recompilation. |
| JX-06 | Vectorization | Derive in_axes/out_axes and compose vmap with jit and grad. |
| JX-07 | Control flow and lax | Use cond, scan, loops, and primitives compatible with tracing. |
| JX-08 | Custom differentiation rules | Write custom_jvp/custom_vjp rules and verify their assumptions. |
| JX-09 | Networks, images, and scientific functions | Explore jax.nn, initializers, jax.image, and jax.scipy. |
| JX-10 | Placement and sharding | Understand meshes, partitioning, and multi-device computation. |
| JX-11 | Memory and precision | Study donation, remat, offloading, X64, and tolerances. |
| JX-12 | Debugging and profiling | Inspect runtime values, errors under transformations, and benchmark synchronization. |
| JX-13 | Export, stages, and interoperability | Study ahead-of-time compilation, export, DLPack, callbacks, and FFI. |
| JX-14 | Experimental APIs and kernels | Map experimental, sparse, and Pallas APIs for the selected version. |
| JX-15 | Extensions and internal representation | Read a jaxpr and locate jax.extend within the system without confusing public and internal APIs. |
| JX-16 | Module audit | Reconcile all documented symbols and their version changes. |

## NN — Neural networks

**Block prerequisites:** MATH; PT or JX fundamentals.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| NN-01 | Linear and logistic regression | Derive objectives and gradients, then compare with an analytical solution. |
| NN-02 | Miniature autograd | Implement a scalar engine, then connect its limitations to tensors. |
| NN-03 | MLPs and backpropagation | Reconstruct forward and backward passes with explicit dimensions. |
| NN-04 | Initialization and activations | Measure variance propagation and saturation. |
| NN-05 | Normalization and regularization | Compare batch/layer normalization, dropout, and penalties. |
| NN-06 | Optimization and diagnosis | Overfit a minibatch, then diagnose gradients and learning curves. |
| NN-07 | Convolutions | Derive padding, stride, receptive fields, and weight sharing. |
| NN-08 | Recurrence and memory | Compare RNNs, LSTMs, and GRUs on a temporal dependency task. |
| NN-09 | Generalization and calibration | Evaluate out-of-sample performance, data splitting, and confidence. |

## REP — Representations and self-supervision

**Block prerequisites:** NN; probability.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| REP-01 | Autoencoders | Distinguish reconstruction, compression, and useful representations. |
| REP-02 | Contrastive learning | Implement a contrastive loss and study temperature and negative examples. |
| REP-03 | Distillation and teachers | Compare stop-gradient, moving targets, and teacher-student learning. |
| REP-04 | Collapse | Construct a degenerate solution and test anti-collapse constraints. |
| REP-05 | Masked prediction | Compare prediction in input space and representation space. |
| REP-06 | Representation evaluation | Distinguish linear probing, fine-tuning, transfer, and information leakage. |

## ATT — Attention and Transformers

**Block prerequisites:** NN; NP: contractions.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| ATT-01 | Additive attention | Construct queries, keys, values, and alignment scores. |
| ATT-02 | Scaled dot-product attention | Derive scaling, softmax, masks, and gradients. |
| ATT-03 | Multi-head and cross-attention | Trace every dimension and test head mixing. |
| ATT-04 | Positions | Compare absolute and relative positions, RoPE, and positional biases. |
| ATT-05 | The Transformer block | Compare residual connections, pre/post-norm, and feed-forward networks. |
| ATT-06 | MQA and GQA | Quantify key/value sharing and cache size. |
| ATT-07 | Local and sparse attention | Construct connectivity patterns and analyze their effect on information flow. |
| ATT-08 | Linear attention | Understand factorizations, approximations, and differences from dense softmax attention. |
| ATT-09 | Efficient exact attention | Explain tiling, online softmax, and the principles of FlashAttention. |
| ATT-10 | Sequence modeling alternatives | Compare recurrence, state-space models, and hybrid architectures under controlled budgets. |

## LM — GPT and language models

**Block prerequisites:** ATT; statistical estimation.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| LM-01 | Tokenization | Implement a simple tokenizer and analyze segmentation and vocabulary. |
| LM-02 | Corpora and preparation | Document provenance, deduplication, splitting, and contamination. |
| LM-03 | Minimal GPT | Assemble a causal decoder-only model and verify the absence of future-token leakage. |
| LM-04 | Pretraining | Connect next-token prediction, batching, loss, and compute budget. |
| LM-05 | Sampling | Compare temperature, top-k, and top-p on controlled distributions. |
| LM-06 | Caching and inference | Verify matching logits with and without a KV cache and measure the memory trade-off. |
| LM-07 | Architectures and efficiency | Study normalizations, activations, MoE, and parameter-efficient adaptation. |
| LM-08 | Evaluation | Compare perplexity, downstream tasks, robustness, and benchmark limitations. |
| LM-09 | Multimodality | Connect encoders, projections, and mixed sequences in a small example. |

## RL — Reinforcement learning foundations

**Block prerequisites:** MATH: probability; NN.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| RL-01 | MDPs and partial observability | Distinguish state, observation, action, reward, and belief. |
| RL-02 | Values and Bellman equations | Solve a small tabular problem and verify the equations. |
| RL-03 | Policy gradients | Derive REINFORCE, baselines, and variance. |
| RL-04 | Actor-critic and PPO | Understand advantages, clipping, constraints, and on-policy data. |
| RL-05 | Off-policy learning and evaluation | Analyze distribution shift and the limitations of estimates. |
| RL-06 | Planning | Compare search, MPC, and a learned policy in the same environment. |

## FB — Feedback and post-training

**Block prerequisites:** LM; RL for reinforcement-based methods.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| FB-01 | Instruction tuning | Construct supervised examples, loss masks, and an evaluation protocol. |
| FB-02 | Preferences | Model comparisons, disagreements, and annotator biases. |
| FB-03 | Reward models | Train a preference score and analyze calibration and extrapolation. |
| FB-04 | RLHF | Connect the policy, reference model, reward, and KL penalty. |
| FB-05 | DPO | Derive the objective and make its assumptions and data requirements explicit. |
| FB-06 | Automated feedback | Compare verifiable rules, model judges, and human supervision. |
| FB-07 | Reward hacking | Construct an example in which optimizing a proxy degrades the actual objective. |
| FB-08 | Post-training evaluation | Separate quality, style, length, preferences, and robustness. |

## RSN — Reasoning models

**Block prerequisites:** LM, FB, and RL.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| RSN-01 | Tasks and protocols | Construct verifiable tasks and splits that prevent trivial memorization. |
| RSN-02 | Reasoning traces | Compare direct answers and explicit steps without equating text with internal mechanisms. |
| RSN-03 | Verification | Compare outcome and process supervision, errors, and annotation cost. |
| RSN-04 | Inference-time computation | Compare best-of-N, voting, and search at equal token budgets. |
| RSN-05 | Reinforcement learning with verifiable rewards | Implement a limited experiment and analyze GRPO-style advantages and normalizations. |
| RSN-06 | Distillation | Transfer solutions while controlling quality and contamination. |
| RSN-07 | Generalization | Measure length, difficulty, robustness, and out-of-distribution transfer. |
| RSN-08 | Critical reproduction | Distinguish published recipes, reproduced results, and unavailable information. |

## GEN — Generative models and latent variables

**Block prerequisites:** MATH, NN.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| GEN-01 | Densities and sampling | Distinguish density estimation, generation, and perceptual quality. |
| GEN-02 | VAEs | Derive the ELBO, reparameterization, and the role of the prior. |
| GEN-03 | Normalizing flows | Implement change of variables, coupling layers, and log-determinants. |
| GEN-04 | GANs and adversarial objectives | Understand the optimization game and diagnose mode collapse. |
| GEN-05 | Score matching | Connect log-density gradients and denoising objectives. |
| GEN-06 | Generative evaluation | Compare coverage, fidelity, metrics, and evaluation biases. |

## DIFF — Diffusion

**Block prerequisites:** GEN; ODEs/SDEs for advanced topics.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| DIFF-01 | The forward process | Derive noising, marginals, and schedules. |
| DIFF-02 | The reverse process | Connect denoising, the training objective, and predicted parameters. |
| DIFF-03 | Miniature DDPM | Learn a 2D distribution and visualize the reverse steps. |
| DIFF-04 | DDIM and solvers | Compare step counts, stochasticity, and numerical error. |
| DIFF-05 | Scores and SDEs | Connect discrete formulations, scores, and continuous dynamics. |
| DIFF-06 | Conditioning and guidance | Compare classifier guidance and classifier-free guidance. |
| DIFF-07 | Latent diffusion | Analyze the role of the autoencoder and information loss. |
| DIFF-08 | U-Net and DiT | Compare denoising architectures under a controlled protocol. |

## FLOW — Flow matching and transport

**Block prerequisites:** GEN; MATH: ODEs.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| FLOW-01 | Continuous transport | Derive the relationship between trajectories, velocity, and densities. |
| FLOW-02 | Conditional paths | Construct interpolation, noise, and velocity targets. |
| FLOW-03 | Conditional flow matching | Derive and implement the objective on a 2D distribution. |
| FLOW-04 | Couplings | Compare independent coupling and transport-oriented couplings. |
| FLOW-05 | Rectified flows | Study rectification, trajectories, and numerical cost. |
| FLOW-06 | Integration and generation | Measure quality and cost as a function of solver and number of evaluations. |
| FLOW-07 | Comparison with diffusion | Make shared parameterizations and differences in objectives explicit. |
| FLOW-08 | Conditioning and distillation | Test guidance and reductions in generation cost. |

## WM — World models — families and uses

**Block prerequisites:** REP, RL; sequences; DIFF/FLOW for generative variants.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| WM-01 | Defining the modeled world | Distinguish observation prediction, state dynamics, and models for control. |
| WM-02 | Deterministic dynamics | Learn transitions and analyze multi-step errors. |
| WM-03 | Probabilistic dynamics | Represent ambiguity, latent variables, and uncertainty. |
| WM-04 | Latent recurrent models | Reconstruct a miniature RSSM and its objectives. |
| WM-05 | Imagination and control | Compare planning within the model and a policy trained in imagination. |
| WM-06 | Token-based world models | Study quantization, sequences, and error accumulation. |
| WM-07 | Generative video models | Compare autoregression, diffusion, and flow matching for temporal prediction. |
| WM-08 | Actions and controllability | Test the effects of actions and interventions rather than visual quality alone. |
| WM-09 | Uncertainty and distribution | Measure drift, calibration, and out-of-distribution failure. |
| WM-10 | Comparative evaluation | Compare pixels, latent states, reward prediction, and control performance. |

## JEPA — JEPA and latent prediction

**Block prerequisites:** REP; ATT depending on the encoder; WM/RL for control.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| JEPA-01 | Predictive architecture | Define the context encoder, target encoder, predictor, and objective. |
| JEPA-02 | Masking and targets | Study prediction difficulty, stop-gradient, and teacher updates. |
| JEPA-03 | Preventing collapse | Analyze what does or does not prevent a constant representation. |
| JEPA-04 | Image JEPA | Build a miniature experiment and make deviations from I-JEPA explicit. |
| JEPA-05 | Video JEPA | Study temporal structure, targets, and representation evaluation. |
| JEPA-06 | Actions and latent planning | Formulate the additional components needed for control. |
| JEPA-07 | Controlled comparison | Compare reconstruction, contrastive learning, and latent prediction with fixed encoders and data. |
| JEPA-08 | Limitations and research | Test useful invariances, lost information, and generalization. |

## PRJ — Capstone projects

**Block prerequisites:** Branch-specific prerequisites.

| Unit | Chapter / subchapter | Observable objective |
|---|---|---|
| PRJ-01 | Libraries without scaffolding | Solve a numerical problem and produce a graphical report without copying a solution. |
| PRJ-02 | End-to-end GPT | Deliver a documented corpus, model, training, generation, and evaluation protocol. |
| PRJ-03 | Verifiable reasoning | Compare SFT, selection, and an RL method while controlling budgets. |
| PRJ-04 | Diffusion versus flow matching | Compare both using the same data, capacity, and evaluation budget. |
| PRJ-05 | A world model for control | Compare a learned model, an oracle model, and a model-free baseline. |
| PRJ-06 | JEPA versus reconstruction | Compare representations and downstream performance with ablations. |
| PRJ-07 | Reproducing a paper | Establish a reproduction plan, record deviations, and report negative results as well. |
