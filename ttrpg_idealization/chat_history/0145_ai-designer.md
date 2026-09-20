---
turn: 145
role: "AI-Designer"
source: chat_history.json
---

# Turn 145 — AI-Designer

This progression is much better. It solves the “invisible advancement” problem while preserving the intended advancement cadence.

1. Reference Good Progression

The revised Good table now has a meaningful change at every Progression Level:

text
Level 1 → 3 first-circle slots
Level 2 → 4 first-circle slots
Level 3 → 4 first-circle, 1 second-circle
Level 4 → 4 first-circle, 2 second-circle
Level 5 → 5 first-circle, 2 second-circle, 1 third-circle

Each advancement now provides at least one of:

An additional slot.
Access to a new Spell Circle.
An additional slot in an existing Circle.

That is exactly the behavior we want.

The new progression also creates a clear rhythm:

text
Odd progression levels:
  Usually introduce a new Circle or a new structural breakpoint.

Even progression levels:
  Usually increase the number of slots in the newly available Circles.

The higher levels follow the same pattern:

7th Circle at Progression Level 13.
8th Circle at Progression Level 15.
9th Circle at Progression Level 17.
Additional 9th-Circle slot volume through Levels 18–20.
2. Derived Mediocre Progression

The Mediocre table is correctly derived by advancing through the Reference table every other Character Level.

The mapping is:

text
Character Levels 1–2:
  Reference Progression Level 1

Character Levels 3–4:
  Reference Progression Level 2

Character Levels 5–6:
  Reference Progression Level 3

Character Levels 7–8:
  Reference Progression Level 4

Character Levels 9–10:
  Reference Progression Level 5

And so on.

At Level 20:

text
Mediocre class:
  10 Spell Slot Advancements
  Uses Reference Progression Level 10

Therefore it has:

text
5 first-circle
4 second-circle
3 third-circle
3 fourth-circle
2 fifth-circle

This is a very clean result:

It reaches 3rd Circle in the Veteran Tier.
It reaches 5th Circle in the Legend Tier.
It never reaches 6th Circle by Level 20.
Every time the class actually gains a Spell Slot Advancement, its slot profile changes.
3. Derived Bad Progression

The Bad table is correctly derived by advancing once every four Character Levels.

The mapping is:

text
Character Levels 1–4:
  Reference Progression Level 1

Character Levels 5–8:
  Reference Progression Level 2

Character Levels 9–12:
  Reference Progression Level 3

Character Levels 13–16:
  Reference Progression Level 4

Character Levels 17–20:
  Reference Progression Level 5

At Level 20:

text
Bad class:
  5 Spell Slot Advancements
  Uses Reference Progression Level 5

Therefore it has:

text
5 first-circle
2 second-circle
1 third-circle

This creates the desired power relationship:

text
Full caster:
  Progression Level 20
  9th-Circle access

Mediocre caster:
  Progression Level 10
  5th-Circle access

Bad caster:
  Progression Level 5
  3rd-Circle access
4. One Formatting Correction

In the Derived Mediocre and Derived Bad tables, the column currently labeled:

text
Progression Level

should probably be labeled:

text
Character Level

because those tables show what the character has at each Character Level.

The hidden mapping is:

text
Character Level → Spell Slot Progression Level

For example:

text
Mediocre Level 9:
  Character Level: 9
  Spell Slot Progression Level: 5
  Slots: 4 / 1 / —

Or, if we want maximum transparency, use both columns:

Tier	Character Level	Spell Slot Progression Level	1st	2nd	3rd
Master	9	5	4	1	—

For the canonical rules, I would keep the Reference Good table as the only core table and generate the derived class examples through the class-table advancement entries.

5. Recommended Terminology

The terminology now works very well:

Spell Slot Advancement: An entry on a class table granting one advancement.
Spell Slot Progression Level: The character’s accumulated position on the Reference Spell Slot Progression.
Reference Good Slot Progression: The universal slot table indexed by Spell Slot Progression Level.
Derived Mediocre Slot Progression: The result of advancing the Reference table every other class level.
Derived Bad Slot Progression: The result of advancing the Reference table once every four class levels.

I would call the first table Reference Good Slot Progression, as you have done, rather than simply “Reference Slot Progression,” because it establishes the full-caster baseline.

6. Overall Assessment

This version is coherent and achieves the intended goals:

No invisible Spell Slot Advancements.
No separate player-facing Good/Mediocre/Bad tracks.
One universal reference table.
Different classes advance through it at different rates.
Full, Mediocre, and Bad casters have clear maximum-circle relationships.
Multiclassing remains a matter of adding class-table advancements.
The progression is generous enough to compensate for removing ability-score bonus slots.
The pattern is easy to display in level-by-level class tables.

The only remaining work is calibration:

Test whether three first-circle slots at Level 1 are sufficient.
Test whether the total slot volume at Levels 5, 9, 13, 17, and 20 is appropriate.
Determine whether 9th-Circle spells at Progression Level 17 are sufficiently distinct from those at Levels 18–20.
Confirm that the reduced Mediocre and Bad slot quantities remain worthwhile for hybrid classes.
Verify the CSV’s derived mappings with the corrected column labels.
