# Class Defense Progression Equivalence Model

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
| Good | 1 | d8 | 2d8 | 48.5352% | 48.5352% | 2.9297% |
| Good | 5 | d8 | 3d8 | 49.5178% | 49.5178% | 0.9644% |
| Good | 9 | d10 | 4d10 | 49.9121% | 49.9121% | 0.1759% |
| Good | 13 | d10 | 5d10 | 49.9643% | 49.9643% | 0.0713% |
| Good | 17 | d12 | 6d12 | 49.9937% | 49.9937% | 0.0126% |
| Medium | 1 | d8 | 1d8 | 43.7500% | 43.7500% | 12.5000% |
| Medium | 5 | d8 | 2d8 | 48.5352% | 48.5352% | 2.9297% |
| Medium | 9 | d10 | 3d10 | 49.7430% | 49.7430% | 0.5140% |
| Medium | 13 | d10 | 4d10 | 49.9121% | 49.9121% | 0.1759% |
| Medium | 17 | d12 | 5d12 | 49.9843% | 49.9843% | 0.0313% |
| Bad | 1 | d8 | 1d8 | 43.7500% | 43.7500% | 12.5000% |
| Bad | 5 | d8 | 1d8 | 43.7500% | 43.7500% | 12.5000% |
| Bad | 9 | d10 | 2d10 | 49.0500% | 49.0500% | 1.9000% |
| Bad | 13 | d10 | 3d10 | 49.7430% | 49.7430% | 0.5140% |
| Bad | 17 | d12 | 4d12 | 49.9553% | 49.9553% | 0.0895% |

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
