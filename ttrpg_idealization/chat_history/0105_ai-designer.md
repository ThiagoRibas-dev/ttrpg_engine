---
turn: 105
role: "AI-Designer"
source: chat_history.json
---

# Turn 105 — AI-Designer

Those are important corrections. I agree that our earlier formulation mixed together three separate questions:

How much does the character know about a Tradition?
What spells can the character access?
How many spells can the character prepare or cast per day?

We should not introduce a generic Spell Capacity stat until we determine whether the existing Tradition ranks and class progression can handle those functions.

1. Tradition Competency versus Spell Rank

Using the highest Tradition mastery alone is attractive, but it creates a problem:

Competency Rank measures proficiency and investment, not necessarily daily magical volume.

A character could have:

text
Arcane: Expert

but that does not tell us whether they can:

Cast three spells per day or ten.
Prepare one spell or twenty.
Cast Novice, Expert, or Master spells.
Cast repeatedly under pressure.
Use metamagic.

Therefore I recommend separating the concepts without necessarily creating a new visible stat.

Tradition Competency

The individual skill rank:

text
Arcane: Trained
Divine: Expert
Life: Master

Determines:

Casting pool.
Competency Floor.
Whether the character can use the Tradition reliably.
Which Tradition feats are available.
Which spell ranks can be cast through that Tradition.
Class/Path Spellcasting Track

A class or path grants an invisible or derived progression that determines:

Number of spell slots.
Daily spell volume.
Whether the character prepares, knows, or receives spells.
Whether the character is a full caster, partial caster, or noncaster.

This does not need to be called Spell Capacity on the character sheet. It can be represented as:

text
Class Spellcasting Track: Full
Class Spellcasting Track: Partial
Class Spellcasting Track: None

or as class/path features:

text
Wizard Path:
  Grants Novice spell slots at Level 1.
  Grants Expert spell slots at Level 5.
  Grants Master spell slots at Level 9.

So the clean distinction becomes:

Tradition skill = quality and access.
Class/path spellcasting track = quantity and daily structure.

This is similar to the existing decision that class protects core combat or spell mastery while general skills provide specialization.

2. Can Tradition Rank Determine Spell Rank?

Yes, but I would use Tradition Rank as a gate, not as the entire spellcasting progression.

Possible gate:

Tradition Rank	Highest Spell Rank Available
Untrained	No spells
Trained	Novice spells
Expert	Expert spells
Master	Master spells
Legendary	Heroic or Legendary spells

This is elegant and uses the existing Competency Rank system.

However, access alone does not grant slots.

A character might have:

text
Life: Master

but only one Master spell slot because their current class/path has limited spellcasting capacity.

Another character might have:

text
Life: Trained

but several Novice slots because they are a specialized low-level caster.

Thus:

text
Tradition Rank:
  Determines spell-rank access and casting quality.

Class/Path Track:
  Determines how many slots and what preparation structure are available.
3. The Multiclassing Problem

You are right that “unified spell slots” and “distinct preparation methods” create tension during multiclassing.

Consider:

text
Level 1 Cleric
Level 2 Wizard

The character has:

Divine access.
Life or Spirit access.
Arcane access.
Possibly a prayer-based preparation method.
Possibly a spellbook-based preparation method.

The core question is:

Does this character have one shared magical resource system, or multiple separate class spellcasting systems?

There are four major models.

4. Model A: Separate Class Spellcasting Pools

Each class grants its own slots.

text
Cleric 1:
  Divine Novice slots

Wizard 1:
  Arcane Novice slots

The multiclass character tracks both pools separately.

Advantages
Maximum class identity.
Cleric and Wizard remain mechanically distinct.
Preparation methods remain fully distinct.
Easy to prevent cross-class exploitation.
Closest to traditional class separation.
Disadvantages
More bookkeeping.
Multiclass casters track several slot tables.
Lower-level slots may become clutter.
Spell resources can become inefficient or awkward.
A character may have unused Divine slots while desperately needing Arcane slots.

This is the most granular model, but probably too cumbersome as the baseline.

