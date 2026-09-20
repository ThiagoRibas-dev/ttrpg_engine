# Phase 1 Checklist — Foundational Framework and Scaffolding

**Project phase:** Phase 1 — Foundational Framework and Scaffolding  
**Authoritative scope record:** [`PROJECT_STATUS.md`](PROJECT_STATUS.md)  
**Outstanding definitions:** [`06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md`](06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md)  
**Completed refactor records:** [`07_archive/documentation_refactor/README.md`](07_archive/documentation_refactor/README.md)

This checklist tracks post-refactor Phase 1 framework work. The R0–R13 Documentation Refactor is complete and archived. This file is a project-management artifact, not a source of canonical mechanics. The canonical rules remain in `03_core_baseline_system/` and `04_simulationist_subsystems/`.

## Completed Documentation Refactor

- [x] R0–R13 Documentation Refactor completed.
- [x] Canonical file ownership consolidated.
- [x] Research and reference material separated from canonical rules.
- [x] Final active-document link and terminology audit completed.
- [x] Historical refactor artifacts archived.

Status markers:

- `[x]` Completed or sufficiently established for the current framework phase.
- `[~]` In progress, provisional, or partially defined.
- `[ ]` Not yet completed.

## How to Read This Checklist

Each substantive task should be understood through three questions:

```text
What has been done?
Where is it defined?
What remains open?
```

When a task has a canonical owner, the owner is listed below or beside the task. Research, simulation, and unresolved questions point to their relevant artifacts rather than being resolved here.

### Core Ownership Map

| Topic | Canonical owner or reference |
|---|---|
| Vocabulary | `03_core_baseline_system/00_baseline_framework_glossary.md` |
| Universal resolution | `03_core_baseline_system/01_resolution_engine.md` |
| Attributes and capacity derivation | `03_core_baseline_system/02_attributes_and_derived_statistics.md` |
| Character and actor schema | `03_core_baseline_system/03_character_schema_and_actor_creation.md` |
| Progression and Spell Slot Advancement | `03_core_baseline_system/06_leveling_and_tier_progression.md` |
| Statistical relationships | `03_core_baseline_system/07_check_pool_generation_and_class_differentiation.md`, `08_statistical_framework_and_check_modes.md` |
| Domains, Skills, Activities, and Craft | `03_core_baseline_system/09_domains_skills_activities_and_crafting.md` |
| Magic and Tradition Skills | `03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md` |
| Equipment framework | `03_core_baseline_system/12_equipment_durability_and_economy.md` |
| Defense, damage, and wounds | `04_simulationist_subsystems/01_defenses_and_damage_modeling.md` |
| Combat maneuvers | `04_simulationist_subsystems/04_combat_maneuvers.md` |
| Resource expenditure and recovery | `04_simulationist_subsystems/03_resources_conditions_and_wounds.md` |
| Probability and calibration evidence | `02_comparative_system_analysis/`, `06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md` |
| Open definitions | `06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md` |

---

## 1. Project Governance and Documentation

- [x] Establish the canonical/research/conversion/archive directory structure.
- [x] Separate canonical rules from discussion artifacts and deprecated designs.
- [x] Create `AGENTS.md` with source-of-truth hierarchy and decision-recording protocol.
- [x] Create `PROJECT_STATUS.md` with current phase, scope boundaries, and exit criteria.
- [x] Create the Outstanding Definitions Index.
- [x] Establish Locked, Provisional, and Open decision-status vocabulary.
- [x] Establish the rule that Agent proposals require explicit User approval before becoming decisions.
- [x] Establish the single-source-of-truth rule for canonical mechanics and terminology.
- [x] Establish low-memory feature-conversion discipline and source-name retention for unfinished conversion content.
- [x] Create the Baseline Framework Glossary for shared canonical vocabulary.
- [x] Archive the former 65-skill Pulverized Master Matrix.
- [~] Perform a complete canonical-document consistency audit.

