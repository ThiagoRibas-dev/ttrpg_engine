# Leveling and Tier Progression

**Status:** Canonical Level 1–20 advancement framework.  
**Scope:** Character Level, High Fantasy Tiers, advancement milestones, Spell Slot Advancement references, and progression ownership. This document does not finalize individual Classes, Feats, Ancestries, spells, equipment, or Mythic content.

## 1. High Fantasy Tiers

The mortal game covers 20 Character Levels divided into five four-level Tiers:

| Tier | Levels | Intended scope |
|---|---:|---|
| Trained | 1–4 | Local |
| Veteran | 5–8 | Regional |
| Master | 9–12 | Country |
| Hero | 13–16 | World |
| Legend | 17–20 | Cosmic |
| Mythic | 21+ | Divine |

The Tier describes the character’s overall scope. It does not replace Character Level, Competency Rank, Spell Slot Progression Level, or any other progression vector.

## 2. Level Advancement

Every Character Level may provide some combination of:

- Class or Prestige Class table benefits.
- Attribute advancement or Secondary Attribute Step Points.
- Skill or Tradition investment.
- Feats.
- Resource capacity or recovery benefits.
- Spell Slot Advancements.
- Tier milestone permissions.

The exact benefits belong to the relevant Class, Prestige Class, Attribute, Skill, Resource, Magic, or Feat document. This file defines the shared cadence and ownership structure rather than individual content.

## 3. Attributes

Starting Attribute Dice, Primary Attribute advancement, Secondary Attribute Score Increases, Attribute Point costs, Attribute Step Investments, and permanent Attribute limits belong to `02_attributes_and_derived_statistics.md`.

This file does not duplicate Attribute procedures or formulas.

## 4. Competency, Skill, and Defense Advancement

Competency Ranks are independent from Character Level, but Class and Prestige Class tables may grant a protected **Good**, **Medium**, or **Bad** progression to a relevant Skill, including a Tradition Skill, or paired defense. The following reference cadence establishes the class-track milestones:

| Character Level | Good | Medium | Bad |
|---:|---|---|---|
| 1–4 | Trained | Untrained | Untrained |
| 5–8 | Veteran | Trained | Untrained |
| 9–12 | Master | Veteran | Trained |
| 13–16 | Hero | Master | Veteran |
| 17–20 | Legend | Hero | Master |

A track retains its preceding Rank between milestones. Before a track’s first listed milestone, it uses Untrained Rank.

The canonical Rank-to-pool mapping belongs to `07_check_pool_generation_and_class_differentiation.md`:

```text
Untrained 1dX
Trained   2dX
Veteran   3dX
Master    4dX
Hero      5dX
Legend    6dX
```

For a paired defense, use the highest of its two paired Attribute Dice as the die size and apply the Class defense track’s Rank as its baseline Dice Pool. Thus, a Good Reflexes progression at Level 1 uses a 2dX final defense pool, while a Bad Reflexes progression uses the 1dX Untrained baseline.

### Manual Skill Investments

Every Character receives Skill Investments on the following Character-Level schedule:

| Character Level | Skill Investments received |
|---:|---:|
| 1 | 6 |
| 2–20 | 1 at each Level |

A character therefore receives **25 baseline Skill Investments** by Character Level 20. Each Skill Investment raises one chosen Skill by one Competency Rank. A Skill cannot be raised above the maximum Rank available at the character’s current Character Level:

| Character Level | Maximum Competency Rank |
|---:|---|
| 1–4 | Trained |
| 5–8 | Veteran |
| 9–12 | Master |
| 13–16 | Hero |
| 17–20 | Legend |

Skill Investments are chosen when received and are not banked unless an explicit rule permits banking. An Investment may only be spent on a Skill from the **Class Skills** list of the Class or Prestige Class advanced at that Character Level, unless an explicit rule grants another access route or exception. Each Investment raises only one Rank; multiple Investments received at the same Level may be spent on the same eligible Skill only if each Rank increase is legal under the current maximum Rank.

