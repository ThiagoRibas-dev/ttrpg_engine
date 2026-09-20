# Project Status

**Current phase:** Phase 1 — Foundational Framework and Scaffolding  
**Status purpose:** Define and stabilize the system’s fundamental structures before developing large bodies of player-facing content.

This document records the project’s current scope and phase boundaries. It does not replace canonical rules, the decision log, or the Outstanding Definitions Index.

---

## Current Phase: Foundational Framework and Scaffolding

The current work is focused on iterating over fundamentals, comparing alternatives, testing assumptions, and recording major architectural decisions.

This phase includes the framework governing:

### Core resolution and intended mathematics

- Mathless-at-the-table resolution.
- Step dice, Dice Pools, Boons, Banes, Difficulty Vectors, Automatic Successes, and opposed checks.
- Bounded Target Numbers and probability expectations.
- Multi-threshold Difficulty Vector resolution.
- Critical results and tactical outcomes.
- Intended mathematical relationships between attributes, competency, equipment, class advancement, and opposition.
- Low-memory feature-conversion discipline: favor broad, explicit effects over stacks of conditional persistent modifiers.
- Planned framework rewrite uses precise Markdown links and a machine-readable semantic relationship registry.
- Calibration of time-to-defeat, resource pressure, and action economy.

The goal is not to eliminate mathematical analysis during design. The goal is to prevent players and GMs from performing arithmetic during ordinary play.

### Character and actor scaffolding

- Universal Actor Schema.
- Race/Ancestry, Background/Origin, Classes and Prestige Classes, Skills, and Feats as building blocks.
- Attributes and derived statistics.
- Competency Ranks independent from Character Level.
- Domains, Skills, Activities, Knowledge, Lore, Craft, and vehicle proficiencies.
- NPC, monster, boss, and underling construction principles.

### Advancement and progression vectors

The framework must account for all major ways an actor becomes more capable, including:

- Character Level.
- Class and Prestige Class advancement.
- Spell Slot Progression.
- Tradition Competency.
- Skill Competency, including universal manual Skill Investments, Character-Level Rank caps, and Class Skill-list access.
- Attribute Die Step-Up.
- Feats and class features.
- Ancestry progression.
- Equipment improvement.
- Magical items and special materials.
- In-world resources and recovery.
- Mythic advancement.

These vectors must have distinct mechanical jobs and must not accidentally duplicate one another.

### Resource and recovery scaffolding

The shared resource-capacity and advancement chassis, zero-resource states, and ordinary recovery events are established. Remaining work concerns the costs, timing, and effect sizes of individual resource expenditures, plus Wound treatment and detailed recovery effects.

Canonical references:

- `03_core_baseline_system/02_attributes_and_derived_statistics.md`
- `03_core_baseline_system/06_leveling_and_tier_progression.md`
- `04_simulationist_subsystems/03_resources_conditions_and_wounds.md`

### Equipment and economic scaffolding

The foundational phase includes the basic framework governing equipment before individual item catalogues are written. A provisional equipment progression is currently used in probability research, but it is not finalized equipment canon.

Questions at this level include:

- How weapon properties affect attacks, damage, maneuvers, and critical profiles.
- How armor affects Damage Absorption without becoming a linear Armor Class bonus.
- How shields interact with Parry and active defense.
- How equipment durability and item sacrifice function.
- How masterwork, magical, and special-material equipment improve capability.
- How equipment interacts with die size, pool volume, Boons, Banes, Traits, and action economy.
- How wealth, equipment availability, crafting, upkeep, and replacement are expected to scale across character levels.
- Whether the game needs wealth-by-level guidance, expected equipment bands, or campaign-economic benchmarks analogous to D&D 3.5e.
- How equipment progression interacts with class, ancestry, feats, and spellcasting.

The current goal is to define the equipment and economy **framework**, not to write the final weapon, armor, magic-item, or equipment catalogue.

### Magic and supernatural scaffolding

- Schools, Traditions, and Traits.
- Canonical 28-Skill Tradition catalogue and modular Cleric / Divine-Domain access mapping.
- Class-specific Magic Mastery-only Skill Investments, normally benchmarked to one at Spell Slot Advancement; Divine Domain Tradition Grants.
- Unified Vancian preparation.
- Shared Spell Slot Progression.
- Spell Slot Advancement in class tables.
- Essence and supernatural expenditure.
- Spell acquisition and preparation framework.
- Psychic/Psionic power as a future Essence-based system.
- Mythic and Epic magic architecture.

Individual classes, spells, and complete spell lists are not yet the main development focus.

