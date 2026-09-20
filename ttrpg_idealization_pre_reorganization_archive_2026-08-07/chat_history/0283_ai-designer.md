---
turn: 283
role: "AI-Designer"
source: chat_history.json
---

# Turn 283 — AI-Designer

We should do them in the same overall probability-calibration pass, but as two sequential steps rather than two unrelated projects.

Recommended Sequence
Step 1: Build the Probability Tables

First calculate the actual probabilities for the current framework:

Pool sizes:
1dX through relevant expanded pools.
2dX through 5dX.
Exceptional pools above 5dX, if retained.
Die sizes:
d4, d6, d8, d10, d12.
DCs:
DC 2.
DC 3.
DC 5.
DC 7.
DC 9.
DC 11.
DC 12.
Competency Floors:
Floor 0.
Floor 3.
Floor 5.
Floor 7.
Floor 9.
Boons.
Banes.
Die Step-Ups.
Required Successes:
DC X (1).
DC X (2).
DC X (3).
Higher thresholds where relevant.
Opposed pools.
Automatic Successes.

This produces the empirical map of how the current rules actually behave.

Step 2: Establish Probability Targets

Only after seeing the tables should we decide what the target probabilities should be.

For example:

text
Routine:
  Trained character should almost always succeed.

Challenging:
  Trained character should succeed reliably but not automatically.

Formidable:
  Expert or specialized characters should have strong odds.

Heroic:
  Master or Legendary characters should have meaningful chances.

Legendary:
  Only high Attribute + high Competency + appropriate resources
  should approach reliable success.

Opposed:
  Equal-tier contests should remain uncertain.
  Superior investment should create a meaningful but not absolute advantage.

The actual percentages should come from the first step rather than being chosen in a vacuum.

Why Doing Targets First Is Risky

If we establish targets first, we may say:

text
Routine should be 85%.
Challenging should be 65%.
Heroic should be 35%.

Then discover that:

Floors make Routine checks automatic.
Boons make Challenging checks too reliable.
Required Successes make high-pool characters too dominant.
Banes have a much larger effect than expected.
Die Step-Ups create hard probability jumps.
Automatic Successes trivialize DC 12.
Opposed ties occur too frequently or too rarely.

The tables need to expose those interactions before the targets can be responsibly locked.

Recommended Workstream Structure

I would organize it as:

Probability Calibration Pass 1 — Baseline Dice
1dX through 5dX.
No Floor.
DC 2–12.
Highest-face success probability.
Number of successful dice.
Probability Calibration Pass 2 — Floors
Apply Floors 3, 5, 7, and 9.
Determine when tasks become automatic.
Verify whether Floors create the intended competency identity.
Probability Calibration Pass 3 — Boons and Banes
Typed effects do not alter probability by type; the number of dice does.
Test Boon/Bane cancellation.
Test one-die Bane Die-Step-Down.
Test Floor behavior after Banes.
Test expanded pools.
Probability Calibration Pass 4 — Die Steps
Compare:
2d8 versus 2d10.
3d8 versus 3d10.
5d10 versus 5d12.
Test Step-Ups against higher DCs.
Test Step-Downs against lower DCs.
Probability Calibration Pass 5 — Required Successes
DC X (1).
DC X (2).
DC X (3).
High-pool characters versus multi-success tasks.
Probability Calibration Pass 6 — Automatic Successes
One Automatic Success.
Two Automatic Successes.
Automatic Successes against DC X (1).
Automatic Successes against DC X (2+).
Interaction with opposed contests.
Probability Calibration Pass 7 — Opposed Contests
Equal pools.
One Die Step difference.
One Boon difference.
One Competency Rank difference.
Different Floors.
Different pool volumes.
Defender-wins-ties frequency.
Automatic Success totals.
Probability Calibration Pass 8 — Target Setting

Only after the above is complete:

Define Routine target behavior.
Define Challenging target behavior.
Define Formidable target behavior.
Define Heroic target behavior.
Define Legendary target behavior.
Define equal-tier opposed expectations.
Define superior-tier opposed expectations.
Important Distinction

We should distinguish:

Mathematical targets

Examples:

text
Trained vs DC 3 should be automatic.
Expert vs DC 5 should be automatic.
Master vs DC 7 should be automatic.
Legendary vs DC 9 should be automatic.

These may already follow from the Floors.

Design targets

Examples:

text
A routine action should usually succeed.
A Heroic action should be possible but risky.
An equal-tier opposed contest should not be predetermined.
A specialist should outperform a generalist without eliminating uncertainty.

The first category comes from calculation. The second comes from play goals.

Recommendation

Do them as one Probability Calibration workstream with two sequential deliverables:

Probability Tables: What the current mathematics produces.
Probability Targets: What the game wants the mathematics to produce.

Then compare the two and decide whether the framework needs adjustment.

I would not mark the probability targets as permanently final until they have been checked against:

Combat pacing.
Equipment.
Spellcasting.
Conditions.
Class progression.
Monster scaling.
Actual playtest scenarios.

But we can establish provisional target bands during the same pass.