5. Model B: One Shared Slot Pool, One Unified Preparation Method

All spells use one universal spell-slot table, and multiclass characters choose one preparation method.

For example:

text
Cleric 1 / Wizard 1:
  Uses one shared spell-slot progression.
  Chooses either:
    Prepared Spellbook
    Prepared Divine List

The character may know Divine and Arcane spells, but prepares all of them through one chassis.

Advantages
Very simple.
Easy multiclassing.
One slot table.
Clear character identity.
Disadvantages
The character must choose which class’s preparation method dominates.
Some class features may become inaccessible or awkward.
A Cleric/Wizard may feel like “a Wizard with Divine spells.”
Switching preparation methods may create abuse.

This is simple but does not fully preserve both class identities.

6. Model C: One Shared Slot Pool, Multiple Preparation Methods

This is the model you are questioning, but it can work if we define slots and preparation as separate layers.

Slots

The character has one shared pool:

text
Novice Slots: 3
Expert Slots: 2
Preparation

Each class or path tells the character how they prepare the spells they access.

text
Wizard:
  Prepare spells from a spellbook.

Cleric:
  Prepare spells through prayer.

Druid:
  Prepare spells through communion with Nature.

Warlock:
  Receive a fixed repertoire from a patron.

A Cleric/Wizard could prepare:

text
Arcane spells from a spellbook.
Divine spells through prayer.

Both use the same shared slots when cast.

Example
text
Cleric 1 / Wizard 1

Prepared Arcane spells:
  Arcane Barrier
  Force Bolt

Prepared Divine spells:
  Bless
  Cure Wounds

Shared daily slots:
  Novice Slot 1
  Novice Slot 2
  Novice Slot 3

The character can cast any prepared spell using an appropriate slot.

Advantages
One slot pool.
Distinct preparation methods remain meaningful.
Strong multiclass identity.
Closest to the desired compromise.
Supports spellbook, prayer, repertoire, pact, and ritual methods.
Disadvantages
Can allow a character to access the strongest preparation features from several classes.
Requires rules for how many spells each class grants.
Requires rules for how spell lists combine.
A character may become extremely flexible.
Required limitation

Preparation methods should be attached to class/path features, not automatically inherited in full through a one-level dip.

For example:

Wizard 1 grants a small spellbook.
Wizard 4 grants broad spellbook preparation.
Cleric 1 grants a limited prayer list.
Cleric 4 grants broader Divine preparation.
A character cannot gain the full Wizard preparation chassis from one level of Wizard.

This model is viable and probably our best candidate.

7. Model D: Shared Slots, Separate Spellcasting Profiles

This is a stricter version of Model C.

The character has one shared daily resource pool, but each spellcasting profile has its own preparation and casting permissions.

text
Spellcasting Profiles:
  Wizard Profile
  Cleric Profile

Each profile defines:

Which Traditions it can prepare.
Whether it uses a book, prayer, repertoire, or pact.
Which spell ranks it can access.
What casting implements it requires.
Which class features affect it.

The slots are shared, but the profile remains distinct.

Example
text
Shared Slots:
  Novice: 3
  Expert: 1

Wizard Profile:
  Arcane and Rune access.
  Spellbook preparation.
  Arcane casting feats.

Cleric Profile:
  Divine and Life access.
  Prayer preparation.
  Divine channeling feats.

This is more technical, but it handles multiclassing cleanly.

8. My Recommendation

I recommend Model D, presented to players as a simpler version of Model C:

Characters have one shared spell-slot pool, but each class/path grants a distinct Spellcasting Profile that defines preparation, access, and casting permissions.

This preserves:

Unified slot progression.
Distinct preparation methods.
Multiclass flexibility.
Class identity.
Tradition-based access.
No separate caster level for every Tradition.
9. What Determines the Shared Slot Pool?

The shared slot pool should be generated from class/path contributions, not from Tradition ranks alone.

Each class/path has a Spellcasting Track:

text
Full Casting
Partial Casting
Limited Casting
No Casting

