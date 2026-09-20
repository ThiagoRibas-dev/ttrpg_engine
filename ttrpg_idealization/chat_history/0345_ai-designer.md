---
turn: 345
role: "AI-Designer"
source: chat_history.json
---

# Turn 345 — AI-Designer

Yes, those revisions make the probability work cleaner.

Revised Interpretation
1. Deprecate the old multi-success artifact

The previous document:

text
12_multi_success_probability_matrices.md

is superseded by the Difficulty Vector model.

It should be archived as historical research rather than rebuilt.

The active probability authority becomes:

text
14_difficulty_vector_probability_matrices.md

The old artifact should be labeled as:

text
Pre-Difficulty-Vector / Deprecated Required-Success Research
2. Generic Dice-Pool Reference Matrices

Agreed. We should not create separate probability systems called:

text
Boon matrices
Bane matrices
Equipment matrices

Those effects only change the final Dice Pool, except for the special Bane-induced Die Step-Down.

The generic research tables should therefore cover:

text
1dX
2dX
3dX
4dX
5dX
6dX
...
expanded NdX pools

The same reference matrix can be applied to:

Competency.
Equipment.
Boons.
Banes that remove dice.
Class features.
Feats.
Spells.
Circumstances.
Any other effect that changes pool volume.

The source of the dice does not matter to the raw probability.

3. Generic Die-Size Reference Matrices

Likewise, Die Step-Up should not receive a separate probability model.

We should compare generic pools across die sizes:

text
Nd4
Nd6
Nd8
Nd10
Nd12

For example:

text
3d8 vs 3d10
4d8 vs 4d10
5d10 vs 5d12
6d10 vs 6d12

The same matrices can be used for:

Attribute advancement.
Equipment effects.
Spell effects.
Feats.
Stamina-driven Die Step-Up.
Essence-driven Die Step-Up.
Conditions imposing Die Step-Down.

The only special case is:

text
Bane on a one-die pool:
  One Die Step-Down.

That remains a specific Bane procedure, but its probability can be read from the generic Die-Size matrices.

4. Floor References

You are right: explicit Floors were removed from the current framework.

Any remaining Floor references in active research artifacts should be treated as stale and removed or marked as superseded.

The research model should now be:

text
Attribute:
  Die Size.

Competency:
  Baseline Dice Pool Size.

Equipment, Boons, Banes, Feats, Spells:
  Final Dice Pool Size or Die Size.

Difficulty Vector:
  Thresholds applied to the final rolled pool.

There should be no Floor-adjusted probability pass in the current model.

5. Automatic Successes and Difficulty Vectors

Yes. An Automatic Success removes one threshold from the Difficulty Vector.

Suppose:

text
Difficulty:
  DC 12,11

With one Automatic Success:

text
Remaining difficulty:
  DC 11

So the probability is equivalent to:

text
P(at least one die in the pool ≥ 11)

It is not equivalent to the probability of DC 12, because the Automatic Success has already satisfied the highest threshold.

Examples
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

The Automatic Successes should cancel the highest remaining thresholds first because that gives the cleanest interpretation.

Opposed contests

For opposed checks:

text
Attacker:
  1 Automatic Success
  6d12

Defender:
  0 Automatic Successes
  4d12

The attacker wins before dice are rolled.

If both sides have the same number of Automatic Successes, those successes cancel for the purpose of deciding the contest, and the remaining dice are resolved normally.

6. Equipment Progression

Agreed. The current equipment progression should remain a provisional research profile.

We should not redesign it during this probability phase.

The current table remains useful because it gives us a consistent benchmark for plotting:

text
Baseline Pool + Provisional Equipment Dice

When we reach the equipment framework task, we can revisit:

Whether equipment really grants that many dice.
Whether different slots contribute independently.
Whether equipment should instead grant Traits, Permissions, Damage effects, or special protections.
Whether the provisional progression is too generous.
Revised Probability Workstream

The updated sequence should be:

Pass A — Archive obsolete Required-Success research
Archive 12_multi_success_probability_matrices.md.
Mark it as superseded by Difficulty Vectors.
Remove active Floor assumptions from related research.
Pass B — Generic pool-volume matrices

Calculate:

text
1dX through expanded NdX

for standard die sizes and Difficulty Vectors.

These tables apply equally to:

Competency.
Equipment.
Boons.
Banes.
Feats.
Spells.
Circumstance.
Pass C — Generic die-size matrices

Compare the same pool volume across:

text
d4, d6, d8, d10, d12

for single and multi-threshold Difficulty Vectors.

Pass D — Full Level 1–20 progression

Use the current provisional equipment profile:

text
Level
Tier
Competency Rank
Attribute Die Size
Baseline Pool
Equipment Dice
Final Pool
Easy Vector
Medium Vector
Hard Vector
Actual probabilities
Pass E — Opposed probability tables

Calculate:

Equal pools.
Different pool sizes.
Different die sizes.
Boon/Bane-driven pool changes.
Automatic Success comparisons.
Defender Wins Ties.
Secondary dice tiebreaks.
Pass F — Automatic Success reductions

Treat Automatic Successes as vector-threshold removal:

text
DC A,B,C
− 1 Automatic Success
→ DC B,C
Pass G — Target-band review

Review whether the current provisional bands remain useful:

text
Easy:   80–85%
Medium: 60–65%
Hard:   40–45%

No new probability framework is needed for Boons, Banes, Equipment, or Die Step-Ups. They all use the same generic pool and die-size tables.
