# Baseline Framework Glossary

**Status:** Canonical framework vocabulary  
**Decision:** DEC-056

This document defines shared terms used across the baseline framework. It does not replace the procedural rules in the relevant subsystem documents.

## Resolution Vocabulary

### Natural Dice Pool

The check pool produced by the actor's ordinary Attribute, Competency, Class, and other persistent factors before temporary or special enhancements are applied.

### Enhanced Dice Pool

A Natural Dice Pool modified by temporary or special sources such as feats, spells, equipment, circumstances, class features, or other explicit effects.

### Die Step-Up

An increase in die size along the ordinary ladder:

```text
d4 → d6 → d8 → d10 → d12
```

### Die Step-Down

A decrease in die size along the ordinary ladder:

```text
d12 → d10 → d8 → d6 → d4
```

The canonical term is Die Step-Up; its inverse is Die Step-Down. The ordinary ladder ends at d12. Exert is the explicit temporary exception that may Step-Up an affected d12 die to d20.

### Boon

A final-pool effect that adds one die of the same size after ordinary pool construction and after applicable Die Step-Ups and Die Step-Downs. Boons use typed stacking rules. Boons from the same named source do not stack with one another.

Boon/Bane types are **Circumstance**, **Enhancement**, **Morale**, **Competence**, and **Untyped**. Effects of the same type do not stack; use only the strongest applicable effect of that type. Effects of different types stack normally. An Untyped effect may stack with typed effects and other Untyped effects unless its source says otherwise.

- **Circumstance:** The immediate situation, environment, positioning, timing, visibility, terrain, or physical conditions surrounding the check.
- **Enhancement:** A direct improvement or degradation of the performance, quality, force, precision, resilience, or output of an actor, object, weapon, armor, or spell.
- **Morale:** Emotional force, confidence, fear, inspiration, social pressure, hope, despair, or group cohesion affecting performance.
- **Competence:** Temporary assistance from training, instruction, advice, preparation, specialized knowledge, coordinated technique, or focused performance.
- **Untyped:** An exceptional effect deliberately excluded from the ordinary categories and permitted to stack with typed effects.

### Bane

A final-pool effect that removes one die after ordinary pool construction and after applicable Die Step-Ups and Die Step-Downs. Banes use the same Circumstance, Enhancement, Morale, Competence, and Untyped categories and stacking rules as Boons. Banes from the same named source do not stack with one another.

If a Bane is applied to a one-die pool, it causes one Die Step-Down instead. Further Banes do not cause additional Die Step-Downs. If a `d4` would be stepped down by this rule, the check is an automatic failure.

### Automatic Success

A success granted directly by an effect rather than produced by a die. An Automatic Success counts toward the required-success total but is not a die and is not affected by Boons, Banes, Die Step-Ups, Die Step-Downs, or opposed-roll tiebreaking.

### Soften Blow

A Stamina-spending maneuver that lowers damage from a source targeting Reflexes, Parry, or Damage Absorption. Its procedure is owned by `../04_simulationist_subsystems/04_combat_maneuvers.md`.

### Ward Self

An Essence-spending maneuver that lowers damage from an effect targeting Fortitude or Willpower. Its procedure is owned by `../04_simulationist_subsystems/04_combat_maneuvers.md`.

### Resource Value

The fixed value assigned to an Attribute Die for resource-capacity derivation. The table and resource formulas are owned by `02_attributes_and_derived_statistics.md`.

### Incapacitated

A zero-Vitality state in which a creature cannot take ordinary Actions or Reactions. Its Wound and death procedure is owned by `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md`.

### Winded

A zero-Stamina state. A Winded creature cannot spend Stamina until it recovers Stamina.

### Drained

A zero-Essence state. A Drained creature cannot spend Essence until it recovers Essence.

### Execution

A tactical maneuver that kills an Incapacitated target on success. Its procedure is owned by `../04_simulationist_subsystems/04_combat_maneuvers.md`.

### Trait

