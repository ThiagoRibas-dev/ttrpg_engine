---
turn: 181
role: "AI-Designer"
source: chat_history.json
---

# Turn 181 — AI-Designer

Agreed. Here is the exact cleanup map for the legacy d12+ terminology, followed by the finalized Bane rules.

A. Legacy d12+ Audit Map
A1. Canonical documents — update

These should be changed because they are active rules or active framework summaries.

03_core_baseline_system/02_character_schema_and_stats.md

Current issue:

text
Attributes rated as Step Dice (d4 to d12+)

Action:

text
Replace with:
Attributes rated as Step Dice (d4 to d12)

Remove any implication that ordinary Attributes can exceed d12.

03_core_baseline_system/05_leveling_and_tier_progression.md

Current issues include:

text
Max Attribute: d12+
Max Attribute: d12+2 / d20
d12 → d12+1 → d12+2

Action:

Remove d12+ and d20 from the Attribute and Tier framework.
Cap ordinary Attributes at d12.
Replace references to over-cap Attribute advancement with discrete Tier or Mythic effects.
Remove or rewrite any claims that Legend or Mythic characters use larger ordinary dice.
Preserve Mythic advancement as exceptional permissions, effects, scope, and capabilities rather than larger check dice.
03_core_baseline_system/06_check_pool_generation_and_class_differentiation.md

Current issues include:

text
Die Size (d4 to d12+)
d12+1
d12+ over-cap pool

Action:

Replace the ordinary Die Size ladder with:
text
d4 → d6 → d8 → d10 → d12
Remove d12+1 as a die size.
Remove examples of 4d12+ or 5d12+.
Replace high-tier examples with bounded d12 pools plus:
Floors.
Additional dice up to the pool ceiling.
Boons.
Explicit special effects.
Action or resource permissions.
03_core_baseline_system/07_attributes_and_derived_statistics.md

Current issue:

text
Step Dice (d4 to d12+)

Action:

text
Replace with:
Step Dice (d4 to d12)

Any over-cap attribute references should be deleted rather than renamed.

03_core_baseline_system/08_sources_of_progression_and_conceptual_mapping.md

Current issues include:

text
d4 → d12+
d12 → d12+1
5d12+1 over-cap pool
4d12+1

Action:

Remove all over-cap die sizes.
Preserve the distinction between:
Attribute Die Size.
Competency Pool Volume.
Floors.
Stamina/Essence expenditure.
Rewrite examples using d12 as the highest ordinary die.
Replace “over-cap pool” examples with discrete effects where necessary.
03_core_baseline_system/09_dnd_3_5e_class_advancement_tracks_mapping.md

Current issues include:

text
Apex Legend Pool (5d12+2 over-cap)

Action:

Replace with a bounded 5d12 pool.
Represent the additional high-level power through:
Floor 9.
Additional multi-success permissions.
Special class features.
Critical or maneuver permissions.
Mythic access, where appropriate.
03_core_baseline_system/10_master_top_to_bottom_system_summary.md

Current issues include:

text
d4 to d12+
X+3
d12+1

Action:

Replace all general ladders with d4 to d12.
Remove over-cap examples.
Rewrite the summary so high-level power remains bounded by:
5d12.
Competency Floor 9.
Die Step-Up only until d12.
Discrete Tier abilities.
03_core_baseline_system/11_check_pool_architecture_comparative_matrix.md

Current issues include:

text
Die Size d4 to d12+
4d12+1 over-cap

Action:

Replace with ordinary d4 to d12.
Replace the Ogre example with a bounded d12 pool.
Preserve the comparative argument that the system is bounded and avoids D&D 3.5e-style modifier escalation.
03_core_baseline_system/13_building_block_domains_and_master_skill_system.md

Current issues include:

text
d8 → d12+1
d12+2
4d12+2
5d12+1 over-cap

Action:

Remove all over-cap Attribute and check-pool references.
Keep the Competency Rank benefits that do not require exceeding d12.
Rewrite examples so Legendary characters use 5d12, Floor 9, and special permissions.
04_simulationist_subsystems/02_skills_and_generic_capabilities.md

Current issue:

text
Legendary: 5dX + Free Hyper-Shift

After the terminology cleanup, this should become a bounded rule:

text
Legendary: 5dX, Floor 9, plus the specified Legendary permission.

Any “free Hyper-Shift” that would exceed d12 should instead become a discrete effect.

04_simulationist_subsystems/03_resources_conditions_and_wounds.md

There are no major d12+ references, but there are old Hyper-Shift references.

