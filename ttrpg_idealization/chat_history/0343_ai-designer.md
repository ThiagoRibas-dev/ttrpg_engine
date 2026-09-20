---
turn: 343
role: "AI-Designer"
source: chat_history.json
---

# Turn 343 — AI-Designer

We have a strong first pass, but the consolidated probability work is not complete yet.

Already completed
Raw Dice Matrices
text
09_at_least_probability_matrices.md

Contains raw probabilities for:

d4.
d6.
d8.
d10.
d12.
Multiple pool sizes.
At-least-one-success thresholds.
Multi-Success Matrices
text
12_multi_success_probability_matrices.md

Contains probabilities for:

text
P(at least R successes in NdS)

This was based on the previous DC X (R) model, so parts of it are now superseded by the Difficulty Vector model.

Difficulty-Vector Matrices
text
14_difficulty_vector_probability_matrices.md

Contains:

Single-threshold DC X probabilities.
Two-threshold DC A,B matrices.
Representative three-threshold calibration.
Selected pools such as:
3d8
4d8
5d8
6d10
8d10
9d12
10d12
Provisional Tier Calibration
text
13_probability_band_calibration.md
15_provisional_tier_difficulty_vectors.png

These use the provisional bands:

text
Easy:   80–85%
Medium: 60–65%
Hard:   40–45%

and the provisional fully equipped pool progression.

What Is Missing
1. Rebuild the multi-success research around Difficulty Vectors

The old artifact:

text
12_multi_success_probability_matrices.md

still describes:

text
DC X (Y)

and Required Successes.

The current model uses:

text
DC X
DC X,Y
DC X,Y,Z

It should either be:

Archived as a historical pre-vector artifact; or
Rewritten as a Difficulty Vector research document.

The old matrices remain mathematically useful, but their terminology and interpretation are outdated.

2. Complete Difficulty-Vector matrices

We currently have useful pair matrices, but not a fully systematic catalogue.

Still needed:

Every single threshold DC X.
Every two-threshold vector DC A,B.
Three-threshold vectors.
Potentially four- and five-threshold vectors.
All relevant standard dice.
All relevant pool sizes.
Expanded pools caused by equipment and other effects.
A documented rule for the maximum ordinary vector length.

The open design question is whether ordinary content can use:

text
DC X,Y,Z

but reserve:

text
DC W,X,Y,Z
DC V,W,X,Y,Z

for complex Activities, rituals, equipment creation, or Mythic effects.

3. Add Boon matrices

We need calculate how Boons change probability in the current system.

Examples:

text
2d8
3d8
4d8
5d8
6d8

and:

text
2d8 +1B
2d8 +2B
2d8 +3B

Because Boons simply add dice, this is mathematically equivalent to comparing different pool sizes.

However, we still need explicit tables for:

At-least-one success.
Difficulty vectors.
Multiple thresholds.
Equipment Boon progression.
Typed Boon combinations.

The type itself does not alter probability. It determines whether the Boon may stack with another Boon.

4. Add Bane matrices

We need calculate the final probabilities for:

text
2d8 +1 Bane
3d8 +1 Bane
4d8 +1 Bane

and so on.

The current rules are:

text
Bane:
  Remove one die.

If only one die remains:
  Die Step-Down once.

Further Banes:
  No additional worsening.

The research should include:

Standard pool reduction.
One-die pool behavior.
d4 Step-Down automatic failure.
Bane effects on Difficulty Vectors.
Bane effects on expanded equipment pools.
Same-type and same-source stacking treated as separate probability versus eligibility questions.
5. Add Die Step-Up matrices

We need compare:

text
Nd4 → Nd6
Nd6 → Nd8
Nd8 → Nd10
Nd10 → Nd12

for the same pool size and difficulty vector.

Examples:

text
3d8 versus 3d10
4d8 versus 4d10
5d10 versus 5d12

This will show the difference between:

