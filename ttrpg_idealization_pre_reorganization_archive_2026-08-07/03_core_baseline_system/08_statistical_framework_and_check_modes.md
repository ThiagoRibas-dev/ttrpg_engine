# Statistical Framework and Check Modes

**Status:** Canonical framework scaffold.

This document is the canonical home for the system-wide statistical model and the relationship between check modes. It consolidates the framework formerly discussed in the attack/spell architecture and comparative check-pool documents without replacing the detailed procedures in the Resolution Engine.

## Scope

This document will define and cross-reference:

- Attribute Die Size as capability ceiling.
- Competency Rank as baseline Dice Pool Size; final pool size and Difficulty Vector determine probability.
- Natural Dice Pools and Enhanced Dice Pools.
- Fixed-DC checks.
- Difficulty Vectors using comma-separated thresholds.
- Opposed checks.
- Defender Wins Ties.
- Multi-success counting.
- Attack and defense pool relationships.
- Spell and skill checks using the universal engine.
- Bounded d12/DC 12 mathematical assumptions.

## Difficulty Vectors

Difficulty uses comma-separated threshold vectors such as `DC 5`, `DC 5,4`, or `DC 6,5,3`. Roll the final Dice Pool, sort dice and thresholds from highest to lowest, and compare positionally.

## Probability Research References

The statistical consequences of this framework are measured in research artifacts, not defined by them:

- `../02_comparative_system_analysis/09_at_least_probability_matrices.md`
- `../02_comparative_system_analysis/13_probability_band_calibration.md`
- `../02_comparative_system_analysis/14_difficulty_vector_probability_matrices.md`
- `../02_comparative_system_analysis/16_generic_pool_volume_probability_matrices.md`
- `../02_comparative_system_analysis/20_automatic_success_probability_tables.md`
- `../02_comparative_system_analysis/24_opposed_tier_profile_probability.md` — opposed Tier-profile calibration.
- `13_tier_difficulty_vector_reference.md` — official suggested Tier Difficulty Vectors.

These documents provide evidence and calibration data. They do not override canonical rules or define final target bands.

## Source of Truth

- Universal resolution procedures: `01_resolution_engine.md`.
- Attributes and derived statistics: `02_attributes_and_derived_statistics.md`.
- Combat and damage procedures: `04_simulationist_subsystems/01_defenses_and_damage_modeling.md`.
- Domains, skills, activities, and crafting: `09_domains_skills_activities_and_crafting.md`.
- Magic Schools, Traditions, Traits, and spellcasting: `10_magic_schools_traditions_and_spellcasting.md`.

The former `attacks_and_spells_vs_skills_architecture` and comparative check-pool documents are retained as reference material under `02_comparative_system_analysis/archived_core_reference/`.

## Current Boundary

This file is a consolidation scaffold. It does not create new mathematical rules or resolve open probability-calibration questions. Those remain tracked in the Outstanding Definitions Index and Phase 1 checklist.
