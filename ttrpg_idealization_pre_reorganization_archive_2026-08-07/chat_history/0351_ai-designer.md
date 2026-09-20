---
turn: 351
role: "AI-Designer"
source: chat_history.json
---

# Turn 351 — AI-Designer

They should remain research artifacts, not rules sources.

The canonical rules should state the procedures and relationships, while the matrices show the probability consequences of those procedures.

Recommended relationship
Canonical rules

These define the mechanics:

text
03_core_baseline_system/01_resolution_engine.md
03_core_baseline_system/07_check_pool_generation_and_class_differentiation.md
03_core_baseline_system/08_statistical_framework_and_check_modes.md

They should not reproduce the probability matrices.

Research artifacts

These remain under:

text
02_comparative_system_analysis/

Including:

text
09_at_least_probability_matrices.md
13_probability_band_calibration.md
14_difficulty_vector_probability_matrices.md
16_generic_pool_volume_probability_matrices.md

They provide:

Exact probability evidence.
Calibration comparisons.
Alternative progression analysis.
Support for future decisions.
Playtest and balance references.
Appropriate cross-reference

The only canonical file that should link to them directly is:

text
03_core_baseline_system/08_statistical_framework_and_check_modes.md

It could include a short research-reference section:

Markdown
## Probability Research

The statistical consequences of the framework are analyzed in:

- `02_comparative_system_analysis/09_at_least_probability_matrices.md`
- `02_comparative_system_analysis/14_difficulty_vector_probability_matrices.md`
- `02_comparative_system_analysis/16_generic_pool_volume_probability_matrices.md`
- `02_comparative_system_analysis/13_probability_band_calibration.md`

These documents are research artifacts and do not define canonical rules.

The Phase 1 Checklist should also point to them under the probability-calibration tasks.

What should not happen

The canonical rules should not say:

text
At Level 5, the probability target is 84.74%.

That belongs in research.

Instead, canonical rules should say:

text
The final Dice Pool is resolved against a Difficulty Vector.

The research artifact then explains what probability that procedure produces.

So the recommended status is:

text
Canonical rules:
  Define the engine.

Research matrices:
  Measure the engine.

Decision log:
  Records decisions made after reviewing the measurements.

Outstanding Definitions Index:
  Tracks what remains unresolved.
