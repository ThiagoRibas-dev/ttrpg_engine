"""Model the proposed Primary Attribute and Secondary ASI cadence.

Research only. Does not establish an advancement rule.
"""
from functools import lru_cache
from pathlib import Path

ROOT = Path('/home/user/ttrpg_idealization')
OUT = ROOT / '02_comparative_system_analysis/27_attribute_advancement_cadence_model.md'

# Die indices and Resource Values.
DICE = (4, 6, 8, 10, 12)
RESOURCE_VALUE = {4: 1, 6: 2, 8: 3, 10: 4, 12: 5}
STEP_COST = {(4, 6): 1, (6, 8): 2, (8, 10): 2, (10, 12): 3}
ASI_LEVELS = (4, 8, 12, 16, 20)
ASI_POINTS = 2
START = (8, 6, 6, 6, 4, 4)  # Primary first; five secondary Attributes follow.


def upgrade(state, index):
    die = state[index]
    die_index = DICE.index(die)
    if die == 12:
        return None, None
    nxt_die = DICE[die_index + 1]
    cost = STEP_COST[(die, nxt_die)]
    nxt = list(state)
    nxt[index] = nxt_die
    return tuple(nxt), cost


@lru_cache(maxsize=None)
def reachable(state, points):
    """Return every final state reachable while spending up to points on secondaries."""
    results = {state}
    for index in range(1, len(state)):
        nxt, cost = upgrade(state, index)
        if nxt and cost <= points:
            results |= reachable(nxt, points - cost)
    return frozenset(results)


states = {START}
by_level = {}
for level in ASI_LEVELS:
    next_states = set()
    for state in states:
        next_states |= set(reachable(state, ASI_POINTS))
    states = next_states
    by_level[level] = states

# The calculation above permits each ASI to spend 0-2 points but does not carry unspent
# points. For the headline examples, use the total 10-point budget, which permits saving.
# Enumerate all secondary profiles reachable by a total budget of 10.
final_states = reachable(START, ASI_POINTS * len(ASI_LEVELS))
secondary_profiles = sorted({tuple(sorted(s[1:], reverse=True)) for s in final_states}, reverse=True)

# Explicit example spending paths, including saved points.
examples = {
    'Focused secondary': [
        (4, 'd6 → d8', 2, 0),
        (8, 'd8 → d10', 2, 0),
        (12, 'save points', 0, 2),
        (16, 'd10 → d12', 3, 1),
        (20, 'd4 → d8', 3, 0),
    ],
    'Two d10 secondaries': [
        (4, 'Secondary A: d6 → d8', 2, 0),
        (8, 'Secondary A: d8 → d10', 2, 0),
        (12, 'Secondary B: d6 → d8', 2, 0),
        (16, 'Secondary B: d8 → d10', 2, 0),
        (20, '1 remaining point may raise d4 → d6; 1 point remains saved', 1, 1),
    ],
}

primary_rows = []
for level in range(1, 21):
    die = 8 if level <= 8 else 10 if level <= 16 else 12
    pool = 2 if level <= 4 else 3 if level <= 8 else 4 if level <= 12 else 5 if level <= 16 else 6
    primary_rows.append((level, f'd{die}', pool))

text = '''# Attribute Advancement Cadence Model

**Status:** Research artifact; non-canonical.  
**Purpose:** Test the proposed permanent Attribute advancement cadence against the existing Tier, Dice Pool, and Difficulty Vector calibration. This artifact does not select or establish an Attribute advancement rule.

## Proposed Inputs Being Modeled

```text
Starting Attributes:
  One d8 Primary Attribute.
  Three d6 secondary Attributes.
  Two d4 secondary Attributes.

Primary Attribute:
  d8 at Level 1.
  d10 at Level 9.
  d12 at Level 17.
  No permanent Attribute Die exceeds d12.

Secondary ASIs:
  2 points at Levels 4, 8, 12, 16, and 20.
  Unspent points may be saved.
```

## Secondary Step Costs

| Increase | Cost |
|---|---:|
| d4 → d6 | 1 point |
| d6 → d8 | 2 points |
| d8 → d10 | 2 points |
| d10 → d12 | 3 points |

The five ASIs provide **10 total points** by Level 20.

## Primary Attribute Alignment

| Level range | Primary Attribute | Baseline Competency Pool | Existing calibration Tier |
|---|---|---:|---|
'''
for level, die, pool in primary_rows:
    if level in (1, 5, 9, 13, 17):
        tier = {1:'Trained',5:'Veteran',9:'Master',13:'Hero',17:'Legend'}[level]
        text += f'| {level}–{min(level+3,20)} | {die} | {pool}d | {tier} |\n'
