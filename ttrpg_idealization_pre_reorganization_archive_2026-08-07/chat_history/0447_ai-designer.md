---
turn: 447
role: "AI-Designer"
source: chat_history.json
---

# Turn 447 — AI-Designer

Explored
4 reads
Read
03_resources_conditions_and_wounds.md
Read
02_attributes_and_derived_statistics.md
Read
10_magic_schools_traditions_and_spellcasting.md
Read
12_equipment_durability_and_economy.md
Resource Framework Recap

The current resource architecture is divided cleanly between capacity derivation and resource procedure.

Capacity derivation

Canonical owner:

text
03_core_baseline_system/02_attributes_and_derived_statistics.md

This file establishes where resource capacity comes from.

Expenditure, depletion, recovery, and conditions

Canonical owner:

text
04_simulationist_subsystems/03_resources_conditions_and_wounds.md

This file is intended to define how resources are spent, depleted, recovered, and affected by Conditions and Wounds.

Magic-specific resource use

Canonical owner:

text
03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md

This file defines what Essence and Spell Slots are used for in relation to magic, while the Resources subsystem should own recovery and depletion consequences.

1. Vitality
Current derivation

The Attributes file establishes:

text
Vitality = STR + CON

The underlying capacity calculation uses the relevant Attribute Die face values.

Current role

Vitality represents:

Physical endurance.
Minor injury.
Shock.
Attrition.
Damage before serious Wounds occur.
Current consequences

The Defense/Damage subsystem establishes that:

Successful impacts may cause Vitality loss.
Natural Criticals produce greater Vitality consequences.
Called Shots produce standard Vitality consequences plus a selected anatomical Wound.
Wounds can also occur through severe impacts or Vitality depletion.
Still open
Exact damage-to-Vitality procedure.
Whether all successful impacts reduce Vitality.
Damage absorption outcomes.
Vitality at zero.
Stabilization.
Death and dying procedures.
Recovery rates.
Healing item and spell interaction.
Whether Vitality recovers fully during a Long Rest or requires additional treatment.

Relevant files:

text
03_core_baseline_system/02_attributes_and_derived_statistics.md
04_simulationist_subsystems/01_defenses_and_damage_modeling.md
04_simulationist_subsystems/03_resources_conditions_and_wounds.md
2. Stamina
Current derivation

The Attributes file states that Stamina is derived primarily from Constitution.

The current working conceptual basis is:

text
Stamina capacity is governed by CON.

The exact formula is intentionally delegated to the resource framework.

Current role

Stamina represents:

Physical exertion.
Breath.
Balance.
Active-defense fatigue.
Martial effort.
Emergency physical action.
Physical Die Step-Up expenditure.
Current possible expenditures

The Resources document lists possible uses:

Active Parry or Evasion beyond the normal Reaction allowance.
Physical Die Step-Up.
Martial Surges.
Emergency movement or reactions.
Physical shock absorption where explicitly permitted.
Current recovery concepts

Possible recovery events include:

Short Breather.
Long Rest or Camp.
Medical intervention.
Other in-world rest or recovery procedures.
Still open
Exact Stamina capacity formula.
Whether Character Level or Class adds capacity.
Whether Stamina is derived solely from CON or also DEX.
Cost of active defense beyond Free Guard.
Cost of physical Die Step-Up.
Whether repeated actions consume Stamina.
Whether Stamina can fuel multiple actions in one turn.
Consequences of Stamina reaching zero.
Whether Stamina zero prevents all active defense or only specific defenses.
Recovery amount after a Short Breather.
Recovery amount after a Long Rest.
Whether wounds reduce maximum Stamina or only current Stamina.

Relevant files:

text
03_core_baseline_system/02_attributes_and_derived_statistics.md
03_core_baseline_system/04_action_economy_and_turn_structure.md
04_simulationist_subsystems/03_resources_conditions_and_wounds.md
3. Essence
Current derivation

