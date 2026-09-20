---
turn: 133
role: "AI-Designer"
source: chat_history.json
---

# Turn 133 — AI-Designer

OD-001A — Shared Spell-Slot Progression
Current Decision Summary for Revision
1. How many spell slots does a character receive at each Character Level and High Fantasy Tier?

The system uses a modified D&D 3.5e-style spell-slot table.

The baseline reference progression is:

text
Spellcasting Progression Level 1–4:
  Trained Tier

Spellcasting Progression Level 5–8:
  Veteran Tier

Spellcasting Progression Level 9–12:
  Master Tier

Spellcasting Progression Level 13–16:
  Hero Tier

Spellcasting Progression Level 17–20:
  Legend Tier

The table’s Spellcasting Progression Level is independent of Character Level.

A full caster whose spellcasting advances once per class level has:

text
Character Level 1 = Spellcasting Progression Level 1
Character Level 2 = Spellcasting Progression Level 2
...
Character Level 20 = Spellcasting Progression Level 20

The baseline full-caster table is:

Tier	Spellcasting Progression Level	1st	2nd	3rd	4th	5th	6th	7th	8th	9th
Trained	1st	4	—	—	—	—	—	—	—	—
Trained	2nd	4	—	—	—	—	—	—	—	—
Trained	3rd	4	2	—	—	—	—	—	—	—
Trained	4th	4	2	—	—	—	—	—	—	—
Veteran	5th	5	2	2	—	—	—	—	—	—
Veteran	6th	5	3	2	—	—	—	—	—	—
Veteran	7th	5	3	2	2	—	—	—	—	—
Veteran	8th	5	3	3	2	—	—	—	—	—
Master	9th	5	4	3	2	2	—	—	—	—
Master	10th	5	4	3	3	2	—	—	—	—
Master	11th	5	4	4	3	2	2	—	—	—
Master	12th	5	4	4	3	3	2	—	—	—
Hero	13th	5	5	4	4	3	2	2	—	—
Hero	14th	5	5	4	4	3	3	2	—	—
Hero	15th	5	5	5	4	4	3	2	2	—
Hero	16th	5	5	5	4	4	3	3	2	—
Legend	17th	5	5	5	5	4	4	3	2	2
Legend	18th	5	5	5	5	4	4	3	3	2
Legend	19th	5	5	5	5	5	4	4	3	3
Legend	20th	5	5	5	5	5	4	4	4	4

This table is the Good/reference progression for class design and comparison. “Good,” “Mediocre,” and “Bad” are design labels, not necessarily player-facing mechanical categories.

The table is intentionally more generous than D&D 3.5e because this system does not grant bonus spell slots from high casting attributes.

2. How do class and modular path levels contribute without fractional caster levels or table-side arithmetic?

Classes and Prestige Classes explicitly state their Spellcasting Advancement cadence.

Examples:

text
Wizard:
  Advances Spellcasting every level.

Cleric:
  Advances Spellcasting every level.

Paladin:
  Advances Spellcasting every 2 class levels.

Eldritch Knight:
  Advances Spellcasting every 3 class levels.

Fighter:
  Does not advance Spellcasting.

The character records completed Spellcasting advancements. The total determines the character’s Spellcasting Progression Level.

For example:

text
Wizard 4:
  4 Spellcasting advancements.
  Spellcasting Progression Level 4.

Paladin 4:
  2 Spellcasting advancements.
  Spellcasting Progression Level 2.

Eldritch Knight 3:
  1 Spellcasting advancement.
  Spellcasting Progression Level 1.

The character then reads the appropriate row of the shared spell-slot table.

This is conceptually similar to SotDL’s Power, except that our progression value determines the character’s position on the slot table, rather than directly determining only the highest Spell Rank.

The calculation occurs during character advancement, not during ordinary play.

3. Should full, partial, limited, and noncasting paths use distinct discrete progression tracks?

There are no formal player-facing “Good,” “Mediocre,” or “Bad” tracks.

Those terms are design guidelines used to describe advancement cadence:

Full/reference caster: advances every class level.
Partial caster: advances every two class levels.
Limited caster: advances every three class levels or another restricted cadence.
Noncaster: does not advance Spellcasting.

Each class provides its actual advancement schedule directly.

This avoids requiring players to understand abstract fractions such as:

text
+1 caster level
+1/2 caster level
+1/3 caster level
4. When a character multiclasses, how are slot contributions combined?

