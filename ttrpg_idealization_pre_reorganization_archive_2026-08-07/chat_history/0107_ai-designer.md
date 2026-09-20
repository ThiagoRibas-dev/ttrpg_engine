---
turn: 107
role: "AI-Designer"
source: chat_history.json
---

# Turn 107 — AI-Designer

That is the exact pressure point in Model D. If a Tradition is shared by two classes, the Tradition itself cannot determine the preparation method.

The solution is to distinguish:

text
Tradition:
  Which magical field the spell belongs to.

Spellcasting Profile:
  Which class/path method is being used to prepare and cast it.

Spell List:
  Which specific spells that profile grants access to.
Recommended Rule: Preparation Provenance

When a character prepares a spell, they choose which Spellcasting Profile is preparing it.

That choice is recorded for the day.

A spell’s Tradition provides access. Its preparation provenance determines the preparation and casting method.

Example

A character is:

text
Cleric 3 / Wizard 3

They have:

text
Death: Expert
Divine Profile
Wizard Profile
Shared Spell Slots

Both Cleric and Wizard grant access to the Death Tradition.

The character prepares:

text
Animate Dead — Wizard Profile
Speak with Dead — Cleric Profile
Death Ward — Cleric Profile
Wither — Wizard Profile

All four spells use the shared spell-slot pool, but they retain their preparation provenance.

What Does Preparation Provenance Affect?

The profile used to prepare the spell determines:

Which spell list the character accesses.
Required implement or focus.
Preparation time and method.
Which class features modify the spell.
Which metamagic or profile abilities apply.
Whether the spell can be cast as a reaction.
Whether the spell has profile-specific manifestations.
Which Tradition access granted by the profile qualifies.

The spell itself still uses the same:

School.
Tradition.
Mantles.
Traits.
Spell rank.
Base effect.
Example: Shared Death Tradition, Different Spell Lists
Cleric Profile

The Cleric’s Death access might include:

Speak with Dead
Death Ward
Gentle Repose
Banish Undead
Restore Life
Consecrate or Desecrate

The Cleric prepares these through:

Prayer
Sacred rites
Divine authority
A deity, pantheon, or cosmic principle
Wizard Profile

The Wizard’s Death access might include:

Animate Dead
Wither
Death Smoke
Soul Cage
Corpse Preservation
Life Drain

The Wizard prepares these through:

Spellbook study
Formulae
Research
Material components
Arcane manipulation

Both profiles access Death, but they do not necessarily access the same Death spells.

What If Both Profiles Grant the Same Specific Spell?

Suppose both Cleric and Wizard can prepare Speak with Dead.

The character chooses one provenance when preparing it:

text
Speak with Dead — Cleric Profile

or:

text
Speak with Dead — Wizard Profile

The effect remains fundamentally the same, but the casting expression and profile interactions differ.

Cleric preparation
May use a holy symbol.
May receive a Divine feature interaction.
May be affected by deity restrictions.
May qualify for a Divine or Death feat.
Wizard preparation
May use a grimoire or arcane focus.
May qualify for Arcane metamagic.
May be modified by Rune or Arcane class features.
May be cast as part of a researched ritual.

This gives the player a meaningful choice without requiring two separate versions of the spell.

Shared Slot Use

The spell slot is not divided by profile.

Example:

text
Shared daily slots:
  Novice: 3
  Expert: 2

Prepared spells:

text
Cleric Profile:
  Speak with Dead
  Death Ward
  Cure Wounds

Wizard Profile:
  Animate Dead
  Wither
  Arcane Barrier

The character may cast any compatible prepared spell using the appropriate slot.

The slot does not care whether the spell came from Cleric or Wizard. The spell’s preparation provenance still determines the profile-specific rules.

Why This Is Better Than “Choose One Preparation Method”

A single dominant preparation method creates unnecessary problems:

text
Cleric 3 / Wizard 3

would have to choose:

Either all spells prepare as Cleric spells;
Or all spells prepare as Wizard spells.

