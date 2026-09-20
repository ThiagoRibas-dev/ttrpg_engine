# Attribute Advancement Cadence Model

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
| 1–4 | d8 | 2d | Trained |
| 5–8 | d8 | 3d | Veteran |
| 9–12 | d10 | 4d | Master |
| 13–16 | d10 | 5d | Hero |
| 17–20 | d12 | 6d | Legend |

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
| 4 | d6 → d8 | 2 | 0 |
| 8 | d8 → d10 | 2 | 0 |
| 12 | save points | 0 | 2 |
| 16 | d10 → d12 | 3 | 1 |
| 20 | d4 → d8 | 3 | 0 |

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
| 4 | Secondary A: d6 → d8 | 2 | 0 |
| 8 | Secondary A: d8 → d10 | 2 | 0 |
| 12 | Secondary B: d6 → d8 | 2 | 0 |
| 16 | Secondary B: d8 → d10 | 2 | 0 |
| 20 | 1 remaining point may raise d4 → d6; 1 point remains saved | 1 | 1 |

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
