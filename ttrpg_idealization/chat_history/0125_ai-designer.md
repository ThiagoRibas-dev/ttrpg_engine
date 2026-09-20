---
turn: 125
role: "AI-Designer"
source: chat_history.json
---

# Turn 125 — AI-Designer

This is a much cleaner direction, and it resolves the main OD-001A problem better than my package-matrix proposal.

Your model is essentially:

Class level determines the character’s Spellcasting Progression Level. The class table explicitly states whether and how that level advances the shared progression. Tradition Skills determine which spells the character can access and how those spells scale.

That is a strong combination of:

D&D 3.5e’s slot volume and intrinsic caster scaling.
D&D 5e’s shared multiclass slot pool.
SotDL’s separation of magical access from overall magical capacity.
1. The Baseline Progression

Your table becomes the Good Spellcasting Progression.

It provides:

Four 1st-Circle slots at Level 1.
Earlier and more numerous low-circle slots than standard 3.5e.
Access to 9th-Circle slots by Level 17.
Five 9th-Circle slots by Level 20.
No bonus slots from ability scores.

That compensation is important. Since our system does not grant bonus spell slots from INT, WIS, or CHA, the baseline progression should indeed be more generous than 3.5e’s ordinary table.

The table also gives full casters meaningful spell volume at every tier:

text
Trained:
  Reliable 1st-Circle casting.

Veteran:
  2nd- and 3rd-Circle access.

Master:
  4th-, 5th-, and 6th-Circle access.

Hero:
  7th- and 8th-Circle access.

Legend:
  9th-Circle access and deep lower-circle reserves.
2. Spellcasting Progression Level

I suggest formally defining this as:

Spellcasting Progression Level is the class-derived advancement track that determines the character’s shared spell-slot pool.

It is distinct from:

Character Level.
Tradition Competency.
Ability scores.
Essence.
Spell Rank.
Spell access.

A character sheet might show:

text
Character Level: 12
Spellcasting Progression Level: 9
Spellcasting Track: Good
Traditions:
  Arcane: Expert
  Elemental: Master

The character uses the Level 9 row of the Good table, even though they are Character Level 12.

3. Full, Mediocre, and Bad Progression

I agree with replacing “Paths” with Classes, including Prestige Classes.

The progression tracks could be:

Good Spellcasting
Mediocre Spellcasting
Bad Spellcasting
No Spellcasting

The important question is how the tracks behave in multiclassing.

Proposed class notation

Each class should explicitly state:

text
Spellcasting:
  Advances Good Spellcasting Progression

or:

Spellcasting:
  Advances Mediocre Spellcasting Progression

or:

Spellcasting:
  Advances Bad Spellcasting Progression

or:

Spellcasting:
  Does Not Advance Spellcasting Progression

This is clearer than requiring players to infer a caster level from class descriptions.

4. Multiclassing

Your intended model appears to be:

Each class level contributes to the character’s shared Spellcasting Progression according to the progression track specified by that class.

The cleanest implementation is to use separate advancement columns on the class table.

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

A multiclass character records their advancement in the relevant tracks.

Example: Wizard 5 / Fighter 3
text
Good progression:
  5 levels

No progression:
  0 levels

Result:

text
Use the Good progression at Spellcasting Progression Level 5.

The Fighter levels contribute no slots but provide their other class features.

Example: Wizard 5 / Paladin 3
text
Good progression:
  5 levels

Mediocre progression:
  3 levels

There are two possible ways to combine this.

Method A: Primary-track method

Use the best progression track only:

text
Good 5 + Mediocre 3
  = Good 5

The Paladin contributes:

Divine, Life, War, or Guardian access.
Smite or Essence features.
Paladin acquisition mechanics.
Armor and weapon abilities.

This is the simplest and safest model.

Method B: Combined-track method

The secondary track contributes to the shared progression through a discrete combination table.

text
Good 5 + Mediocre 3
  = Good 6

or:

text
Good 5 + Mediocre 3
  = Good 5 with a support increase

This lets partial casting improve daily spell volume, but requires a multiclass combination rule.

Given your preference for simplicity, I recommend beginning with Method A:

The highest active Spellcasting Progression determines the shared slot pool. Secondary classes do not automatically add slots unless a class or Prestige Class explicitly says they do.

This prevents multiclass slot inflation while preserving all the other benefits of multiclassing.

5. Why This Is Simpler Than My Earlier Package Model

The earlier package model required categories such as:

text
Full
Full Plus
Partial
Partial Plus
Limited
Limited Plus

Your model instead says:

text
Which Spellcasting Progression Level does the class advance?

The character then reads one row from one table.

Example:

text
Wizard 7 / Fighter 5
Spellcasting Progression Level: 7
Spell Slots: Read Good Progression Level 7

That is much easier to understand and maintain.

6. The Role of Mediocre and Bad Progression

The main unresolved issue is whether Mediocre and Bad tracks are:

Used only by characters whose strongest casting class is Mediocre or Bad; or
Combined with Good progression during multiclassing.

For the first version, I recommend:

Primary-track rule

The character uses the best Spellcasting Progression they possess:

text
Good > Mediocre > Bad > None

If the character has one or more Good classes:

Good progression determines slots.
Mediocre and Bad classes do not add slots automatically.
They may still add Traditions, spells, Essence features, and acquisition methods.

If the character has no Good class:

Their best Mediocre class determines the slot pool.
If they have no Mediocre class, their best Bad class determines it.

This makes the tracks useful without requiring a complicated combination formula.

Example
text
Paladin 8 / Ranger 8

Both are partial casters.

text
Result:
  Use the stronger of the Paladin and Ranger progression tracks.

If both are Mediocre, the character does not automatically become a Good caster.

