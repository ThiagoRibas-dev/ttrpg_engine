---
turn: 337
role: "AI-Designer"
source: chat_history.json
---

# Turn 337 — AI-Designer

Ran commands
3

Executed the approved transition from explicit Floors/Required Successes to difficulty vectors.

Canonical changes
Removed
Competency Floor as an active mechanic.
Floor lookup and Floor cap rules.
DC X (Y) notation.
Required Successes as a universal difficulty axis.
Floor references from Attribute, Skill, Magic, Progression, and Resolution documents.
Established
Competency Rank determines baseline Dice Pool Size.
Attribute determines Die Size.
Equipment, Boons, Banes, Feats, Spells, and other effects modify final Dice Pool Size.
Difficulty uses comma-separated vectors:
text
DC 5
DC 5,4
DC 6,5,3
Final dice and difficulty thresholds are sorted highest-to-lowest and compared positionally.
Extra dice beyond the vector length are ignored for that vector.
Larger pools continue adding dice.
No conversion of excess dice into Automatic Successes.
Automatic Successes remain a separate content-provided effect.
Updated canonical files
00_baseline_framework_glossary.md
01_resolution_engine.md
07_check_pool_generation_and_class_differentiation.md
08_statistical_framework_and_check_modes.md
02_attributes_and_derived_statistics.md
06_leveling_and_tier_progression.md
09_domains_skills_activities_and_crafting.md
10_magic_schools_traditions_and_spellcasting.md
04_simulationist_subsystems/02_skills_and_generic_capabilities.md
12_equipment_durability_and_economy.md
Research artifacts updated

The probability artifacts now describe final Dice Pools and Difficulty Vectors rather than Floors and Required Successes:

09_at_least_probability_matrices.md
11_floor_equipment_dc_target_calibration.md
12_multi_success_probability_matrices.md
13_probability_band_calibration.md
14_difficulty_vector_probability_matrices.md
Tracking updated
Added DEC-064.
Updated the Outstanding Definitions Index.
Updated PHASE_1_CHECKLIST.md.
Recorded that the explicit Floor framework has been superseded.
Updated the checklist’s probability task to focus on Dice Pools, Difficulty Vectors, Boons, Banes, and Die Steps.

The glossary now contains Difficulty Vector rather than Required Successes as the multi-threshold framework term.
