---
turn: 363
role: "AI-Designer"
source: chat_history.json
---

# Turn 363 — AI-Designer

Yes. The next probability-calibration step is:

Pass D — Full Level 1–20 Progression

This pass will apply the current provisional progression across every character level rather than only using Tier-entry snapshots.

Inputs

For each level, record:

Character Level.
High Fantasy Tier.
Competency Rank.
Attribute Die Size.
Baseline Dice Pool.
Provisional Equipment Boons.
Final Dice Pool.
Easy Difficulty Vector.
Medium Difficulty Vector.
Hard Difficulty Vector.
Actual probability of each vector.
Current provisional progression
text
Levels 1–4:
  Trained
  d8 Attribute
  2d8 baseline
  +1 equipment die
  3d8 final

Levels 5–8:
  Veteran
  d8 Attribute
  3d8 baseline
  +1 equipment die
  4d8 final

Levels 9–12:
  Master
  d10 Attribute
  4d10 baseline
  +2 equipment dice
  6d10 final

Levels 13–16:
  Hero
  d10 Attribute
  5d10 baseline
  +3 equipment dice
  8d10 final

Levels 17–20:
  Legend
  d12 Attribute
  6d12 baseline
  +3 equipment dice
  9d12 final
Current provisional Difficulty Vectors

From the previous calibration:

Tier	Easy	Medium	Hard
Trained	DC 5	DC 5,4	DC 5,5
Veteran	DC 6	DC 6,5	DC 6,6
Master	DC 8	DC 9,7	DC 10
Hero	DC 9	DC 9,8	DC 9,9
Legend	DC 11	DC 11,10	DC 12

Pass D should apply those vectors across all twenty levels and report:

text
P(Easy)
P(Medium)
P(Hard)

Since the provisional progression is constant within each Tier, several consecutive levels will have identical mathematical probabilities unless we introduce additional level-by-level changes. That is useful information rather than a problem.

Deliverables

I recommend producing:

text
02_comparative_system_analysis/18_full_level_1_20_probability_progression.md
02_comparative_system_analysis/18_full_level_1_20_probability_progression.png
06_brainstorming_logs_and_roadmap/sim_full_level_probability_progression.py

The chart should plot:

Level 1–20 on the X-axis.
Easy, Medium, and Hard probabilities on the Y-axis.
Target-band shading.
Tier boundaries.
The provisional equipment assumptions.

After Pass D, the next step would be:

text
Pass E — Opposed probability tables

which would test the same progression against equal-tier and cross-tier opposition.