### Probability and statistical scaffolding

- Generic Dice Pool volume research.
- Generic Die Size research.
- Difficulty Vector matrices and Tier references.
- Opposed Tier-profile probability research.
- Automatic Success reduction research.
- Final design-calibration bands: Easy 80–95%, Medium 60–75%, Hard 40–55%.
- Final playtest validation remains deferred until framework consolidation and MVP content creation.

Canonical references:

- `03_core_baseline_system/08_statistical_framework_and_check_modes.md`
- `03_core_baseline_system/13_tier_difficulty_vector_reference.md`

### Combat and encounter scaffolding

- Three-action economy.
- Distance tiers and movement modes.
- Active defenses.
- Parry and defensive reactions.
- Damage Absorption.
- Vitality, wounds, and anatomical conditions.
- Universal combat maneuvers, owned by `04_simulationist_subsystems/04_combat_maneuvers.md`.
- Natural Criticals, Called Shots, and Execution.
- Encounter pacing and time-to-defeat targets.

Simplified-actor procedures such as Rabble or Underlings are deferred. They require a dedicated future subsystem document rather than being embedded in the defense, damage, or resource frameworks.

### Conversion scaffolding

- Procedures for translating D&D 3.5e content, foremost among the compatibility targets.
- Procedures for translating other d20 content.
- Procedures for adapting non-d20 inspirations and tactical material.
- Preservation of conceptual identity while replacing incompatible mechanics.

---

## Framework, Derived-Subsystem, and Content Boundary

The project separates universal framework work from derived subsystem design and player-facing content. This boundary prevents unfinished examples or later catalogues from silently changing the shared engine.

### Fundamental framework

Fundamental work establishes universal procedures, ownership, boundaries, and shared vocabulary. Examples include resource tracks, recovery events, depletion and zero states, Wound and stabilization baseline, Action and Reaction procedures, Activity Tags, default spellcasting-resource ownership, and explicit deferrals.

### Derived subsystem design

Derived work uses the established framework to define subsystem-specific procedures, values, and exceptions. Examples include individual maneuver costs, individual Spell and Metamagic costs, healing-item effects, Class-feature resource effects, weapon and armor values, Durability values, and campaign logistics.

### Content

Content implements the framework through specific Classes, Feats, Spells, items, monsters, equipment catalogues, and adventures.

Fundamental framework decisions belong in their canonical owner and the decision log. Derived procedures and content must not contradict or silently redefine the fundamental framework; they state their own specific costs, effects, exceptions, and Requirements within the established structure.

---

## Gameplay Loop Validation Note

**Status:** Project-process and validation note; non-canonical.  
**Purpose:** Make the system’s explicit procedures and expected emergent play patterns visible so future modeling, scenario tests, conversion tests, and playtests can compare actual behavior against design intent.

### Prescriptive loops

Prescriptive loops are procedures the rules explicitly instruct participants to perform.

| Loop | Current procedure | Current status |
|---|---|---|
| Encounter | Initiative → Turns → Actions / Reactions → Attack and defense sequence → Damage Absorption → mitigation → Vitality / Wounds | Framework established; selected maneuver and equipment details remain open |
| Recovery | Stabilize → treat / rest → recover Vitality, Wounds, Stamina, Essence, and Slots as applicable | Baseline established; content-specific treatment remains open |
| Craft and repair | Meet Craft / tool / recipe requirements → spend stated time → resolve recipe or repair Activity → receive stated output | Activity and core repair baseline established; recipe, project, workshop, and material content remains open |
| Spellcasting | Meet spell requirements → spend stated Actions/resources → resolve stated Activity → apply tags and explicit disruption rules | Framework established; individual Spells and preparation content remain open |
| Advancement | Gain Character Level and Class Level grants → apply Attribute, Skill/defense, resource, slot, feature, and Permission investments | Framework established; representative Class tables remain to be modeled |

### Emergent loops to validate

Emergent loops are expected patterns created by several procedures interacting. They are hypotheses, not rules.

