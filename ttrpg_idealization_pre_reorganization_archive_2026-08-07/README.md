# Project Vault: Idealized Mathless Simulationist TTRPG System

This workspace develops a high-option-density, simulationist fantasy TTRPG.

The current development phase, scope boundaries, and phase exit criteria are maintained in [`PROJECT_STATUS.md`](PROJECT_STATUS.md). Read that document before interpreting examples of future content as active design work.

The project’s major references, inspirations, and compatibility targets are documented in [`01_design_philosophy_and_pillars/02_inspirations_and_anchors.md`](01_design_philosophy_and_pillars/02_inspirations_and_anchors.md).

---

## Canonical Documentation

The README is navigation-only. Canonical mechanics are maintained in:

- `03_core_baseline_system/`
- `04_simulationist_subsystems/`

The current project phase and scope boundaries are maintained in [`PROJECT_STATUS.md`](PROJECT_STATUS.md). The active Phase 1 work items are tracked in [`PHASE_1_CHECKLIST.md`](PHASE_1_CHECKLIST.md). The canonical documentation refactor is tracked in [`07_archive/documentation_refactor/DOCUMENTATION_REFACTOR_PLAN_COMPLETED.md`](07_archive/documentation_refactor/DOCUMENTATION_REFACTOR_PLAN_COMPLETED.md), with focused phase audits recorded in [`07_archive/documentation_refactor/DOCUMENTATION_REFACTOR_AUDITS_COMPLETED.md`](07_archive/documentation_refactor/DOCUMENTATION_REFACTOR_AUDITS_COMPLETED.md).

The canonical baseline vocabulary is maintained in [`03_core_baseline_system/00_baseline_framework_glossary.md`](03_core_baseline_system/00_baseline_framework_glossary.md).

The current unresolved definitions and decision history are maintained in:

- `06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md`
- `06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md`

## Compatibility, Conversion, and Inspiration

The distinctions between primary compatibility targets, secondary conversion targets, design inspirations, and research references are maintained in:

```text
01_design_philosophy_and_pillars/02_inspirations_and_anchors.md
05_conversion_and_content_engine/
```

The research evidence and design-process resources are catalogued in [`02_comparative_system_analysis/25_rpg_system_design_process_resources.md`](02_comparative_system_analysis/25_rpg_system_design_process_resources.md). It records external designer case studies, forum lessons, playtesting guidance, and actionable process practices that inform—without overriding—the canonical rules.

The complete index of catalogued game systems, engines, tactical references, and process references is [`02_comparative_system_analysis/00_reference_and_inspiration_system_index.md`](02_comparative_system_analysis/00_reference_and_inspiration_system_index.md).

## Workspace Structure

