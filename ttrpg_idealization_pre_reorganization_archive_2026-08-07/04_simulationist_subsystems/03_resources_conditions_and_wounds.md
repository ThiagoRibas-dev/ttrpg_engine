# Resources, Conditions, and Wounds

**Status:** Canonical resource, condition, and recovery subsystem owner.  
**Scope:** Resource expenditure, depletion, recovery, ongoing Conditions, Wound consequences, stabilization, and treatment.

## 1. Resource Ownership

Resource capacity derivations belong to:

```text
../03_core_baseline_system/02_attributes_and_derived_statistics.md
```

This document owns how resources are spent, depleted, recovered, and affected by conditions.

Current in-world resources include:

- Vitality.
- Stamina.
- Essence.
- Spell Slots.
- Equipment Durability.
- Provisions and other campaign resources.

## 2. Stamina

Stamina represents physical exertion, breath, balance, active-defense fatigue, and martial effort. It is spent by the applicable action, maneuver, Class, Feat, Equipment, or other effect. The base framework’s resource-based maneuver procedures, including **Soften Blow**, are defined with the other combat maneuvers in `04_combat_maneuvers.md`.

Other potential Stamina expenditures include:

- Triggered Deflect or Evasion.
- Physical Die Step-Up.
- Martial Surges.
- Emergency movement or reactions.

The exact cost of each expenditure belongs to the action, Class, Feat, Equipment, or other effect that grants it. This document owns recovery and depletion consequences.

## 3. Essence

Essence is the magical and supernatural exertion resource. It is spent by the applicable action, maneuver, Class, Feat, Spell, Equipment, or other effect. The base framework’s resource-based maneuver procedure, **Ward Self**, is defined with the other combat maneuvers in `04_combat_maneuvers.md`.

Spellcasting-specific Essence expenditure belongs to `../03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md`. A non-spell supernatural ability declares its own Essence cost.

## 4. Depletion and Zero-Resource States

A resource cannot be spent below zero. Its resource-specific consequences apply when it reaches zero.

### Vitality: Incapacitated, Wounds, and Death

A **Wound Roll** uses the following Anatomical Wound Die. A Natural Critical or any other effect that forces a Wound Roll uses this table.

| d8 | At more than 0 Vitality | At 0 Vitality |
|---:|---|---|
| 1 | Nothing | Death |
| 2 | Head Wound: Dazed | Head Wound: Dazed |
| 3 | Chest Wound: Fatigued | Chest Wound: Fatigued |
| 4 | Abdomen Wound: Nauseated | Abdomen Wound: Nauseated |
| 5 | Shield or Off-Arm Wound: Impaired | Shield or Off-Arm Wound: Impaired |
| 6 | Weapon Arm Wound: Impaired | Weapon Arm Wound: Impaired |
| 7 | Leg Wound: Flat-Footed | Leg Wound: Flat-Footed |
| 8 | Nothing | Nothing |

At more than 0 Vitality, results 1 and 8 produce no Wound. A forced Wound Roll therefore has a 2-in-8 chance of no Wound before the creature is Incapacitated.

When a creature reaches **0 Vitality**, it becomes **Incapacitated**: it cannot take ordinary Actions or Reactions. Immediately make a Wound Roll. Make another Wound Roll each time an Incapacitated creature is hit by a subsequent Attack.

The creature dies if any of the following occurs:

- A successful **Execution** maneuver kills it.
- The Wound Roll shows 1 while it has 0 Vitality.
- The Wound Roll shows a location result from 2 through 7 that the creature has already received since becoming Incapacitated. The matching result need not be consecutive; intervening results do not remove the earlier location result.

### Stamina: Winded

At 0 Stamina, a creature is **Winded**. It cannot spend Stamina until it recovers Stamina. Its practical limitations follow from the costs of the actions, maneuvers, and Permissions it no longer has resources to use.

### Essence: Drained

At 0 Essence, a creature is **Drained**. It cannot spend Essence until it recovers Essence. Its practical limitations follow from the costs of the actions, maneuvers, spells, and Permissions it no longer has resources to use. Spell Slot casting remains available unless the specific spell requires Essence.

## 5. Conditions

Conditions are binary flags, state changes, Banes, Die Step-Downs, action restrictions, movement restrictions, or explicit Permissions. Each Condition must state its own effects rather than relying on an unstated universal modifier rule.

Examples include:

- Blinded.
- Deafened.
- Exhausted.
- Confused or Muddled.
- Prone.
- Restrained or Grappled.
- Shaken or Frightened.
- Concussed.
- Bleeding.
- Disabled limb.

Conditions may restrict Reactions, Actions, movement, spellcasting, or resource expenditure. They do not alter opposed tie rules unless their specific entry explicitly says so.

### Bleeding

A Bleeding creature must spend Essence each turn or take damage. The source that inflicts Bleeding states the damage it deals and any additional treatment or removal procedure.

### Wound Conditions

When a Wound Roll produces a result from 2 through 7, apply the listed Wound Condition. A creature may have several different Wound Conditions. A Wound Condition does not stack with itself unless its entry says otherwise. Each Wound Condition remains until removed by applicable treatment, recovery, or an explicit effect.

#### Dazed — Head Wound

A Dazed creature cannot spend Essence. It also pays **+1 Action** to perform Activities with the **Concentrate** Tag.

If the increased cost exceeds the creature’s Actions remaining for the turn, it cannot perform that Activity.

#### Fatigued — Chest Wound

A Fatigued creature cannot spend Stamina.

