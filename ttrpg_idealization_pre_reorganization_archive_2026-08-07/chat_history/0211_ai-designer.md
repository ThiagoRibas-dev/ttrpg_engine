---
turn: 211
role: "AI-Designer"
source: chat_history.json
---

# Turn 211 — AI-Designer

Edited files
5
PHASE_1_CHECKLIST.md
MD
AGENTS.md
MD
PROJECT_STATUS.md
MD
README.md
MD
Documentation Refactor Plan
MD
Documentation Refactor Plan

Purpose: Track the staged consolidation, renaming, reordering, and consistency audit of canonical documentation.
Scope: Documentation structure and canonical ownership only. This plan must not silently redesign game mechanics.

Canonical rules remain in:

03_core_baseline_system/
04_simulationist_subsystems/

Status markers:

[x] Completed.
[~] In progress or partially completed.
[ ] Not started.
[!] Blocked or requires an explicit design decision.
Refactor Principles
One topic has one canonical owner.
Glossaries define terms; subsystem documents define procedures.
Summaries link to rules rather than duplicate them.
Research may explain rationale but does not override canon.
Historical material is labeled or archived.
File moves happen before content deletion.
Every move is followed by link validation.
No mechanical redesign is hidden inside an editorial refactor.
Contradictions discovered during refactoring become explicit open issues unless already resolved by the User.
Phase R0 — Refactor Inventory and Safety Baseline
 R0.1 Record the current file tree.
 R0.2 Identify every active canonical file.
 R0.3 Identify duplicated mechanics and terminology.
 R0.4 Identify deprecated terms and mechanics.
 R0.5 Identify internal links and cross-references.
 R0.6 Assign a provisional canonical owner to each topic.
 R0.7 Record known contradictions without fixing them.
 R0.8 Add the refactor plan to the project navigation.
 R0.9 Confirm that no mechanical decision is being changed by the refactor.

Deliverable: Before-state inventory and topic-authority map.

Phase R1 — Canonical Filename and Numbering Plan
 R1.1 Decide whether Attributes and Derived Statistics share one file.
 R1.2 Decide whether Character Schema remains separate.
 R1.3 Decide whether Magic receives its own canonical file.
 R1.4 Decide whether Skills, Domains, Activities, and Craft receive their own canonical file.
 R1.5 Decide whether the comparative check-pool matrix moves out of the canonical directory.
 R1.6 Decide whether the D&D advancement-track file is conversion reference or canonical framework.
 R1.7 Obtain explicit approval for final filenames and numbering.
 R1.8 Create the approved rename/move table.

Deliverable: Approved file-migration map.

Phase R2 — Safe File Renames and Link Migration
 R2.1 Rename files according to the approved migration map.
 R2.2 Update all internal links.
 R2.3 Update README navigation.
 R2.4 Update PROJECT_STATUS.md navigation.
 R2.5 Update AGENTS.md path references if needed.
 R2.6 Update the Outstanding Definitions Index links.
 R2.7 Update decision-log references.
 R2.8 Search for references to old filenames.
 R2.9 Confirm every moved file remains reachable.
 R2.10 Do not delete content during this phase.

Deliverable: Same content in the approved structure with valid links.

Phase R3 — Attributes and Derived Statistics Consolidation

Proposed owner: 03_core_baseline_system/02_attributes_and_derived_statistics.md

 R3.1 Consolidate Attribute definitions.
 R3.2 Consolidate Attribute Die progression.
 R3.3 Consolidate Primary and Secondary Attribute advancement.
 R3.4 Consolidate Vitality, Stamina, Essence, and paired defenses.
 R3.5 Remove duplicate Attribute definitions elsewhere.
 R3.6 Normalize STR, DEX, CON, INT, WIS, CHA terminology.
 R3.7 Normalize the d12 ceiling.
 R3.8 Link Character Schema to this owner.
 R3.9 Link Resolution Engine to this owner.
 R3.10 Audit all derived-stat formulas for contradictions.

Deliverable: One authoritative Attribute and Derived Statistics file.

Phase R4 — Universal Resolution Consolidation

