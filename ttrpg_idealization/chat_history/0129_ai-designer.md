---
turn: 129
role: "AI-Designer"
source: chat_history.json
---

# Turn 129 — AI-Designer

You’re right—I was conflating High Fantasy Tier, Spellcasting Progression Level, and Spell Circle. The table is clear when those are treated as separate axes.

Correct interpretation
Spellcasting Progression Level

This is the position on the spell-slot table.

A full caster whose spellcasting advances at the same rate as their character level has:

text
Character Level 1 → Spellcasting Progression Level 1
Character Level 2 → Spellcasting Progression Level 2
...
Character Level 20 → Spellcasting Progression Level 20

Therefore:

text
Level 1 Wizard:
  Spellcasting Progression Level 1
  4 first-circle slots

Level 4 Wizard:
  Spellcasting Progression Level 4
  4 first-circle slots
  2 second-circle slots

Level 5 Wizard:
  Spellcasting Progression Level 5
  5 first-circle slots
  2 second-circle slots
  2 third-circle slots

Level 8 Wizard:
  Spellcasting Progression Level 8
  5 first-circle slots
  3 second-circle slots
  3 third-circle slots
  2 fourth-circle slots
High Fantasy Tier

The Tier label describes the character’s overall scope, not a separate spell-slot progression:

High Fantasy Tier	Character Levels	Full-Caster Progression Levels	Spell-Circle Access
Trained	1–4	1–4	1st and 2nd
Veteran	5–8	5–8	3rd and 4th
Master	9–12	9–12	5th and 6th
Hero	13–16	13–16	7th and 8th
Legend	17–20	17–20	9th
Mythic	21+	Epic access	Epic Traditions and Spells

So your table is a modified D&D 3.5e-style full-caster table with:

More early slots.
No ability-score bonus slots.
2nd-circle access by Progression Level 3.
3rd-circle access by Progression Level 5.
4th-circle access by Progression Level 7.
5th-circle access by Progression Level 9.
6th-circle access by Progression Level 11.
7th-circle access by Progression Level 13.
8th-circle access by Progression Level 15.
9th-circle access by Progression Level 17.

That is now completely clear.

Implications for Multiclassing

The important value is the character’s Spellcasting Progression Level, not their High Fantasy Tier.

Examples:

text
Level 8 Wizard:
  Character Level: 8
  Spellcasting Progression Level: 8
  Uses the Level 8 row.

Wizard 4 / Fighter 4:
  Character Level: 8
  Spellcasting Progression Level: 4
  Uses the Level 4 row.

The second character is Veteran by overall character level but only has Trained-level spell-slot capacity.

Full caster multiclassing

If both classes advance the same full Spellcasting Progression:

text
Wizard 4 / Cleric 4:
  Spellcasting Progression Level: 8
  Uses the Level 8 row.

There is one shared spell-slot pool. The character does not have separate Wizard and Cleric slots.

Prestige Classes

Prestige Classes work identically to Base Classes:

text
Wizard 4 / Archmage 4:
  If Archmage advances Spellcasting Progression,
  total Progression Level becomes 8.

The Prestige Class requirement is what prevents Archmage from being taken at Level 1; its spellcasting contribution follows the same rules once entered.

Corrected Meaning of Mediocre and Bad Tracks

The Mediocre and Bad tracks are not additional tiers layered on top of the Good table. They are alternate slot tables indexed by Spellcasting Progression Level.

For example:

text
Wizard 8:
  Good Spellcasting Progression Level 8.

Paladin 8:
  Mediocre Spellcasting Progression Level 8.

Fighter 8:
  No Spellcasting Progression.

All three characters are Level 8 and Veteran, but they have different magical capacities because they use different progression tracks.

The table index remains:

text
Spellcasting Progression Level 1–20

The track changes the number and availability of slots at each index.

Corrected OD-001A Structure

The questions now resolve into this architecture:

Good Spellcasting Progression: the supplied table.
Mediocre Spellcasting Progression: a slower/reduced table using the same Progression Level index.
Bad Spellcasting Progression: an even slower/restricted table using the same index.
No Spellcasting Progression: no ordinary spell slots.
Spellcasting Progression Level: a class-derived value that may be lower than Character Level for multiclass characters.
Spell Circle: the level of the spell and the slot consumed.
Tradition Rank: determines which spells the character can access and how those spells intrinsically scale.
High Fantasy Tier: describes overall campaign scope and does not itself determine slot count.
Mythic: adds access to Epic Traditions and Spells, using the existing ordinary slot framework unless a future Mythic rule says otherwise.

The remaining specific question is now much narrower:

How exactly do different class progression tracks contribute to one Spellcasting Progression Level when multiclassing—for example, Wizard 4 / Paladin 4?

But the table itself is now understood correctly: Progression Level 4 is the top of Trained, Progression Level 8 is the top of Veteran, Progression Level 12 is the top of Master, and so on.
