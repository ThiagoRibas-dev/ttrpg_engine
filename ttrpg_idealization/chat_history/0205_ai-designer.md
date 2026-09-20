---
turn: 205
role: "AI-Designer"
source: chat_history.json
---

# Turn 205 — AI-Designer

Ran commands
2
Canonical Glossary Consistency Report

Scope checked:

text
03_core_baseline_system/
04_simulationist_subsystems/

Changes made: None.

The canonical glossary is a useful authority, but several active canonical files still contain older rules, terminology, or procedures that conflict with it.

1. Critical Resolution Conflicts
03_core_baseline_system/01_resolution_engine.md

This file contains the most important inconsistencies.

Bane procedure conflict

The current Bane table still says:

text
-1 Bane → 1dX
-2 Banes → 2dX keep lowest
-3 Banes → 3dX keep lowest

This conflicts with the current rule:

text
Each Bane removes one die.

If only one die remains:
  One Bane causes one Die Step-Down.

Further Banes:
  No additional worsening.
Floor conflict

The new canonical decision states that Banes lower the effective Floor when they reduce the final pool state.

However, the appended Bane rule currently says:

“Competency Floors remain active after Bane reduction; Banes clip the pool ceiling but do not remove the Floor.”

That wording conflicts with the more recent decision that Banes can lower the Floor.

This needs clarification between:

A Floor remaining active as a concept.
A Floor being numerically reduced by a Bane.

The current intended interpretation appears to be:

text
A Floor remains part of the check,
but a Bane may lower the final Floor value.
[SET] references remain

The file still references:

text
Special Effect Tokens ([SET])

This conflicts with the removal of [SET] tokens and the replacement of those effects with Required Successes, maneuvers, and explicit class/feat permissions.

Examples occur in:

Complex task resolution.
Maneuver explanations.
Older Called Shot and combat entries.
Focus remains

The Die Step-Up section still refers to:

text
mental Focus

The current canonical term is:

text
Essence
Soak remains

The Bypass Absorption example includes:

text
Soak 0

The canonical term is:

text
Damage Absorption
2. Difficulty Class Inconsistencies
03_core_baseline_system/01_resolution_engine.md

The DC table uses labels such as:

text
DC 5 — Challenging
DC 7 — Formidable
DC 9 — Heroic / Severe
DC 11 — Legendary

The glossary’s working labels are:

text
DC 2 — Trivial
DC 3 — Routine
DC 5 — Challenging
DC 7 — Formidable
DC 9 — Heroic
DC 11 — Legendary
DC 12 — Extreme

Differences:

The resolution engine does not clearly include DC 2, DC 3, or DC 12 in the same table.
It uses “Heroic / Severe” where the glossary uses “Heroic.”
It describes required natural die sizes using forms such as d6+, which are not formally defined in the glossary.

The concepts are compatible, but the labels and coverage are not fully synchronized.

3. Complex Difficulty Inconsistencies

The glossary defines:

text
DC X (Y)

as:

text
Target Number X
Required Successes Y

The Resolution Engine does use Required Successes, but its procedure still says that extra successes beyond the requirement generate [SET] tokens.

That should eventually become an explicit rule for:

Extra Successes.
Superior results.
Overwhelming results.
Maneuver permissions.
Called Shots.
Complex-task progress.

At present, the framework has the correct DC X (Y) notation but still contains an obsolete consequence for exceeding Y.

4. Opposed-Roll Inconsistencies

The glossary now defines:

text
Defender Wins Ties

The Resolution Engine includes this in the appended terminology, but the earlier opposed-roll procedure does not yet fully specify:

Comparing secondary dice in order.
What happens when one pool has more dice.
What happens when both pools have identical results.
How a neutral tie, such as a race, differs from an attacker/defender contest.

The rule is recorded, but the main opposed-roll procedure still needs to be reconciled with it.

5. Automatic Success Is Defined but Not Integrated

The glossary defines Automatic Success, but the core rules do not yet provide a complete universal procedure for it.

Missing or unclear points include:

When Automatic Successes are added.
Whether they are added before or after dice are rolled.
Whether they count toward DC X (Y).
Whether they apply in opposed checks.
Whether they participate in tiebreakers.
Whether Banes can remove or suppress them.
Whether multiple Automatic Successes can stack.
How they are granted by Legendary, Mythic, class, feat, equipment, or spells.

The glossary definition is clear, but the mechanic remains under-integrated.

6. Legacy Attribute Terminology
03_core_baseline_system/02_character_schema_and_stats.md

The current Attribute model uses:

text
STR, DEX, CON, INT, WIS, CHA

But the file still contains older terminology such as:

text
MIG
AGI

These appear in example actors and should eventually be normalized.

The file also still uses:

text
Focus
Soak
[SET]

in active character-schema descriptions.

7. Legacy Resource Terminology

The current canonical resource is:

text
Essence

But older active files still refer to:

text
Focus
Focus Pool
Focus Step-Up
Focus actions

Examples occur in:

02_character_schema_and_stats.md
05_leveling_and_tier_progression.md
13_building_block_domains_and_master_skill_system.md
04_simulationist_subsystems/01_defenses_and_damage_modeling.md
04_simulationist_subsystems/03_resources_conditions_and_wounds.md