Owner: 03_core_baseline_system/01_resolution_engine.md

 R4.1 Consolidate Natural Dice Pool and Enhanced Dice Pool procedures.
 R4.2 Consolidate base 2dX keep highest resolution.
 R4.3 Consolidate Competency Rank and Floor effects.
 R4.4 Consolidate typed Boons and same-source non-stacking.
 R4.5 Consolidate one-for-one Boon/Bane cancellation.
 R4.6 Replace the obsolete Bane table.
 R4.7 Consolidate one-die Bane Die Step-Down and d4 automatic failure.
 R4.8 Consolidate Floor interaction with Banes.
 R4.9 Consolidate Die Step-Up and Die Step-Down ordering.
 R4.10 Consolidate DC, Required Successes, and DC X (Y).
 R4.11 Consolidate opposed-roll tiebreaking and Defender Wins Ties.
 R4.12 Consolidate Automatic Successes, Requirements, and Permissions.
 R4.13 Remove [SET] procedures.
 R4.14 Remove obsolete Focus, Soak, Hyper-Shift, and over-cap terminology.
 R4.15 Link all other canonical files to this owner.

Deliverable: One authoritative universal resolution procedure.

Phase R5 — Character Schema Consolidation

Proposed owner: 03_core_baseline_system/03_character_schema_and_actor_creation.md

 R5.1 Consolidate the Universal Actor Schema.
 R5.2 Consolidate Race/Ancestry, Background/Origin, Classes, Prestige Classes, Skills, and Feats as actor blocks.
 R5.3 Remove duplicate five-block definitions.
 R5.4 Move or label historical alternative arrangements.
 R5.5 Normalize Classes and Prestige Classes terminology.
 R5.6 Link to Attributes, Resolution, Skills, Progression, Equipment, and Magic owners.
 R5.7 Verify PC, NPC, monster, boss, and underling applicability.
Phase R6 — Action, Movement, and Spatial Consolidation

Proposed owners:

03_core_baseline_system/04_action_economy_and_turn_structure.md

03_core_baseline_system/05_spatial_and_distance_engine.md

 R6.1 Consolidate actions, reactions, and Free Guard.

 R6.2 Consolidate multi-action and multiple-attack rules.

 R6.3 Consolidate Close, Near, Medium, Far, and Distant.

 R6.4 Consolidate Stride and movement-mode rules.

 R6.5 Remove duplicate distance definitions.

 R6.6 Normalize spatial terminology.

 R6.7 Remove ambiguity between spatial shifts and Die Steps.

Phase R7 — Progression and Advancement Consolidation

Proposed owner: 03_core_baseline_system/06_progression_and_tier_advancement.md

 R7.1 Consolidate Levels 1–20 and High Fantasy Tiers.
 R7.2 Consolidate Background and Attribute advancement.
 R7.3 Consolidate Class table standards.
 R7.4 Consolidate Spell Slot Advancement and Spell Slot Progression Level.
 R7.5 Consolidate Mythic placeholder scope.
 R7.6 Remove old Path-based advancement from active rules.
 R7.7 Normalize Base Class and Prestige Class terminology.
 R7.8 Link conversion-track material rather than duplicating it.
Phase R8 — Skills, Domains, Activities, and Craft Consolidation

Proposed owner: 03_core_baseline_system/07_domains_skills_activities_and_crafting.md

 R8.1 Consolidate the eight current Domains.
 R8.2 Remove the old five-umbrella active presentation.
 R8.3 Move or label historical 65-skill material.
 R8.4 Consolidate Lore and Knowledge rules.
 R8.5 Consolidate Craft specialties.
 R8.6 Consolidate vehicle proficiencies.
 R8.7 Consolidate Activities and Procedures.
 R8.8 Consolidate tools, assistance, Requirements, and Permissions.
 R8.9 Link to the Resolution Engine rather than duplicate check procedures.
Phase R9 — Combat, Defense, Damage, and Wounds Consolidation

Proposed owner: 04_simulationist_subsystems/01_defenses_damage_and_wounds.md

 R9.1 Consolidate Reflexes, Parry, Fortitude, and Willpower references.
 R9.2 Replace Soak with Damage Absorption.
 R9.3 Consolidate Damage-versus-Damage Absorption.
 R9.4 Consolidate Natural Criticals and Called Shots.
 R9.5 Consolidate hit locations and wounds.
 R9.6 Remove [SET] consequences.
 R9.7 Consolidate Stamina defense expenditure.
 R9.8 Consolidate conditions and recovery.
 R9.9 Remove duplicate condition definitions.
