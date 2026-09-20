"""Research-only Level 1 fixed Damage Box / armor / defense calibration model."""
from itertools import product
from pathlib import Path
import random
import statistics

ROOT = Path('/home/user/ttrpg_idealization')
OUT = ROOT / '02_comparative_system_analysis/30_level_1_fixed_damage_and_armor_model.md'
SIDES = 8
DAMAGE_BANDS = (2, 4, 6)
ABSORPTION_BANDS = (0, 2, 3, 4)
TRIALS = 8_000
MAX_ATTACKS = 200

# Representative Level 1 profiles. Attribute Resource Values: d8=3; d6=2.
# Good Vitality/Stamina progression at class level 1 contributes +1.
# Deflect martial: STR d8, DEX d6, CON d6, INT d6 -> V6, S5.
# Evasion martial: DEX d8, INT d6, CON d6, STR d6 -> V5, S6.
PROFILES = {
    'Deflect': {'vitality': 6, 'stamina': 5},
    'Evasion': {'vitality': 5, 'stamina': 6},
}


def roll_pool(n, rng):
    return tuple(sorted((rng.randint(1, SIDES) for _ in range(n)), reverse=True))


def roll_reflex(rng):
    # DEX d8 + INT d6, keep highest: a one-die defense result.
    return (max(rng.randint(1, 8), rng.randint(1, 6)),)


def attacker_wins(attack, defense):
    for a, d in zip(attack, defense):
        if a != d:
            return a > d
    return len(attack) > len(defense)


def exact_deflect_odds(pool):
    rows = [tuple(sorted(v, reverse=True)) for v in product(range(1, 9), repeat=pool)]
    total = len(rows) ** 2
    wins = ties = 0
    for attack in rows:
        for defense in rows:
            if attacker_wins(attack, defense):
                wins += 1
            elif attack == defense:
                ties += 1
    return wins / total, ties / total


def exact_evasion_odds(pool):
    attacks = [tuple(sorted(v, reverse=True)) for v in product(range(1, 9), repeat=pool)]
    defenses = [(max(dex, intel),) for dex in range(1, 9) for intel in range(1, 7)]
    total = len(attacks) * len(defenses)
    wins = sum(attacker_wins(a, d) for a in attacks for d in defenses)
    return wins / total


def resolve_attack(pool, damage, armor, defender, defense, policy, rng):
    attack = roll_pool(pool, rng)
    if defender['stamina'] >= 1:
        defender['stamina'] -= 1
        defense_roll = roll_pool(pool, rng) if defense == 'Deflect' else roll_reflex(rng)
        if not attacker_wins(attack, defense_roll):
            return
    remaining = max(0, damage - armor)
    if remaining and policy == 'aggressive_soften' and defender['stamina'] > 0:
        spend = min(remaining - 1, defender['stamina'])
        defender['stamina'] -= spend
        remaining -= spend
    defender['vitality'] -= remaining


def duel(pool, damage, armor, defense_a, defense_b, policy, rng):
    a = dict(PROFILES[defense_a])
    b = dict(PROFILES[defense_b])
    a_first = bool(rng.randint(0, 1))
    attacks = 0
    while attacks < MAX_ATTACKS and a['vitality'] > 0 and b['vitality'] > 0:
        if (attacks % 2 == 0) == a_first:
            resolve_attack(pool, damage, armor, b, defense_b, policy, rng)
        else:
            resolve_attack(pool, damage, armor, a, defense_a, policy, rng)
        attacks += 1
    return attacks, a['vitality'] <= 0, b['vitality'] <= 0

rng = random.Random(20260730)
pool_profiles = {'Strict base': 2, 'Fully-equipped calibration': 3}
policies = {'Deflect-first': 'deflect_only', 'Deflect then aggressive Soften Blow': 'aggressive_soften'}
matchups = (('Deflect', 'Deflect'), ('Evasion', 'Evasion'), ('Deflect', 'Evasion'))

text = '''# Level 1 Fixed Damage, Armor, and Defense Model

**Status:** Research artifact; non-canonical.  
**Purpose:** Test proposed fixed Damage Box and armor Absorption bands with equal Level 1 combatants using Deflect, Evasion, and mixed-defense matchups. This artifact selects no weapon, armor, or balance rule.

## Assumptions

```text
Damage bands tested:
  2, 4, and 6 fixed Damage Boxes.

Armor Absorption bands tested:
  0, 2, 3, and 4.

Armor may reduce incoming damage to 0.

Strict base attack profile:
  Trained 2d8 Strike.

Fully-equipped calibration attack profile:
  3d8 Strike / Deflect.

Deflect martial:
  STR d8, DEX d6, CON d6, INT d6.
  Vitality 6; Stamina 5.
  Deflect uses the same 2d8 or 3d8 pool as its Strike.

Evasion martial:
  DEX d8, INT d6, CON d6, STR d6.
  Vitality 5; Stamina 6.
  Evasion uses Reflexes: d8 + d6, keep highest.

No Stamina or Vitality recovery occurs during the duel.
No Wound Roll, downed state, Critical, Power Attack, Cleave, Charge,
Condition, weapon Trait, range, Reach, or initiative effect is included.
```

## Static Damage after Absorption

| Fixed Damage Boxes | Absorption 0 | Absorption 2 | Absorption 3 | Absorption 4 |
|---:|---:|---:|---:|---:|
'''
for damage in DAMAGE_BANDS:
    text += f'| {damage} | ' + ' | '.join(str(max(0, damage - armor)) for armor in ABSORPTION_BANDS) + ' |\n'

