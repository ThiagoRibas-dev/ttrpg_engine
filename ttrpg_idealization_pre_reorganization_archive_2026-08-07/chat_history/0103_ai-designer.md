---
turn: 103
role: "AI-Designer"
source: chat_history.json
---

# Turn 103 — AI-Designer

Excellent. This gives us a clear foundation for OD-001. The key architectural principle is:

Traditions are individually ranked skills. Classes and paths determine which traditions can receive investment. Spell capacity is a separate class/path progression.

That preserves the granular multiclassing of D&D 3.5e without requiring every tradition to have its own independent spell-slot table.

OD-001 Revised Foundation
1. Tradition Access

Traditions function like other skills, but access to them is controlled by class and path.

Each class or path provides:

A list of available Tradition skills.
A number of skill allocations.
Possibly a minimum Tradition Rank for specific spells or feats.
Potentially one or more automatic Tradition advancements.
Example
text
Cleric Class Skill List:
  Divine
  Life
  Spirit
  Death
  Rune
  Knowledge — Religions and Rites

Wizard Class Skill List:
  Arcane
  Rune
  Space
  Time
  Elemental
  Knowledge — Magic and Spellcrafting

Rogue Class Skill List:
  Shadow
  Dream
  Rune
  Space
  Knowledge — Languages and Scripts

A character may only invest general or class-granted skill points into a Tradition if the current class or path grants access to it.

Multiclass example
text
Level 1: Cleric
  Divine: 1 point
  Life: 1 point

Level 2: Wizard
  Arcane: 1 point
  Rune: 1 point

Final Tradition investment:
  Divine: Trained
  Life: Trained
  Arcane: Trained
  Rune: Trained

Or, if the character invests twice into one Tradition:

text
Divine: Expert
Life: Trained
Arcane: Trained
Rune: Untrained

This supports highly granular hybrid characters without requiring a separate class-specific spell list.

2. Tradition Skill Progression

I recommend using the same Competency Rank structure as every other skill:

Rank	Meaning
Untrained	No formal Tradition training
Trained	Basic ability to use the Tradition
Expert	Reliable specialist
Master	Major practitioner
Legendary	Mortal or near-mythic apex

However, we should distinguish two things:

Tradition Competency

This measures how well the character performs magic through a specific Tradition.

Example:

text
Arcane: Expert
Divine: Trained
Life: Master
Shadow: Untrained

It controls:

Casting pool volume.
Competency Floor.
Access to higher-quality applications.
Tradition-specific feats.
Ability to perform difficult spells.
Spell Capacity

This measures how much magical power the character can prepare and expend per day.

Example:

text
Spell Capacity: Expert

It controls:

Maximum spell rank.
Number of spell slots.
Daily preparation.
Number of spells available.
Possibly Focus/Essence capacity.

These should not be the same statistic.

A Level 10 character might have:

text
Spell Capacity: Master
Arcane: Trained
Divine: Expert

They can prepare powerful spells through their class track, but they are not equally skilled at casting every Tradition.

3. Individual Caster Levels

I would avoid the phrase caster level for every Tradition.

If each Tradition has its own caster level, we risk recreating:

text
Arcane Caster Level 4
Divine Caster Level 2
Life Caster Level 3
Spirit Caster Level 1

That is granular, but it creates:

Multiple parallel advancement tracks.
Confusion about spell rank versus casting proficiency.
Difficulty balancing multiclass characters.
A return to the 3.5e problem of tracking separate level-based progressions.

Instead, use three separate terms:

Character Level

Overall advancement from 1–20.

Tradition Rank

Investment-driven proficiency in a specific Tradition.

Spell Capacity

Class/path-driven access to spell ranks and daily spell slots.

The character sheet might show:

text
Character Level: 6
Spell Capacity: Veteran
Arcane Tradition: Trained
Divine Tradition: Expert
Life Tradition: Expert

This preserves the underlying granularity without requiring a separate “caster level” for every Tradition.

4. Recommended Tradition Advancement Model

Your two proposed models are:

Model A: Direct Skill Investment

Each level grants allocations that can be invested into available Tradition skills.

text
Level 1 Cleric:
  Invest one point into Divine.

Level 2 Wizard:
  Invest one point into Arcane.

Level 3 Cleric:
  Invest one point into Life.
Advantages
Maximum granularity.
Strong multiclass identity.
Closest to D&D 3.5e skill points.
Every level creates a meaningful choice.
Supports characters with unusual combinations.
Disadvantages
More bookkeeping.
More opportunities for inefficient builds.
Class skill lists become very important.
Players may delay core Tradition investment for utility skills.
Model B: Tier-Based Class Advancement

At certain class levels, a class grants automatic Tradition progression.

text
Wizard Level 1:
  Arcane becomes Trained.

Wizard Level 5:
  Arcane becomes Expert.

Wizard Level 9:
  Arcane becomes Master.

Wizard Level 15:
  Arcane becomes Legendary.
