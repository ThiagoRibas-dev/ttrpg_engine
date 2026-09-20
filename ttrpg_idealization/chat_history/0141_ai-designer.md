---
turn: 141
role: "AI-Designer"
source: chat_history.json
---

# Turn 141 — AI-Designer

Yes—this clarification means we do not need separate Mediocre and Bad slot tables.

We need one canonical table: the Reference Spell Slot Progression. Classes simply advance through that table at different rates.

Recommended Terminology

I recommend replacing “Spellcasting Slot Progression” with:

Spell Slot Progression

It is direct and accurately describes what the progression controls.

Use the following terms:

Spell Slot Advancement: An entry on a class table granting one advancement.
Spell Slot Progression Level: The character’s accumulated position on the Reference Spell Slot Progression.
Reference Spell Slot Progression: The universal table showing slots at Progression Levels 1–20.

This does not need to be treated as an independent character statistic like an Attribute or Tradition Skill. It is a derived advancement value recorded for slot calculation.

Class table example
text
Wizard:
  Spell Slot Progression: +1 at every class level.

Paladin:
  Spell Slot Progression: +1 at class levels 2, 4, 6, 8, and 10.

Eldritch Knight:
  Spell Slot Progression: +1 at class levels 3, 6, and 9.

Fighter:
  No Spell Slot Progression advancement.

The class table—not a generic cadence statement—is authoritative.

The Three Advancement Rates
Full

Advances every class level.

text
20 class levels
→ Spell Slot Progression Level 20
→ 9th-circle slots
Mediocre

Advances every other class level.

text
10 class levels at 20th class level
→ Spell Slot Progression Level 10
Bad

Advances once every four class levels.

text
5 class levels at 20th class level
→ Spell Slot Progression Level 5

These are not rules tracks. They are design shorthand for class-table advancement patterns.

Important Correction to the Proposed Mediocre Table

Under the rule:

“Advance through the Reference Spell Slot Progression table every other class level,”

a character with 20 levels in a Mediocre-casting class reaches Progression Level 10, not Progression Level 11.

Therefore, they would use the Reference Progression Level 10 row:

text
5 first-circle
4 second-circle
3 third-circle
3 fourth-circle
2 fifth-circle

They would not yet have sixth-circle slots.

To reach sixth-circle slots, the character must reach Reference Progression Level 11.

So the pure rates produce:

Advancement Rate	Progression Level at Class Level 20	Highest Circle
Full: every level	20	9th
Mediocre: every 2 levels	10	5th
Bad: every 4 levels	5	3rd

This is the mathematically consistent result using the current Reference table.

If we specifically want:

text
Full: 9th-circle maximum
Mediocre: 6th-circle maximum
Bad: 3rd-circle maximum

then Mediocre cannot simply be “every other level” unless it receives an additional advancement somewhere.

Possible solutions include:

Give Mediocre classes one extra Spell Slot Advancement at Level 1.
Give Mediocre classes one extra advancement at a later class level.
Make the Mediocre cadence +1 at levels 1, 2, 4, 6, 8, ..., 20.
Accept that pure Mediocre progression ends at 5th Circle.
Use a separate class feature to grant sixth-circle access without changing the slot progression.

My preferred solution is probably Option 4 unless playtesting indicates that sixth-circle access is necessary. It keeps the advancement cadence mathematically clean.

Important Correction to the Proposed Bad Table

The Bad table as written also appears to be an independent slot table rather than a direct reading of the Reference Spell Slot Progression table.

If Bad classes advance once every four class levels, then their slot results should be:

Class Level	Progression Level	Reference Slot Row
1–4	1	4 first-circle
5–8	2	4 first-circle
9–12	3	4 first-circle, 2 second-circle
13–16	4	4 first-circle, 2 second-circle
17–20	5	5 first-circle, 2 second-circle, 2 third-circle

That is the direct consequence of moving through the Reference table once per four class levels.

So a pure Bad caster at Class Level 20 would have:

text
5 first-circle slots
2 second-circle slots
2 third-circle slots

not the much larger slot values in the proposed Bad table.

If the larger Bad table is intentional, then it represents a separate slot-volume table, not simply a slower advancement through the Reference progression.

Multiclassing

The clean multiclass rule is:

Add all Spell Slot Advancements granted by all Base Classes and Prestige Classes. Use the resulting total to read the Reference Spell Slot Progression table.

Examples
Wizard 4 / Fighter 4
text
Wizard: 4 advancements
Fighter: 0 advancements

Total:
  Progression Level 4
Wizard 4 / Paladin 4
text
Wizard: 4 advancements
Paladin: 2 advancements

Total:
  Progression Level 6
Paladin 4 / Ranger 4

If both are Mediocre:

text
Paladin: 2 advancements
Ranger: 2 advancements

Total:
  Progression Level 4
Wizard 4 / Eldritch Knight 3
text
Wizard: 4 advancements
Eldritch Knight: 1 advancement

Total:
  Progression Level 5
Wizard 4 / Cleric 4
text
Wizard: 4 advancements
Cleric: 4 advancements

Total:
  Progression Level 8

There are no separate Full, Mediocre, or Bad tracks during play. Those terms describe how quickly each class table grants advancements.

Revised OD-001A Formulation
How many slots?

Use one universal Reference Spell Slot Progression table, with the current Level 1–20 values you designed.

How do classes contribute?

Each Base Class and Prestige Class has a level-by-level Spell Slot Advancement column.

Are there separate full, mediocre, and bad tracks?

No. Those are design labels:

Full: advancement every class level.
Mediocre: advancement every other class level.
Bad: advancement once every four class levels.
None: no advancement.
How does multiclassing work?

Add all completed Spell Slot Advancements from all classes and Prestige Classes. Use the total as the character’s Spell Slot Progression Level.

Does Tradition Rank limit slots?

No.

Spell Slot Progression determines daily slot volume. Tradition Skills determine:

Spell access.
Preparation eligibility.
Intrinsic spell scaling.
Tradition-specific casting competence.
Do advanced classes increase slot quantity or maximum Circle?

A class or Prestige Class may grant:

Spell Slot Advancements.
Tradition access.
Tradition advancement.
Spell acquisition.
Essence features.
Metamagic.
Epic or restricted spell permissions.

These are separate class-table benefits.

What does Mythic do?

Mythic advancement does not automatically create new ordinary slot rows. It grants Epic Traditions and Epic Spells that use the existing shared slot framework.

Recommended Canonical Wording

Spell Slot Progression: Every Base Class and Prestige Class has a level-by-level Spell Slot Advancement column. Each marked level grants one Spell Slot Advancement. Add all Spell Slot Advancements granted by all of a character’s classes. The resulting total is the character’s Spell Slot Progression Level, which determines the character’s daily shared Spell Slot pool using the Reference Spell Slot Progression table. Classes may advance Spell Slot Progression at different rates; these rates are design guidelines rather than separate player-facing tracks.

This is simpler than maintaining separate Mediocre and Bad tables and matches the intended SotDL-like model: the character’s progression value determines their position on a universal capacity table.