Each class contributes Spellcasting advancements according to its own cadence.

The contributions are added to one shared Spellcasting Progression Level.

Examples:

text
Wizard 4 / Fighter 4:
  Wizard: 4 advancements
  Fighter: 0 advancements
  Total: Spellcasting Progression Level 4
text
Wizard 4 / Paladin 4:
  Wizard: 4 advancements
  Paladin: 2 advancements
  Total: Spellcasting Progression Level 6
text
Wizard 4 / Eldritch Knight 3:
  Wizard: 4 advancements
  Eldritch Knight: 1 advancement
  Total: Spellcasting Progression Level 5
text
Wizard 4 / Cleric 4:
  Wizard: 4 advancements
  Cleric: 4 advancements
  Total: Spellcasting Progression Level 8

All classes and Prestige Classes use the same rule. Prestige Classes differ from Base Classes through prerequisites, not through a separate multiclassing procedure.

The character has one shared slot pool determined by the final Spellcasting Progression Level.

5. Does a character’s highest Tradition Rank limit the highest slot they can use?

No.

Spellcasting Progression determines the character’s available daily spell slots.

Tradition Skills determine:

Which Tradition spells the character can access.
Which spells the character can learn or prepare.
The intrinsic scaling of those spells.
Their casting proficiency and Competency Floor.

A character may possess a high Spellcasting Progression Level while having shallow investment in a particular Tradition.

Example:

text
Spellcasting Progression Level: 10
Death: Trained
Arcane: Expert

The character receives the complete Progression Level 10 slot pool, but:

Can use only Trained-scale Death spells.
Can use Expert-scale Arcane spells.
Cannot access Death spells requiring deeper Tradition mastery.
May use higher-circle slots to cast lower-circle spells, subject to the spell rules.

This is intentional. Spellcasting capacity and Tradition mastery are separate vectors.

6. Do advanced classes and Prestige Classes increase slot quantity, maximum Spell Rank, or both?

A class or Prestige Class may provide any combination of:

Spellcasting advancements.
Tradition Skill access.
Tradition Skill advancement.
Spell acquisition.
Essence features.
Metamagic.
Special spell permissions.
Access to advanced or restricted Traditions.

Spellcasting advancement increases the character’s position on the shared slot table. It does not automatically increase Tradition mastery.

A Prestige Class may therefore specialize in:

text
Advancing Spellcasting.

or:

text
Advancing Death Tradition.

or:

text
Granting Time Tradition access.

or:

text
Providing Essence and metamagic features.

These do not need to advance together.

The class entry should state its Spellcasting Advancement cadence explicitly.

7. How does Mythic advancement expand or transform the shared slot pool?

Mythic advancement does not automatically add new ordinary spell slots beyond the Level 20 table.

Instead, Mythic advancement grants access to:

Epic Traditions.
Epic Spells.
Mythic spell effects.
Mythic versions of existing Traditions.
Cosmic or divine magical permissions.
Special uses for existing high-circle slots.

Epic Spells use the character’s existing shared Spell Slots, subject to their requirements.

For example:

text
Epic Creation Spell:
  Requires access to the Creation Tradition.
  Requires Legendary or Mythic Tradition Competency.
  Consumes a 7th-, 8th-, or 9th-circle slot.
  May also require Essence, a ritual, or a unique component.

Mythic advancement expands what magic can be done, not merely how many ordinary slots the character receives.

Consolidated OD-001A Decision
text
Spellcasting Progression Level:
  A derived value that determines position on the shared slot table.

Spellcasting Advancement:
  A discrete class-based advancement granted at a defined cadence.

Full caster:
  +1 Spellcasting Advancement per class level.

Partial caster:
  +1 Spellcasting Advancement every 2 class levels.

Limited caster:
  +1 Spellcasting Advancement every 3 class levels,
  or another explicitly defined restricted cadence.

Noncaster:
  No Spellcasting Advancement.

Multiclassing:
  Add all completed Spellcasting Advancements from all classes
  and Prestige Classes into one shared Progression Level.

Tradition Skills:
  Determine spell access, preparation eligibility, and intrinsic scaling.

Spell Circles:
  Determine spell complexity and slot cost.

Shared slots:
  One universal daily pool.

Mythic:
  Adds Epic Traditions and Spells using the existing slot framework.

This is the revised version of your OD-001A decisions, with the table and multiclassing model represented correctly.
