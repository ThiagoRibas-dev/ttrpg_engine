# Defenses, Damage, and Wounds

**Status:** Canonical combat-defense and injury subsystem owner.  
**Scope:** Defensive layers, Damage Absorption, damage impact, Natural Criticals, anatomical wounds, and the relationship between attacks and defenses. Tactical maneuver procedures belong to `04_combat_maneuvers.md`.

## 1. Defensive Layers

The system does not use one universal Armor Class. The appropriate defensive layer depends on the threat:

- **Reflexes:** DEX + INT paired defense against projectiles, area effects, traps, and sudden hazards.
- **Parry:** Combat Mastery defense against physical attacks that can be actively intercepted.
- **Fortitude:** STR + CON paired defense against physical, metabolic, and bodily threats.
- **Willpower:** WIS + CHA paired defense against mental, emotional, spiritual, and identity threats.
- **Damage Absorption:** Equipment, hide, or other material protection checked after a physical or kinetic hit.

Attribute derivations belong to `../03_core_baseline_system/02_attributes_and_derived_statistics.md`. Universal opposed-check procedure belongs to `../03_core_baseline_system/01_resolution_engine.md`.

## 2. Defense Selection and Resolution

The attacker and defender use the universal opposed-check procedure. The defender wins complete ties.

### Triggered Physical Defenses

**Deflect** and **Evasion** are triggered Stamina defenses, not Reactions.

- **Deflect** answers an eligible physical Attack through a weapon, shield, body, or suitable defense.
- **Evasion** answers an eligible Attack that can be avoided through movement, footwork, positioning, or reflex.
- A defender may use one eligible triggered physical defense against an Attack or decline active defense.

### Passive Resistances

**Fortitude** and **Willpower** are passive defenses. An effect that targets one of them is resolved through the universal opposed-check procedure without requiring a Reaction or resource expenditure to make the resistance roll.

- Fortitude resists poison, disease, petrification, bodily shock, and physical transformation.
- Willpower resists fear, domination, curses, psychic effects, and spiritual intrusion.

When damage follows an effect resolved through Fortitude or Willpower, Ward Self may lower that damage. Its procedure is defined in `04_combat_maneuvers.md`.

### Combat Sequence

1. The attacker declares an Attack and its target.
2. Identify the defense or defenses the Attack can target.
3. For a physical Attack, the defender may use one eligible triggered physical defense or decline active defense. A defender who cannot or does not use an active defense does not make a triggered defense roll.
4. For a Fortitude- or Willpower-targeting effect, the defender makes the relevant passive resistance roll.
5. Resolve the applicable opposed check. The defender wins a complete tie.
6. If the Attack succeeds, apply Damage Absorption when applicable.
7. Apply Soften Blow or Ward Self when applicable.
8. Mark remaining Damage Boxes against Vitality and make a Wound Roll when required.

Specific Attacks, weapons, spells, Conditions, and Permissions may restrict, replace, bypass, or add eligible defenses.

## 3. Damage Mitigation

### Damage Absorption

Damage Absorption is a post-hit layer. It is not a universal attack-avoidance value and does not replace Deflect or Evasion.

The system uses fixed Damage Boxes rather than damage dice. Damage Absorption prevents some of an incoming physical or kinetic Attack’s fixed Damage Boxes after the Attack succeeds. The exact weapon Damage Box values, armor absorption values, categories, and special interactions remain part of the equipment and combat-calibration pass.

The canonical term is **Damage Absorption**. When damage follows a source resolved through Deflect, Evasion, or Damage Absorption, **Soften Blow** may lower that damage. Its maneuver procedure is defined in `04_combat_maneuvers.md`.

### Internal Mitigation

**Ward Self** is the distinct resource-based mitigation option for damage from effects resolved through Fortitude or Willpower. It is not armor or Damage Absorption: it represents internal, magical, or spiritual resistance to a threat that acts directly upon the actor’s inner state. Its maneuver procedure is defined in `04_combat_maneuvers.md`.

## 4. Natural Criticals

A Natural Critical is determined by the applicable weapon or effect Critical Threat Profile. It produces an exceptional impact, increased Vitality consequence, and a Wound Roll according to the current Critical and Wound rules in `03_resources_conditions_and_wounds.md`.

Natural Criticals are distinct from Called Shots; the latter is a tactical maneuver defined in `04_combat_maneuvers.md`.

## 5. Anatomical Wounds

The current anatomical framework includes locations such as:

- Head.
- Chest.
- Abdomen.
- Shield or off-arm.
- Weapon arm.
- Legs.

Severe Wounds may produce conditions such as:

- Concussion.
- Winded or rib trauma.
- Bleeding.
- Disabled arm.
- Dropped weapon.
- Prone or disabled leg.

[Resources, Conditions, and Wounds](03_resources_conditions_and_wounds.md) owns Wound Rolls, ongoing Wound Conditions, treatment, stabilization, recovery, and resource interactions.

## 6. Source Links

- Vocabulary and resolution: `../03_core_baseline_system/00_baseline_framework_glossary.md`, `../03_core_baseline_system/01_resolution_engine.md`
- Attributes and paired defenses: `../03_core_baseline_system/02_attributes_and_derived_statistics.md`
- Actions and Reactions: `../03_core_baseline_system/04_action_economy_and_turn_structure.md`
- Combat maneuvers: `04_combat_maneuvers.md`
- Equipment and item framework: `../03_core_baseline_system/12_equipment_durability_and_economy.md`
- Resources, Conditions, and recovery: `03_resources_conditions_and_wounds.md`
