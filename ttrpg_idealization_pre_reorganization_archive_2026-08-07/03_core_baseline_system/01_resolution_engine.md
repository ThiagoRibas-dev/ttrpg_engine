# Resolution Engine

**Status:** Canonical universal resolution procedure.  
**Vocabulary:** See `00_baseline_framework_glossary.md` for shared definitions.

## 1. Core Check Procedure

When an actor attempts an uncertain action:

1. Identify the relevant Skill, Tradition, defense, or other capability.
2. Determine the relevant Attribute Die Size.
3. Build the Natural Dice Pool from Attribute and Competency.
4. Apply permanent or ordinary class, feat, equipment, and situational effects.
5. Apply Die Step-Ups and Die Step-Downs.
6. Apply final Boons and Banes, including cancellation and typed stacking.
7. Resolve the final Difficulty Vector or opposed contest.
8. Roll the final dice pool.
9. Compare successful faces against the DC, Required Successes, or opposing pool.
10. Apply the resulting success, failure, maneuver, condition, or Permission.

Ordinary resolution uses no linear numerical modifiers.

## 2. Dice and Pools

The ordinary Attribute Die ladder is:

```text
d4 → d6 → d8 → d10 → d12
```

The ordinary mathematical ceiling is `d12`. Former permanent over-cap die notation is deprecated. Exert may temporarily Step-Up an affected d12 die to d20 under its specific maneuver procedure.

The base check is normally:

```text
2dX keep highest
```

where `X` is the relevant Attribute Die Size. Competency Rank, class features, Boons, Banes, equipment, and other explicit effects change the final pool or its permissions.

### Natural Dice Pool

The pool produced by ordinary Attribute, Competency, Class, and persistent actor factors before temporary or special enhancements.

### Enhanced Dice Pool

The final or temporarily modified pool after applicable feats, spells, equipment, circumstances, and other explicit effects are applied.

The normal unbuffed pool range is generally `1dX` to `6dX`, with `6dX` reserved for Legend Competency and equivalent content. Content may exceed that guideline through explicit Legend or Mythic effects, but such expansion must remain controlled by the content granting it.


## 4. Difficulty Classes and Difficulty Vectors

Ordinary Difficulty Classes use a bounded Target Number from 2 through 12.

| DC | Working description |
|---:|---|
| 2 | Trivial |
| 3 | Routine |
| 5 | Challenging |
| 7 | Formidable |
| 9 | Heroic |
| 11 | Legendary |
| 12 | Extreme |

A difficulty vector is written with comma-separated thresholds:

```text
DC 5
DC 5,4
DC 6,5,3
```

Roll the final Dice Pool, sort dice from highest to lowest, sort the vector thresholds from highest to lowest, and compare them positionally. Extra dice beyond the vector length are ignored for that vector. The check succeeds only when every threshold in the vector is met.

The exact calibration of DC names and vector choices remains a Phase 1 research task.

## 5. Boons and Banes

Boons and Banes are final-pool effects. They are resolved after ordinary pool construction and after applicable Die Step-Ups and Die Step-Downs.

### Cancellation

One Boon cancels one Bane and one Bane cancels one Boon.

```text
2d8 +2B +1X → 2d8 +1B → 3d8
```

### Typed stacking

Boon and Bane types follow a PF2e-inspired stacking model:

- **Circumstance:** Immediate situation, environment, positioning, timing, visibility, terrain, or physical conditions.
- **Enhancement:** Direct improvement or degradation of an actor, object, weapon, armor, or spell’s performance.
- **Morale:** Emotional force, confidence, fear, inspiration, social pressure, hope, despair, or group cohesion.
- **Competence:** Temporary assistance from training, instruction, advice, preparation, specialized knowledge, coordinated technique, or focused performance.
- **Untyped:** An exceptional effect deliberately excluded from ordinary categories.

Multiple effects of the same type do not stack; use only the largest applicable Boon or Bane dice quantity of that type. Effects of different types stack normally. Untyped effects may stack with typed effects and other Untyped effects unless the source says otherwise.

The same named source cannot apply the same Boon or Bane more than once to the same target or check unless it explicitly says otherwise.

### Boons

Each remaining Boon adds one die of the same size to the final pool.

```text
2d8 +1B → 3d8
```

Boons participate normally in Required Success counting. A Boon does not grant an Automatic Success unless its specific effect says so.

### Banes

Each remaining Bane removes one die from the final pool.