Essence is derived from the Wisdom/Intelligence resource framework.

Conceptually:

text
Essence = WIS + INT

The exact capacity presentation is still subject to resource-system implementation.

Current role

Essence is the magical and supernatural exertion resource.

It may power:

0th-Circle spells.
Cantrips and orisons.
Metamagic.
Casting stability.
Emergency casting.
Turn or Rebuke Undead.
Smites.
Devotion Feats.
Other supernatural Class, Feat, Ancestry, Tradition, or Equipment effects.
Future Psychic/Psionic disciplines.
Current relationship to Spell Slots

Essence and Spell Slots are separate resources:

text
Spell Slots:
  Daily Vancian spell capacity.

Essence:
  Flexible supernatural exertion and spell-support resource.

Ordinary prepared spells consume Spell Slots. Essence is reserved for the additional magical or supernatural uses defined by the specific effect.

Still open
Exact Essence capacity.
Whether Essence scales with Character Level.
Whether Classes add Essence.
Whether Traditions add Essence.
Exact cost of 0th-Circle spells.
Metamagic costs.
Casting-stability costs.
Emergency-casting costs.
Whether Essence is required for concentration or sustained spells.
Essence recovery after Short Breather.
Essence recovery after Meditation.
Essence recovery after Long Rest.
Consequences of Essence reaching zero.
Whether Essence depletion causes fatigue, magical instability, or simply disables further Essence abilities.
Interaction with future Psychic/Psionic power.

Relevant files:

text
03_core_baseline_system/02_attributes_and_derived_statistics.md
03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md
04_simulationist_subsystems/03_resources_conditions_and_wounds.md
4. Spell Slots
Current role

Spell Slots are the daily Vancian resource.

The system uses:

One shared pool.
Spell Slots organized by Spell Circle.
One universal preparation system.
Fixed spell lists by Tradition.
Class and Prestige Class acquisition methods.
Spell Slot Progression derived from level-by-level class-table advancements.
Current ownership
Slot progression
text
03_core_baseline_system/06_leveling_and_tier_progression.md
Preparation and acquisition
text
03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md
Resource recovery
text
04_simulationist_subsystems/03_resources_conditions_and_wounds.md
Still open
Exact preparation duration.
Number of spells prepared.
Number of spells learned per Class or Prestige Class level.
Duplicate spell acquisition.
Downtime research.
Scroll learning.
Divine or institutional acquisition.
Spell Slot recovery.
Whether slots recover only after a Long Rest.
Whether any Classes, Feats, or Features recover individual slots.
Whether 0th-Circle spells are prepared or entirely Essence-based.
5. Equipment Durability
Current role

Equipment Durability is an item-based resource rather than a character Attribute resource.

It may govern:

Item damage.
Armor sacrifice.
Shield Block.
Sunder.
Magical item strain.
Repair and replacement.
Material quality.
Current owner
text
03_core_baseline_system/12_equipment_durability_and_economy.md

That file is currently only an ownership scaffold.

Current calibration reference

The provisional fully equipped progression is documented in:

text
02_comparative_system_analysis/13_probability_band_calibration.md

It is explicitly not finalized equipment canon.

Still open
Number of Durability Slots by item type.
Material progression.
Masterwork equipment.
Magical equipment.
Shield Durability.
Armor Durability.
Repair.
Replacement.
Sunder.
Item sacrifice.
Whether Durability recovers during downtime.
Whether magical repair costs Essence, money, materials, or time.
Wealth and equipment access by level.
6. Provisions

Provisions are listed as a possible campaign resource.

They may represent:

Food.
Water.
Travel supplies.
Camp supplies.
Ammunition or other consumables, if later included.
Forced-march and environmental survival pressure.
Current status

The category exists conceptually, but there is no complete canonical procedure yet.

