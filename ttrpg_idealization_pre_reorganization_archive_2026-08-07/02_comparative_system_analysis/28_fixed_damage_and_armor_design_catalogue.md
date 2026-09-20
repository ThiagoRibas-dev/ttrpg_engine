# Fixed Damage and Armor Design Catalogue

**Status:** Research catalogue; non-canonical.  
**Purpose:** Compare weapon-damage and armor-protection patterns before selecting fixed Damage Box and Damage Absorption values for the project.

This document does not establish a weapon, armor, shield, Damage Box, or Damage Absorption rule.

## 1. Current Project Constraints

The current canonical framework supplies these boundaries:

```text
Weapons and damaging effects use fixed Damage Boxes.
Damage Absorption is a post-hit layer.
Soften Blow applies after Damage Absorption.
Vitality receives remaining Damage Boxes.
Wounds use the separate d8 Wound Roll procedure when required.
```

The open task is therefore not whether damage is rolled; it is how fixed weapon Damage Boxes, armor Damage Absorption, weapon Traits, shields, and exceptional effects interact.

## 2. Reference-System Matrix

| System | Weapon damage pattern | Armor pattern | Transferable lesson | Fit with fixed Damage Boxes |
|---|---|---|---|---|
| D&D 3.5e | Variable weapon dice plus ability modifiers | Armor Class prevents hits; Damage Reduction is exceptional | Separating avoidance from absorption is useful; ordinary AC is not | Partial: use its weapon categories and Damage Reduction concept, not AC/dice |
| Pathfinder 2e | Variable weapon dice and modifiers | AC prevents hits; item Hardness reduces damage to the item; Shield Block transfers some damage to a shield | Item Hardness / Broken / repair is a clean item-state pattern | Partial: useful for later Durability, not for the core actor armor rule |
| Shadow of the Demon Lord | Variable weapon damage | Armor primarily affects Defense; optional variants explore damage reduction | Armor can carry mobility/Agility trade-offs instead of only protection | Partial: useful for armor drawbacks and tier identity |
| Mythras / BRP | Variable weapon damage plus location | Armor Points reduce damage at the struck location | Armor can make weak weapons ineffective while location and weapon effects preserve tactical distinction | Strong conceptual fit; use flat absorption, not local HP arithmetic |
| GURPS | Variable damage, often with damage-type modifiers | Damage Resistance subtracts from incoming damage | Set protection by the attacks armor should reliably stop | Strong fit for calibration philosophy; avoid its arithmetic and location multipliers |
| Year Zero Engine | Fixed weapon Damage rating plus extra-success damage | Armor rolls dice; each success blocks one damage | Small fixed weapon ratings are easy to read; armor can be a separate post-hit defense | Strong for weapon bands; armor dice conflict with the current fixed/fast goal |
| Dragonbane | Variable weapon damage | Armor Rating subtracts from physical damage | Flat armor rating plus movement/skill drawbacks is highly table-friendly | Strong fit for basic flat absorption and armor trade-offs |
| Savage Worlds | Damage roll compared to Toughness | Armor contributes to Toughness, then wounds depend on margin | Thresholds can distinguish glancing impact from Wounds | Limited fit: margin conversion conflicts with fixed Boxes but informs pacing |

## 3. Design Patterns

### Pattern A — Fixed Weapon Damage plus Flat Armor Absorption

```text
Weapon / effect:
  Fixed Damage Boxes.

Armor:
  Fixed Damage Absorption per eligible Attack.

Resolution:
  Damage Boxes
  − Damage Absorption
  = remaining Damage Boxes.
```

**Examples:** GURPS Damage Resistance, Dragonbane Armor Rating, Mythras Armor Points.

**Benefits**

- Directly matches the current fixed Damage Box direction.
- No damage roll after a successful Attack.
- Dagger, sword, great weapon, and monster attacks can have immediately readable identities.
- Armor is reliably valuable against low-damage attacks.
- Easy to combine with Soften Blow, Power Attack, and Armor-Piercing Traits.

**Risks**