#### Nauseated — Abdomen Wound

Each Activity a Nauseated creature takes costs **+1 Action**.

If the increased cost exceeds the creature’s Actions remaining for the turn, it cannot begin that Activity.

#### Impaired — Arm Wound

When performing a Strike Activity or an Activity with the **Manipulate** Tag, an Impaired creature rolls `1d10`. On a result of **1–2**, the Activity fails. Its Actions are spent, but other resource costs for that Activity are not spent.

A creature has only one Impaired condition regardless of how many arms it has. Additional arm Wounds do not stack Impaired.

#### Flat-Footed — Leg Wound

A Flat-Footed creature cannot use Reflexes. It counts as flanked against physical attackers.

Any Activity with the **Movement** Tag costs **+1 Action**.

If the increased cost exceeds the creature’s Actions remaining for the turn, it cannot begin that Activity.

## 6. Wound Consequences and Recovery

The Defenses, Damage, and Wounds subsystem determines when a Wound is inflicted and which anatomical location is affected. This document determines:

- Ongoing Wound consequences.
- Treatment requirements.
- Recovery time.
- Stabilization.
- Vitality and resource interactions.
- Recovery from Minor, Moderate, Severe, and Critical Wounds.

### Stabilization

**Cost:** 1 Action.

A creature may be stabilized with a successful **Knowledge — Anatomy and Healing** check against **DC 5**. Stabilization leaves the creature at 0 Vitality and unconscious; it does not heal a Wound.

### Wound Duration and Recovery

A Wound Condition lasts until its associated Wound is healed. A Long Rest heals one Wound.

A successful Knowledge — Anatomy and Healing check improves the next Long Rest by healing one additional Wound. The healer may voluntarily increase the check’s DC by 5 for each further additional Wound healed by that Long Rest.

A specific Spell, Potion, item, ability, or other effect states whether and how it heals Vitality, Wounds, or Conditions. Wounds do not escalate through a separate universal procedure.

## 7. Resource Recovery

Recovery uses the following in-world events. No out-of-character recovery currency is used.

| Resource | Short Breather | Focused recovery | Long Rest or safe camp | Other restoration |
|---|---|---|---|---|
| Vitality | No recovery | No recovery | Restore CON Resource Value | Medical treatment and magical restoration may restore Vitality as their specific rules state |
| Stamina | Fully restore after 10 minutes without an immediate threat | — | Fully restore | An explicit effect may restore Stamina |
| Essence | — | Fully restore after 10 uninterrupted minutes of meditation, prayer, or similar practice | Fully restore | An explicit effect may restore Essence |
| Spell Slots | No recovery | No recovery | Recover during and after the Long Rest preparation procedure | No default exceptional restoration exists |

Wounds and Conditions may limit or change a recovery event where their individual rules say so.

## 8. Control Conditions

### Prone

A Prone creature does not count for flanking.

**Crawl:** A Prone creature may use a 1-Action Movement Activity to move up to 5 feet or 1 square in exact-distance play. Crawl does not change an abstract Distance Tier by default.

**Stand:** A Prone creature may use a 1-Action Movement Activity to stand. Standing triggers Attack of Opportunity.

A Prone creature takes 1 **Circumstance Bane** on Strike and Deflect checks. It cannot use Evasion against a melee Attack.

A melee Attack targeting a Prone creature gains 1 **Circumstance Boon**. A ranged Attack targeting a Prone creature takes 1 **Circumstance Bane**.

### Restrained

A Restrained creature has 2 Actions instead of 3 on each Turn. It may use Movement Activities, Manipulate Activities, Concentrate Activities, Spell Activities, Deflect, and Strikes normally unless another rule says otherwise.

At the start of each Turn, a Restrained creature automatically spends 1 Stamina and 1 Essence. A resource at 0 cannot be spent below 0 and causes no additional universal consequence.

### Immobilized

An Immobilized creature cannot use Movement Activities. It otherwise acts normally unless another rule says otherwise.

A source may apply Immobilized together with Restrained or another Condition. Each source defines its own combined effects and Escape procedure.

## 9. Social Conditions

Social Conditions use the existing typed Boon/Bane stacking rules. Effects of the same type do not stack; effects of different types stack normally. A Social Condition has no general early-removal rule. A specific Ability or effect may state that it removes one.

### Rallied

A Rallied creature gains 1 **Morale Boon** to its next Strike, Defense Maneuver, or Resistance check using Fortitude or Willpower before the end of its next turn.

### Shaken

An Attack that can legally target a Shaken Actor gains 1 **Circumstance Boon** before the end of the Shaken Actor’s next turn. Shaken does not itself grant permission to target an Actor that the Attack could not otherwise legally target.

### Distracted

A Distracted creature takes 1 **Circumstance Bane** on its next Strike or Defense Maneuver check before the end of its next turn.

## 10. Source Links

- Vocabulary and universal resolution: `../03_core_baseline_system/00_baseline_framework_glossary.md`, `../03_core_baseline_system/01_resolution_engine.md`
- Attributes and capacity derivation: `../03_core_baseline_system/02_attributes_and_derived_statistics.md`
- Actions and Reactions: `../03_core_baseline_system/04_action_economy_and_turn_structure.md`
- Magic and Essence uses: `../03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md`
- Equipment Durability: `../03_core_baseline_system/12_equipment_durability_and_economy.md`
- Defenses, Damage Absorption, and anatomical impact: `01_defenses_and_damage_modeling.md`
- Combat maneuvers: `04_combat_maneuvers.md`