Still open
Whether Provisions are tracked individually or as abstract units.
Consumption by Character Size.
Forced March costs.
Foraging.
Weather and environmental costs.
Camp requirements.
Interaction with Survival.
Interaction with Wealth and equipment.
Whether provisions affect Stamina, Vitality, or Conditions.

Relevant files:

text
03_core_baseline_system/09_domains_skills_activities_and_crafting.md
04_simulationist_subsystems/03_resources_conditions_and_wounds.md
7. Conditions

Conditions are not necessarily resource pools, but they affect resource use and recovery.

The current framework allows Conditions to impose:

Banes.
Die Step-Downs.
Action restrictions.
Movement restrictions.
Reaction restrictions.
Spellcasting restrictions.
Resource-expenditure restrictions.
Explicit Permissions or prohibitions.

Examples include:

Blinded.
Deafened.
Exhausted.
Confused.
Prone.
Restrained.
Shaken or Frightened.
Concussed.
Bleeding.
Disabled limbs.
Still open
Complete Condition catalogue.
Duration.
Stacking.
Removal.
Interaction with resources.
Whether Conditions reduce current resources, maximum resources, or only permissions.
Whether Stamina zero is a Condition.
Whether Essence zero creates a Condition.

Canonical owner:

text
04_simulationist_subsystems/03_resources_conditions_and_wounds.md
8. Wounds
Current division
Defense/Damage subsystem

Determines:

Whether a Wound is inflicted.
Which anatomical location is affected.
Natural Critical location.
Called Shot location.
Damage Absorption interaction.
text
04_simulationist_subsystems/01_defenses_and_damage_modeling.md
Resources/Conditions subsystem

Determines:

Ongoing Wound consequences.
Treatment.
Stabilization.
Recovery.
Wound severity.
Relationship to Vitality and other resources.
text
04_simulationist_subsystems/03_resources_conditions_and_wounds.md
Still open
Exact Wound severity categories.
Wound stacking.
Wound recovery.
Medical treatment.
Surgery.
Magical healing.
Concussion and disabled-limb duration.
Death and dying.
Vitality-zero behavior.
Wound interaction with Stamina and Essence.
9. Rabble and Underlings

Rabble and Underlings use simplified resource and injury procedures.

The current framework intends:

Rabble to avoid full Vitality and Wound bookkeeping.
Underlings to use simplified durability or defeat boxes.
Iconic Champions to use full resource and injury procedures.
Still open
Exact Rabble defeat threshold.
Underling box structure.
Underling Morale.
Underling Stamina and Reactions.
Whether Rabble use resources at all.
How Underling Wounds are represented.
How boss resources differ from PC resources.
Current Resource Ownership
text
02_attributes_and_derived_statistics.md:
  Capacity derivation.

03_resources_conditions_and_wounds.md:
  Spending, depletion, recovery, Conditions, Wounds, and simplified enemies.

10_magic_schools_traditions_and_spellcasting.md:
  Spell Slots, Essence uses, spell preparation, and spell acquisition.

12_equipment_durability_and_economy.md:
  Equipment Durability and item-based resources.

01_defenses_and_damage_modeling.md:
  Defense, Damage Absorption, impact, Criticals, Called Shots, and Wound triggering.
Main Open Questions for the Next Resource Pass

The next design work should probably focus on these questions in order:

What is the exact capacity formula for Stamina?
What is the exact capacity formula for Essence?
What resources recover on a Short Breather?
What resources recover on a Long Rest?
What happens when Stamina reaches zero?
What happens when Essence reaches zero?
What happens when Vitality reaches zero?
Which effects spend Stamina versus Essence?
Which Wounds reduce or restrict resources?
How do equipment Durability and repair interact with recovery?
How are Spell Slots recovered?
Which resource procedures apply to Rabble, Underlings, and bosses?

The current framework is therefore well organized, but deliberately incomplete. The categories and ownership are established; the actual expenditure, depletion, recovery, and zero-state procedures remain the next major resource-design task.
