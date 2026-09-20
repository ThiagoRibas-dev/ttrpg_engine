---
turn: 123
role: "AI-Designer"
source: chat_history.json
---

# Turn 123 — AI-Designer

You are right. My package-combination model is more complicated than either of the two systems we are trying to learn from.

The comparison is:

1. D&D 5e: Shared Slot Stacking

D&D 5e separates:

text
Spell slots:
  Shared through a multiclass caster-level table.

Spell access:
  Still class-specific.

Preparation/known spells:
  Still class-specific.

Caster progression:
  Full, half, and third-caster contributions.

A multiclass character adds their class contributions to determine one shared ordinary spell-slot table.

For example:

text
Wizard 5 / Cleric 5

Both are full casters, so the character uses the shared slot progression for an effective 10th-level spellcaster.

A Paladin or Ranger contributes more slowly. Warlock Pact Magic remains separate.

Strengths for our system
One slot pool.
Very familiar.
Multiclassing is easy to understand.
Full, partial, and limited casting are clearly differentiated.
Slot quantity and spell access are already separate concepts.
We can remove class spell-list problems because our Traditions have fixed shared lists.
Weaknesses
The effective-caster-level calculation uses fractions and rounding.
A player may need to consult a multiclass table.
Full casters can stack very efficiently.
The system still has separate class spell lists and preparation rules, though we would eliminate those.
It assumes that spell-slot progression and caster-level scaling are closely related.
2. Shadow of the Demon Lord: Power

SotDL does not use shared spell slots.

Instead, a character has Power, which determines the highest spell rank they can cast.

Traditions and paths determine:

Which spells the character knows.
Which traditions they can access.
Which talents they receive.

Each spell then has its own number of castings or uses.

A character might have:

text
Power: 5

Traditions:
  Arcana
  Battle
  Fire
  Teleportation

Spell uses:
  Fireball: 1 casting
  Force Missile: 3 castings
  Teleport: 2 castings
Strengths for our system
Extremely simple multiclassing.
No slot tables.
No fractional caster levels.
Power cleanly determines maximum spell rank.
Modular paths grant access without separate class-owned spell lists.
Individual spell uses allow designers to balance unusually strong spells.
Very compatible with SotDL-style Tradition access.
Weaknesses for our system
It is not Vancian slot casting.
Every spell needs its own casting-use value.
A powerful spell may have one casting while a weaker spell has three, creating a lot of individual spell bookkeeping.
It does not naturally support the D&D 3.5e model where spells improve with caster level while higher-level slots do not automatically improve them.
It gives less strategic value to choosing which spell rank to spend.
It may make spells feel more like individual class powers than entries in a prepared spell system.
3. Why the Two Systems Feel Simpler

They simplify different problems.

D&D 5e simplifies quantity

The central question is:

How many slots do I have today?

The answer comes from one shared table.

SotDL simplifies maximum power

The central question is:

What is the highest rank of spell I can cast?

The answer comes from Power.

Our system currently wants both:

text
What is the highest Spell Rank I can cast?
  Tradition Competency.

How many spells can I cast today?
  Shared Vancian slots.

That is not inherently too complicated. It is only complicated if we add a third independent caster statistic.

4. Best Simplification for Our System

I recommend adopting the D&D 5e slot-stacking structure, but removing the parts that conflict with our architecture.

Keep from D&D 5e
One shared ordinary spell-slot pool.
Full, partial, and limited casting contributions.
A shared progression table.
Higher-rank slots as a daily resource.
Class and path levels contributing to slot progression.
Spell preparation and spell acquisition tracked separately from slots.
Remove or replace
Class-owned spell lists.
Class-specific spell preparation systems.
Fractional caster levels on the character sheet.
Ability-score bonus spell slots.
Separate Pact Magic unless we deliberately add it as a later subsystem.
Replace with our rules
text
Spell access:
  Fixed Tradition spell lists.

Casting quality and maximum Spell Rank:
  Tradition Competency.

Daily spell volume:
  Shared spell-slot table.

Spell scaling:
  Tradition Competency, not a separate Caster Level.

Spell acquisition:
  Class/path features.

Metamagic and casting stability:
  Essence.
