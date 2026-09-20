---
turn: 193
role: "AI-Designer"
source: chat_history.json
---

# Turn 193 — AI-Designer

These decisions fit together very well. They produce a more flexible mathematical framework than the earlier strict 5dX ceiling while still preserving a bounded face-value scale.

The biggest resulting principle is:

Die size controls the numerical ceiling; pool volume, automatic successes, requirements, and permissions control high-tier superiority.

That gives us PF2e-like cross-system reasoning without forcing every advantage into larger numerical modifiers.

A. Boons and Banes
A1. One-for-one cancellation

Locked:

text
+1B cancels +1X
+2B cancels +2X

Cancellation occurs before the remaining Boons and Banes are applied.

Example:

text
2d8 +2B +1X
→ 2d8 +1B
→ 3d8
A2. Boon types and stacking

The system will borrow PF2e’s typed-bonus logic.

This gives each Boon a type, such as:

Circumstance.
Status.
Item.
Untyped or special.
Tradition-specific or class-specific, if needed later.

The default rule would be:

Multiple Boons of the same type do not stack; use only the strongest applicable Boon of that type.

Different types may stack.

Example:

text
+1B circumstance
+1B status
+1B item
→ +3B total

But:

text
+1B circumstance
+2B circumstance
→ +2B circumstance

This is useful for D&D 3.5e conversion because existing bonus categories can be mapped into a controlled typed system.

However, the conversion guide will need a mapping table because D&D 3.5e’s bonus types and PF2e’s bonus categories are not perfectly identical.

A3. Bane stacking

There is no hard numerical Bane cap.

The operational limit is procedural:

Banes cancel Boons.
Remaining Banes remove dice.
If only one die remains, one additional Bane causes one Die Step-Down.
Further Banes do not worsen the result.

Example:

text
4d8 +1X → 3d8
4d8 +2X → 2d8
4d8 +3X → 1d8
4d8 +4X → 1d6
4d8 +5X or more → 1d6

No effect may stack with itself from the same source.

Example:

text
Three castings of the same spell:
  Do not provide three separate Boons.
  Do not provide three separate Banes.

This should be a universal anti-stacking rule:

The same named source cannot apply the same benefit or penalty more than once to the same target or check unless it explicitly says otherwise.

A4. How Banes interact with the dice

Your instinct is mathematically sound.

Suppose the pool is:

text
3d8 +1X

There are two procedures:

Procedure 1: Remove a die before rolling
text
Roll 2d8.
Procedure 2: Roll 3d8, ignore the highest result, keep the highest remaining result
text
Roll 3d8.
Ignore the highest face.
Keep the higher of the remaining two.

These are mathematically equivalent if the Bane simply removes one die from a same-size pool.

The difference is procedural and psychological.

Remove before rolling

Advantages:

Faster.
Less cognitive load.
Keeps the core “pool volume” model clean.
Makes Bane cancellation easy to calculate.
Avoids rolling dice that will be discarded.
Ignore the highest roll

Advantages:

Feels more painful and dramatic.
Makes the penalty visually obvious.
Preserves the character’s original pool size on the table.
Resembles disadvantage mechanics in some games.

Disadvantages:

Players roll extra dice only to throw one away.
It can be confusing when multiple effects interact.
It makes Bane resolution look different from the stated “remove dice” rule.
It becomes more cumbersome when a Bane also causes a Die Step-Down.
Recommendation

I recommend:

Banes remove dice before rolling.

The “ignore the highest die” method is mathematically equivalent but procedurally less efficient.

If we want a particularly severe effect to feel different, it should be a named condition or special rule—not the default Bane procedure.

A5. Timing

Locked:

Boons and Banes are calculated after all other normal pool calculations.

The order becomes:

Determine the relevant Attribute Die.
Apply Competency Rank.
Apply Skill, Class, Feat, Equipment, and other normal effects.
Apply Die Step-Ups and Die Step-Downs.
Apply typed Boons and Banes.
Cancel Boons and Banes.
Remove Bane dice.
Apply the single Bane-induced Die Step-Down if the pool has reached one die.
Apply the resulting Floor.
Roll.

The phrase “after all other calculations” should eventually be expressed in non-arithmetic terminology, perhaps:

Boons and Banes are final pool modifiers.

A6. Floors and Banes

This updates the earlier decision.

Floors are not completely protected from Banes. A Bane lowers the Floor because it reduces the character’s final effective pool state.

Example:

text
Expert:
  3d8, Floor 5

+1 Bane:
  2d8, Floor 5

+2 Banes:
  1d8, Floor 5

+3 Banes:
  1d6, Floor 3

