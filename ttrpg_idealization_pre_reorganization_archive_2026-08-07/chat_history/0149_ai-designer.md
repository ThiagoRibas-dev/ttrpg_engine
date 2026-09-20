---
turn: 149
role: "AI-Designer"
source: chat_history.json
---

# Turn 149 — AI-Designer

Write
ttrpg_idealization/README.md
168 lines
open
Project Vault: Idealized Mathless Simulationist TTRPG System
MD
Project Vault: Idealized Mathless Simulationist TTRPG System

This workspace develops a high-option-density, simulationist fantasy TTRPG that combines:

D&D 3.5e’s class depth, feats, prestige classes, spell volume, and conversion wealth.
Pathfinder 2e’s structured progression, traits, and tactical three-action economy.
Mythras/BRP’s opposed combat, differential success, hit locations, wounds, and underlings.
Shadow of the Demon Lord / Weird Wizard’s modular class design and Tradition inspiration.
Gloomhaven-style tactical pacing and enemy management.

The system’s core constraint is zero table-side arithmetic: resolution compares die faces directly against static DCs or opposed rolls, using Die Step-Up, Die Step-Down, Boons, and Banes rather than linear numerical modifiers.

Canonical Design Pillars

Mathless Core Resolution

Step pools such as 2dX keep highest.
Fixed DCs from 2 to 12.
Opposed rolls by highest face and tie-breaking procedures.
Boons add same-size dice; Banes remove dice or force worse results.
No linear +1, -2, BAB, ability modifiers, or circumstance stacking.

Simulationist Tactical Play

Three-action turns plus a Free Guard reaction.
Active defenses, paired defenses, Damage Absorption, wounds, hit locations, and combat maneuvers.
Specific skills, activities, tools, equipment, and class permissions.
Rabble, Underlings, and Iconic Champions for practical enemy management.

Zero Meta-Currencies

No Fate Points, Hero Points, Inspiration, Luck Points, or narrative tokens.
In-world resources include Vitality, Stamina, Essence, Vancian Spell Slots, and Equipment Durability.

Universal Actor Schema

Every actor uses:
Race/Ancestry + Background/Origin + Class/Prestige Classes + Skills + Feats.
The schema applies to PCs, NPCs, monsters, bosses, and underlings.

High Fantasy Progression

Trained: Local, Levels 1–4.
Veteran: Regional, Levels 5–8.
Master: Country, Levels 9–12.
Hero: World, Levels 13–16.
Legend: Cosmic, Levels 17–20.
Mythic: Divine, Level 21+.
Canonical Architecture Highlights
Skills and Domains

The canonical skill architecture uses functional Domains containing specific transferable skills:

Combat Mastery.
Athletics, Movement, and Survival.
Subterfuge and Perception.
Knowledge and Technical Practice.
Lore and Cultural Familiarity.
Social and Influence.
Magic Mastery.
Craft and Production.

Activities such as Investigation, Forgery, Disguise, Escape Artistry, Lockpicking, Trap Disarming, Shadowing, Treaty Negotiation, and Interrogation select appropriate skills by method rather than becoming universal skills.

Magic

Magic uses separate axes:

Schools: Eight D&D-compatible technical classifications.
Traditions: Modular magical access and specialization packages.
Mantles: Conceptual domains expressed by magic.
Traits: Practical delivery and interaction descriptors.

Traditions are individual skills with fixed shared spell lists. Classes and Prestige Classes grant Tradition access and spell-acquisition methods; they do not own separate spell lists.

Alchemy is governed by Knowledge and Craft rather than being a Magic Mastery Tradition. Psychic/Psionic power is provisionally a separate Essence-based supernatural system.

Spell Slots

All ordinary spellcasters use one shared daily Spell Slot pool.

Spell Slot Advancement: A level-by-level entry on a class table granting one advancement.
Spell Slot Progression Level: The character’s accumulated position on the Reference Good Slot Progression.
Reference Good Slot Progression: The universal table showing spell slots at Progression Levels 1–20.

Full classes advance every class level, Mediocre classes every other level, and Bad classes every four levels. Every Base Class and Prestige Class displays its actual Spell Slot Advancements level by level.

Workspace Structure
text
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
│   └── spell_slot_progression_reference_derived.csv
├── 03_core_baseline_system/
│   ├── 01_resolution_engine.md
│   ├── 02_character_schema_and_stats.md
│   ├── 03_action_economy_and_turn_structure.md
│   ├── 04_spatial_and_distance_engine.md
│   ├── 05_leveling_and_tier_progression.md
│   ├── 06_check_pool_generation_and_class_differentiation.md
│   ├── 07_attributes_and_derived_statistics.md
│   ├── 08_sources_of_progression_and_conceptual_mapping.md
│   ├── 09_dnd_3_5e_class_advancement_tracks_mapping.md
│   ├── 10_master_top_to_bottom_system_summary.md
│   ├── 11_check_pool_architecture_comparative_matrix.md
│   ├── 12_attacks_and_spells_vs_skills_architecture.md
│   └── 13_building_block_domains_and_master_skill_system.md
├── 04_simulationist_subsystems/
│   ├── 01_defenses_and_damage_modeling.md
│   ├── 02_skills_and_generic_capabilities.md
│   └── 03_resources_conditions_and_wounds.md
├── 05_conversion_and_content_engine/
│   ├── 01_dnd_3_5e_conversion_procedure.md
│   ├── 02_demon_lord_conversion_procedure.md
│   └── 03_pf2e_and_general_content_guidelines.md
├── 06_brainstorming_logs_and_roadmap/
│   ├── 01_master_brainstorm_log.md
│   ├── 02_probability_and_dice_simulations.md
│   └── 03_outstanding_definitions_index.md
└── 07_archive/
    ├── README.md
    └── deprecated_skill_architecture/
        ├── README.md
        └── 14_pulverized_skill_matrix_and_hybrid_path_classes_ARCHIVED.md
Document Status
Canonical rules: Active files in 03_core_baseline_system and 04_simulationist_subsystems.
Conversion and content procedures: 05_conversion_and_content_engine.
Discussion and research: 01_design_philosophy_and_pillars, 02_comparative_system_analysis, and 06_brainstorming_logs_and_roadmap.
Archived/deprecated designs: 07_archive.

The authoritative index of unresolved definitions and stale option language is:

text
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md
Recommended Next Work
Complete OD-001B: preparation and learned-spell limits.
Complete OD-001C: acquisition stacking and multiclass spell acquisition.
Complete OD-001D: Essence expenditure and casting stability.
Finalize the Magic Mastery and spellcasting engine.
Build the Core Feat Compendium.
Convert the first complete spell catalogue.
Perform a canonical-document consistency audit for historical option language and superseded terminology.
Open

It was not fully up to date. The previous README still contained:

An outdated directory listing.
References to the old five-domain skill model.
Older terminology such as Soak and Mana.
The archived 65-skill matrix in the active core directory.
No reference to DEC-052 or DEC-053.
No clear distinction between canonical, research, discussion, and archived material.
No summary of the current unified Tradition and Spell Slot architecture.

I updated it comprehensively.

The README now reflects:

The current canonical design pillars.
The eight-domain skill architecture.
The Schools / Traditions / Mantles / Traits magic model.
Unified spell slots and Spell Slot Progression.
Level-by-level class and Prestige Class Spell Slot Advancements.
The current workspace structure.
The archive location.
The outstanding definitions index.
The current recommended development sequence.
