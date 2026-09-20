# Cortex, One Roll Engine, Silhouette, and Ironclaw — Comparative Review

**Status:** Research / comparison artifact; non-canonical.  
**Purpose:** Evaluate Cortex Prime, the One Roll Engine, Dream Pod 9’s Silhouette system, and Ironclaw for useful inspiration, confirmation, and rejected approaches. This document does not change the current resolution engine, resources, Skill progression, or feature-conversion policy.

## 1. Executive Summary

| System | Strongest lesson for this project | Primary caution |
|---|---|---|
| Cortex Prime | Modular trait / feature packages can make a generic engine support very different Classes and settings. | Its meta-currency, add-two arithmetic, broad pool construction, and persistent asset / complication dice conflict with current priorities. |
| One Roll Engine | One roll can encode several combat facts at once; Actions can be resolved with a rich result instead of a chain of rolls. | Width / Height interpretation, match scanning, and hit-location coupling add cognitive burden beyond the current single-highest-die procedure. |
| Dream Pod 9 Silhouette | A Skill-ranked same-die pool read by highest die is a clean, fast, simulationist core; wound consequences can replace a large abstract health buffer. | Exploding 6s, margin arithmetic, and all-ones critical mishaps are not needed for the current bounded framework. |
| Ironclaw | Mixed die pools read by highest face validate discrete die-step advancement, equipment / career identity, and routine procedures. | Adding every applicable Trait to a pool and counting multiple successes risks pool bloat, subjective relevance arguments, and extra interpretation. |

The closest mechanical relatives to the current core are **Silhouette** and **Ironclaw**. The current framework is deliberately simpler at the table because it:

```text
Uses one Attribute die size rather than mixed die sizes.
Uses Competency Rank as baseline pool volume.
Uses explicit Boons and Banes rather than free-form Trait accumulation.
Uses Difficulty Vectors and explicit procedures rather than margin arithmetic.
Keeps resources in-world; no Plot Point / Willpower narrative currency.
```

## 2. System Snapshots

### Cortex Prime

**Core observed pattern**

- Characters use modular trait sets such as Attributes, Skills, Distinctions, Powers, Relationships, or Values.
- A player builds a pool from relevant traits, rolls varied step dice, keeps two results, and adds them.
- Assets and Complications can become temporary rated traits.
- Plot Points are earned and spent to influence pools, effects, and narrative outcomes.

**Useful reference ideas**

| Cortex idea | Potential use here | Boundary |
|---|---|---|
| Trait sets / modular packages | A Class, Domain, Feat, item, or Ancestry can be a self-contained package of Skills, Permissions, Features, and resource procedures. | We already use explicit ownership rather than letting every package freely add a die. |
| SFX plus Limit | Every powerful Feature can state a concrete benefit, cost, Requirement, and limit together. | Use Actions, Essence, Stamina, Slots, Conditions, Tags, and Durability—not Plot Points. |
| Assets / Complications as named fiction | A clear named state can make temporary fiction visible. | Prefer existing Conditions, Tags, Traits, and short explicit durations; avoid a growing list of persistent conditional die traits. |
| Toolkit presentation | A core framework can support different content packages. | Do not adopt unrestricted subsystem mixing that weakens single-source ownership. |

**Do not import**

```text
Keep-two-and-add arithmetic.
Plot Points or other narrative meta-currency.
Hitches as a universal complication trigger.
Free-form adding of every relevant trait die.
Persistent asset / complication die stacks as the default state model.
```

### One Roll Engine (ORE)

**Core observed pattern**

- Roll a pool of d10s, normally built from Stat + Skill.
- A matching set succeeds.
- **Width** is the number of matching dice; **Height** is their face value.
- In many implementations, Width determines speed and damage while Height determines quality and, in combat, hit location.
- Hard Dice and Wiggle Dice create assured or chosen results in some games.

**Useful reference ideas**