- Weak weapons may do no damage against strong armor.
- Small changes to a Damage Box or Absorption value can strongly affect pacing.
- Requires a deliberate answer on whether armor may reduce damage to zero.

### Pattern B — Fixed Weapon Damage plus Armor Threshold

```text
If Damage Boxes do not exceed the armor threshold:
  No Vitality damage.

If Damage Boxes exceed the threshold:
  Apply a stated fixed remainder or full damage.
```

**Examples:** Some threshold/Hardness systems; Savage Worlds’ Toughness concept.

**Benefits**

- Fast to read at the table.
- Makes armor feel categorical: some attacks simply cannot penetrate.
- Good for creature hide, barriers, and large monsters.

**Risks**

- Coarser than flat absorption.
- Creates binary immunity bands quickly.
- Needs special rules for big weapons, Armor Piercing, Called Shots, and magic.

### Pattern C — Fixed Damage plus Penetration Rating

```text
Weapon:
  Damage Boxes + Penetration rating.

Armor:
  Damage Absorption.

Resolution:
  Reduce Absorption by Penetration, then absorb remaining damage.
```

**Examples:** GURPS armor divisors; Savage Worlds Armor Piercing; Mythras bypass-armor effects.

**Benefits**

- Keeps a dagger, warhammer, spear, pick, and great weapon tactically different even when their Damage Boxes overlap.
- Supports special materials, magic, monster hide, siege weapons, and anti-armor tactics.
- Makes a weapon better against armor without automatically making it best against unarmored targets.

**Risks**

- Adds one additional equipment statistic.
- Needs bounded values and a clear order of operations.

### Pattern D — Fixed Damage plus Damage-Type Matchups

```text
Weapons / effects have damage Tags:
  Slashing, Piercing, Bludgeoning, Fire, Cold, etc.

Armor or targets state:
  Absorption changes, resistance, vulnerability, or immunity
  against stated Tags.
```

**Examples:** Dragonbane armor-type adjustments; Mythras weapon Special Effects; many d20 resistances.

**Benefits**

- Strong simulationist identity.
- Makes weapon choice and monster research matter.
- Fits the project’s Tag architecture.

**Risks**

- A full universal matchup table is content-heavy.
- Should be selective: use only where fiction matters, not on every armor/weapon pair.

### Pattern E — Absorption plus Item Durability

```text
Armor absorbs normally.
Exceptional attacks, criticals, corrosive effects, or explicit maneuvers
reduce item Durability or impair the item.
```

**Examples:** PF2e Shield Block / Broken item pattern; Dragonbane gear Durability; Mythras Sunder.

**Benefits**

- Separates everyday protection from extraordinary equipment harm.
- Preserves the current decision not to make routine attacks erode equipment.
- Gives special weapons and monster attacks a distinctive role.

**Risks**

- Requires Durability procedures and repair content.
- Currently deferred by project scope.

### Pattern F — Margin-to-Damage Conversion

```text
The amount by which an Attack beats a defense
increases damage or converts a hit into Wounds.
```

**Examples:** Savage Worlds Raises; Torg-style success margin systems.

**Benefits**

- Connects combat skill directly to damage severity.
- Makes superior hits feel distinct.

**Risks**

- Conflicts with the current decision that weapons deal fixed Damage Boxes.
- Adds a second result-evaluation layer after an already opposed resolution roll.
- Better reserved for Natural Criticals, Permissions, or special effects if desired.

### Pattern G — Location-Specific Armor Absorption

```text
A Wound location determines which armor value applies.
```

**Examples:** Mythras / BRP hit-location armor.

**Benefits**

- Highly simulationist.
- Gives helmets, bracers, greaves, shields, and Called Shots concrete meaning.

**Risks**

- The project’s Wound Roll currently occurs only when required, not on every hit.
- Applying locations to every ordinary hit would add tracking and resolution overhead.
- Best deferred until body-slot and armor catalogue work.

## 4. Catalogue of Appropriate Building Blocks

These ideas are compatible with the present project direction and can be combined.

