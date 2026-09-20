# Outstanding Definitions Index

**Status:** Active meta-document  
**Purpose:** Index unresolved definitions, provisional subsystems, and documents that still contain historical option language. This is a navigation document, not a rules document.

Canonical rules override discussion artifacts. Where an entry is marked **Documentation cleanup**, the design decision is already made; only the older document wording remains to be revised.

---

## 1. Active Architectural Definitions

### OD-001 — Magic Mastery tradition skills and spellcasting engine

**Status:** Core architecture resolved by DEC-051; implementation details remain open.

The current tradition list is established provisionally, but the following implementation questions remain:

#### OD-001A — Shared Spell-Slot Progression

**Status:** Resolved by DEC-052; remaining work is calibration and supporting tables.

**Research catalogue:** [Comparative Shared Spell-Slot Progression Catalogue](../02_comparative_system_analysis/08_shared_spell_slot_progression_comparative_catalog.md)

- **Resolved:** Use the modified D&D 3.5e-style Good/Reference slot table indexed by Spellcasting Progression Level.
- **Resolved:** Classes and Prestige Classes show level-by-level Spellcasting Advancement entries in their class tables.
- **Resolved:** Add all completed advancements across classes into one shared Spellcasting Progression Level.
- **Resolved:** “Good,” “Mediocre,” and “Bad” are design guidelines, not player-facing tracks.
- **Resolved:** Tradition Competency does not limit slot access; it controls spell access and intrinsic scaling.
- **Resolved:** Mythic adds Epic Traditions and Spells using the existing slot framework rather than ordinary new slots.
- **Resolved:** Mediocre and Bad are derived views of the Reference Good table, using every-other-level and every-four-level advancement cadences.
- **Resolved:** Derived tables are indexed by Character Level; the Reference table is indexed by Spell Slot Progression Level.
- Remaining: place the authoritative Reference Good Slot Progression table in its canonical owner.
- Remaining: test the proposed slot volume and explicit Heightened spell rules.
- Remaining: define 0th-Circle/Essence interaction and Mythic spell requirements.

#### OD-001B — Preparation and Learned-Spell Limits

- How many spells does a character learn at each level from each class or path?
- How many spells may a character prepare after daily preparation?
- Is the preparation limit based on Character Level, Tradition Competency, class/path features, Essence, or a combination?
- Are prepared spells selected freely from every accessible Tradition, or does each Tradition have a separate preparation allowance?
- Can a character prepare multiple copies of the same spell?
- Does a spell remain learned if the character later loses access to its Tradition?
- Are rituals, cantrips, and 0th-rank spells prepared separately?
- Can a character prepare a spell above their current Tradition Rank for future use?
- How long does preparation take, and what conditions interrupt or restrict it?

#### OD-001C — Acquisition Stacking and Multiclassing

- When a character gains levels in multiple classes, do all class-based spell-acquisition features apply?
- If a Cleric grants five learned spells and a Wizard grants two, does a Cleric/Wizard receive both acquisitions?
- Can multiple classes grant the same spell, and how is the duplicate handled?
- Can a class acquisition feature teach spells from any accessible Tradition, or only its associated Traditions?
- Can research, scroll transcription, prayer, revelation, mentors, feats, and paths all add spells to the same learned-spell collection?
- Are there limits on non-level-based acquisition during downtime?
- Can one class’s acquisition method expand another class’s preferred Tradition?
- Does access to a Tradition permit learning its entire fixed spell list over time, or are individual acquisition permissions still required?
- How do Prestige Classes and advanced Paths add spells without making early multiclass dips disproportionately efficient?

#### OD-001D — Essence Expenditure and Casting Stability

**Status:** Resource capacity, recovery, zero-resource state, and tagged disruption framework are resolved by DEC-071, DEC-078, and DEC-079. Spell-specific expenditure remains open.

Remaining questions:

- Which effects always cost Essence, and which effects are paid for with Spell Slots?
- How much Essence does each metamagic feat cost?
- Can multiple metamagic effects apply to one spell, and is there a maximum Essence expenditure per casting?
- What happens when a caster cannot or will not spend a required Essence cost?
- How do Turn or Rebuke Undead, Smites, Devotion Feats, and other supernatural features compete with spellcasting for Essence?
- How will the future Psychic/Psionic system use Essence without becoming strictly superior to Vancian spellcasting?

**Relevant documents:**

