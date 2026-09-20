# Foundational Math Reference Analysis

**Status:** Research artifact; no canonical mechanics decided.  
**Sources reviewed:**

- `pathfinder 2e Fundamental Math.txt`
- `An aggregation of the base stats of all D&D 3.5 System Reference Document monsters organisation by Challenge Rating.csv`

## 1. Pathfinder 2e Fundamental Math — Useful Findings

The reference material emphasizes that a small numerical bonus can affect more than ordinary success probability because it can also change critical-failure and critical-success boundaries.

Useful observations for our system:

- Success probability and degree-of-success probability should be measured separately.
- A bonus or Boon can change the probability of reaching a higher outcome band, not merely the probability of passing.
- Advancement systems often maintain a relatively stable relationship between character capability and level-appropriate challenges by increasing both capability and expected difficulty.
- Extreme mismatches should be intentionally classified as impossible, automatic, or exceptional rather than accidentally produced by ordinary scaling.
- Automatic Bonus Progression is a useful reference for separating character advancement from item advancement.
- PF2e’s level-based DC and attack/AC comparisons are useful as a model for maintaining a stable expected curve, even though our system uses bounded dice rather than d20 modifiers.

These observations do not establish our target probabilities. They identify which probability outputs should eventually be measured:

- At least one success.
- Multiple successes.
- Critical or exceptional outcomes.
- Automatic success or failure boundaries.
- Equal-tier opposed contests.
- Extreme-tier mismatches.

## 2. D&D 3.5e SRD Monster Aggregation — Useful Findings

The CSV aggregates average and maximum monster statistics by Challenge Rating, including:

- Hit Points.
- Initiative.
- Armor Class.
- Touch AC.
- Flat-footed AC.
- Base Attack Bonus.
- Fortitude.
- Reflex.
- Will.

It is useful as an empirical content-distribution reference, not as a direct mathematical target.

### Useful applications

- Estimate the spread of monster durability at each Challenge Rating.
- Compare average and maximum defensive values.
- Identify how sharply monster durability and defenses expand at high Challenge Ratings.
- Identify outlier monsters that should not define baseline expectations.
- Compare physical defense growth with save growth.
- Build conversion envelopes for PC-versus-monster calibration.

### Limitations

- Challenge Rating is not equivalent to Character Level or our High Fantasy Tier.
- The dataset aggregates heterogeneous monsters with radically different roles.
- Average values obscure role-specific distributions.
- Maximum values are strongly affected by outliers.
- D&D 3.5e’s linear modifier math cannot be copied directly into bounded dice.
- Small sample sizes at high Challenge Ratings make averages unstable.
- HP, AC, BAB, and saves are not independent variables in the original system.

## 3. Suggested Use in Current Phase 1 Work

### Step 1 — Build our raw probability reference

Use the existing exact matrices for:

- `1dX` through expanded pools.
- `d4`, `d6`, `d8`, `d10`, and `d12`.
- At-least thresholds.
- Required-success thresholds.
- Boons and Banes.
- Floors.
- Automatic Successes.
- Opposed pools.

### Step 2 — Measure outcome bands

Do not measure only “pass/fail.” Add columns for:

- At least 1 success.
- At least 2 successes.
- At least 3 successes.
- Automatic Success contribution.
- Defender-wins-ties frequency.
- Probability of total failure.

Maximum-face events are not a primary probability target. Increasing die size makes a specific maximum face rarer, while increasing pool volume makes at least one maximum face more common. Since current Natural Criticals use an independent d100 Critical Threat Profile, a maximum face is not automatically a Critical. Maximum-face frequency should only be measured when a specific future effect explicitly uses it.

### Step 3 — Create role-based opposition bands

Use the 3.5e monster data to create broad reference envelopes rather than direct conversions:

- Fragile/Rabble durability.
- Standard enemy durability.
- Elite enemy durability.
- Boss durability.
- Low-defense specialist.
- High-defense specialist.
- Strong Fortitude, Reflex, or Will profiles.

The averages and maxima should be treated as clues for what kinds of opposition the framework must represent, not as values to reproduce numerically.

### Step 4 — Map source-system vectors to our vectors

| D&D 3.5e / PF2e concept | Possible role in our system | Status |
|---|---|---|
| Attack bonus/proficiency | Combat Skill, Attribute Die, pool volume, Floor | Framework established; calibration open |
| Armor Class | Reflexes, Parry, Damage Absorption | Framework established; calibration open |
| Fortitude/Reflex/Will | Paired defenses | Framework established |
| Item bonus | Typed Enhancement Boon or Equipment Trait | Framework direction; details open |
| Circumstance bonus | Circumstance Boon/Bane | Framework established |
| Status/morale bonus | Morale Boon/Bane | Framework established |
| Competence bonus | Competence Boon/Bane | Framework established |
| Level-based DC | Fixed DC plus Required Successes | Framework established; calibration open |
| Critical success threshold | Required Successes, Automatic Successes, or explicit effect | Framework direction; calibration open |
| Caster level | Tradition Competency and Spell Slot Progression | Framework established |
| Power/ability score scaling | Attribute Die and Competency Floor | Framework established |

## 4. Questions for the Next Probability Pass

These remain research questions, not decisions:

1. What is the probability of at least one success for every raw pool and threshold?
2. How quickly does a second or third Required Success become reliable?
3. How much does each additional die improve high-threshold reliability?
4. How much does a Floor change the lower tail?
5. How much does a Boon change multiple-success probability?
6. How much does a Bane reduce it?
7. How often do opposed pools tie after secondary dice?
8. How often do Automatic Successes determine an opposed contest before dice are rolled?
9. What pool and Floor combinations represent fragile, standard, elite, and boss actors?
10. What equipment and spell effects can be added without making the bounded curve unstable?

## 5. Current Recommendation

Use the two supplied references as calibration inputs, not as rules templates:

- Use PF2e to study stable level-appropriate probability curves, degree-of-success boundaries, and item/level advancement relationships.
- Use the D&D 3.5e monster aggregation to study empirical opposition distributions and conversion envelopes.
- Keep our own exact dice matrices as the primary mathematical foundation.
- Delay final probability targets until the raw dice, Floors, Boons/Banes, Required Successes, Automatic Successes, and opposed-tie procedures have all been measured together.