| ORE idea | Potential use here | Boundary |
|---|---|---|
| One roll resolves several combat facts | Continue seeking procedures where an opposed check plus fixed Damage Boxes and explicit Conditions resolve a full exchange without follow-up damage rolls. | Do not bind universal hit location, initiative, and damage to one result axis. |
| Player chooses between result qualities | Content can offer a clear trade-off such as Power Attack’s Banes for Damage Boxes, rather than a raw bonus. | Keep each trade-off written in its own Feature; no universal Width / Height subsystem. |
| Hard / Wiggle Dice | Confirms the value of explicit automatic or controlled exceptional outcomes. | Current equivalents are explicit Permissions, Automatic Successes, or feature-defined outcomes—not special die species. |
| Simultaneous declaration | A useful reference for future Ready / delayed-action and side-initiative testing. | Current initiative modes remain canonical. |

**Do not import**

```text
Match-scanning as the universal resolution test.
Two-axis Width / Height interpretation on every roll.
Universal hit-location-by-face procedure.
Hard / Wiggle dice as an extra character-building currency.
```

### Dream Pod 9 Silhouette

**Core observed pattern**

- Skills determine the number of normally d6 dice rolled.
- The highest die is read against a threshold or opposed highest die.
- Additional 6s can increase the result above 6.
- A roll of all 1s is a critical mishap.
- Margin of Success / Failure affects outcome; combat uses wounds and can be lethal.

**Useful reference ideas**

| Silhouette idea | Potential use here | Boundary |
|---|---|---|
| Same-size Skill pool, highest die read | Strong independent confirmation for the current pool-volume / highest-result resolution structure. | Current Attribute Dice determine die size and Competency determines pool size; do not return to a universal d6. |
| Threshold / opposed highest-face play | Confirms that direct face comparison is fast and practical. | Current Difficulty Vectors and defender-wins-ties are more explicit and remain unchanged. |
| Wound-focused combat | Supports the project’s separate Vitality, 0-Vitality, Wound Roll, and location-Condition layers. | Current Wounds are not Margin-of-Success arithmetic or a generic all-ones mishap. |
| RPG and tactical-scale compatibility | Encourages testing one core engine across character, vehicle, monster, and future large-scale procedures. | Do not inherit Silhouette’s vehicle / wargame subsystems without separate design work. |

**Do not import**

```text
Additional-max-face explosion.
All-ones universal critical mishap.
Margin-of-Success arithmetic as a default outcome layer.
Generic wound penalties tied to accumulating numerical margins.
```

### Ironclaw

**Core observed pattern**

- Relevant Traits and Skills contribute d4–d12 dice to a pool.
- Read the highest die; no dice are added.
- Many tasks treat each die that beats a difficulty or opposition as an additional success.
- Careers and Species grant both fictional identity and dice on defined Skills.
- Rote procedures allow familiar, unstressed tasks to avoid ordinary uncertainty.

**Useful reference ideas**

| Ironclaw idea | Potential use here | Boundary |
|---|---|---|
| Highest-of-mixed-step pool | Strong confirmation that highest-face mixed dice are playable and expressive. | Current framework intentionally avoids mixed die sizes in one ordinary pool: Attribute establishes shared die size. |
| Career / Species as access packages | Confirms the actor architecture: Ancestry, Background, Class, Skills, and Feats can each grant defined access and Features. | Access packages must not create duplicate hidden progression or arbitrary pool dice. |
| Carry-over die-step advancement | Supports the conceptual distinction between increasing a die’s ceiling and adding more chances. | Current Attribute and Competency advancement already separate ceiling from reliability; do not add Ironclaw’s over-d12 carry-over dice. |
| Rote procedure | Useful reference for future routine-Activity procedures: correct requirements, tools, time, and calm conditions can remove a trivial roll. | Must be written as explicit Activity content, not a universal player declaration. |
| Equipment matters through permissions / defense | Supports distinct armor, weapon, and shield interaction rather than generic attack bonuses. | Equipment catalogue still needs its own calibration. |

**Do not import**

```text
“Roll every applicable Trait” pool construction.
Multiple-success counting as a default extra-resolution layer.
Species / Career dice that silently stack on every broadly related check.
Large mixed-die pools with open-ended trait relevance arguments.
```

## 3. Cross-System Comparison Against Current Canon

