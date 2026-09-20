---
turn: 319
role: "AI-Designer"
source: chat_history.json
---

# Turn 319 — AI-Designer

Yes—the current chart is scuffed, but it is exposing a real structural issue rather than merely a plotting problem.

The problem is that we are varying several discrete vectors simultaneously:

text
Die Size
Pool Size
Floor
Equipment Boons
Required Successes
Difficulty Class

Each vector is individually sensible, but their combinations create a jagged probability surface.

Why the Progression Is Not Neat
1. Dice are discrete

With a d8, the per-die thresholds are fixed:

text
DC 5 → 50% per die
DC 6 → 37.5%
DC 7 → 25%
DC 8 → 12.5%

There is no threshold between DC 5 and DC 6.

With a d10:

text
DC 7 → 40%
DC 8 → 30%
DC 9 → 20%

With a d12:

text
DC 8 → 41.67%
DC 9 → 33.33%
DC 10 → 25%

Changing die size does not simply make the character “5% better.” It changes the entire probability grid.

2. Pool size is also discrete

Changing:

text
3d8 → 4d8

does not shift the curve smoothly. It changes the probability of at least one success and the probability of multiple successes in a nonlinear way.

Equipment causes exactly these jumps:

text
2d8 → 3d8
3d8 → 4d8
5d10 → 8d10

The last example is especially large.

3. Required Successes create another grid

DC X (1) and DC X (2) are not small adjustments to one another.

For example, with 4d8:

text
DC 6 (1) → roughly 84.7%
DC 7 (1) → roughly 68.4%
DC 6 (2) → roughly 48.1%

So changing Required Successes can move the probability much more dramatically than changing the DC by one point.

4. The target bands are very close together

The current targets are:

text
Easy:   85%
Medium: 65%
Hard:   55%

The gaps are only:

text
Easy → Medium: 20 percentage points
Medium → Hard: 10 percentage points

But our available probability steps are often larger than 10 percentage points.

That means many levels simply cannot produce all three target bands with distinct DC X (R) combinations within ±2%.

The Bigger Design Issue

We are currently asking one framework to do two different jobs:

Die Size

Represents:

text
What numerical thresholds can this character reach?
Pool Size

Represents:

text
How reliable is this character?
How many successes can they produce?
How high is their Floor?

That is a good conceptual separation, but it creates a two-dimensional advancement lattice rather than a smooth one-dimensional progression.

PF2e avoids much of this by having one d20 and letting the modifier scale continuously. We have a bounded die ladder and discrete pool jumps, so our probability surface will inherently be chunkier.

The Chart May Be Asking the Wrong Question

Instead of asking:

What DC gives this exact character an 85%, 65%, or 55% chance at every level?

we may need to ask:

What probability bands should this character occupy at each Tier and role?

For example:

text
Trained specialist:
  Easy: 80–95%
  Medium: 50–75%
  Hard: 25–55%

Veteran specialist:
  Easy: 85–100%
  Medium: 60–85%
  Hard: 35–65%

Master specialist:
  Easy: 90–100%
  Medium: 65–90%
  Hard: 45–75%

This respects the discrete nature of the engine instead of forcing exact percentages that the dice cannot provide.

Better Calibration Approach

I recommend changing the workflow.

Step 1: Define probability bands, not exact targets

Instead of:

text
Easy = exactly 85%
Medium = exactly 65%
Hard = exactly 55%

define acceptable bands:

text
Easy:
  80–95%

Medium:
  55–75%

Hard:
  40–65%

The bands should overlap somewhat because the system is intentionally discrete.

Step 2: Calibrate by Tier, not every level

Do not demand a new DC progression at every Character Level.

Use anchor levels:

text
Level 1
Level 5
Level 9
Level 13
Level 17

These correspond to the five High Fantasy Tiers.

Levels within a Tier should improve:

Pool reliability.
Required Success capacity.
Equipment.
Spell access.
Tactical permissions.

But they do not necessarily need new baseline DCs every level.

Step 3: Use DC X (R) for granularity

The flat DC is the coarse axis.

Required Successes provide the second axis.

For example:

text
DC 6 (1)
DC 6 (2)
DC 7 (1)
DC 7 (2)

These should be treated as different challenge profiles, not as attempts to hit perfectly spaced percentages.

Step 4: Separate “difficulty” from “success chance”

A DC should describe the fictional difficulty of the task.

The resulting probability depends on:

Character capability.
Equipment.
Conditions.
Required Successes.
Opposition.

We should not redefine the fiction of a task merely because one character’s probability is inconvenient.

Equipment Is Creating Very Large Jumps

The assumed equipment progression is:

Tier	Baseline Pool	Equipment Boons	Final Pool
Trained	2d8	+1B	3d8
Veteran	3d8	+1B to +2B	4d8–5d8
Master	4d10	+2B	6d10
Hero	5d10	+3B	8d10
Legend	6d12	+3B to +4B	9d12–10d12

That is not a minor equipment effect. It is a major progression vector.

For example:

text
5d10 → 8d10

creates a substantial increase in:

At-least-one success probability.
Multiple-success probability.
Floor.
Resistance to Banes.
Likelihood of extreme results.

This may be completely appropriate, but it means equipment cannot be treated as a small adjustment. It is effectively a second advancement track.

Possible Design Directions
Option A: Accept chunky probability

Keep the current architecture and accept that probability bands will be uneven.

Use:

Tier-based benchmarks.
Probability ranges.
DC X (R) for intermediate difficulty.
Fiction-first DC assignment.
Equipment as a major progression vector.

This preserves the current high-option-density model.

Option B: Reduce equipment pool impact

Equipment could grant:

A Boon of a typed category.
A Die Step-Up in specific situations.
A Permission.
A Trait.
Damage or defense effects.

Instead of routinely adding three or four dice to the pool.

This would make character progression smoother but reduce equipment’s direct reliability impact.

Option C: Let equipment affect only certain vectors

For example:

Weapons improve Damage Dice and Traits.
Armor improves Damage Absorption and Durability.
Magic items grant Permissions.
Only rare items grant Boons to general checks.

This prevents every equipment upgrade from simultaneously improving:

text
Pool volume
Floor
Multiple successes
High-threshold reliability
Option D: Use different target bands

Maybe the current targets are simply too tightly clustered.

For example:

text
Easy:   85%
Medium: 60%
Hard:   35%

This gives the system more room to express meaningful difficulty differences.

The current 65% and 55% targets are close enough that the discrete probability grid often cannot separate them.

My Recommendation

I recommend not changing the dice architecture yet.

Instead:

Replace exact probability targets with Tier-based probability bands.
Plot representative profiles at Levels 1, 5, 9, 13, and 17.
Separate unmodified, normally equipped, and heavily enhanced profiles.
Use DC X (R) combinations to fill meaningful gaps.
Reconsider whether equipment should routinely add multiple dice.
Use probability calibration to identify problem cases rather than forcing every level into an exact DC ladder.

The current result does not necessarily show that Die Size and Pool Size are a mistake. It shows that they create a discrete two-axis probability system, which needs to be calibrated in bands and archetypal snapshots rather than exact level-by-level target percentages.
