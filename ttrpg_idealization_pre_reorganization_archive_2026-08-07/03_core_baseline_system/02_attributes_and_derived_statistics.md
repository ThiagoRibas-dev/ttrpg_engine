# Attributes and Derived Statistics

**Status:** Canonical foundation for Attributes and directly derived statistics.  
**Scope:** Attribute definitions, Attribute Dice, advancement, resource capacities, and paired defense derivations. Procedures for using those values belong to the relevant subsystem owners.

## 1. Core Attributes

Every actor has six core Attributes rated as Step Dice:

```text
d4 → d6 → d8 → d10 → d12
```

The ordinary Attribute Die ceiling is `d12`. Former permanent over-cap Attribute notation is deprecated. Exert may temporarily Step-Up an affected d12 die to d20; it does not permanently increase an Attribute beyond d12.

| Attribute | Abbreviation | Core representation |
|---|---|---|
| Strength | STR | Muscular force, leverage, carrying power, physical momentum |
| Dexterity | DEX | Coordination, precision, balance, manual control, reflexive movement |
| Constitution | CON | Metabolic health, endurance, tissue vitality, toxin resistance |
| Intelligence | INT | Analysis, memory, spatial reasoning, technical understanding |
| Wisdom | WIS | Sensory awareness, discipline, emotional poise, perception of living or spiritual forces |
| Charisma | CHA | Personality, presence, soul identity, social and spiritual projection |

Attributes determine the relevant Die Size for a check. They do not provide linear modifiers.

## 2. Attribute Advancement

### Starting Attribute Array

At character creation, assign the following six Attribute Dice:

```text
One d8.
Three d6.
Two d4.
```

The d8 is the character’s **Primary Attribute**. The remaining five Attributes are Secondary Attributes.

### Primary Attribute Advancement

A character’s Background/Origin designates its Primary Attribute. Permanent Attribute Dice never exceed d12.

| Character Level | Primary Attribute Die |
|---:|---|
| 1–8 | d8 |
| 9–16 | d10 |
| 17–20 | d12 |

The temporary `d12 → d20` Exert exception does not permanently increase an Attribute Die.

### Secondary Attribute Score Increases

At Levels 4, 8, 12, 16, and 20, a character gains **3 Attribute Points**. Attribute Points may be invested only in Secondary Attributes.

| Attribute increase | Attribute Point cost |
|---|---:|
| d4 → d6 | 1 |
| d6 → d8 | 2 |
| d8 → d10 | 2 |
| d10 → d12 | 3 |

### Attribute Step Investment

Attribute Points are invested in a specified Secondary Attribute’s next permanent Die Step. A partial **Attribute Step Investment** remains assigned to that Attribute and its next Die Step until completed. It cannot be reassigned unless an explicit rule permits it.

When the required investment is complete, increase the Attribute Die by one step.

### Secondary Attribute Limits

- A permanent Secondary Attribute cannot exceed the character’s Primary Attribute.
- No more than one permanent Secondary Attribute may equal the character’s Primary Attribute Die.
- An Attribute Step Investment may not complete an increase that would violate either limit.
- A permanent Attribute Die cannot exceed d12.

## 3. Derived Resource Capacities

Resource capacity is measured in points. A resource’s maximum capacity equals its Attribute Base, its accumulated class-track contributions, and any explicit permanent additions. Spending, depletion, recovery, and zero-resource procedures belong to `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md`. Class-track progression and multiclass accumulation belong to `06_leveling_and_tier_progression.md`.

### Resource Values

For capacity derivation, each Attribute Die has the following **Resource Value**:

| Attribute Die | Resource Value |
|---|---:|
| d4 | 1 |
| d6 | 2 |
| d8 | 3 |
| d10 | 4 |
| d12 | 5 |

### Attribute Bases

| Resource | Attribute Base | Represents |
|---|---|---|
| Vitality | STR Resource Value + CON Resource Value | Physical capacity to remain functional under injury and attrition |
| Stamina | DEX Resource Value + CON Resource Value | Physical exertion, active defense, movement, and martial effort |
| Essence | INT Resource Value + WIS Resource Value | Magical, mental, spiritual, and supernatural exertion |

The ordinary Attribute Base range is 2 through 10. Attribute advancement changes a resource’s Attribute Base when it changes one of that resource’s contributing Attributes.

### Permanent Additions

Ancestries, Feats, Class features, and other explicit rules may permanently add resource capacity. Equipment does not ordinarily add permanent personal resource capacity; its distinct contribution rules belong to `12_equipment_durability_and_economy.md`.

## 4. Paired Defenses

The system uses three paired resilience defenses. Each is assembled from one die of each listed Attribute and keeps the highest face as its base paired pool:

```text
Fortitude = 1dSTR + 1dCON, keep highest
Reflexes  = 1dDEX + 1dINT, keep highest
Willpower = 1dWIS + 1dCHA, keep highest
```

### Fortitude

Resists physical and metabolic threats such as poison, disease, bodily shock, and environmental trauma.

### Reflexes

Resists threats requiring rapid physical and tactical response, such as projectiles, traps, area effects, and sudden movement hazards.

### Willpower

Resists mental, emotional, spiritual, and identity-based threats such as fear, domination, curses, and psychic intrusion.

The Defense and Damage subsystem owns the procedures for when each defense is targeted. The Resolution Engine owns the universal roll procedure.

## 5. Source-of-Truth Links

- Universal vocabulary: `00_baseline_framework_glossary.md`
- Universal resolution: `01_resolution_engine.md`
- Character and actor structure: `03_character_schema_and_actor_creation.md`
- Level and Tier advancement: `06_leveling_and_tier_progression.md`
- Pool generation and class differentiation: `07_check_pool_generation_and_class_differentiation.md`
- Defense and damage procedures: `../04_simulationist_subsystems/01_defenses_and_damage_modeling.md`
- Resource expenditure and recovery: `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md`
- Magic and Essence uses: `10_magic_schools_traditions_and_spellcasting.md`
- Equipment framework: tracked in the Outstanding Definitions Index until its canonical owner is created.