text
Wizard 8 / Paladin 8
text
Result:
  Use Good progression at Level 8.

The Paladin contributes its non-slot features.

7. Prestige Classes

I agree that Prestige Classes should work exactly like Base Classes for spellcasting.

The only difference is access requirements.

A Prestige Class may say:

text
Spellcasting:
  Advances Good Spellcasting Progression

Requirements:
  Arcane: Expert
  Knowledge — Magic and Spellcrafting: Trained
  Ability to cast Expert spells

Or:

text
Spellcasting:
  Advances Mediocre Spellcasting Progression

Special:
  Adds Death and Spirit Tradition access.

A Prestige Class may also explicitly advance an existing progression:

text
Spellcasting:
  Continue your existing Good or Mediocre Spellcasting Progression.

However, we should avoid the ambiguous 3.5e phrasing “+1 level of existing spellcasting class.” Use explicit terms:

text
This class advances your Good Spellcasting Progression by 4 levels.

or:

text
This class advances the Spellcasting Progression already granted by one of your previous classes.
8. Tradition Rank and Spell Slots

I agree with your decision:

Tradition Rank does not limit the highest slot a character can use.

It limits spell access and scaling, not slot access.

Example:

text
Character:
  Good Spellcasting Progression Level 10
  Arcane: Expert
  Death: Trained

The character possesses the full Level 10 shared slot pool, including high-circle slots.

They may use those slots to cast:

Expert Arcane spells.
Trained Death spells.
Other spells from sufficiently ranked Traditions.

They cannot cast Master Death spells because Death is only Trained.

Why this is acceptable

It creates an intentional build distinction:

text
High Spellcasting Progression:
  Large daily resource pool.

High Tradition Rank:
  High-quality, high-scaling spells.

Broad Tradition investment:
  Many types of spells.

Focused Tradition investment:
  Deep scaling in one magical field.

A character could have powerful slot volume but shallow Tradition mastery. That is not a flaw; it is a possible multiclass or poorly optimized build.

However, class design should normally ensure that a full caster’s primary Tradition advances at a reasonable rate.

9. Lower-Circle Spells in Higher-Circle Slots

Since higher slots do not automatically improve spells, we need to decide what happens when a character spends a higher-circle slot on a lower-circle spell.

I recommend:

A spell may be cast using any slot of equal or higher Circle, but the spell uses its normal version unless its entry specifically defines a Heightened version.

Example:

text
Cure Wounds:
  1st Circle
  Heightened at 3rd Circle: affects more targets
  Heightened at 5th Circle: restores a severe wound

Fireball:
  3rd Circle
  No automatic improvement from a 4th-Circle slot.
  Specific Heightened versions may be added later.

This gives higher slots flexibility without making every low-circle spell automatically scale.

It also preserves the D&D 3.5e-style principle you identified:

Intrinsic spell improvement comes from Tradition Skill/Caster Level, not merely from spending a higher slot.

10. Mythic Advancement

Your Mythic solution is elegant:

Mythic advancement does not add new ordinary spell slots. It grants access to Epic Traditions and Epic Spells that use the existing slot pool.

This avoids creating a second resource table at Level 21+.

A Mythic spell could have requirements such as:

text
Requires:
  Legendary or Mythic Tradition Rank
  Access to an Epic Tradition
  One 7th-, 8th-, or 9th-Circle slot
  Essence expenditure
  Special ritual, focus, or component

Epic Traditions might include:

Creation
Time
Space
Order
Chaos
Void
Cosmic Celestial
Divine Authority

The important distinction is:

text
Mythic:
  Expands what spells exist and what they can do.

Not necessarily:
  Adds more ordinary daily slots.
11. Revised OD-001A Answers
Slot quantity

Use the proposed modified 3.5e table as the Good Spellcasting Progression.

Create corresponding:

Mediocre Spellcasting Progression.
Bad Spellcasting Progression.
No Spellcasting Progression.
Class contribution

Each class explicitly states which Spellcasting Progression it advances.

No fractional caster levels are displayed or calculated during play.

Full, mediocre, bad, and noncasting tracks

Yes. They are distinct named progression tracks.

Multiclassing

Recommended initial rule:

The character uses the strongest Spellcasting Progression they possess at the number of levels invested in that progression. Secondary casting classes do not automatically stack additional slots, but may grant Traditions, spells, acquisition methods, Essence features, and class abilities.

This is the simplest first implementation.

Tradition Rank and maximum slot

Tradition Rank does not limit slot access. It limits:

Which spells can be accessed.
Which spells can be prepared and cast.
How strongly those spells scale.
Advanced Classes and Prestige Classes

They may increase:

Spellcasting Progression.
Tradition Rank.
Tradition access.
Spell acquisition.
Essence capacity.
Metamagic.
Special spell permissions.

They do not necessarily need to increase all of these.

Mythic

Mythic advancement grants Epic Traditions and Epic Spells using the existing slot pool. It does not automatically create a new tier of ordinary spell slots.

12. One Important Clarification

The phrase “the class advances the character’s Spellcasting Progression” should be defined carefully.

I recommend that every class table include a field like:

text
Spellcasting Progression:
  Good
  Mediocre
  Bad
  None

Then also include:

text
Primary Tradition:
  Divine

Tradition Access:
  Divine, Life, Spirit

Spell Acquisition:
  5 spells per class level

Essence:
  Grants Essence features at Levels 2, 6, and 10

That makes the class’s magical contribution transparent.

The only remaining major question inside this model is whether secondary Mediocre or Bad casting ever improves the shared pool when a character already has Good casting. My recommendation is to exclude that in the initial version and let secondary classes contribute through Traditions, spells, acquisition, and Essence instead. That gives us a clean baseline to playtest before adding more multiclass complexity.