More dice.
Larger dice.
More difficult thresholds.
Multi-threshold vectors.

This is especially important because our system separates:

text
Attribute:
  Die Size.

Competency/Equipment:
  Pool Size.
6. Recalculate with the current Competency progression

The current full-investment progression is now:

Tier	Competency	Baseline Pool
Trained	Trained	2 dice
Veteran	Veteran	3 dice
Master	Master	4 dice
Hero	Hero	5 dice
Legend	Legend	6 dice

The probability artifacts should use this nomenclature and should no longer include Floors.

7. Recalculate the full Level 1–20 progression

The current chart uses representative Tier entry levels:

text
1, 5, 7, 9, 13, 17, 19

We should eventually produce a complete level-by-level table using:

Character Level.
Tier.
Competency Rank.
Attribute Die Size.
Baseline Pool.
Equipment Boons.
Final Dice Pool.
Provisional Easy vector.
Provisional Medium vector.
Provisional Hard vector.
Actual probability of each vector.

This will show whether the apparent smoothness holds across every level, not just representative breakpoints.

8. Reconcile the equipment progression

The latest equipment progression differs from some earlier research assumptions.

Current provisional table:

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

The research artifacts need to clearly identify this as the current provisional calibration profile.

It should not yet be treated as canonical equipment rules.

9. Add opposed probability tables

The current matrices mostly analyze fixed Difficulty Vectors.

We still need tables for:

Equal pools.
Different pool sizes.
Different die sizes.
Boon differences.
Bane differences.
Equipment differences.
Defender Wins Ties.
Automatic Success totals before dice.
Equal Automatic Success totals followed by normal tiebreaking.

Examples:

text
3d8 vs 3d8
4d8 vs 3d8
5d10 vs 4d8
6d10 vs 8d10
9d12 vs 10d12
10. Decide how to handle Automatic Successes in calibration

The framework says:

Automatic Successes do not alter the Dice Pool.
They may coexist with Boons and Banes.
In opposed checks, compare Automatic Success totals before rolling.
Equal totals proceed to normal dice resolution.

We still need research tables showing:

text
0 Automatic Successes
1 Automatic Success
2 Automatic Successes

against:

text
DC X
DC X,Y
DC X,Y,Z

and opposed pools.

Recommended Completion Sequence

I recommend completing the probability work in this order:

Pass A — Update terminology and archive superseded analysis
Archive or rewrite the old DC X (Y) artifact.
Normalize all research to Difficulty Vectors.
Remove obsolete Floor references.
Pass B — Raw vector matrices
Single thresholds.
Two-threshold vectors.
Three-threshold vectors.
Expanded pool sizes.
Pass C — Boons and Banes
Added dice.
Removed dice.
One-die Step-Down.
d4 automatic failure.
Same-size Step-Ups and Step-Downs.
Pass D — Die Size versus Pool Size
Same pool, larger die.
Same die, larger pool.
Combined changes.
Equipment progression.
Pass E — Full Level 1–20 progression
Apply the provisional equipment progression.
Select Easy, Medium, and Hard vectors per Tier and level.
Generate actual probability curves.
Pass F — Opposed checks
Equal and unequal pools.
Ties.
Automatic Success totals.
Equipment and Boon/Bane differences.
Pass G — Target-band review

Only after all prior passes should we decide whether:

text
Easy: 80–85%
Medium: 60–65%
Hard: 40–45%

remain suitable.

Short Version

The existing work has established the raw mathematical foundation and shown that Difficulty Vectors produce much smoother curves.

What remains is to consolidate the system around the new model by adding:

text
Difficulty Vector matrices
Boon matrices
Bane matrices
Die Step-Up matrices
Full Level 1–20 equipment-aware tables
Opposed-roll tables
Automatic Success tables

The next most logical task is Pass A: archive or rewrite the old Required Success matrices and produce the complete Difficulty Vector matrix catalogue using the new pool-derived framework.