## 2. Core Resolution Mathematics

- [x] Establish step-pool resolution as the universal core engine.
- [x] Establish the baseline `2dX keep highest` check.
- [x] Establish fixed DC resolution.
- [x] Establish opposed-roll resolution.
- [x] Establish Defender Wins Ties for opposed checks.
- [x] Establish the ordinary die ladder: `d4 → d6 → d8 → d10 → d12`.
- [x] Remove deprecated `d12+`, `d12+1`, and `d12+2` terminology from active documentation.
- [x] Establish that the ordinary mathematical ceiling is `d12`.
- [x] Establish Boons as same-size additional dice.
- [x] Establish Banes as dice removed from the pool.
- [x] Establish that a Bane applied to a one-die pool causes one Die Step-Down.
- [x] Establish that further Banes do not apply additional Die Step-Downs.
- [x] Establish automatic failure when a Bane would step a `d4` down.
- [x] Establish Die Step-Up and Die Step-Down terminology.
- [x] Remove deprecated Hyper-Shift terminology from active documentation.
- [x] Establish the normal pool range of `1dX` to `6dX` for baseline Competency.
- [x] Remove the explicit Competency Floor mechanic.
- [x] Establish the six Competency Ranks: Untrained, Trained, Veteran, Master, Hero, Legend.
- [x] Establish Good, Medium, and Bad protected Skill / paired-defense progression tracks.
- [x] Establish Target Number and Difficulty Class as separate concepts.
- [x] Establish working Difficulty Class names.
- [x] Establish comma-separated Difficulty Vectors such as `DC X`, `DC X,Y`, and `DC X,Y,Z`.
- [x] Establish multi-success resolution as a core framework.
- [x] Finalize all Boon/Bane stacking and cancellation edge cases.
- [x] Establish the shared Tag / Trait taxonomy and Piercing Trait / Attack Tag interaction.
- [x] Finalize all opposed-roll secondary tie-break procedures.
- [x] Finalize the interpretation of exceptional high-tier effects that previously used over-cap dice.
- [x] Archive superseded Required-Success probability research.
  - Archive: `07_archive/phase1_probability/12_multi_success_probability_matrices_DEPRECATED_REQUIRED_SUCCESS.md`.
- [x] Keep probability matrices and calibration plots as research artifacts referenced by the Statistical Framework.
- [x] Generate generic Die Size probability matrices holding pool volume constant.
  - Research: `02_comparative_system_analysis/17_generic_die_size_probability_matrices.md`.
- [x] Generate full Level 1–20 probability progression using provisional equipped pools and Tier Difficulty Vectors.
  - Research: `02_comparative_system_analysis/18_full_level_1_20_probability_progression.md`.
- [x] Generate opposed probability tables with Defender Wins Ties.
  - Research: `02_comparative_system_analysis/19_opposed_probability_tables.md`.
- [x] Calculate and plot opposed probabilities across Attacker/Defender Tier profiles.
  - Research: `02_comparative_system_analysis/24_opposed_tier_profile_probability.md`.
- [x] Generate Automatic Success reduction tables and chart.
  - Research: `02_comparative_system_analysis/20_automatic_success_probability_tables.md`.
- [x] Generate the Tier Easy/Medium/Hard Difficulty Vector convention table.
  - Research: `02_comparative_system_analysis/21_tier_difficulty_vector_convention_table.md`.
- [x] Exhaustively enumerate all Difficulty-Vector combinations within the Easy/Medium/Hard calibration bands for the representative pools.
  - Research: `02_comparative_system_analysis/22_all_probability_band_vector_combinations.md`.
- [x] Canonize official one-vector-per-length Tier Difficulty Vector suggestions.
  - Research: `03_core_baseline_system/13_tier_difficulty_vector_reference.md`.
