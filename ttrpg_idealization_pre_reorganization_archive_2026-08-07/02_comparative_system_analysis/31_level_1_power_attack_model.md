# Level 1 Power Attack Model

**Status:** Research artifact; non-canonical.  
**Purpose:** Test the current DEC-083 Level 1 Power Attack procedure against a non-Power-Attacking equal-level opponent. This artifact selects no balance rule.

## Assumptions

```text
At Level 1:
  Power Attack X maximum = 1.
  Character Level sets the cap, even though the relevant d8
  Attribute Die would permit a higher cap at later levels.

Power Attacker:
  Uses X=1 whenever it has at least 1 Stamina on its own turn.
  Takes 1 Bane: 2d8 becomes 1d8; 3d8 becomes 2d8.
  Adds 1 Damage Box on a hit before Damage Absorption.

Opponent:
  Never uses Power Attack.

Both sides:
  Use their selected triggered defense whenever they have Stamina.
  Have the same armor Absorption band.
```

The model uses the same Level 1 Deflect and Evasion profiles as `30_level_1_fixed_damage_and_armor_model.md`. It does not include Criticals, Wounds, range, Traits, conditions, or tactical maneuvers.

## Single-Attack Tradeoff

| Attack profile | Normal Strike pool | Power Attack pool at X=1 | Damage change |
|---|---|---|---|
| Strict base | 2d8 | 1d8 | +1 Damage Box before Absorption |
| Fully-equipped calibration | 3d8 | 2d8 | +1 Damage Box before Absorption |

## Duel Simulation

`Power Attacker down` and `Normal Attacker down` show which side reaches 0 Vitality. The Power Attacker uses Power Attack until its Stamina is depleted, then makes ordinary Strikes.

