# Documentation Refactor Plan

**Purpose:** Track the staged consolidation, renaming, reordering, and consistency audit of canonical documentation.  
**Scope:** Documentation structure and canonical ownership only. This plan must not silently redesign game mechanics.

**Canonical rules remain in:**

- `03_core_baseline_system/`
- `04_simulationist_subsystems/`

**Status markers:**

- `[x]` Completed.
- `[~]` In progress or partially completed.
- `[ ]` Not started.
- `[!]` Blocked or requires an explicit design decision.

---

## Refactor Principles

- One topic has one canonical owner.
- Glossaries define terms; subsystem documents define procedures.
- Summaries link to rules rather than duplicate them.
- Research may explain rationale but does not override canon.
- Historical material is labeled or archived.
- File moves happen before content deletion.
- Every move is followed by link validation.
- No mechanical redesign is hidden inside an editorial refactor.
- Refactor tasks may relocate, consolidate, relabel, or cross-reference existing decisions, but may not create or resolve new rules definitions.
- Contradictions discovered during refactoring become explicit open issues unless already resolved by the User.
- Any topic that is still TBD must link to `06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md` rather than being decided during the refactor.

---

# Phase R0 — Refactor Inventory and Safety Baseline

- [x] R0.1 Record the current file tree.
- [x] R0.2 Identify every active canonical file.
- [x] R0.3 Identify duplicated mechanics and terminology.
- [x] R0.4 Identify deprecated terms and mechanics.
- [x] R0.5 Identify internal links and cross-references.
- [x] R0.6 Assign a provisional canonical owner to each topic.
- [x] R0.7 Record known contradictions without fixing them.
- [x] R0.8 Add the refactor plan to the project navigation.
- [x] R0.9 Confirm that no mechanical decision is being changed by the refactor.
- [x] R0.10 Perform a focused R0 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

**Deliverable:** Before-state inventory and topic-authority map.

# Phase R1 — Canonical Filename and Numbering Plan

- [x] R1.1 Decide whether Attributes and Derived Statistics share one file.
- [x] R1.2 Decide whether Character Schema remains separate.
- [x] R1.3 Decide whether Magic receives its own canonical file.
- [x] R1.4 Decide whether Skills, Domains, Activities, and Craft receive their own canonical file.
- [x] R1.5 Decide whether the comparative check-pool matrix moves out of the canonical directory.
- [x] R1.6 Decide whether the D&D advancement-track file is conversion reference or canonical framework.
- [x] R1.7 Obtain explicit approval for final filenames and numbering for the current core files, including `12_equipment_durability_and_economy.md`.
- [x] R1.8 Create the approved rename/move table.
- [x] R1.9 Perform a focused R1 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

**Deliverable:** Approved file-migration map.

# Phase R2 — Safe File Renames and Link Migration

- [x] R2.1 Rename files according to the approved migration map.
- [x] R2.2 Update all internal links.
- [x] R2.3 Update README navigation.
- [x] R2.4 Update `PROJECT_STATUS.md` navigation.
- [x] R2.5 Update `AGENTS.md` path references if needed.
- [x] R2.6 Update the Outstanding Definitions Index links.
- [x] R2.7 Update decision-log references.
- [x] R2.8 Search for references to old filenames.
- [x] R2.9 Confirm every moved file remains reachable.
- [x] R2.10 Do not delete content during this phase.
- [x] R2.11 Perform a focused R2 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

**Deliverable:** Same content in the approved structure with valid links.

# Phase R3 — Attributes and Derived Statistics Consolidation

**Proposed owner:** `03_core_baseline_system/02_attributes_and_derived_statistics.md`

- [x] R3.1 Consolidate Attribute definitions.
- [x] R3.2 Consolidate Attribute Die progression.
- [x] R3.3 Consolidate Primary and Secondary Attribute advancement.
- [x] R3.4 Consolidate Vitality, Stamina, Essence, and paired defenses.
- [x] R3.5 Remove duplicate Attribute definitions elsewhere.
- [x] R3.6 Normalize STR, DEX, CON, INT, WIS, CHA terminology.
- [x] R3.7 Normalize the d12 ceiling.
- [x] R3.8 Link Character Schema to this owner.
- [x] R3.9 Link Resolution Engine to this owner.
- [x] R3.10 Audit all derived-stat formulas for contradictions.
- [x] R3.11 Perform a focused R3 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

**Deliverable:** One authoritative Attribute and Derived Statistics file.

# Phase R4 — Universal Resolution Consolidation

**Owner:** `03_core_baseline_system/01_resolution_engine.md`