A full caster path contributes strongly to the shared slot progression. A partial caster path contributes less. A noncaster contributes nothing.

The character’s total spellcasting progression is derived from the class/path bands they have selected.

However, the table should not require fractional caster levels. We can use discrete progression thresholds.

Example:

Spellcasting Contribution	Result
None	No slots
Limited	0th-rank Essence effects and a few Novice slots
Partial	Novice and Expert slots at slower progression
Full	Complete Novice through Legendary progression

At each modular path boundary, the character’s combined spellcasting track advances according to a fixed table.

10. Tradition Rank as the Spell Gate

A spell requires both:

A compatible Spellcasting Profile.
Sufficient Tradition Rank.

Example:

text
Spell: Fireball
School: Evocation
Traditions: Arcane, Elemental, War
Required Tradition Rank: Expert
Required Slot: Expert

A character could cast it if they have:

text
Arcane: Expert

or:

text
Elemental: Expert

or:

text
War: Expert

provided they have a spellcasting profile that grants access to that Tradition.

This creates useful distinctions:

text
Wizard 5:
  Arcane: Expert
  Spellcasting Profile: Wizard
  Can cast Arcane Expert spells.

Cleric 5:
  Divine: Expert
  Spellcasting Profile: Cleric
  Cannot cast Fireball unless Cleric also has Elemental or War access.

Cleric 3 / Wizard 2:
  Divine: Trained
  Arcane: Trained
  Spellcasting Profiles: Cleric and Wizard
  Can cast Novice Divine and Arcane spells.
11. Spell Preparation under the Recommended Model

A character may have more than one preparation method, but each method remains bounded by its profile.

Wizard Profile
Maintains a spellbook.
Prepares a daily selection from the spellbook.
May learn spells through research, scrolls, mentors, and experimentation.
Cleric Profile
Prepares from the Divine or deity-approved list.
May change the daily list through prayer.
May have access to specific deity, Celestial, or Mantle spells.
Nature Profile
Prepares through communion with the natural world.
May prepare spells from Nature, Elemental, Spirit, and Life.
May require a living environment, seasonal connection, or natural focus.
War Profile
May prepare a small fixed list of combat spells.
May cast certain spells as reactions or weapon-linked effects.
May use weapons as implements.
Rune Profile
Prepares spells by inscription.
Some spells may be stored in objects rather than memorized.
Preparation may take longer but create persistent effects.
12. Essence and Psychic Power

Your clarification works well:

Psychic/Psionic power can be a purely Essence-based system.

That gives it a distinct identity without requiring a decision now.

Potential future structure:

text
Psychic Power:
  No daily spell slots.
  Uses Essence directly.
  Powers are Disciplines rather than prepared spells.
  Stronger effects require more Essence or augmentation.
  Excessive use may cause Strain.

The exact costs and augmentation rules can remain part of a later subsystem.

13. Updated OD-001 Resolution
Agreed
Traditions are individual skills.
Classes and paths grant Tradition skill access.
Tradition skills use normal Competency Ranks.
Primary Tradition mastery is protected by class/path progression.
General investment can specialize secondary Traditions.
Essence replaces Focus.
Essence remains separate from Stamina.
Essence powers 0th-rank spells, metamagic, casting stability, and supernatural features.
Advanced Traditions are accessed through Prestige Classes, Paths, Feats, and similar permissions.
Celestial is folded into Divine as a specialization.
Nature replaces Primal as the formal tradition name.
Traditions have no unique subsystems for now.
Psychic/Psionic power may use a purely Essence-based system.
Recommended working model
Do not create an independent caster level for every Tradition.
Tradition Rank gates spell-rank access and determines casting quality.
Class/path Spellcasting Profiles determine preparation method and class-specific permissions.
Class/path spellcasting contributions determine one shared spell-slot pool.
Multiclass characters may possess multiple Spellcasting Profiles.
The shared slot pool is used by all compatible prepared spells.
Preparation remains profile-specific.

The remaining major design task is therefore:

Build the shared spell-slot progression and define how modular class/path contributions combine into that progression without fractional caster levels or multiclass exploits.