Action:

Replace those with the current Die Step-Up terminology.
Ensure a Die Step-Up at d12 does not create a larger die.
Define the relevant content-specific consequence separately.
A2. Comparative and research documents — label or update selectively

These documents are not canonical, so they may preserve historical language where it explains earlier design thinking. However, current comparisons should not present d12+ as active rules.

02_comparative_system_analysis/04_mathematical_calibration_and_ttk_vectors.md

Current language:

text
d4 to d12+

Action:

Replace in current calibration claims with d4 to d12.
Add a note that earlier drafts considered over-cap dice but that this is no longer part of the ordinary framework.
02_comparative_system_analysis/06_level_by_level_progression_comparison_vs_sotdl.md

Current examples include:

text
d12 → d12+1

Action:

Replace with bounded d12 language.
Remove outdated Hyper-Shift terminology.
Recast higher-tier power as special abilities, Floors, pool ceilings, and permissions.
02_comparative_system_analysis/07_dnd_3_5e_comparative_analysis_and_progression.md

Current examples include:

text
d12+1
d12+2
d12+1 over-cap damage

Action:

Update current-system comparison examples to stop using over-cap dice.
Preserve the document’s historical comparative purpose.
Explain that the bounded d12 ceiling is an intentional contrast with D&D 3.5e’s expanding modifiers.
02_comparative_system_analysis/01_architecture_matrix_v3_expanded.md

The d12+ references should be treated as stale current-system descriptions.

Action:

Update the current-system column to use d12.
Preserve unrelated historical examples from other systems.
02_comparative_system_analysis/02_mathless_resolution_case_studies.md

Action:

Replace d12+ wherever it describes the current system.
Keep any genuinely historical discussion labeled as an earlier rejected option.
A3. Decision log and status documents
06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md

Existing historical entries contain d12+ language.

Action:

Do not rewrite old decision history silently.
Add a new decision entry stating:
text
The ordinary die ceiling is d12.
The former d12+ / d12+1 / d12+2 notation is deprecated.
High-tier and Mythic escalation must use bounded d12 resolution plus discrete effects.

This preserves the history while making the current decision explicit.

06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md

The d12+ question should be converted from open to resolved:

text
Resolved:
  Ordinary checks never use d12+ notation.
  The maximum ordinary die is d12.
  High-tier exceptional effects must use discrete permissions,
  resource effects, or other bounded mechanics.
B. Finalized Bane Procedure

The Bane rule is now:

Each Bane removes one die from the pool. If the pool contains only one die, the Bane instead applies one Die Step-Down to that die. A pool cannot be reduced below one die through Banes, and only one Die Step-Down can be applied through this rule.

Examples:

text
2d8 +1X → 1d8
3d8 +2X → 1d8
1d8 +1X → 1d6
1d4 +1X → automatic failure
Bane limits
Banes cannot reduce a pool below 1dX.
Multiple Banes do not cause multiple Die Step-Downs.
Once the pool reaches one die, further Banes do not worsen it beyond the one Die Step-Down.
A d4 stepped down by this rule produces automatic failure.
The Competency Floor remains active after Bane reduction.

The last point is important:

text
Expert 1d8, Floor 5
+1 Bane
→ 1d6, Floor 5

The character’s ceiling is clipped, but the Floor remains 5.

C. Opposed Rolls and Complex DCs

These are now resolved as follows.

Opposed ties

The defender wins ties.

This applies to all opposed checks unless a specific rule explicitly says otherwise.

Multi-success DC notation

Complex difficulties use:

text
DC 5 (2)

Meaning:

text
DC 5
Requires 2 successful faces

A rolled face counts as a success if it meets or exceeds the DC.

Example:

text
Roll: 3, 5, 7, 8
Difficulty: DC 5 (2)

The roll achieves three successes and clears the task.

D. Current Phase 1 Status

Resolved:

Ordinary ceiling is d12.
d12+ notation is deprecated.
Banes remove dice.
One-die pools receive one Die Step-Down from a Bane.
Further Banes do not worsen a one-die pool.
d4 stepped down by a Bane causes automatic failure.
Floors remain active after Bane reduction.
Defenders win opposed ties.
Complex difficulties use DC X (Y) notation.

Deferred:

Final probability targets.
Resource cost and limits for Die Step-Up/Die Step-Down.
Equipment interaction with bounded math.
Mythic exceptional effects.

The next cleanup should be the canonical-document audit, beginning with the files in 03_core_baseline_system/ and 04_simulationist_subsystems/, before touching historical research language.
