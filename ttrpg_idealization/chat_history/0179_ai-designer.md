---
turn: 179
role: "AI-Designer"
source: chat_history.json
---

# Turn 179 — AI-Designer

used
Bash
113ms

Understood. These corrections substantially narrow Phase 1.

Resolved Phase 1 Definitions
d12+ Notation

There is currently no approved general use for d12+, d12+1, or d12+2.

Those references are remnants of earlier design iterations. The current ordinary mathematical ceiling is:

text
Maximum die size: d12
Maximum ordinary DC: DC 12

The old notation still appears in several documents, including:

03_core_baseline_system/02_character_schema_and_stats.md
03_core_baseline_system/05_leveling_and_tier_progression.md
03_core_baseline_system/06_check_pool_generation_and_class_differentiation.md
03_core_baseline_system/07_attributes_and_derived_statistics.md
03_core_baseline_system/08_sources_of_progression_and_conceptual_mapping.md
03_core_baseline_system/09_dnd_3_5e_class_advancement_tracks_mapping.md
03_core_baseline_system/10_master_top_to_bottom_system_summary.md
03_core_baseline_system/11_check_pool_architecture_comparative_matrix.md
03_core_baseline_system/13_building_block_domains_and_master_skill_system.md
Several comparative documents and historical decision entries.

These should eventually be audited and replaced with bounded d12 terminology or discrete exceptional effects.

Banes

The current rule is:

Each Bane removes one die from the pool. If the pool contains only one die, the Bane instead applies a Die Step-Down to the remaining die.

Examples:

text
2d8 +1X → 1d8
3d8 +2X → 1d8
1d8 +1X → 1d6

The remaining edge cases are:

What happens when a d4 would be stepped down.
Whether multiple Banes can cause multiple Die Step-Downs after the pool reaches one die.
Whether a Floor remains active after a Bane reduces the pool.

Those are minor implementation details, not a need for a different Bane model.

Opposed Ties

The rule is:

The defender wins ties.

This applies to opposed:

Attacks.
Parry.
Reflexes.
Fortitude.
Willpower.
Social contests.
Other active opposed checks.

The defender’s win on ties makes offensive success require a clear superiority rather than merely matching the defense.

Multi-Success Difficulty

Complex difficulty is expressed as:

text
DC 5 (2)

Meaning:

text
Target Number: 5
Required Successes: 2

A face counts as a success if it meets or exceeds the DC.

Example:

text
Roll: 3, 5, 7, 8
Difficulty: DC 5 (2)

The result has three successful faces:

text
5, 7, 8

Therefore it achieves the required two successes.

This same structure applies to:

Complex tasks.
Combat maneuvers.
Called Shots.
Superior and Overwhelming Hits.
Multi-stage challenges.
Probability Targets

Status remains:

text
Open / Deferred

We will treat probability calibration as a dedicated future Phase 1 workstream rather than guessing at final target percentages now.

Resource-Driven Die Step-Ups

Status:

text
Deferred to the content or subsystem that uses them.

There is no universal cost or universal limit yet.

A particular subsystem may define:

Whether Stamina or Essence is spent.
The cost.
The maximum number of Step-Ups.
Whether the Step-Up applies to the entire pool, damage, defense, or another die.

The universal terminology remains:

text
Die Step-Up
Die Step-Down
Up-Shift: d8 → d10
Down-Shift: d10 → d8
Bounded Math

The intended mathematical principle is:

The system remains bounded because ordinary resolution never exceeds the d12 ceiling and fixed DC range.

This means:

Equipment should not create larger ordinary dice.
Feats should create discrete permissions rather than linear numerical escalation.
Spell effects should use bounded checks and explicit Traits.
Conditions should use Banes, Die Step-Downs, action restrictions, or defined state changes.
Higher-tier power should come from better pools, Floors, resources, actions, permissions, and effects—not endlessly increasing target numbers.

The remaining work is not to invent another mathematical layer, but to ensure that each future subsystem respects the existing ceiling.

Updated Phase 1 Priority

The fundamental math work now looks like this:

Remove or mark old d12+ terminology.
Formalize the Bane procedure and boundary cases.
Formalize opposed ties: defender wins.
Formalize required-success notation such as DC 5 (2).
Build the probability-calibration framework.
Define how future equipment, spells, feats, and conditions operate within the d12/DC 12 ceiling.

The key correction is that d12+ is not an active mathematical feature. It is legacy terminology that should be removed from current rules language.
