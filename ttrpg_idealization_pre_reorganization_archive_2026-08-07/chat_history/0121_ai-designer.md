---
turn: 121
role: "AI-Designer"
source: chat_history.json
---

# Turn 121 — AI-Designer

Yes. Let me make the idea concrete—and also clarify that the previous wording was a proposed implementation direction, not yet a finished rule.

The goal is to avoid this:

text
Wizard 3 / Cleric 3 / Paladin 2

3 + 3 + ½ + ½ = 7 caster levels

Instead, each class or path contributes a discrete casting package.

1. Casting Packages

Each class or path is assigned one of four casting grades:

text
Full
Partial
Limited
None

Each modular path band grants a defined package.

For example:

Full Casting Path
Path Band	Package
Band 1	Novice spell slots
Band 2	Expert spell slots
Band 3	Master spell slots
Band 4	Heroic spell slots
Band 5	Legendary spell slots
Partial Casting Path
Path Band	Package
Band 1	Small Novice slot package
Band 2	Larger Novice package
Band 3	Limited Expert package
Band 4	Larger Expert package
Band 5	Limited Master package
Limited Casting Path
Path Band	Package
Band 1	Essence feature or one Novice slot
Band 2	Small Novice package
Band 3	Additional Novice package
Band 4	Limited Expert access
Band 5	Specialized Expert access

The packages are written directly on the class/path advancement table. They are not calculated through caster-level fractions.

2. The Simplest Version: Highest Track Wins

The simplest combination rule would be:

Use the strongest casting package the character possesses. Other casting paths grant Traditions, spells, acquisition features, and magical class abilities, but do not duplicate the main slot pool.

Example: Wizard 4 / Fighter 4
text
Wizard Band 1:
  Full Novice package

Fighter Band 1:
  None

Final result:
  Full Novice package

The Fighter levels provide martial features but no spell slots.

Example: Wizard 4 / Paladin 4
text
Wizard Band 1:
  Full Novice package

Paladin Band 1:
  Partial Novice package

Final result:
  Full Novice package
  Plus perhaps one defined Paladin support slot or Essence feature

The Paladin does not double the character’s slots merely because both classes provide magic.

This is extremely easy to run, but it makes secondary casting paths contribute very little to daily spell volume.

3. A More Flexible Version: Package Combination Matrix

To make secondary casting matter, we can use a discrete combination matrix.

At each path band, identify the character’s strongest two casting packages.

Strongest Path	Secondary Path	Result
Full	None	Full
Full	Limited	Full
Full	Partial	Full Plus
Full	Full	Full Plus, capped
Partial	None	Partial
Partial	Limited	Partial Plus
Partial	Partial	Full at selected thresholds
Limited	Limited	Partial at selected thresholds
Limited	None	Limited

The words Full Plus, Partial Plus, and so on would correspond to predefined slot packages.

They would not mean “add 25% of a caster level.”

Example package definitions
text
Full:
  Standard full-caster slots.

Full Plus:
  Standard full-caster slots plus one additional slot at selected ranks.

Partial:
  Reduced slot progression.

Partial Plus:
  Partial progression with earlier access to the next rank.

Limited:
  Small specialized slot progression.


The actual slot table would define exactly what each package means.

4. Example: Cleric/Wizard

Suppose both Cleric and Wizard are Full Casting paths.

text
Wizard Band 1: Full
Cleric Band 1: Full

The combination does not produce double slots.

Instead:

text
Full + Full = Full Plus

For example:

text
Full at Level 1:
  2 Novice slots

Full Plus at Level 1:
  3 Novice slots

At later bands:

text
Wizard Band 2: Full
Cleric Band 2: Full

Full + Full:
  More slots, but still capped below simply doubling the pool.

This rewards the multiclass caster without allowing the character to become twice as powerful as a single-class Wizard.

5. Example: Wizard/Cleric with Shared Traditions
text
Character:
  Wizard 4 / Cleric 4

Traditions:
  Arcane: Expert
  Divine: Trained
  Death: Expert
  Life: Trained

Casting Packages:
  Wizard: Full Band 1
  Cleric: Full Band 1

Combined Slot Package:
  Full Plus Band 1

The character receives:

One shared pool.
A modest increase over a single full caster.
Arcane and Divine acquisition features.
One Death spell list.
One Life spell list.
No separate Wizard or Cleric slots.

The character’s trade-off is that they have:

More spell acquisition methods.
More Tradition options.
More class features.
Fewer high-level Tradition investments than a pure caster.
6. Example: Wizard/Paladin
text
Wizard 4 / Paladin 4

Casting Packages:
  Wizard: Full Band 1
  Paladin: Partial Band 1

Combination:

text
Full + Partial = Full Plus

