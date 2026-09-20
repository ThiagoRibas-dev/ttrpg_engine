---
turn: 207
role: "AI-Designer"
source: chat_history.json
---

# Turn 207 — AI-Designer

Canonical Consolidation Plan

The goal should be to create a clear one-authority-per-topic structure rather than merely replacing old words inside every file.

The cleanup should therefore do three things simultaneously:

Correct obsolete terminology and mechanics.
Move each rule to one canonical owner.
Convert other canonical files into short summaries and links rather than duplicate rule chapters.

No changes should be applied until this plan is approved.

1. Establish the Canonical Ownership Map

Before editing, assign one authoritative file to each topic.

Topic	Canonical Owner
Shared framework vocabulary	00_baseline_framework_glossary.md
Core resolution procedure	01_resolution_engine.md
Attributes, derived statistics, resources	02_character_schema_and_stats.md
Actions, reactions, turns	03_action_economy_and_turn_structure.md
Distance and movement tiers	04_spatial_and_distance_engine.md
Level and Tier progression	05_leveling_and_tier_progression.md
Pool generation and class differentiation	06_check_pool_generation_and_class_differentiation.md
Attribute-derived values	07_attributes_and_derived_statistics.md
Progression-vector theory	08_sources_of_progression_and_conceptual_mapping.md
Class-track conversion reference	09_dnd_3_5e_class_advancement_tracks_mapping.md
Executive summary/navigation	10_master_top_to_bottom_system_summary.md
Comparative architecture	Move to 02_comparative_system_analysis/ or archive as historical
Attack/spell architecture	12_attacks_and_spells_vs_skills_architecture.md
Domains, Skills, Activities, Magic, Craft	13_building_block_domains_and_master_skill_system.md
Defenses and Damage Absorption	04_simulationist_subsystems/01_defenses_and_damage_modeling.md
Skills and generic procedures	04_simulationist_subsystems/02_skills_and_generic_capabilities.md
Resources, conditions, wounds	04_simulationist_subsystems/03_resources_conditions_and_wounds.md

The most important consolidation principle is:

A summary may point to a rule, but it must not redefine the rule.

2. Consolidate the Resolution Engine
Canonical owner
text
03_core_baseline_system/01_resolution_engine.md

This file should contain the complete universal procedure for:

Natural Dice Pools.
Enhanced Dice Pools.
Attribute Die Size.
Competency Rank effects.
Competency Floors.
Boons.
Banes.
One-for-one cancellation.
Typed Boon stacking.
Same-source non-stacking.
Die Step-Up and Die Step-Down.
Bane removal limits.
d4 Step-Down automatic failure.
Floor interaction.
Fixed DCs.
Required Successes.
DC X (Y).
Opposed contests.
Secondary dice tiebreaking.
Defender Wins Ties.
Automatic Successes.
Requirements and Permissions.
Multi-success resolution.
Remove from this file
[SET] token mechanics.
Old Bane tables.
Old “keep lowest” Bane rules.
Focus-based universal Step-Up costs.
Soak terminology.
Over-cap d12 language.
Any unresolved alternative models presented as current rules.
Update related files

Other files should link to the Resolution Engine for these procedures instead of reproducing them.

3. Keep the Glossary Definition-Only
Canonical owner
text
03_core_baseline_system/00_baseline_framework_glossary.md

The glossary should define terms briefly.

It should not contain:

Full Bane procedures.
Complete opposed-roll procedures.
Full spellcasting rules.
Complete damage rules.
Full equipment rules.
Probability analyses.

For example, the glossary may define:

text
Bane:
  A final-pool effect that removes one die...

The full sequencing and edge cases belong in the Resolution Engine.

This prevents the glossary and rules chapter from becoming parallel rulebooks.

4. Consolidate Attributes and Resources

There is currently overlap among:

text
02_character_schema_and_stats.md
07_attributes_and_derived_statistics.md
03_resources_conditions_and_wounds.md
Recommended ownership
02_character_schema_and_stats.md

Own:

Universal actor statistics.
Attribute definitions.
Character data schema.
Derived-stat overview.
Resource overview.
How those statistics appear on an actor record.
07_attributes_and_derived_statistics.md

