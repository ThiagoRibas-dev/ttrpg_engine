---
turn: 333
role: "AI-Designer"
source: chat_history.json
---

# Turn 333 — AI-Designer

Yes. The recent conclusions are not fully recorded yet. The following items are either newly decided, newly proposed, or now supersede earlier decisions.

Newly Decided but Not Yet Recorded
1. Remove the explicit Floor mechanic

The Floor should be removed as an independent resolution mechanic.

The new model is:

text
Competency Rank → Baseline Dice Pool Size
Equipment/Boons/Banes → Final Dice Pool Size
Dice Pool + Difficulty Vector → Probability of success

There is no separate:

text
Floor
Floor lookup
Competency-specific Floor
Floor cap

This supersedes the recently recorded pool-derived Floor model from DEC-062.

The remaining role of Competency is primarily:

Baseline Dice Pool Size.
Tradition or Skill access.
Content-specific Permissions.
Rank-based advancement.
2. Replace DC X (Y) with difficulty vectors

The new notation is:

text
DC X,Y

rather than:

text
DC X (Y)

Examples:

text
DC 5
DC 5,4
DC 5,5
DC 6,5,3

A difficulty vector consists of ordered Target Numbers rather than one Target Number plus a Required Success count.

3. Difficulty-vector resolution procedure

The intended procedure is:

Roll the final Dice Pool.
Sort the dice from highest to lowest.
Sort the difficulty vector from highest to lowest.
Compare them positionally.
Extra dice beyond the vector length are ignored for that specific difficulty vector.
The check succeeds only if every vector threshold is met.

Example:

text
Pool: 8, 6, 3
Difficulty: DC 5,4

Result:

text
8 ≥ 5
6 ≥ 4
Success
4. Fixed-die difficulty vectors are now the preferred calibration model

The vector approach produced substantially smoother probability curves than the previous flat-DC/Required-Success approach.

The current research direction is therefore:

text
Single-threshold difficulty:
  DC X

Multi-threshold difficulty:
  DC X,Y
  DC X,Y,Z

No DC X (Y) notation should remain in the eventual canonical system.

Newly Established Provisional Calibration Assumptions
5. Probability bands

The current working target bands are:

text
Easy:   80–85%
Medium: 60–65%
Hard:   40–45%

These are still calibration targets, not finalized universal DC rules.

6. Equipment progression profile

The current provisional fully equipped progression is:

Tier	Levels	Attribute Die	Baseline Pool	Equipment Boons	Final Pool
Trained	1–4	d8	2d	+1B	3d8
Veteran	5–8	d8	3d	+1B	4d8
Veteran	7–8	d8	3d	+2B	5d8
Master	9–12	d10	4d	+2B	6d10
Hero	13–16	d10	5d	+3B	8d10
Legend	17–20	d12	6d	+3B	9d12

Your latest table uses a slightly simplified version:

text
Levels 1–4:
  3d8

Levels 5–8:
  4d8

Levels 9–12:
  6d10

Levels 13–16:
  8d10

Levels 17–20:
  9d12

The precise level-by-level equipment schedule still needs to be recorded as a provisional calibration profile rather than canonical equipment rules.

7. Provisional per-tier difficulty vectors

The current representative vectors are:

Tier	Pool	Easy	Medium	Hard
Trained	3d8	DC 5	DC 5,4	DC 5,5
Veteran	4d8	DC 6	DC 6,5	DC 6,6
Master	6d10	DC 8	DC 9,7	DC 10
Hero	8d10	DC 9	DC 9,8	DC 9,9
Legend	9d12	DC 11	DC 11,10	DC 12

These currently produce a much smoother curve, generally within roughly a five-percentage-point band.

They should be recorded as:

text
Provisional probability-calibration examples

not as final Difficulty Class assignments.

Previously Recorded Decisions Now Superseded
Pool-derived Floors

DEC-062 recorded:

text
Final Dice Pool Size → Floor

That decision is now superseded by the decision to remove explicit Floors.

The future decision log should record a new entry explicitly superseding it.

Competency Rank table

The Tier-aligned Competency model from DEC-063 remains useful:

text
Untrained: 1dX
Trained: 2dX
Veteran: 3dX
Master: 4dX
Hero: 5dX
Legend: 6dX

However, its Floor column must be removed.

Still Open After These Changes
1. How high-tier reliability is represented

Without Floors, high-tier reliability must come from:

Larger Dice Pools.
Difficulty vectors.
Automatic Successes.
Permissions.
Equipment.
Class and Feat effects.
Mythic effects.

We need to decide when larger pools should convert into Automatic Successes or simply continue adding dice.

2. Vector length limits

We still need to decide whether ordinary content may use:

text
DC X
DC X,Y
DC X,Y,Z

and whether four- or five-threshold vectors are reserved for:

Complex Activities.
Legendary tasks.
Mythic tasks.
Rituals.
Crafting clocks.
3. Extra-die behavior

Under the vector system:

text
8d10 against DC 9,8

uses the two highest dice to meet the two thresholds, while six additional dice are ignored for that vector.

We need to decide whether extra dice can provide:

Additional effect.
Faster completion.
Extra damage.
Automatic Successes.
Critical or exceptional results.
4. Bane effects without Floors

Banes now simply affect Dice Pools:

text
4d8 +1 Bane → 3d8
1d8 +1 Bane → 1d6

But without Floors, we need to re-evaluate:

Untrained low-pool behavior.
How harsh Banes should be.
Whether one-die pools are too fragile.
Whether a Step-Down from d4 remains automatic failure.
Whether conditions should impose Banes or direct Permissions/Restrictions.
5. Competency Rank and die size

Competency now determines baseline pool size, but not Die Size.

We still need to preserve the separate role of:

text
Attribute Die Size:
  Numerical ceiling.

Competency Pool Size:
  Number of attempts at satisfying a difficulty vector.

Equipment:
  Additional dice and special effects.
Immediate Recording Needed

The next decision-recording update should include:

text
DEC-064 — Difficulty Vectors and Removal of Explicit Floors

It should record:

Explicit Floors are removed.
Competency determines baseline Dice Pool Size only.
Difficulty uses comma-separated threshold vectors.
DC X is a single-threshold vector.
DC X,Y compares the two highest dice to two thresholds.
Probability calibration uses Easy 80–85%, Medium 60–65%, and Hard 40–45% as provisional bands.
The current fully equipped tier profiles are provisional calibration assumptions.
DEC-062 is superseded.

The recent vector matrices and chart are already recorded as research artifacts, but the canonical rules and decision log have not yet been updated to reflect this change.