| Attack profile | Policy | Defense matchup | Base Damage | Absorption | Mean attacks to 0 | Power Attacker down | Normal Attacker down | Mean Power Attacks used | Mean Power Attacks that dealt damage |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Strict base | Deflect-first | Deflect vs Deflect | 2 | 0 | 7.50 | 82.85% | 17.15% | 2.46 | 0.68 |
| Strict base | Deflect-first | Deflect vs Deflect | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Deflect vs Deflect | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Deflect vs Deflect | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Deflect vs Deflect | 4 | 0 | 5.59 | 79.60% | 20.40% | 2.26 | 0.63 |
| Strict base | Deflect-first | Deflect vs Deflect | 4 | 2 | 7.46 | 81.10% | 18.90% | 2.47 | 0.69 |
| Strict base | Deflect-first | Deflect vs Deflect | 4 | 3 | 13.38 | 72.80% | 27.20% | 2.50 | 0.70 |
| Strict base | Deflect-first | Deflect vs Deflect | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Deflect vs Deflect | 6 | 0 | 2.49 | 67.35% | 32.65% | 1.12 | 0.31 |
| Strict base | Deflect-first | Deflect vs Deflect | 6 | 2 | 5.59 | 80.80% | 19.20% | 2.22 | 0.60 |
| Strict base | Deflect-first | Deflect vs Deflect | 6 | 3 | 5.55 | 79.10% | 20.90% | 2.25 | 0.64 |
| Strict base | Deflect-first | Deflect vs Deflect | 6 | 4 | 7.54 | 82.30% | 17.70% | 2.45 | 0.66 |
| Strict base | Deflect-first | Evasion vs Evasion | 2 | 0 | 6.43 | 58.60% | 41.40% | 2.75 | 0.95 |
| Strict base | Deflect-first | Evasion vs Evasion | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Evasion vs Evasion | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Evasion vs Evasion | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Evasion vs Evasion | 4 | 0 | 3.32 | 41.10% | 58.90% | 1.66 | 0.59 |
| Strict base | Deflect-first | Evasion vs Evasion | 4 | 2 | 6.39 | 58.45% | 41.55% | 2.74 | 0.96 |
| Strict base | Deflect-first | Evasion vs Evasion | 4 | 3 | 10.38 | 66.30% | 33.70% | 3.00 | 1.04 |
| Strict base | Deflect-first | Evasion vs Evasion | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Evasion vs Evasion | 6 | 0 | 1.90 | 70.55% | 29.45% | 0.84 | 0.29 |
| Strict base | Deflect-first | Evasion vs Evasion | 6 | 2 | 3.29 | 41.25% | 58.75% | 1.65 | 0.59 |
| Strict base | Deflect-first | Evasion vs Evasion | 6 | 3 | 4.78 | 78.80% | 21.20% | 2.13 | 0.72 |
| Strict base | Deflect-first | Evasion vs Evasion | 6 | 4 | 6.38 | 55.85% | 44.15% | 2.75 | 0.99 |
| Strict base | Deflect-first | Deflect vs Evasion | 2 | 0 | 6.74 | 51.75% | 48.25% | 2.43 | 0.84 |
| Strict base | Deflect-first | Deflect vs Evasion | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Deflect vs Evasion | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Deflect vs Evasion | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Deflect vs Evasion | 4 | 0 | 3.72 | 39.95% | 60.05% | 1.73 | 0.59 |
| Strict base | Deflect-first | Deflect vs Evasion | 4 | 2 | 6.74 | 51.85% | 48.15% | 2.43 | 0.81 |
| Strict base | Deflect-first | Deflect vs Evasion | 4 | 3 | 11.83 | 44.20% | 55.80% | 2.51 | 0.86 |
| Strict base | Deflect-first | Deflect vs Evasion | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Deflect-first | Deflect vs Evasion | 6 | 0 | 2.31 | 61.55% | 38.45% | 1.07 | 0.37 |
| Strict base | Deflect-first | Deflect vs Evasion | 6 | 2 | 3.65 | 37.15% | 62.85% | 1.75 | 0.62 |
| Strict base | Deflect-first | Deflect vs Evasion | 6 | 3 | 5.32 | 69.45% | 30.55% | 2.22 | 0.79 |
| Strict base | Deflect-first | Deflect vs Evasion | 6 | 4 | 6.65 | 47.75% | 52.25% | 2.46 | 0.87 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 2 | 0 | 8.93 | 86.15% | 13.85% | 2.04 | 0.58 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 4 | 0 | 5.44 | 71.40% | 28.60% | 1.45 | 0.51 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 4 | 2 | 8.92 | 86.45% | 13.55% | 2.01 | 0.55 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 4 | 3 | 13.76 | 83.35% | 16.65% | 2.48 | 0.68 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 6 | 0 | 4.18 | 72.50% | 27.50% | 1.22 | 0.43 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 6 | 2 | 5.46 | 70.35% | 29.65% | 1.49 | 0.52 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 6 | 3 | 6.65 | 77.35% | 22.65% | 1.78 | 0.54 |
| Strict base | Aggressive Soften Blow | Deflect vs Deflect | 6 | 4 | 8.96 | 86.70% | 13.30% | 2.03 | 0.55 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 2 | 0 | 7.65 | 85.65% | 14.35% | 2.27 | 0.80 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 4 | 0 | 4.25 | 77.35% | 22.65% | 1.59 | 0.57 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 4 | 2 | 7.67 | 84.90% | 15.10% | 2.30 | 0.84 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 4 | 3 | 11.23 | 82.60% | 17.40% | 3.00 | 1.06 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 6 | 0 | 3.82 | 72.90% | 27.10% | 0.92 | 0.38 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 6 | 2 | 4.27 | 78.10% | 21.90% | 1.61 | 0.59 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 6 | 3 | 6.36 | 82.45% | 17.55% | 1.83 | 0.63 |
| Strict base | Aggressive Soften Blow | Evasion vs Evasion | 6 | 4 | 7.65 | 85.20% | 14.80% | 2.30 | 0.81 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 2 | 0 | 8.68 | 71.25% | 28.75% | 2.00 | 0.71 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 4 | 0 | 5.25 | 50.85% | 49.15% | 1.51 | 0.56 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 4 | 2 | 8.71 | 70.20% | 29.80% | 2.02 | 0.70 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 4 | 3 | 13.04 | 56.15% | 43.85% | 2.50 | 0.86 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 6 | 0 | 4.08 | 66.95% | 33.05% | 1.21 | 0.52 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 6 | 2 | 5.29 | 51.70% | 48.30% | 1.50 | 0.53 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 6 | 3 | 6.58 | 77.20% | 22.80% | 1.76 | 0.63 |
| Strict base | Aggressive Soften Blow | Deflect vs Evasion | 6 | 4 | 8.65 | 68.70% | 31.30% | 2.01 | 0.74 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 2 | 0 | 7.24 | 75.20% | 24.80% | 2.43 | 0.84 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 4 | 0 | 5.29 | 73.65% | 26.35% | 2.21 | 0.77 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 4 | 2 | 7.17 | 74.10% | 25.90% | 2.44 | 0.86 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 4 | 3 | 13.04 | 65.25% | 34.75% | 2.50 | 0.89 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 6 | 0 | 2.30 | 61.25% | 38.75% | 1.07 | 0.37 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 6 | 2 | 5.35 | 69.95% | 30.05% | 2.21 | 0.82 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 6 | 3 | 5.36 | 71.25% | 28.75% | 2.22 | 0.79 |
| Fully-equipped calibration | Deflect-first | Deflect vs Deflect | 6 | 4 | 7.09 | 72.95% | 27.05% | 2.42 | 0.89 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 2 | 0 | 4.83 | 25.80% | 74.20% | 2.44 | 1.63 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 4 | 0 | 2.21 | 16.35% | 83.65% | 1.28 | 0.84 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 4 | 2 | 4.81 | 28.05% | 71.95% | 2.43 | 1.60 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 4 | 3 | 7.89 | 23.25% | 76.75% | 3.00 | 2.03 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 6 | 0 | 1.41 | 57.20% | 42.80% | 0.67 | 0.43 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 6 | 2 | 2.11 | 15.75% | 84.25% | 1.24 | 0.84 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 6 | 3 | 3.81 | 58.00% | 42.00% | 1.85 | 1.26 |
| Fully-equipped calibration | Deflect-first | Evasion vs Evasion | 6 | 4 | 4.77 | 25.90% | 74.10% | 2.42 | 1.64 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 2 | 0 | 5.07 | 17.55% | 82.45% | 2.26 | 1.50 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 4 | 0 | 2.37 | 10.80% | 89.20% | 1.34 | 0.89 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 4 | 2 | 5.06 | 15.50% | 84.50% | 2.28 | 1.51 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 4 | 3 | 8.71 | 11.70% | 88.30% | 2.49 | 1.68 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 6 | 0 | 1.70 | 40.25% | 59.75% | 0.89 | 0.59 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 6 | 2 | 2.35 | 9.85% | 90.15% | 1.33 | 0.90 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 6 | 3 | 4.36 | 36.95% | 63.05% | 2.07 | 1.40 |
| Fully-equipped calibration | Deflect-first | Deflect vs Evasion | 6 | 4 | 5.06 | 17.10% | 82.90% | 2.28 | 1.51 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 2 | 0 | 8.75 | 80.95% | 19.05% | 2.01 | 0.72 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 4 | 0 | 5.27 | 66.75% | 33.25% | 1.43 | 0.62 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 4 | 2 | 8.74 | 80.15% | 19.85% | 2.01 | 0.72 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 4 | 3 | 13.54 | 76.65% | 23.35% | 2.49 | 0.90 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 6 | 0 | 4.10 | 65.85% | 34.15% | 1.22 | 0.53 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 6 | 2 | 5.29 | 65.70% | 34.30% | 1.47 | 0.63 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 6 | 3 | 6.53 | 73.25% | 26.75% | 1.76 | 0.66 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Deflect | 6 | 4 | 8.76 | 79.05% | 20.95% | 2.01 | 0.73 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 2 | 0 | 7.15 | 69.50% | 30.50% | 2.20 | 1.50 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 4 | 0 | 3.66 | 63.15% | 36.85% | 1.53 | 1.01 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 4 | 2 | 7.15 | 69.45% | 30.55% | 2.21 | 1.50 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 4 | 3 | 10.17 | 65.00% | 35.00% | 3.00 | 1.99 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 6 | 0 | 3.37 | 57.10% | 42.90% | 0.77 | 0.54 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 6 | 2 | 3.67 | 61.40% | 38.60% | 1.55 | 1.04 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 6 | 3 | 5.75 | 64.35% | 35.65% | 1.72 | 1.13 |
| Fully-equipped calibration | Aggressive Soften Blow | Evasion vs Evasion | 6 | 4 | 7.16 | 67.55% | 32.45% | 2.22 | 1.51 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 2 | 0 | 7.97 | 44.00% | 56.00% | 2.00 | 1.33 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 2 | 2 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 2 | 3 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 2 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 4 | 0 | 4.42 | 23.20% | 76.80% | 1.47 | 1.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 4 | 2 | 7.97 | 41.85% | 58.15% | 2.01 | 1.37 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 4 | 3 | 11.46 | 21.30% | 78.70% | 2.53 | 1.72 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 4 | 4 | — | 0.00% | 0.00% | 0.00 | 0.00 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 6 | 0 | 3.66 | 42.40% | 57.60% | 1.18 | 0.88 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 6 | 2 | 4.48 | 24.05% | 75.95% | 1.45 | 0.97 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 6 | 3 | 6.02 | 48.35% | 51.65% | 1.75 | 1.18 |
| Fully-equipped calibration | Aggressive Soften Blow | Deflect vs Evasion | 6 | 4 | 7.99 | 44.10% | 55.90% | 1.99 | 1.34 |

## Interpretation

- At Level 1, Power Attack is a one-Box, one-Bane trade because the Character-Level cap is 1. The Bane-floor issue does not occur in this pass.
- The Power Attacker spends Stamina on offense and therefore has fewer Stamina points for Deflect/Evasion and Soften Blow. This is the intended offensive-versus-defense trade.
- Against armor that fully stops the base Damage Box value but not the Power Attack value, Power Attack can be the only modeled route to deal damage without another Trait or Permission.
- The model does not determine whether later-level X values remain balanced. A Level 5, 9, 17, and 20 progression pass is required once weapon Damage Box and Absorption bands are selected.

## Questions Raised

1. Does the one-Box, one-Bane Power Attack trade feel worthwhile at Level 1?
2. Should Power Attack be the expected answer to armor thresholds, or should Penetrating / Armor-Piercing weapons fill that role?
3. How many Stamina points should a Power Attacker preserve for triggered defense and Soften Blow?
4. Does the Character-Level cap remain safe once X exceeds the Strike pool’s number of dice at later levels?
