---
turn: 111
role: "AI-Designer"
source: chat_history.json
---

# Turn 111 — AI-Designer

Yes. This solves the conundrum much more cleanly than the Profile/Provenance model.

The key change is:

Classes grant access to Traditions and grant acquisition/preparation features, but they do not own spell lists or casting methods.

There is one universal spellcasting system.

Simplified Magic Architecture
1. Shared Spell Slots

All spellcasters use one shared pool of daily spell slots organized by Spell Rank.

text
Novice Slots: 3
Expert Slots: 2
Master Slots: 1

A character can spend any appropriate slot on any prepared spell they know.

There are no separate:

Cleric slots
Wizard slots
Death slots
Arcane slots
Prepared-caster slots
Spontaneous-caster slots

The character simply has a shared daily pool.

2. Fixed Tradition Spell Lists

Each Tradition has one fixed spell list.

text
Death Tradition:
  Animate Dead
  Speak with Dead
  Death Ward
  Wither
  Life Drain
  Soul Cage
  ...

Death is the same Tradition regardless of how the character accessed it:

Cleric
Wizard
Death prestige class
Feat
Ancestry
Mentor
Relic

The source of access does not create a different version of Death.

3. Tradition Skills Control Magical Competence

Each Tradition is an individual skill.

text
Arcane: Expert
Death: Trained
Life: Master
Rune: Untrained

Tradition Competency determines:

The highest spell rank the character can cast through that Tradition.
The casting pool and Competency Floor.
Automatic scaling of spells.
Access to Tradition feats.
The character’s ability to perform difficult casting.

This uses the existing skill system rather than introducing a separate caster-level statistic.

4. Spell Slots Control Daily Volume

Tradition Skill determines what the character can cast.

Shared Spell Slots determine how many spells they can cast per day.

Example:

text
Death: Expert
Life: Trained
Spell Slots:
  Novice: 3
  Expert: 2

This character can cast:

Expert Death spells.
Novice Life spells.
No Master spells.
A total number of times determined by their shared slots.

This preserves the distinction between:

Magical competence.
Daily magical endurance.
D&D 3.5e-Style Spell Scaling

This is also a good solution.

A spell’s effect scales with the caster’s Tradition Skill, not with the slot used.

For example:

text
Death: Trained
Animate Dead:
  Uses the Trained version.

Death: Expert
Animate Dead:
  Uses the Expert version.

Death: Master
Animate Dead:
  Uses the Master version.

Casting a Novice spell with an Expert slot does not automatically improve it.

This preserves the D&D 3.5e distinction between:

Caster-level scaling.
Spell-slot level.
Metamagic or deliberate spell modification.

In our terminology:

Tradition Competency determines the spell’s intrinsic scale. Spell Rank determines the spell slot consumed.

Multiclassing

Your Cleric/Wizard example now works naturally.

Cleric/Wizard Example
text
Character:
  Cleric 3 / Wizard 3

Tradition Skills:
  Divine: Expert
  Death: Expert
  Arcane: Trained
  Rune: Trained

Shared Slots:
  Novice: 3
  Expert: 2

The character has:

One Death spell list.
One Arcane spell list.
One Divine spell list.
One shared slot pool.
One preparation system.
One acquisition record for each spell.

They can prepare spells from any Tradition in which they have access and sufficient investment.

Class acquisition features

The classes do not grant different spell lists. They grant different ways to expand the character’s overall spell collection.

Wizard level

Might grant:

Learn two spells.
Research additional spells.
Copy spells from scrolls.
Learn spells from a spellbook.
Analyze magical effects.
Exchange spells through experimentation.
Cleric level

Might grant:

Learn five spells.
Receive spells through prayer.
Gain access to a deity’s selected offerings.
Learn ritual or sacred spells.
Acquire spells through religious instruction.
Receive new spells from divine revelation.

Both sets of features operate on the same universal spell collection.

What the Character Actually Tracks

A character sheet might show:

text
Traditions:
  Arcane — Expert
  Death — Expert
  Divine — Trained
  Rune — Trained

Shared Spell Slots:
  Novice: 3
  Expert: 2

Prepared Spells:
  Arcane:
    Detect Magic
    Force Bolt

  Death:
    Speak with Dead
    Death Ward

  Divine:
    Bless
    Cure Wounds

Acquisition Features:
  Wizard:
    Research
    Scroll transcription
    Learn 2 spells per Wizard level

  Cleric:
    Prayer
    Divine revelation
    Learn 5 spells per Cleric level