This is a direct glossary inconsistency.

8. Legacy Damage-Absorption Terminology

The canonical term is:

text
Damage Absorption

However, active canonical documents still use:

text
Soak
Soak Rank
Soak d4–d12
Soak 0

Examples occur in:

02_character_schema_and_stats.md
03_action_economy_and_turn_structure.md
05_leveling_and_tier_progression.md
11_check_pool_architecture_comparative_matrix.md
12_attacks_and_spells_vs_skills_architecture.md
04_simulationist_subsystems/01_defenses_and_damage_modeling.md

This is one of the largest terminology-cleanup areas.

9. Legacy [SET] Token References

[SET] was explicitly removed from the system, but it still appears in several active canonical files:

01_resolution_engine.md
02_character_schema_and_stats.md
05_leveling_and_tier_progression.md
08_sources_of_progression_and_conceptual_mapping.md
09_dnd_3_5e_class_advancement_tracks_mapping.md
10_master_top_to_bottom_system_summary.md
11_check_pool_architecture_comparative_matrix.md
12_attacks_and_spells_vs_skills_architecture.md
13_building_block_domains_and_master_skill_system.md

These references are not merely terminology remnants. Some still assign actual mechanical consequences to [SET].

They need to be classified as either:

Historical comparison material that should be labeled as superseded; or
Canonical rules that require conversion to Required Successes and explicit permissions.
10. Legacy Class/Path Terminology

The current project terminology uses:

text
Classes
Prestige Classes

However, 13_building_block_domains_and_master_skill_system.md still contains extensive historical language about:

text
Paths
Novice Paths
Expert Paths
Master Paths
Path #3
Prestige Paths

Some of this is clearly historical comparison material, but because the file is in the canonical directory, it can be mistaken for current architecture.

This needs either:

A clearly labeled historical section; or
Terminology conversion to Classes and Prestige Classes.
11. Over-Cap Language Without d12+

The literal d12+ notation has been removed, but some canonical documents still use phrases such as:

text
over-cap d12
Apex d12
double Step-Up beyond d12

These appear primarily in:

05_leveling_and_tier_progression.md
06_check_pool_generation_and_class_differentiation.md
08_sources_of_progression_and_conceptual_mapping.md
09_dnd_3_5e_class_advancement_tracks_mapping.md
10_master_top_to_bottom_system_summary.md
11_check_pool_architecture_comparative_matrix.md
13_building_block_domains_and_master_skill_system.md

The new Phase 1 decision is not simply “rename d12+.” It is:

Ordinary resolution does not exceed d12. Exceptional high-tier effects must be represented through bounded dice, additional dice, Automatic Successes, Requirements, Permissions, Traits, and special effects.

Therefore, “over-cap d12” is still conceptually stale even when the literal plus notation has disappeared.

12. Glossary Items Not Yet Fully Integrated

These terms are defined in the glossary but not consistently used in the canonical rules:

Natural Dice Pool.
Enhanced Dice Pool.
Automatic Success.
Requirement.
Permission.
Required Successes.
Defender Wins Ties.
Reference Good Slot Progression.

The glossary is currently ahead of the rules documents. That is acceptable temporarily, but the rules need to adopt the vocabulary consistently.

Summary by Severity
High-priority mechanical conflicts
Bane table contradicts the current Bane procedure.
Floor behavior after Banes is inconsistent.
[SET] still has active mechanical consequences.
Automatic Success is defined but not procedurally integrated.
Opposed-roll tiebreaking is not fully integrated.
Some rules still use Focus instead of Essence.
Some rules still use Soak instead of Damage Absorption.
Medium-priority terminology conflicts
MIG/AGI/WIL versus STR/DEX/INT/WIS.
Paths versus Classes and Prestige Classes.
Over-cap d12 language.
Older DC labels and missing DC 2/DC 3/DC 12 entries.
Required Successes terminology not consistently replacing older [SET] language.
Lower-priority historical labeling issues
Old class/path architecture examples.
Older design comparisons embedded in canonical files.
Historical references to removed mechanics that are not being presented as current rules.
Overall Assessment

The glossary and recent decisions are coherent, but the canonical documents have not yet fully caught up with them.

The biggest issue is not the glossary itself. It is that several older canonical sections still contain active mechanical procedures from before:

[SET] was removed.
Focus became Essence.
Soak became Damage Absorption.
Banes were redefined.
Floors were clarified.
Automatic Successes were introduced.
d12+ was deprecated.
Paths were replaced by Classes and Prestige Classes.

The next logical cleanup should begin with:

text
03_core_baseline_system/01_resolution_engine.md
03_core_baseline_system/02_character_schema_and_stats.md
03_core_baseline_system/05_leveling_and_tier_progression.md
03_core_baseline_system/10_master_top_to_bottom_system_summary.md
03_core_baseline_system/12_attacks_and_spells_vs_skills_architecture.md
03_core_baseline_system/13_building_block_domains_and_master_skill_system.md

No changes have been made in response to this report.
