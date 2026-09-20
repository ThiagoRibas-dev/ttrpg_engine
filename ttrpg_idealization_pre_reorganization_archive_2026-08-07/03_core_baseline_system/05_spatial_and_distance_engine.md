# Spatial and Distance Engine

**Status:** Canonical spatial-framework owner.  
**Scope:** Abstract Distance Tiers, exact measurement mode, movement, Reach, range, zones, and movement modes.

## 1. Distance Tiers

The game supports both exact measurements and abstract Distance Tiers.

```text
Tier 0: Close   — 0–5 ft / melee
Tier 1: Near    — 10–30 ft / 1 zone
Tier 2: Medium  — 35–60 ft / 2 zones
Tier 3: Far     — 65–120 ft / 3 zones
Tier 4: Distant — 125–300+ ft / artillery or horizon
```

The abstract mode is a spatial representation, not a numerical modifier system.

## 2. Stride

A standard Stride is one Action and normally shifts the actor one Distance Tier. In exact-measurement play, it normally moves the actor’s listed Speed, with equipment, ancestry, conditions, and movement modes modifying that movement through explicit rules.

## 3. Exact and Abstract Modes

### Exact mode

Uses feet, meters, grid squares, measured Reach, measured Areas of Effect, and exact movement distances.

### Abstract mode

Uses Distance Tiers, zones, Reach categories, and zone-based Areas of Effect. Conversion guidance should preserve the tactical relationship rather than introduce arithmetic modifiers.

## 4. Reach and Range

Reach is a weapon, ancestry, creature, or effect Trait. Range is defined by the relevant weapon, spell, ability, or equipment rule.

When an attack or effect exceeds its normal range, the relevant rule may impose a Bane, restrict targeting, or make the action unavailable. The universal Resolution Engine determines how any Bane is resolved.

## 5. Movement Modes

Climbing, swimming, flying, burrowing, forced marching, and similar capabilities are movement modes or Activities. They may be granted by Ancestry, Equipment, Feat, Spell, Skill, Class, or creature design.

They are not automatically universal Skills.

## 6. Spatial Positioning

Flanking, cover, high ground, prone positioning, difficult terrain, concealment, and line of sight are represented through spatial conditions and explicit Boons, Banes, Requirements, or Permissions.

The specific tactical effect belongs to the relevant Combat, Equipment, Spell, Condition, or Activity rule. This document owns the spatial meaning of the situation.

## 7. Source Links

- Action costs and turn budget: `04_action_economy_and_turn_structure.md`.
- Universal checks and Boons/Banes: `01_resolution_engine.md`.
- Defenses and Damage Absorption: `../04_simulationist_subsystems/01_defenses_and_damage_modeling.md`.
- Spell Areas and movement effects: `10_magic_schools_traditions_and_spellcasting.md`.
- Equipment range, Reach, and movement: `12_equipment_durability_and_economy.md`.
