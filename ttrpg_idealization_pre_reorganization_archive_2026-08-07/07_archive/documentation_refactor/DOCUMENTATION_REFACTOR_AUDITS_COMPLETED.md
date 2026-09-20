# Documentation Refactor Audit Log

**Purpose:** Record the focused consistency audit performed at the end of each Documentation Refactor phase.

This log records documentation state and unresolved findings. It does not authorize mechanical changes. Any design decision discovered during an audit must follow the approval and decision-recording procedures in `AGENTS.md`.

## Audit Record Template

```text
Phase:
Date:
Auditor:
Scope checked:
Files checked:
Terminology checked:
Cross-references checked:
Contradictions found:
Changes made:
Items deferred:
Result:
```

## Phase Audit Records

### Phase R0 — Refactor Inventory and Safety Baseline

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** Active canonical files in `03_core_baseline_system/` and `04_simulationist_subsystems/`, plus current governance artifacts.

**Files checked:** See `DOCUMENTATION_REFACTOR_INVENTORY.md`.

**Terminology checked:** Deprecated `[SET]`, Soak, Focus, old Attribute labels, old Path language, old over-cap terminology, and legacy resolution procedures.

**Cross-references checked:** README, AGENTS, PROJECT_STATUS, PHASE_1_CHECKLIST, decision log, and Outstanding Definitions Index.

**Contradictions found:** Several canonical files contain duplicated or stale procedures, especially the Resolution Engine, Character Schema/Attributes, executive summary, comparative matrix, attack/spell architecture, Domains/Skills document, and simulationist subsystems.

**Changes made:** Created the inventory and marked R0 tasks complete. No game mechanics were changed and no files were moved.

**Items deferred:** Final file names, ownership, moves, merges, and content cleanup require R1 decision and approval.

**Result:** R0 complete; R1 is ready for review.

### Phase R1 — Canonical Filename and Numbering Plan

**Status:** Completed for the approved ownership decisions; final equipment definitions remain deferred; the approved canonical owner is now `12_equipment_durability_and_economy.md`.

**Date:** 2026-07-24

**Scope checked:** Renamed and reordered the approved Attribute/Derived Statistics and Character Schema files, with dependent files shifted to preserve numeric order.

**Files checked:** The affected `03_core_baseline_system/` files and all repository Markdown cross-references.

**Changes made:** `02_attributes_and_derived_statistics.md` is now the Attribute owner; `03_character_schema_and_actor_creation.md` is now the Character Schema owner; Action, Spatial, Progression, and Pool files moved to 04–07 respectively.

**Items deferred:** Final equipment filename/owner and any further numbering refinements remain subject to explicit review. R1.7 is therefore partial, not complete. No mechanics were changed.

**Result:** Approved R1 subset and R2 migration complete.

### Phase R2 — Safe File Renames and Link Migration

**Status:** Completed for the approved R1 decisions and statistical-framework split.

**Date:** 2026-07-24

**Scope checked:** Internal Markdown references, README navigation, Project Status, and active canonical paths affected by the approved moves.

**Changes made:** Updated dependent paths and preserved all file content. No files were deleted and no mechanics were changed.

**Items deferred:** Equipment owner move and any future content consolidation remain deferred.

**Result:** Approved subset migrated; remaining files await R1 decisions.

### Phase R3 — Attributes and Derived Statistics Consolidation

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** Attributes, derived statistics, paired defenses, actor schema, and direct cross-references.

**Changes made:** Consolidated Attribute and derived-stat ownership in `02_attributes_and_derived_statistics.md`; reduced `03_character_schema_and_actor_creation.md` to actor-building structure and links; preserved pre-consolidation files in `02_comparative_system_analysis/archived_core_reference/r3_pre_consolidation/`.

**Definitions changed:** None. Existing decisions were reorganized and stale duplicate procedures removed from the active owners.

