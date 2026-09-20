---
turn: 373
role: "AI-Designer"
source: chat_history.json
---

# Turn 373 — AI-Designer

used
Bash
100ms

Yes—at the framework-reference level, this task is complete.

The work now has separate generic artifacts for:

Pool Volume

16_generic_pool_volume_probability_matrices.md

Die Size / Die Step-Up / Die Step-Down

17_generic_die_size_probability_matrices.md

Difficulty Vectors

14_difficulty_vector_probability_matrices.md

Automatic Success reduction

20_automatic_success_probability_tables.md

Opposed contests

19_opposed_probability_tables.md

Level 1–20 provisional progression

18_full_level_1_20_probability_progression.md

Boons and Banes do not require their own separate probability systems because they modify the generic Dice Pool:

text
Boon:
  Add dice → use the larger pool matrix.

Bane:
  Remove dice → use the smaller pool matrix.

One-die Bane:
  Apply the special Die Step-Down → use the lower die-size matrix.

Die Step-Ups and Die Step-Downs likewise use the generic die-size matrices.

Tracking updated
Marked the consolidated probability-reference task complete in PHASE_1_CHECKLIST.md.
Added DEC-067.
Updated the Outstanding Definitions Index.

Still open:

Final probability targets.
Final equipment progression.
Content-specific Automatic Success sources and limits.
Full playtest calibration.
Any future adjustments revealed by combat, magic, or equipment testing.