Either:

Move into an Attributes appendix under 02_character_schema_and_stats.md; or
Keep it as the detailed mathematical derivation file.

If retained, it should own:

Attribute-derived pools.
Vitality derivation.
Stamina derivation.
Essence derivation.
Paired defenses.
Speed and carrying capacity.

The character schema file should link to it rather than repeat formulas.

03_resources_conditions_and_wounds.md

Own:

Resource spending and recovery.
Stamina depletion.
Essence usage.
Conditions.
Wound consequences.
Recovery procedures.

It should not redefine how Stamina or Essence is derived from Attributes.

Required terminology cleanup
Replace Focus with Essence where referring to the canonical resource.
Replace Soak with Damage Absorption.
Replace obsolete MIG/AGI/WIL names with STR/DEX/WIS/etc.
Remove [SET] references.
5. Consolidate Action and Spatial Rules
03_action_economy_and_turn_structure.md

Own:

Three-action turn.
Reaction and Free Guard.
Action costs.
Multiple attacks.
Full Defense.
Interact and Use Item.
Action-based combat maneuvers.
Action fatigue.

Remove or link out:

Detailed distance-tier definitions.
Detailed Damage Absorption rules.
Complete condition definitions.
04_spatial_and_distance_engine.md

Own:

Close.
Near.
Medium.
Far.
Distant.
Stride.
Zone movement.
Movement modes.
Reach and spatial positioning.

The Action Economy file should say:

See the Spatial and Distance Engine for movement distances and Tier shifts.

This avoids repeating “one Stride equals one Tier shift” in multiple files.

6. Consolidate Advancement and Progression
05_leveling_and_tier_progression.md

Own:

Character Levels 1–20.
High Fantasy Tiers.
Level milestones.
Background Attribute progression.
Secondary Attribute Step Points.
General advancement cadence.
Mythic as a future extension.
Spell Slot Advancement overview.

The detailed Reference Good Slot Progression should either live here or in a dedicated canonical file.

Recommended location:

text
03_core_baseline_system/05_leveling_and_tier_progression.md

The CSV remains a research/reference artifact, not the primary rule source.

Class advancement file
text
09_dnd_3_5e_class_advancement_tracks_mapping.md

This should be reframed as a conversion/reference file. It should not define the current universal class progression rules.

It may explain how D&D tracks translate into:

Vitality.
Defense advancement.
Skill allocations.
Spell Slot Advancement.
Tradition advancement.
Remove or revise
“Good,” “Okay,” and “Bad” as if they were player-facing tracks.
Old path-based progression.
Over-cap attribute language.
[SET] progression.
Focus progression.
Old Soak references.
7. Consolidate Pool Generation
06_check_pool_generation_and_class_differentiation.md

This file should own the detailed relationship between:

text
Attribute → Die Size
Competency → Pool Volume and Floor
Class/Tactics → Additional pool or permissions

It should explain:

Natural Dice Pool.
Enhanced Dice Pool.
Competency Rank.
Attribute-based ceiling.
Pool-volume limits.
Class differentiation.

It should not redefine:

Boon/Bane procedures.
Fixed DCs.
Opposed-roll tiebreaks.
Multi-success rules.

Those belong in the Resolution Engine.

All examples must be revised to remove:

d12+.
Over-cap d12.
Hyper-Shift.
[SET].
Obsolete Attribute abbreviations.
8. Consolidate Domains, Skills, and Magic
13_building_block_domains_and_master_skill_system.md

This file should own:

Domain structure.
Canonical Skill list.
Lore.
Knowledge.
Craft specialties.
Activities and Procedures.
Magic Mastery Traditions.
Spell Schools, Traditions, and Traits.
Spell Slot Progression references.
Spell acquisition architecture.
Essence overview.

It should not duplicate:

Universal check procedures.
Full Attribute derivations.
Full action economy.
Complete resource recovery rules.
Complete spell preparation rules once those receive a dedicated magic file.
Historical material

The old five-umbrella matrix and old Path architecture should either:

Be moved to 07_archive/; or
Be placed under a clearly marked historical appendix.

Since the old 65-skill matrix is already archived, the remaining historical sections should be treated consistently.