- [x] Complete consolidated probability tables for pool sizes, Difficulty Vectors, Boons, Banes, and Die Step-Ups.
  - Generic pool-volume research: `02_comparative_system_analysis/16_generic_pool_volume_probability_matrices.md`.
  - Generic die-size research: `02_comparative_system_analysis/17_generic_die_size_probability_matrices.md`.
  - Difficulty-vector research: `02_comparative_system_analysis/14_difficulty_vector_probability_matrices.md`.
  - Automatic Success research: `02_comparative_system_analysis/20_automatic_success_probability_tables.md`.
  - Research: `02_comparative_system_analysis/14_difficulty_vector_probability_matrices.md`, `13_probability_band_calibration.md`, and `15_provisional_tier_difficulty_vectors.png`.
- [x] Establish final design-calibration bands: Easy 80–95%, Medium 60–75%, Hard 40–55%.
- [x] Complete opposed probability evaluation across Attacker/Defender Tier profiles.
  - Research: `02_comparative_system_analysis/24_opposed_tier_profile_probability.md`.
- [x] Defer Automatic/Impossible classification to natural Dice Size, Dice Pool, and Difficulty Vector outcomes.
- [x] Remove the need for a separate Extreme-vector convention.
- [ ] Validate the framework through playtesting after consolidation and MVP content creation.
- [ ] Validate the probability model through dedicated simulations and playtest data.

### Resource Ownership Clarification

- [x] Establish resource capacity derivations and Resource Values.
  - Owner: `03_core_baseline_system/02_attributes_and_derived_statistics.md`
- [x] Establish shared resource expenditure, recovery, depletion, and zero-resource consequences.
  - Owner: `04_simulationist_subsystems/03_resources_conditions_and_wounds.md`
  - Status: Framework complete. Content-specific ability procedures, detailed treatment content, and deferred Provision/campaign-resource procedures are separately owned.
- [x] Establish the shared magical Essence framework.
  - Owner: `03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md`
  - Status: Framework complete. Spell-specific, Metamagic, Class-feature, Feat, item, and future psychic/psionic costs are separately owned content work.

## 3. Attributes and Actor Statistics

- [x] Establish the six Attributes: STR, DEX, CON, INT, WIS, CHA.
- [x] Establish Attributes as die sizes rather than numerical modifiers.
- [x] Establish paired defenses:
  - [x] Fortitude: STR + CON.
  - [x] Reflexes: DEX + INT.
  - [x] Willpower: WIS + CHA.
- [x] Establish the Universal Actor Schema.
- [x] Establish Race/Ancestry, Background/Origin, Class/Prestige Classes, Skills, and Feats as actor blocks.
- [x] Establish Background Primary Attribute Focus.
- [x] Establish Secondary Attribute Step Points as a progression concept.
- [x] Establish permanent Attribute advancement, Attribute Score Increase levels, Attribute Point costs, Attribute Step Investments, and d12 limits; Exert remains the explicit temporary d12-to-d20 exception.
- [x] Establish Resource Values, Attribute Bases, and Good/Mediocre/Bad/None resource advancement tracks.

## 4. Competency, Skills, and Domains

- [x] Establish Competency Ranks as independent from Character Level.
- [x] Establish individual Skills rather than universal broad checks.
- [x] Establish Domains as game entities that may interact with classes, feats, equipment, and prerequisites.
- [x] Establish the eight current Domains:
  - [x] Combat Mastery.
  - [x] Athletics, Movement, and Survival.
  - [x] Subterfuge and Perception.
  - [x] Knowledge and Technical Practice.
  - [x] Lore and Cultural Familiarity.
  - [x] Social and Influence.
  - [x] Magic Mastery.
  - [x] Craft and Production.
