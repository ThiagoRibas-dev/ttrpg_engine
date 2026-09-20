---
turn: 327
role: "AI-Designer"
source: chat_history.json
---

# Turn 327 — AI-Designer

Ran commands
3
Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/sim_difficulty_vectors.py
98 lines
open
used
Bash
timeout 30s
Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/sim_difficulty_vectors.py
106 lines
open
sim_difficulty_vectors.py
PYTHON
from itertools import combinations_with_replacement
from pathlib import Path
from collections import defaultdict

OUT = Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/14_difficulty_vector_probability_matrices.md')

def distribution(sides, pool, keep=3):
    states = {(): 1}
    for _ in range(pool):
        nxt = defaultdict(int)
        for state, count in states.items():
            for face in range(1, sides + 1):
                values = tuple(sorted(state + (face,), reverse=True)[:keep])
                nxt[values] += count
        states = nxt
    return states

def pvec(sides, pool, vector):
    req = tuple(sorted(vector, reverse=True))
    dist = distribution(sides, pool, len(req))
    total = sides ** pool
    hits = sum(count for values, count in dist.items() if all(values[i] >= req[i] for i in range(len(req))))
    return hits / total

def fmt(p):
    return f'{p * 100:.2f}%'

profiles = [
    (1, 'Trained', 8, 3), (5, 'Veteran', 8, 4),
    (7, 'Veteran', 8, 5), (9, 'Master', 10, 6),
    (13, 'Hero', 10, 8), (17, 'Legend', 12, 9),
    (19, 'Legend', 12, 10),
]
bands = {'Easy': (.80, .85), 'Medium': (.60, .65), 'Hard': (.40, .45)}

text = """# Difficulty-Vector Probability Matrices

**Status:** Phase 1 research artifact; no vector bands or DC assignments are canonical.

## Model

A difficulty vector is written with comma-separated thresholds:

```text
DC 5,4
```

Roll the final pool, sort dice from highest to lowest, sort the vector thresholds from highest to lowest, and compare positionally. Extra dice beyond the vector length are ignored for that vector. `DC 5` is a one-threshold vector. There is no `DC X (Y)` notation in this model.

The probability calculated is:

```text
P(die[0] ≥ threshold[0], die[1] ≥ threshold[1], ...)
```

## Pair Matrices

Each matrix gives the probability for every two-threshold vector `DC A,B`, with `A ≥ B`.

"""

for sides, pool in [(8, 3), (8, 4), (8, 5), (10, 6), (10, 8), (12, 9), (12, 10)]:
    text += f'### {pool}d{sides}\n\n'
    values = list(range(2, sides + 1))
    text += '| A \\ B | ' + ' | '.join(str(b) for b in values) + ' |\n'
    text += '|---:|' + '---:|' * len(values) + '\n'
    for a in values:
        cells = []
        for b in values:
            cells.append(fmt(pvec(sides, pool, (a, b))) if a >= b else '—')
        text += f'| {a} | ' + ' | '.join(cells) + ' |\n'
    text += '\n'

text += """## Per-Tier Target-Band Calibration

This table searches vectors of length one through three for representative fully equipped progression profiles. Target bands are Easy 80–85%, Medium 60–65%, and Hard 40–45%. It prefers vectors inside the band and otherwise reports the closest vector.

| Level | Tier | Pool | Easy | Medium | Hard |
|---:|---|---:|---|---|---|
"""

for level, tier, sides, pool in profiles:
    cells = []
    for name, (low, high) in bands.items():
        options = []
        for length in range(1, min(3, pool) + 1):
            for vector in combinations_with_replacement(range(2, sides + 1), length):
                vector = tuple(sorted(vector, reverse=True))
                probability = pvec(sides, pool, vector)
                inside = low <= probability <= high
                distance = 0 if inside else min(abs(probability - low), abs(probability - high))
                options.append((0 if inside else 1, distance, abs(probability - (low + high) / 2), vector, probability, inside))
        _, _, _, vector, probability, inside = min(options)
        cells.append(f'DC {",".join(map(str, vector))} → {fmt(probability)}' + (' ✓' if inside else ' (nearest)'))
    text += f'| {level} | {tier} | {pool}d{sides} | ' + ' | '.join(cells) + ' |\n'

text += """
## Notes

- A vector is not the same as “keep highest R”; it is a set of ordered thresholds applied to the highest rolled dice.
- This artifact does not yet apply Floors, Boons, Banes, Automatic Successes, or opposed contests.
- The calibration table uses representative fully equipped pools only as a research profile.
"""
OUT.write_text(text)
print(OUT)

Open
used
Bash
43s

Created and ran the difficulty-vector probability artifact:

text
02_comparative_system_analysis/14_difficulty_vector_probability_matrices.md

The supporting script is:

text
06_brainstorming_logs_and_roadmap/sim_difficulty_vectors.py
Included matrices

Matrices were generated for:

text
3d8
4d8
5d8
6d10
8d10
9d12
10d12

Each matrix contains the probability for every two-threshold vector:

text
DC A,B

with A ≥ B.

The procedure is:

Roll the pool.
Sort the dice from highest to lowest.
Sort the thresholds from highest to lowest.
Compare them positionally.
Ignore extra dice beyond the vector length.
Per-tier calibration

The artifact also searches difficulty vectors of one to three thresholds against the current fully equipped progression and the target bands:

text
Easy:   80–85%
Medium: 60–65%
Hard:   40–45%

The results are much smoother than the earlier DC X (R) model.

Examples:

text
Level 5 — 4d8
Easy:   DC 6,3   → 82.40%
Medium: DC 7,4   → 63.09%
Hard:   DC 7,6,2 → 42.77%
text
Level 13 — 8d10
Easy:   DC 9,5,4 → 82.55%
Medium: DC 8,8,7 → 62.71%
Hard:   DC 9,8,8 → 43.69%
text
Level 19 — 10d12
Easy:   DC 11,8,5 → 82.47%
Medium: DC 11,10,9 → 61.58%
Hard:   DC 12,11 → 41.96%

The full calibration table currently finds in-band vectors for the representative profiles tested. The artifact remains research-only and does not yet apply Floors, Boons, Banes, Automatic Successes, or opposed contests.