text += '''
The proposed Primary Attribute cadence exactly matches the Attribute Die progression already used by the official Tier Difficulty Vector calibration profile:

```text
Levels 1–8:   d8
Levels 9–16:  d10
Levels 17–20: d12
```

This means it does not require recalculating the existing Tier-profile probability tables. The established calibrated pools remain:

```text
Trained: 3d8
Veteran: 4d8
Master:  6d10
Hero:    8d10
Legend:  9d12
```

## Example Secondary Builds

### Focused Secondary Attribute

| ASI Level | Expenditure | Points spent | Points saved after ASI |
|---:|---|---:|---:|
'''
for level, use, cost, saved in examples['Focused secondary']:
    text += f'| {level} | {use} | {cost} | {saved} |\n'
text += '''
Result at Level 20:

```text
One d12 secondary Attribute.
One d8 former-d4 Attribute.
Two d6 secondary Attributes.
One d4 secondary Attribute.
```

A d6 secondary Attribute reaching d12 gains three Resource Values when it contributes to a resource or paired defense:

```text
d6 Resource Value 2 → d12 Resource Value 5.
```

### Two d10 Secondary Attributes

| ASI Level | Expenditure | Points spent | Points saved after ASI |
|---:|---|---:|---:|
'''
for level, use, cost, saved in examples['Two d10 secondaries']:
    text += f'| {level} | {use} | {cost} | {saved} |\n'
text += '''
Result at Level 20:

```text
Two d10 secondary Attributes.
One d6 former-d4 Attribute.
One d6 secondary Attribute.
One d4 secondary Attribute.
One saved Step Point.
```

Each d6 secondary Attribute reaching d10 gains two Resource Values where relevant:

```text
d6 Resource Value 2 → d10 Resource Value 4.
```

## Feasibility Result

The proposed 10-point Secondary ASI budget supports both stated goals:

| Goal | Total cost | Achievable by Level 20? |
|---|---:|---|
| Raise one d6 secondary Attribute to d12 | 7 | Yes |
| Raise one d4 secondary Attribute to d8 at the same time | 3 | Yes |
| Raise two d6 secondary Attributes to d10 | 8 | Yes |
| Raise one d4 secondary Attribute to d6 at the same time | 1 | Yes; 1 point remains saved |

## Implications for Existing Calibration

- The Primary Attribute cadence is already the cadence assumed by the official Level 1–20 calibration reference.
- Secondary ASIs increase flexibility, paired defenses, Resource Values, and off-role checks; they do **not** change the reference Primary Attribute probability profile unless the player invests in the Attribute used by that profile.
- The model preserves the permanent d12 ceiling. The temporary `d12 → d20` Exert exception remains separate from permanent advancement.
- The current probability research does not yet model optimized secondary-Attribute defense profiles. A future paired-defense pass can use the focused-secondary and two-d10-secondary examples above.

## Questions Before Canonization

1. Is the Primary Attribute progression exactly `d8 → d10 at 9 → d12 at 17`?
2. Do unused Secondary Step Points carry forward indefinitely?
3. Does the Primary Attribute receive no automatic milestone at Levels 5, 15, or 20?
4. May Secondary Step Points improve any non-Primary Attribute, including an Attribute that has become important through multiclassing?
5. Are the listed per-step costs final, including their treatment of an Attribute already at d12?
'''
OUT.write_text(text, encoding='utf-8')
print(OUT)
print(f'Reachable Level-20 secondary profiles under a 10-point budget: {len(secondary_profiles)}')