- [x] Establish Activities and Procedures as distinct from Skills.
- [x] Move Investigation, Forgery, Disguise, Escape Artistry, Lockpicking, Trap Disarming, Shadowing, and similar tasks into the activity/procedure framework.
- [x] Establish open-ended Lore specialties as a concept.
- [x] Establish formal Knowledge skills as a concept.
- [x] Establish Craft specialties as a concept.
- [x] Establish vehicle proficiencies as a concept.
- [x] Establish Craft specialty catalogue, separate specialty Competency Ranks, and `Craft — X` sheet notation.
- [x] Establish Craft Activity families, workshops, hybrid materials, projects, Outcome Rolls, and core repair procedures; individual recipes and projects are content work.
- [x] Establish Lore specialty rank, `Lore — X` sheet notation, scope boundary, and content-grant ownership.
- [x] Establish the baseline Activity, assistance, tool, failure, multi-skill, Craft, Lore, and Knowledge procedure framework.
- [~] Define individual Activity procedures, Difficulty Vectors, costs, outputs, and failure consequences.
- [x] Establish Domains as canonical Skill categories that other mechanics, effects, and content may reference without creating a second proficiency rank.

### Spell Slot Progression Ownership

- [x] Establish Spell Slot Advancement and Spell Slot Progression Level.
  - Owner: `03_core_baseline_system/06_leveling_and_tier_progression.md`
- [ ] Place the authoritative Reference Good Slot Progression table in its canonical owner.
  - Owner: `03_core_baseline_system/06_leveling_and_tier_progression.md`
  - Current reference artifact: `02_comparative_system_analysis/spell_slot_progression_reference_derived.csv`
- [x] Cross-reference the Magic framework to the Spell Slot Progression owner.
  - Magic: `03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md`
  - Progression: `03_core_baseline_system/06_leveling_and_tier_progression.md`
- [ ] Define explicit Heightened spell entries and their relationship to Spell Circle.
  - Owner: `03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md`
  - Status: Open in the Outstanding Definitions Index.

## 5. Character Advancement Architecture

- [x] Establish six High Fantasy Tiers.
- [x] Establish the 20-level mortal progression.
- [x] Establish Mythic as Level 21+.
- [x] Establish Classes and Prestige Classes as the current terminology.
- [x] Establish level-by-level class tables as the authoritative advancement format.
- [x] Establish that Prestige Classes use the same advancement procedure as Base Classes, with entry requirements.
- [x] Establish Class and Prestige Class Spell Slot Advancement entries.
- [x] Establish multiclassing by adding completed Spell Slot Advancements.
- [x] Establish Good, Medium, and Bad Competency / paired-defense progression cadence.
- [x] Establish universal manual Skill Investment schedule: 6 at Level 1 and 1 at each later Character Level.
- [x] Establish Character-Level Skill Rank caps, Class Skill-list access, and class-granted additional Skill Investments.
- [x] Establish universal Class document structure and level-by-level Class table column standards.
- [~] Finalize the remaining relationship between class features, Feats, Skills, Domains, Attributes, Equipment, and resources through representative Class tables.
- [ ] Draft representative framework-only class tables for testing; do not yet expand into finalized class content.

## 6. Action Economy and Combat Scaffolding

- [x] Establish six-second Rounds, one Turn per Actor, fixed and round-by-round Reflex Initiative, and fixed-choice or round-by-round Fast-Slow Side Initiative.
- [x] Establish Delay as a move-later initiative option for the current Round.
- [x] Establish awareness and no-surprise-round encounter entry.
- [x] Establish the three-action turn structure.
- [x] Establish one Reaction per Turn for special interventions; remove Free Guard.
- [x] Establish five spatial distance tiers.
- [x] Establish Stride as a one-tier movement action.
- [x] Establish triggered Deflect/Evasion, passive Fortitude/Willpower, and special-intervention Reaction pressure.
- [x] Establish the baseline combat-maneuver catalogue and its defined Action/resource procedures.
- [~] Finalize remaining detailed baseline maneuver procedures: Shove forced movement, Disarm, Rally, Intimidate, Taunt, and Assess.
- [x] Establish Attack of Opportunity and Trip baseline procedures.
- [x] Establish Prone, Restrained, Immobilized, Grapple, and Escape baseline procedures.
- [x] Establish multi-success maneuver triggers.
- [x] Establish Natural Criticals and Called Shots as distinct mechanics.
- [x] Establish anatomical location and wound concepts.
- [~] Defer Rabble, Underling, Iconic Champion, and other simplified-actor procedures pending a dedicated future subsystem.
- [~] Finalize action-cost and multi-action attack fatigue procedures.
- [x] Establish baseline Deflect, Evasion, Interpose, Soften Blow, Ward Self, and Full Defense Stamina expenditure.
- [~] Finalize other active-defense and maneuver-resolution procedures.
- [~] Finalize combat pacing and encounter calibration.

