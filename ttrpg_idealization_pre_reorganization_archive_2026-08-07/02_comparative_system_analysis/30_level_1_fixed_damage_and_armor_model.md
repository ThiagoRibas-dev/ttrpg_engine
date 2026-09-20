# Level 1 Fixed Damage and Armor Model

**Status:** Research artifact; non-canonical.  
**Purpose:** Test the proposed fixed Damage Box and Damage Absorption bands against a representative Level 1 martial duel. This artifact selects no weapon, armor, or balance rule.

## Assumptions

```text
Damage bands tested:
  2, 4, and 6 fixed Damage Boxes.

Armor Absorption bands tested:
  0, 2, 3, and 4.

Armor may reduce incoming damage to 0.

Level 1 martial resource profile:
  STR d8 primary; DEX d6; CON d6.
  Good Vitality and Good Stamina at class level 1.
  Vitality: 6.
  Stamina: 5.

No Stamina or Vitality recovery occurs during the duel.
No Wound Roll, downed state, critical, Power Attack, Cleave,
Charge, Condition, or weapon-Trait effect is included.
```

The strict base profile uses the Level 1 Trained `2d8` Strike/Deflect pool. The fully-equipped calibration profile uses the existing probability-calibration assumption of `3d8`. Both combatants are equal.

## Static Damage after Absorption

| Fixed Damage Boxes | Absorption 0 | Absorption 2 | Absorption 3 | Absorption 4 |
|---:|---:|---:|---:|---:|
| 2 | 2 | 0 | 0 | 0 |
| 4 | 4 | 2 | 1 | 0 |
| 6 | 6 | 4 | 3 | 2 |

## Equal-Pool Attack versus Deflect Odds

| Profile | Strike / Deflect pool | Attacker success | Complete tie, defender wins |
|---|---|---:|---:|
| Strict base | 2d8 vs 2d8 | 48.54% | 2.93% |
| Fully-equipped calibration | 3d8 vs 3d8 | 49.52% | 0.96% |

## Duel Pacing Simulation

Each combatant makes one Strike per turn. Before a Strike can inflict damage, the defender spends 1 Stamina to Deflect whenever possible. The simulation uses two deliberately simple policies:

```text
Deflect-first:
  Spend Stamina on Deflect only.

Deflect then aggressive Soften Blow:
  Spend Stamina on Deflect; if hit, spend all necessary remaining
  Stamina, up to what is available, to reduce remaining damage toward 1.
```

Results report the mean number of individual attacks until either combatant reaches 0 Vitality. A duel that has not ended after 200 attacks is reported as not defeated within the simulation horizon.