Advantages
Easier to manage.
Protects core class identity.
Similar to PF2e’s proficiency progression.
Prevents a primary caster from accidentally falling behind.
Disadvantages
Less granular.
More difficult to represent unusual hybrid casters.
Tradition rank becomes strongly tied to class.
Multiclassing can produce awkward breakpoint behavior.
Recommended Hybrid

Use both, but give them different jobs.

Automatic Class/Path Advancement

Classes automatically advance their primary Tradition at major boundaries.

text
Wizard:
  Arcane at Levels 1, 5, 9, 15

Cleric:
  Divine at Levels 1, 5, 9, 15

Druid:
  Nature at Levels 1, 5, 9, 15
General Skill Investment

Players may invest additional points into any Tradition granted by their current class or path.

This allows:

text
Wizard:
  Automatic Arcane advancement
  Optional Rune, Elemental, Space, or Time investment

Cleric:
  Automatic Divine advancement
  Optional Life, Spirit, Death, or Rune investment

This is consistent with the earlier attack/spell decision:

The class automatically protects core role mastery; skill investment provides specialization and multiclass customization.

5. Spell Preparation Structures

We should separate spell access from spell preparation style.

A Tradition determines which spells a character may learn. A class or path determines how those spells are prepared or accessed.

Possible preparation models include:

Prepared Spellbook

The character maintains a spellbook and chooses a daily subset.

Typical users:

Wizards
Arcane scholars
Rune practitioners
Researchers

Advantages:

Maximum flexibility.
Strong downtime and research identity.
Excellent for Arcane and Rune traditions.
Prepared Divine List

The character prepares from a broader Tradition list through prayer, ritual, or sacred communion.

Typical users:

Clerics
Priests
Divine champions

Advantages:

Strong Divine identity.
Allows daily adaptation.
Works well with Life, Death, Spirit, and Celestial specializations.
Repertoire or Known Spells

The character knows a fixed number of spells and can cast them spontaneously.

Typical users:

Sorcerers
Innate casters
Bloodline casters
Some Primal characters

Advantages:

Simple at the table.
Strong character identity.
Less daily bookkeeping.
Pact or Granted Spells

The character receives spells from a patron, spirit, deity, or supernatural source.

Typical users:

Warlocks
Spirit mediums
Celestial champions
Shadow initiates

Advantages:

Strong narrative relationship.
Allows unique access rules.
Useful for patron-based paths.
Recommended Structure

Use one universal Vancian slot progression, but allow several preparation interfaces:

text
Spell Capacity:
  Universal slot progression.

Preparation Method:
  Spellbook
  Prepared List
  Repertoire
  Pact/Granted
  Ritual/Inscription

This gives us 5e-like unified slot scaling without making every class feel identical.

6. Spell Slot Progression Options
Option A: Full D&D 5e-Style Unified Slots

All full casters use the same spell-slot progression.

Advantages:

Easy multiclassing.
Simple shared chart.
Familiar.
Prevents severe multiclass slot exploits.

Weaknesses:

A Cleric, Wizard, and Druid may feel too mechanically similar.
Does not naturally distinguish prepared, spontaneous, and ritual casters.
Half-casters and prestige casters need separate treatment.
Option B: PF2e-Style Rank-Based Slots

Spell ranks progress by level, usually with a fixed number of slots per rank.

Advantages:

Clear spell-rank structure.
Easy to represent heightened spells.
Strong bounded progression.
Good for high fantasy.

Weaknesses:

Less flexible for unusual multiclassing.
Can require tracking many rank rows.
Still tends toward class-defined spell capacity.
Option C: SotDL-Style Power Stat

A character has a Power or Spell Capacity value that determines the highest spell rank available.

Advantages:

Simple.
Strongly supports modular paths.
Natural for a 10- or 20-level game.
Easy to give partial casters reduced capacity.

Weaknesses:

Requires designing a new slot framework.
“Power” may feel like a numerical level separate from skill ranks.
Does not by itself determine how many spells are available.
Option D: Class Track Spell Capacity

Each class or path contributes a defined amount to a shared Spell Capacity track.

text
Full Caster Path:
  Strong Spell Capacity advancement

Half Caster Path:
  Medium Spell Capacity advancement

Noncaster Path:
  No Spell Capacity advancement

Multiclassing combines the contributions into one capacity result.

Advantages:

Closest to the existing Good/Okay/Bad class-track model.
Strongly supports modular paths.
Allows class identity without separate caster levels.
Works with unified slots.

Weaknesses:

Requires a careful shared cadence.
May recreate fractional caster-level problems if not abstracted cleanly.
Recommendation

Use a hybrid of Option C and Option D:

Spell Capacity is a shared class/path track, expressed as a bounded capacity tier rather than a separate caster level.

Classes and paths contribute to:

Maximum Spell Rank.
Number of slots.
Preparation breadth.
Focus/Essence capacity.
Tradition access.

The table should not require adding fractions or calculating caster levels.

Example:

text
Spell Capacity:
  Trained
  Veteran
  Master
  Hero
  Legend

