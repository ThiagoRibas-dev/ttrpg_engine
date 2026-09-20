---
turn: 389
role: "AI-Designer"
source: chat_history.json
---

# Turn 389 — AI-Designer

Yes. Option A uses arithmetic internally to calculate the probabilities—but only as design-time research mathematics, not as a player-facing game mechanic.

That is fully compatible with our system principles.

The distinction is:

text
Design phase:
  Use exact arithmetic, combinatorics, dynamic programming, and simulations.

At the table:
  Roll dice and compare faces.
  Do not add or subtract modifiers.

The script would calculate probabilities using:

Fractions.
Binomial or multinomial relationships.
Dynamic programming.
Exact counts of successful outcomes.

None of that becomes part of the game procedure.

For example, the game rule is still simply:

text
Roll 9d12.
Sort the dice.
Compare them against DC 11,10,8.

The script may calculate that this succeeds 43.92% of the time, but players never perform that calculation.

Option C, Monte Carlo simulation, also uses arithmetic internally; it merely estimates rather than calculates exact probabilities.

So:

Option A: Exact, deterministic, slower unless optimized.
Option B: Exact precomputed distributions, efficient.
Option C: Approximate simulation, simpler to implement but less precise.

For this artifact, I recommend an optimized exact method because we are specifically trying to identify every valid Difficulty Vector within narrow probability bands. Approximation could incorrectly include or exclude vectors near the band boundaries.
