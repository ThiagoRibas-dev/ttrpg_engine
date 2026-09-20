---
turn: 109
role: "AI-Designer"
source: chat_history.json
---

# Turn 109 — AI-Designer

SotDL and Weird Wizard handle this much more simply than the model we have been designing because they do not use separate class-owned preparation methods in the same way.

1. How SotDL Handles Traditions

In Shadow of the Demon Lord, traditions are primarily learned through:

Novice paths.
Expert paths.
Master paths.
Tradition talents.
Individual spells.

A path grants access to one or more traditions and usually grants specific spells from those traditions. The character may then learn additional spells as advancement provides them.

The important point is:

A tradition is not usually “owned” by a specific class in a way that creates a separate spellcasting profile.

A character simply has access to traditions and spells.

For example, a character might have:

text
Traditions:
  Arcana
  Battle
  Fire
  Teleportation

The character does not maintain:

text
Wizard Fire
Warrior Fire

or:

text
Cleric Death Slots
Wizard Death Slots

Instead, all magical abilities belong to the character. Paths determine what they can acquire.

SotDL spell capacity

SotDL uses a Power statistic, which controls:

The highest rank of spell the character can cast.
The power level of spells available.
Some spell effects and scaling.

It does not use a traditional unified Vancian slot system. Spells typically have their own number of castings or uses.

Thus, SotDL avoids the shared-tradition preparation problem because it has no need to decide whether a Death spell was prepared as a Cleric spell or Wizard spell.

2. How Weird Wizard Handles Traditions

Weird Wizard follows a similar broad philosophy.

Traditions are obtained through:

Paths.
Talents.
Individual spell choices.
Character advancement.
Special features.

A character might gain:

text
Aeromancy
War
Teleportation
Divination

from different paths. Those traditions are simply part of the character’s magical repertoire.

The system does not normally distinguish:

text
This spell belongs to the Wizard side of your character.
This spell belongs to the Cleric side of your character.

Nor does it require separate spell-preparation profiles for shared traditions.

The relevant distinctions are instead:

Which traditions the character knows.
Which spells they know.
Their Power.
How many times each spell can be cast.
Which talents modify those spells.
3. What SotDL/WW Suggest for Our System

Your proposal is close to the SotDL solution:

When a class or path grants access to a new Tradition, the character records the class or path as the source of that access.

For example:

text
Death — Cleric Origin
Death — Wizard Origin

However, I would avoid saying that the class “owns” the Tradition itself. The character should own the Tradition skill.

Instead, distinguish:

Tradition Mastery

The character’s actual skill:

text
Death: Expert

This is shared across all class and path sources.

Tradition Access Source

The class or path that granted access:

text
Death Access:
  Cleric Path

or:

text
Death Access:
  Wizard Path

This is a permission record, not a separate skill.

4. Three Ways to Use Tradition Ownership
Model 1: First-Source Ownership

The first class or path that grants a Tradition becomes its owner.

text
Level 1 Cleric:
  Death — owned by Cleric

Level 2 Wizard:
  Wizard also grants Death, but does not replace ownership.
Advantages
Very simple.
The character has one clear preparation method.
Prevents constant switching.
Easy to track.
Disadvantages
The order of multiclassing matters permanently.
A character who starts Wizard and later takes Cleric may have a different Death identity from a Cleric/Wizard.
The second class may grant spells that cannot use its preferred preparation method.

This is too rigid for our system.

Model 2: Latest-Source Ownership

The most recent class or path that grants a Tradition becomes its owner.

text
Cleric 1:
  Death — Cleric-owned

Wizard 1:
  Death becomes Wizard-owned
Advantages
Simple.
The character’s current class identity dominates.
Easy for retraining or path changes.
Disadvantages
Multiclassing can unexpectedly rewrite an existing Tradition.
Players may take a one-level dip just to change preparation.
Creates order-of-leveling exploits.

I would not use this.

Model 3: Tradition Access with Profile Choice

When the character first gains a Tradition, they choose which current class or path grants the access profile.

text
Death:
  Skill Rank: Expert
  Access Source: Cleric

If another class later grants the same Tradition, the character can either:

Retain the existing source; or
Add a second access profile if the class feature explicitly allows it.