| Expected loop | Intended behavior to test |
|---|---|
| Martial resource loop | Deflect, Evasion, Interpose, Soften Blow, Exert, Charge, Power Attack, and Escape create meaningful Stamina offense-versus-defense decisions |
| Armor and weapon counterplay | Fixed Damage Boxes, Damage Absorption, Piercing, Power Attack, Traits, and future weapon categories create distinct answers to armored and unarmored targets |
| Class specialization loop | Attribute advancement, protected Skills, Good/Medium/Bad defense tracks, resource tracks, Slots, and Class features create distinct but viable archetypes |
| Tactical control loop | Prone, Restrained, Immobilized, Grapple, Trip, Shove, Escape, positioning, and Attacks of Opportunity reward tactical choices without creating unusable restriction stacks |
| Social and information loop | Rally, Intimidate, Taunt, Assess, Lore, Knowledge, and Activities make social and informational choices mechanically meaningful without overriding player agency |
| Craft and expedition loop | Craft specialties, recipe requirements, repair, materials, workshops, downtime, and future Provisions create useful preparation choices without spreadsheet play |
| Conversion loop | D&D 3.5e concepts convert through shared Skills, Traits, Tags, Procedures, Requirements, Permissions, and content-specific effects without reintroducing linear modifiers |

### Validation practice

For each loop, record:

```text
Design intent.
Scenario or conversion case.
Assumptions and actor profiles.
Observed mathematical or play behavior.
Expected behavior.
Difference or failure mode.
Decision, revision, or explicit acceptance.
```

Do not treat an elegant procedure or probability table as proof of an emergent loop. Validate loops through focused simulation, representative content models, conversion examples, and later playtesting.

---

## Framework Re-evaluation Note — Pool Volume and Competency Floors

**Status:** Non-canonical future re-evaluation note. This note does not alter the current Dice Pool, Competency, Bane, or Attribute rules.

The current framework grants higher proficiency through greater Dice Pool volume. Its original design intent is that more dice increase the chance of high results and make an Actor more resistant to Banes.

A future re-evaluation may instead assign Attributes to Die Size and Competency/Proficiency to a guaranteed roll floor. Under that alternative, stronger and more proficient Actors would not necessarily roll more dice; they would produce better results through an increasingly reliable minimum face value.

Any such reconsideration would require dedicated probability modeling, review of Bane interaction, examination of class differentiation and conversion impact, and explicit approval before changing the current canon.

---

## Explicitly Not Yet in Active Scope

The following may appear as examples or future targets, but are not yet being broadly designed or finalized:

- Complete Base Class compendia.
- Complete Prestige Class compendia.
- Finalized feat compendia.
- Finalized spell compendia.
- Complete ancestry compendia.
- Complete monster and NPC rosters.
- Final equipment and magic-item catalogues.
- Complete wealth-by-level tables or campaign economy tables.
- Finished adventure content.
- Full Psychic/Psionic rules.
- Large-scale content balance passes.

References to a Wizard, Cleric, Fighter, spell, feat, ancestry, monster, or item are normally illustrative unless explicitly marked as canonical content.

---

## Phase Exit Criteria

The Foundational Framework and Scaffolding phase is complete when:

- The core resolution engine is stable.
- The intended mathematical vectors are documented and calibrated.
- Character and Universal Actor structures are stable.
- Skills, Domains, Activities, Knowledge, Lore, Craft, and specialties are stable enough for sheet design.
- Action economy and spatial procedures are stable.
- Defenses, Damage Absorption, wounds, and conditions are stable.
- Resource tracks and recovery procedures are stable.
- Class, Prestige Class, and level-by-level advancement architecture is stable.
- Spell Traditions, Spell Slot Progression, preparation, acquisition, and Essence scaffolding are stable.
- Equipment, item scaling, durability, and economic progression frameworks are stable.
- Major conversion procedures are usable.
- Outstanding framework definitions are resolved or deliberately deferred.
- Canonical documents have undergone a consistency audit.

Completion of this phase does **not** require every class, spell, feat, ancestry, item, or monster to be written. It means the structures governing those future content categories are sufficiently stable to support systematic creation.

---

## Completed Structural Work

The R0–R13 Documentation Refactor is complete. Canonical files were reordered and consolidated, research/reference material was separated from canonical rules, and the final link and terminology audit was performed.

Historical refactor records are archived in:

```text
07_archive/documentation_refactor/
```

## Current Navigation

- [Phase 1 Checklist](PHASE_1_CHECKLIST.md)
- [Completed Documentation Refactor Records](07_archive/documentation_refactor/README.md)
- [Project README](README.md)
- [Outstanding Definitions Index](06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md)
- [Master Brainstorm and Decision Log](06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md)
- [Canonical Core Rules](03_core_baseline_system/)
- [Canonical Simulationist Subsystems](04_simulationist_subsystems/)

---

## Update Protocol

Update this document when:

- The project enters a new design phase.
- The active scope materially changes.
- A major framework category is completed, deferred, or reopened.
- Content development formally begins.
- Phase exit criteria are revised.

Do not duplicate individual rules or decisions here. Link to their canonical documents instead.