| Design question | Current framework | Cortex | ORE | Silhouette | Ironclaw | Research conclusion |
|---|---|---|---|---|---|---|
| Table arithmetic | No addition / subtraction in ordinary resolution. | Adds best two. | No addition but scans matches. | No addition in core read. | No addition in highest read. | Silhouette and Ironclaw directly validate the target. |
| Die size | Attribute establishes shared die size. | Trait dice vary in one pool. | Uniform d10. | Usually uniform d6. | Mixed d4–d12 pool. | Current separation is clearer than mixed pools for this project. |
| Proficiency | Competency Rank adds pool volume. | Trait-step dice and pool composition. | Stat + Skill dice. | Skill adds d6 count. | Skill / trait dice. | Silhouette is the closest confirmation; Ironclaw validates extra dice as reliability. |
| Difficulty | Bounded Difficulty Vectors / opposition. | Opposing total / difficulty dice. | Match plus height / contest. | Threshold / highest opposition. | Highest opposition / target. | Direct threshold or opposed face comparison remains a sound choice. |
| Degree of outcome | Explicit Activity entries; optional Outcome Roll. | Effect die. | Width / Height. | Margin of Success. | Multiple successes. | Keep degree tools opt-in, not universal. |
| Costs | Actions, Reaction, Stamina, Essence, Slots, Durability, Banes. | Plot Points plus trait effects. | Willpower / special dice in some games. | Modifiers and thresholds. | Gifts / reactions / dice. | Current in-world resource policy remains distinctive and appropriate. |
| Persistent states | Conditions / Tags / Traits only when explicit. | Assets and complications can accumulate. | Wounds / dice penalties. | Wound penalties. | Conditions / tactical states. | DEC-101’s low-memory policy is reinforced. |

## 4. Candidate References for Future Work

These are **research prompts**, not adopted mechanics.

### A. Rote / routine Activities — Ironclaw reference

Explore an explicit Activity option such as:

```text
When an Actor meets a stated Rank, tool, time, and safety Requirement,
the Activity succeeds without a check.
```

This could be valuable for routine Craft, travel, field medicine, or professional work. It must be Activity-specific and must not erase consequential uncertainty.

### B. Feature package template — Cortex reference

Use a standard content-record shape:

```text
Feature name
Fiction / scope
Requirement
Activation / Action
Cost
Resolution
Effect
Duration
Limit / exception
Tags
```

This is compatible with the current Class-document standard and directly supports DEC-101’s low-memory conversion policy.

### C. One-roll combat audit — ORE reference

When combat content is tested, ask:

```text
Can the declared Attack, defense selection, opposed check,
Damage Absorption, mitigation, and stated Condition resolve
one meaningful exchange without another universal roll?
```

The purpose is not to add Width / Height; it is to prevent accidental roll cascades.

### D. Ranks versus ceiling — Ironclaw / Silhouette reference

Future Attribute and Competency playtests should continue testing the current split:

```text
Attribute die size:
  what result is possible?

Competency pool volume:
  how reliably can that result occur?
```

Ironclaw’s mixed dice and Silhouette’s Skill dice offer useful comparative baselines, but neither replaces the current model.

## 5. Sources Consulted

- Cortex Prime overview and modular trait-set discussion: <https://cthonicstudios.com/cortex-prime/>; <https://www.atlas-games.com/cortexprime>
- One Roll Engine tutorial: <https://arcdream.com/home/2011/04/a-one-roll-engine-tutorial/>
- Dream Pod 9 / Silhouette overview: <https://index.rpg.net/display-generalinfo.phtml?key=system&value=Silhouette>; probability / alternate-dice reference: <https://www.jestertrek.com/temp/heavy-gear/manuals/SilCOREdiceprob.pdf>
- Ironclaw 2e mechanics discussion: <https://www.rpg.net/reviews/archive/18/18371.phtml>; Cardinal system reference: <https://ironclaw.fandom.com/wiki/Cardinal_Game_System>

## 6. Scope Boundary

This comparison does not alter canon. Any candidate above requires its own explicit design decision, canonical owner, calibration, and conversion-impact review before adoption.
