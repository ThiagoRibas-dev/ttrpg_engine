"""Exact research model: class defense tracks versus equivalent Strike/Deflect pools."""
from collections import defaultdict
from math import factorial
from pathlib import Path

ROOT = Path('/home/user/ttrpg_idealization')
OUT = ROOT / '02_comparative_system_analysis/33_class_defense_progression_equivalence_model.md'

TRACKS = {
    'Good': [(1, 8, 2), (5, 8, 3), (9, 10, 4), (13, 10, 5), (17, 12, 6)],
    'Medium': [(1, 8, 1), (5, 8, 2), (9, 10, 3), (13, 10, 4), (17, 12, 5)],
    'Bad': [(1, 8, 1), (5, 8, 1), (9, 10, 2), (13, 10, 3), (17, 12, 4)],
}


def ordered_distribution(sides, pool):
    # Distribution over sorted results, represented compactly by counts per face.
    # Each multiset has multinomial multiplicity among all ordered rolls.
    states = {(0,) * sides: 1}
    for _ in range(pool):
        nxt = defaultdict(int)
        for counts, multiplicity in states.items():
            for face in range(sides):
                updated = list(counts)
                updated[face] += 1
                nxt[tuple(updated)] += multiplicity
        states = nxt
    total = sides ** pool
    # Dynamic construction counts each ordered roll exactly once.
    return {counts: count / total for counts, count in states.items()}


def tie_probability(sides, pool):
    dist = ordered_distribution(sides, pool)
    return sum(prob * prob for prob in dist.values())

text = '''# Class Defense Progression Equivalence Model

**Status:** Research artifact; non-canonical.  
**Purpose:** Verify whether Good, Medium, and Bad class defense tracks produce the same direct opposed-roll mathematics as an equivalent Strike/Deflect pool.

## Assumptions

```text
A paired defense uses:
  Highest paired Attribute Die as die size.
  Assigned class defense Rank as baseline pool volume.

A representative primary Attribute progression uses:
  d8 at Levels 1–8.
  d10 at Levels 9–16.
  d12 at Levels 17–20.

No armor, shield, Boon, Bane, Condition, Stamina expenditure,
Equipment, Trait, or Class feature is applied.
```

When a Good Reflex progression and an equivalent Good Strike progression use the same die size and pool volume, Evasion and Deflect use identical opposed-roll mathematics. Any later difference must therefore come from their distinct eligibility, armor, shield, movement, or feature interactions—not from the base pool.

## Equal-Track Strike / Deflect / Evasion Equivalence

| Track | Level | Die Size | Pool | Attacker success vs equal Deflect | Attacker success vs equal Evasion | Complete tie, defender wins |
|---|---:|---:|---:|---:|---:|---:|
'''
for track, rows in TRACKS.items():
    for level, sides, pool in rows:
        tie = tie_probability(sides, pool)
        win = (1 - tie) / 2
        text += f'| {track} | {level} | d{sides} | {pool}d{sides} | {win*100:.4f}% | {win*100:.4f}% | {tie*100:.4f}% |\n'

text += '''
## Interpretation

```text
Good Reflex:
  Matches Good Strike / Deflect when the relevant primary Attribute
  produces the same die size.

Medium Reflex:
  Matches Medium Strike / Deflect under the same condition.

Bad Reflex:
  Matches Bad Strike / Deflect under the same condition.
```

The prior Level 1 Evasion model used only the bare paired Reflex base (`d8 + d6, keep highest`) without a Good Reflex class track. It therefore modeled a Bad/Untrained Reflex profile, not a Rogue- or Ranger-like Good Reflex profile.

## Deliberate Sources of Later Difference

The equivalence demonstrated here does not remove intended distinctions:

| Source | Deflect | Evasion |
|---|---|---|
| Required source | Suitable weapon, shield, body, or Permission | Eligible attack that can be avoided through movement, footwork, position, or reflex |
| Shield | Shield grants 1 Boon | No shield benefit by default |
| Heavy Armor | No baseline Bane | 1 Bane |
| Interpose | Required underlying defense | Not the underlying Interpose defense |
| Position / movement | Limited by Deflect applicability | May later gain distinct movement or terrain advantages |
| Class features | May improve Deflect / shield interactions | May improve Evasion / movement interactions |

## Conclusion

The Good / Medium / Bad defense tracks resolve the earlier modeling concern. No baseline Evasion pool increase is required merely to match a corresponding Class combat progression. Future models should use the assigned class defense track rather than the bare paired-Attribute base when evaluating a classed Actor.
'''
OUT.write_text(text, encoding='utf-8')
print(OUT)
