# Combat Maneuver Framework — Canonical and TBD Working Draft

**Status:** Working draft and planning index; non-canonical.  
**Purpose:** Separate the canonized baseline maneuver framework from the detailed procedures still to be designed. This document is a review aid only. Where it summarizes a rule, the linked canonical owner controls.

## 1. Canonical Owners

| Subject | Canonical owner |
|---|---|
| Maneuver catalogue, families, Action costs, resource costs, and defined maneuver procedures | `../04_simulationist_subsystems/04_combat_maneuvers.md` |
| Conditions, Wound Rolls, Social Conditions, depletion, recovery, stabilization, and treatment | `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md` |
| Attack defenses, Damage Absorption, Natural Criticals, and anatomical impact | `../04_simulationist_subsystems/01_defenses_and_damage_modeling.md` |
| Actions, Reactions, movement, and Action cost framework | `../03_core_baseline_system/04_action_economy_and_turn_structure.md` |
| Activity Tags and Skill access | `../03_core_baseline_system/09_domains_skills_activities_and_crafting.md` |

## 2. Canonized Timing Framework

```text
Round: approximately six seconds; one normal Turn per Actor.
Initiative: fixed or round-by-round Reflex Initiative; fixed-choice or round-by-round Fast-Slow Side Initiative.
Delay: move later in the current Round only in fixed-order Reflex Initiative.
Reaction: one, regained at the start of the Actor’s Turn.
Surprise: no separate surprise round; awareness controls early access to Reactions and triggered defenses.
```

## 2. Canonized Baseline Framework

### 2A. Maneuver Families

| Family | Canonical members |
|---|---|
| Triggered defenses | Deflect, Evasion |
| Reaction maneuvers | Interpose |
| Damage responses | Soften Blow, Ward Self |
| Turn Activities | Full Defense, Exert, Charge, Grapple, Trip, Shove, Disarm, Rally, Intimidate, Taunt, Assess |
| Strike variants | Power Attack, Cleave, Called Shot |
| State responses | Escape, Execution |

### 2B. Canonized Procedures

| Maneuver | Canonized procedure summary | Detail still outside this entry |
|---|---|---|
| Deflect | Triggered; 1 Stamina; use a suitable Strike against an eligible physical Attack; shield grants 1 Boon | Shield categories and detailed physical-attack applicability |
| Evasion | Triggered; 1 Stamina; roll Reflexes against an eligible Attack; Heavy Armor gives 1 Bane | Armor categories and detailed Attack applicability |
| Interpose | 1 Reaction + 2 Stamina; intercept then Deflect an Attack that can plausibly be Deflected | Targeting, Reach, and redirection procedure |
| Soften Blow | Once per Attack; each Stamina prevents 1 Damage Box after damage is determined and before Vitality is marked; 1 Damage Box remains | Fixed weapon/armor damage procedure |
| Ward Self | Once per Attack; each Essence prevents 1 Damage Box after damage is determined and before Vitality is marked; 1 Damage Box remains | Fixed effect-damage procedure; damage only |
| Full Defense | 2 Actions; until next turn, may spend up to Character Level in Stamina separately on each Deflect, Evasion, or Interpose; 1 Stamina = 1 Boon | None in its own procedure; relies on defensive-Reaction rules |
| Exert | No Action; on a STR- or DEX-based roll, spend up to Character Level in Stamina to Step-Up that many selected pool dice once; d12 may temporarily become d20 | Future playtest of broad availability |
| Charge | 2 Actions + 1 Stamina; move up to Speed against one target; at most one Strike plus one Grapple or Shove in allowed sequences; next Deflect/Evasion within 1 round gets 1 Bane | Exact movement and resolution sequence |
| Power Attack | Once per Strike; spend X Stamina, take X Banes, and on a hit add X Damage Boxes before Damage Absorption; X ≤ Character Level, to a maximum of the higher face value of the Attribute Dice used to make the Strike | Fixed weapon Damage Box / Damage Absorption procedure |
| Cleave | Once per Strike; melee weapon; 1 Bane; attack up to 3 different creatures within Reach | Multi-target Strike and Reach procedure |
| Called Shot | 2 Actions + 1 Stamina; Strike with 1 Bane; on hit choose and apply the location Wound Condition | No additional baseline rule currently required |
| Escape | 1 Action + 1 Stamina; Reflexes, Acrobatics, or Athletics against an opposed check or DC to escape a Grapple | Other restraints; exact check selection |
| Execution | 2 Actions; a damaging Execution Strike that leaves the target at 0 Vitality kills it; a target already at 0 has no defenses but retains applicable Damage Absorption | Final Attack, damage, and targeting procedure |