So the rule becomes:

A Bane can reduce both the pool’s volume and its effective Floor, but it cannot reduce the pool below one die or cause more than one Bane-induced Die Step-Down.

This distinction should be formalized carefully because it means Floors are derived from the final state rather than being inviolable character properties.

A7. Die Step-Ups and Banes

Locked:

Boons, Banes, and all Die Step-Ups/Die Step-Downs are resolved at the end of pool construction.

This creates a clean finalization stage.

A possible terminology distinction:

text
Die Step-Up/Die Step-Down:
  Changes die size.

Boon/Bane:
  Changes pool volume or final pool reliability.

Automatic Success:
  Adds success directly to the outcome.

Permission:
  Allows an action or effect that ordinary rules do not allow.

Requirement:
  States what must be true before an action or effect is available.
A8. Boons and Multi-Successes

Locked:

Boons add dice to the pool, and those dice participate normally in multi-success counting.

Example:

text
2d8 +1B → 3d8
Difficulty: DC 5 (2)

All three dice can contribute successful faces.

A Boon does not directly add a success. It increases the chance of producing one or more successes through normal dice.

B. Opposed Rolls
B1. Tie-breaking

The proposed rule is:

Compare the highest face.
If tied, compare the next-highest face.
Continue comparing dice in descending order.
If both pools have identical results across the same number of dice, the defender wins.
If one pool has no remaining die to compare, the defender wins the tie.

Example:

text
Attacker: 3d8 → 8, 6, 2
Defender: 3d8 → 8, 6, 4

Defender wins because the third die is higher.

Example:

text
Attacker: 3d8 → 8, 6, 4
Defender: 2d8 → 8, 6

The results tie through the defender’s available dice. Defender wins.

Example:

text
Attacker: 3d8 → 8, 6, 4
Defender: 3d8 → 8, 6, 4

Defender wins the complete tie.

This is elegant and gives additional dice an important role beyond increasing the chance of a high face.

B2. Noncombat contests

The same attacker/defender structure applies when one party initiates the contest.

text
Initiator = Attacker
Responding party = Defender

The defender wins ties.

However, not every contest needs a winner.

A race, debate, or timed contest may end in:

text
Tie

when neither party achieves superiority.

This distinction should be encoded in the procedure:

Contest with required victor: Defender wins ties.
Contest with neutral outcome: Ties produce a tie or stalemate.
B3. Opposed multi-successes

The first resolution layer is highest-face comparison.

Only after determining the opposed winner do we apply the relevant effect:

Success.
Failure.
Maneuver.
Counteraction.
Special class or feat feature.

This means opposed checks do not automatically compare total successful faces against one another.

The existing DC X (Y) multi-success system applies primarily to:

Fixed-DC tasks.
Combat effects where the attacker must generate multiple successes.
Special abilities that explicitly require multiple successes.
B4. Defensive superior results

The baseline framework only produces:

text
Success
Failure

A superior defensive result does not automatically grant a Riposte, Disarm, or counter-maneuver.

Those effects belong to:

Classes.
Feats.
Equipment.
Special abilities.
Explicit defensive mechanics.

This prevents the universal engine from becoming overburdened with automatic counter-effects.

B5. Floors and ties

The Floor only changes the lower bound of a result.

It does not:

Change tie ownership.
Add automatic successes.
Alter the tiebreak sequence.
Change attacker/defender designation.
Create a counteraction.
B6. Conditions

Conditions define their own interactions.

A condition may:

Prevent reactions.
Prevent active defense.
Apply Banes.
Apply Die Step-Downs.
Change whether an actor counts as attacker or defender.
Remove a special ability.

The universal opposed-tie rule remains unchanged unless the condition specifically overrides it.

C. High-Tier Capability Without Larger Dice
C1. Additional dice and Automatic Successes

This is a strong solution.

High-tier superiority progresses through:

Larger ordinary pools, initially up to the normal natural range.
Automatic successes once further pool expansion becomes excessive.
Higher required-success DCs.
Expanded requirements and permissions.
Mythic effects that alter the structure of the task.

Example:

text
Difficulty:
  DC 9 (3)

Legendary character:
  5d12
  +1 automatic success

The character still needs two rolled successes at DC 9 to complete the task.

A more extreme effect could be:

text
DC 9 (3)
5d12 +2 automatic successes

The character needs only one rolled success.

Important automatic-success rule

Automatic successes are not dice and do not interact with:

Boons.
Banes.
Die Step-Ups.
Die Step-Downs.
Tiebreakers.

They are added after the roll result is determined.

They also count toward a required-success threshold.