A full Wizard path advances this track quickly. A Paladin path advances it more slowly. A Fighter path does not advance it unless a specialized path grants limited magic.

7. Focus, Essence, Mana, and Stamina

I recommend renaming Focus to:

Essence

Reasons:

“Focus” sounds like mental concentration.
The resource will power more than concentration.
Essence can represent magical force, spiritual reserve, and supernatural exertion.
It is clearly distinct from Stamina.
Keep Essence separate from Stamina

Do not unify Essence and Stamina.

Stamina

Represents:

Physical exertion.
Active Parry fatigue.
Athletics.
Heroic physical Die Step-Ups.
Martial overextension.
Sprinting and forced effort.
Essence

Represents:

Cantrips and 0th-rank spells.
Metamagic.
Casting under distraction.
Casting adjacent to enemies.
Emergency casting.
Maintaining concentration.
Turning or Rebuking Undead.
Smites.
Devotion feats.
Other supernatural exertion.

This preserves the existing zero-meta-currency principle because both are in-world resources.

Essence source

The current derivation is:

text
Essence = WIS + INT

That is appropriate for a universal supernatural resource, but it may be too generous to characters who are not spellcasters.

Possible solutions:

Universal Essence pool

Every character has Essence, but only supernatural abilities consume it.

Caster-only Essence pool

Only characters with magical or supernatural access derive Essence.

Base plus access

Every character has a small Essence reserve, expanded by:

Magic Mastery.
Class.
Feats.
Ancestry.
Special resources.

My recommendation is to retain a universal Essence track, but make magical access and supernatural feats determine what it can be spent on.

8. What Essence Does
Cantrips and Orisons

0th-rank spells consume Essence rather than daily slots.

This gives casters reliable low-level magical activity without creating unlimited free effects.

Metamagic

Metamagic feats spend Essence to modify a spell:

Change range.
Change area.
Alter damage type.
Remove verbal or somatic components.
Extend duration.
Split targets.
Protect allies.
Cast as a reaction.
Preserve a slot under difficult conditions.
Casting Interference

Essence may be spent to maintain a spell when:

Adjacent to an enemy.
Injured.
Distracted.
Restrained.
Forced to cast defensively.
Casting without an implement.
Casting in poor conditions.
Casting while maintaining another effect.
Supernatural Class Features

Essence may fuel:

Turn or Rebuke Undead.
Smites.
Devotion feats.
Arcane overcasting.
Spirit commands.
Tradition-specific later abilities.
Psionic powers, if the separate system uses Essence.
9. Casting Failure and Emergency Casting

A spell should not normally be lost simply because the caster is under pressure. However, adverse conditions can require an Essence expenditure or create a casting complication.

Possible rule:

If a caster is distracted, adjacent to an enemy, wounded, restrained, or missing a required component, they may spend Essence to cast normally. If they do not, the spell is cast with a Bane, delayed, or risks interruption according to the specific condition.

This avoids adding a universal “concentration check” every time a caster is attacked.

Spell loss

I would avoid randomly losing prepared spells due to ordinary interruption. That is frustrating and can make casters too fragile.

Instead:

The spell slot is spent only when the spell successfully resolves.
A failed casting may still consume Essence.
Severe magical backlash may consume the slot, cause a condition, or require a special consequence.
10. Advanced Tradition Access

Your proposal is sound:

Prestige Classes.
Modular Paths.
Feats.
Ancestry features.
Backgrounds.
Mentors, institutions, relics, or pacts.

Tradition access should have levels:

text
Access:
  You may learn spells from the Tradition.

Training:
  You possess a Tradition Competency Rank.

Capacity:
  You possess enough Spell Capacity to cast the spell rank.

Knowledge:
  You know or have prepared the specific spell.

Focus:
  You can modify or stabilize the spell under pressure.

This prevents a feat that grants “access to Shadow” from immediately granting a complete Shadow spellbook.

11. Current OD-001 Resolution

The following can now be treated as accepted working principles:

Traditions are individual skills.
Classes and paths grant Tradition skill access.
Tradition skills use the normal Competency Rank system.
Class and path progression automatically protects primary Tradition mastery.
General investment can specialize secondary Traditions.
Spell Capacity is separate from Tradition Competency.
Use a unified spell-slot framework rather than independent caster levels.
Preparation method may vary by class while slot progression remains shared.
Rename Focus to Essence, pending final confirmation.
Keep Essence separate from Stamina.
Essence powers 0th-rank spells, metamagic, casting stability, and supernatural class features.
Advanced Traditions are accessed through Prestige Classes, Paths, Feats, and similar permissions.
Celestial is folded into Divine as a specialization.
Use Nature instead of Primal as the formal tradition name.
Traditions currently have no unique subsystems beyond spell access and specialization.
Psychic/Psionic power remains a separate unresolved subsystem.

The largest remaining OD-001 task is now to build the actual unified Spell Capacity and slot progression table across Levels 1–20 and the six High Fantasy Tiers.
