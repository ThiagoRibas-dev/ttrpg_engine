---
turn: 315
role: "AI-Designer"
source: chat_history.json
---

# Turn 315 — AI-Designer

Ran commands
2

Created and ran the multi-success probability analysis.

Script
text
06_brainstorming_logs_and_roadmap/sim_multi_success_probabilities.py
Research artifact
text
02_comparative_system_analysis/12_multi_success_probability_matrices.md

The artifact calculates:

text
P(at least R successes in NdS against threshold T)

using:

text
p = (S − T + 1) / S

P(at least R successes)
= Σ[k=R..N] C(N,k) p^k (1−p)^(N−k)

It includes matrices for:

d4 pools.
d6 pools.
d8 pools.
d10 pools.
d12 pools.

The matrices cover pool sizes from 1dS through SdS, with every possible Required Success count from 1 through the pool size.

I interpreted “keep highest N” as the existing DC X (Y) Required Success system rather than a dice-discarding mechanic:

Every die meeting the Target Number counts as a success; the check requires Y successful dice.

Equipment-aware calibration

The artifact also searches the supplied fully equipped progression for combinations near:

text
Easy:   85%
Medium: 65%
Hard:   55%

using:

text
DC X (R)

and the revised Floor model:

text
Floor = min(final pool size, die size − 1)

This confirms the value of Required Successes: many probability gaps that could not be filled by a flat DC can be approached through combinations such as:

text
DC 7 (2)
DC 8 (2)
DC 10 (1)
DC 10 (2)

The research artifact remains non-canonical. No DC target bands or Required Success standards were locked.
