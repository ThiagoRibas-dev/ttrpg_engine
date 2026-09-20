---
turn: 127
role: "AI-Designer"
source: chat_history.json
---

# Turn 127 — AI-Designer

Yes, I understand the intended structure now. The table is not showing a separate spell-slot table for each High Fantasy Tier. It is one continuous Good Spellcasting Progression from Character Level 1 through 20, with the Tier column indicating the character’s current High Fantasy scope.

So the structure is:

text
Character Level 1–4   = Trained Tier
Character Level 5–8   = Veteran Tier
Character Level 9–12  = Master Tier
Character Level 13–16 = Hero Tier
Character Level 17–20 = Legend Tier

The Spellcasting Progression Level is effectively the character’s position on the class’s spellcasting track, while the Tier label indicates the character’s overall campaign tier.

Corrected Interpretation
Good Spellcasting Progression
Character Tier	Spellcasting Progression Level	1st	2nd	3rd	4th	5th	6th	7th	8th	9th
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

This is much clearer.

Important Consequences
1. Spell circles are not aligned one-to-one with High Fantasy Tiers

A Veteran character can already access:

1st Circle
2nd Circle
3rd Circle
4th Circle

A Master character can access all the way through:

6th Circle

A Legend character reaches:

9th Circle

This is more generous than standard D&D 3.5e, but it makes sense because:

Ability-score bonus slots are removed.
Tradition Competency is a separate gate.
Spell access is distributed across Traditions.
The system is aiming for high fantasy.
The caster’s class progression needs to feel rewarding early.
2. Spellcasting Progression Level is not Character Level

A Level 10 character could have:

text
Character Level: 10
Spellcasting Progression Level: 6

if they multiclassed into noncasting classes.

Conversely, a dedicated caster might have:

text
Character Level: 10
Spellcasting Progression Level: 10

This is exactly the distinction we need.

3. Spellcasting Progression is class-derived

Each class should specify whether and how it advances the Good, Mediocre, or Bad Spellcasting Progression.

For example:

text
Wizard:
  Spellcasting Progression: Good

Cleric:
  Spellcasting Progression: Good

Paladin:
  Spellcasting Progression: Mediocre

Ranger:
  Spellcasting Progression: Bad

Fighter:
  Spellcasting Progression: None

The class table then determines how many levels of Spellcasting Progression the character gains.

Corrected Multiclass Interpretation

The critical question is now:

When a character takes levels in multiple classes, how many levels do they gain in each Spellcasting Progression?

The cleanest version remains:

text
Wizard 5 / Fighter 3

Good Spellcasting Progression: 5
No Spellcasting Progression: 0

Result:
  Use the Good Progression Level 5 row.

For a multiclass character with multiple spellcasting classes:

text
Wizard 5 / Cleric 3

Good Spellcasting Progression:
  Wizard contribution: 5
  Cleric contribution: 3

The unresolved question is whether those contributions:

Combine into Good Progression Level 8; or
Use only the highest individual contribution, Good Level 5; or
Combine through a separate rule for Good, Mediocre, and Bad advancement.

Given the design you are describing, I think the intended answer is likely:

All classes that explicitly advance the same Spellcasting Progression contribute their class levels to that progression.

So:

text
Wizard 5 / Cleric 3
= Good Spellcasting Progression Level 8

This is the direct analogue of D&D 5e’s shared slot stacking, except the class tables explicitly tell the player whether a class level advances the progression.

A character sheet could simply record:

text
Spellcasting Progression:
  Good 8

No caster-level calculation is needed during play.

Mediocre and Bad Tracks

The refined table also makes the purpose of the additional tracks clearer.

They are not necessarily added on top of Good progression. Rather, they are alternate class-derived progressions.

For example:

text
Full Wizard:
  Good Progression Level 8

Paladin/Ranger:
  Mediocre Progression Level 8

Fighter:
  No Progression

The exact Mediocre and Bad tables would have:

Later access to higher spell circles.
Fewer slots at each circle.
Lower maximum Spell Circle.
Or some combination of those.

A Paladin/Ranger should not automatically become equivalent to a Wizard 8 merely because both have eight levels of classes. Their class levels would advance the Mediocre or Bad table, not the Good table.

Tradition Rank Still Does Not Gate Slots

Your clarification is also important:

text
Spellcasting Progression:
  Determines available daily slots.

Tradition Skill:
  Determines spell access and intrinsic spell scaling.

Example:

text
Character:
  Good Spellcasting Progression Level 10
  Death: Trained
  Arcane: Expert

They have all the slots listed on the Good Level 10 row, but:

They can cast only Novice Death spells.
They can cast Expert Arcane spells.
They cannot cast Master Death spells.
They can spend higher-circle slots on lower-circle spells if the rules allow it.

This is intentional. It creates characters with:

Broad daily magical endurance but shallow Tradition investment.
Deep Tradition mastery but limited slot capacity.
Multiple Traditions at different ranks.
Interesting multiclass trade-offs.
Spell Scaling

Your model now has a clean three-way division:

text
Spellcasting Progression:
  Determines how many slots the character has.

Spell Circle:
  Determines the slot cost and baseline spell complexity.

Tradition Competency:
  Determines whether the character can access the spell
  and how strongly the spell scales.

Example:

text
Death: Trained
Animate Dead:
  Trained-scale effect.

Death: Expert
Animate Dead:
  Expert-scale effect.

Death: Master
Animate Dead:
  Master-scale effect.

Using a higher-circle slot does not automatically cause the spell to use the higher Tradition-scale version.

Revised OD-001A Resolution

With your clarification, I would now state the decisions as:

The provided table is the Good Spellcasting Progression from Levels 1–20.
The Tier column describes the character’s High Fantasy Tier, not a separate spell-slot table.
Spellcasting Progression Level is separate from Character Level.
Good, Mediocre, Bad, and None are distinct class-based progression tracks.
Each class explicitly states whether it advances one of those tracks.
Prestige Classes use the same rules as Base Classes; their difference is their entry requirements.
Classes that advance the same track contribute their levels to that shared progression.
Tradition Competency does not limit the character’s available spell slots.
Tradition Competency limits spell access and controls intrinsic spell scaling.
Mythic advancement grants Epic Traditions and Epic Spells using the existing slot pool rather than adding new ordinary spell slots.

The one point that still needs a precise rule is whether a class advancing a lower track can contribute to a character already advancing a higher track. For example:

text
Wizard 5 / Paladin 3

Does the character have:

text
Good 5
Mediocre 3

or:

text
Good 8

if both classes are considered to advance the shared Spellcasting Progression?

Your wording suggests the latter may be the intended model, but that would need an explicit conversion rule for how Mediocre and Bad class levels contribute when combined with Good progression.
