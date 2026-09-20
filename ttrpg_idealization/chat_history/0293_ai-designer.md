---
turn: 293
role: "AI-Designer"
source: chat_history.json
---

# Turn 293 — AI-Designer

Yes, plotting progression is useful—but I would not begin by fitting dice directly to Character Level.

The key reason is that Floors are tied to Competency Rank, not Character Level. A Level 10 character can be:

text
Untrained in a Skill:
  Floor 0

Trained:
  Floor 3

Expert:
  Floor 5

Master:
  Floor 7

So Probability Calibration Pass 2 should first study the mathematical effect of Floors independently, then apply those results to level-by-level character profiles.

1. First Define the Floor Model Mathematically

The current implied model is:

A Floor clips any rolled die face below the Floor up to the Floor.

Example:

text
Roll: 2, 4, 8
Floor: 5

Final result: 5, 5, 8

This matters for both:

Highest-result checks.
Required-success counting.

For a pool of N dice of size S with Floor F:

text
Each die result becomes:
  max(rolled face, F)
Consequence for one-success checks

For a threshold T:

text
If T ≤ F:
  Every die succeeds automatically.

If T > F:
  The Floor does not change the probability of that die
  reaching T; the raw die still needs to roll T or higher.

Therefore:

text
P(at least one success with Floor F)

is:

text
100% whenever DC ≤ Floor

and otherwise follows the raw dice probability.

This means Floors primarily create reliability bands, not higher ceilings.

2. Important Consequence

An Expert character with:

text
3d8, Floor 5

has:

text
100% success against DC 5

but their odds against DC 7 are still determined by rolling 3d8.

A Master character with:

text
4d10, Floor 7

has:

text
100% success against DC 7

but still relies on the raw dice against DC 9.

This is mathematically elegant because:

Competency Floor determines the lower band they cannot fail.
Die Size determines the upper numerical ceiling.
Pool Volume determines reliability at higher thresholds.
3. Required-Success Floors

Floors become especially important when we use:

text
DC X (Y)

Example:

text
3d8, Floor 5
DC 5 (2)

Every die is clipped to at least 5, so all three dice count as successes:

text
3 automatic rolled successes

The character automatically clears DC 5 (2).

For:

text
DC 7 (2)

the Floor does not automatically help, because the dice still need to roll 7 or higher.

This produces a useful distinction:

text
Floor:
  Guarantees success against lower thresholds.

Pool Volume:
  Improves the chance of multiple successes.

Die Size:
  Determines access to higher thresholds.
4. Recommended Calibration Pass 2 Structure
Pass 2A — Single-Success Floor Matrices

Create matrices for:

1d4 through relevant pool sizes.
Floors 0, 3, 5, 7, and 9.
Thresholds 1 through 12.

Each cell answers:

text
What is the probability of at least one die
meeting or exceeding threshold T?

Expected pattern:

text
Floor 3:
  100% against DC 1–3.

Floor 5:
  100% against DC 1–5.

Floor 7:
  100% against DC 1–7.

Floor 9:
  100% against DC 1–9.

This visually demonstrates what Floors do.

Pass 2B — Multi-Success Floor Matrices

Then calculate:

text
P(at least Y successes against DC X)

for:

text
DC X (1)
DC X (2)
DC X (3)
DC X (4)

For example:

text
3d8, Floor 5, DC 5 (2)

is automatic because all three dice are at least 5.

But:

text
3d8, Floor 5, DC 7 (2)

requires at least two natural results of 7 or higher.

This pass is essential because Floors may make low-DC multi-success challenges automatic much earlier than expected.

Pass 2C — Floor Impact Curves

Plot the difference between:

text
No Floor
Floor 3
Floor 5
Floor 7
Floor 9

for the same dice pool.

For example:

text
3d8:
  Floor 0
  Floor 3
  Floor 5

against thresholds from 1 to 12.

The plot should reveal:

Where the Floor makes no difference.
Where it creates automatic success.
Where it has no effect because the threshold exceeds the Floor.
How Floors reshape the lower tail of the distribution.
5. Only Then Add Level-by-Level Profiles

After understanding Floors independently, we can create level snapshots.

These should not assume that every character has the same Skill Rank. Instead, define representative profiles.

Example profiles
Generalist
text
Attribute: d8 by Veteran
Competency: Trained
Pool: 3d8
Floor: 3
Specialist
text
Attribute: d8
Competency: Expert
Pool: 3d10
Floor: 5
Master
text
Attribute: d10
Competency: Master
Pool: 4d12
Floor: 7
Legendary specialist
text
Attribute: d12
Competency: Legendary
Pool: 5d12
Floor: 9

Then place them at representative levels:

text
Level 1
Level 5
Level 9
Level 13
Level 17
Level 20

This gives us progression snapshots without falsely assuming that Character Level automatically determines Skill Competency.

6. What to Plot for Each Profile

For each profile, plot:

One-success probability
text
P(at least 1 success against DC 2–12)
Multi-success probability
text
P(DC X (2))
P(DC X (3))
P(DC X (4))
Automatic bands

Mark:

text
Thresholds automatically cleared by the Floor.
Ceiling access

Mark:

text
Highest DC that the die size can possibly reach.

For example:

text
3d8, Floor 5:
  Automatically clears DC 5.
  Can reach DC 8.
  Cannot reach DC 9 without a Die Step-Up.
7. Should We Fit the Dice to Desired Percentages?

Eventually, yes—but not immediately.

The correct sequence is:

text
1. Calculate what the current dice and Floors produce.
2. Plot representative advancement profiles.
3. Compare the curves to desired play goals.
4. Identify mismatches.
5. Decide whether to alter:
   - Dice.
   - Pool volume.
   - Floors.
   - DC categories.
   - Required Successes.
6. Recalculate.

We should not begin by declaring:

text
Routine = 85%
Challenging = 65%
Heroic = 35%

Instead, first observe the current model.

8. Main Questions for Floor Calibration

The most important questions are:

Should Floor 3 make all DC 3 tasks automatic even for a one-die pool?
Should Floor 5 make DC 5 (2) automatic for every Expert pool?
Should Floors clip every individual die or only the highest result?
Should a Floor apply to damage and defense pools?
Should a Bane lower the Floor only when it causes a pool-volume reduction?
Should conditions be able to lower Floors directly?
Should Automatic Successes and Floors count identically toward Required Successes?
Should a Floor ever exceed the final die size minus one?
Should high-tier content grant additional Floors, Automatic Successes, or both?
Should the Floor be recalculated from the final pool after Boons and Banes?

The current framework points toward:

text
Floors clip individual die faces.
Floors affect Required Success counting.
Banes may lower the effective Floor through pool reduction.
The final Floor cannot exceed one less than the final die size.

Those assumptions should be explicitly tested in Pass 2.

Recommendation

Yes, create level-by-level progression plots—but only after making the Floor matrices first.

The recommended order is:

text
1. Raw dice matrices.
2. Floor-adjusted single-success matrices.
3. Floor-adjusted Required-Success matrices.
4. Floor impact curves.
5. Representative Level 1–20 competency profiles.
6. Comparison against provisional play-goal targets.
7. Final probability-target discussion.

The key principle is:

Do not fit Floors to Level. Fit Floors to Competency, then observe how Classes and Skill investment distribute Competency across Levels.
