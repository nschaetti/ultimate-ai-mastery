# Teaching guidelines

## Understand, reconstruct, revisit

A lesson must answer four questions: what problem are we solving, how does the method work, how can we reconstruct it, and when does it fail? The review note supports a quick revisit; the notebook contains the derivation and experiments. A note always links to its lesson and sources. “Feynman book” here refers to this personal practice of reconstruction and explanation, without attributing a specific method to Feynman.

## Anatomy of a lesson

1. A stable identifier, observable objectives, exact prerequisites, and a link to the solution.
2. Versions, hardware, data, a resource budget measured after execution, and experimental limitations.
3. A concrete problem and a prediction to write before running the code.
4. An intuitive explanation and a fully worked minimal example.
5. A derivation: symbols, dimensions, assumptions, intermediate steps, and edge cases.
6. Graded exercises: recognize, derive, implement, diagnose, and transfer.
7. Tests of properties, edge cases, and an independent reference where possible.
8. An experiment with a baseline, a controlled variable, visualization, and interpretation.
9. An ablation or counterexample; distinguish observation from a proposed explanation.
10. A learner-written summary without copying formulas from the lesson.
11. A review note and essential/advanced readings with specific sections to read.

## Exercises and hints

Cells to complete carry the `exercise` tag and an identifier such as `NP-04-E02`. Use `raise NotImplementedError("NP-04-E02")` for incomplete functions, never a silently incorrect implementation. Verification cells carry the `check` tag. Open-ended questions carry `reflection` and ask for justification rather than a single expected answer.

Three progressive hints can appear in collapsible Markdown blocks: a useful idea, an approach, and pseudocode. The full solution stays in the adjacent file. Exercises must address mechanisms, not copying an example or memorizing a signature.

An incomplete learner notebook may stop at an exercise. This is expected and must not be confused with a failing solution notebook. Never globally ignore exceptions to declare an execution successful.

## Solutions

Keep the same identifiers and order as in the lesson. Explain choices, provide verification results, discuss at least one plausible mistake, and distinguish multiple valid solutions. For a stochastic experiment, provide observed ranges or trends and the seeds, not an arbitrary value presented as universal. The solution must run sequentially from a fresh kernel without hidden state.

## Library reference

Every inventoried public symbol needs a contextualized explanation: purpose, version-specific signature, inputs/outputs, shapes and dtypes, mutation or allocation, a minimal example, pitfalls, and alternatives. Related variants may share a lesson, but each variant retains its own entry and specific behavior. Specialized subpackages remain in the curriculum even when they are not used in a GPT.

## Sources and limitations

Prefer official documentation, original papers, and authors' code. Place sources near the claims or equations they support; record URL, version/date, section, and access date. Distinguish demonstrated results, the authors' experimental results, and teaching interpretations. Do not copy documentation pages into notebooks.

For a proprietary method, document what has actually been published and what remains unknown. A teaching implementation must describe its deviations from the paper. Video prediction alone is not evidence of causal understanding; a generated reasoning trace is not a direct reading of internal computations.

## When is a lesson complete?

- Text, derivations, and sources reviewed; dimensions and conventions consistent.
- Objectives connected to identified exercises and solutions.
- Solution executed from a fresh kernel in the locked environment.
- Readable figures with axes, units, legends, and interpretation.
- Resource budget actually measured and hardware limitations stated.
- Review note, navigation, and coverage updated.
- `validated` status only with execution evidence: environment, command, date, and result.

A status describes content quality, not learner mastery. Personal self-assessments remain separate and are not published automatically.
