# Floor and Equipment Dice: DC Target Mapping

**Status:** Phase 1 research artifact; no DC targets or equipment assumptions are canonical.

**Assumption:** The supplied Equipment Boons are treated as net additional same-size dice after all type and same-source stacking rules.

**Target bands:** Easy 85%, Medium 65%, Hard 55%. A DC is reported only when the closest available fixed DC from 2–12 is within ±2 percentage points. Otherwise the cell is `NA`.

**Probability model:** `P(max ≥ DC)`, with `no Floor mechanic applied`. Since all listed floors are below the target DCs selected here, the calculated probabilities use the raw maximum-of-pool distribution for those cells.

| Level | Tier | Die | Baseline Pool | Equipment Boons | Final Pool | Floor | Easy DC / Actual | Medium DC / Actual | Hard DC / Actual |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | Trained | d8 | 2d | +1B | 3d8 | 3 | `NA` (nearest DC 5: 87.50%) | `NA` (nearest DC 7: 57.81%) | `NA` (nearest DC 7: 57.81%) |
| 2 | Trained | d8 | 2d | +1B | 3d8 | 3 | `NA` (nearest DC 5: 87.50%) | `NA` (nearest DC 7: 57.81%) | `NA` (nearest DC 7: 57.81%) |
| 3 | Trained | d8 | 2d | +1B | 3d8 | 3 | `NA` (nearest DC 5: 87.50%) | `NA` (nearest DC 7: 57.81%) | `NA` (nearest DC 7: 57.81%) |
| 4 | Trained | d8 | 2d | +1B | 3d8 | 3 | `NA` (nearest DC 5: 87.50%) | `NA` (nearest DC 7: 57.81%) | `NA` (nearest DC 7: 57.81%) |
| 5 | Veteran | d8 | 3d | +1B | 4d8 | 4 | `6` / 84.74% | `NA` (nearest DC 7: 68.36%) | `NA` (nearest DC 7: 68.36%) |
| 6 | Veteran | d8 | 3d | +1B | 4d8 | 4 | `6` / 84.74% | `NA` (nearest DC 7: 68.36%) | `NA` (nearest DC 7: 68.36%) |
| 7 | Veteran | d8 | 3d | +2B | 5d8 | 5 | `NA` (nearest DC 6: 90.46%) | `NA` (nearest DC 7: 76.27%) | `NA` (nearest DC 8: 48.71%) |
| 8 | Veteran | d8 | 3d | +2B | 5d8 | 5 | `NA` (nearest DC 6: 90.46%) | `NA` (nearest DC 7: 76.27%) | `NA` (nearest DC 8: 48.71%) |
| 9 | Master | d10 | 4d | +2B | 6d10 | 6 | `NA` (nearest DC 8: 88.24%) | `NA` (nearest DC 9: 73.79%) | `NA` (nearest DC 10: 46.86%) |
| 10 | Master | d10 | 4d | +2B | 6d10 | 6 | `NA` (nearest DC 8: 88.24%) | `NA` (nearest DC 9: 73.79%) | `NA` (nearest DC 10: 46.86%) |
| 11 | Master | d10 | 4d | +2B | 6d10 | 6 | `NA` (nearest DC 8: 88.24%) | `NA` (nearest DC 9: 73.79%) | `NA` (nearest DC 10: 46.86%) |
| 12 | Master | d10 | 4d | +2B | 6d10 | 6 | `NA` (nearest DC 8: 88.24%) | `NA` (nearest DC 9: 73.79%) | `NA` (nearest DC 10: 46.86%) |
| 13 | Hero | d10 | 5d | +3B | 8d10 | 8 | `9` / 83.22% | `NA` (nearest DC 10: 56.95%) | `10` / 56.95% |
| 14 | Hero | d10 | 5d | +3B | 8d10 | 8 | `9` / 83.22% | `NA` (nearest DC 10: 56.95%) | `10` / 56.95% |
| 15 | Hero | d10 | 5d | +3B | 8d10 | 8 | `9` / 83.22% | `NA` (nearest DC 10: 56.95%) | `10` / 56.95% |
| 16 | Hero | d10 | 5d | +3B | 8d10 | 8 | `9` / 83.22% | `NA` (nearest DC 10: 56.95%) | `10` / 56.95% |
| 17 | Legend | d12 | 6d | +3B | 9d12 | 9 | `NA` (nearest DC 11: 80.62%) | `NA` (nearest DC 12: 54.30%) | `12` / 54.30% |
| 18 | Legend | d12 | 6d | +3B | 9d12 | 9 | `NA` (nearest DC 11: 80.62%) | `NA` (nearest DC 12: 54.30%) | `12` / 54.30% |
| 19 | Legend | d12 | 6d | +4B | 10d12 | 10 | `11` / 83.85% | `NA` (nearest DC 12: 58.11%) | `NA` (nearest DC 12: 58.11%) |
| 20 | Legend | d12 | 6d | +4B | 10d12 | 10 | `11` / 83.85% | `NA` (nearest DC 12: 58.11%) | `NA` (nearest DC 12: 58.11%) |

## Interpretation

- `NA` means no single fixed DC from 2–12 lands within ±2 percentage points of the requested target for that level/profile.
- Equipment increases pool volume and therefore also increases the Floor, subject to the die-size cap.
- At this stage, Easy/Medium/Hard are target labels only; they are not yet canonical DC categories.
- This pass uses at-least-one-success probabilities only. Required Successes, Boons/Banes beyond the stated equipment assumption, Automatic Successes, and opposed checks are deferred.
