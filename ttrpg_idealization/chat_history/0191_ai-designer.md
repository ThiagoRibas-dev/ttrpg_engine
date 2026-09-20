---
turn: 191
role: "AI-Designer"
source: chat_history.json
---

# Turn 191 — AI-Designer

Phase 1 Questionnaire
Boons/Banes, Opposed Ties, and High-Tier Capability Ceilings

This questionnaire is intended to guide discussion without prematurely deciding the answers. The reference examples are prompts for comparison, not recommendations to copy.

A. Boon and Bane Stacking
Current framework

The current working rules are:

A Boon adds one die of the same size.
A Bane removes one die.
A pool cannot fall below one die.
A Bane applied to a one-die pool causes one Die Step-Down.
Further Banes do not apply additional Die Step-Downs.
Floors remain active after Bane reduction.
Mixed-size Boon dice are not used.
A1. Do Boons and Banes cancel one-for-one?

Example:

text
2d8 +2B +1X

Possible outcomes:

text
3d8
2d8

depending on whether one Bane cancels one Boon before the remaining Boon is applied.

Reference examples
Shadow of the Demon Lord: Boons and Banes generally cancel one-for-one before determining the final number of dice.
D&D 5e: Advantage and Disadvantage generally cancel each other completely; multiple sources do not create multiple dice.
Pathfinder 2e: Circumstance and status modifiers use category-specific stacking rules rather than universal cancellation.
Question

Should our system use:

Complete one-for-one Boon/Bane cancellation?
Boons and Banes applied in a fixed order?
A maximum of one net Boon or Bane?
Separate Boon/Bane categories that do not cancel each other?
A2. Can Boons stack beyond +3B?

Example:

text
2d8 +4B

Possible outcomes:

text
5d8, with excess ignored

or:

text
5d8 plus a Die Step-Up

or:

text
5d8 plus an additional effect
Reference examples
SotDL/WW: Boons and Banes are commonly capped or kept within a manageable range; excessive values do not normally create enormous pools.
D&D 5e: Advantage does not stack beyond advantage.
Pathfinder 2e: Multiple bonuses of the same type generally do not stack, though different bonus types may combine.
Question

What happens when net Boons exceed the 5dX pool ceiling?

A3. Can Banes stack beyond +3X?

The current rule says:

text
One-die pool + one Bane → one Die Step-Down
Further Banes → no additional Die Step-Down

But what happens before the pool reaches one die?

Example:

text
4d8 +3X

Possible result:

text
1d8
Reference examples
SotDL: Banes can substantially reduce the effective pool, but the system has a bounded and relatively simple interaction.
D&D 5e: Multiple Disadvantages do not worsen the result beyond normal Disadvantage.
Pathfinder 2e: Multiple penalties can stack if they are different types, but identical penalties do not normally multiply without a specific rule.
Question

Should Banes always remove dice until only one remains, or should there be a maximum number of removable dice per check?

A4. Does a Bane remove the highest die, a random die, or simply reduce pool volume?

Example:

text
3d10 +1X

Possible interpretations:

text
2d10

or:

text
Roll 3d10 and discard the highest die

or:

text
Roll 3d10 and keep the lowest two
Reference examples
SotDL: Banes reduce the number of dice rolled, rather than forcing the player to roll and discard a particular result.
D&D 5e: Disadvantage rolls two dice and keeps the lower result.
Pathfinder 2e: Penalties alter the target number rather than manipulating the dice pool.
Question

Should our Bane always be resolved before rolling by reducing the number of dice?

A5. Does a Bane affect pool volume before or after Competency Rank?

Example:

text
Expert skill:
  3d8, Floor 5

Apply one Bane.

Possible results:

text
2d8, Floor 5

or:

text
3d8, but keep the lowest two
Reference examples
SotDL: Boons and Banes modify the final roll pool after the character’s normal capability is determined.
D&D 5e: Advantage and Disadvantage are applied after the character’s normal modifier and proficiency are established.
Pathfinder 2e: Circumstance/status effects are applied after the base statistic is determined.
Question

Is the normal Competency Rank pool always established first, with Boons and Banes applied afterward?

A6. Does a Bane suppress a Floor?

Current decision:

text
No. Floors remain active.

Example:

text
Expert:
  2d8, Floor 5

After a Bane:
  1d8, Floor 5