The character might receive:

text
Full baseline:
  2 Novice slots

Full Plus:
  3 Novice slots

But the Paladin contribution could instead be expressed as:

A Divine or War Tradition access feature.
A Smite fueled by Essence.
One additional prepared spell.
A reaction-casting feature.
A limited defensive spell.

This prevents every secondary caster from being valuable only because it adds more slots.

7. Example: Paladin/Ranger
text
Paladin 4 / Ranger 4

Casting Packages:
  Paladin: Partial Band 1
  Ranger: Partial Band 1

Combination:

text
Partial + Partial = Partial Plus

At a later boundary, the system might say:

text
Partial Plus Band 2:
  Unlocks Expert slots earlier than either class alone.

Or:

text
Partial + Partial:
  Never becomes Full, but receives more slots and broader access.

That is a major design choice.

If two partial paths can eventually create full casting, multiclass builds may become too efficient. If they can never combine upward, multiclassing remains more conservative.

My initial recommendation would be:

Two Partial paths can create an improved Partial track, but not a Full track without a dedicated “Full Casting” Prestige Path.

8. Example: Three-Way Multiclassing
text
Wizard 4 / Cleric 4 / Fighter 4

Packages:

text
Wizard: Full Band 1
Cleric: Full Band 1
Fighter: None

Result:

text
Full Plus Band 1

The Fighter contributes no slots, but contributes:

Combat skills.
Feats.
Martial class features.
Possibly Essence-based abilities.

Now consider:

text
Wizard 4 / Cleric 4 / Rogue 4

Packages:

text
Wizard: Full Band 1
Cleric: Full Band 1
Rogue: Limited Band 1

The result might still be:

text
Full Plus Band 1

The third class expands:

Skill access.
Shadow or Trickery Tradition access.
Spell acquisition options.
Essence features.

But it does not stack another full pool on top.

9. What Does “Without Arithmetic” Mean Here?

There are two different kinds of arithmetic to distinguish.

Character-building arithmetic

At level-up, the player may need to determine their new slot package.

That can be handled through:

A progression table.
A character-builder worksheet.
A class/path combination chart.
A precomputed character sheet.

This is acceptable because it is not repeated during ordinary action resolution.

Table-side arithmetic

During play, the player should not calculate:

text
3 Wizard levels + 2 Cleric levels + half Paladin level

Instead, the character sheet should simply say:

text
Shared Spell Package: Full Plus — Veteran

or list the actual slots:

text
Novice: 3
Expert: 2
10. A Cleaner Alternative: Casting Advancement Tags

Instead of calling this a combination matrix, we could give each path discrete advancement tags:

text
Full Casting Step
Partial Casting Step
Limited Casting Step

At each level band, the path grants one or more tags. A character’s build sheet converts those tags into a named package:

text
No Casting
Limited
Partial
Partial Plus
Full
Full Plus

The player never handles fractions.

Example:

text
Wizard Band 1:
  Full Casting Step

Cleric Band 1:
  Full Casting Step

Combined:
  Full Plus Package

This is conceptually similar to combining “Good,” “Medium,” and “Bad” advancement tracks elsewhere in our system.

11. Is This Better Than a Shared Spellcasting Track?

There is an even simpler alternative:

Every character has one Spellcasting Track determined by their strongest casting path. Secondary casting paths never modify slot quantity; they only add access, spells, and class features.

This is easier to balance and resembles how many multiclass systems prevent spell-slot inflation.

The trade-off is:

Cleaner balance.
Less reward for combining two caster classes.
More emphasis on Tradition breadth and acquisition mechanics.
12. My Current Recommendation

I would use a two-layer approach:

Primary Casting Package

The strongest class/path contribution determines the character’s baseline shared slots.

text
Full > Partial > Limited > None
Secondary Casting Package

Secondary casting paths may grant a predefined support benefit:

A small number of additional slots.
Earlier access to a lower Spell Rank.
More prepared spells.
Additional Tradition access.
More Essence.
A unique acquisition method.
A special casting feature.

This is safer than allowing every class to add directly to the slot pool.

So:

text
Wizard 4 / Cleric 4:
  Full baseline
  Cleric support package

Wizard 4 / Fighter 4:
  Full baseline
  Fighter supernatural support package, if any

Paladin 4 / Ranger 4:
  Partial baseline
  Secondary partial support package
13. The Actual Concept in One Sentence

The idea is:

A class or path grants a named casting package at discrete advancement points; the strongest package establishes the shared slot baseline, and secondary casting packages modify that baseline only through explicit capped benefits—not fractional caster levels.

This is probably the safest starting point for playtesting because it prevents multiclass spell-slot explosions while still allowing secondary classes to matter through Traditions, acquisition, Essence, and class features.