A persistent descriptor of an object, creature, Spell, weapon, armor, shield, item, or other game entity. A Trait states an inherent characteristic or capability. Weapon Traits, Spell Traits, Item Traits, and Creature Traits are applications of this shared category.

### Tag

An operational label carried by an Activity, Attack, effect, Condition, or event. A rule uses Tags as interaction anchors: it states which Tags it affects, grants, removes, suppresses, or requires. A Tag has no automatic effect unless another rule refers to it.

Tag families include Activity Tags, Attack Tags, Effect Tags, Damage Tags, and Condition Tags.

### Activity Tag

A Tag carried by an Activity. Baseline Activity Tags are owned by `09_domains_skills_activities_and_crafting.md`.

### Piercing

**Piercing** is a Weapon or other persistent attack-source Trait. A Strike or other Attack made with a Piercing source gains the Piercing Attack Tag. A successful damaging Attack with the Piercing Attack Tag deals at least 1 Damage Box after Damage Absorption.

Class Features, Feats, Spells, Abilities, item enhancements, and other explicit effects may grant the Piercing Attack Tag conditionally or add the Piercing Trait to an eligible source.

### Wound Roll

A roll of the Anatomical Wound Die, made when a Natural Critical or another effect requires it. Its procedure and results are owned by `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md`.

### Reaction

An out-of-turn response. Each actor normally has one Reaction per Turn. Interpose, Attack of Opportunity, Counterspell, and similar special interventions require a Reaction when their specific rules say so.

### Triggered Defense

A defense used in response to an eligible Attack that costs its stated resource but does not use a Reaction. Deflect and Evasion are triggered defenses.

### Passive Resistance

A defense roll that does not require a Reaction or resource expenditure to make. Fortitude and Willpower are passive resistances.

### Round

Approximately six seconds of simultaneous combat time, containing one normal Turn for each participating Actor. The procedure is owned by `04_action_economy_and_turn_structure.md`.

### Turn

An Actor’s opportunity to act within a Round. At the start of its Turn, an Actor regains three Actions and one Reaction.

### Initiative

The procedure establishing Turn order. The game supports fixed-order and round-by-round Reflex Initiative, plus fixed-choice and round-by-round Fast-Slow Side Initiative. Its procedures are owned by `04_action_economy_and_turn_structure.md`.

### Fast Turn

A two-Action Turn in Fast-Slow Side Initiative.

### Slow Turn

A three-Action Turn in Fast-Slow Side Initiative.

### Delay

In Reflex Initiative — Fixed Order, a choice to move later in the initiative queue for the current Round. It never moves an Actor earlier that Round.

### Disruption

An explicit effect that can interrupt an Activity with one or more stated Tags. Ordinary damage does not itself cause Disruption. The effect states the Tags it can interrupt and any other limits.

`Disrupt Permission` is deprecated terminology retained only in older documents pending the framework rewrite.

### Requirement

A condition that must be satisfied before an action, spell, ability, or effect can be used.

Examples:

```text
Requires Veteran Death Tradition.
Requires a visible target.
Requires a weapon with the Reach Trait.
```

### Access

An explicit rule allowing an actor to select, learn, prepare, wield, use, or otherwise engage with a stated category of content or capability.

Examples:

```text
War Domain grants access to the War Tradition.
A Class grants access to its Class Skills.
A weapon Feature grants access to Heavy Blades.
```

### Exception

A specific rule that changes or overrides an ordinary baseline procedure in a stated circumstance. An Exception must state exactly what it changes.

Examples:

```text
You can use Deflect against stated ranged physical Attacks.
You can cast this Spell as a Reaction.
This effect can affect a target normally immune to it.
```

### Rule Hierarchy

When two rules conflict, the most specific applicable rule supersedes the more general rule within its stated scope. The general rule remains in effect outside that scope.