There is no need to track:

text
Death — Cleric
Death — Wizard
Death Caster Level
Wizard Death Slots
Cleric Death Slots
What Happens When Both Classes Grant the Same Tradition?

Nothing special happens.

If both Cleric and Wizard grant Death:

The character has one Death skill.
The character has one Death spell list.
The character may invest in Death through either class, if both provide access.
Both classes’ acquisition mechanics can add Death spells to the same spell collection.
The character may use any shared spell slot to cast a prepared Death spell.

The classes may differ in how many spells they add, but not in the content of the Death Tradition.

Your Specialization Trade-Off

This produces the intended strategic tension.

Pure Wizard
text
Wizard 6

Traditions:
  Arcane: Expert
  Rune: Expert
  Elemental: Expert
  Space: Expert

Acquisition:
  Strong research and scroll mechanics.
  Moderate number of spells learned per level.

Result:
  Fewer acquisition engines.
  Deeper Tradition investment.
  Broad magical specialization through several Traditions.
Cleric/Wizard
text
Cleric 3 / Wizard 3

Traditions:
  Death: Expert
  Divine: Expert
  Arcane: Trained
  Life: Trained

Acquisition:
  Wizard research and scroll learning.
  Cleric prayer and revelation.
  More varied acquisition mechanics.
  Fewer opportunities to maximize every Tradition.

Result:

More class mechanics.
More ways to acquire spells.
More potential for unusual spell access.
Fewer Traditions at maximum competency.

That is a very desirable multiclass trade-off.

One Necessary Rule: Spell Duplication

Because a spell may belong to more than one Tradition, we need a simple acquisition rule.

Suppose Cure Wounds belongs to:

text
Divine, Life, Primal, Spirit

If the character learns it through Divine, they should not need to learn it again through Life.

Recommended rule:

A spell is learned once. If the character has access to at least one of its Traditions, they may prepare and cast it if their Tradition Competency meets the spell’s requirement.

However, this creates a possible edge case: a character may lose access to one Tradition later.

We can handle that with:

A learned spell remains known, but the character must have at least one currently active compatible Tradition to prepare or cast it.

Example:

text
Cure Wounds:
  Learned through Divine.

Divine access later lost:
  Life remains active.

Result:
  Cure Wounds can still be prepared through Life.

This reinforces the usefulness of multi-Tradition spell tags.

One Necessary Rule: Acquisition Does Not Equal Competency

A class may teach a character a spell from a Tradition they are only Trained in.

For example:

text
Wizard learns Death spell from a scroll.
Death: Trained.
Spell: Expert Death spell.

The character knows the spell but cannot currently cast it because their Death Tradition competency is insufficient.

If Death later advances to Expert, the spell becomes usable.

This creates useful long-term spellbook development without allowing acquisition to bypass skill requirements.

One Necessary Rule: Spell Rank versus Tradition Rank

The clean gate should be:

Tradition Competency	Highest Usable Spell Rank
Untrained	None
Trained	Novice
Expert	Expert
Master	Master
Legendary	Heroic/Legendary

The character’s available slot pool must also contain a slot of that rank.

A character with:

text
Death: Expert

but no Expert slots cannot cast Expert Death spells.

A character with:

text
Death: Trained
Expert slots available

still cannot cast Expert Death spells.

Final Assessment

Yes, this resolves the earlier problem.

The final model becomes:

text
Classes and Paths:
  Grant Tradition access.
  Grant spell acquisition methods.
  Grant shared slot progression.
  Grant class features and special casting options.

Traditions:
  Individual skills.
  One fixed spell list each.
  Shared across all classes.
  Determine spell access, competence, and scaling.

Spell Collection:
  One unified collection of learned spells.

Preparation:
  One universal preparation system.
  Character prepares spells from any accessible Tradition.

Spell Slots:
  One shared daily pool by Spell Rank.

Essence:
  Fuels 0th-rank spells, metamagic, casting stability,
  and supernatural class features.

Psychic/Psionic:
  Potentially a separate Essence-based system.

Spells:
  School + Tradition(s) + Mantle(s) + Trait(s).

The previous Spellcasting Profile and Preparation Provenance models are no longer necessary. The major remaining OD-001 task is now to define:

The shared spell-slot progression.
The universal preparation rules.
Spell acquisition rules.
How class/path levels contribute slots without fractional caster levels.
How Tradition Competency automatically scales spell effects.