**Items deferred:** Equipment definitions, detailed resource procedures, complete classes, feats, ancestries, and content catalogues remain deferred.

**Result:** R3 complete.

### Phase R4 — Universal Resolution Consolidation

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** Universal pool construction, Competency Floors, Boons, Banes, Die Steps, DCs, Required Successes, opposed checks, Automatic Successes, Requirements, and Permissions.

**Changes made:** Replaced the old Resolution Engine with a consolidated canonical procedure and reduced the pool-generation document to its statistical relationship role. Preserved the pre-consolidation Resolution Engine and pool-generation document under `02_comparative_system_analysis/archived_core_reference/r4_pre_consolidation/`.

**Definitions changed:** None. The procedure was reconciled to previously approved decisions, including Bane limits, Defender Wins Ties, `DC X (Y)`, and bounded d12 resolution.

**Items deferred:** Probability calibration, content-specific resource costs, high-tier Automatic Success progression, and detailed combat consequences remain deferred.

**Result:** R4 complete.

### Phase R5 — Character Schema Consolidation

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** Universal Actor Schema, Race/Ancestry, Background/Origin, Classes, Prestige Classes, Skills, Feats, and actor applicability.

**Changes made:** Confirmed `03_character_schema_and_actor_creation.md` as the actor-structure owner. It now links to Attributes, Resolution, Progression, Domains/Skills, Magic, Combat, and Resources rather than duplicating their procedures.

**Definitions changed:** None. No classes, feats, ancestries, monsters, or other content were designed or finalized.

**Items deferred:** Complete actor content and compendia remain outside the current framework scope.

**Result:** R5 complete.

### Phase R6 — Action, Movement, and Spatial Consolidation

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** Three-action turn, Actions, Reactions, Free Guard, movement, Distance Tiers, Reach, range, zones, and movement modes.

**Changes made:** Consolidated action ownership in `04_action_economy_and_turn_structure.md` and spatial ownership in `05_spatial_and_distance_engine.md`. Preserved pre-consolidation files under `02_comparative_system_analysis/archived_core_reference/r6_pre_consolidation/`.

**Definitions changed:** None. Existing action and spatial concepts were reorganized and stale duplicated procedures were removed from the active owners.

**Items deferred:** Detailed repeated-action fatigue, equipment movement effects, spell-specific Areas of Effect, and condition-specific action restrictions remain owned by their future/current subsystem documents.

**Result:** R6 complete.

### Phase R7 — Progression and Advancement Consolidation

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** High Fantasy Tiers, Levels 1–20, advancement ownership, Classes and Prestige Classes, Spell Slot Advancement, and Mythic scope boundaries.

**Changes made:** Consolidated the Level and Tier framework in `06_leveling_and_tier_progression.md`. Preserved the pre-consolidation file under `02_comparative_system_analysis/archived_core_reference/r7_pre_consolidation/`.

**Definitions changed:** None. The existing Level, Tier, Spell Slot Advancement, and Mythic-scope decisions were reorganized without creating individual class or Mythic content.

**Items deferred:** Specific Class tables, Prestige Class content, full Spell Slot calibration, equipment progression, and Mythic mechanics remain deferred.

**Result:** R7 complete.

### Phase R8 — Skills, Domains, Activities, and Craft Consolidation

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** Domains, Skills, Lore, Knowledge, Craft, Activities, Procedures, Tools, vehicle proficiencies, and Magic Domain cross-reference.

**Changes made:** Consolidated the active skill framework in `09_domains_skills_activities_and_crafting.md`, removing historical option analysis and duplicate architecture. Preserved the pre-consolidation file under `02_comparative_system_analysis/archived_core_reference/r8_pre_consolidation/`.

**Definitions changed:** None. The existing approved taxonomy was reorganized; unresolved Craft, Lore, vehicle, and activity details remain deferred.

**Items deferred:** Complete Skill, Craft, Lore, vehicle, Class, Feat, Ancestry, and content catalogues remain outside current scope.

