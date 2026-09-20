---
turn: 119
role: "AI-Designer"
source: chat_history.json
---

# Turn 119 — AI-Designer

Based on the comparison, I would answer OD-001A with a five-rank shared Vancian progression, using Tradition Rank as the spell-quality/access gate and class/path casting tracks as the source of daily slot volume.

Recommended OD-001A Answers
1. How many spell slots does a character receive at each Character Level and High Fantasy Tier?

I recommend five ordinary Spell Ranks aligned to the five mortal High Fantasy Tiers:

Spell Rank	High Fantasy Tier	Typical Availability
Novice	Trained	Levels 1–4
Expert	Veteran	Levels 5–8
Master	Master	Levels 9–12
Heroic	Hero	Levels 13–16
Legendary	Legend	Levels 17–20
Mythic	Mythic	Level 21+

A full caster’s baseline slot progression could be:

Level	Novice	Expert	Master	Heroic	Legendary
1	2	—	—	—	—
2	3	—	—	—	—
3	4	—	—	—	—
4	4	—	—	—	—
5	3	2	—	—	—
6	3	3	—	—	—
7	4	3	—	—	—
8	4	4	—	—	—
9	3	3	2	—	—
10	3	3	3	—	—
11	4	3	3	—	—
12	4	4	3	—	—
13	3	3	3	2	—
14	3	3	3	3	—
15	4	3	3	3	—
16	4	4	3	3	—
17	3	3	3	3	2
18	3	3	3	3	3
19	4	3	3	3	3
20	4	4	3	3	3

This provides:

More slots as the character advances.
A new maximum Spell Rank at each major tier boundary.
A recognizable D&D-style progression.
A manageable five-column table.
No need for ninth-level spell slots before the Mythic tier.

This table should be regarded as a full-caster baseline, not a final balance result. We would still need to test whether five ranks provide enough differentiation between levels inside each tier.

Cantrips and 0th-rank spells

I recommend that 0th-rank spells do not use these slots.

They use Essence instead.

text
0th-Rank Spell:
  Costs Essence.
  Does not consume a daily Spell Slot.

That gives spellcasters reliable minor magic while preserving slots for meaningful daily choices.

2. How do class and modular path levels contribute without fractional caster levels?

Use discrete Spellcasting Track contributions, not caster-level fractions.

Each class or modular path has a casting track:

Full Casting
Partial Casting
Limited Casting
No Casting

A path’s casting track provides specific rank-based progression at its own level-band boundaries.

For example:

Full Casting Path
text
Path Band 1:
  Grants Novice slot progression.

Path Band 2:
  Grants Expert slot progression.

Path Band 3:
  Grants Master slot progression.

Path Band 4:
  Grants Heroic slot progression.

Path Band 5:
  Grants Legendary slot progression.
Partial Casting Path
text
Path Band 1:
  Grants Novice access or a small Novice slot package.

Path Band 2:
  Improves Novice slots or grants limited Expert access.

Path Band 3:
  Grants stronger Novice and Expert capacity.

Path Band 4:
  Grants limited Master capacity.

Path Band 5:
  Remains below full-caster progression.
Limited Casting Path

A limited path may grant:

A small number of Novice slots.
A restricted Tradition.
A few class-granted spells.
Essence-based supernatural abilities.
No progression beyond Expert or Master unless a later path expands it.

The character sheet records the resulting slot package directly. The player does not calculate:

text
Wizard 3 + Cleric 2 + half-caster fraction + prestige fraction

Instead, each path grants discrete advancement entries.

3. Should full, partial, limited, and noncasting paths use distinct tracks?

Yes.

They should use distinct discrete tracks rather than one universal formula.

Full Casting
Access to all five ordinary Spell Ranks.
Highest slot rank advances at the major tier boundaries.
Receives the largest daily slot pool.
Typical examples: Wizard, Cleric, Nature caster, dedicated magical paths.
Partial Casting
Receives fewer slots.
Reaches higher ranks later.
May stop at Master or Heroic without a prestige path.
Typical examples: Paladin, Ranger, War Mage, Arcane Warrior.
Limited Casting
Receives a small number of slots.
Has restricted Tradition access.
Often relies on Essence, class features, weapons, or specific spells.
Typical examples: Eldritch Knight-style paths, magical rogues, specialized prestige paths.
Noncasting
Receives no ordinary daily spell slots.
May still use Essence for supernatural feats, martial techniques, ancestry powers, or psionic effects.
Can gain limited spell access through feats, items, rituals, or later paths.

This also allows “noncaster” to mean “no Vancian casting” rather than “no supernatural ability.”

4. When a character multiclasses, how are slot contributions combined?

I recommend discrete slot-package combination, not fractional caster levels.

Each path grants a recorded package:

text
Full Path Band:
  Full contribution.

Partial Path Band:
  Partial contribution.

Limited Path Band:
  Limited contribution.

At character advancement, the character’s total casting result is determined by a progression matrix.

The important rule is:

Multiclassing can broaden access and acquisition, but it should not allow a one-level dip to provide a full new tier of spell capacity.

Recommended combination priority
A full-casting path advances the primary shared slot progression.
Additional full-casting paths may broaden Traditions and acquisition, but do not duplicate the full slot package at the same level.
Partial paths contribute only when the character lacks equivalent full-casting progression.
Limited paths add narrow slot packages, Essence features, or specific spell access.
Multiple partial paths can eventually combine into a stronger progression, but only at defined discrete thresholds.

This produces three possible multiclass results:

Full caster plus noncaster
text
Wizard 4 / Fighter 4
Retains the Wizard’s full casting progression.
Gains Fighter features.
Does not gain additional slots from Fighter.
May gain martial use of Essence through Fighter feats or paths.
Full caster plus partial caster
text
Wizard 4 / Paladin 4
Wizard provides the main full-casting progression.
Paladin broadens Divine, Life, War, or Guardian access.
Paladin may provide limited additional acquisition or Essence abilities.
Paladin does not double the slot pool.
Partial caster plus partial caster
text
Paladin 4 / Ranger 4
Each contributes a partial casting package.
A combination matrix determines whether they remain Limited, become Partial, or reach a new slot threshold.
The result is recorded directly on the sheet.

This last case needs playtesting, but it is preferable to adding fractions.

5. Does highest Tradition Rank limit the highest slot a character can use?

Yes.

A character must satisfy both:

The Spell Slot requirement.
The Tradition Rank requirement.

Recommended gate:

Tradition Rank	Highest Spell Rank
Untrained	None
Trained	Novice
Expert	Expert
Master	Master
Legendary	Heroic and Legendary, subject to final Mythic rules

Example:

text
Death: Expert
Available Slots: Novice and Expert

The character can cast Expert Death spells.

text
Death: Trained
Available Slots: Novice and Expert

The character can only cast Novice Death spells.

text
Death: Expert
Available Slots: Novice only

The character understands Expert Death magic but cannot currently cast it.

This preserves the distinction between:

Magical competence.
Daily magical volume.
Spell knowledge.
Spell access.
What happens to higher slots?

A character may retain higher-rank slots even if they currently lack a sufficiently ranked Tradition. Those slots can be:

Used with another sufficiently ranked Tradition.
Used for metamagic, if permitted.
Used for future advancement.
Converted into a special ritual or Essence effect, if a rule permits.
6. Do advanced paths increase slot quantity, maximum Spell Rank, or both?

They can increase either, but they should not automatically increase both.

This gives advanced paths meaningful specialization.

Capacity Paths

Increase:

Number of slots.
Maximum usable Spell Rank.
Spell acquisition volume.

These are appropriate for:

Archmage.
High Priest.
Master Druid.
Legendary Thaumaturge.
Tradition Paths

Increase:

Tradition Rank.
Tradition access.
Spell list breadth.
Tradition feats.
Spell scaling.

These may grant few or no additional slots.

Examples:

text
Death Adept:
  Increases Death to Master.
  Adds Death spells.
  Grants necromantic feats.
  Does not increase total slots.

Archmage:
  Adds an Expert slot.
  Unlocks Master and Heroic slots.
  Does not necessarily improve Death, Rune, or Elemental rank.
Hybrid Paths

Increase:

One Tradition Rank.
A small number of slots.
A specific spell acquisition method.
A limited maximum Spell Rank.

This allows prestige classes to have distinct identities without all of them becoming “more caster level.”

7. How does Mythic advancement expand or transform the shared slot pool?

Mythic advancement should not simply add an endless number of ordinary Legendary slots.

That would encourage spell-slot inflation rather than mythic transformation.

I recommend that Mythic introduces a sixth category:

Mythic Spell Rank

Mythic spells should be:

Rare.
Expensive.
Often ritualized.
World-scale or divine in consequence.
Limited by Essence, preparation, components, locations, or narrative conditions.
Not merely stronger combat spells.
Mythic slot model

At the beginning of Mythic advancement:

text
Mythic Slots: 1

Further Mythic development may grant:

Additional Mythic slots.
A Mythic reserve that can empower lower-rank spells.
A unique Mythic signature spell.
A permanent magical domain.
A once-per-campaign or once-per-arc effect.
Access to Creation, Time, Space, Order, or Chaos.

However, we should not introduce a meta-currency. Mythic resources must remain in-world:

Essence.
Divine authority.
Bound relics.
Cosmic vows.
Mythic reagents.
Permanent transformation.
Domain control.
Long rituals.
Mythic spell scaling

At Mythic, the distinction between slot rank and Tradition Competency becomes even more important:

text
Legendary Death + Mythic Slot:
  Mythic-scale Death effect.

Legendary Death + Legendary Slot:
  Legendary-scale Death effect.

Expert Death + Mythic Slot:
  Cannot cast a Mythic Death spell.

A higher slot cannot substitute for insufficient Tradition Competency.

Recommended OD-001A Resolution
Core answers
Use five ordinary Spell Ranks aligned with the five mortal High Fantasy Tiers.
Use one shared spell-slot pool.
Give full, partial, limited, and noncasting paths separate discrete tracks.
Combine multiclassing through discrete slot packages and a progression matrix, not fractional caster levels.
Require both sufficient Tradition Rank and an appropriate Spell Slot.
Let advanced paths increase slot quantity, maximum Spell Rank, Tradition Rank, spell acquisition, or a focused combination of these.
Introduce Mythic Slots at Level 21+ rather than endlessly expanding Legendary slots.
Use Essence for 0th-rank spells, metamagic, casting stability, and supernatural features.
Keep intrinsic spell scaling tied to Tradition Competency.
Do not make higher-rank slots automatically improve lower-rank spells.
Remaining implementation tasks

The main remaining OD-001A work is now:

Finalize whether the five ordinary Spell Ranks should be called Novice, Expert, Master, Heroic, and Legendary.
Build the exact Full, Partial, Limited, and Noncasting slot tables.
Build the discrete multiclass combination matrix.
Test whether the proposed full-caster slot volume produces the desired daily resource pressure.
Determine how partial-plus-partial casting combines.
Determine whether spell slots are restored by a long camp only or through additional in-world recovery methods.
Design Mythic Slots and Mythic spell access.
