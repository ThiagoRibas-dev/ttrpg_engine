---
turn: 453
role: "AI-Designer"
source: chat_history.json
---

# Turn 453 — AI-Designer

Searched for "RPG systems health wounds no hit point subtraction damage tracks health levels Fate Savage Worlds Cortex Year Zero health mechanics comparison highest level progression monster damage soak dice pools RPG design damage tracks no math spreadsheet per level HP alternatives"

Yes. Several systems model durability without requiring “take 17 damage, subtract 17 from 84 HP” every time. The most relevant references for us are these.

1. Savage Worlds

Savage Worlds is probably the closest useful reference for fast combat plus wound states.

Core model

Characters generally have:

A small number of Wounds.
A Shaken state.
Toughness.
Armor.
Soak-like mitigation.
Wild Card status for important characters.
Extras that are defeated quickly.

Damage is resolved by comparing an attack’s result against Toughness and determining whether it causes:

No meaningful effect.
Shaken.
One or more Wounds.
Incapacitation.
Why it is useful for us

Savage Worlds does not require large HP pools for every character. Durability comes from:

Wild Card status.
Armor.
Toughness.
Edges.
Wound tolerance.
Temporary conditions.

This aligns strongly with our:

text
Vitality
Damage Absorption
Wounds
Rabble/Underlings/Iconic Champions
Limitation

Savage Worlds still uses numerical damage and comparison against Toughness, so it is not fully mathless. Its main lesson is structural:

Use a small wound track plus conditions instead of enormous HP totals.

2. Fate

Fate uses:

Stress boxes.
Consequences.
Aspects.
Armor and weapon shifts in some versions.
Core model

Stress represents short-term ability to absorb or avoid meaningful consequences. When stress is exhausted, the character takes Consequences such as:

Bruised.
Wounded.
Broken arm.
Terrified.
Knocked out.

Consequences impose narrative and mechanical complications rather than simply subtracting more HP.

Why it is useful for us

Fate provides a strong model for separating:

text
Temporary combat endurance
from
Persistent injury

That maps naturally to:

text
Stamina or temporary Vitality:
  Short-term combat reserve.

Wounds:
  Persistent injuries and Conditions.
Limitation

Fate does not strongly model progressive level-based durability in the D&D sense. Characters become more capable mostly through Skills, Stunts, Stress, and Consequences rather than acquiring dramatically larger health totals.

3. Legends of the Five Rings

L5R uses a very useful distinction between:

Fatigue.
Critical Strikes.
Wounds and lasting consequences.

A character can accumulate Fatigue without immediately suffering a severe injury. Once their defensive or endurance capacity is overwhelmed, attacks generate Critical Strikes that produce serious injuries.

Why it is useful for us

This is very close to a possible Vitality model:

text
Vitality/Stamina:
  Absorbs ordinary combat attrition.

Critical impact:
  Bypasses the temporary buffer and creates a Wound.

Wounds:
  Impose meaningful conditions and lasting consequences.

A useful design insight is:

Not every successful hit needs to draw blood or create a serious wound.

This supports tactical combat pacing while preserving the significance of anatomical injury.

4. Cypher System

Cypher has three pools:

Might.
Speed.
Intellect.

These pools function as:

Resource reserves.
Effort pools.
Damage buffers.
Ability fuel.

Damage can reduce a relevant pool, and when pools become depleted, characters suffer increasingly serious consequences.

Why it is useful for us

Cypher demonstrates how a resource can simultaneously represent:

Capability.
Exertion.
Resistance.
Injury.
Ability usage.

It is an interesting reference for our idea of symmetrical resources:

text
Vitality
Stamina
Essence

It also has a strong progression model: higher-tier characters have larger pools and more options for spending them.

Limitation

Cypher does involve reducing numeric pools during play, so it does not solve our arithmetic problem by itself. The conceptual separation between different kinds of reserves is more useful than the literal procedure.

5. Mutants & Masterminds

Mutants & Masterminds generally does not use traditional HP. It uses:

Toughness saves.
Degrees of failure.
Conditions such as Bruised, Staggered, and Disabled.
Hero Points.
Protection and defensive powers.
Core model

A successful attack does not necessarily remove a number of HP. It forces a resistance result. The degree of failure determines the severity of the consequence.

Repeated failures worsen the character’s condition.

Why it is useful for us

This gives us a strong model for:

text
Damage as a severity result
rather than
Damage as a subtraction quantity.

It can represent higher-level durability by improving:

Resistance pools.
Protection.
Conditions tolerated.
Recovery.
Defensive powers.
Limitation

Mutants & Masterminds still uses numerical save DCs and modifiers, so the architecture would need to be translated into our Dice Pool/Difficulty Vector framework.

6. Cortex Prime

Cortex often models stress using:

Stress tracks.
Stress die sizes.
Complications.
Assets.
Condition tracks.

A character may suffer:

text
Stress d6
Stress d8
Stress d10

or specific complications.

Why it is useful for us

Cortex offers a very relevant idea:

Durability itself can be represented by a die size or track rather than a giant HP value.

A higher-tier character might have:

text
Vitality Track: d10

while a lower-tier character has:

text
Vitality Track: d6

Damage could step the track up, create a Condition, or force a complication rather than subtracting a number.

Limitation

Cortex’s rules vary significantly by implementation, and its resource/plot-point economy is not compatible with our zero-meta-currency policy.

7. Blades in the Dark

Blades uses Harm rather than HP.

Harm has levels such as:

Lesser Harm.
Serious Harm.
Fatal or incapacitating Harm.

Characters can also use:

Armor.
Special armor.
Resistance rolls.
Trauma.
Recovery downtime.
Why it is useful for us

