"""Research-only Level 1 Power Attack model under DEC-083."""
from itertools import product
from pathlib import Path
import random
import statistics

ROOT = Path('/home/user/ttrpg_idealization')
OUT = ROOT / '02_comparative_system_analysis/31_level_1_power_attack_model.md'
SIDES = 8
DAMAGE_BANDS = (2, 4, 6)
ABSORPTION_BANDS = (0, 2, 3, 4)
TRIALS = 2_000
MAX_ATTACKS = 60

# Same representative profiles as the Level 1 armor model.
PROFILES = {
    'Deflect': {'vitality': 6, 'stamina': 5},
    'Evasion': {'vitality': 5, 'stamina': 6},
}
POOL_PROFILES = {'Strict base': 2, 'Fully-equipped calibration': 3}
POLICIES = {'Deflect-first': 'deflect_only', 'Aggressive Soften Blow': 'aggressive_soften'}
MATCHUPS = (('Deflect', 'Deflect'), ('Evasion', 'Evasion'), ('Deflect', 'Evasion'))


def roll_pool(n, rng):
    return tuple(sorted((rng.randint(1, SIDES) for _ in range(n)), reverse=True))


def roll_reflex(rng):
    return (max(rng.randint(1, 8), rng.randint(1, 6)),)


def attacker_wins(attack, defense):
    for attack_face, defense_face in zip(attack, defense):
        if attack_face != defense_face:
            return attack_face > defense_face
    return len(attack) > len(defense)


def resolve_attack(pool, base_damage, armor, attacker, defender, defense, policy, power, rng):
    # DEC-083: Level 1 x=1 because Character Level is 1, even though the d8 cap is higher.
    x = 1 if power and attacker['stamina'] >= 1 else 0
    if x:
        attacker['stamina'] -= x
    attack = roll_pool(max(1, pool - x), rng)
    # The ordinary Bane floor is irrelevant at Level 1 because x cannot exceed 1.
    if defender['stamina'] >= 1:
        defender['stamina'] -= 1
        defense_roll = roll_pool(pool, rng) if defense == 'Deflect' else roll_reflex(rng)
        if not attacker_wins(attack, defense_roll):
            return x, False
    remaining = max(0, base_damage + x - armor)
    if remaining and policy == 'aggressive_soften' and defender['stamina'] > 0:
        spend = min(remaining - 1, defender['stamina'])
        defender['stamina'] -= spend
        remaining -= spend
    defender['vitality'] -= remaining
    return x, remaining > 0


def duel(pool, damage, armor, defense_a, defense_b, policy, rng):
    # A always uses Power Attack whenever it has 1 Stamina; B never does.
    a = dict(PROFILES[defense_a])
    b = dict(PROFILES[defense_b])
    a_first = bool(rng.randint(0, 1))
    attacks = power_attempts = power_hits = 0
    while attacks < MAX_ATTACKS and a['vitality'] > 0 and b['vitality'] > 0:
        if (attacks % 2 == 0) == a_first:
            x, dealt = resolve_attack(pool, damage, armor, a, b, defense_b, policy, True, rng)
            power_attempts += x
            power_hits += int(x and dealt)
        else:
            resolve_attack(pool, damage, armor, b, a, defense_a, policy, False, rng)
        attacks += 1
    return attacks, a['vitality'] <= 0, b['vitality'] <= 0, power_attempts, power_hits

rng = random.Random(20260730)
text = '''# Level 1 Power Attack Model

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
'''
for profile_label, pool in POOL_PROFILES.items():
    for policy_label, policy in POLICIES.items():
        for defense_a, defense_b in MATCHUPS:
            for damage in DAMAGE_BANDS:
                for armor in ABSORPTION_BANDS:
                    # If even the Power Attack hit cannot penetrate, neither side can reach 0.
                    if damage + 1 <= armor:
                        row = ('—', '0.00%', '0.00%', '0.00', '0.00')
                    else:
                        results = [duel(pool, damage, armor, defense_a, defense_b, policy, rng) for _ in range(TRIALS)]
                        ended = [n for n, a_down, b_down, _, _ in results if a_down or b_down]
                        if not ended:
                            row = ('—', '0.00%', '0.00%', '0.00', '0.00')
                        else:
                            row = (
                                f'{statistics.mean(ended):.2f}',
                                f'{sum(a for _, a, _, _, _ in results) / TRIALS * 100:.2f}%',
                                f'{sum(b for _, _, b, _, _ in results) / TRIALS * 100:.2f}%',
                                f'{statistics.mean(x for _, _, _, x, _ in results):.2f}',
                                f'{statistics.mean(x for _, _, _, _, x in results):.2f}',
                            )
                    text += f'| {profile_label} | {policy_label} | {defense_a} vs {defense_b} | {damage} | {armor} | ' + ' | '.join(row) + ' |\n'

text += '''
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
'''
OUT.write_text(text, encoding='utf-8')
print(OUT)