text += '''
## One-Attack Defense Odds

| Attack pool | Defense | Attacker success | Notes |
|---|---|---:|---|
'''
for label, pool in pool_profiles.items():
    win, tie = exact_deflect_odds(pool)
    evasion = exact_evasion_odds(pool)
    text += f'| {label}: {pool}d8 | Deflect {pool}d8 | {win*100:.2f}% | Complete tie {tie*100:.2f}%; defender wins ties |\n'
    text += f'| {label}: {pool}d8 | Evasion d8+d6 keep highest | {evasion*100:.2f}% | Reflex profile for a DEX-primary Level 1 martial |\n'

text += '''
## Duel Pacing Simulation

Each combatant makes one Strike per Turn. A defender with Stamina always uses its selected triggered defense. The first actor is randomized each duel.

Policies:

```text
Deflect-first:
  Spend Stamina on the selected triggered defense only.

Deflect then aggressive Soften Blow:
  Spend Stamina on the selected triggered defense. If hit, spend all
  remaining necessary Stamina, up to what is available, to reduce
  remaining damage toward 1 Damage Box.
```

Results report the mean number of individual attacks until either combatant reaches 0 Vitality. `—` means armor fully negates the tested Damage Box value, so no actor can reach 0 within this model.

| Attack profile | Policy | Defense matchup | Damage | Absorption | Mean attacks to 0 | Deflect actor down | Evasion actor down |
|---|---|---|---:|---:|---:|---:|---:|
'''
for profile_label, pool in pool_profiles.items():
    for policy_label, policy in policies.items():
        for defense_a, defense_b in matchups:
            for damage in DAMAGE_BANDS:
                for armor in ABSORPTION_BANDS:
                    if damage <= armor:
                        text += f'| {profile_label} | {policy_label} | {defense_a} vs {defense_b} | {damage} | {armor} | — | 0.00% | 0.00% |\n'
                        continue
                    results = [duel(pool, damage, armor, defense_a, defense_b, policy, rng) for _ in range(TRIALS)]
                    ended = [n for n, a_down, b_down in results if a_down or b_down]
                    a_down = sum(a_down for _, a_down, _ in results) / TRIALS
                    b_down = sum(b_down for _, _, b_down in results) / TRIALS
                    text += f'| {profile_label} | {policy_label} | {defense_a} vs {defense_b} | {damage} | {armor} | {statistics.mean(ended):.2f} | {a_down*100:.2f}% | {b_down*100:.2f}% |\n'

text += '''
## Interpretation

- Deflect is materially more reliable than the modeled Level 1 Evasion profile because it uses the same multi-die Combat Mastery pool as the Attack, while Evasion uses the paired Reflexes keep-highest pool.
- The Evasion martial has one more Stamina but one less Vitality under the stated primary-Attribute assumptions. The mixed matchup displays both effects.
- Armor thresholds remain decisive: Absorption equal to or greater than the Damage Box value creates a stalemate in a pure fixed-damage model without Power Attack, Penetration, Called Shot, other Traits, or external effects.
- Aggressive Soften Blow helps both defense profiles, but the more vulnerable Evasion profile typically needs it sooner and exhausts its Stamina reserve under sustained attacks.
- This is a narrow baseline model, not a verdict on Deflect versus Evasion balance. Movement, terrain, range, heavy-armor Evasion Banes, shields, Interpose, Full Defense, Reach, and Traits must be added before final calibration.

## Questions Raised

1. Should Evasion use a fuller pool than paired Reflexes keep-highest, or should its lower reliability be compensated by movement/position benefits?
2. Is a DEX-primary martial intended to have lower Vitality but higher Stamina than a STR-primary martial?
3. Should Deflect require a weapon/shield Trait that limits its availability, so it is not the universal best defense?
4. Do the armor thresholds require a common Penetrating / Armor-Piercing option for all martial groups?
5. Which defense profile should be used for future monster and NPC assumptions?
'''
OUT.write_text(text, encoding='utf-8')
print(OUT)