That makes shared Traditions awkward and makes multiclassing feel like one class has overwritten the other.

Preparation provenance allows:

Cleric spells to remain Cleric spells.
Wizard spells to remain Wizard spells.
Shared Traditions to work naturally.
One unified slot pool.
Class identity to survive multiclassing.
Why This Does Not Create Double Preparation

The character does not get to prepare the same spell twice for extra benefit.

Each spell occupies one preparation entry, regardless of how many profiles grant it.

If both profiles grant Death Ward, the character can prepare:

text
Death Ward — Cleric Profile

or:

text
Death Ward — Wizard Profile

but not both unless they deliberately want two prepared copies, and even then both copies would draw from the same shared slot pool.

A spell is therefore a single prepared object with one provenance.

Alternative: Spellbook and Divine List Intersection

We can formalize preparation access through a list intersection.

A character’s final spell access is:

text
Tradition Skill
+ Spellcasting Profile
+ Specific Profile Spell List

For each spell:

text
If Profile A grants the spell:
  It may be prepared through Profile A.

If Profile B grants the spell:
  It may be prepared through Profile B.

If both grant the spell:
  The player chooses provenance during preparation.
What About a Spell from a Tradition the Profile Does Not Normally Use?

Suppose a character has:

text
Wizard Profile
Arcane: Expert
Death: Expert

but Wizard does not normally grant Death.

The character still cannot prepare Death spells merely because they have the skill. They need one of:

A Cleric or Death path.
A feat granting Death Profile access.
A Prestige Class.
A patron or mentor.
A class feature that expands Wizard Tradition access.
A special item or institution.

This maintains the distinction between:

text
Tradition Competency:
  How well you know Death.

Profile Access:
  Whether this class/path lets you prepare Death spells.
Shared Tradition Does Not Mean Shared Spell List

This is important.

If Cleric and Wizard both have Death, that means:

Both classes participate in the Death Tradition.

It does not mean:

Both classes automatically receive the same complete Death spell list.

Each class profile can emphasize different parts of the Tradition.

For example:

Tradition	Cleric Emphasis	Wizard Emphasis
Death	Repose, protection, judgment, resurrection	Corpse manipulation, decay, soul theory
Life	Healing, restoration, blessing	Mutation, vitality transfer, biological alteration
Spirit	Exorcism, guidance, communion	Binding, summoning, possession
Elemental	Sacred storms, divine fire	Formulaic energy manipulation
Shadow	Protection from darkness, concealment	Illusion, entropy, shadow substance
Interaction with Tradition Rank

The character’s Tradition Rank remains one value:

text
Death: Expert

The profile determines which spells are available; the Tradition Rank determines whether the character can use a spell of the required rank.

Example:

text
Death: Trained
Spell Capacity: Expert

The character may have access to an Expert Death spell through a profile, but cannot cast it because their Death mastery is only Trained.

Conversely:

text
Death: Expert
Spell Capacity: Trained

The character understands Expert Death magic but lacks the daily spell capacity to cast Expert spells.

This is a useful distinction between:

Knowledge and skill.
Magical availability.
Daily power volume.
Final Model

The cleanest structure is:

text
Tradition:
  The magical field shared by multiple classes.

Spellcasting Profile:
  The class/path-specific method and spell list.

Preparation Provenance:
  Which profile prepared this specific spell today.

Tradition Rank:
  The character’s skill and casting proficiency in that Tradition.

Shared Spell Slots:
  The universal daily casting resource.

Spell:
  School + Traditions + Mantles + Traits.
Example
text
Character:
  Cleric 3 / Wizard 3
  Death: Expert
  Divine Profile
  Wizard Profile
  Shared Expert Slots

Prepared:
  Death Ward — Cleric Profile
  Speak with Dead — Cleric Profile
  Animate Dead — Wizard Profile
  Wither — Wizard Profile

All four spells use the shared slot pool. Each retains the preparation method and class interactions of the profile that prepared it.

This resolves the multiclass problem without forcing shared Traditions to have a single universal preparation method.