9. Consolidate Combat, Defenses, and Damage
04_simulationist_subsystems/01_defenses_and_damage_modeling.md

Own:

Reflexes.
Parry.
Fortitude.
Willpower.
Damage Absorption.
Damage-versus-Absorption procedure.
Armor.
Shields.
Weapon Damage Dice.
Critical Threat Profiles.
Natural Criticals.
Called Shots.
Hit locations.
Wound severity.
01_resolution_engine.md

Should only explain the universal opposed-check and comparison procedures.

It should link to this file for:

Damage.
Wounds.
Damage Absorption.
Critical anatomy.
Required cleanup

Replace:

text
Soak
Soak Rank
Soak 0

with:

text
Damage Absorption
Damage Absorption Step
No Damage Absorption

Remove [SET] mechanics and replace them with:

Required Successes.
Maneuver permissions.
Class or feat permissions.
Automatic Successes where explicitly appropriate.
10. Reclassify the Comparative Matrix
03_core_baseline_system/11_check_pool_architecture_comparative_matrix.md

This file is fundamentally comparative rather than canonical.

Recommended action:

text
Move to:
02_comparative_system_analysis/

or archive it and create a cleaned comparative version there.

It should not sit among canonical core rules while presenting:

Model A/B/C as if still open.
Old [SET] mechanics.
Old over-cap dice.
Old attribute systems.
Old path architecture.

This is a major source of apparent contradiction.

11. Reclassify the Executive Summary
03_core_baseline_system/10_master_top_to_bottom_system_summary.md

This should remain a concise navigation and executive summary.

It should:

State the current architecture.
Link to the authoritative subsystem files.
Avoid duplicating full tables and procedures.
Avoid old examples that imply superseded mechanics.

Its role should be:

text
What are the major subsystems?
Where is each rule defined?

not:

text
A second complete copy of every rule.
12. Update the Checklist and Status Documents
PHASE_1_CHECKLIST.md

Add a canonical-consolidation task group:

 Assign one authoritative owner to every core rule topic.
 Remove duplicated procedures from non-owning canonical files.
 Move comparative files out of the canonical directory.
 Replace stale terminology.
 Remove [SET] procedures.
 Remove over-cap d12 concepts.
 Normalize Essence, Damage Absorption, and Attribute terminology.
 Complete canonical cross-reference audit.
PROJECT_STATUS.md

Add canonical consolidation to the current phase scope and exit criteria.

03_outstanding_definitions_index.md

Add a documentation-cleanup item for the canonical consolidation audit.

13. Recommended Execution Order

The edits should be applied in this order:

Finalize the authority map.
Clean 00_baseline_framework_glossary.md.
Rewrite 01_resolution_engine.md as the authoritative universal procedure.
Clean 02_character_schema_and_stats.md and 07_attributes_and_derived_statistics.md.
Clean 03_action_economy_and_turn_structure.md and 04_spatial_and_distance_engine.md.
Clean 05_leveling_and_tier_progression.md.
Clean 06_check_pool_generation_and_class_differentiation.md.
Clean 04_simulationist_subsystems/01_defenses_and_damage_modeling.md.
Clean 04_simulationist_subsystems/02_skills_and_generic_capabilities.md.
Clean 04_simulationist_subsystems/03_resources_conditions_and_wounds.md.
Consolidate 13_building_block_domains_and_master_skill_system.md.
Reclassify or archive 11_check_pool_architecture_comparative_matrix.md.
Reduce 10_master_top_to_bottom_system_summary.md to a linked executive summary.
Update the decision log, outstanding index, checklist, and project status.
Perform a final repository-wide terminology and contradiction search.
Final Result

The desired structure should be:

text
00:
  What terms mean.

01:
  How universal resolution works.

02/07:
  What actors and statistics are.

03/04:
  How actions and space work.

05/06:
  How progression and pools work.

04_simulationist_subsystems/:
  How combat, damage, skills, resources, and wounds work.

13:
  How Domains, Skills, Craft, Lore, and Magic are organized.

10:
  How to navigate the system.

02_comparative_system_analysis/:
  Why the system uses these structures and how it compares to references.

This will remove duplication while preserving research history and making the canonical rules much easier to maintain.