```text
3d8 +1X → 2d8
3d8 +2X → 1d8
```

A pool cannot be reduced below one die. If a Bane is applied to a one-die pool, apply one Die Step-Down to that die:

```text
1d8 +1X → 1d6
```

Further Banes do not apply additional Die Step-Downs. If the die is already a `d4`, the check is an automatic failure.


## 6. Die Step-Up and Die Step-Down

A Die Step-Up increases the size of every affected die by one step. A Die Step-Down decreases the size of every affected die by one step.

```text
Up-Shift: d8 → d10
Down-Shift: d10 → d8
```

Die Step-Ups and Die Step-Downs are applied before final Boons and Banes. The ordinary ladder ends at d12; Exert is the explicit temporary d12-to-d20 exception. Universal resource costs and limits are not defined here; the specific Stamina, Essence, Class, Feat, Spell, Equipment, or Condition rule provides them.

If a Die Step-Down would reduce a `d4` under a specific effect, that effect must state its consequence. A Bane-induced `d4` Step-Down specifically causes automatic failure.

## 7. Opposed Checks

An opposed check uses the same final-pool construction procedure for both participants.

1. Identify the initiator as the attacker for that contest.
2. Identify the responding party as the defender.
3. Compare the highest rolled faces.
4. If tied, compare the remaining dice in descending order.
5. If the pools remain identical through all comparable dice, the defender wins the tie.
6. Apply the contest’s success or failure consequence.

The defender wins ties in ordinary opposed contests. A specific neutral contest, such as a race, may explicitly allow a tie instead of requiring a victor.

The base opposed framework is success or failure. Superior defensive results, counterattacks, ripostes, or other exceptional outcomes require an explicit Class, Feat, Equipment, Spell, or other Permission.

## 8. Automatic Successes

An Automatic Success is granted directly by a specific effect. It is not a die.

Automatic Successes are resolved after the final pool has been constructed, including all Boons, Banes, and Die Steps, and when that pool is rolled. They do not alter the pool itself.

An Automatic Success:

- Counts toward Required Successes.
- Is not affected by Boons, Banes, Die Step-Ups, or Die Step-Downs.
- May be granted by the same effect that grants a Boon or Bane.
- May exceed the number of Required Successes under the base framework.

In opposed contests, compare Automatic Success totals before rolling dice. The side with more Automatic Successes wins. If both sides have the same number, roll the pools and resolve the ordinary opposed procedure.

Example:

```text
DC 9 (3)
5d12 +1 Automatic Success
```

The character needs two successful rolled faces because one success is already guaranteed.

The base framework does not itself grant sources of Automatic Successes or directly alter Required Successes. Specific Classes, Feats, Spells, Equipment, Traditions, Ancestries, or Mythic effects may provide those Permissions.

## 9. Requirements and Permissions

A **Requirement** states what must be true before an action or effect may be used.

A **Permission** explicitly allows an actor to do something outside the ordinary baseline procedure.

Examples:

```text
Requirement: Veteran Death Tradition.
Requirement: A visible target.
Permission: Cast as a Reaction.
Permission: Affect an immune target.
Permission: Choose one die result after rolling.
```

Requirements and Permissions belong to the specific Class, Feat, Spell, Equipment, Tradition, Ancestry, or Condition that grants them.

## 10. Complex Checks and Maneuvers

Additional successful faces can satisfy Required Successes or trigger explicitly defined results.

Universal combat maneuvers and Called Shots use Required Successes or an explicit Bane trade-off. The exact maneuver procedures and consequences belong to `../04_simulationist_subsystems/04_combat_maneuvers.md`.

The Resolution Engine does not automatically generate counterattacks, special effects, or superior defensive maneuvers unless a specific rule grants that Permission.

## 11. Related Canonical Owners

- Framework vocabulary: `00_baseline_framework_glossary.md`
- Attributes and derived statistics: `02_attributes_and_derived_statistics.md`
- Statistical relationships: `08_statistical_framework_and_check_modes.md`
- Domains and Skills: `09_domains_skills_activities_and_crafting.md`
- Magic: `10_magic_schools_traditions_and_spellcasting.md`
- Defenses, damage, and wounds: `../04_simulationist_subsystems/01_defenses_and_damage_modeling.md`
- Combat maneuvers: `../04_simulationist_subsystems/04_combat_maneuvers.md`
- Resources and conditions: `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md`
