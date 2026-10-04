# Exhaustive, measurable, versioned coverage

## Initial status

[DOMAINS.md](DOMAINS.md) and [domains.json](domains.json) define a **domain-level planning and progress matrix**. NP-01 has a [curated chapter ledger](numpy/2.3.5-NP-01.json) linked to executed checks; it is not the full versioned NumPy inventory. They are not yet an exhaustive inventory of functions, classes, attributes, and methods. No symbol coverage percentage is reported until the denominator has been established. A `planned` entry does not mean that a topic has been explained.

## Scope

Goal: review the entire documented public Python API of NumPy, pandas, Matplotlib, PyTorch, and JAX for the selected versions, including class methods and specialized subpackages. Documented properties and constants belong in the reference. Experimental and deprecated APIs have separate categories. Aliases are inventoried with a canonical target, not removed.

C/C++ interfaces, extensions, backends, and internal mechanisms have dedicated chapters. Any symbol-by-symbol inventory of these interfaces is a separate scope from the Python API. Undocumented private elements are not a stable API to memorize. Every exclusion must be visible and justified; it must not be counted as a completed lesson.

## Building the inventory

1. Install and test a coherent set of versions; lock dependencies and record Python, OS, architecture, and accelerator.
2. Use that version's documentation indexes and, where available, its Sphinx `objects.inv` inventory. Record the URL, access date, and checksum of the source inventory file.
3. Filter documentation objects: a Sphinx inventory also contains headings and labels. Retrieve documented class members and check for missing sections. Introspection alone misses dynamic APIs and exposes private details; use it as a supplement.
4. Reconcile symbols, aliases, inherited methods, overloaded signatures, and subpackages; check additions and removals against the previous version.
5. Assign each symbol to a lesson and reference note; keep unassigned entries in an explicit backlog.
6. Verify links and evidence before calculating coverage.

## Format of a future symbol entry

Required fields: `library`, `version`, `symbol`, `kind`, `canonical_symbol`, `public_status`, `source_url`, `source_section`, `retrieved_at`, `lesson_id`, `reference_path`, `exercise_ids`, `explanation_status`, `exercise_status`, `solution_status`, `validation_evidence`, `exclusion_reason`.

An unknown field is `null`, never an invented value. Inventories for a published version are not overwritten when `stable` or `latest` changes.

## Statuses and metrics

- `planned`: content identified, not written.
- `draft`: content in progress, not validated.
- `reviewed`: content reviewed, execution not yet certified.
- `validated`: content reviewed and validation evidence available.
- `deprecated` / `experimental`: API properties, independent of content maturity.

Report separately: inventoried symbols, explained symbols, symbols practiced in exercises, validated solutions, and exclusions. The coverage denominator remains the set of documented public symbols in the relevant category. Display experimental, deprecated, and specialized APIs separately. Never turn “100% of rows filled in” into “100% of functions mastered.”