Reference examples
SotDL: Boons/Banes change the roll’s reliability but do not normally erase a character’s underlying level or attribute identity.
PF2e: Penalties do not remove proficiency training.
D&D 3.5e: A penalty generally modifies the final check but does not remove skill ranks.
Question

Are there any effects that should explicitly suppress or bypass a Competency Floor?

A7. Can a Die Step-Down and Bane coexist?

Example:

text
2d8 +1X
and
Down-Shift the pool once

Possible orderings:

text
1d8, then d6

or:

text
2d6, then 1d6
Reference examples
SotDL: Boons/Banes and other modifiers are generally resolved through defined modifier interactions.
D&D 5e: Advantage/disadvantage and other modifiers are separate categories, but their interactions are tightly specified.
Pathfinder 2e: Multiple condition effects and penalties use explicit order and type rules.
Question

Should all Die Step-Ups/Die Step-Downs be applied before Boons/Banes, or should the specific effect define the order?

A8. Do Boons improve multi-success counts?

Example:

text
2d8 → 3d8
Difficulty: DC 5 (2)

Does the additional die merely improve the chance of two successes, or does the Boon itself produce an extra success?

Reference examples
Mythras: Better levels of success are determined by the degree of success, not by a generic “bonus token” automatically added to the result.
D&D 5e: Advantage improves the chance of success but does not automatically produce a critical or higher degree of success.
Pathfinder 2e: A +1 can move a result across a critical-success threshold, but the modifier does not directly add a success.
Question

Should Boons affect only probability, or can specific Boons explicitly add a success?

B. Opposed-Roll Tie Procedures
Current framework

The current decision is:

The defender wins ties.

Complex checks use:

text
DC X (Y)

where X is the Target Number and Y is the number of required successes.

B1. What exactly counts as a tie?

Example:

text
Attacker highest face: 8
Defender highest face: 8

Possible interpretations:

Defender automatically wins.
Compare the second-highest faces.
Compare the number of successful faces.
Compare the relevant Attribute Die.
Invoke a special tie-breaking trait.
Reference examples
Mythras/BRP: Opposed rolls compare levels of success; equal levels often result in a tie or special resolution procedure.
D&D 5e: In an opposed ability check, a tie may result in no change, a stalemate, or a reroll depending on the situation.
Gloomhaven: Initiative ties are resolved by secondary initiative values or card-order rules.
Pathfinder 2e: Degree-of-success comparisons normally use the final result against a fixed DC rather than defender-versus-attacker ties.
Question

Is “defender wins ties” always sufficient, or do we need a formal secondary tiebreak for special contests?

B2. Does the defender win ties in noncombat contests?

Examples:

A diplomat persuading a monarch.
A thief avoiding a guard.
A tracker hiding their trail.
A monster resisting a spell.
Two characters racing.
Reference examples
D&D 5e: Contested checks do not always have a universal winner-on-ties rule; the GM often determines the result.
Mythras: Opposed resolution is generally symmetrical, with levels of success determining the outcome.
Pathfinder 2e: Many contests are expressed as checks against DCs rather than opposed rolls.
Question

Should defender-wins-ties apply universally, or only to active attack-versus-defense contests?

B3. How are opposed multi-success results calculated?

Example:

text
Attacker:
  3d10 → 6, 8, 10

Defender:
  2d8 → 5, 8

Possible models:

Compare highest faces only.
Count successes against the defender’s highest face.
Count the attacker’s successes minus the defender’s successes.
Compare the number of successful faces on each side.
Use highest-face victory first, then count additional successes.
Reference examples
Mythras: Opposed rolls compare levels of success and then use the difference to determine Special Effects.
D&D 5e: Opposed checks usually compare one final result and do not count multiple successful dice.
Pathfinder 2e: Degree of success is determined by the result’s relationship to a DC, usually in four steps.
Gloomhaven: Attack modifiers and effects are resolved through card results rather than opposed success counts.
Question

Which opposed-roll model best preserves the importance of multiple dice without making contests too complicated?

B4. Can the defender generate a superior defensive result?

Example:

text
Attacker hits with 1 success.
Defender has a defensive result equivalent to 2 successes.

Possible outcomes:

The attack fails completely.
The defender gains a Riposte or counteraction.
The attacker suffers a defensive maneuver.
The extra defense is ignored.
Reference examples
Mythras: Strong defensive results can generate Special Effects.
Pathfinder 2e: Critical success on a defense or saving throw can produce stronger outcomes.
D&D 3.5e: Defenses generally either stop an attack or fail to stop it; extra defense rarely creates an active counter-effect.
Question