```text
/home/user/ttrpg_idealization/
├── README.md
├── 01_design_philosophy_and_pillars/
│   ├── 01_core_design_pillars.md
│   └── 02_inspirations_and_anchors.md
├── 02_comparative_system_analysis/
│   ├── 01_architecture_matrix_v3_expanded.md
│   ├── 02_mathless_resolution_case_studies.md
│   ├── 03_mythras_and_brp_case_study.md
│   ├── 04_mathematical_calibration_and_ttk_vectors.md
│   ├── 05_sotdl_and_weird_wizard_comparative_analysis.md
│   ├── 06_level_by_level_progression_comparison_vs_sotdl.md
│   ├── 07_dnd_3_5e_comparative_analysis_and_progression.md
│   ├── 08_shared_spell_slot_progression_comparative_catalog.md
│   ├── 09_at_least_probability_matrices.md
│   ├── 10_foundational_math_reference_analysis.md
│   ├── 11_floor_equipment_dc_target_calibration.md
│   ├── 13_probability_band_calibration.md
│   ├── 14_difficulty_vector_probability_matrices.md
│   ├── 15_provisional_tier_difficulty_vectors.png
│   ├── 16_generic_pool_volume_probability_matrices.md
│   ├── 17_generic_die_size_probability_matrices.md
│   ├── 18_full_level_1_20_probability_progression.md
│   ├── 18_full_level_1_20_probability_progression.png
│   ├── 19_opposed_probability_tables.md
│   ├── 20_automatic_success_probability_tables.md
│   ├── 20_automatic_success_probability.png
│   ├── 22_all_probability_band_vector_combinations.md
│   ├── 24_opposed_tier_profile_probability.md
│   ├── 24_opposed_tier_profile_probability.png
│   ├── 25_rpg_system_design_process_resources.md
│   ├── 26_conditions_and_injury_state_catalogue.md
│   ├── 27_attribute_advancement_cadence_model.md
│   ├── 28_fixed_damage_and_armor_design_catalogue.md
│   ├── 29_weapon_and_armor_category_matrix_draft.md
│   ├── 30_level_1_fixed_damage_and_armor_model.md
│   ├── 31_level_1_power_attack_model.md
│   ├── 32_level_1_penetration_and_power_attack_model.md
│   ├── 33_class_defense_progression_equivalence_model.md
│   └── spell_slot_progression_reference_derived.csv
├── 03_core_baseline_system/
│   ├── 00_baseline_framework_glossary.md
│   ├── 01_resolution_engine.md
│   ├── 02_attributes_and_derived_statistics.md
│   ├── 03_character_schema_and_actor_creation.md
│   ├── 04_action_economy_and_turn_structure.md
│   ├── 05_spatial_and_distance_engine.md
│   ├── 06_leveling_and_tier_progression.md
│   ├── 07_check_pool_generation_and_class_differentiation.md
│   ├── 08_statistical_framework_and_check_modes.md
│   ├── 09_domains_skills_activities_and_crafting.md
│   ├── 10_magic_schools_traditions_and_spellcasting.md
│   ├── 11_master_top_to_bottom_system_summary.md
│   ├── 12_equipment_durability_and_economy.md
│   └── 13_tier_difficulty_vector_reference.md
├── 04_simulationist_subsystems/
│   ├── 01_defenses_and_damage_modeling.md
│   ├── 02_skills_and_generic_capabilities.md
│   ├── 03_resources_conditions_and_wounds.md
│   └── 04_combat_maneuvers.md
├── 05_conversion_and_content_engine/
│   ├── 01_dnd_3_5e_conversion_procedure.md
│   ├── 02_demon_lord_conversion_procedure.md
│   ├── 03_pf2e_and_general_content_guidelines.md
│   └── classes/
│       ├── README.md
│       ├── 01_dnd_3_5e_base_class_profiles_draft.md
│       └── dnd_3_5e_srd_sources/
├── 06_brainstorming_logs_and_roadmap/
│   ├── 01_master_brainstorm_log.md
│   ├── 02_probability_and_dice_simulations.md
│   ├── 03_outstanding_definitions_index.md
│   ├── 04_maneuver_activity_matrix_draft.md
│   ├── 05_maneuver_activity_matrix_revision_1_draft.md
│   ├── 06_maneuver_activity_matrix_revision_2_draft.md
│   ├── 07_maneuver_framework_canonical_and_tbd_draft.md
│   ├── 09_activity_procedure_model_draft.md
│   ├── 10_craft_downtime_and_repair_research_draft.md
│   └── 11_craft_procedure_comparison_matrix.md
└── 07_archive/
    ├── README.md
    └── deprecated_skill_architecture/
        ├── README.md
        └── 14_pulverized_skill_matrix_and_hybrid_path_classes_ARCHIVED.md
```

---

## Document Status

- **Canonical rules:** Active files in `03_core_baseline_system` and `04_simulationist_subsystems`.
- **Conversion and content procedures:** `05_conversion_and_content_engine`.
- **Discussion and research:** `01_design_philosophy_and_pillars`, `02_comparative_system_analysis`, and `06_brainstorming_logs_and_roadmap`.
- **Archived/deprecated designs:** `07_archive`.

The authoritative index of unresolved definitions and stale option language is:

```text
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md
```

---

## Recommended Next Work

1. Complete OD-001B: preparation and learned-spell limits.
2. Complete OD-001C: acquisition stacking and multiclass spell acquisition.
3. Complete OD-001D: Essence expenditure and casting stability.
4. Finalize the Magic Mastery and spellcasting engine.
5. Build the Core Feat Compendium.
6. Convert the first complete spell catalogue.
7. Perform a canonical-document consistency audit for historical option language and superseded terminology.
