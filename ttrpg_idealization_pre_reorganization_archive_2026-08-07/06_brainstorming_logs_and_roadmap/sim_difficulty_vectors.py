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
    text += '| A \ B | DC A | ' + ' | '.join(str(b) for b in values) + ' |\n'
    text += '|---:|---:|' + '---:|' * len(values) + '\n'
    for a in values:
        cells = []
        for b in values:
            cells.append(fmt(pvec(sides, pool, (a, b))) if a >= b else '—')
        single = fmt(pvec(sides, pool, (a,)))
        text += f'| {a} | {single} | ' + ' | '.join(cells) + ' |\n'
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
