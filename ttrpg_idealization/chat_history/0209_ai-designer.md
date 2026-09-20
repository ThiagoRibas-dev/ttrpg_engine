---
turn: 209
role: "AI-Designer"
source: chat_history.json
---

# Turn 209 — AI-Designer

I agree. A large canonical rewrite would be risky because many files currently contain overlapping material and historical remnants. We should treat this as a documentation refactor, not a rules redesign.

The safest approach is a sequence of small, auditable phases where each phase leaves the repository in a coherent state.

Proposed Documentation Refactor Structure
Principles
No mechanical redesign during the refactor.
One topic receives one canonical owner.
Rename and move files before deleting duplicated content.
Update links immediately after every move.
Keep historical material in the archive or clearly labeled appendices.
Run a contradiction search after every phase.
Use sequential task IDs and checkboxes.
Do not combine structural refactoring with balance decisions.
Phase R0 — Refactor Inventory and Safety Baseline

Purpose: establish what exists before moving anything.

Tasks
 R0.1 Record the current file tree.
 R0.2 Identify every active canonical file.
 R0.3 Identify every document containing duplicated mechanics.
 R0.4 Identify every file containing deprecated terms.
 R0.5 Identify every internal link and cross-reference.
 R0.6 Assign a provisional canonical owner to each topic.
 R0.7 Record known contradictions without fixing them.
 R0.8 Create a refactor tracking section in PHASE_1_CHECKLIST.md.
 R0.9 Confirm that no design decision is being changed by the refactor.
Deliverable

A documented before-state and authority map.

This phase should not modify rules.

Phase R1 — Canonical Filename and Numbering Plan

Purpose: decide the final file structure before moving anything.

Proposed Core Structure
text
03_core_baseline_system/
├── 00_baseline_framework_glossary.md
├── 01_resolution_engine.md
├── 02_attributes_and_derived_statistics.md
├── 03_character_schema_and_actor_creation.md
├── 04_action_economy_and_turn_structure.md
├── 05_spatial_and_distance_engine.md
├── 06_progression_and_tier_advancement.md
├── 07_skill_pool_generation_and_class_differentiation.md
├── 08_attacks_spells_and_skill_architecture.md
├── 09_domains_skills_activities_and_crafting.md
├── 10_magic_traditions_and_spellcasting_framework.md
├── 11_sources_of_progression_and_equipment_vectors.md
├── 12_master_system_summary.md
└── 13_conversion_mapping_reference.md

The exact names should be approved before implementation.

Tasks
 R1.1 Decide whether Attributes and Derived Statistics share one file.
 R1.2 Decide whether Character Schema remains separate.
 R1.3 Decide whether Magic receives its own canonical file.
 R1.4 Decide whether Skills/Domains/Crafting receive their own canonical file.
 R1.5 Decide whether the comparative check-pool matrix moves out of the canonical directory.
 R1.6 Decide whether the D&D advancement-track file is canonical conversion material or research material.
 R1.7 Approve final filenames and numbering.
 R1.8 Create a rename/move table before moving anything.
Deliverable

An approved file-migration map.

Phase R2 — Safe File Renames and Link Migration

Purpose: change structure without changing content.

Tasks
 R2.1 Rename files according to the approved migration map.
 R2.2 Update all internal links.
 R2.3 Update README navigation.
 R2.4 Update PROJECT_STATUS.md.
 R2.5 Update 
AGENTS.md
 where file paths are referenced.
 R2.6 Update the Outstanding Definitions Index.
 R2.7 Update the decision log links.
 R2.8 Search for references to old filenames.
 R2.9 Confirm every moved file is still reachable.
 R2.10 Do not delete any content yet.
Deliverable

The same content in the new structure, with working links.

Phase R3 — Attribute and Derived-Statistics Consolidation

This should be the first substantive content consolidation because Attributes are foundational and Derived Statistics directly depend on them.

Proposed canonical file
text
03_core_baseline_system/02_attributes_and_derived_statistics.md
It should own
STR, DEX, CON, INT, WIS, CHA.
Attribute Die ladder.
Attribute advancement.
Primary and Secondary Attribute rules.
Vitality.
Stamina.
Essence.
Fortitude.
Reflexes.
Willpower.
Speed.
Carrying capacity.
Other directly derived statistics.
Tasks
 R3.1 Move Attribute definitions from the old files into the new owner.
 R3.2 Move all derived-stat formulas into the same file.
 R3.3 Remove duplicate Attribute definitions elsewhere.
 R3.4 Remove stale Attribute names such as MIG, AGI, or WIL.
 R3.5 Normalize Essence terminology.
 R3.6 Normalize the d12 ceiling.
 R3.7 Add cross-references from the Character Schema file.
 R3.8 Add cross-references from the Resolution Engine.
 R3.9 Verify paired defenses against the canonical definitions.
 R3.10 Search for inconsistent Attribute derivations.
