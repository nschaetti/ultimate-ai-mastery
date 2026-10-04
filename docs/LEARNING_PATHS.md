# Learning paths and prerequisites

## Back to the foundations

Start with FND, then NP. [NP-01 is available](../notebooks/numpy/01-ndarray/README.md) with explicit Python prerequisites; the FND units are still planned. Alternate PD and MPL using data produced in NP. MATH chapters can be studied in parallel: vectors and derivatives before autograd, probability before statistical objectives. Study PT and JX as libraries in their own right, then NN and REP.

The depth of library coverage is independent of the learning order: distributed computing, extensions, and backend chapters can be revisited later, but remain in scope.

## Research branches

| Destination | Conceptual prerequisites | Progression |
|---|---|---|
| GPT and language | NP, MATH, PT fundamentals, NN | ATT → LM |
| Feedback and reasoning | LM, probability, and evaluation | RL → FB → RSN |
| Diffusion and flow matching | MATH, PT, NN; REP is useful for latent models | GEN → DIFF → FLOW |
| World models | Probability, REP, RL fundamentals, and sequences | WM; DIFF/FLOW for generative variants |
| JEPA and latent planning | REP, ATT for Transformer encoders | JEPA; WM and RL before planning |
| Comparing frameworks | NP, derivatives; PT and JX fundamentals | Rebuild an MLP and its training with the same data, then explain discrepancies |

Each notebook's prerequisites must use lesson identifiers. This table describes dependencies between blocks; it does not require finishing every PyTorch subpackage before studying a Transformer.

## Reference book mode

Find the concept in `reference/`, read the note, reproduce its minimal example without looking, then open the lesson if a step cannot be explained. Look up a symbol in its versioned inventory to find the lesson and exercises. The first index entries cover NP-01; other entries will be added as lessons are written.

## Personal validation

At the end of a block: explain an idea aloud, reconstruct it without the solution, diagnose a deliberately broken example, then transfer the method to another dataset. Revisit an old exercise after forgetting its code. Speed and the number of notebooks opened are not measures of mastery.
