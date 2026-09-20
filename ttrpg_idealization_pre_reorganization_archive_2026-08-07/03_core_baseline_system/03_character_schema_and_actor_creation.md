# Character Schema and Actor Creation

**Status:** Canonical actor-structure framework.  
**Scope:** The building blocks used to create PCs, NPCs, monsters, bosses, and underlings. This file does not duplicate Attribute derivations, universal resolution, skill procedures, combat procedures, or spellcasting procedures.

## 1. Universal Actor Schema

Every actor is built from five building blocks:

```text
Race/Ancestry
Background/Origin
Class and Prestige Classes
Skills
Feats
```

The same schema applies to:

- Player Characters.
- Human and humanoid NPCs.
- Monsters.
- Bosses.
- Rabble and Underlings.

The implementation may simplify presentation for Rabble and Underlings, but the conceptual building blocks remain universal.

## 2. Race/Ancestry

Race/Ancestry represents biological, species-based, or origin-based traits, including:

- Size.
- Movement modes.
- Senses.
- Natural weapons.
- Natural defenses.
- Immunities and resistances.
- Ancestry Traits.
- Ancestry Feats.

Attribute Dice, derived statistics, and paired defenses are defined in `02_attributes_and_derived_statistics.md`.

## 3. Background/Origin

Background/Origin represents upbringing, prior vocation, training context, and life history.

It may provide:

- Primary Attribute designation.
- Starting Skill access or Competency.
- Background permissions.
- Lore or Knowledge specialties.
- Equipment or social access.

Background does not replace Class or Skills. Its Attribute and advancement procedures belong to the Attributes and Level Advancement documents.

## 4. Class and Prestige Classes

Classes represent the actor’s primary vocational and advancement structure. Prestige Classes use the same framework but require entry conditions.

Class and Prestige Class tables may provide:

- Vitality, Stamina, and Essence track assignments and advancement.
- Spell Slot Advancements.
- Tradition access.
- Skill allocations.
- Feats and class features.
- Combat or magical competency protection.
- Requirements and Permissions.

The level-by-level class table is authoritative for advancement. Class content is not being broadly designed during the current Foundational Framework phase.

## 5. Skills

Skills represent transferable domains of learned competence. Individual Skills are organized into Domains, but Domain organization does not create a second proficiency rank.

The canonical Skill, Domain, Lore, Knowledge, Craft, Activity, and Tool framework belongs in:

```text
09_domains_skills_activities_and_crafting.md
```

This file should not duplicate that taxonomy.

## 6. Feats

Feats are discrete vector traits and permissions. They may affect:

- Action economy.
- Requirements and Permissions.
- Combat maneuvers.
- Skills and Activities.
- Equipment use.
- Magic and Metamagic.
- Ancestry capabilities.
- Resource expenditure.

The full Feat Compendium is future content and is not being developed during this consolidation phase.

## 7. Actor Record and Source Links

A character or actor record should reference, rather than duplicate:

- Attributes and derived statistics: `02_attributes_and_derived_statistics.md`
- Universal resolution vocabulary and procedures: `00_baseline_framework_glossary.md` and `01_resolution_engine.md`
- Action economy: `04_action_economy_and_turn_structure.md`
- Progression: `06_leveling_and_tier_progression.md`
- Skills and Domains: `09_domains_skills_activities_and_crafting.md`
- Magic: `10_magic_schools_traditions_and_spellcasting.md`
- Combat and wounds: `../04_simulationist_subsystems/01_defenses_and_damage_modeling.md`
- Resources and recovery: `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md`

## 8. Current Scope Boundary

This document defines actor scaffolding only. It does not finalize:

- Complete Classes.
- Complete Prestige Classes.
- Complete Ancestry catalogues.
- Complete Feat catalogues.
- Complete Monster catalogues.
- Equipment catalogues.

Those remain future content work unless explicitly reopened through the project status and Outstanding Definitions process.