5. Can We Use 5e Slot Stacking Without Fractions?

Yes. The fractions do not need to appear on the player-facing character sheet.

Instead of:

text
Full caster: +1
Half caster: +1/2
Third caster: +1/3

we could define discrete contribution bands.

Example

At each level or path milestone, a class grants a Spellcasting Contribution:

text
Full:
  Contributes at every level.

Partial:
  Contributes at selected levels.

Limited:
  Contributes only at designated path boundaries.

None:
  Contributes nothing.

During character creation or level-up, a worksheet converts the class/path combination into one result:

text
Shared Spellcasting Progression: Level 8

The player then reads the ordinary slot table.

This is still conceptually 5e, but avoids showing fractions to players.

6. A More Direct Option: Precomputed Contribution Table

We could also make multiclassing use an official table.

Combination	Shared Progression
Full + Full	Add both contributions using the multiclass table
Full + Partial	Full progression plus partial contribution
Full + Limited	Full progression with limited advancement
Partial + Partial	Combined partial progression
Partial + Limited	Partial progression with limited advancement
Limited + Limited	Limited progression unless a path says otherwise
Any + None	No additional casting contribution

The table would provide the result directly.

For example:

text
Wizard 5 / Cleric 3:
  Shared Spellcasting Progression: 8

Wizard 5 / Paladin 3:
  Shared Spellcasting Progression: 6

Paladin 5 / Ranger 3:
  Shared Spellcasting Progression: 4

The exact values would need to be designed, but the player would not calculate fractions.

7. Important Difference from Our Earlier Package Model

The earlier package model attempted to prevent slot inflation by treating each path as a named package and combining packages through a matrix.

That gives tighter control, but it creates many new categories:

text
Full
Full Plus
Partial
Partial Plus
Limited
Limited Plus

The 5e model is cleaner because it accepts that class contributions stack into a single progression.

Given your preference for high option density but manageable play, I now think the 5e approach is preferable.

8. How Tradition Competency Fits

We can still use Tradition Competency as the SotDL-like Power gate.

Example:

text
Shared spell slots:
  Novice: 4
  Expert: 3
  Master: 1

Traditions:
  Arcane: Expert
  Death: Trained
  Life: Untrained

The character may cast:

Expert Arcane spells.
Novice Death spells.
No Life spells.

The character cannot cast Master spells yet, even though they possess a Master slot, unless one of their Traditions reaches Master.

This means:

text
Shared slot progression = quantity.
Tradition Competency = maximum quality.

That is probably the cleanest combination of 5e and SotDL.

9. Higher-Rank Slots and Lower-Rank Spells

Your D&D 3.5e preference creates an important difference from D&D 5e.

In our system:

text
Casting a Novice spell in an Expert slot:
  Does not automatically improve the spell.

The slot is simply consumed.

This gives higher-rank slots a different role from 5e upcasting.

We can later decide whether certain spells have explicit:

text
Heightened:
  Expert version
  Master version

But heightening should be an explicit spell rule, not an automatic property of using a higher slot.

10. My Revised Recommendation

I would now answer OD-001A this way:

Use a D&D 5e-style shared slot pool, with discrete class/path contributions and a single multiclass spellcasting table. Use SotDL-style Tradition progression to determine spell access and maximum Spell Rank. Use D&D 3.5e-style Tradition Competency scaling for intrinsic spell improvement. Do not create separate class-owned spell lists, casting profiles, or individual Tradition caster levels.

The final architecture becomes:

text
Tradition Competency:
  Determines spell access, casting quality, and maximum Spell Rank.

Class/Path Casting Contribution:
  Determines daily shared slot quantity.

Shared Spell Slots:
  One universal pool by Spell Rank.

Spell Lists:
  Fixed by Tradition, not class.

Spell Acquisition:
  Granted by class and path features.

Essence:
  Fuels 0th-rank spells, metamagic, casting stability,
  and supernatural features.

Psychic/Psionic:
  Future Essence-based parallel system.

This is significantly simpler than the package matrix and better aligned with the three reference systems:

D&D 5e supplies shared slots.
SotDL supplies Tradition access and Power-like spell-rank gating.
D&D 3.5e supplies intrinsic caster-level scaling.
