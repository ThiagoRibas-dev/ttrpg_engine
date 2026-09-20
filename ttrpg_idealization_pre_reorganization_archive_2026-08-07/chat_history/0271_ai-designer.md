---
turn: 271
role: "AI-Designer"
source: chat_history.json
---

# Turn 271 — AI-Designer

The three checklist items are mostly resolved at the framework level. What remains is formalizing edge cases and making the procedures precise enough that different future content writers will handle them identically.

1. Boon/Bane Stacking and Cancellation
Already resolved

The current framework establishes:

One Boon cancels one Bane.
One Bane cancels one Boon.
Boons are typed.
Multiple Boons of the same type do not stack.
Different Boon types may stack.
The same named source cannot apply the same Boon or Bane more than once to the same target or check.
Remaining Boons add same-size dice.
Remaining Banes remove dice.
A pool cannot be reduced below one die.
A Bane applied to a one-die pool causes one Die Step-Down.
Further Banes do not cause additional Die Step-Downs.
A Bane-induced Step-Down from d4 causes automatic failure.
Boons participate normally in Required Success counting.
Boons and Banes are applied after ordinary pool construction and Die Steps.
Still unresolved
A. Exact type vocabulary

We agreed to borrow the concept of typed modifiers from PF2e, but we have not established the actual types.

Questions:

Which Boon/Bane types exist?
Do we use:
Circumstance.
Status.
Item.
Ability.
Morale.
Environment.
Tradition.
Class.
Equipment.
Are all types mutually exclusive?
Can a Class Boon stack with a Feat Boon if both are technically “ability” effects?
Are some effects explicitly untyped?
B. Translating D&D 3.5e bonus types

We need a conversion mapping from common D&D categories:

Circumstance.
Competence.
Enhancement.
Morale.
Insight.
Luck.
Sacred.
Profane.
Size.
Racial.
Resistance.
Deflection.
Natural armor.

The open issue is whether all of these map cleanly to our smaller PF2e-inspired type vocabulary or whether some should become:

Traits.
Requirements.
Permissions.
Die Step-Ups.
Equipment properties.
Immunities.
C. Same-source identity

The current rule says the same named source cannot stack with itself.

We still need to define what counts as the same source.

Examples:

Three castings of the same spell: clearly same source.
Three different spells from the same Tradition: same source or different sources?
Two different Feats from the same Class: same source or separate sources?
Two allies using the same aura effect: same source because the effect is identical, or different because the casters differ?
A weapon and armor both granting “Item” Boons: same type but different sources.
D. Bane effect on Floors

The framework currently says:

Floors remain active.
Banes can lower the effective Floor when they reduce the final pool state.

The exact conversion is not yet formalized.

For example:

text
Expert:
  3d8, Floor 5

+1 Bane:
  2d8, Floor ?

Possible interpretations:

Floor remains 5.
Floor drops to Trained Floor 3.
Floor is reduced by one step but remains otherwise rank-based.
Floor is recalculated from the final effective pool.
Floor is unchanged unless the Bane causes a Die Step-Down.

This is the most important remaining Bane edge case.

E. Boons beyond the normal pool range

The normal natural pool is generally 2dX to 5dX, but high-tier content may exceed that guideline.

Still to define:

Do typed Boons continue stacking above 5dX?
Are additional dice always rolled?
Do excess dice become Automatic Successes?
Does content need to explicitly grant the permission to exceed 5dX?
Does a Bane remove dice from an expanded 7dX pool normally?
Can a pool of 10d12 exist, or should high-tier effects convert excess dice into Automatic Successes?
F. Interactions with Automatic Successes

Still to define:

Can Boons grant Automatic Successes?
Can Banes remove Automatic Successes?
Can a typed effect grant both a Boon and an Automatic Success?
Are Automatic Successes checked before or after a Bane?
Can a character have more Automatic Successes than the Required Success count?
G. Step order

The current intended order is:

Build the Natural Dice Pool.
Apply ordinary permanent and temporary effects.
Apply Die Step-Ups and Die Step-Downs.
Cancel typed Boons and Banes.
Add remaining Boon dice.
Remove remaining Bane dice.
Apply the Bane-induced one-die Step-Down if applicable.
Determine the final Floor.
Apply Automatic Successes.
Roll and resolve.

This needs to be written as the definitive order, especially because Floor behavior and Automatic Successes remain sensitive to sequencing.

2. Opposed-Roll Secondary Tie-Break Procedures
Already resolved

The current framework establishes:

The initiator is the attacker.
The responding party is the defender.
Compare the highest faces.
If tied, compare remaining dice in descending order.
If the results remain tied, the defender wins.
Some contests, such as races, may explicitly allow a neutral tie.
Baseline opposed checks produce success or failure only.
Counterattacks, Ripostes, and superior defensive effects require explicit Permissions.
Still unresolved
A. Exact sorting procedure

We need explicitly state whether a pool is sorted before comparison.

Example:

text
Attacker: 2, 7, 9
Defender: 3, 6, 9

The intended comparison appears to be:

text
Highest: 9 vs 9 — tie
Second: 7 vs 6 — attacker wins

The procedure should explicitly say:

Sort each pool from highest face to lowest face before applying secondary tiebreaks.

B. Different pool sizes

Example:

text
Attacker: 9, 7, 4
Defender: 9, 7

Questions:

Does the defender win because all defender dice tie?
Does the attacker win because the third die remains?
Does pool size itself become the final tiebreak?
Does the defender-win-ties rule apply as soon as the defender has no remaining die?

The current intended answer seems to be:

If all comparable dice tie and one pool has no remaining die, the defender wins.

But this needs explicit wording.

C. Different die sizes

Example:

text
Attacker: 2d10 → 10, 7
Defender: 2d8 → 8, 8

The attacker wins on the highest face.

But:

text
Attacker: 10, 7
Defender: 10, 8

The defender wins on the second die.

Questions:

Are raw face values always compared directly?
Does die size matter after the face is rolled?
Does a max-face result receive a special tiebreak advantage?
Are Automatic Successes excluded from tiebreaks? Current intent: yes.
D. Floors and tiebreaks

Example:

text
Attacker rolls: 3, 7
Floor 5 → 5, 7

Defender rolls: 5, 7
Floor 0

Are the tiebreak faces compared after Floors are applied?

The likely answer is yes:

Tiebreaking uses the final face values after Floors and other final result transformations.

That needs to be stated.

E. Boons and Banes in tiebreaks

Questions:

Are removed dice absent from the tiebreak pool?
Are added Boon dice eligible as secondary tiebreak dice?
Does a Bane that changes a one-die pool to a Step-Down affect only the die size or also the number of tiebreak dice?
Are automatic successes excluded from tiebreaking?

The current framework implies:

Removed dice do not exist for the tiebreak.
Boon dice are ordinary dice and participate normally.
Automatic Successes do not participate.
Die Step-Ups and Step-Downs affect the dice before rolling.
F. Neutral contests

We have an exception for races or contests that may end in a tie.

Still to define:

Which contests are neutral by default?
Does the GM choose whether a contest requires a winner?
Does “race” mean any movement contest, or only a formal race?
Can opposed Craft, Research, or Social contests end in a tie?
Does a neutral tie mean no progress, shared success, or a new complication?
G. Multi-success opposed contests

The current framework says highest-face comparison determines the opposed result, but it does not yet fully define what happens when both parties produce multiple successes.

Questions:

Is the contest always just won or lost?
Can an attacker win with a superior margin?
Does the number of successful secondary faces affect the consequence?
Can a Class, Feat, or Spell explicitly use the number of extra successes?
Does a DC X (Y) requirement apply to an opposed result?
3. High-Tier Effects Without Over-Cap Dice
Already resolved

The current framework establishes:

Ordinary dice stop at d12.
d12+ notation is deprecated.
Ordinary DCs remain within DC 2–12.
High-tier content may provide more dice.
5dX is a natural, unbuffed guideline rather than an absolute universal cap.
High-tier content may grant Automatic Successes.
Automatic Successes count toward Required Successes.
Automatic Successes are not dice.
Mythic continues using the bounded resolution language.
Mythic expands fictional scope more than it simply inflates numbers.
Immunities are not automatically bypassed by level or Competency.
Immunity bypass requires a specific Class, Feat, Spell, Equipment, Tradition, or Mythic Permission.
Still unresolved
A. Exact Automatic Success progression

We need decide how Automatic Successes enter the baseline framework.

Possible sources:

Legendary Competency.
Tier milestones.
Class features.
Feats.
Equipment.
Spells.
Mythic advancement.

Questions:

Does Legendary Competency grant an Automatic Success universally?
Does it apply to all checks in that Skill?
Does it apply only to tasks below a certain DC?
Can multiple Automatic Successes be earned from different sources?
Is there a normal cap per check?
Can a character use Automatic Successes on opposed checks?
B. Automatic Successes and ordinary failure

Example:

text
DC 12 (1)
4d8 +1 Automatic Success

Current intent:

text
Automatic success means the check succeeds regardless of the DC.

This is powerful, so we need to determine:

Whether that is universally true.
Whether some effects grant only “one success toward the requirement” rather than guaranteed task completion.
Whether a task can explicitly require a minimum rolled face in addition to Required Successes.
Whether special Requirements can block Automatic Success.
C. Maximum pool size

The system no longer has a hard universal pool cap, but 5dX remains the natural range.

Still to define:

What counts as a normal enhanced pool?
When should additional dice convert into Automatic Successes?
Can a content entry grant 8d12?
Can multiple content sources each extend the pool?
Does the same-source non-stacking rule apply to extra-dice effects?
Should Mythic characters receive additional dice, Automatic Successes, or both?
D. Required Success escalation

The current model allows:

text
DC 9 (3)
DC 12 (5)

Still to define:

The maximum normal Required Success value.
Whether DC 12 (5) is ordinary, Legendary, or Mythic.
Whether Required Successes can exceed the number of dice rolled.
Whether Automatic Successes can make otherwise impossible difficulties possible.
Whether high-tier characters gain special permissions against impossible DC combinations.
E. Mythic result manipulation

Possible Mythic Permissions include:

Choosing one or more die results.
Replacing a die result.
Rerolling a die using Essence.
Changing the Required Success count.
Changing the DC.
Treating a result as a maximum face.
Converting a failure into a partial success.
Affecting an entire zone, region, plane, or world.

The framework has accepted the general direction, but none of these are yet universal rules.

F. Equipment and high-tier effects

Equipment may eventually grant:

Permanent typed Boons.
Automatic Successes.
Fixed damage.
Immunities.
Penetration.
Ignoring certain attacks.
Ignoring certain defenses.
Action-economy Permissions.

Still to define:

Which of these are universal equipment vectors.
Which remain item-specific.
Whether an Automatic Success from equipment can stack with one from a Class or Feat.
Whether godly equipment can bypass an immunity without a separate Permission.
Recommended Next Work

The three checklist items are not fully complete yet, but their baseline architecture is established.

The remaining work should be handled in this order:

Write the final Boon/Bane sequencing procedure.
Define typed Boon categories and same-source identity.
Resolve Bane/Floor interaction precisely.
Write the exact opposed-roll sorting and tiebreak procedure.
Define the neutral-contest exception.
Define Automatic Success interaction with DCs, Required Successes, Banes, and ties.
Define the natural versus exceptional pool ranges.
Leave Mythic-specific content effects for later content design.

The single most important immediate issue is the Bane/Floor interaction, followed by the exact definition of Automatic Success. These two decisions affect nearly every future subsystem.