Phase R10 — Magic Framework Consolidation

Proposed owner: 03_core_baseline_system/08_magic_schools_traditions_and_spellcasting.md

 R10.1 Consolidate Schools, Traditions, and Traits.
 R10.2 Consolidate Tradition Skills and access.
 R10.3 Consolidate fixed Tradition spell lists.
 R10.4 Consolidate universal preparation and spell acquisition.
 R10.5 Consolidate Spell Slot Progression references.
 R10.6 Consolidate Essence overview.
 R10.7 Remove old Mantle and class-owned spell-list assumptions.
 R10.8 Link to Resolution and Progression owners.
 R10.9 Keep individual spell design out of this refactor.
 R10.10 Keep Psychic/Psionic mechanics explicitly provisional.
Phase R11 — Equipment and Economic Framework

Proposed owner: 03_core_baseline_system/09_equipment_durability_and_economy.md

 R11.1 Consolidate equipment progression vectors.
 R11.2 Define the relationship between weapons, Damage Dice, and Traits.
 R11.3 Define armor, shields, and Damage Absorption.
 R11.4 Define Durability Slots.
 R11.5 Define masterwork, magical, and special-material scaling.
 R11.6 Define crafting, repair, and replacement assumptions.
 R11.7 Define wealth and expected equipment bands.
 R11.8 Decide whether formal wealth-by-level guidance is required.
 R11.9 Avoid final item catalogues during this framework phase.
Phase R12 — Summary and Comparative Reclassification
 R12.1 Reduce 10_master_top_to_bottom_system_summary.md to a linked executive summary.
 R12.2 Move the comparative check-pool matrix out of the canonical directory.
 R12.3 Reclassify historical option documents.
 R12.4 Mark comparative material as non-canonical.
 R12.5 Remove duplicate canonical rules from research documents where necessary.
 R12.6 Make README navigation-only.
 R12.7 Update AGENTS.md if authority relationships change.
Phase R13 — Cross-Reference and Contradiction Audit
 R13.1 Search for deprecated terminology.
 R13.2 Search for [SET].
 R13.3 Search for Soak.
 R13.4 Search for Focus where Essence is intended.
 R13.5 Search for obsolete Attribute names.
 R13.6 Search for over-cap die language.
 R13.7 Search for old Path architecture.
 R13.8 Search for duplicate DC, Floor, Boon, Bane, and Spell Slot definitions.
 R13.9 Validate every internal link.
 R13.10 Confirm every canonical topic has one owner.
 R13.11 Update the Outstanding Definitions Index.
 R13.12 Record refactor completion in the decision log.
Refactor Completion Criteria

The documentation refactor is complete when:

Every canonical topic has one authoritative owner.
Canonical files no longer contain contradictory active procedures.
Historical and comparative material is clearly labeled or archived.
All internal links work.
The README is navigation-focused.
AGENTS.md, PROJECT_STATUS.md, the checklist, decision log, and Outstanding Definitions Index agree.
No mechanical redesign was silently introduced during the refactor.
Open

Recorded the full documentation-refactor plan in:

text
DOCUMENTATION_REFACTOR_PLAN.md

It now tracks sequential phases R0 through R13, including:

Inventory and safety baseline.
File naming and numbering.
Safe file moves and link migration.
Attribute and Derived Statistics consolidation.
Resolution Engine consolidation.
Character Schema consolidation.
Action and Spatial consolidation.
Progression consolidation.
Skills, Domains, Activities, and Craft consolidation.
Combat, Defense, Damage, and Wound consolidation.
Magic framework consolidation.
Equipment and economic framework.
Summary and comparative-file reclassification.
Final cross-reference and contradiction audit.

Each phase has sequential checkbox tasks and deliverables.

Updated references in:

README.md
PROJECT_STATUS.md
AGENTS.md
PHASE_1_CHECKLIST.md

The plan explicitly states that the refactor must not silently redesign mechanics and that contradictions discovered during the process become explicit issues rather than being resolved implicitly.
