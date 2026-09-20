# Automatic Success Probability Tables

**Status:** Phase 1 research artifact; no Automatic Success sources or limits are canonical.

## Model

An Automatic Success satisfies the highest remaining threshold in a Difficulty Vector before ordinary dice are evaluated.

```text
DC 12,11 +1 Automatic Success → DC 11
DC 12,11,9 +2 Automatic Successes → DC 9
```

The remaining vector is resolved using the ordinary Difficulty Vector procedure. If all thresholds are removed, the task succeeds automatically. In opposed contests, compare Automatic Success totals before rolling dice; equal totals proceed to normal dice resolution.

## Vector Reductions

| Original Vector | 0 Auto | 1 Auto | 2 Auto | 3 Auto |
|---|---|---|---|---|
| DC 5 | DC 5 | Automatic Success | Automatic Success | Automatic Success |
| DC 5,4 | DC 5,4 | DC 4 | Automatic Success | Automatic Success |
| DC 5,5 | DC 5,5 | DC 5 | Automatic Success | Automatic Success |
| DC 6,5,3 | DC 6,5,3 | DC 5,3 | DC 3 | Automatic Success |
| DC 9,8,7 | DC 9,8,7 | DC 8,7 | DC 7 | Automatic Success |
| DC 12,11 | DC 12,11 | DC 11 | Automatic Success | Automatic Success |

## Pool Probability Tables

Each cell is the probability of completing the remaining vector with the listed pool.

| Pool | Vector | 0 Auto | 1 Auto | 2 Auto | 3 Auto |
|---|---|---:|---:|---:|---:|
| 8d3 | DC 5 | 0.00% | 100.00% | 100.00% | 100.00% |
| 8d3 | DC 5,4 | 0.00% | 0.00% | 100.00% | 100.00% |
| 8d3 | DC 5,5 | 0.00% | 0.00% | 100.00% | 100.00% |
| 8d3 | DC 6,5,3 | 0.00% | 0.00% | 96.10% | 100.00% |
| 8d3 | DC 9,8,7 | 0.00% | 0.00% | 0.00% | 100.00% |
| 8d3 | DC 12,11 | 0.00% | 0.00% | 100.00% | 100.00% |
| 8d4 | DC 5 | 0.00% | 100.00% | 100.00% | 100.00% |
| 8d4 | DC 5,4 | 0.00% | 89.99% | 100.00% | 100.00% |
| 8d4 | DC 5,5 | 0.00% | 0.00% | 100.00% | 100.00% |
| 8d4 | DC 6,5,3 | 0.00% | 0.00% | 99.61% | 100.00% |
| 8d4 | DC 9,8,7 | 0.00% | 0.00% | 0.00% | 100.00% |
| 8d4 | DC 12,11 | 0.00% | 0.00% | 100.00% | 100.00% |
| 8d5 | DC 5 | 83.22% | 100.00% | 100.00% | 100.00% |
| 8d5 | DC 5,4 | 78.74% | 98.32% | 100.00% | 100.00% |
| 8d5 | DC 5,5 | 49.67% | 83.22% | 100.00% | 100.00% |
| 8d5 | DC 6,5,3 | 0.00% | 82.96% | 99.93% | 100.00% |
| 8d5 | DC 9,8,7 | 0.00% | 0.00% | 0.00% | 100.00% |
| 8d5 | DC 12,11 | 0.00% | 0.00% | 100.00% | 100.00% |
| 10d6 | DC 5 | 98.27% | 100.00% | 100.00% | 100.00% |
| 10d6 | DC 5,4 | 97.61% | 99.90% | 100.00% | 100.00% |
| 10d6 | DC 5,5 | 89.60% | 98.27% | 100.00% | 100.00% |
| 10d6 | DC 6,5,3 | 79.46% | 98.25% | 100.00% | 100.00% |
| 10d6 | DC 9,8,7 | 0.00% | 0.00% | 0.00% | 100.00% |
| 10d6 | DC 12,11 | 0.00% | 0.00% | 100.00% | 100.00% |
| 10d8 | DC 5 | 99.90% | 100.00% | 100.00% | 100.00% |
| 10d8 | DC 5,4 | 99.83% | 99.99% | 100.00% | 100.00% |
| 10d8 | DC 5,5 | 98.93% | 99.90% | 100.00% | 100.00% |
| 10d8 | DC 6,5,3 | 98.34% | 99.90% | 100.00% | 100.00% |
| 10d8 | DC 9,8,7 | 0.00% | 64.31% | 94.37% | 100.00% |
| 10d8 | DC 12,11 | 0.00% | 0.00% | 100.00% | 100.00% |
| 12d9 | DC 5 | 99.99% | 100.00% | 100.00% | 100.00% |
| 12d9 | DC 5,4 | 99.99% | 100.00% | 100.00% | 100.00% |
| 12d9 | DC 5,5 | 99.90% | 99.99% | 100.00% | 100.00% |
| 12d9 | DC 6,5,3 | 99.84% | 99.99% | 100.00% | 100.00% |
| 12d9 | DC 9,8,7 | 63.03% | 92.02% | 99.23% | 100.00% |
| 12d9 | DC 12,11 | 0.00% | 0.00% | 100.00% | 100.00% |
| 12d10 | DC 5 | 100.00% | 100.00% | 100.00% | 100.00% |
| 12d10 | DC 5,4 | 100.00% | 100.00% | 100.00% | 100.00% |
| 12d10 | DC 5,5 | 99.97% | 100.00% | 100.00% | 100.00% |
| 12d10 | DC 6,5,3 | 99.95% | 100.00% | 100.00% | 100.00% |
| 12d10 | DC 9,8,7 | 85.19% | 97.31% | 99.78% | 100.00% |
| 12d10 | DC 12,11 | 0.00% | 0.00% | 100.00% | 100.00% |

## Interpretation

- Automatic Successes do not add dice or change the Dice Pool.
- They remove the highest thresholds from the Difficulty Vector.
- This pass measures mathematical impact only; it does not decide which future content grants Automatic Successes.
- These results should be read alongside the Difficulty Vector matrices and the full Level 1–20 progression research.

## Related Artifacts

- `14_difficulty_vector_probability_matrices.md` — generic vector probabilities.
- `16_generic_pool_volume_probability_matrices.md` — pool-volume effects.
- `17_generic_die_size_probability_matrices.md` — die-size effects.
- `18_full_level_1_20_probability_progression.md` — provisional level progression.
- `19_opposed_probability_tables.md` — opposed checks and ties.
