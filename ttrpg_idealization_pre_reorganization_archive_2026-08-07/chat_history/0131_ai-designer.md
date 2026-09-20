---
turn: 131
role: "AI-Designer"
source: chat_history.json
---

# Turn 131 — AI-Designer

Exactly. That is much cleaner.

The system does not have Good, Mediocre, or Bad tracks as player-facing mechanics. Those are only design guidelines describing how frequently a class advances its Spellcasting Progression Level.

Spellcasting Progression Level

A character has one derived value:

text
Spellcasting Progression Level

It determines the character’s position on the shared Spell Slot table.

Classes and Prestige Classes simply state how often they advance that value.

Examples
text
Wizard:
  +1 Spellcasting Progression Level per Wizard level.

Cleric:
  +1 Spellcasting Progression Level per Cleric level.

Paladin:
  +1 Spellcasting Progression Level every 2 Paladin levels.

Eldritch Knight:
  +1 Spellcasting Progression Level every 3 Eldritch Knight levels.

Fighter:
  No Spellcasting Progression advancement.

The terms “Good,” “Mediocre,” and “Bad” describe these advancement cadences during design and class comparison, but they do not appear in the actual rules procedure.

Multiclassing

Each class contributes its own discrete advancement.

Wizard 4 / Paladin 4
text
Wizard:
  4 levels × 1 advancement per level = 4

Paladin:
  4 levels ÷ 2 = 2

Spellcasting Progression Level:
  6

The character uses the Spell Slot table’s Progression Level 6 row.

text
Slots:
  5 first-circle
  3 second-circle
  2 third-circle
Wizard 4 / Eldritch Knight 3
text
Wizard:
  4 progression advances

Eldritch Knight:
  1 progression advance

Spellcasting Progression Level:
  5

The character uses the Progression Level 5 row.

Paladin 4 / Eldritch Knight 3
text
Paladin:
  2 progression advances

Eldritch Knight:
  1 progression advance

Spellcasting Progression Level:
  3

The character uses the Progression Level 3 row.

Wizard 4 / Cleric 4
text
Wizard:
  4 progression advances

Cleric:
  4 progression advances

Spellcasting Progression Level:
  8

The character uses the Progression Level 8 row.

There is still only one shared slot pool.

No Fractions on the Character Sheet

The class cadence can be written in a way that avoids fractional caster levels:

text
Wizard:
  Spellcasting Advancement: Every Level

Paladin:
  Spellcasting Advancement: Every 2 Levels

Eldritch Knight:
  Spellcasting Advancement: Every 3 Levels

At level-up, the character records the number of completed advancements.

text
Spellcasting Progression Level: 6

During play, there is no calculation. The character simply uses the corresponding row.

This is essentially SotDL’s Power model applied to the spell-slot table rather than directly to maximum spell rank.

Difference from SotDL Power
SotDL Power

Power determines:

The highest spell rank available.
The general scale of magical effects.

Individual spells determine:

How many times they can be cast.
Their daily use limits.
Our Spellcasting Progression Level

Spellcasting Progression Level determines:

The quantity of shared spell slots.
Which Spell Circles are available through the slot table.

Tradition Skill determines:

Which Tradition spells the character can access.
The highest spell Circle they can use through that Tradition, if we retain that gate.
Intrinsic spell scaling.

However, based on your earlier decision that Tradition Rank does not limit slot access, the final division is:

text
Spellcasting Progression Level:
  Daily spell-slot volume and slot-table position.

Tradition Skill:
  Spell access and intrinsic spell scaling.

Spell Circle:
  Spell complexity and slot cost.

Character Level:
  Overall advancement and High Fantasy Tier.

A character can therefore have:

text
Spellcasting Progression Level: 8
Death: Trained
Arcane: Expert

They receive the full Progression Level 8 slot pool, but:

Their Death spells use Trained-scale effects.
Their Arcane spells use Expert-scale effects.
They may spend high-circle slots on lower-circle spells.
They cannot access spells that their class, Tradition, or spell-acquisition rules have not made available.
Important Tracking Rule

The advancement cadence should be based on levels in the relevant class, not total Character Level.

For example:

text
Paladin 3 / Wizard 1

Paladin contribution:

text
3 Paladin levels:
  1 completed advancement if advancement occurs every 2 levels.

Wizard contribution:

text
1 Wizard level:
  1 advancement.

Total:

text
Spellcasting Progression Level 2

The character’s class order does not matter unless a class feature explicitly says otherwise.

Prestige Classes

Prestige Classes work the same way as Base Classes.

text
Archmage:
  Advances Spellcasting every level.

Eldritch Knight:
  Advances Spellcasting every 3 levels.

Death Knight:
  Advances Spellcasting every 2 levels.

The difference is only that Prestige Classes have prerequisites.

A Prestige Class may also grant:

Tradition access.
Tradition Skill investment.
Spell acquisition.
Essence features.
Metamagic.
Special spell permissions.
Corrected OD-001A Model

The current model is now:

text
Classes and Prestige Classes:
  Grant a Spellcasting Advancement cadence.

Spellcasting Progression Level:
  A derived value increased by completed class-based advancements.

Shared Spell Slot Table:
  Uses Spellcasting Progression Level.

Traditions:
  Individual skills with fixed shared spell lists.

Tradition Competency:
  Controls spell access and intrinsic spell scaling.

Spell Circles:
  Determine spell complexity and slot cost.

Essence:
  Powers 0th-circle spells, metamagic, casting stability,
  and supernatural class features.

High Fantasy Tiers:
  Describe overall character scope, not independent spellcasting tables.

Mythic:
  Adds Epic Traditions and Spells without necessarily adding
  a new ordinary slot progression.

This removes the need for:

Good/Mediocre/Bad player-facing tracks.
Spellcasting Profiles.
Separate caster levels for each Tradition.
Separate class spell lists.
Fractional caster levels.
A package-combination matrix.

The only remaining implementation detail is how to write fractional-looking cadences such as “every two levels” in a completely transparent class table. The cleanest wording is probably:

text
Spellcasting Advancement:
  Paladin levels 2, 4, 6, 8, and 10 each grant one advancement.

That makes the actual progression explicit and avoids even conceptual fraction arithmetic.
