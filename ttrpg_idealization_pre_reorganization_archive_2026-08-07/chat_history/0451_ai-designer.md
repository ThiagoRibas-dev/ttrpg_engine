---
turn: 451
role: "AI-Designer"
source: chat_history.json
---

# Turn 451 — AI-Designer

We modeled Vitality as an Attribute-derived capacity, primarily using Strength and Constitution:

text
Base Vitality = STR + CON

In practice, that means using the maximum face values of the relevant Attribute Dice.

Example:

text
STR d8 + CON d10
→ 8 + 10
→ 18 Base Vitality
Current ownership

The derivation belongs to:

text
03_core_baseline_system/02_attributes_and_derived_statistics.md

That file establishes the Attribute relationship but delegates spending, depletion, recovery, and Wound consequences to:

text
04_simulationist_subsystems/03_resources_conditions_and_wounds.md
What Vitality represents

Vitality is the actor’s general physical endurance and capacity to remain functional despite:

Scrapes.
Blows.
Shock.
Minor injuries.
Attritional damage.
Environmental harm.

It is separate from concrete Wounds.

What is still open

The framework has not yet finalized:

Class additions to Vitality.
Ancestry or size modifiers.
Level-based Vitality growth.
Equipment effects on Vitality.
Exact damage-to-Vitality procedures.
Vitality-zero consequences.
Stabilization and death.
Healing and recovery rates.
Whether Wounds reduce maximum Vitality or only impose Conditions.

So the current model is:

text
Attributes:
  Establish Base Vitality.

Class, Ancestry, Feats, and other content:
  May add or modify Vitality through explicit progression.

Damage and Wounds subsystem:
  Defines how Vitality is lost and recovered.
