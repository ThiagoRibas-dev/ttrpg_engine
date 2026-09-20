---
turn: 369
role: "AI-Designer"
source: chat_history.json
---

# Turn 369 — AI-Designer

Yes. The next step is Pass F — Automatic Success Reduction.

This pass should be much simpler than the earlier version because Automatic Successes do not create another probability engine. They simply remove the highest thresholds from a Difficulty Vector before the dice are evaluated.

Pass F Model
text
DC 12,11
+1 Automatic Success
→ DC 11
text
DC 12,11,9
+1 Automatic Success
→ DC 11,9
text
DC 12,11,9
+2 Automatic Successes
→ DC 9

The remaining vector is then evaluated using the ordinary Dice Pool and Difficulty Vector probability tables.

Pass F Should Measure
1. Fixed Difficulty Vectors

For vectors such as:

text
DC 5
DC 5,4
DC 5,5
DC 6,5,3
DC 9,8,7
DC 12,11

calculate probabilities with:

text
0 Automatic Successes
1 Automatic Success
2 Automatic Successes
3 Automatic Successes

where the vector is shortened from the highest threshold first.

2. Pool-Size Progression

Apply Automatic Success reductions to representative pools:

text
3d8
4d8
5d8
6d10
8d10
9d12
10d12

This will show whether Automatic Successes:

Smooth out probability curves.
Make difficulty vectors too easy.
Create meaningful Legendary/Mythic progression.
Replace the need for larger Dice Pools.
Allow lower-tier characters to overcome higher thresholds too easily.
3. Fully Equipped Level Progression

Apply the current provisional Tier vectors to the full Level 1–20 progression.

For each level, measure:

text
0 Automatic Successes
1 Automatic Success
2 Automatic Successes

This should show what happens if future:

Classes.
Feats.
Equipment.
Spells.
Mythic features.

grant Automatic Successes.

4. Opposed Automatic Successes

The opposed rule is already:

Compare Automatic Success totals.
The side with more wins before dice are rolled.
If totals are equal, roll dice normally.
Resolve secondary dice tiebreaking.
Defender wins any remaining tie.

Pass F should measure this separately rather than combining Automatic Successes with ordinary Difficulty Vector probability.

Expected Research Artifact

I recommend creating:

text
02_comparative_system_analysis/20_automatic_success_probability_tables.md
02_comparative_system_analysis/20_automatic_success_probability.png
06_brainstorming_logs_and_roadmap/sim_automatic_success_probabilities.py

The artifact should record:

Original vector.
Automatic Success count.
Remaining vector.
Dice Pool.
Probability.
Whether the effect automatically resolves the task.

Example:

Pool	Original Vector	Auto Successes	Remaining Vector	Probability
6d12	DC 12,11	0	DC 12,11	45.93%
6d12	DC 12,11	1	DC 11	66.51%
6d12	DC 12,11	2	—	100%

The final row succeeds automatically because the entire vector has been satisfied before rolling.

Important Boundary

Pass F should not decide:

Which Classes grant Automatic Successes.
Which Feats grant them.
How many Mythic Automatic Successes exist.
Whether equipment grants them.
Whether Automatic Successes can be removed.
Whether specific spells provide them.

Those are future content decisions.

Pass F should only measure:

What mathematical effect does removing one or more difficulty-vector thresholds have?

This keeps the pass analytical rather than turning it into a content-design phase.