Blades is useful for:

Compact injury tracks.
Consequences instead of hit-point subtraction.
Armor as permission to reduce a consequence.
Recovery as a dedicated procedure.
Harm severity as a design language.
Limitation

It does not model level-based fantasy durability in the same way as D&D. Its characters generally become more capable through action ratings, abilities, and resistance capacity rather than massively larger health totals.

8. Traveller

Traveller applies damage directly to physical characteristics such as:

Strength.
Dexterity.
Endurance.

As those characteristics are reduced, the character becomes less capable. Reaching zero in certain characteristics causes serious consequences.

Why it is useful for us

This is a strong reference for damage degrading capability:

text
Damage:
  Reduces a physical reserve.

Reduced reserve:
  Makes future actions worse.

Severe depletion:
  Creates incapacitation or death.

It is more simulationist than a separate HP pool.

Limitation

Traveller characters do not generally gain large Attribute increases through level progression, so it does not directly solve our high-level durability problem.

9. Mythras and BRP

Mythras uses:

Hit Locations.
Local HP.
Serious and Major Wounds.
Armor.
Damage and location comparisons.
Recovery procedures.
Why it is useful for us

Mythras demonstrates how to make damage profiles matter:

A limb injury behaves differently from a chest injury.
Armor protects locations.
A single heavy blow can cause a major Wound.
Many small wounds do not need to become a giant arithmetic HP pool.
Damage severity can be more important than total damage quantity.

This aligns strongly with our existing:

text
Natural Criticals
Called Shots
Anatomical Location Matrix
Wound Conditions
Damage Absorption
Limitation

Mythras still uses numerical local HP and damage values, although the numbers remain relatively small.

10. Daggerheart and Similar Modern Systems

Some newer systems use:

Stress.
Hit points.
Conditions.
Armor.
Hope/Fear or other narrative resources.

These provide useful examples of separating:

Immediate harm.
Persistent consequences.
Defensive mitigation.
Emotional or narrative effects.

However, their meta-currency structures are not appropriate for our design unless translated into Stamina, Essence, Vitality, Durability, or other in-world resources.

Most Relevant Models for Us

The strongest references are:

Savage Worlds

For:

Wound tracks.
Shaken states.
Important characters versus Extras.
Armor and toughness.
L5R

For:

Fatigue before serious injury.
Critical impact.
Wounds as separate from ordinary combat attrition.
Mythras

For:

Hit locations.
Damage profiles.
Serious/Major Wounds.
Armor and local injury.
Mutants & Masterminds

For:

Damage severity.
Resistance results.
Conditions instead of HP subtraction.
Cortex

For:

Stress represented by die size or tracks.
Complications and conditions.
Scalable durability without huge numbers.
Cypher

For:

Symmetrical resource pools.
Resource depletion reducing capability.
Attribute/resource interactions.
Possible Model for Our System

A promising synthesis would be:

text
Vitality:
  A capacity track derived from Attributes and Class progression.

Stamina:
  Short-term exertion and combat endurance.

Essence:
  Magical and supernatural reserve.

Damage Absorption:
  Material protection that determines whether impact becomes injury.

Wounds:
  Discrete anatomical or systemic consequences.

Vitality depletion:
  Leads to Conditions, incapacitation, or Wounds rather than only subtraction.

Class progression:
  Increases resource capacity through Good, Medium, and Bad tracks.

Equipment:
  Improves Damage Absorption, Durability, Traits, and Permissions.
Three Ways to Handle Vitality Without Table-Side Subtraction
Model A — Vitality Boxes

A character has a number of Vitality boxes.

text
Trained:
  4 Vitality boxes

Veteran:
  6 Vitality boxes

Master:
  8 Vitality boxes

Damage produces:

One box.
Multiple boxes.
A Wound.
A Critical Wound.

Advantages:

No subtraction.
Easy to track.
Level-based durability is straightforward.
Model B — Damage Severity versus Vitality Track

Damage has a severity category:

text
Minor
Moderate
Severe
Critical

Vitality determines how many hits of each severity a character tolerates.

Example:

text
A Veteran can absorb:
  3 Minor impacts.
  2 Moderate impacts.
  1 Severe impact.

Advantages:

Better than raw HP for different damage profiles.
A dagger and a greatclub can produce different severity patterns.
Easy to combine with anatomical Wounds.
Model C — Vitality Die and Impact Comparison

Vitality is represented by a die or track:

text
Trained: d6 Vitality
Veteran: d8 Vitality
Master: d10 Vitality
Hero: d12 Vitality

Damage is also a die or severity category. Compare the two, similar to Damage Absorption.

Advantages:

Fits the rest of our bounded dice architecture.
Higher-tier characters can absorb larger impacts.
No subtraction.

Risks:

Adds another Die Size vector.
May create too many overlapping dice comparisons.
Can make Vitality and Damage Absorption feel redundant.
My Recommendation

I would initially investigate a hybrid of Model A and Model B:

text
Vitality:
  A bounded track of boxes or segments.

Damage:
  Produces discrete impact severity rather than a number to subtract.

Damage Absorption:
  Reduces, negates, or downgrades impact severity.

Wounds:
  Serious or critical impacts create specific anatomical Conditions.

Stamina:
  Absorbs ordinary combat shock and fuels exertion.

Vitality:
  Represents remaining ability to stay in the fight.

Wounds:
  Represent actual structural injury.

This would let a higher-tier actor take more punishment through a larger Vitality capacity, while different damage profiles remain meaningful without requiring arithmetic.

The main design question for the next resource pass would be:

Should Vitality be a simple box track, a severity-based track, or a bounded die/impact comparison system?
