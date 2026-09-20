# Opposed Probability by Tier Profile

**Status:** Phase 1 research artifact; no opposed probability target is canonical.

## Profiles

These profiles use the current provisional fully equipped Dice Pools:

| Tier | Die Size | Final Pool |
|---|---:|---:|
| Trained | d8 | 3d8 |
| Veteran | d8 | 4d8 |
| Master | d10 | 6d10 |
| Hero | d10 | 8d10 |
| Legend | d12 | 9d12 |

## Procedure

- Sort each final Dice Pool from highest to lowest.
- Compare the highest results.
- Continue through lower results if tied.
- Defender wins complete ties.
- No Floors, Boons, Banes, Automatic Successes, or special Class/Equipment Permissions are applied.

The tables use exact multinomial distributions of sorted dice, not Monte Carlo sampling.

## Attacker Win Probability

Rows are Attacker Tier; columns are Defender Tier.

| Attacker \\ Defender | Trained | Veteran | Master | Hero | Legend |
|---|---:|---:|---:|---:|---:|
| Trained | 49.52% | 39.53% | 6.96% | 3.14% | 0.41% |
| Veteran | 60.47% | 49.80% | 9.17% | 4.25% | 0.57% |
| Master | 93.04% | 90.83% | 49.98% | 39.29% | 6.77% |
| Hero | 96.86% | 95.75% | 60.71% | 50.00% | 8.78% |
| Legend | 99.59% | 99.43% | 93.23% | 91.22% | 50.00% |

## Raw Tie Probability

| Attacker \\ Defender | Trained | Veteran | Master | Hero | Legend |
|---|---:|---:|---:|---:|---:|
| Trained | 0.96% | 0.40% | 0.01% | 0.00% | 0.00% |
| Veteran | 0.81% | 0.40% | 0.02% | 0.00% | 0.00% |
| Master | 0.18% | 0.07% | 0.03% | 0.01% | 0.00% |
| Hero | 0.10% | 0.04% | 0.02% | 0.01% | 0.00% |
| Legend | 0.01% | 0.01% | 0.00% | 0.00% | 0.00% |

## Interpretation

- Because the defender wins ties, mirror matchups produce attacker win rates below 50%.
- Higher Dice Pool and Die Size progression creates a strong diagonal advantage across Tiers.
- This artifact isolates the raw opposed-roll engine. Future passes may add equipment variation, Boons, Banes, Automatic Successes, defenses, and Class/Feat Permissions.