- [Canonical Magic Architecture](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#2e-canonical-magic-architecture-dec-050)
- [Attacks, Spells, and Skill Architecture](../02_comparative_system_analysis/archived_core_reference/12_attacks_and_spells_vs_skills_architecture_REFERENCE.md#canonical-magic-classification-cross-reference-dec-050)
- [Magic and Focus Decision](../06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md#dec-032)
- [Magic roadmap](../06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md#3-immediate-next-steps--iteration-roadmap)

### Exception-Based Rule Hierarchy

**Status:** Resolved by DEC-103.

The most specific applicable rule supersedes the more general rule within its stated scope. Player-facing entries use the defined rules vocabulary—Traits, Prerequisite, Requirement, Trigger, Frequency, Cost, Effect, Restriction, Exception, and Special—to make their scope and interaction explicit.

**Canonical vocabulary:** [Baseline Framework Glossary](../03_core_baseline_system/00_baseline_framework_glossary.md).

### Resolution and Probability Calibration

**Status:** Core resolution and probability calibration are resolved by DEC-055, DEC-068, and DEC-069.

The current canonical procedure uses bounded DCs and comma-separated Difficulty Vectors. The final calibration bands are Easy 80–95%, Medium 60–75%, and Hard 40–55%; the opposed Tier-profile evaluation is complete. Automatic and impossible outcomes emerge from the ordinary Dice Size, Dice Pool, and Difficulty Vector framework.

Current remaining work is playtest validation, content-specific calibration, and the resource costs or limits granted by individual effects. Canonical references:

- [Resolution Engine](../03_core_baseline_system/01_resolution_engine.md)
- [Statistical Framework and Check Modes](../03_core_baseline_system/08_statistical_framework_and_check_modes.md)
- [Tier Difficulty Vector Reference](../03_core_baseline_system/13_tier_difficulty_vector_reference.md)

### OD-012 — Resource Mitigation Maneuvers

**Status:** Resolved by DEC-070 and DEC-072; later playtest validation may reopen the procedures.

**Soften Blow** and **Ward Self** establish the distinct defensive roles of Stamina and Essence. Their canonical procedure is owned by [Combat Maneuvers](../04_simulationist_subsystems/04_combat_maneuvers.md), alongside the other base combat maneuvers. Resource capacity, zero-resource states, and recovery are resolved by DEC-071.

Soften Blow and Ward Self each prevent one Damage Box per resource point, operate once per Attack before Vitality is marked, and leave one Damage Box from any damaging Attack. Ward Self currently mitigates damage only. Individual maneuvers and abilities declare their own other resource costs.

### OD-004A — Baseline Framework Glossary

**Status:** Resolved by DEC-056.

Canonical shared vocabulary is defined in [Baseline Framework Glossary](../03_core_baseline_system/00_baseline_framework_glossary.md). The glossary defines terminology without duplicating complete procedures.

### Pool-size-derived Floors

**Status:** Resolved by DEC-062.

Competency Rank determines baseline Dice Pool Size. Attribute determines Die Size. Final Dice Pool and comma-separated Difficulty Vectors determine probability. The implementation must use single-source ownership and references rather than duplicate procedures.

Implementation map: `07_archive/phase1_decision_reports/FLOOR_POOL_SIZE_DECISION_REPORT_COMPLETED.md`.

### OD-002 — Psychic/Psionic power

**Status:** Direction resolved; subsystem implementation open.

The current direction is a separate Essence-based supernatural system rather than a Vancian Magic Mastery Tradition. Its disciplines, augmentation, strain, and interaction with ordinary spellcasting remain to be designed.

**Relevant documents:**

- [Canonical Magic Architecture](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#2e-canonical-magic-architecture-dec-050)
- [DEC-050](../06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md#dec-050)

### OD-003 — Universal Mantle Axis

**Status:** Closed and removed from the canonical architecture.

Mantles are not a universal spell-record classification. Any future conceptual domains belong to a specific class, Tradition, feat, setting, or other subsystem rather than the universal spell framework.

### OD-004 — Craft specialty presentation and rank behavior

**Status:** Partially defined; implementation open.

Craft is a canonical Domain with a closed specialty list. Each Craft specialty is recorded as `Craft — X` and has its own separate Competency Rank. Craft Activity families, workshops, materials, projects, repair, and Outcome Rolls are resolved by DEC-091 and DEC-094.

Specific recipes, projects, item outputs, Difficulty Vectors, material quantities, and special Craft exceptions are content work.

**Relevant documents:**

- [Revised Domain-and-Activity Architecture](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#2a-revised-domain-and-activity-architecture-dec-049)
- [Craft and Production Domain](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#domain-viii-craft-and-production)
- [Crafting specialties](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#2c-vehicle-proficiencies)

### OD-005 — Lore specialty presentation and adjudication

**Status:** Partially defined; implementation open.

Lore is canonical as an open-ended focused familiarity skill. Each specialty is recorded as `Lore — X`, has its own Competency Rank, and is less broad than a Knowledge Skill; its scope is adjudicated by the GM. Content states its own Background, Ancestry, Class, and faction Lore grants.

Remaining: clarify practical Knowledge/Lore adjudication examples as content and Activity procedures are developed.

**Relevant documents:**

- [Lore and Cultural Familiarity](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#domain-v-lore-and-cultural-familiarity)
- [Knowledge and Lore distinction](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#2b-authoritative-domain-list)

### OD-006 — Vehicle proficiency taxonomy

**Status:** Partially defined; implementation open.

Vehicle operation is a family of proficiencies rather than one universal skill. Still to define:

- The final vehicle categories.
- Whether vehicle proficiencies are skills, Craft specialties, or equipment permissions.
- Which attributes and Domains govern each category.
- Crew assistance and command procedures.
- Vehicle combat and damage procedures.
- How magical, aerial, subterranean, and siege vehicles work.

**Relevant documents:**

- [Vehicle Proficiencies](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#2c-vehicle-proficiencies)

### OD-007 — Domain-level mechanics

**Status:** Resolved by DEC-089.

Domains are canonical categories that organize Skills and may be referenced by other mechanics, effects, and content. Domains do not provide a separate proficiency rank. Specific Class, Feat, Equipment, Activity, or Actor content states its own Domain reference when needed; there is no second universal Domain progression system.

**Relevant documents:**

- [Revised Domain-and-Activity Architecture](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#2a-revised-domain-and-activity-architecture-dec-049)
- [DEC-049](../06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md#dec-049)

### OD-008 — Activity and multi-skill procedure framework

**Status:** Baseline framework resolved by DEC-091; specific Activity content remains open.

Activities use one primary Skill check by default. Assistance, tools, support, stages, Requirements, Permissions, costs, success, and failure are defined by the Activity entry. Multiple Skills do not automatically stack or create stages.

Remaining: write the specific procedures, Difficulty Vectors, costs, outputs, and failure consequences for individual Activities.

**Relevant documents:**

- [Activity Examples](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#2d-activity-examples)
- [Skills and Generic Capabilities](../04_simulationist_subsystems/02_skills_and_generic_capabilities.md#revised-skill-architecture-cross-reference-dec-049)

---

### OD-013 — Combat, Damage, and Wound Procedures

**Status:** Framework established; procedures and calibration remain open.

Remaining work includes action-cost and repeated-attack fatigue procedures; Ready and other delayed-action procedures; detailed Shove forced-movement, Disarm, Rally, Intimidate, Taunt, and Assess procedures; fixed weapon Damage Box values; detailed shield interaction; Wound severity, treatment, recovery; and combat pacing/time-to-defeat calibration. Prone, Restrained, Immobilized, Grapple, and Escape are resolved by DEC-087. Triggered defenses, Reactions, passive resistances, and the combat sequence are resolved by DEC-075. Baseline Activity Tags, Wound Rolls, location Wound Conditions, and the baseline maneuver catalogue are resolved by DEC-073 and DEC-074.

**Canonical owners:**

- [Action Economy and Turn Structure](../03_core_baseline_system/04_action_economy_and_turn_structure.md)
- [Defenses, Damage, and Wounds](../04_simulationist_subsystems/01_defenses_and_damage_modeling.md)
- [Resources, Conditions, and Wounds](../04_simulationist_subsystems/03_resources_conditions_and_wounds.md)
- [Combat Maneuvers](../04_simulationist_subsystems/04_combat_maneuvers.md)

### OD-014 — Equipment and Economic Framework

**Status:** Body-slot structure resolved by DEC-071; broader framework open.

Items have maximum Durability points; each Magical Effect adds 1 maximum Durability; items above 0 are Damaged but functional; at 0 they are Broken and nonfunctional. Simple Repair is automatic with correct tools and recipe-gated Rank, restoring 1 Durability per minute. Broken Repair uses the relevant Craft specialty, recipe-stated materials, and a Craft check. Tag / Trait taxonomy and Piercing are resolved by DEC-086. Remaining work includes weapon categories and fixed Damage Box values, detailed armor and shield category Traits, masterwork and special materials, magical-item scaling, crafting interfaces, and wealth/equipment-access expectations. General Durability expenditure, replacement, Sunder, armor sacrifice, and magical-item strain are deferred.

**Canonical owner:** [Equipment, Durability, and Economy](../03_core_baseline_system/12_equipment_durability_and_economy.md).

### OD-015 — Universal Class-Table Standards

**Status:** Partially resolved by DEC-092 and DEC-095.

Universal Class-table columns and the manual Skill Investment framework are established. Every Class has a Class Skills list; Investments received while advancing that Class use its list unless an explicit rule creates another access route. A Class may grant additional Skill Investments in its own level-by-level table.

Remaining: define the remaining relationship between class features, Feats, Domains, Attributes, Equipment, and resources in representative framework-only Class tables; then test multiclass presentation and conversion use.

**Canonical owner:** [Leveling and Tier Progression](../03_core_baseline_system/06_leveling_and_tier_progression.md).

### OD-016 — Conversion-Document Audit and Validation

**Status:** Open.

Audit conversion documents for stale terminology and mechanics, then validate the framework through representative D&D 3.5e conversion and later comparative conversions.

**Canonical owner:** `../05_conversion_and_content_engine/`.

### OD-017 — Simplified Actor Framework

**Status:** Deferred; no active canonical subsystem owner.

Rabble, Underling, and similar simplified-actor procedures are not part of the active defense, damage, or resource documents. If resumed, they require a dedicated canonical file. The Phase 1 Checklist still contains the historical completed encounter-category item and requires a future checklist/status cleanup decision.

---

## 2. Provisional Content Definitions

### OD-009 — Canonical Magic Mastery Tradition catalogue and Divine-Domain mapping

**Status:** Resolved by DEC-098.

The 28 individual Magic Mastery Tradition Skills and the Divine-Domain-to-Tradition access reference are canonical. Cleric grants Divine access; each Divine Domain grants one specified additional Tradition plus a Domain Tradition Grant, and may grant further explicit Features. The final individual Domain catalogue, deity portfolios, Domain Features, Domain-granted Ranks, spell entries, and Class tables remain content work.

**Magic Mastery Investment cadence (DEC-097, revised by DEC-100):** A spellcasting Class or Prestige Class table decides whether and when it grants extra Investments restricted to Domain VII: Magic Mastery. The normal caster-class design benchmark is one such Investment at a Spell Slot Advancement level, not a mandatory universal cadence.

**Canonical documents:**

- [Magic Schools, Traditions, and Spellcasting](../03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md)
- [Divine Domains and Tradition Access](../03_core_baseline_system/14_divine_domains_and_tradition_access.md)

### OD-010 — Spell record and tag vocabulary

**Status:** Framework accepted; final vocabulary open.

The multi-axis record is established as:

```text
School
Traditions
Traits
```

Still to define:

- Complete spell Trait list.
- Whether Delivery is a separate axis or a Trait family.
- Spell resistance, defense targeting, range, duration, and action tags.
- Tradition-specific versions of the same spell.

**Relevant document:**

- [Canonical Multi-Axis Spell Record](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#canonical-multi-axis-spell-record)

### OD-011 — Spell conversion catalogue

**Status:** Open content task.

The roadmap calls for conversion of at least fifteen classic spells and eventually a larger spellbook. Need to define:

- Spell levels and Tier equivalents.
- Vancian slot requirements.
- Tradition tags for each spell.
- School classification for legacy spells.
- Defense targets and conditions.
- Multi-tradition versions.
- Ritual versus combat casting.

**Relevant documents:**

- [D&D 3.5e conversion procedure](../05_conversion_and_content_engine/01_dnd_3_5e_conversion_procedure.md)
- [Spellbook translation roadmap](../06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md#3-immediate-next-steps--iteration-roadmap)

---

## 3. Definitions Already Decided but Still Described as Options

These are not open design questions. They are documentation-cleanup items.

### DC-001 — Check-pool architecture

**Decision:** Model A, Pure Role Separation, is locked by DEC-038.

**Stale references:**

- [Check-pool architecture comparative matrix](../02_comparative_system_analysis/archived_core_reference/11_check_pool_architecture_comparative_matrix_REFERENCE.md#3-executive-decision-guide-which-architecture-best-fits-our-vision)
- [Check-pool generation and class differentiation](../03_core_baseline_system/07_check_pool_generation_and_class_differentiation.md#1-the-core-architectural-dilemma-separating-ceiling-vs-reliability)

These documents should be relabeled as historical comparison or updated to identify Model A as canonical.

### DC-002 — Attacks and spells as skills with class-granted advancement

**Decision:** Option 3, Hybrid Class-Granted Domain Allocations, is locked by DEC-041.

**Stale references:**

- [Attacks and spells architecture](../02_comparative_system_analysis/archived_core_reference/12_attacks_and_spells_vs_skills_architecture_REFERENCE.md)

The document still presents Options 1–3 at length. Those sections should be retained as design history but clearly marked non-canonical.

### DC-003 — Skill architecture and the historical 65-skill matrix

**Decision:** DEC-049 is canonical. The 65-skill matrix is archived.

**Status:** The file has already been moved to the archive. Remaining references should point to the archived path and describe it as historical.

### DC-004 — Old five-domain skill taxonomy

**Decision:** The eight-domain architecture in DEC-049 is canonical.

**Stale reference:**

- [Historical five-umbrella matrix](../03_core_baseline_system/09_domains_skills_activities_and_crafting.md#2-historical-skill-taxonomy-superseded-5-umbrella-matrix)

This section is correctly retained for provenance but should remain explicitly marked historical.

### DC-006 — Deprecated Permission terminology

**Decision:** DEC-102 deprecates general `Permission` and `Disrupt Permission` terminology. New / rewritten material uses Access, Requirement, Effect, Exception, Restriction, and Disruption according to the glossary.

**Status:** Documentation cleanup during the approved framework rewrite. Legacy canonical wording remains readable but must not be perpetuated into the new structure.

**Canonical vocabulary:** [Baseline Framework Glossary](../03_core_baseline_system/00_baseline_framework_glossary.md).

### DC-005 — Old resolution terminology and mechanics

**Status:** Review required.

Some older documents still contain superseded language such as `[SET]`, “Soak,” or older Called Shot thresholds. These are not necessarily open questions; they are consistency errors requiring a canonical-rules audit.

**Relevant documents:**

- [Master top-to-bottom summary](../03_core_baseline_system/11_master_top_to_bottom_system_summary.md)
- [Resolution engine](../03_core_baseline_system/01_resolution_engine.md)
- [Defenses and damage modeling](../04_simulationist_subsystems/01_defenses_and_damage_modeling.md)

---

## 4. Historical Calibration Questions

The following questions appear in comparative and simulation documents. They were used to establish the current baseline and should not automatically be treated as open architecture unless a future playtest reopens them.

- Competency success curves and target probabilities.
- Critical frequency.
- Time to defeat and combat pacing.
- Offensive versus defensive scaling.
- Stamina depletion under repeated active defense.
- Resource reset cadence.
- Opposed-roll tie frequency.

**Relevant document:**

- [Mathematical calibration and TTK vectors](../02_comparative_system_analysis/04_mathematical_calibration_and_ttk_vectors.md)

These are calibration targets, not unresolved taxonomy decisions.

---

## 5. Recommended Resolution Order

1. Complete the Magic Mastery and Vancian spellcasting engine.
2. Resolve Psychic/Psionic power as a separate subsystem or tradition.
3. Define the character-sheet presentation for Domains, Skills, Specialties, Lore, and Knowledge.
4. Define domain-level mechanics and class/path interactions.
5. Define activity procedures and assistance rules.
6. Finalize Craft, Lore, Vehicle, and Magic specialties.
7. Build the universal Spell Trait compendium.
8. Perform a canonical-document consistency audit and relabel historical option sections.

### Tier-Aligned Competency Ranks

**Status:** Resolved by DEC-063.

Competency Ranks align with High Fantasy Tier nomenclature: Untrained, Trained, Veteran, Master, Hero, and Legend. Baseline pool size is 1dX through 6dX, and final pool size determines Floor subject to the final die-size cap.

### Consolidated Probability Reference Tables

**Status:** Framework research complete by DEC-067.

Generic pool-volume, die-size, Difficulty Vector, opposed, Automatic Success, and provisional progression artifacts are available. Final probability targets and content-specific calibration remain open.

### Official Tier Difficulty Vector Suggestions

**Status:** Resolved by DEC-068.

The condensed per-pool, per-band Difficulty Vector suggestions are canonicalized in `03_core_baseline_system/13_tier_difficulty_vector_reference.md`. The exhaustive vector search remains research support.

### Probability Band Scope and Calibration Boundaries

**Status:** Resolved by DEC-069; opposed Tier-profile evaluation is complete.

Final design-calibration bands are Easy 80–95%, Medium 60–75%, and Hard 40–55%. Automatic/Impossible outcomes emerge naturally from the Dice Size, Dice Pool, and Difficulty Vector framework. No separate Extreme-vector convention is required. Equipment validation is deferred to the Equipment/content phase, and playtest validation is deferred until framework consolidation and MVP content creation.