| Building block | Suggested current role |
|---|---|
| Fixed Damage Boxes | Core weapon/effect output |
| Flat Damage Absorption | Core armor/hide/material protection |
| Penetration / Armor-Piercing Trait | Limited weapon, spell, monster, and special-material differentiation |
| Damage Tags | Selective matchup and fiction tool, not mandatory universal matrix |
| Shield Boon to Deflect | Already canonized defensive identity |
| Shield Damage Absorption | Candidate additional shield role |
| Heavy Armor Bane to Evasion | Already canonized armor trade-off |
| No routine Durability loss | Current scope boundary |
| Critical / exceptional Durability loss | Future special effect or item rule |
| Called Shot location interaction | Future armor body-slot pass |
| Natural armor / hide | Same interface as armor, with explicit creature exceptions |

## 5. Patterns That Do Not Fit the Current Direction

| Pattern | Why not now |
|---|---|
| Weapon damage dice | Superseded by fixed Damage Boxes |
| One universal Armor Class | Superseded by layered Deflect, Evasion, Fortitude, Willpower, and Damage Absorption |
| Damage margin as normal damage scaling | Competes with fixed Damage Boxes and adds a second post-roll calculation |
| Armor rolls after every hit | Adds variability and extra rolls where the current model seeks fixed resolution |
| Routine armor/weapon degradation from every hit | Deferred; conflicts with the current minimal Durability scope |
| Location armor on every hit | Wound locations are not rolled on every ordinary hit |

## 6. Candidate Starting Packages

### Package 1 — Clean Fixed Baseline

```text
Weapons:
  1–4 fixed Damage Boxes by category.

Armor:
  0–3 fixed Damage Absorption by category.

Shield:
  +1 Boon to Deflect.

Traits:
  Selective Armor-Piercing or damage Tags.
```

**Best for:** fastest first combat model and easiest time-to-defeat calibration.

### Package 2 — Fixed Baseline plus Penetration

```text
Weapons:
  1–4 fixed Damage Boxes.
  0–2 Penetration.

Armor:
  0–4 Damage Absorption.

Resolution:
  Penetration reduces applicable Absorption before boxes are absorbed.
```

**Best for:** weapon identity and armored-target tactics.

### Package 3 — Fixed Baseline plus Selective Matchups

```text
Weapons:
  Fixed Damage Boxes plus Tags.

Armor / creatures:
  Fixed Absorption plus selected resistance or vulnerability clauses.

Examples:
  Piercing may bypass a stated armor.
  Bludgeoning may pressure rigid armor.
  Fire may ignore ordinary hide.
```

**Best for:** simulationist content conversion without a full lookup table.

## 7. Calibration Questions for the Next Pass

1. What fixed Damage Box range should ordinary weapons occupy?
2. What fixed Damage Absorption range should ordinary armor occupy?
3. May armor fully negate a damaging Attack, or must one Box always remain after Damage Absorption?
4. Is Penetration a universal Trait, a selective Trait, or deferred?
5. Does a shield only grant its Deflect Boon, or also Damage Absorption?
6. Which damage Tags are worth defining in the baseline, if any?
7. Which effects may bypass armor: Natural Criticals, Called Shots, weapon Traits, spells, or all of these?
8. What time-to-defeat target should representative weapons and armor produce against representative Vitality tracks?

## 8. Reference Notes

- PF2e item Hardness and Broken state: <https://2e.aonprd.com/Rules.aspx?ID=195>
- Mythras armor-point and Sunder discussion: <https://www.reddit.com/r/Mythras/comments/126wm3i/equipment_hp/>
- Dragonbane Armor Rating: <https://anyflip.com/ksvio/rnah/basic/51-100>
- Year Zero fixed weapon damage and armor dice: <https://www.weylan-yutani.com/year_zero_engine>
- GURPS Damage Resistance discussion: <https://www.reddit.com/r/gurps/comments/1052vy1/question-about-armor-damage-resistance/>
- Savage Worlds Toughness / armor context: <http://savage-worlds.wikidot.com/rules-quick-reference>
