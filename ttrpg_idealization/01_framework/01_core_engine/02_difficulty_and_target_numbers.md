# Difficulty and Target Numbers

**Status:** Locked canonical specification.  
**Spine:** 01 Core Engine, Batch 2 of 5 ([DEC-109](../../02_decisions/01_master_decision_log.md)).  
**Source:** Migrated 2026-09-19 from archived `03_core_baseline_system/01_resolution_engine.md` §4 and `08_statistical_framework_and_check_modes.md`.  
**Voice:** [DEC-110](../../02_decisions/01_master_decision_log.md), [DEC-111](../../02_decisions/01_master_decision_log.md) — rules and meaning unchanged.

## Purpose <a id="purpose"></a>

Before any dice hit the table, someone decides how hard the task is. This specification owns that scale: the Difficulty Class (DC), a single number, and the difficulty vector, a short list of numbers that one roll has to satisfy.

For example, forcing a stuck door might be DC 5: your best die must show 5 or better. Leaping a chasm, catching the far ledge, and hauling yourself up in one motion might be DC 6,5,3: your best die must meet 6, your second-best must meet 5, and a third die must meet 3.

## Scope <a id="scope"></a>

**Owns:**
- The bounded DC scale (2 through 12) and its working descriptions.
- Difficulty vector notation and the positional comparison rule.
- The check-mode and statistical relationships of the difficulty model.

**Does not own:**
- The check procedure itself: [Core Checks and Dice Pools](01_checks_and_dice_pools.md) (its steps 7 and 9 read this scale).
- Opposed checks and defender-wins-ties: Batch 4 specification.
- Required Successes procedures in maneuvers: Conflict Framework.
- Suggested Tier Difficulty Vectors and probability data: research, in the [Tier Difficulty Vector Reference](../../04_research/probability_and_calibration/tier_difficulty_vector_reference.md).

## Canonical Procedure <a id="canonical-procedure"></a>

### Difficulty Classes <a id="difficulty-classes"></a>

An ordinary Difficulty Class is a Target Number from 2 through 12.

| DC | Working description |
|---:|---|
| 2 | Trivial |
| 3 | Routine |
| 5 | Challenging |
| 7 | Formidable |
| 9 | Heroic |
| 11 | Legendary |
| 12 | Extreme |

Roll the final pool and compare your kept result against the DC, per [the core check](01_checks_and_dice_pools.md#core-check-procedure). If it meets or beats the DC, the check succeeds.

The names are working labels, GM shorthand for the numbers. You don't need to memorize them; the number is the rule.

### Difficulty Vectors <a id="difficulty-vectors"></a>

A difficulty vector is written as comma-separated thresholds:

```text
DC 5
DC 5,4
DC 6,5,3
```

Roll the final Dice Pool, sort your dice from highest to lowest, sort the vector's thresholds from highest to lowest, and compare them in order: first die against first threshold, second against second, and so on. A die meets its threshold by equalling or beating it. Extra dice beyond the vector's length are ignored for that vector. The check succeeds only when every threshold in the vector is met.

For example, you roll 5d8 against DC 6,5,3 and get 8, 6, 6, 3, 1. Compare in order: the 8 meets 6, the first 6 meets 5, the second 6 meets 3. Every threshold is met, so the check succeeds. Your two remaining dice, the 3 and the 1, are ignored for this vector.

### Check Modes and Statistical Relationships <a id="check-modes"></a>

The difficulty model ties the check modes together (consolidated from the archived statistical framework):

- Attribute Die Size is the capability ceiling; Competency Rank sets the baseline pool size. The final pool and the difficulty together determine the odds (pool model: [Core Checks and Dice Pools](01_checks_and_dice_pools.md); Competency: Actor Framework, pending migration).
- Fixed-DC checks and difficulty vectors are the two unopposed modes. Opposed checks resolve against another pool instead of a number (Batch 4 specification).
- Multi-success counting: successful faces beyond a vector's requirements can satisfy Required Successes or trigger explicitly defined results (procedure owner: Conflict Framework).
- The scale is bounded on both ends: the ordinary die ladder tops out at d12 and the DC scale at 12 (see [the die ladder](01_checks_and_dice_pools.md#die-ladder)). A d12 is the only ordinary die that can meet DC 12; anything above requires an explicit exception, such as Exert's d20.

## State Changes and Results <a id="state-changes"></a>

Resolving against a DC or vector yields success or failure. Counted-successes outcomes (Required Successes, triggered results) belong to the calling rule, as in [Core Checks and Dice Pools](01_checks_and_dice_pools.md#state-changes). The difficulty scale itself creates no persistent state.

## Rule Interactions <a id="rule-interactions"></a>

- [Core Checks and Dice Pools](01_checks_and_dice_pools.md) **uses** this scale at steps 7 and 9 of the core check.
- Boons, Banes, and Die Steps **modify** the pool that reads this scale ([Batch 3 specification](03_boons_banes_and_die_steps.md)); they affect the pool, never the DC or vector itself.
- Maneuvers and complex checks **use** vectors as Required Successes (Conflict Framework).
- The [Tier Difficulty Vector Reference](../../04_research/probability_and_calibration/tier_difficulty_vector_reference.md) **tests** this scale: it is the suggested calibration data for choosing DCs and vectors by Tier.
- The World/GM layer will consume the working descriptions when it migrates.

Formal edges live in the [Framework Registry](../../00_architecture/framework_registry.yaml), not in this file.

## Open Definitions and Deferred Content <a id="open-definitions"></a>

1. **Calibration:** the exact DC names and vector choices remain a research task; the working descriptions are provisional. Calibration data: [Tier Difficulty Vector Reference](../../04_research/probability_and_calibration/tier_difficulty_vector_reference.md).
2. **Unnamed intermediate DCs:** the working-description table names DC 2, 3, 5, 7, 9, 11, and 12. DC 4, 6, 8, and 10 have no working names; the source neither names them nor states how they interpolate.
3. **Tier-pool assumptions:** the research reference's summary table assumes Tier pool compositions (for example, Trained 2d8+1B). Those derive from leveling decisions (DEC-095) that are still archived; re-validate the table when the Actor Framework migrates.
4. **Cross-reference debt:** opposed checks and defender-wins-ties links land with Batch 4; the Required Successes procedure link lands with the Conflict Framework.

## References <a id="references"></a>

- Decisions: [DEC-102](../../02_decisions/01_master_decision_log.md) (terminology), DEC-103 (rule hierarchy), DEC-104 (link policy), DEC-109 (this migration), DEC-110 and DEC-111 (voice).
- Research: [Tier Difficulty Vector Reference](../../04_research/probability_and_calibration/tier_difficulty_vector_reference.md).
- [Migration Manifest](../../00_architecture/migration_manifest.md) — migration provenance.
- Archived sources: `ttrpg_idealization_pre_reorganization_archive_2026-08-07/03_core_baseline_system/01_resolution_engine.md` (§4) and `08_statistical_framework_and_check_modes.md`.
