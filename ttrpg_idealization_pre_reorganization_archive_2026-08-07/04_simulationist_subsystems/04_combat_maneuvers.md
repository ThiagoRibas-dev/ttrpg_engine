# Combat Maneuvers

**Status:** Canonical base combat-maneuver framework owner.  
**Scope:** Baseline tactical maneuvers that operate on top of the defense, damage, action, resource, and condition frameworks. This document owns a maneuver’s baseline purpose, timing, Action cost, resource cost, and stated effect. Where a named baseline maneuver is explicitly marked incomplete, its detailed resolution procedure remains open.

## 1. Maneuver Framework

A maneuver is a tactical Activity, Reaction, Strike variant, damage response, or state response. It uses the universal resolution procedure and its stated requirements, trade-offs, resource expenditure, or explicit Class, Feat, Spell, Equipment, or other Permission.

The universal resolution procedure belongs to `../03_core_baseline_system/01_resolution_engine.md`. Action availability belongs to `../03_core_baseline_system/04_action_economy_and_turn_structure.md`. Activity Tags belong to `../03_core_baseline_system/09_domains_skills_activities_and_crafting.md`. Conditions and Wound consequences belong to `03_resources_conditions_and_wounds.md`.

### 1A. Maneuver Families

| Family | Timing role |
|---|---|
| Reaction maneuver | Uses the actor’s Reaction outside its turn in response to a stated trigger |
| Triggered defense | Used in response to an eligible Attack; costs the stated resource but not a Reaction |
| Damage response | Used after an Attack’s damage is determined and before Vitality is marked |
| Turn Activity | Uses Actions during the actor’s turn |
| Strike variant | Modifies or follows a Strike without being a separate Activity unless stated otherwise |
| State response | Used only when its stated target state exists |

## 2. Triggered Defenses

### Deflect

**Cost:** 1 Stamina.  
**Trigger:** An eligible physical Attack.

The defender rolls a suitable Strike against the Attack. A shield grants 1 Boon to this check. Shield Block is a Deflect mode, not a separate baseline maneuver.

### Evasion

**Cost:** 1 Stamina.  
**Trigger:** An eligible Attack that can be avoided through movement, footwork, positioning, or reflex.

The defender rolls Reflexes against the Attack. Heavy Armor imposes 1 Bane on this check.

## 3. Reaction Maneuvers

### Interpose

**Cost:** 1 Reaction and 2 Stamina.  
**Trigger:** An Attack the interposing creature can plausibly Deflect.

The creature intercepts the Attack to protect another Actor, object, route, or position, then makes the required Deflect. One Stamina pays for Interpose and one Stamina pays for Deflect.

### Attack of Opportunity

**Trigger:** An adjacent creature uses a Manipulate or Movement Activity.

**Cost:** 1 Reaction.

The reacting creature makes 1 Strike against the triggering Actor without paying the Strike’s Action cost.

## 4. Damage Responses

### Soften Blow

**Timing:** No Action; once per Attack.

A creature may spend Stamina to lower damage from a source that targets Reflexes, Deflect, or Damage Absorption. After applicable damage is determined and before Damage Boxes are marked against Vitality, each Stamina spent prevents one remaining Damage Box. A damaging Attack must still mark at least one Damage Box.

### Ward Self

**Timing:** No Action; once per Attack.

A creature may spend Essence to lower damage from an effect that targets Fortitude or Willpower. After damage is determined and before Damage Boxes are marked against Vitality, each Essence spent prevents one remaining Damage Box. A damaging Attack must still mark at least one Damage Box. Ward Self mitigates damage only; it does not prevent Conditions, Wounds, possession, curses, or other non-damage consequences.

## 5. Turn Activities

### Full Defense

**Cost:** 2 Actions.

Until the start of its next turn, a creature may spend up to its Character Level in Stamina whenever it makes a Deflect, Evasion, or Interpose. Each Stamina spent grants 1 Boon to that separate defensive check. The Character-Level cap applies separately to each defensive check.

### Exert

**Cost:** No Action and X Stamina, where X cannot exceed the creature’s Character Level.

When making a Strength- or Dexterity-based check or roll, a creature may choose up to X dice in its Dice Pool and Step-Up each chosen die once. Exert may Step-Up a d12 die to d20. This is a temporary exception to the ordinary d12 Attribute Die ceiling.

### Charge

**Cost:** 2 Actions and 1 Stamina.

The creature moves up to its Speed and targets one Actor. It may then perform at most one Strike and one of either Grapple or Shove against that Actor. Default Charge combinations are Strike then Grapple, Strike then Shove, and Shove then Strike when Reach permits. Grapple then Shove and Shove then Grapple are not default Charge combinations.

The creature takes 1 Bane on the next Deflect or Evasion it makes within 1 round.

### Grapple

**Cost:** 1 Action.

The grappler rolls Martial Arts against the target’s Reflexes. The target must be within one Size category of the grappler. The grappler takes 1 Circumstance Bane when Grappling a larger target and gains 1 Circumstance Boon when Grappling a smaller target.