```text
General rule:
  Deflect applies to eligible physical Attacks.

Specific Exception:
  This Feat allows you to use Deflect against stated ranged physical Attacks
  while wielding a shield.

Result:
  The Feat changes Deflect eligibility only for its stated user, equipment,
  and Attack scope. It does not redefine Deflect for every Actor.
```

A rule must state its own Traits, Requirements, Trigger, Cost, Effect, Restriction, or Exception precisely enough to establish its scope. Do not infer an Exception from flavor text or an unstated interaction.

### General Rule

A baseline procedure applying whenever no more specific applicable rule changes it.

### Specific Rule

A rule with a narrower stated scope than a relevant General Rule. A Specific Rule may state an Exception, Restriction, or other Effect that supersedes the General Rule within that scope.

### Restriction

A specific rule that prohibits or limits an ordinary action, effect, or capability in a stated circumstance.

Examples:

```text
You cannot use Movement Activities while Immobilized.
You cannot spend Stamina while Fatigued.
This Spell cannot affect undead creatures.
```

### Target Number

The face value a die must meet or exceed to produce one success.

### Difficulty Class

A bounded Target Number assigned to a task, defense, effect, or obstacle. Ordinary Difficulty Classes normally range from 2 to 12. The current working names are:

```text
DC 2 — Trivial
DC 3 — Routine
DC 5 — Challenging
DC 7 — Formidable
DC 9 — Heroic
DC 11 — Legendary
DC 12 — Extreme
```

These names are established as working categories; their exact numerical calibration remains subject to future probability and playtest work.

### Difficulty Vector

A comma-separated ordered set of Target Numbers such as `DC 5`, `DC 5,4`, or `DC 6,5,3`. Roll the final Dice Pool, sort dice and thresholds from highest to lowest, and compare them positionally. The check succeeds when every threshold in the vector is met.

### Defender Wins Ties

The default opposed-contest rule. After comparing the highest faces and all applicable secondary dice, the defender wins if the results remain tied.

The party that initiates an opposed contest is the **attacker** for that contest; the responding party is the **defender**. Some contests, such as races, may explicitly allow a neutral tie instead of requiring a victor.

## Spellcasting Vocabulary

### Spell School

The technical classification of what a spell does. The baseline system preserves the eight traditional D&D-compatible Schools:

- Abjuration
- Conjuration
- Divination
- Enchantment
- Evocation
- Illusion
- Necromancy
- Transmutation

### Spell Tradition

A magical field governing access to and specialization in a spell. A spell may belong to multiple Traditions. Classes and Prestige Classes grant access to Tradition Skills; Traditions have fixed shared spell lists.

### Spell Trait

A practical descriptor governing a spell's delivery, interaction, targeting, or special behavior.

### Spell Slot Advancement

An entry on a Base Class or Prestige Class table granting one advancement toward the character's shared Spell Slot Progression.

### Spell Slot Progression Level

The character's accumulated position on the Reference Good Slot Progression.

### Reference Good Slot Progression

The universal table showing the shared daily Spell Slot pool at Spell Slot Progression Levels 1–20.

## Deprecation Note — Rewrite Target

The general framework noun **Permission** is deprecated. It is not to be introduced in new rules text or design documents. During the framework rewrite, replace each legacy use according to its actual job:

| Legacy use | Rewrite term / wording |
|---|---|
| Allows selection or use of a category | **Access** |
| Must be true before use | **Requirement** |
| Changes the normal baseline in a stated case | **Exception** or direct “you can / cannot” wording |
| Prohibits or limits ordinary use | **Restriction** |
| States what a rule does | **Effect** |
| Interrupts a tagged Activity | **Disruption** |

Existing canonical documents still use `Permission` and `Disrupt Permission`. They remain readable as legacy wording until the approved repository rewrite; this glossary records the required replacement vocabulary so that the new framework does not perpetuate the term.

## Governance Note

This glossary defines vocabulary only. Complete procedures belong in the relevant canonical subsystem documents, especially:

- `01_resolution_engine.md`
- `02_character_schema_and_stats.md`
- `09_domains_skills_activities_and_crafting.md`
