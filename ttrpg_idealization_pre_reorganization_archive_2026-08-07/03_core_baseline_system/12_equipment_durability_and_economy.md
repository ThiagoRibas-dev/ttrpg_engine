# Equipment, Durability, and Economy

**Status:** Canonical framework owner; definitions remain open.  
**Scope:** Future canonical home for equipment vectors, durability, item scaling, crafting interfaces, and campaign-economic guidance.

## Equipment Traits

Weapons, armor, shields, and other items may have persistent Traits. A weapon Trait may cause an Attack to gain a corresponding Attack Tag. The shared Tag / Trait taxonomy, including Piercing, is defined in `00_baseline_framework_glossary.md`. Specific equipment Traits and their category assignments remain part of the future equipment framework.

## Baseline Armor Damage Absorption

Armor applies fixed post-hit Damage Absorption to an eligible physical or kinetic Attack:

| Armor category | Damage Absorption |
|---|---:|
| Unarmored | 0 |
| Light Armor | 2 |
| Medium Armor | 3 |
| Heavy Armor | 4 |

Full plate is a foremost example of Heavy Armor. Specific armor entries within a category may have distinct Traits, requirements, penalties, materials, Durability, or other explicit properties, but use the category’s listed baseline Damage Absorption unless they say otherwise.

Armor may reduce an Attack’s Damage Boxes to 0. Penetration, Piercing, Armor-Piercing, and other exceptions are governed by their own rules when defined.

## Equipment Durability

Each item has a maximum number of **Durability points** determined by that item. Each Magical Effect on an item increases its maximum Durability by 1.

### Item States

```text
Damaged:
  The item has at least 1 Durability and performs its normal function
  unless a specific rule says otherwise.

Broken:
  At 0 Durability, the item is Broken and cannot perform its normal function.
```

There are no universal intermediate Durability thresholds. An item may state an additional threshold only when its specific procedure requires one.

### Simple Repair

With the appropriate tools and the Competency Rank required by the item’s recipe, **Simple Repair** automatically restores 1 Durability per minute, up to the item’s maximum Durability. Simple Repair may be performed during a Short Breather.

### Broken Repair

Repairing a Broken item requires:

```text
The relevant Craft — X specialty.
The materials stated by the item’s recipe.
A Craft check using the item recipe’s Difficulty Vector.
The recipe’s stated repair time and special requirements.
```

An item recipe states the Durability restored by Broken Repair. Its repair materials are less than the materials required to create the item from scratch unless the item explicitly says otherwise.

Craft, magic, or another explicit effect may repair an item only as its specific rule states.

There is no current universal procedure for Durability expenditure, replacement, Sunder, armor sacrifice, or magical-item strain. Those subjects are deferred.

## Current Refactor Scope

This file establishes ownership only. It does not finalize equipment rules, item catalogues, wealth guidance, or crafting procedures.

Future framework work may address:

- Weapon Damage Dice and Traits.
- Armor, shields, and Damage Absorption interaction.
- Equipment Durability Slots.
- Masterwork, magical, and special-material scaling.
- Repair, replacement, and crafting interfaces.
- Equipment permissions and requirements.
- Wealth, availability, upkeep, and expected equipment bands.

These remain TBD and are tracked in the Outstanding Definitions Index. The current provisional fully equipped progression used for Phase 1 probability calibration is documented in `../02_comparative_system_analysis/13_probability_band_calibration.md`; revisit that artifact when equipment framework work begins. They must not be resolved as part of the documentation refactor.

## Related Canonical Documents

- Resolution vocabulary and procedures: `00_baseline_framework_glossary.md`, `01_resolution_engine.md`
- Attributes and derived statistics: `02_attributes_and_derived_statistics.md`
- Actions and spatial rules: `04_action_economy_and_turn_structure.md`, `05_spatial_and_distance_engine.md`
- Combat and Damage Absorption: `../04_simulationist_subsystems/01_defenses_and_damage_modeling.md`
- Skills and Craft: `09_domains_skills_activities_and_crafting.md`
- Current open definitions: `../06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md`
