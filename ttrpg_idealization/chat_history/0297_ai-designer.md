---
turn: 297
role: "AI-Designer"
source: chat_history.json
---

# Turn 297 — AI-Designer

I agree with the design goal. The current model has too many interacting layers:

text
Competency Rank → Pool Volume
Competency Rank → Floor
Banes → Pool Volume
Banes → Effective Floor
Die Size → Floor Cap

That is unnecessarily complicated.

The cleaner model is:

text
Competency Rank → Pool Volume
Pool Volume → Floor
Banes → Pool Volume

The Floor becomes a direct consequence of the final number of dice. A Bane lowering the pool automatically lowers the Floor without requiring a separate Bane-specific Floor rule.

Proposed New Structure
Competency Rank determines pool size

For example:

Competency Rank	Dice Pool
Untrained	2 dice
Trained	3 dice
Expert	4 dice
Master	5 dice
Legendary	6 dice

Then the pool size determines the Floor.

Floor mapping

To preserve the general shape of our existing Floor progression:

Final Pool Size	Floor
1 die	0
2 dice	0
3 dice	3
4 dice	5
5 dice	7
6 dice	9

This can be expressed as a simple lookup table rather than a separate Competency rule.

Bane Examples
Expert character
text
Expert:
  4d8, Floor 5

Apply one Bane:

text
3d8, Floor 3

Apply another Bane:

text
2d8, Floor 0

Apply another Bane:

text
1d8, Floor 0

Apply another Bane:

text
1d6, Floor 0

Apply further Banes:

text
Still 1d6, Floor 0

The Floor changes automatically because the pool size changes.

Important Consequence

This makes the pool-size ceiling a little different.

Previously:

text
Legendary:
  5dX, Floor 9

Under the new mapping, preserving Floor 9 requires:

text
6dX

That gives us three possible directions.

Option A — Expand the ordinary pool ceiling

Adopt:

text
Legendary:
  6dX, Floor 9

Advantages:

Preserves the existing Floor progression exactly.
Makes Legendary characters visibly distinct.
Makes the pool-to-Floor relationship very clean.
Supports high-tier automatic reliability.

Cost:

The natural pool ceiling becomes 6dX, not 5dX.
Probability tables must eventually include 6dX.
Boon stacking and high-tier pool expectations need recalibration.
Option B — Keep the 5dX ceiling

Use:

text
Untrained: 2dX, Floor 0
Trained: 3dX, Floor 3
Expert: 4dX, Floor 5
Master: 5dX, Floor 7
Legendary: 5dX, Floor 7

Advantages:

Preserves the 5dX ceiling.
Requires fewer dice.
No new Legendary pool category.

Cost:

Legendary no longer has a distinct Floor from Master.
Legendary advancement must be expressed through:
Automatic Successes.
Permissions.
Extra actions.
Special effects.
Larger fictional scope.
The former Floor 9 concept disappears or becomes content-specific.
Option C — Use 6dX only for Legendary content

Keep normal pools at 5dX, but grant:

text
Legendary:
  6dX, Floor 9

only through:

Legendary Competency.
Certain Class features.
Mythic or high-tier content.

This is effectively a controlled exception to the normal 5dX guideline.

My Recommendation

I recommend Option A:

text
Untrained: 2dX, Floor 0
Trained: 3dX, Floor 3
Expert: 4dX, Floor 5
Master: 5dX, Floor 7
Legendary: 6dX, Floor 9

This preserves the original competency fantasy:

text
Trained:
  Never fail DC 3.

Expert:
  Never fail DC 5.

Master:
  Never fail DC 7.

Legendary:
  Never fail DC 9.

It also makes the rule extremely easy to explain:

More dice mean both greater reliability and a higher Floor.

The cost is that we must update the earlier assumption that 5dX is the maximum natural pool. The new natural range would be:

text
2dX through 6dX

and enhanced content could exceed that when explicitly granted.

What Changes

This would supersede the current parts of:

00_baseline_framework_glossary.md
01_resolution_engine.md
07_check_pool_generation_and_class_differentiation.md
PHASE_1_CHECKLIST.md
03_outstanding_definitions_index.md
DEC-019
DEC-038
DEC-055
DEC-059

The new core principle would be:

Competency Rank determines Dice Pool Size. Final Dice Pool Size determines Competency Floor. Boons and Banes modify Dice Pool Size and therefore automatically modify the Floor.

Before recording this change, we need to settle one precise point:

Should Legendary Competency use a natural 6dX pool to preserve Floor 9, or should the natural pool ceiling remain 5dX with Legendary power represented through Automatic Successes and Permissions?