| Profile | Policy | Damage | Absorption | Mean attacks to 0 Vitality | Defeated within 200 attacks |
|---|---|---:|---:|---:|---:|
| Strict base | Deflect-first | 2 | 0 | 8.61 | 100.00% |
| Strict base | Deflect-first | 2 | 2 | — | 0.00% |
| Strict base | Deflect-first | 2 | 3 | — | 0.00% |
| Strict base | Deflect-first | 2 | 4 | — | 0.00% |
| Strict base | Deflect-first | 4 | 0 | 5.41 | 100.00% |
| Strict base | Deflect-first | 4 | 2 | 8.60 | 100.00% |
| Strict base | Deflect-first | 4 | 3 | 15.29 | 100.00% |
| Strict base | Deflect-first | 4 | 4 | — | 0.00% |
| Strict base | Deflect-first | 6 | 0 | 2.07 | 100.00% |
| Strict base | Deflect-first | 6 | 2 | 5.43 | 100.00% |
| Strict base | Deflect-first | 6 | 3 | 5.42 | 100.00% |
| Strict base | Deflect-first | 6 | 4 | 8.61 | 100.00% |
| Strict base | Deflect then aggressive Soften Blow | 2 | 0 | 9.71 | 100.00% |
| Strict base | Deflect then aggressive Soften Blow | 2 | 2 | — | 0.00% |
| Strict base | Deflect then aggressive Soften Blow | 2 | 3 | — | 0.00% |
| Strict base | Deflect then aggressive Soften Blow | 2 | 4 | — | 0.00% |
| Strict base | Deflect then aggressive Soften Blow | 4 | 0 | 6.49 | 100.00% |
| Strict base | Deflect then aggressive Soften Blow | 4 | 2 | 9.71 | 100.00% |
| Strict base | Deflect then aggressive Soften Blow | 4 | 3 | 15.30 | 100.00% |
| Strict base | Deflect then aggressive Soften Blow | 4 | 4 | — | 0.00% |
| Strict base | Deflect then aggressive Soften Blow | 6 | 0 | 4.05 | 100.00% |
| Strict base | Deflect then aggressive Soften Blow | 6 | 2 | 6.49 | 100.00% |
| Strict base | Deflect then aggressive Soften Blow | 6 | 3 | 7.11 | 100.00% |
| Strict base | Deflect then aggressive Soften Blow | 6 | 4 | 9.70 | 100.00% |
| Fully-equipped calibration | Deflect-first | 2 | 0 | 8.51 | 100.00% |
| Fully-equipped calibration | Deflect-first | 2 | 2 | — | 0.00% |
| Fully-equipped calibration | Deflect-first | 2 | 3 | — | 0.00% |
| Fully-equipped calibration | Deflect-first | 2 | 4 | — | 0.00% |
| Fully-equipped calibration | Deflect-first | 4 | 0 | 5.35 | 100.00% |
| Fully-equipped calibration | Deflect-first | 4 | 2 | 8.50 | 100.00% |
| Fully-equipped calibration | Deflect-first | 4 | 3 | 15.20 | 100.00% |
| Fully-equipped calibration | Deflect-first | 4 | 4 | — | 0.00% |
| Fully-equipped calibration | Deflect-first | 6 | 0 | 2.01 | 100.00% |
| Fully-equipped calibration | Deflect-first | 6 | 2 | 5.35 | 100.00% |
| Fully-equipped calibration | Deflect-first | 6 | 3 | 5.34 | 100.00% |
| Fully-equipped calibration | Deflect-first | 6 | 4 | 8.50 | 100.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 2 | 0 | 9.64 | 100.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 2 | 2 | — | 0.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 2 | 3 | — | 0.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 2 | 4 | — | 0.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 4 | 0 | 6.46 | 100.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 4 | 2 | 9.62 | 100.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 4 | 3 | 15.19 | 100.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 4 | 4 | — | 0.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 6 | 0 | 4.01 | 100.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 6 | 2 | 6.45 | 100.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 6 | 3 | 7.05 | 100.00% |
| Fully-equipped calibration | Deflect then aggressive Soften Blow | 6 | 4 | 9.63 | 100.00% |

## Interpretation

- Armor 2 completely stops the 2-Box band; Armor 4 completely stops both 2- and 4-Box bands. This is a deliberate threshold effect of allowing Armor to reduce damage to zero.
- The 6-Box band remains meaningful against every tested armor band, dealing 2 Boxes through Absorption 4 before Soften Blow.
- Equal-pool Deflect keeps attacker success below 50% because complete ties belong to the defender. The 3d8 calibration profile has fewer complete ties and therefore a slightly higher attacker success rate than the 2d8 profile.
- Aggressive Soften Blow can sharply extend survival in the first few successful hits, but rapidly empties the Level 1 Stamina reserve. It is a resource-spike defense rather than a sustainable every-hit solution.
- Results are not a final time-to-defeat target. Weapon Traits, armor trade-offs, heavy-armor Evasion Banes, Damage Tags, Penetration, Criticals, Wounds, Class features, and tactical maneuvers must be modeled before selecting final values.

## Questions Raised by the Model

1. Is it desirable that Armor 2 fully stops a 2-Box weapon?
2. Must every combatant carry a Penetrating / Armor-Piercing option to threaten Heavy Armor?
3. Is a 6-Box ordinary weapon too high, or should it be reserved for very heavy weapons, monsters, siege weapons, and Power Attack?
4. Should Heavy Armor absorb 3 or 4 Boxes when it already imposes an Evasion Bane?
5. Should a shield add Damage Absorption only when Deflecting, or remain a Deflect/Interpose tool only?
6. Which Stamina-defense policy produces the intended encounter pacing once the complete combat sequence is modeled?
