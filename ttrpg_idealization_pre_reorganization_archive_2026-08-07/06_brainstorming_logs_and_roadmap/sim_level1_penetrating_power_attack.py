"""Research-only Level 1 Penetration 1 / Power Attack calibration model."""
from itertools import product
from pathlib import Path
import random
import statistics

ROOT = Path('/home/user/ttrpg_idealization')
OUT = ROOT / '02_comparative_system_analysis/32_level_1_penetration_and_power_attack_model.md'
SIDES = 8
DAMAGE_BANDS = (2, 4, 6)
ABSORPTION_BANDS = (0, 2, 3, 4)
TRIALS = 1_000
MAX_ATTACKS = 60
PROFILES = {'Deflect': {'vitality': 6, 'stamina': 5}, 'Evasion': {'vitality': 5, 'stamina': 6}}
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
    # DEC-083 limits Level 1 Power Attack to X=1.
    x = 1 if power and attacker['stamina'] >= 1 else 0
    if x:
        attacker['stamina'] -= 1
    attack = roll_pool(max(1, pool - x), rng)
    if defender['stamina'] >= 1:
        defender['stamina'] -= 1
        defense_roll = roll_pool(pool, rng) if defense == 'Deflect' else roll_reflex(rng)
        if not attacker_wins(attack, defense_roll):
            return x, False
    # Penetration 1 in this pass means a successful Attack deals at least one Box.
    remaining = max(1, base_damage + x - armor)
    if policy == 'aggressive_soften' and defender['stamina'] > 0:
        # Soften Blow can reduce damage only toward 1, never below it.
        spend = min(remaining - 1, defender['stamina'])
        defender['stamina'] -= spend
        remaining -= spend
    defender['vitality'] -= remaining
    return x, True


def duel(pool, damage, armor, defense_a, defense_b, policy, rng):
    a = dict(PROFILES[defense_a])
    b = dict(PROFILES[defense_b])
    a_first = bool(rng.randint(0, 1))
    attacks = power_attempts = 0
    while attacks < MAX_ATTACKS and a['vitality'] > 0 and b['vitality'] > 0:
        if (attacks % 2 == 0) == a_first:
            x, _ = resolve_attack(pool, damage, armor, a, b, defense_b, policy, True, rng)
            power_attempts += x
        else:
            resolve_attack(pool, damage, armor, b, a, defense_a, policy, False, rng)
        attacks += 1
    return attacks, a['vitality'] <= 0, b['vitality'] <= 0, power_attempts

rng = random.Random(20260731)
text = '''# Level 1 Penetration 1 and Power Attack Model

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
'''
for damage in DAMAGE_BANDS:
    text += f'| {damage} | ' + ' | '.join(str(max(1, damage - armor)) for armor in ABSORPTION_BANDS) + ' |\n'

text += '''
## Duel Simulation

| Attack profile | Policy | Defense matchup | Base Damage | Absorption | Mean attacks to 0 | Power Attacker down | Normal Attacker down | Mean Power Attacks used |
|---|---|---|---:|---:|---:|---:|---:|---:|
'''
for profile_label, pool in POOL_PROFILES.items():
    for policy_label, policy in POLICIES.items():
        for defense_a, defense_b in MATCHUPS:
            for damage in DAMAGE_BANDS:
                for armor in ABSORPTION_BANDS:
                    results = [duel(pool, damage, armor, defense_a, defense_b, policy, rng) for _ in range(TRIALS)]
                    ended = [n for n, a_down, b_down, _ in results if a_down or b_down]
                    text += f'| {profile_label} | {policy_label} | {defense_a} vs {defense_b} | {damage} | {armor} | {statistics.mean(ended):.2f} | {sum(a for _, a, _, _ in results) / TRIALS * 100:.2f}% | {sum(b for _, _, b, _ in results) / TRIALS * 100:.2f}% | {statistics.mean(x for _, _, _, x in results):.2f} |\n'

text += '''
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
'''
OUT.write_text(text, encoding='utf-8')
print(OUT)