## 7. Defenses, Damage, and Wounds

- [x] Establish layered defenses rather than one universal Armor Class.
- [x] Establish Damage Absorption as a post-hit defensive layer.
- [x] Establish Vitality and wound conditions as separate consequences.
- [x] Establish the distinction between Natural Critical wounds and Called Shot wounds.
- [x] Establish baseline anatomical Wound Rolls and location Conditions.
- [x] Establish fixed Damage Boxes, post-hit Damage Absorption, and the ordinary damage sequence.
- [~] Finalize weapon Damage Box values, categories, Traits, and selective Piercing access.
- [~] Finalize armor-category Traits and detailed shield interaction.
- [~] Finalize Wound severity and detailed treatment content; baseline stabilization and recovery are complete.
- [ ] Run complete combat probability and time-to-defeat calibration after the above rules are stable.

## 8. Equipment and Economic Scaffolding

- [~] Establish the requirement that equipment must use bounded, discrete vectors rather than linear bonuses.
- [x] Identify bounded equipment vectors: Damage Boxes, Damage Absorption, Durability, Traits, critical profiles, and action permissions.
- [~] Define weapon-category and fixed Damage Box framework.
- [x] Establish standard equipment body slots.
- [x] Establish baseline armor Damage Absorption bands: Unarmored 0, Light 2, Medium 3, Heavy 4.
- [~] Define armor-category Traits, requirements, and detailed Damage Absorption framework.
- [ ] Define shields and Deflect interaction.
- [x] Establish core Equipment Durability points, Damaged/Broken states, Simple Repair, and Broken Repair; detailed attrition remains deferred.
- [ ] Define masterwork, magical, and special-material scaling.
- [ ] Define crafting, repair, and replacement assumptions.
- [ ] Define wealth, equipment access, and campaign-economic expectations by level.
- [ ] Decide whether formal wealth-by-level guidance is required.
- [ ] Test equipment progression against character, monster, and spell progression during the future Equipment/content phase.

### Automatic Success Ownership

- [x] Establish Automatic Success as a universal framework concept.
  - Vocabulary: `03_core_baseline_system/00_baseline_framework_glossary.md`
  - Procedure: `03_core_baseline_system/01_resolution_engine.md`
- [~] Define which Classes, Feats, Spells, Equipment, and Mythic effects grant Automatic Successes.
  - Owners: Relevant future content files.
  - Status: Sources and limits remain open.
- [ ] Calibrate Automatic Success frequency and impact.
  - Research: `02_comparative_system_analysis/`
  - Simulation notes: `06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md`

## 9. Magic and Spellcasting Scaffolding