- [x] R4.1 Consolidate Natural Dice Pool and Enhanced Dice Pool procedures.
- [x] R4.2 Consolidate base `2dX keep highest` resolution.
- [x] R4.3 Consolidate Competency Rank and Floor effects.
- [x] R4.4 Consolidate typed Boons and same-source non-stacking.
- [x] R4.5 Consolidate one-for-one Boon/Bane cancellation.
- [x] R4.6 Replace the obsolete Bane table.
- [x] R4.7 Consolidate one-die Bane Die Step-Down and d4 automatic failure.
- [x] R4.8 Consolidate Floor interaction with Banes.
- [x] R4.9 Consolidate Die Step-Up and Die Step-Down ordering.
- [x] R4.10 Consolidate DC, Required Successes, and `DC X (Y)`.
- [x] R4.11 Consolidate opposed-roll tiebreaking and Defender Wins Ties.
- [x] R4.12 Consolidate Automatic Successes, Requirements, and Permissions.
- [x] R4.13 Remove `[SET]` procedures.
- [x] R4.14 Remove obsolete Focus, Soak, Hyper-Shift, and over-cap terminology.
- [x] R4.15 Link all other canonical files to this owner.
- [x] R4.16 Perform a focused R4 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

**Deliverable:** One authoritative universal resolution procedure.

# Phase R5 — Character Schema Consolidation

**Proposed owner:** `03_core_baseline_system/03_character_schema_and_actor_creation.md`

- [x] R5.1 Consolidate the Universal Actor Schema.
- [x] R5.2 Consolidate Race/Ancestry, Background/Origin, Classes, Prestige Classes, Skills, and Feats as actor blocks.
- [x] R5.3 Remove duplicate five-block definitions.
- [x] R5.4 Move or label historical alternative arrangements.
- [x] R5.5 Normalize Classes and Prestige Classes terminology.
- [x] R5.6 Link to Attributes, Resolution, Skills, Progression, Equipment, and Magic owners.
- [x] R5.7 Verify PC, NPC, monster, boss, and underling applicability.
- [x] R5.8 Perform a focused R5 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

# Phase R6 — Action, Movement, and Spatial Consolidation

**Proposed owners:**

- `03_core_baseline_system/04_action_economy_and_turn_structure.md`
- `03_core_baseline_system/05_spatial_and_distance_engine.md`

- [x] R6.1 Consolidate actions, reactions, and Free Guard.
- [x] R6.2 Consolidate multi-action and multiple-attack rules.
- [x] R6.3 Consolidate Close, Near, Medium, Far, and Distant.
- [x] R6.4 Consolidate Stride and movement-mode rules.
- [x] R6.5 Remove duplicate distance definitions.
- [x] R6.6 Normalize spatial terminology.
- [x] R6.7 Remove ambiguity between spatial shifts and Die Steps.
- [x] R6.8 Perform a focused R6 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

# Phase R7 — Progression and Advancement Consolidation

**Proposed owner:** `03_core_baseline_system/06_leveling_and_tier_progression.md`

- [x] R7.1 Consolidate Levels 1–20 and High Fantasy Tiers.
- [x] R7.2 Consolidate Background and Attribute advancement.
- [x] R7.3 Consolidate Class table standards.
- [x] R7.4 Consolidate Spell Slot Advancement and Spell Slot Progression Level.
- [x] R7.5 Consolidate Mythic placeholder scope.
- [x] R7.6 Remove old Path-based advancement from active rules.
- [x] R7.7 Normalize Base Class and Prestige Class terminology.
- [x] R7.8 Link conversion-track material rather than duplicating it.
- [x] R7.9 Perform a focused R7 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

# Phase R8 — Skills, Domains, Activities, and Craft Consolidation

**Proposed owner:** `03_core_baseline_system/09_domains_skills_activities_and_crafting.md`

- [x] R8.1 Consolidate the eight current Domains.
- [x] R8.2 Remove the old five-umbrella active presentation.
- [x] R8.3 Move or label historical 65-skill material.
- [x] R8.4 Consolidate Lore and Knowledge rules.
- [x] R8.5 Consolidate Craft specialties.
- [x] R8.6 Consolidate vehicle proficiencies.
- [x] R8.7 Consolidate Activities and Procedures.
- [x] R8.8 Consolidate tools, assistance, Requirements, and Permissions.
- [x] R8.9 Link to the Resolution Engine rather than duplicate check procedures.
- [x] R8.10 Perform a focused R8 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

# Phase R9 — Combat, Defense, Damage, and Wounds Consolidation

**Proposed owner:** `04_simulationist_subsystems/01_defenses_damage_and_wounds.md`