Should opposed defense degrees create defensive maneuvers, or should they only determine whether the attack succeeds?

B5. How do Floors interact with ties?

Example:

text
Attacker:
  Expert, Floor 5

Defender:
  Trained, Floor 3

Both final results:
  5

The defender wins the tie under the current rule.

Reference examples
Pathfinder 2e: Proficiency and level affect the final result, and critical thresholds can make small differences significant.
Mythras: Equal success levels may produce a stalemate.
D&D 5e: Equal contested results are normally resolved by the situation or a tie rule.
Question

Should the defender win even when the attacker’s underlying Competency Rank is higher?

B6. Do conditions that prevent reactions affect ties?

Example:

text
A defender is Stunned or Confused.
The defender still wins an opposed tie.
Reference examples
SotDL/WW: Conditions often prevent reactions or impose restrictions rather than directly modifying every roll.
Pathfinder 2e: Conditions can prevent actions or impose penalties, but their precise effects are explicitly listed.
Mythras: Combat conditions and Special Effects can limit defensive options.
Question

Should a defender who cannot actively defend still benefit from defender-wins-ties, or should passive defenses use a different tie rule?

C. High-Tier Effects Without Over-Cap Dice
Current framework

The ordinary mathematical ceiling is:

text
Maximum ordinary die: d12
Maximum ordinary DC: DC 12

Former d12+, d12+1, and d12+2 notation is deprecated.

C1. How should Legendary capability exceed ordinary competency without larger dice?

Possible tools:

Higher Competency Floors.
More dice, up to the normal pool ceiling.
Additional required successes.
Automatic maneuver permissions.
Expanded action economy.
Equipment Traits.
Special defenses.
New spell effects.
Resource-based permissions.
Immunities or resistances.
Reference examples
D&D 3.5e: Epic characters continue increasing numerical bonuses and may access Epic Skills and Epic Spellcasting.
Pathfinder 2e: High-level characters remain within the same d20 framework but gain powerful feats, proficiency, traits, and critical-success effects.
13th Age: High-level abilities often gain stronger narrative permissions and class-specific effects rather than merely larger numbers.
SotDL: Power and higher-rank spells expand effect scale without necessarily requiring infinite numerical escalation.
Question

Which vectors should represent Legend-level superiority while keeping all ordinary dice at d12?

C2. Should high-tier effects increase pool volume beyond 5dX?

Current working ceiling:

text
Maximum ordinary pool: 5dX
Reference examples
D&D 3.5e: Bonuses and attack sequences continue scaling beyond ordinary bounds.
Pathfinder 2e: Proficiency and level continue scaling, but the d20 remains the same.
SotDL: Boons remain bounded rather than creating arbitrarily large dice pools.
13th Age: Escalation and class features provide special scaling rather than unlimited dice.
Question

Should Legendary and Mythic effects ever exceed 5d12, or should they instead produce automatic successes, extra success counts, or special permissions?

C3. How should Mythic characters interact with DC 12?

Possible models:

Mythic characters automatically succeed against ordinary DC 12 tasks.
Mythic characters gain additional successes rather than higher faces.
Mythic tasks use DC 12 (2+).
Mythic challenges use opposed checks rather than higher DCs.
Mythic characters use special Mythic conditions or Traits.
Reference examples
D&D 3.5e Epic: Difficulty numbers continue increasing beyond normal mortal scales.
Pathfinder 2e: Extreme-level tasks use higher level-based DCs while retaining the d20.
13th Age: Epic effects often depend on tier, class power, and narrative permission.
SotDL: Higher Power unlocks stronger spells and effects rather than expanding ordinary target numbers indefinitely.
Question

Should Mythic challenges remain within DC 2–12 with increased success requirements, or should Mythic introduce a separate resolution layer?

C4. Should Mythic effects be stronger mathematically or broader fictionally?

Compare:

text
A spell deals more damage.

against:

text
A spell can affect an entire city.
Reference examples
D&D 3.5e: Epic magic often increases numerical magnitude dramatically.
13th Age: High-level effects frequently combine large fictional permissions with class-specific mechanics.
SotDL: Master spells often provide broad, unusual, or encounter-defining effects.
Exalted: Mythic power often expands what actions are possible, not merely how successful ordinary actions are.
Question