### 2C. Canonized Conditions and Tags

| Item | Canonical effect / definition | Owner |
|---|---|---|
| Concentrate Tag | Identifies an Activity requiring mental focus, careful magical shaping, or sustained attention | Activities document |
| Manipulate Tag | Identifies an Activity requiring physical handling or use of an object, component, weapon, shield, tool, or similar item | Activities document |
| Movement Tag | Identifies an Activity that spends movement allowance or changes position | Activities document |
| Rallied | 1 Morale Boon to next Strike, Defense Maneuver, Fortitude, or Willpower check before end of next turn | Conditions document |
| Shaken | 1 Circumstance Boon to a legal Attack targeting the affected Actor before end of its next turn | Conditions document |
| Distracted | 1 Circumstance Bane on next Strike or Defense Maneuver before end of next turn | Conditions document |

## 3. TBD Procedure Queue

The entries below are baseline maneuvers already selected as canonical, but their detailed resolution procedures have not been finalized.

### 3A. Control and position procedures

| Maneuver | Required decisions |
|---|---|
| Shove | Forced distance; terrain; hazards; ledges; and size-limit edge cases |
| Disarm | Check and defense; item placement; retrieval; shields, foci, tools, and multi-handed items |
| Charge | Exact movement requirement and target constraints; exact sequence of Strike plus Grapple/Shove; failure outcomes |
| Interpose | What can be protected; required position/reach; whether the interceptor becomes the target or merely performs a defense on its behalf |
| Cleave | Target ordering; interaction with target defeat, Reach, and multi-target Strike procedure |

### 3B. Conditions and social procedures

| Maneuver / Condition | Required decisions |
|---|---|
| Rally / Rallied | Range, target eligibility, application check, reapplication, and interaction with existing Morale effects |
| Intimidate / Shaken | Range, target eligibility, application check, immunity, repeated-use limits, and interaction with fear effects |
| Taunt / Distracted | Range, target eligibility, application check, immunity, repeated-use limits, and interaction with deception, performance, and illusions |
| Assess | Check format; difficulty; information tiers; failure and false-information outcomes; creature-stat disclosure boundaries |

### 3C. Combat-engine dependencies

| Dependency | Blocks or informs |
|---|---|
| Fixed weapon Damage Boxes | Power Attack, Execution, Soften Blow, weapon design |
| Damage Absorption and armor categories | Deflect, Evasion, Interpose, Power Attack, Execution, Soften Blow |
| Shield categories | Deflect, Interpose |
| Combat-specific defense applicability and exception rules | Deflect, Evasion, Interpose, Execution, other maneuver checks |
| Reach, adjacency, forced movement, collision, and hazards | Charge, Shove, Interpose, Cleave |
| Prone, Grabbed, Restrained, and Immobilized Conditions | Grapple, Trip, Escape |
| Item Ready/Stow/retrieval procedure | Disarm |
| Multi-target Strike procedure | Cleave |

## 4. Deferred Maneuvers

These are deliberately not baseline maneuver Activities at this time:

```text
Bleed
Sunder / Damage Equipment
Pin Weapon
Entangle
Reposition / Pull / Drag
Compel Surrender
Aim
Take Cover
Ready
Mounted maneuvers
```

Their eventual owners are the Wound, Equipment, weapon Trait, spatial, Action Economy, social-conflict, or mount/vehicle frameworks, as applicable.

## 5. Recommended Next Design Order

1. Define the fixed weapon Damage Box and Damage Absorption procedure.
2. Define Prone, Grabbed, Restrained, and Immobilized.
3. Finalize Trip, Grapple, Escape, Shove, and Disarm.
4. Finalize Attack-versus-defense procedure, shield categories, and armor categories.
5. Finalize Interpose, Charge, Cleave, and Execution edge cases.
6. Define social application procedures and Assess information tiers.
7. Run focused simulations and scenario tests before expanding the baseline list.