- [x] R9.1 Consolidate Reflexes, Parry, Fortitude, and Willpower references.
- [x] R9.2 Replace Soak with Damage Absorption.
- [x] R9.3 Consolidate Damage-versus-Damage Absorption.
- [x] R9.4 Consolidate Natural Criticals and Called Shots.
- [x] R9.5 Consolidate hit locations and wounds.
- [x] R9.6 Remove `[SET]` consequences.
- [x] R9.7 Consolidate Stamina defense expenditure.
- [x] R9.8 Consolidate conditions and recovery.
- [x] R9.9 Remove duplicate condition definitions.
- [x] R9.10 Perform a focused R9 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

# Phase R10 — Magic Framework Consolidation

**Proposed owner:** `03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md`

- [x] R10.1 Consolidate Schools, Traditions, and Traits.
- [x] R10.2 Consolidate Tradition Skills and access.
- [x] R10.3 Consolidate fixed Tradition spell lists.
- [x] R10.4 Consolidate universal preparation and spell acquisition.
- [x] R10.5 Consolidate Spell Slot Progression references.
- [x] R10.6 Consolidate Essence overview.
- [x] R10.7 Remove old Mantle and class-owned spell-list assumptions.
- [x] R10.8 Link to Resolution and Progression owners.
- [x] R10.9 Keep individual spell design out of this refactor.
- [x] R10.10 Keep Psychic/Psionic mechanics explicitly provisional.
- [x] R10.11 Perform a focused R10 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

# Phase R11 — Equipment and Economic Framework

**Proposed owner:** `03_core_baseline_system/12_equipment_durability_and_economy.md`

- [x] R11.1 Inventory existing equipment-progression references without resolving their open definitions.
- [x] R11.2 Consolidate existing references to weapons, Damage Dice, and Traits under the designated equipment owner.
- [x] R11.3 Consolidate existing references to armor, shields, and Damage Absorption under the designated equipment owner.
- [x] R11.4 Consolidate existing references to Durability Slots under the designated equipment owner.
- [x] R11.5 Mark unresolved masterwork, magical, and special-material scaling questions as TBD and link the Outstanding Definitions Index.
- [x] R11.6 Mark unresolved crafting, repair, and replacement questions as TBD and link the Outstanding Definitions Index.
- [x] R11.7 Mark unresolved wealth and expected equipment-band questions as TBD and link the Outstanding Definitions Index.
- [x] R11.8 Mark the unresolved wealth-by-level question as TBD and link the Outstanding Definitions Index.
- [x] R11.9 Avoid creating or finalizing equipment definitions or item content during this refactor.
- [x] R11.10 Perform a focused R11 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

# Phase R12 — Summary and Comparative Reclassification

- [x] R12.1 Reduce `10_master_top_to_bottom_system_summary.md` to a linked executive summary.
- [x] R12.2 Move the comparative check-pool matrix out of the canonical directory.
- [x] R12.3 Reclassify historical option documents.
- [x] R12.4 Mark comparative material as non-canonical.
- [x] R12.5 Remove duplicate canonical rules from research documents where necessary.
- [x] R12.6 Make README navigation-only.
- [x] R12.7 Update `AGENTS.md` if authority relationships change.
- [x] R12.8 Perform a focused R12 consistency audit and record it in `DOCUMENTATION_REFACTOR_AUDITS.md`.

# Phase R13 — Cross-Reference and Contradiction Audit

- [x] R13.1 Search for deprecated terminology.
- [x] R13.2 Search for `[SET]`.
- [x] R13.3 Search for Soak.
- [x] R13.4 Search for Focus where Essence is intended.
- [x] R13.5 Search for obsolete Attribute names.
- [x] R13.6 Search for over-cap die language.
- [x] R13.7 Search for old Path architecture.
- [x] R13.8 Search for duplicate DC, Floor, Boon, Bane, and Spell Slot definitions.
- [x] R13.9 Validate every internal link.
- [x] R13.10 Confirm every canonical topic has one owner.
- [x] R13.11 Update the Outstanding Definitions Index.
- [x] R13.12 Record refactor completion in the decision log.

---

## Refactor Completion Criteria

The documentation refactor is complete when:

- Every canonical topic has one authoritative owner.
- Canonical files no longer contain contradictory active procedures.
- Historical and comparative material is clearly labeled or archived.
- All internal links work.
- The README is navigation-focused.
- `AGENTS.md`, `PROJECT_STATUS.md`, the checklist, decision log, and Outstanding Definitions Index agree.
- No mechanical redesign was silently introduced during the refactor.
