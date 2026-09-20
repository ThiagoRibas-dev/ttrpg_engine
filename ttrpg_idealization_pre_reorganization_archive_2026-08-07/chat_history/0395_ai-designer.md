---
turn: 395
role: "AI-Designer"
source: chat_history.json
---

# Turn 395 — AI-Designer

Agreed. We’ll use an exact combinatorial approach rather than brute-force enumeration.

The implementation will use:

Precomputed per-die threshold probabilities.
Multinomial category counts for threshold bands.
Dynamic programming where useful for ordered vector requirements.
Exact rational probabilities where computationally practical.

The new calculation should handle:

text
DC X
DC X,Y
DC X,Y,Z
...
up to the full Dice Pool length

without treating every possible individual dice roll as a separate case.

The existing brute-force script should be replaced rather than optimized incrementally, because its basic strategy repeatedly scans enormous sorted-result spaces. The research artifact will retain the same intended output:

text
All Difficulty Vectors within:
  Easy:   80–95%
  Medium: 60–75%
  Hard:   40–55%

for:

text
3d8
4d8
6d10
8d10
9d12

and the probability plot will visualize the full set of matching vector lengths and success probabilities.