On success, the target becomes Restrained by the Grapple. The Grapple lasts until the target succeeds at Escape or another explicit effect ends it.

A Grappling Actor and a Grappled Actor cannot move independently. When either attempts a Movement Activity, the moving Actor rolls Athletics or Martial Arts in an opposed contest against the other Actor. On success, both Actors move together; on failure, neither moves.

Multiple Grapples do not stack their Restrained penalties. A Grappled Actor attempting to move must win the movement contest against each Grappling creature.


### Trip

**Cost:** 1 Action and 1 Stamina.

The attacker rolls a Strike against the target’s Athletics or Acrobatics. On success, the target becomes Prone.

### Shove

**Cost:** 1 Action.

The attacker rolls Athletics or Martial Arts against the target’s Athletics or Acrobatics. Apply the same Size limits and Circumstance modifiers as Grapple: the target must be within one Size category; the attacker takes 1 Circumstance Bane against a larger target and gains 1 Circumstance Boon against a smaller target.

A Shove moves the target by its future defined forced-movement distance. If the Shove forces the target against a wall, the target takes Unarmed Strike damage. If the Shove forces the target against another Actor, both Actors take Unarmed Strike damage. The exact forced-movement distance, hazard, ledge, and other collision procedures remain open.

### Disarm

**Cost:** 1 Action.

Disarm is a baseline maneuver that attempts to make a held item unavailable, dropped, displaced, or subject to retrieval. Its exact check, defense, item-placement, and retrieval procedure remain open.

### Rally

**Cost:** 1 Action.  
**Access:** Leadership or Diplomacy.

Rally applies the Rallied Condition. Its targeting, range, and application procedure remain open.

### Intimidate

**Cost:** 1 Action.  
**Access:** Intimidation.

Intimidate applies the Shaken Condition. Its targeting, range, immunity, and application procedure remain open.

### Taunt

**Cost:** 1 Action.  
**Access:** Deception or Performance.

Taunt applies the Distracted Condition. Its targeting, range, immunity, and application procedure remain open.

### Assess

**Cost:** 1 Action.  
**Access:** Insight, Knowledge, or Lore.

Assess reveals useful information about an Actor, object, hazard, location, or ongoing effect suited to the Skill used. Insight reveals immediate behavior or focus; Knowledge reveals systematic facts and vulnerabilities; Lore reveals specific history, identity, culture, or reputation. Assess does not compel or lock a target’s future action. Its exact check and information-disclosure procedure remain open.

## 6. Strike Variants

### Power Attack

**Cost:** No Action; once per Strike; X Stamina.

X cannot exceed the creature’s Character Level, to a maximum of the higher face value of the Attribute Dice used to make the Strike. The creature makes the Strike with X Banes. On a hit, add X Damage Boxes to the Attack’s fixed damage before Damage Absorption is applied.

### Cleave

**Cost:** No Action; once per Strike.  
**Requirement:** A melee weapon.

The creature makes one Cleave Strike with 1 Bane against up to three creatures in its Reach. Resolve the Strike separately against each creature. A creature cannot be targeted more than once by the same Cleave.

### Called Shot

**Cost:** 2 Actions and 1 Stamina.

The creature makes a Strike with 1 Bane. On a hit, it chooses the Wound location and applies that location’s listed Wound Condition. A Called Shot is distinct from a Natural Critical.

## 7. State Responses

### Escape

**Cost:** 1 Action and 1 Stamina.

To end a Grapple, the creature rolls Acrobatics or Athletics against the grappler’s Martial Arts. On success, the Grapple ends.

Other sources of Restrained or Immobilized state their own Escape procedure.

### Execution

**Cost:** 2 Actions.

The creature makes a Strike against a target. If the Strike damages the target and leaves it at 0 Vitality, the target immediately dies. An Actor already at 0 Vitality has no defenses, but Execution must still deal damage after any applicable Damage Absorption.

## 8. Deferred Maneuvers

Bleed; Sunder or Damage Equipment; Pin Weapon; Entangle; Reposition, Pull, or Drag; Compel Surrender; Aim; Take Cover; Ready; and mounted maneuvers are not baseline Combat Maneuvers at this time. Their future owners are the Wound, Equipment, weapon Trait, spatial, Action Economy, social-conflict, or mount/vehicle frameworks as applicable.

## 9. Source Links

- Vocabulary and universal resolution: `../03_core_baseline_system/00_baseline_framework_glossary.md`, `../03_core_baseline_system/01_resolution_engine.md`
- Actions, Reactions, and Action costs: `../03_core_baseline_system/04_action_economy_and_turn_structure.md`
- Activity Tags and Skill access: `../03_core_baseline_system/09_domains_skills_activities_and_crafting.md`
- Defenses, Damage Absorption, Natural Criticals, and anatomical impact: `01_defenses_and_damage_modeling.md`
- Resources, Conditions, Wounds, stabilization, treatment, and recovery: `03_resources_conditions_and_wounds.md`