Deliverable

One authoritative Attribute and Derived Statistics file.

Phase R4 — Universal Resolution Consolidation
Canonical file
text
03_core_baseline_system/01_resolution_engine.md
It should own
Natural Dice Pools.
Enhanced Dice Pools.
Base 2dX keep highest.
Competency effects.
Floors.
Boons.
Banes.
Die Steps.
DCs.
Required Successes.
Opposed rolls.
Defender Wins Ties.
Automatic Successes.
Requirements.
Permissions.
Multi-success resolution.
Tasks
 R4.1 Replace the old Bane table.
 R4.2 Implement one-for-one Boon/Bane cancellation.
 R4.3 Implement typed Boons and same-source non-stacking.
 R4.4 Implement Bane dice removal.
 R4.5 Implement one-die Bane Die Step-Down.
 R4.6 Implement d4 automatic failure after Bane Step-Down.
 R4.7 Resolve the Floor/Bane procedure.
 R4.8 Remove [SET] mechanics.
 R4.9 Add opposed tie procedures.
 R4.10 Add DC X (Y) procedures.
 R4.11 Add Automatic Success procedures.
 R4.12 Remove old Focus-based universal rules.
 R4.13 Remove Soak terminology.
 R4.14 Remove remaining over-cap die language.
 R4.15 Link all other canonical files to this file.
Deliverable

One authoritative universal resolution procedure.

Phase R5 — Character Schema Consolidation
Proposed canonical file
text
03_core_baseline_system/03_character_schema_and_actor_creation.md
It should own
Universal Actor Schema.
Race/Ancestry.
Background/Origin.
Class and Prestige Classes.
Skills.
Feats.
Actor record structure.
PC/NPC/monster construction relationships.

It should link to:

Attributes and Derived Statistics.
Resolution Engine.
Domains and Skills.
Progression.
Magic.
Tasks
 R5.1 Move the Universal Actor Schema into one location.
 R5.2 Remove duplicate five-block definitions.
 R5.3 Remove old Race + Class + Skills alternatives from active text.
 R5.4 Mark historical arrangements as historical or move them to the archive.
 R5.5 Clarify that Classes and Prestige Classes are current terminology.
 R5.6 Add links to canonical advancement and skill documents.
 R5.7 Verify monster and underling applicability.
Phase R6 — Action, Movement, and Spatial Consolidation
Proposed files
text
03_core_baseline_system/04_action_economy_and_turn_structure.md
03_core_baseline_system/05_spatial_and_distance_engine.md
Tasks
 R6.1 Consolidate action types and costs.
 R6.2 Consolidate reactions and Free Guard.
 R6.3 Consolidate multiple-attack rules.
 R6.4 Move all distance definitions to the Spatial file.
 R6.5 Remove duplicate Stride definitions.
 R6.6 Normalize Close/Near/Medium/Far/Distant terminology.
 R6.7 Move movement modes into the Spatial file.
 R6.8 Link action examples to the Spatial file.
 R6.9 Remove old “Tier Shift” ambiguity where it conflicts with Die Step language.
Phase R7 — Progression and Advancement Consolidation
Proposed file
text
03_core_baseline_system/06_progression_and_tier_advancement.md
It should own
Levels 1–20.
High Fantasy Tiers.
Background advancement.
Attribute advancement schedule.
Competency advancement cadence.
Class table structure.
Spell Slot Advancement.
Spell Slot Progression Level.
Mythic placeholder scope.
Tasks
 R7.1 Move Level and Tier tables into one owner.
 R7.2 Remove duplicate tier tables.
 R7.3 Consolidate Spell Slot Progression references.
 R7.4 Remove old class/path advancement language.
 R7.5 Normalize Base Class and Prestige Class terminology.
 R7.6 Remove obsolete over-cap advancement.
 R7.7 Clarify Mythic as intentionally deferred.
 R7.8 Link class conversion material rather than duplicating it.
Phase R8 — Skills, Domains, Activities, and Craft Consolidation
Proposed file
text
03_core_baseline_system/07_domains_skills_activities_and_crafting.md
It should own
Domains.
Skills.
Lore.
Knowledge.
Craft.
Activities.
Procedures.
Tools.
Vehicle proficiencies.
Skill-based Requirements and Permissions.
Tasks
 R8.1 Consolidate the eight current Domains.
 R8.2 Remove the old five-umbrella active presentation.
 R8.3 Move historical 65-skill material to archive or historical appendix.
 R8.4 Consolidate Craft specialties.
 R8.5 Consolidate Lore rules.
 R8.6 Consolidate Knowledge rules.
 R8.7 Consolidate activity procedures.
 R8.8 Remove duplicate skill procedures from simulationist files.
 R8.9 Link the Resolution Engine for check mechanics.
 R8.10 Link the Activity file from class and feat design documents.
