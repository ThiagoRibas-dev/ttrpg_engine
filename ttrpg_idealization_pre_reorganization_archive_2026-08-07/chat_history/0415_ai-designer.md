---
turn: 415
role: "AI-Designer"
source: chat_history.json
---

# Turn 415 — AI-Designer

Yes, I think we should record it—but as a calibration profile table, not as a fundamental equipment or advancement rule.

The table is useful because it combines the vectors we need to interpret together:

text
Tier
Character Level
Competency Rank
Attribute Die Size
Baseline Pool
Equipment Boons
Fully Equipped Pool
Easy Vector
Medium Vector
Hard Vector

It would make the official suggestions much easier to use than separate per-pool sections.

Where It Should Live

I recommend adding it to:

text
03_core_baseline_system/13_tier_difficulty_vector_reference.md

That document already owns the official Tier Difficulty Vector suggestions.

It should be clearly labeled:

text
Provisional Calibration Profile

because:

Equipment Boons are still provisional.
Equipment progression is not yet canonized.
The table is a framework reference, not an equipment rules table.
Future equipment work may change the assumed fully equipped pools.
Should We Repeat All 20 Levels?

Yes, if the goal is practical usability.

Although the values repeat within each Tier, a full Level 1–20 table is useful for:

Class design.
Spell calibration.
Monster design.
Equipment comparison.
Encounter planning.
Future character-sheet references.
Level-by-level progression analysis.

The repeated rows are not a mathematical problem. They make the artifact usable without requiring someone to infer the Tier range.

Proposed Table Format
text
| Tier | Character Level | Competency Rank | Attribute Die | Baseline Pool | Equipment Boons | Equipped Pool | Easy DC | Medium DC | Hard DC |

Example:

text
| Trained | 1 | Trained | d8 | 2d | +1B | 3d8 | DC 5 | DC 5,4 | DC 5,5 |

The table should include the recommended vector candidates for each band, potentially in the format:

text
DC 5 / DC 5,2

if more than one vector of that length is being retained.

Important Distinction

This table should not replace:

The exhaustive vector research artifact.
The generic pool-volume matrices.
The generic die-size matrices.
The equipment framework.
The progression framework.

Its role would be:

A practical official reference showing the current recommended Tier-relative Difficulty Vector calibration under the current provisional preparation assumptions.

So I recommend adding it as a clearly labeled appendix to:

text
03_core_baseline_system/13_tier_difficulty_vector_reference.md

rather than placing it in the Equipment or Leveling documents.
