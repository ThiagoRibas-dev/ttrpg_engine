---
turn: 449
role: "AI-Designer"
source: chat_history.json
---

# Turn 449 — AI-Designer

I like this direction. It is more flexible than a Warrior/Mage matrix because it treats Stamina and Essence as independent progression vectors.

A class can therefore be:

text
Good Stamina / Bad Essence
Bad Stamina / Good Essence
Good Stamina / Good Essence
Medium Stamina / Medium Essence
Bad Stamina / Bad Essence

A Monk could have:

text
Good Stamina
Good Essence
No Spell Slots

That would represent exceptional internal discipline without making the Monk a conventional Vancian caster.

Suggested Starting Model
1. Attribute-Based Base Capacity

Use paired Attributes to establish each resource’s natural reserve.

Stamina
text
Base Stamina Capacity = STR + CON

This represents:

Muscular reserve.
Structural resilience.
Breath and endurance.
Ability to exert force repeatedly.
Essence
text
Base Essence Capacity = INT + WIS

This represents:

Mental structure.
Magical comprehension.
Spiritual discipline.
Ability to channel or contain supernatural force.

This mirrors the existing Attribute logic and keeps the two resources conceptually distinct:

text
Stamina:
  Physical reserve.

Essence:
  Mental, magical, and spiritual reserve.

Charisma can still influence specific Traditions or supernatural effects without being part of the universal Essence formula.

2. Independent Class Progressions

Every Class and Prestige Class gets two separate progression columns:

text
Stamina Advancement
Essence Advancement

Each uses one of:

text
Good
Medium
Bad
None

These are not combined into a Warrior/Mage class matrix. They are selected independently.

Example class profiles
Class Concept	Stamina	Essence	Spell Slots
Fighter	Good	Bad	None
Wizard	Bad	Good	Good
Cleric	Medium	Good	Good
Paladin	Good	Medium	Medium
Rogue	Medium	Bad	None
Monk	Good	Good	None or Limited
Alchemist	Medium	Medium	None
Warlock-style class	Medium	Good	Limited or special
Commoner	Bad	Bad	None

Spell Slots remain a separate progression from Essence. A character can have:

text
Good Essence
No Spell Slots

or:

text
Good Spell Slots
Medium Essence
3. Suggested Advancement Cadences

A simple starting point would mirror the Spell Slot Advancement concept.

Good Resource Progression
text
+2 capacity at Level 1
+1 capacity every level afterward

Cumulative class contribution:

Class Level	Good Contribution
1	2
2	3
3	4
4	5
5	6
9	10
13	14
17	18
20	21
Medium Resource Progression
text
+1 capacity at Level 1
+1 capacity every 2 class levels afterward

Cumulative class contribution:

Class Level	Medium Contribution
1	1
2	1
3	2
4	2
5	3
8	4
9	5
12	6
16	8
20	10
Bad Resource Progression
text
+1 capacity at Level 1
+1 capacity every 4 class levels afterward

Cumulative class contribution:

Class Level	Bad Contribution
1–4	1
5–8	2
9–12	3
13–16	4
17–20	5
None
text
No class contribution.

The exact numbers are provisional. The important architectural decision is that the advancement cadences are independent.

4. Example Characters

Assume:

text
STR d8
CON d8
INT d8
WIS d8

Then:

text
Base Stamina = 16
Base Essence = 16
Fighter 5
text
Stamina:
  Base 16 + Good Class Contribution 6 = 22

Essence:
  Base 16 + Bad Class Contribution 2 = 18

Spell Slots:
  None

This character has plenty of physical exertion capacity but can still possess some supernatural reserve for Feats or special abilities.

Wizard 5
text
Stamina:
  Base 16 + Bad Class Contribution 2 = 18

Essence:
  Base 16 + Good Class Contribution 6 = 22

Spell Slots:
  Good Spell Slot Progression
Monk 5
text
Stamina:
  Base 16 + Good Class Contribution 6 = 22

Essence:
  Base 16 + Good Class Contribution 6 = 22

Spell Slots:
  None

The Monk has strong capacity for:

Physical Die Step-Ups.
Defensive exertion.
Martial techniques.
Internal or supernatural disciplines.
Essence-powered abilities.
Cleric/Wizard 4/4
text
Stamina:
  Cleric Medium contribution + Wizard Bad contribution

Essence:
  Cleric Good contribution + Wizard Good contribution

Spell Slots:
  Combined Spell Slot Advancements from both classes

The precise multiclass combination remains a later calibration issue, but the architecture is straightforward: each class contributes independently to each resource track.

5. What Good, Medium, and Bad Mean

The labels describe capacity growth, not resource identity.

text
Good Stamina:
  The class is designed to exert itself frequently.

Good Essence:
  The class is designed to fuel many supernatural abilities.

Bad Stamina:
  The class must conserve physical exertion.

Bad Essence:
  The class has limited supernatural reserve.


A class can be excellent in both, poor in both, or specialized in one.

6. Resource Expenditure Categories

The resources should remain distinct by fictional function.

Stamina

Possible uses:

Active Parry beyond Free Guard.
Physical Die Step-Up.
Martial Surges.
Emergency movement.
Physical resistance.
Certain combat maneuvers.
Forced Marching.
Athletics exertion.
Essence

Possible uses:

0th-Circle spells.
Metamagic.
Casting stability.
Emergency casting.
Turn or Rebuke Undead.
Smites.
Devotion Feats.
Monk disciplines.
Psychic/Psionic abilities.
Supernatural Ancestry or Class features.

A specific effect may allow Stamina or Essence substitution, but that should be an explicit Permission.

7. Recovery Starting Point

For initial brainstorming, use distinct recovery identities:

Stamina
Recovers through a Short Breather.
May recover fully after a safe rest.
Wounds, exhaustion, and forced travel may interfere.
Essence
Recovers through meditation, preparation, prayer, sleep, or another appropriate in-world activity.
May recover more slowly or require a suitable mental/spiritual condition.
Magical disruption or psychic strain may interfere.
Spell Slots
Recover through the daily preparation/rest cycle.
Remain separate from Essence.

These recovery rules should be designed after we determine how frequently each resource is expected to be spent.

Recommended Starting Definition

Stamina and Essence are mirrored in-world resource tracks. Their base capacities derive from Attributes, while their class-derived capacities advance through independent Good, Medium, Bad, or None progression columns. Classes and Prestige Classes may combine these progressions freely. Spell Slots are a separate progression from Essence.

The main provisional numbers I would start testing are:

text
Base Stamina = STR + CON
Base Essence = INT + WIS

Good:
  +2 at Level 1, then +1 every class level.

Medium:
  +1 at Level 1, then +1 every 2 class levels.

Bad:
  +1 at Level 1, then +1 every 4 class levels.

None:
  No class contribution.

This gives us a simple starting point for probability and resource-pressure testing without creating a Warrior/Mage matrix.
