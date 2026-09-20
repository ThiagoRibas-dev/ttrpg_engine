---
turn: 295
role: "AI-Designer"
source: chat_history.json
---

# Turn 295 — AI-Designer

used
Bash
77ms
Explored
1 read
Read
07_check_pool_generation_and_class_differentiation.md

The canonical decision is Model A: Floors are tied directly to Competency Rank, not to the number of dice in the pool.

Primary canonical definitions
03_core_baseline_system/01_resolution_engine.md

The current Competency table is:

Competency Rank	Pool Volume	Die Step-Up	Floor
Untrained	2 dice	—	0
Trained	3 dice	—	3
Expert	3 dice	1	5
Master	4 dice	2	7
Legendary	5 dice	3	9

This is the most direct procedural definition.

03_core_baseline_system/07_check_pool_generation_and_class_differentiation.md

This file explicitly separates the three mathematical variables:

text
Die Size (X)
Pool Volume (N)
Competency Floor (F)

It states that:

Attribute determines Die Size.
Competency determines Pool Volume and Floor.
Class, Feats, Equipment, Tactics, and Resources provide other effects.
Decision log

The definitive architectural decision is:

text
DEC-038 — Official Check Engine Lock-In

It states:

Attribute sets Die Size (X); Competency sets Pool Volume (N) and Floor (F); Class sets Feats.

The original Floor decision is recorded in:

text
DEC-019 — Hybrid Competency Floors

with the progression:

text
Untrained 0
Trained 3
Expert 5
Master 7
Legendary 9
The rejected alternative

The alternative where the Floor is derived from the number of dice in the pool was not adopted.

The number of dice and the Floor are separate variables:

text
3d8, Floor 3
3d8, Floor 5
4d8, Floor 7
5d8, Floor 9

A pool may have the same volume while differing in Floor because the actor has different Competency Rank or another explicit effect.

Later modifications to the base Floor

Two later decisions modify the final Floor without changing the original source of the Floor:

Banes

A Bane can lower the effective Floor when it reduces the final pool state.

The Floor remains a Competency-based mechanic, but the final effective Floor may be reduced by the degraded pool state.

Die-size cap

The final Floor cannot exceed one less than the final die size.

Examples:

text
3d4:
  Maximum final Floor 3

5d6:
  Maximum final Floor 5

7d8:
  Maximum final Floor 7

10d12:
  Maximum final Floor 11

This is a cap on the final Floor, not a replacement for the Competency-based Floor system.

Final model
text
Competency Rank:
  Determines the base Floor.

Pool Volume:
  Determines how many dice are rolled.

Die Size:
  Determines the numerical ceiling.

Banes:
  Can reduce the final pool and therefore the effective Floor.

Final Die Size:
  Caps the maximum possible Floor at die size − 1.

So the answer is:

The Floor is fundamentally tied to Competency Rank. Pool volume does not generate the Floor, although final pool degradation and the final die-size cap can modify or constrain the effective Floor.
