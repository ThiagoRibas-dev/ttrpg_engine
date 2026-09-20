---
turn: 375
role: "AI-Designer"
source: chat_history.json
---

# Turn 375 — AI-Designer

It means deciding what probability the game should normally produce for each combination of actor capability and task difficulty.

It is not simply assigning:

text
Routine = DC 3
Challenging = DC 5
Formidable = DC 7

because the same DC can be trivial for a Legend character and difficult for an Untrained character.

What Final Probability Targets Entail
1. Define the difficulty categories

We need define what these labels mean fictionally:

Routine.
Challenging.
Formidable.
Heroic.
Legendary or Extreme, if retained.

For example:

text
Routine:
  A trained professional should usually succeed.

Challenging:
  A competent specialist should succeed more often than not,
  but failure remains meaningful.

Formidable:
  Requires serious specialization, preparation, or favorable conditions.

Heroic:
  Normally unreliable without exceptional investment or expenditure.

Legendary:
  Normally inaccessible except to top-tier characters or special content.

The names should describe the task, not merely the probability.

2. Define reference actor profiles

We need decide whose probability we are measuring.

Possible profiles:

text
Untrained generalist
Trained specialist
Veteran specialist
Master specialist
Hero specialist
Legend specialist
Fully equipped specialist
Poorly equipped specialist

For example:

text
Level 1 Trained specialist:
  d8
  2d8 baseline
  3d8 equipped

Level 9 Master specialist:
  d10
  4d10 baseline
  6d10 equipped

Level 17 Legend specialist:
  d12
  6d12 baseline
  9d12 equipped

The target probability for a difficulty category is meaningless without a reference profile.

3. Define success type

We need distinguish:

Single-threshold success
text
DC 7

The highest die must meet or exceed 7.

Difficulty-vector success
text
DC 7,5

The highest die must meet 7 and the second-highest must meet 5.

Opposed success
text
Attacker pool versus Defender pool

The attacker must beat the defender under the tiebreak procedure.

These should not necessarily have identical probability targets.

4. Define probability bands

The current provisional bands are:

text
Easy:
  80–85%

Medium:
  60–65%

Hard:
  40–45%

Final calibration would determine whether those bands are actually suitable and how they apply across tiers.

For example:

Difficulty	Fully equipped specialist target
Routine/Easy	80–85%
Challenging/Medium	60–65%
Formidable/Hard	40–45%
Heroic	20–35%
Legendary	5–20%

Those additional bands are only examples; they are not currently decided.

5. Define whether targets apply before or after equipment

This is crucial.

A task may be calibrated against:

text
Unmodified character pool

or:

text
Expected fully equipped character pool

Your recent tables use fully equipped pools, for example:

text
Level 1:
  2d8 baseline → 3d8 equipped

Level 9:
  4d10 baseline → 6d10 equipped

We need decide whether “expected success chance” means:

Baseline character without equipment.
Normally equipped character.
Optimally equipped specialist.
Character with normal temporary support.
Character with all available Boons and resources.

Different choices produce very different DC recommendations.

6. Define advancement expectations

Final probability targets should describe how the probability curve evolves.

For example:

text
A Trained specialist should have:
  High odds against Routine tasks.
  Moderate odds against Challenging tasks.
  Low odds against Formidable tasks.

A Master specialist should have:
  Automatic or near-automatic Routine success.
  High odds against Challenging tasks.
  Moderate odds against Formidable tasks.
  Meaningful odds against Heroic tasks.

This establishes whether advancement should:

Maintain a stable difficulty curve.
Make lower-tier tasks automatic.
Increase access to higher Difficulty Vectors.
Increase the number of successes possible.
Create more Permissions rather than merely higher odds.
7. Define opposed probability targets

For opposed checks, we need decide expected win rates.

Examples:

text
Equal pools:
  Attacker wins slightly less than 50% because Defender Wins Ties.

One-die pool advantage:
  Superior actor wins approximately 55–65%.

One-die size advantage:
  Superior actor wins approximately 60–70%.

One Competency Tier advantage:
  Superior actor wins approximately 70–85%.

Multiple-tier mismatch:
  Lower-tier actor usually fails unless using special resources or Permissions.

These are not yet final targets.

We should measure:

Equal pool versus equal pool.
Different pool sizes.
Different die sizes.
Different pool and die sizes.
Automatic Success differences.
Equipment differences.
Conditions and Banes.
8. Define multiple-success expectations

Difficulty Vectors allow us to distinguish:

text
DC 5
DC 5,4
DC 5,5
DC 6,5,3

Final probability targets should determine whether:

Routine tasks use one threshold.
Complex tasks use two thresholds.
Heroic tasks use three or more thresholds.
Higher-tier characters should gain access to longer vectors.
Equipment should add dice so characters can attempt longer vectors.
Extra dice beyond the vector create no benefit or some secondary effect.
9. Define impossible and automatic ranges

We need deliberately classify extremes.

Impossible

A character cannot satisfy the vector because:

text
The die cannot reach the threshold.

Example:

text
2d6 against DC 8
Automatic

A character succeeds without rolling because:

A Permission says so.
Automatic Successes satisfy the whole vector.
The task is beneath their Competency.
The content explicitly treats it as routine.
Exceptional

A character can attempt something normally impossible because of:

A Die Step-Up.
Equipment.
A spell.
A Class feature.
A Mythic Permission.
Automatic Successes.

This prevents the rules from accidentally making extreme outcomes ordinary.

10. Define what “final” means

A final probability target should specify:

text
Actor profile
Task category
Equipment state
Temporary Boon/Bane state
Difficulty vector
Success type
Expected probability range

For example:

text
Level 9 fully equipped Master specialist
against a Formidable task
using a single check
with no temporary Boons or Banes
should succeed approximately 40–60% of the time.

That is a usable target.

What We Have Already Established

We currently have:

Raw Dice Pool matrices.
Difficulty Vector matrices.
Equipment-aware provisional progression.
Provisional bands:
Easy: 80–85%.
Medium: 60–65%.
Hard: 40–45%.
Opposed probability tables.
Automatic Success reduction tables.
Difficulty-vector charts.
What Remains

To complete this task, we need decide:

Final names for the difficulty bands.
Final probability ranges for each band.
Which actor profile is used for calibration.
Whether calibration assumes normal equipment.
Whether temporary Boons/Banes are excluded.
How many thresholds each category normally uses.
Expected opposed win rates.
How automatic and impossible results are classified.
How progression should change probability versus permissions.
Whether the current bands remain appropriate after full combat, equipment, and magic testing.

So, in short:

Final probability targets are the game’s intended success-rate benchmarks for representative actors performing representative tasks under explicitly defined equipment, progression, and opposition assumptions.

They are the bridge between the raw mathematical tables and actual game-balance decisions.