This schedule guarantees one manual Skill-advancement choice at every Character Level. Its ordinary baseline permits a focused character to reach up to four Legend Skills by Level 20, alongside additional breadth or lower-Rank specialization.

Class and Prestige Class tables may grant additional Skill Investments at stated class levels. Such an Investment is part of that Class Level’s self-contained grant and follows that Class or Prestige Class’s Skill list unless its rule states otherwise. A spellcasting Class or Prestige Class may instead state that an additional Investment is restricted to eligible Skills in Domain VII: Magic Mastery. There is no universal spellcaster extra-Investment cadence: every Class table states its own grants. The normal caster-class design benchmark is **one** Magic Mastery-only Investment at a Class Level granting Spell Slot Advancement, but a Class table may intentionally use a different quantity or cadence.

Class and Prestige Class tables determine which specific Skills, Traditions, and defenses receive protected progression. Protected progression, Class features, Feats, Permissions, and explicit content grants may provide additional investment or exceptions.

## 5. Resource Track Advancement

Every Base Class and Prestige Class assigns an independent **Good**, **Mediocre**, **Bad**, or **None** progression to Vitality, Stamina, and Essence. The three assignments are independent; a class may be Good in more than one resource or in none of them.

| Class Level | Good | Mediocre | Bad | Cumulative Good | Cumulative Mediocre | Cumulative Bad |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | +1 | +0 | +0 | 1 | 0 | 0 |
| 2 | +1 | +1 | +1 | 2 | 1 | 1 |
| 3 | +1 | +1 | +0 | 3 | 2 | 1 |
| 4 | +1 | +1 | +1 | 4 | 3 | 2 |
| 5 | +1 | +0 | +0 | 5 | 3 | 2 |
| 6 | +1 | +1 | +1 | 6 | 4 | 3 |
| 7 | +1 | +1 | +0 | 7 | 5 | 3 |
| 8 | +1 | +1 | +1 | 8 | 6 | 4 |
| 9 | +1 | +0 | +0 | 9 | 6 | 4 |
| 10 | +1 | +1 | +1 | 10 | 7 | 5 |
| 11 | +1 | +1 | +0 | 11 | 8 | 5 |
| 12 | +1 | +1 | +1 | 12 | 9 | 6 |
| 13 | +1 | +0 | +0 | 13 | 9 | 6 |
| 14 | +1 | +1 | +1 | 14 | 10 | 7 |
| 15 | +1 | +1 | +0 | 15 | 11 | 7 |
| 16 | +1 | +1 | +1 | 16 | 12 | 8 |
| 17 | +1 | +0 | +0 | 17 | 12 | 8 |
| 18 | +1 | +1 | +1 | 18 | 13 | 9 |
| 19 | +1 | +1 | +0 | 19 | 14 | 9 |
| 20 | +1 | +1 | +1 | 20 | 15 | 10 |

**Cadence:** Good advances every class level. Mediocre advances at Levels 2–4 of each four-level cycle. Bad advances at each even class level. None grants no class contribution.

### Multiclass Resource Advancement

Each completed class or Prestige Class level contributes the value shown by that class’s assigned track at its actual class level. Add contributions from every class and Prestige Class to determine the accumulated class contribution for each resource. Do not recalculate an Attribute Base when multiclassing.

### Capacity Limits and Permanent Sources

There is no universal numerical maximum beyond the bounded Attribute Base, accumulated class tracks, and explicit permanent additions. Before exceptional content, the ordinary Level 20 natural ceiling is an Attribute Base of 10 plus a Good contribution of 20, for a capacity of 30.

- Ancestry may grant +0 to +2 permanent capacity to a fitting resource when justified by biology or origin; it does not normally scale by level.
- A Feat, Class feature, or other explicit rule may grant permanent capacity, a recovery improvement, or a resource-use Permission.
- Equipment ordinarily grants protection, Permissions, temporary reserves, or restoration rather than permanent personal capacity.

## 6. Spell Slot Advancement

