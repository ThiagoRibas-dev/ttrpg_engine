# Level 1 Penetration 1 and Power Attack Model

**Status:** Research artifact; non-canonical.  
**Purpose:** Compare a Level 1 Power Attacker against a non-Power-Attacking equal-level opponent when all tested weapons have Penetration 1. This artifact selects no Penetration, weapon, armor, or Power Attack rule.

## Assumptions

```text
Penetration 1 in this model:
  A successful Attack deals at least 1 Damage Box after
  Damage Absorption.

It does not reduce Armor Absorption by 1.
It sets a minimum post-absorption damage floor of 1.

Power Attack:
  Level 1 X maximum = 1.
  The Power Attacker uses X=1 whenever it has Stamina.
  The opponent never uses Power Attack.
```

Other Level 1 profile, defense, and resource assumptions match `31_level_1_power_attack_model.md`.

## Static Penetration Result

| Fixed Damage Boxes | Absorption 0 | Absorption 2 | Absorption 3 | Absorption 4 |
|---:|---:|---:|---:|---:|
| 2 | 2 | 1 | 1 | 1 |
| 4 | 4 | 2 | 1 | 1 |
| 6 | 6 | 4 | 3 | 2 |

## Duel Simulation

| Attack profile | Policy | Defense matchup | Base Damage | Absorption | Mean attacks to 0 | Power Attacker down | Normal Attacker down | Mean Power Attacks used |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Strict base | Deflect-first | Deflect vs Deflect | 2 | 0 | 7.55 | 83.90% | 16.10% | 2.48 |
| Strict base | Deflect-first | Deflect vs Deflect | 2 | 2 | 13.93 | 91.10% | 8.90% | 2.48 |
| Strict base | Deflect-first | Deflect vs Deflect | 2 | 3 | 13.93 | 90.50% | 9.50% | 2.50 |
| Strict base | Deflect-first | Deflect vs Deflect | 2 | 4 | 13.92 | 91.80% | 8.20% | 2.52 |
| Strict base | Deflect-first | Deflect vs Deflect | 4 | 0 | 5.55 | 79.20% | 20.80% | 2.22 |
| Strict base | Deflect-first | Deflect vs Deflect | 4 | 2 | 7.44 | 80.80% | 19.20% | 2.46 |
| Strict base | Deflect-first | Deflect vs Deflect | 4 | 3 | 13.43 | 73.80% | 26.20% | 2.49 |
| Strict base | Deflect-first | Deflect vs Deflect | 4 | 4 | 13.93 | 91.40% | 8.60% | 2.51 |
| Strict base | Deflect-first | Deflect vs Deflect | 6 | 0 | 2.48 | 66.60% | 33.40% | 1.14 |
| Strict base | Deflect-first | Deflect vs Deflect | 6 | 2 | 5.56 | 81.30% | 18.70% | 2.26 |
| Strict base | Deflect-first | Deflect vs Deflect | 6 | 3 | 5.59 | 80.90% | 19.10% | 2.28 |
| Strict base | Deflect-first | Deflect vs Deflect | 6 | 4 | 7.52 | 83.80% | 16.20% | 2.44 |
| Strict base | Deflect-first | Evasion vs Evasion | 2 | 0 | 6.46 | 56.00% | 44.00% | 2.77 |
| Strict base | Deflect-first | Evasion vs Evasion | 2 | 2 | 11.39 | 90.10% | 9.90% | 3.00 |
| Strict base | Deflect-first | Evasion vs Evasion | 2 | 3 | 11.34 | 89.30% | 10.70% | 3.00 |
| Strict base | Deflect-first | Evasion vs Evasion | 2 | 4 | 11.42 | 90.90% | 9.10% | 3.00 |
| Strict base | Deflect-first | Evasion vs Evasion | 4 | 0 | 3.42 | 43.80% | 56.20% | 1.69 |
| Strict base | Deflect-first | Evasion vs Evasion | 4 | 2 | 6.42 | 59.70% | 40.30% | 2.74 |
| Strict base | Deflect-first | Evasion vs Evasion | 4 | 3 | 10.19 | 65.60% | 34.40% | 3.00 |
| Strict base | Deflect-first | Evasion vs Evasion | 4 | 4 | 11.31 | 91.00% | 9.00% | 3.00 |
| Strict base | Deflect-first | Evasion vs Evasion | 6 | 0 | 1.91 | 72.90% | 27.10% | 0.83 |
| Strict base | Deflect-first | Evasion vs Evasion | 6 | 2 | 3.34 | 40.00% | 60.00% | 1.67 |
| Strict base | Deflect-first | Evasion vs Evasion | 6 | 3 | 4.74 | 78.50% | 21.50% | 2.11 |
| Strict base | Deflect-first | Evasion vs Evasion | 6 | 4 | 6.42 | 57.30% | 42.70% | 2.75 |
| Strict base | Deflect-first | Deflect vs Evasion | 2 | 0 | 6.74 | 52.60% | 47.40% | 2.45 |
| Strict base | Deflect-first | Deflect vs Evasion | 2 | 2 | 13.39 | 63.30% | 36.70% | 2.53 |
| Strict base | Deflect-first | Deflect vs Evasion | 2 | 3 | 13.28 | 61.50% | 38.50% | 2.48 |
| Strict base | Deflect-first | Deflect vs Evasion | 2 | 4 | 13.29 | 65.40% | 34.60% | 2.50 |
| Strict base | Deflect-first | Deflect vs Evasion | 4 | 0 | 3.82 | 40.60% | 59.40% | 1.75 |
| Strict base | Deflect-first | Deflect vs Evasion | 4 | 2 | 6.64 | 50.70% | 49.30% | 2.44 |
| Strict base | Deflect-first | Deflect vs Evasion | 4 | 3 | 11.94 | 43.40% | 56.60% | 2.50 |
| Strict base | Deflect-first | Deflect vs Evasion | 4 | 4 | 13.37 | 63.40% | 36.60% | 2.49 |
| Strict base | Deflect-first | Deflect vs Evasion | 6 | 0 | 2.30 | 60.50% | 39.50% | 1.07 |
| Strict base | Deflect-first | Deflect vs Evasion | 6 | 2 | 3.74 | 37.10% | 62.90% | 1.75 |
| Strict base | Deflect-first | Deflect vs Evasion | 6 | 3 | 5.32 | 70.40% | 29.60% | 2.22 |
| Strict base | Deflect-first | Deflect vs Evasion | 6 | 4 | 6.70 | 50.40% | 49.60% | 2.43 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 2 | 0 | 8.87 | 86.70% | 13.30% | 2.02 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 2 | 2 | 13.95 | 90.90% | 9.10% | 2.52 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 2 | 3 | 13.94 | 90.50% | 9.50% | 2.49 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 2 | 4 | 14.00 | 91.50% | 8.50% | 2.48 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 4 | 0 | 5.45 | 69.40% | 30.60% | 1.51 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 4 | 2 | 8.90 | 85.00% | 15.00% | 2.03 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 4 | 3 | 13.70 | 86.00% | 14.00% | 2.49 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 4 | 4 | 13.89 | 91.90% | 8.10% | 2.52 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 6 | 0 | 4.17 | 73.10% | 26.90% | 1.22 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 6 | 2 | 5.53 | 71.90% | 28.10% | 1.48 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 6 | 3 | 6.60 | 79.40% | 20.60% | 1.77 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 6 | 4 | 8.97 | 85.30% | 14.70% | 2.03 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 2 | 0 | 7.66 | 86.20% | 13.80% | 2.28 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 2 | 2 | 11.39 | 90.60% | 9.40% | 3.00 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 2 | 3 | 11.44 | 91.00% | 9.00% | 3.00 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 2 | 4 | 11.35 | 91.40% | 8.60% | 3.00 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 4 | 0 | 4.25 | 77.20% | 22.80% | 1.60 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 4 | 2 | 7.67 | 84.60% | 15.40% | 2.30 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 4 | 3 | 11.26 | 83.80% | 16.20% | 3.00 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 4 | 4 | 11.25 | 91.10% | 8.90% | 3.00 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 6 | 0 | 3.82 | 72.10% | 27.90% | 0.94 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 6 | 2 | 4.32 | 77.10% | 22.90% | 1.63 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 6 | 3 | 6.41 | 83.20% | 16.80% | 1.85 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 6 | 4 | 7.65 | 85.20% | 14.80% | 2.26 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 2 | 0 | 8.73 | 68.20% | 31.80% | 2.02 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 2 | 2 | 13.22 | 60.50% | 39.50% | 2.48 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 2 | 3 | 13.29 | 61.70% | 38.30% | 2.51 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 2 | 4 | 13.36 | 65.10% | 34.90% | 2.50 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 4 | 0 | 5.25 | 51.50% | 48.50% | 1.50 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 4 | 2 | 8.73 | 69.10% | 30.90% | 2.04 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 4 | 3 | 12.98 | 51.80% | 48.20% | 2.49 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 4 | 4 | 13.34 | 64.90% | 35.10% | 2.51 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 6 | 0 | 4.05 | 68.80% | 31.20% | 1.19 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 6 | 2 | 5.27 | 50.60% | 49.40% | 1.53 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 6 | 3 | 6.60 | 75.70% | 24.30% | 1.81 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 6 | 4 | 8.68 | 70.00% | 30.00% | 2.03 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 2 | 0 | 7.16 | 74.50% | 25.50% | 2.43 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 2 | 2 | 13.88 | 86.50% | 13.50% | 2.49 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 2 | 3 | 13.81 | 86.90% | 13.10% | 2.47 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 2 | 4 | 13.90 | 89.10% | 10.90% | 2.49 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 4 | 0 | 5.35 | 72.50% | 27.50% | 2.21 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 4 | 2 | 7.14 | 73.40% | 26.60% | 2.46 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 4 | 3 | 12.91 | 62.50% | 37.50% | 2.50 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 4 | 4 | 13.91 | 88.20% | 11.80% | 2.55 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 6 | 0 | 2.30 | 62.90% | 37.10% | 1.05 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 6 | 2 | 5.28 | 72.10% | 27.90% | 2.23 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 6 | 3 | 5.39 | 72.30% | 27.70% | 2.20 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 6 | 4 | 7.17 | 73.90% | 26.10% | 2.43 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 2 | 0 | 4.85 | 24.70% | 75.30% | 2.45 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 2 | 2 | 10.42 | 74.50% | 25.50% | 3.00 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 2 | 3 | 10.40 | 72.80% | 27.20% | 3.00 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 2 | 4 | 10.34 | 74.00% | 26.00% | 3.00 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 4 | 0 | 2.19 | 16.10% | 83.90% | 1.27 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 4 | 2 | 4.80 | 27.60% | 72.40% | 2.42 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 4 | 3 | 7.98 | 25.30% | 74.70% | 3.00 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 4 | 4 | 10.32 | 70.50% | 29.50% | 3.00 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 6 | 0 | 1.39 | 58.60% | 41.40% | 0.64 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 6 | 2 | 2.20 | 15.50% | 84.50% | 1.27 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 6 | 3 | 3.80 | 59.90% | 40.10% | 1.82 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 6 | 4 | 4.83 | 28.60% | 71.40% | 2.43 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 2 | 0 | 5.05 | 17.70% | 82.30% | 2.25 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 2 | 2 | 12.07 | 28.90% | 71.10% | 2.50 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 2 | 3 | 12.02 | 30.70% | 69.30% | 2.51 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 2 | 4 | 12.10 | 30.70% | 69.30% | 2.53 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 4 | 0 | 2.37 | 9.80% | 90.20% | 1.34 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 4 | 2 | 5.05 | 14.00% | 86.00% | 2.30 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 4 | 3 | 8.83 | 13.50% | 86.50% | 2.49 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 4 | 4 | 12.03 | 31.50% | 68.50% | 2.50 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 6 | 0 | 1.68 | 39.70% | 60.30% | 0.88 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 6 | 2 | 2.40 | 11.80% | 88.20% | 1.35 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 6 | 3 | 4.44 | 37.10% | 62.90% | 2.08 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 6 | 4 | 5.05 | 17.00% | 83.00% | 2.28 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 2 | 0 | 8.73 | 80.70% | 19.30% | 2.01 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 2 | 2 | 13.89 | 87.70% | 12.30% | 2.52 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 2 | 3 | 13.82 | 88.70% | 11.30% | 2.50 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 2 | 4 | 13.79 | 88.10% | 11.90% | 2.53 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 4 | 0 | 5.34 | 66.20% | 33.80% | 1.47 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 4 | 2 | 8.77 | 82.00% | 18.00% | 1.99 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 4 | 3 | 13.57 | 74.80% | 25.20% | 2.47 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 4 | 4 | 13.85 | 88.30% | 11.70% | 2.50 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 6 | 0 | 4.12 | 66.50% | 33.50% | 1.24 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 6 | 2 | 5.31 | 67.10% | 32.90% | 1.47 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 6 | 3 | 6.57 | 71.50% | 28.50% | 1.74 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 6 | 4 | 8.69 | 78.70% | 21.30% | 2.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 2 | 0 | 7.16 | 68.40% | 31.60% | 2.20 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 2 | 2 | 10.38 | 74.30% | 25.70% | 3.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 2 | 3 | 10.40 | 72.30% | 27.70% | 3.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 2 | 4 | 10.42 | 75.40% | 24.60% | 3.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 4 | 0 | 3.69 | 65.80% | 34.20% | 1.51 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 4 | 2 | 7.16 | 68.80% | 31.20% | 2.20 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 4 | 3 | 10.22 | 64.50% | 35.50% | 3.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 4 | 4 | 10.34 | 72.20% | 27.80% | 3.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 6 | 0 | 3.38 | 55.20% | 44.80% | 0.77 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 6 | 2 | 3.71 | 62.00% | 38.00% | 1.56 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 6 | 3 | 5.74 | 63.30% | 36.70% | 1.72 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 6 | 4 | 7.12 | 68.50% | 31.50% | 2.21 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 2 | 0 | 8.00 | 42.50% | 57.50% | 2.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 2 | 2 | 12.02 | 32.40% | 67.60% | 2.51 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 2 | 3 | 12.04 | 33.20% | 66.80% | 2.52 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 2 | 4 | 12.00 | 30.90% | 69.10% | 2.47 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 4 | 0 | 4.49 | 26.20% | 73.80% | 1.47 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 4 | 2 | 8.01 | 41.40% | 58.60% | 2.01 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 4 | 3 | 11.56 | 24.00% | 76.00% | 2.52 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 4 | 4 | 12.14 | 31.70% | 68.30% | 2.49 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 6 | 0 | 3.60 | 41.40% | 58.60% | 1.14 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 6 | 2 | 4.42 | 25.50% | 74.50% | 1.46 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 6 | 3 | 6.03 | 48.20% | 51.80% | 1.78 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 6 | 4 | 7.99 | 40.40% | 59.60% | 2.00 |

## Interpretation

- Penetration 1 removes pure armor stalemates: every successful Attack deals at least one Damage Box.
- Against armor that fully absorbs a normal weapon, Power Attack increases damage from the Penetration floor of 1 only when its added Box exceeds the Absorption threshold.
- Power Attack still spends offensive Stamina and therefore can leave the Power Attacker less able to Deflect, Evade, or Soften Blow later in the duel.
- Penetration 1 is therefore a universal fallback, while Power Attack remains a high-risk method of improving damage beyond that fallback.

## Questions Raised

1. Should Penetration 1 be a common Trait, a rare Trait, or a property of particular weapon categories such as picks and piercing weapons?
2. Should Penetration be a minimum-damage floor as modeled here, or should it reduce Damage Absorption instead?
3. Does Penetration 1 make the 2/4/6 weapon Damage Box bands more usable across armor bands?
4. Does the current Level 1 Power Attack trade remain attractive enough when Penetration ensures at least 1 Damage Box without it?