Phase R9 — Combat, Defense, Damage, and Wounds Consolidation
Proposed files
text
04_simulationist_subsystems/01_defenses_damage_and_wounds.md
04_simulationist_subsystems/02_conditions_resources_and_recovery.md

Potentially merge the current three subsystem files into two clearer owners.

Tasks
 R9.1 Consolidate Reflexes, Parry, Fortitude, and Willpower references.
 R9.2 Replace Soak with Damage Absorption.
 R9.3 Consolidate Damage-versus-Absorption.
 R9.4 Consolidate Natural Criticals.
 R9.5 Consolidate Called Shots.
 R9.6 Consolidate anatomical wound conditions.
 R9.7 Remove [SET] consequences.
 R9.8 Consolidate Stamina defense expenditure.
 R9.9 Consolidate recovery rules.
 R9.10 Normalize Essence and Stamina terminology.
 R9.11 Remove duplicated condition definitions.
Phase R10 — Magic Framework Consolidation
Proposed file
text
03_core_baseline_system/08_magic_schools_traditions_and_spellcasting.md
It should own
Schools.
Traditions.
Traits.
Tradition Skills.
Tradition access.
Fixed Tradition spell lists.
Universal preparation.
Spell acquisition.
Spell Slot Progression references.
Essence overview.
Psychic/Psionic status.
Mythic/Epic magic placeholder.
Tasks
 R10.1 Move all canonical Magic Mastery rules into one owner.
 R10.2 Remove magic definitions from general character files.
 R10.3 Remove old Mantle references.
 R10.4 Remove old Arcane/Divine class-owned spell-list assumptions.
 R10.5 Consolidate Essence terminology.
 R10.6 Consolidate Spell Slot terminology.
 R10.7 Link the Resolution Engine for casting checks.
 R10.8 Link the Progression file for slot tables.
 R10.9 Keep individual spell design out of scope.
 R10.10 Keep Psychic/Psionic mechanics explicitly provisional.
Phase R11 — Equipment and Economic Framework
Proposed file
text
03_core_baseline_system/09_equipment_durability_and_economy.md
It should own
Equipment vectors.
Weapons.
Armor.
Shields.
Damage Dice.
Damage Absorption.
Durability Slots.
Special materials.
Magical equipment.
Equipment Traits.
Wealth and expected equipment bands.
Tasks
 R11.1 Move equipment principles out of comparison files.
 R11.2 Define equipment’s mathematical vectors.
 R11.3 Define masterwork and magical progression.
 R11.4 Define durability and repair.
 R11.5 Define campaign-economic assumptions.
 R11.6 Define wealth-by-level guidance or its replacement.
 R11.7 Link equipment to Combat, Craft, and Progression files.
 R11.8 Avoid final item catalogues during this phase.
Phase R12 — Summary and Comparative-File Reclassification
Tasks
 R12.1 Reduce 10_master_top_to_bottom_system_summary.md to a linked executive summary.
 R12.2 Move 11_check_pool_architecture_comparative_matrix.md into 02_comparative_system_analysis/.
 R12.3 Reclassify historical option documents.
 R12.4 Mark all comparative material clearly as non-canonical.
 R12.5 Remove duplicate canonical rules from research documents where they imply current authority.
 R12.6 Update README.md to point to owners rather than summarize mechanics.
 R12.7 Update 
AGENTS.md
 if file authority changes.
Phase R13 — Cross-Reference and Contradiction Audit
Tasks
 R13.1 Search for deprecated terminology.
 R13.2 Search for [SET].
 R13.3 Search for Soak.
 R13.4 Search for Focus where Essence is intended.
 R13.5 Search for old Attribute names.
 R13.6 Search for d12+ and over-cap language.
 R13.7 Search for old Path architecture.
 R13.8 Search for duplicate definitions of DCs, Floors, Boons, Banes, and Spell Slots.
 R13.9 Validate every internal link.
 R13.10 Confirm every canonical topic has one owner.
 R13.11 Update the Outstanding Definitions Index.
 R13.12 Record the refactor completion in the decision log.
Recommended Immediate Next Step

I recommend starting with Phase R0, then obtaining approval for the exact file migration map in Phase R1.

The first low-impact substantive consolidation should be:

text
Attributes + Derived Statistics

because it is conceptually self-contained and provides a clean dependency base for:

Resolution.
Defenses.
Resources.
Skills.
Progression.
Equipment.
Magic.

No rule should be rebalanced during this refactor. Any discovered mechanical contradiction should be logged as an open issue unless its resolution has already been explicitly approved.