This is cleaner than automatic ownership changes.

5. Recommended Simplification

For our system, I would adapt the SotDL/WW approach and remove most preparation provenance complexity.

Use the following rule:

A character has one Tradition skill, one shared spell repertoire, and one or more access sources. The first class or path that grants a Tradition establishes its default casting profile. Later classes that grant the same Tradition expand access but do not create a second Tradition skill or slot pool.

Example:

text
Cleric 3 / Wizard 3

Death:
  Mastery: Expert
  Access Sources: Cleric, Wizard
  Default Profile: Cleric

The character may learn Death spells from either class’s available list, but all Death spells use the character’s default Death profile unless a feat or path feature says otherwise.

This avoids tracking:

text
Death — Cleric
Death — Wizard

as separate magical competencies.

6. Could the Player Choose Ownership?

Yes. A clean rule could be:

When a character first gains access to a Tradition, they choose one granting class or path as its initial Tradition Profile.

Example:

text
A Cleric/Wizard gains Death from both classes.

They choose:
  Death — Divine Profile
or
  Death — Arcane Profile

That choice determines:

Which spell list they use.
Which preparation method applies.
Which profile features modify the spells.
Which implement or focus is required.
Which class features interact with the Tradition.

Their skill remains:

text
Death: Expert

not:

text
Death Cleric: Trained
Death Wizard: Trained
7. What If the Player Wants Both Profiles?

This should be possible only through an explicit feature, such as:

A Prestige Class.
A feat.
A Master Path.
A special multiclass feature.
A rare magical initiation.

For example:

Dual Tradition Profile: Choose one Tradition you know. You may use the preparation and casting features of two different class profiles for that Tradition.

Without this feature:

text
Death:
  Skill: Expert
  Profile: Divine

With the feature:

text
Death:
  Skill: Expert
  Profiles: Divine and Arcane

This gives dual-profile access a meaningful cost and prevents every shared Tradition from becoming complicated.

8. How This Compares to SotDL/WW
Question	SotDL/WW	Our Proposed Adaptation
Are traditions shared by multiple paths?	Yes	Yes
Does a tradition have class ownership?	Usually no	Optional access source/profile
Are spells prepared through separate class methods?	Not generally	Usually one default profile
Are there separate class slot pools?	No traditional Vancian pools	One shared slot pool
Does Power determine spell rank?	Yes	Tradition Rank gates spell rank; class paths grant slot progression
Can traditions be mixed freely?	Yes, through paths	Yes, through class/path access
Are duplicate traditions separate?	No	No, one Tradition skill
Can profiles be combined?	Not usually necessary	Only through explicit features
9. Recommended Rule Text

A provisional rule could read:

Tradition Access: When a class, path, feat, ancestry, mentor, or other feature grants access to a Tradition, record the Tradition and the source that granted it. The character has one Competency Rank in that Tradition regardless of how many sources grant access. When the Tradition is first gained through a class or path, choose one granting source as its Default Profile. The Default Profile determines the Tradition’s spell list, preparation method, casting implements, and profile-specific interactions. Later sources that grant the same Tradition expand the character’s available spell options but do not create a second Tradition skill, spell-slot pool, or automatic profile. A feature may grant additional profiles for a Tradition.**

10. Example
text
Character: Human Cleric 3 / Wizard 3

Tradition Skills:
  Divine: Trained
  Arcane: Expert
  Death: Expert
  Rune: Trained

Tradition Access:
  Divine — Cleric
  Arcane — Wizard
  Death — Cleric
  Death — Wizard
  Rune — Wizard

Default Profiles:
  Divine — Cleric
  Arcane — Wizard
  Death — Cleric
  Rune — Wizard

The character can:

Use Death spells from the Cleric Death list.
Learn additional Death spells made available by Wizard access.
Cast those spells using the shared spell-slot pool.
Use Divine preparation for their Death magic by default.
Use Arcane preparation for Death magic only if they obtain a Dual Tradition Profile feature.

This is more granular than SotDL but significantly simpler than maintaining separate caster levels and spell pools for each class.

My recommendation is therefore:

Adopt one Tradition skill per Tradition, record one Default Profile when the Tradition is first acquired, and treat additional class access as expanded spell access unless a feature explicitly grants a second Profile.