Automatic success and DC value

Your proposed rule is:

An automatic success counts toward the success requirement regardless of the DC’s numerical value.

Therefore:

text
DC 12 (1)
+1 automatic success
→ Automatically succeeds.

This is powerful and should probably be reserved for:

Legendary Competency.
High-tier class features.
Specific feats.
Major equipment.
Mythic abilities.
C2. Pool volume beyond 5dX

The earlier strict maximum of 5dX is now superseded.

The revised position is:

5dX is the normal natural, unbuffed, unequipped pool range—not an absolute universal cap.

Additional dice may come from:

Ancestries.
Classes.
Feats.
Spells.
Equipment.
Skill investment.
Mythic effects.
Special circumstances.

However, such effects should be content-controlled rather than freely stackable.

This creates three practical bands:

text
Natural Pool:
  Normal Attribute + Competency pool.

Enhanced Pool:
  Pool increased by class, equipment, spells, or feats.

Exceptional Pool:
  Large pool granted by Legendary or Mythic effects.

The probability model should eventually test where additional dice become redundant because automatic successes are more efficient.

C3. Mythic and DC 12

Mythic continues the ordinary framework:

Same basic die types.
Same DC ceiling of 12.
More dice.
More automatic successes.
Higher required-success thresholds.
More powerful requirements and permissions.
More ability to manipulate the difficulty or choose rolled results.

Examples:

text
DC 12 (3)
5d12 +1 automatic success

or:

text
Mythic ability:
  Choose the result of one die after rolling.

Mythic therefore does not need:

text
DC 18
d20
d30
d12+3

It scales through success requirements and exceptional resolution permissions.

C4. Mythic power

Mythic should provide both:

Stronger mathematical reliability.
Broader fictional effect.

The balance should lean toward the second.

Examples:

Affect a city instead of a room.
Speak across planes.
Create permanent magical structures.
Rewrite a condition.
Alter the area or duration of a spell.
Manipulate the required success count.
Choose or replace a rolled die.
Gain access to otherwise restricted Traditions.
C5. Immunities

The baseline framework does not allow Legendary status to bypass immunity.

Immunity is overcome only through:

A class feature.
A feat.
A spell.
A Tradition feature.
A weapon or item.
A Mythic permission.
A specific exception in the effect.

This preserves the importance of creature identity and prevents high-level competency from flattening all defenses.

C6. Equipment

Equipment may exceed ordinary capability through all of the proposed discrete vectors:

Boons.
Automatic successes.
Damage effects.
Fixed damage.
Immunities.
Resistance bypass.
Penetration.
Special defenses.
Action permissions.
Durability.
Critical effects.
Ignoring specific attack or defense categories.

Example concept:

text
Godly weapon:
  Grants one permanent typed Boon.
  Grants one automatic success on a defined attack type.
  Provides an immunity or resistance.

The actual values belong to equipment and crafting design, not Phase 1’s universal math rules.

D. Universal Mathematical Ceiling

All subsystems use the same core ceiling and resolution language:

d4 through d12.
DCs generally from 2 through 12.
DC X (Y) for required successes.
Shared Boon/Bane logic.
Shared Floor logic.
Shared opposed-roll tie rules.
Shared automatic-success logic.

This supports cross-system interactions such as:

text
Parrying a spell with a weapon.
Resisting a social spell with Willpower.
Using Craft to disable a magical device.
Using a weapon Trait against a magical barrier.

The key exception is not a separate mathematical engine but an effect-specific permission.

E. New Terminology to Formalize

I agree that we should add a baseline-framework glossary. The most important new terms are:

Requirement

A condition that must be met before an action, ability, spell, or effect can be used.

Examples:

text
Requires Expert Death Tradition.
Requires a visible target.
Requires a weapon with the Reach Trait.
Permission

An explicit rule that allows an actor to do something outside the ordinary baseline procedure.

Examples:

text
May cast as a Reaction.
May target an immune creature.
May choose one die result after rolling.
May affect an additional target.
Automatic Success

A success added directly to the result after rolling. It is not a die and cannot be altered by Boons, Banes, or tiebreak rules.

Natural Pool

The pool produced by Attribute, Competency, and ordinary character factors before temporary enhancements.

Enhanced Pool

A pool expanded by class, feat, spell, equipment, or circumstance.

Required Successes

The number in parentheses in a difficulty such as:

text
DC 9 (3)
Defender Wins Ties

The universal opposed-contest tie rule unless a specific effect says otherwise.

These should eventually go into a Baseline Framework Glossary, with the glossary linked from the canonical resolution engine rather than duplicating full rules across documents.
