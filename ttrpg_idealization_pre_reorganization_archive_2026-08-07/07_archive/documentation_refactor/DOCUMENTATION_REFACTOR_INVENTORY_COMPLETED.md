# Documentation Refactor Inventory

**Phase:** R0 — Refactor Inventory and Safety Baseline  
**Status:** Completed as an initial inventory; no rules were changed.

## Active Canonical Files

### Core Baseline

- `03_core_baseline_system/00_baseline_framework_glossary.md`
- `03_core_baseline_system/01_resolution_engine.md`
- `03_core_baseline_system/03_character_schema_and_actor_creation.md`
- `03_core_baseline_system/04_action_economy_and_turn_structure.md`
- `03_core_baseline_system/05_spatial_and_distance_engine.md`
- `03_core_baseline_system/06_leveling_and_tier_progression.md`
- `03_core_baseline_system/07_check_pool_generation_and_class_differentiation.md`
- `03_core_baseline_system/02_attributes_and_derived_statistics.md`
- `02_comparative_system_analysis/archived_core_reference/08_sources_of_progression_and_conceptual_mapping_REFERENCE.md`
- `02_comparative_system_analysis/archived_core_reference/09_dnd_3_5e_class_advancement_tracks_mapping_REFERENCE.md`
- `03_core_baseline_system/11_master_top_to_bottom_system_summary.md`
- `02_comparative_system_analysis/archived_core_reference/11_check_pool_architecture_comparative_matrix_REFERENCE.md`
- `02_comparative_system_analysis/archived_core_reference/12_attacks_and_spells_vs_skills_architecture_REFERENCE.md`
- `03_core_baseline_system/09_domains_skills_activities_and_crafting.md`

### Simulationist Subsystems

- `04_simulationist_subsystems/01_defenses_and_damage_modeling.md`
- `04_simulationist_subsystems/02_skills_and_generic_capabilities.md`
- `04_simulationist_subsystems/03_resources_conditions_and_wounds.md`

## Provisional Topic Ownership Before R1

This was the provisional inventory before the approved R1/R2 migration subset. The current file structure is tracked in the README and refactor plan.

| Topic | Current likely owner | Refactor note |
|---|---|---|
| Shared vocabulary | `03/.../00_baseline_framework_glossary.md` | Already established |
| Universal resolution | `03/.../01_resolution_engine.md` | Contains stale duplicated procedures requiring cleanup |
| Attributes and derived statistics | `03/.../02...` and `07...` | Candidate consolidation |
| Character schema | `03/.../02...` and `13...` | Candidate separation/consolidation |
| Action economy | `03/.../03...` | Duplicate references elsewhere |
| Spatial rules | `03/.../04...` | Duplicate references elsewhere |
| Level and Tier progression | `03/.../05...` | Candidate rename/consolidation |
| Pool generation | `03/.../06...` | Must link to Resolution Engine |
| Progression vectors | `03/.../08...` | Likely research/framework reference |
| D&D advancement conversion | `03/.../09...` | Classification requires R1 decision |
| Executive summary | `03/.../10...` | Should become navigation-focused |
| Comparative matrix | `03/.../11...` | Candidate move to comparative directory |
| Attack/spell architecture | `03/.../12...` | Candidate consolidation into combat/magic owners |
| Domains, skills, activities, magic | `03/.../13...` | Likely split into focused owners |
| Defense and damage | `04/.../01...` | Candidate rename/consolidation |
| Skills and generic capabilities | `04/.../02...` | Candidate merge into canonical skill owner |
| Resources, conditions, wounds | `04/.../03...` | Candidate split or merge after R1 |

## Known Refactor Findings

- `01_resolution_engine.md` still contains stale `[SET]`, old Bane table, Soak, Focus, and older procedure language alongside newer `DEC-055` additions.
- `02_character_schema_and_stats.md` and `07_attributes_and_derived_statistics.md` overlap substantially.
- `10_master_top_to_bottom_system_summary.md` duplicates many subsystem rules.
- `11_check_pool_architecture_comparative_matrix.md` is comparative material located in the canonical directory.
- `12_attacks_and_spells_vs_skills_architecture.md` contains architecture history and current cross-references together.
- `13_building_block_domains_and_master_skill_system.md` contains current architecture alongside historical option material.
- `04_simulationist_subsystems/01_defenses_and_damage_modeling.md` and `03_resources_conditions_and_wounds.md` overlap on wounds, conditions, and resources.
- Old terminology and historical mechanics remain in active files and require focused cleanup after ownership is approved.

## Post-R1/R2 Note

The approved R1/R2 work moved Attributes, Character Schema, Action, Spatial, Progression, and Pool files into their ordered positions; moved reference-only files into `02_comparative_system_analysis/archived_core_reference/`; created `08_statistical_framework_and_check_modes.md`; and split Domains/Skills/Crafting from Magic.

## Scope Boundary

This inventory records documentation structure only. It does not resolve any mechanical questions, rename files, move files, or delete content.
