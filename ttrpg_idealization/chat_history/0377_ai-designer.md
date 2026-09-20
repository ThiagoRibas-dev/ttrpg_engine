---
turn: 377
role: "AI-Designer"
source: chat_history.json
---

# Turn 377 — AI-Designer

Yes. Your comments simplify the target-calibration task considerably. We do not need to invent a separate universal difficulty taxonomy if the research tables already provide Tier-relative vectors.

Revised Interpretation of the Ten Points
1. Difficulty categories

We do not need globally canonical labels such as:

text
Easy
Medium
Hard

Those can remain research shorthand.

The more useful design language is:

text
Trained-Tier Check
Veteran-Tier Check
Master-Tier Check
Hero-Tier Check
Legend-Tier Check

with internal difficulty bands such as:

text
Trained-Tier:
  Easy / Moderate / Hard

Veteran-Tier:
  Easy / Moderate / Hard

But these are design-analysis labels, not necessarily table-facing rules.

At the table, the GM uses the actual vector:

text
DC 5
DC 5,4
DC 6,6

The labels help designers compare equivalent tasks across tiers.

2. Reference actor profiles

The research already contains the necessary provisional information.

We should formalize the profiles as:

text
Decently prepared Tier character:
  Appropriate Attribute Die.
  Full-investment Competency Rank.
  Good, but not optimal, equipment.
  No extreme temporary stacking.

For example:

Tier	Attribute Die	Competency Pool	Equipment Profile	Final Pool
Trained	d8	2d8	+1 die	3d8
Veteran	d8	3d8	+1 or +2 dice	4d8 or 5d8
Master	d10	4d10	+2 dice	6d10
Hero	d10	5d10	+3 dice	8d10
Legend	d12	6d12	+3 dice	9d12

The “good but not optimal equipment” assumption should become the standard calibration profile.

3. Success types

These are already conceptually separated:

text
DC X:
  One-threshold check.

DC X,Y:
  Two-threshold check.

DC X,Y,Z:
  Three-threshold check.

Opposed:
  Compare attacker and defender pools.

The distinction between vector lengths is not merely difficulty. It also gates complexity by requiring enough useful Dice Pool volume.

A character may technically roll a three-threshold vector with three dice, but a one-die character cannot meaningfully attempt it.

For opposed checks, we do not need to impose arbitrary target probabilities. The probabilities emerge from:

Die Size.
Pool Size.
Equipment dice.
Boons and Banes.
Secondary dice.
Defender Wins Ties.

Your intended combat result is:

Equal attacker and defender pools favor the defender because the defender wins ties.

That creates a reason to attack weaker defenses or seek positional and tactical advantages.

4. Probability bands

These can be promoted from provisional targets to design-canon calibration bands:

text
Easy:
  80–85%

Medium:
  60–65%

Hard:
  40–45%

They apply relative to the actor’s Tier.

That means:

text
Trained character performing a Trained-Tier Easy check:
  80–85%

Veteran character performing a Veteran-Tier Easy check:
  80–85%

Master character performing a Master-Tier Easy check:
  80–85%

The mathematical curve is intentionally similar across Tiers, like PF2e’s level-relative math.

Lower-Tier checks become easier for higher-Tier actors because the higher-Tier actor has:

Larger Dice.
Larger Dice Pools.
More equipment support.
More available Permissions.
Better access to Automatic Successes.

This is a strong and coherent design objective.

5. Equipment assumptions

The calibration profile assumes:

text
Better than baseline,
but not best-in-slot or fully optimized.

This means the probability bands are calculated after:

Appropriate equipment.
Expected equipment dice.
Ordinary temporary support.
No extreme stacking.
No Mythic effects.
No exceptional Class or Feat combinations unless specifically part of the profile.

The exact equipment system remains open, but the calibration assumption is now clear.

6. Advancement expectations

We do not need to invent separate advancement probability targets.

We derive them from:

text
Character Tier
+ Attribute Die
+ Competency Pool
+ Equipment Profile
+ Tier-relative Difficulty Vector

The research progression charts already show whether the intended constant-band behavior is occurring.

The key advancement expectation is:

text
Same-Tier checks:
  Stable probability band.

Lower-Tier checks:
  Increasingly easy as the character advances.

Higher-Tier checks:
  Increasingly difficult or impossible without exceptional tools.

7. Opposed probability targets

We can calculate these using the same representative progression profiles.

The opposed research should measure:

text
Same-Tier attacker vs same-Tier defender.
One Tier advantage.
One Dice Pool advantage.
One Die Size advantage.
Equipment advantage.
Boon/Bane advantage.

We do not need to define a universal target such as “the attacker should win 45% of the time.”

Instead, we should observe whether the resulting probability behavior matches the desired tactical principle:

Equal pools favor the defender; attacking a weaker defense is strategically important.

8. Multiple-success expectations

I agree that this should become the first next step.

We should establish a convention based on vector length:

text
Easy:
  Always one threshold.

Medium:
  One or two thresholds.

Hard:
  Two or three thresholds.

Extreme:
  Three or more thresholds.

The notation should refer to thresholds in the Difficulty Vector, not dice.

For example:

text
Easy:
  DC 6

Medium:
  DC 6,5
  or DC 7

Hard:
  DC 7,6
  or DC 8,7,5

Different vector shapes can produce similar probabilities while gating the task differently.

This is especially valuable because:

text
DC 8

and:

text
DC 6,5

may have similar success chances for one pool but demand different capability profiles.

One favors:

High Die Size.

The other favors:

More Dice.
Better pool volume.
The ability to satisfy multiple thresholds.

This should be the next calibration pass.

9. Impossible and automatic ranges

These should be derived after the vector calibration.

Once we have the available vectors and representative pools, we can identify:

Impossible

A vector cannot be satisfied because:

The Die Size cannot reach a threshold.
The pool does not have enough dice.
The required vector length exceeds the available pool.
The final probability is mathematically zero.
Automatic or near-automatic

A vector becomes:

Automatic through an Automatic Success.
Near-automatic through high Dice Pool volume.
Routine through Tier-relative calibration.
Exceptionally easy for higher-Tier actors.

These should be observed rather than imposed prematurely.

10. What “Final Probability Targets” means

The final target framework depends on the Difficulty Vector pass.

At this point, we can formalize only the general design principles:

text
Tier-relative difficulty bands remain stable.

Equipment is included in the expected prepared profile.

Difficulty vectors may use different lengths to gate different capability profiles.

Opposed probabilities emerge from the shared framework.

Automatic and impossible ranges are consequences of the vectors and pools.

The actual per-level vector assignments should be the final result of the next calibration phase.

Revised Priority Order

The correct order is now:

Keep the current probability bands as design-canon calibration bands.
Formalize the decently prepared Tier profiles.
Build one-, two-, and three-threshold vector options for each Tier.
Tune each Tier’s Easy, Medium, and Hard vectors.
Compare vector options with similar probabilities but different capability gates.
Derive automatic and impossible cases.
Calculate opposed probabilities from the resulting progression profiles.
Review whether the bands remain appropriate.
Record the finalized probability targets and vector conventions.

So yes: Multiple-threshold Difficulty Vector calibration should come before finalizing the rest of the probability-target framework. It determines how much granularity and capability-gating the system actually has.