**Result:** R8 complete.

### Phase R9 — Combat, Defense, Damage, and Wounds Consolidation

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** Defensive layers, Damage Absorption, Natural Criticals, Called Shots, anatomical Wounds, resources, Conditions, recovery, Rabble, and Underlings.

**Changes made:** Consolidated defense and injury ownership in `01_defenses_and_damage_modeling.md` and resource/condition ownership in `03_resources_conditions_and_wounds.md`. Preserved pre-consolidation files under `02_comparative_system_analysis/archived_core_reference/r9_pre_consolidation/`.

**Definitions changed:** None. The files were reorganized around existing approved concepts; unresolved damage calibration, equipment interaction, and recovery details remain deferred.

**Items deferred:** Detailed damage calibration, final armor/equipment procedures, exact Wound recovery timing, and content-specific resource costs.

**Result:** R9 complete.

### Phase R10 — Magic Framework Consolidation

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** Schools, Traditions, Traits, Tradition Skills, shared spell lists, universal preparation, acquisition, shared Spell Slots, Spell Slot Progression, Essence, and Psychic/Psionic scope.

**Changes made:** Consolidated the canonical magic framework in `10_magic_schools_traditions_and_spellcasting.md`. Removed duplicated general Skill and Domain material, leaving references to `09_domains_skills_activities_and_crafting.md`. Preserved the pre-consolidation file under `02_comparative_system_analysis/archived_core_reference/r10_pre_consolidation/`.

**Definitions changed:** None. Existing approved magic architecture was reorganized without creating individual spell, Class, or Tradition content.

**Items deferred:** Spell acquisition limits, preparation limits, detailed Essence procedures, Psychic/Psionic mechanics, individual spells, and Mythic magic remain deferred.

**Result:** R10 complete.

### Phase R11 — Equipment and Economic Framework

**Status:** Ownership scaffold completed; definitions remain deferred.

**Date:** 2026-07-24

**Scope checked:** Equipment references and the approved canonical owner location.

**Changes made:** Created `03_core_baseline_system/12_equipment_durability_and_economy.md` as the canonical ownership scaffold. It contains no new equipment rules or item content and links unresolved questions to the Outstanding Definitions Index.

**Items deferred:** All equipment, durability, crafting, magical-item, and wealth definitions remain TBD.

**Result:** R11 ownership task complete; equipment rules remain outside the current refactor scope.

### Phase R12 — Summary and Comparative Reclassification

**Status:** Completed.

**Date:** 2026-07-24

**Scope checked:** Executive summary, canonical navigation, comparative material, historical reference files, README pointers, and canonical authority relationships.

**Changes made:** Replaced `11_master_top_to_bottom_system_summary.md` with a navigation-focused summary. Confirmed former core comparison and conversion-reference files are retained under `02_comparative_system_analysis/archived_core_reference/` rather than presented as canonical rules. Preserved the pre-consolidation summary under `r12_pre_consolidation/`.

**Definitions changed:** None. The summary now points to canonical owners without duplicating their procedures.

**Items deferred:** Final R13 repository-wide contradiction and link audit.

**Result:** R12 complete.

### Phase R13 — Final Cross-Reference and Contradiction Audit

**Status:** Completed after cleanup pass.

**Date:** 2026-07-24

**Report:** `DOCUMENTATION_REFACTOR_R13_REPORT.md`

**Checks completed:** Deprecated-term scan, stale-mechanics scan, canonical ownership scan, status-language scan, and active Markdown link validation.

**Result:** Zero missing active Markdown links. The main remaining finding is stale Attribute terminology and duplicated Activity/maneuver procedures in `04_simulationist_subsystems/02_skills_and_generic_capabilities.md`. No canonical mechanics were changed during the audit.

**Remaining:** R13.11 and R13.12 await the cleanup pass and final synchronization after findings are reviewed.
