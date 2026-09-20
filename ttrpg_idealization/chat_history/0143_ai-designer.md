---
turn: 143
role: "AI-Designer"
source: chat_history.json
---

# Turn 143 — AI-Designer

Yes—I agree with the design concern.

A Spell Slot Advancement should produce a visible change whenever possible. If the player gains an advancement but the table row is identical to the previous row, the advancement feels invisible and creates exactly the confusion you describe.

Important Clarification

Your Mediocre and Bad tables are not independent rules systems. They are derived from the Good/Reference table by applying a slower advancement cadence:

text
Full:
  Uses the next Reference row every class level.

Mediocre:
  Uses the next Reference row every 2 class levels.

Bad:
  Uses the next Reference row every 4 class levels.

For example:

text
Mediocre Level 10:
  Five Spell Slot Advancements.
  Uses Reference Progression Level 5.

Bad Level 16:
  Four Spell Slot Advancements.
  Uses Reference Progression Level 4.

That means the Good/Reference table is the critical table. If two adjacent Reference rows are identical, every class that advances into the second row gets no visible benefit.

The “No Invisible Advancement” Principle

I recommend adding this design requirement:

Every Reference Spell Slot Progression Level should differ meaningfully from the previous level.

A difference can be:

A new Spell Circle becoming available.
An additional slot at an existing Circle.
An increase in lower-Circle slot volume.
A new slot flexibility rule, if we eventually use one.

For the basic table, the cleanest version is:

Every advancement should either add a slot or unlock a new Spell Circle.

Current Problematic Repetitions

In the current Good table:

text
Progression Level 1:
  4 first-circle slots

Progression Level 2:
  4 first-circle slots

No change occurs.

Likewise:

text
Progression Level 3:
  4 first-circle, 2 second-circle

Progression Level 4:
  4 first-circle, 2 second-circle

Again, no change occurs.

This has amplified consequences:

Full caster

The full caster receives no new slot benefit at Progression Levels 2 and 4.

Mediocre caster

The same issue appears at the corresponding character levels after applying the slower cadence.

Bad caster

The problem becomes more noticeable because the class advances less frequently. A Bad caster may wait four levels for an advancement and then discover that the new table row is identical.

Recommended Adjustment

I would revise the Reference table so that Progression Levels 1–20 are all distinct.

The revision does not necessarily require dramatically increasing total spell slots. We can redistribute increases across the existing slot columns.

For example, instead of:

text
Level 1: 4
Level 2: 4
Level 3: 4 / 2
Level 4: 4 / 2

we might use a pattern such as:

text
Level 1: 4
Level 2: 5
Level 3: 5 / 2
Level 4: 5 / 3

However, that specific version would need to be tested against the rest of the table. We should not simply add slots without recalibrating the total daily spell volume.

The revision criteria should be:

Every row changes from the previous row.
Slot quantities never decrease.
Spell Circle unlocks remain at the intended progression points.
Full casters still reach 9th Circle at Progression Level 17.
Mediocre casters still reach 5th Circle at Character Level 17 and do not reach 6th Circle by Level 20 under the pure every-other-level cadence.
Bad casters still reach 3rd Circle at Character Level 17 under the every-four-level cadence.
The total daily spell volume remains within the intended resource budget.
Derived Progression Behavior

With the current cadence definitions:

Full caster
text
Class Level 1 → Reference Row 1
Class Level 2 → Reference Row 2
Class Level 3 → Reference Row 3
...
Class Level 20 → Reference Row 20
Mediocre caster
text
Class Level 1–2 → Reference Row 1
Class Level 3–4 → Reference Row 2
Class Level 5–6 → Reference Row 3
Class Level 7–8 → Reference Row 4
...
Class Level 19–20 → Reference Row 10
Bad caster
text
Class Level 1–4 → Reference Row 1
Class Level 5–8 → Reference Row 2
Class Level 9–12 → Reference Row 3
Class Level 13–16 → Reference Row 4
Class Level 17–20 → Reference Row 5

So if every Reference row is distinct, every Spell Slot Advancement produces a visible result for all three advancement rates.

Naming

The terminology you approved works well:

Spell Slot Advancement: An entry on a class table granting one advancement.
Spell Slot Progression Level: The character’s accumulated position on the Reference Spell Slot Progression.
Reference Spell Slot Progression: The universal table showing slots at Progression Levels 1–20.

I would add one design term:

No Invisible Advancement Principle: Every increase in Spell Slot Progression Level should produce a meaningful change in the Reference table.

My Recommendation

I agree with revising the Reference table before finalizing the Mediocre and Bad examples.

The correct architecture is:

text
One Reference Spell Slot Progression table.

Classes:
  Mark Spell Slot Advancements level by level.

Full caster:
  Advances every class level.

Mediocre caster:
  Advances every other class level.

Bad caster:
  Advances every four class levels.

Multiclass character:
  Adds all completed Spell Slot Advancements.

No separate player-facing Mediocre or Bad slot tables.

Every Reference row:
  Must provide a visible mechanical improvement.

The next practical step should be to revise the Good/Reference table in a spreadsheet while preserving the desired Circle unlock schedule and ensuring that every row is meaningfully different.
