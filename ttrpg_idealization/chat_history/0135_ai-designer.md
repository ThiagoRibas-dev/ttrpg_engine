---
turn: 135
role: "AI-Designer"
source: chat_history.json
---

# Turn 135 — AI-Designer

Agreed. The class table should show Spellcasting Advancement level by level, rather than using a shorthand cadence in the class description.

That keeps the progression transparent and makes multiclassing straightforward.

Class Table Treatment

Every class and Prestige Class should include a dedicated column:

text
Spellcasting Progression

Each class level explicitly shows whether that level grants a Spellcasting Progression advance.

Wizard Example
Wizard Level	Spellcasting Progression Level
1	1
2	2
3	3
4	4
5	5
6	6
7	7
8	8
9	9
10	10

A Wizard advances spellcasting every level, but the table makes that visible rather than requiring the player to infer it.

Paladin Example
Paladin Level	Spellcasting Progression Advances	Total Contribution
1	—	0
2	✓	1
3	—	1
4	✓	2
5	—	2
6	✓	3
7	—	3
8	✓	4
9	—	4
10	✓	5

The character does not track a fractional caster level. They simply record the total number of Spellcasting Progression advances granted by their Paladin levels.

Eldritch Knight Example
Eldritch Knight Level	Spellcasting Progression Advances	Total Contribution
1	—	0
2	—	0
3	✓	1
4	—	1
5	—	1
6	✓	2
7	—	2
8	—	2
9	✓	3
10	—	3
Multiclass Example
text
Character:
  Wizard 4 / Paladin 4
Wizard contribution
text
Wizard Level 1: +1
Wizard Level 2: +1
Wizard Level 3: +1
Wizard Level 4: +1

Total Wizard contribution: 4
Paladin contribution
text
Paladin Level 1: +0
Paladin Level 2: +1
Paladin Level 3: +0
Paladin Level 4: +1

Total Paladin contribution: 2
Final result
text
Spellcasting Progression Level: 6

The character uses the Progression Level 6 row of the shared slot table.

Recommended Class Table Structure

The Spellcasting Advancement column should appear beside other level-by-level progression tracks:

Level	Vitality	Combat	Saves	Skill Allocations	Spellcasting Progression	Class Features
1	Good	Good	Good	2	+1	Arcane Initiation
2	Good	Good	Good	1	+1	Spell Research
3	Good	Good	Good	1	+1	Tradition Feat
4	Good	Good	Good	1	+1	Ability Feature

For a Paladin:

Level	Vitality	Combat	Saves	Skill Allocations	Spellcasting Progression	Class Features
1	Good	Good	Good	1	—	Divine Initiation
2	Good	Good	Good	1	+1	Smite
3	Good	Good	Good	1	—	Divine Tradition Feature
4	Good	Good	Good	1	+1	Sacred Path Feature

This has several advantages:

Advancement is visible.
Multiclassing is easy to audit.
Prestige Classes use the same table format.
No fractional spellcasting calculations are required.
Class identity is preserved.
The player can see exactly what each level contributes.
Prestige Classes

Prestige Classes should use the identical format.

text
Archmage:
  +1 Spellcasting Progression at every level.

Eldritch Knight:
  +1 Spellcasting Progression at levels 3, 6, and 9.

Death Knight:
  +1 Spellcasting Progression at levels 2, 4, 6, 8, and 10.

The prerequisite structure prevents a Prestige Class from being selected at Level 1. Once selected, its table contributes exactly like any Base Class table.

Terminology

I recommend distinguishing:

Spellcasting Progression Advance: The +1 entry on a class table.
Spellcasting Progression Level: The character’s total accumulated advances.
Spell Slot Table: The table indexed by Spellcasting Progression Level.

Example:

text
Wizard 4 / Paladin 4

Spellcasting Progression Advances:
  Wizard: 4
  Paladin: 2

Spellcasting Progression Level:
  6

Spell Slots:
  Use Spellcasting Progression Level 6 row.

This is clearer than saying that the character has “caster level 6,” because that might be confused with Tradition Skill scaling.

The level-by-level class table should therefore be the authoritative source for Spellcasting Advancement. The class description can summarize it, but the actual advancement entries belong in the table.
