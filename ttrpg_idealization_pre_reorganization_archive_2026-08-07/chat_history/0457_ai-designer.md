---
turn: 457
role: "AI-Designer"
source: chat_history.json
---

# Turn 457 — AI-Designer

Yes, that is simpler and probably easier to run.

The basic model would be:

text
Weapon Damage Boxes
− Armor Absorption Boxes
= Vitality Boxes marked

But instead of doing numerical subtraction, the player physically cancels boxes.

Basic Procedure
The weapon or effect has a fixed Damage Box value.
The target’s armor has an Absorption value.
Cancel the armor’s Absorption Boxes against the incoming Damage Boxes.
Mark any remaining Damage Boxes on the target’s Vitality track.
Apply any Wound, Condition, or Trait effect.
Example
text
Dagger:
  1 Damage Box

Leather:
  Absorbs 1 Box per attack

Result:

text
1 damage box
1 absorption box
→ all damage absorbed
→ no Vitality marked
Greatsword against Leather
text
Greatsword:
  2 Damage Boxes

Leather:
  Absorbs 1 Box

Result:

text
[Damage] [Damage]
[Armor ] 

One Damage Box remains:

text
Target marks 1 Vitality Box.
Greatsword against Plate
text
Greatsword:
  2 Damage Boxes

Plate:
  Absorbs 2 Boxes per attack

Result:

text
No Vitality damage.

The attack may still cause:

Stamina loss.
Knockback.
Armor Durability stress.
A special effect if the weapon has the right Trait.
High-Level Magic Hammer

A powerful hammer might have:

text
Magic Hammer:
  4 Damage Boxes
  Forceful
  Armor-Piercing
  Thunderous

Against armor absorbing 2:

text
4 Damage Boxes
2 Armor Absorption Boxes
→ 2 Vitality Boxes marked

On a critical or special effect:

Mark additional boxes.
Ignore some Absorption.
Damage Armor Durability.
Inflict Concussion.
Knock the target Prone.
Break a shield or structure.
Why This Is Simpler

This removes the need for:

Damage Dice.
Damage Die faces.
Damage-versus-Absorption comparisons.
Variable weapon damage rolls.
Armor step dice.
“Did the damage face beat the armor face?” resolution.

The combat sequence becomes:

text
Attack succeeds
→ Fixed Damage Boxes
→ Armor cancels some boxes
→ Mark remaining Vitality Boxes
→ Apply Traits or Wounds

That is highly compatible with our mathless design. The only arithmetic is visually canceling or marking a small number of boxes.

Armor Absorption Options

We should distinguish two concepts.

Absorption per attack

Armor absorbs a fixed amount from every incoming attack.

text
Leather:
  Absorbs 1 box per hit.

Chain:
  Absorbs 2 boxes per hit.

Plate:
  Absorbs 3 boxes per hit.

This is simple and reliable.

Armor durability

Armor also has a separate Durability track.

Armor may lose Durability when:

A hit exceeds its Absorption.
A Critical hits.
A Sunder attempt succeeds.
A corrosive or magical effect damages it.
The wearer chooses Item Sacrifice.

Absorption and Durability should remain separate:

text
Absorption:
  How much each attack is canceled.

Durability:
  How long the armor remains functional.
Weapon Identity

Fixed Damage Boxes make weapon Traits especially important.

Dagger
text
Damage: 1 box
Traits:
  Finesse
  Concealable
  Precise
  Throwable

It is weak against armor but strong for:

Called Shots.
Surprise.
Grappling range.
Vulnerable targets.
Poison.
Bleed.
Concealment.
Greatsword
text
Damage: 2 boxes
Traits:
  Heavy
  Two-Handed
  Forceful
  Cleaving

It deals reliable damage and may affect multiple targets or armor.

Warhammer
text
Damage: 2 boxes
Traits:
  Forceful
  Crushing
  Armor-Breaking

It may reduce Armor Absorption or damage Durability rather than simply dealing more boxes.

Magic Hammer
text
Damage: 4 boxes
Traits:
  Magical
  Armor-Piercing
  Thunderous
  Knockdown

It represents high-tier power through:

More fixed Damage Boxes.
Armor-piercing Permissions.
Conditions.
Structural damage.
Special target interactions.
Vitality Scaling

A higher-level actor can take more punishment through a larger Vitality track.

For example:

text
Trained:
  6 Vitality Boxes

Veteran:
  8 Vitality Boxes

Master:
  10 Vitality Boxes

Hero:
  12 Vitality Boxes

Legend:
  14 Vitality Boxes

These are only starting values for calibration.

Class and Attributes can independently contribute:

text
Base Vitality:
  Attribute-derived.

Class Vitality:
  Good, Medium, or Bad progression.

Ancestry:
  Size, biology, natural toughness.

Equipment:
  Armor Absorption and Durability.
Critical Hits and Wounds

A Critical should not necessarily double Damage Boxes. It could instead grant a discrete enhancement:

+1 Damage Box.
Ignore some Armor Absorption.
Inflict a severe Wound.
Damage armor Durability.
Trigger a random anatomical location.
Apply a Condition.
Mark Vitality and Wound simultaneously.

For example:

text
Natural Critical:
  Mark +1 Damage Box
  and roll the Anatomical Location Matrix.

A Called Shot could be:

text
Normal Damage Boxes
plus chosen anatomical Wound

without requiring double damage.

Important Questions Still Open

This model is simpler, but we would eventually need to decide:

Does Armor Absorption apply to every attack or only physical attacks?
Does magical armor have Absorption?
Does Absorption cancel Damage Boxes one-for-one?
Does armor Absorption have a maximum per attack?
Does armor Absorption apply before or after weapon Traits?
Can Armor-Piercing reduce Absorption?
Does armor lose Durability when it absorbs damage?
Can a dagger ever damage heavy armor?
Do Damage Boxes remain fixed across all levels?
How much Vitality does each Class progression provide?
How do spells express damage?
What happens when a character’s Vitality Boxes are full?
Does Stamina absorb damage before Vitality?
Do Wounds mark Vitality Boxes or exist separately?
How do Rabble and Underlings use the same system?
Recommendation

This is a promising simplification:

text
Weapons:
  Fixed Damage Boxes.

Armor:
  Fixed Absorption Boxes per attack.

Characters:
  Vitality Boxes.

Criticals:
  Extra Boxes, Armor bypass, Conditions, or Wounds.

Equipment:
  Absorption, Durability, Traits, and Permissions.

It keeps the simulationist distinction between dagger, greatsword, and magic hammer while removing the variable Damage Die and post-hit die comparison.

The next important design question would be whether Stamina absorbs ordinary combat impact before Vitality, or whether it is reserved exclusively for exertion and active defense.