Should Mythic progression primarily provide:

Larger scale.
Wider targets.
Permanent or world-changing effects.
New action types.
New conditions.
Greater reliability.
Larger numerical output.
Or some combination?
C5. How should Legendary characters overcome lower-tier immunities?

Example:

text
A Legendary Death caster uses a Death spell against an undead boss
that is normally immune to Death effects.
Reference examples
D&D 3.5e: Epic and high-level abilities may overcome resistances through caster level, spell penetration, or specific feats.
Pathfinder 2e: Traits, immunities, and incapacitation rules often remain meaningful even at high level.
SotDL/WW: High-Difficulty creatures frequently become immune to control effects, making spell selection and specialization important.
Mythras: Stronger effects and Special Effects do not necessarily erase all creature immunities.
Question

Should high-tier mastery:

Ignore some immunities.
Convert immunity into resistance.
Permit a special opposed check.
Require a Mythic or Legendary feat.
Leave immunity absolute?
C6. How should high-tier equipment exceed ordinary equipment?

Possible tools:

Higher Damage Die is not available beyond d12.
Better Critical Threat Profiles.
Penetration Traits.
Automatic maneuver effects.
Additional Durability Slots.
Immunity to lower-tier weapons.
Special material interactions.
Action-economy permissions.
Reference examples
D&D 3.5e: Enhancement bonuses and special weapon abilities continue scaling.
Pathfinder 2e: Fundamental and property runes provide bounded but layered equipment advancement.
SotDL: Equipment quality and magic properties often provide direct but discrete benefits.
Gloomhaven: Higher-level cards and item effects create new tactical permissions rather than large mathematical bonuses.
Question

Which equipment vectors should represent Legendary and Mythic quality without exceeding d12?

D. Cross-System Consistency Questions
D1. Should every subsystem use the same ceiling?

Examples:

Skills.
Attacks.
Damage.
Defenses.
Spells.
Equipment.
Crafting.
Social contests.
Reference examples
D&D 3.5e: Different subsystems often scale at different rates.
Pathfinder 2e: Most checks use a unified level-based mathematical framework.
SotDL: Power, spell rank, attribute, and difficulty interact through several distinct systems.
Gloomhaven: Attack, defense, card loss, and scenario effects use different bounded mechanisms.
Question

Should d12 and DC 12 be universal, or should certain subsystems have their own bounded scales?

D2. Should every high-tier advantage be visible in probability?

A character may be stronger because they:

Succeed more often.
Cannot fail routine tasks.
Gain more successes.
Have more actions.
Ignore conditions.
Affect larger areas.
Use stronger equipment.
Have better resource reserves.
Question

Must every tier increase improve the probability of a normal check, or can high-tier progression primarily grant permissions and scale?

D3. Should exceptional effects be universal or tagged?

Example:

text
Legendary characters gain an extra success on every Master-level task.

versus:

text
A specific Legendary Feat grants an extra success only for a defined activity.
Reference examples
Pathfinder 2e: Strong effects are usually tied to feats, traits, class features, or proficiency.
D&D 3.5e: Some scaling is universal through level and bonuses; other scaling is feat- or class-specific.
SotDL: Higher path tiers grant specific talents and spells.
Question

Should bounded high-tier superiority primarily come from:

Universal tier rules.
Class features.
Competency Ranks.
Feats.
Equipment.
Spell rank.
Or a combination?
Current Decisions from This Questionnaire

The following points can now be treated as resolved:

The ordinary die ceiling is d12.
d12+ notation is deprecated.
Banes remove dice from the pool.
A one-die pool receiving a Bane gets one Die Step-Down.
Further Banes do not cause further Die Step-Downs.
Stepping down a d4 causes automatic failure.
Floors remain active after Bane reduction.
Defenders win opposed ties.
Complex difficulties use DC X (Y).
Probability targets remain deferred.
Universal costs and limits for Die Step-Up/Die Step-Down remain content-specific.
Mythic should not be designed as an unbounded expansion of the ordinary mathematical engine.

The major unresolved Phase 1 questions are now:

Whether Boons and Banes cancel one-for-one in every circumstance.
Whether Boons above the pool ceiling convert into another effect.
The exact opposed multi-success procedure.
How high-tier superiority is expressed without larger dice.
Whether Mythic remains within the same DC scale using increased success requirements and permissions.
How equipment and spell effects express exceptional capability while respecting the bounded framework.