- [x] Establish Schools, Traditions, and Traits as the universal spell classifications.
- [x] Remove Mantles as a universal spell axis.
- [x] Establish fixed spell lists by Tradition.
- [x] Establish Classes and Prestige Classes as granting Tradition access rather than class-owned spell lists.
- [x] Establish the Cleric / Divine-Domain access pattern: Cleric grants Divine access; each Divine Domain grants a specified additional Tradition and may grant other Features.
- [x] Canonize the 28-Skill Magic Mastery Tradition catalogue and Divine-Domain-to-Tradition mapping, including Domain Tradition Grants, the four elements, Sound, and cardinal alignment Traditions.
- [x] Establish Class-specific additional Magic Mastery-only Skill Investments; one at a Spell Slot Advancement is the normal caster-class benchmark, not a universal requirement.
- [x] Establish one universal preparation system.
- [x] Establish one shared daily Spell Slot pool.
- [x] Establish Spell Slot Advancement.
- [x] Establish Spell Slot Progression Level.
- [x] Establish the Reference Good Slot Progression.
- [x] Establish full, every-other-level, and every-four-level advancement cadences as design guidelines.
- [x] Establish Tradition Competency as controlling spell access and intrinsic scaling, not slot access.
- [x] Rename Focus to Essence.
- [x] Keep Essence separate from Stamina.
- [~] Define preparation and learned-spell limits.
- [~] Define spell-acquisition stacking and multiclass acquisition.
- [~] Define Essence expenditure and casting stability.
- [~] Define explicit Heightened spell rules.
- [~] Define 0th-Circle and Essence interaction.
- [~] Define Mythic spell requirements.
- [ ] Begin broad spell conversion only after the framework is stable.

### Skill Architecture versus Content Catalogue

- [x] Establish the Domain, Skill, Activity, Procedure, Lore, Knowledge, Craft, and vehicle framework.
  - Owner: `03_core_baseline_system/09_domains_skills_activities_and_crafting.md`
- [~] Finalize Craft, Lore, Knowledge, vehicle, and Activity procedures.
  - Owner: `03_core_baseline_system/09_domains_skills_activities_and_crafting.md`
  - Status: Framework exists; detailed procedures remain open.
- [ ] Create complete Skill, Craft, Lore, Activity, and specialty catalogues.
  - Status: Future content task, outside the current framework consolidation.

## 10. Conversion and Compatibility Framework

- [x] Establish D&D 3.5e as the foremost compatibility target.
- [x] Establish separate documentation categories for compatibility targets, conversion targets, inspirations, and research references.
- [x] Establish conversion procedures as distinct from canonical rules.
- [~] Audit conversion documents for stale mechanics and terminology.
- [ ] Validate the framework by converting representative D&D 3.5e material.
- [ ] Validate the framework against Pathfinder, SotDL/WW, Mythras/BRP, and tactical content after the core is stable.

## Project-Status Synchronization Reminder

- [ ] After each substantive Phase 1 decision, execution step, or scope change, review and update `PROJECT_STATUS.md` so it remains synchronized with this checklist and the Outstanding Definitions Index.

## 11. Phase 1 Exit Review

- [ ] Core mathematical framework is internally consistent.
- [ ] Validate prescriptive and emergent gameplay loops against stated design intent through scenario tests, conversion cases, simulations, and later playtesting.
- [ ] All ordinary resolution stays within the d12/DC 12 bounded framework.
- [ ] Probability targets have been tested and accepted.
- [ ] Character progression vectors have distinct mechanical roles.
- [ ] Equipment and economic scaffolding is defined.
- [ ] Spell-slot and Essence scaffolding is defined.
- [ ] Combat, defense, and wound math is calibrated.
- [ ] Major outstanding framework questions are resolved or explicitly deferred.
- [ ] Canonical documents pass a consistency audit.
- [ ] The project is ready to begin systematic content production.

---

## Current Immediate Priorities

1. Define equipment and economic scaffolding.
2. Finalize activity, Craft, Lore, and Domain procedures.
3. Complete spell preparation, acquisition, and Essence expenditure definitions.
4. Calibrate combat, damage, Wounds, action costs, and encounter pacing.
5. Create representative framework-only class tables and validate conversion procedures.
6. Validate the completed probability framework through content-specific testing and later playtest data.
7. Only then begin systematic framework-test classes, feats, spells, ancestries, and monsters.

Mythic expansion remains intentionally deferred until the Level 1–20 framework is stable.