Every Base Class and Prestige Class includes a level-by-level **Spell Slot Advancement** column.

A marked class level grants one Spell Slot Advancement. The character’s total completed advancements across all classes and Prestige Classes determine their **Spell Slot Progression Level**.

```text
Spell Slot Advancement:
  A class-table entry granting one advancement.

Spell Slot Progression Level:
  The accumulated position on the Reference Good Slot Progression.
```

The Reference Good Slot Progression is the universal shared daily Spell Slot table. Derived full, every-other-level, and every-four-level views are generated from that reference table; they are not separate player-facing slot systems.

The canonical spellcasting framework belongs to:

```text
10_magic_schools_traditions_and_spellcasting.md
```

## 7. Classes and Prestige Classes

Classes and Prestige Classes use level-by-level tables. Prestige Classes use the same advancement and multiclassing procedures as Base Classes but have entry requirements.

### Class Document Standard

Every Class or Prestige Class document uses this structure:

```text
Class Name
Class Description
Class Requirements (optional)
Class Skills
Level-by-Level Class Table
Description of Individual Abilities
```

### Level-by-Level Class Table

Every Class table uses the following columns. Optional columns may be omitted only when the Class does not use that progression.

| Level | Vitality | Stamina | Essence | Fortitude | Reflexes | Willpower | Spell Slot (optional) | Other Specific Progression (optional) | Special |
|---:|---|---|---|---|---|---|---|---|---|

Each Class Level is a self-contained investment: its row states exactly what that Class Level grants.

```text
Vitality / Stamina / Essence:
  State the actual resource contribution granted by that Class Level.

Fortitude / Reflexes / Willpower:
  State the actual paired-defense Rank advancement granted by that Class Level.

Spell Slot:
  State the Spell Slot Advancement granted by that Class Level.

Other Specific Progression:
  State an additional progression unique to that Class,
  including an additional Skill Investment when applicable.

Special:
  State Class Features, choices, Feats, Permissions,
  Tradition access, or other individual grants.

Class Skills:
  State the Skills eligible for Skill Investments received while
  advancing that Class, unless an explicit rule creates an exception.
```

Good, Medium, and Bad progression tracks are design-reference and calibration tools. They are not player-facing table labels. A Class table records the resulting individual level-by-level grants rather than naming a track.

Universal Character Level benefits—such as Attribute Score Increases, General Feats, Ancestry benefits, and other cross-Class milestones—belong to their own Character Level procedures and are not repeated in every Class table unless a specific Class explicitly modifies them.

## 8. Universal Actor Application

The Level and Tier framework applies conceptually to PCs, NPCs, monsters, bosses, and Underlings. Presentation may be simplified for Rabble and Underlings, but the Universal Actor Schema remains the structural reference.

## 9. Mythic Scope Boundary

Mythic begins beyond Level 20. The current framework establishes only that Mythic may provide:

- Epic Traditions.
- Epic Spells.
- Divine-scale Requirements and Permissions.
- Broader fictional scope.
- Exceptional effects using the bounded framework.

Mythic slot expansion, Mythic Attributes, Mythic classes, Mythic monsters, and Mythic resolution exceptions remain deferred. They are not part of the Level 1–20 framework consolidation.

## 10. Source Links

- Vocabulary: `00_baseline_framework_glossary.md`
- Attributes: `02_attributes_and_derived_statistics.md`
- Actor structure: `03_character_schema_and_actor_creation.md`
- Resolution: `01_resolution_engine.md`
- Pool/statistical model: `07_check_pool_generation_and_class_differentiation.md`, `08_statistical_framework_and_check_modes.md`
- Skills and Domains: `09_domains_skills_activities_and_crafting.md`
- Magic and Spell Slots: `10_magic_schools_traditions_and_spellcasting.md`
- Equipment framework: `12_equipment_durability_and_economy.md`
- Conversion reference: `../02_comparative_system_analysis/archived_core_reference/09_dnd_3_5e_class_advancement_tracks_mapping_REFERENCE.md`
