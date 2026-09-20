---
turn: 299
role: "AI-Designer"
source: chat_history.json
---

# Turn 299 — AI-Designer

I think this is substantially cleaner.

The new rule becomes:

Competency Rank determines baseline Dice Pool Size. Final Dice Pool Size determines Floor.

text
Competency Rank | Baseline Pool | Floor
Untrained       | 1dX           | 1
Trained         | 2dX           | 2
Expert          | 3dX           | 3
Master          | 4dX           | 4
Legendary       | 5dX           | 5

No separate Floor lookup table is needed.

Why This Is Better

The previous model had separate relationships:

text
Competency Rank → Pool Volume
Competency Rank → Floor
Banes → Pool Volume
Banes → Floor
Die Size → Floor Cap

The new model is:

text
Competency Rank → Baseline Pool Volume
Final Pool Volume → Floor

Then:

text
Boons add dice.
Banes remove dice.
Pool size automatically determines Floor.

This gives us a very clean mathematical relationship.

Example
text
Expert:
  3d8, Floor 3

+1 Enhancement Boon:
  4d8, Floor 4

+1 Circumstance Boon:
  5d8, Floor 5

+1 Bane:
  4d8, Floor 4

A Bane lowering the Floor is no longer a special rule. It follows automatically from removing a die.

Untrained Floor 1

I think Floor 1 is acceptable.

Since our ordinary DCs begin at DC 2, this means:

text
Untrained:
  Cannot automatically succeed against ordinary DCs.

It still provides a meaningful minimum result without making untrained characters automatically pass routine tests.

Equipment and External Investment

This model also makes equipment and external investment much easier to represent.

Example:

text
Trained character:
  2d8, Floor 2

Masterwork equipment:
  +1 Enhancement Boon
  3d8, Floor 3

Superior equipment:
  +2 Enhancement Boons
  4d8, Floor 4

Legendary equipment:
  +3 Enhancement Boons
  5d8, Floor 5

The equipment does not need a separate Floor rule. It expands the pool, and the Floor follows from the expanded pool.

This supports the intended design:

Character advancement, Skill Competency, equipment, spells, and temporary circumstances can all affect pool volume, while the Floor emerges from the final pool size.

Important Edge Case: Floor Above Die Size

There is one major implication we need to define.

Under this rule:

text
5d4 → Floor 5

But a d4 cannot roll a face of 5.

There are two possible interpretations.

Interpretation A — Floors may exceed die faces

A Floor is a final-result guarantee rather than a literal die face.

text
5d4, Floor 5

means the character cannot produce a final result below 5, even though the individual dice only show 1–4.

This would allow equipment and other external investment to create reliable success against low DCs without increasing the character’s numerical Die Size.

Interpretation B — Floor is capped by Die Size

The final Floor cannot exceed the die size.

text
5d4 → Floor 4

This preserves the idea that a character cannot achieve a result numerically above their Die Size without a Die Step-Up.

The first interpretation makes equipment exceptionally powerful and supports your idea that equipment can meaningfully expand baseline capability. The second preserves a stricter separation between:

text
Die Size:
  Numerical ceiling.

Pool Size:
  Reliability and Floor.

This is the main conceptual question created by the new model.

Bane Behavior Under the New Model

The Bane rule becomes very elegant:

text
5dX, Floor 5
+1 Bane
→ 4dX, Floor 4

4dX, Floor 4
+1 Bane
→ 3dX, Floor 3

3dX, Floor 3
+1 Bane
→ 2dX, Floor 2

2dX, Floor 2
+1 Bane
→ 1dX, Floor 1

1dX, Floor 1
+1 Bane
→ 1d(Die Step-Down), Floor 1

The Floor is based on number of dice, while the Die Step-Down affects the die size.

That means a Bane can reduce:

Reliability and Floor through die removal.
Numerical ceiling through a Die Step-Down.
But it cannot reduce the pool below one die.

This is much cleaner than the earlier system.

Boon Behavior

Boons similarly become direct:

text
1dX → Floor 1
2dX → Floor 2
3dX → Floor 3
4dX → Floor 4
5dX → Floor 5
6dX → Floor 6

Typed Boons remain useful because the types determine whether different external effects stack.

For example:

text
+1B Circumstance
+1B Enhancement
+1B Morale

produces:

text
+3 dice

and therefore raises the Floor by three.

Critical Interaction: Paired Defenses

We need to decide how the new pool-size Floor applies to paired defenses.

A standard paired defense is currently:

text
1dDEX + 1dINT keep highest

That is a two-die pool, so under the new rule it would naturally have:

text
Floor 2

Possible interpretation:

text
Fortitude:
  1dSTR + 1dCON
  2 dice total
  Floor 2

This seems consistent and probably desirable.

However, if the two Attributes have different die sizes:

text
1d8 + 1d12

the pool has:

text
2 dice
Floor 2

The Floor would be based on total dice, while the die sizes remain independently determined by the paired Attributes.

This means the glossary should eventually define:

For a mixed-die pool, Floor is based on the total number of rolled dice, not on the number of dice of each size.

Recommended New Universal Rule

The framework could state:

Final Pool Floor: The Floor of a check equals the final number of dice in its pool. Competency Rank establishes a baseline pool size, while Boons and Banes modify that size. The Floor is recalculated after all final pool-volume changes. Die Step-Up and Die Step-Down alter die size, not the number of dice. A pool cannot be reduced below one die.

Then we need one additional sentence deciding whether:

text
5d4 has Floor 5

or whether the Floor is capped at the final die size.

My Recommendation

I recommend adopting the new pool-to-Floor model, but keeping this one point open for explicit decision:

Should a Floor be allowed to exceed the face ceiling of the dice in the pool?

My initial preference is yes, because it gives equipment and external investment a powerful but simple role:

text
5d4, Floor 5

would mean:

The character is not numerically capable of rolling a natural 5 on any die.
But their total pool is sufficiently large and supported that the final check cannot fall below 5.
A Die Step-Up would still improve the ceiling to d6.
Equipment can improve reliability without automatically improving peak capability.

That creates a clean distinction:

text
Die Size:
  Peak numerical capability.

Pool Size:
  Reliability and minimum performance.

Floor:
  The minimum final result generated by that pool.

This is mathematically simple, but it does mean the Floor is no longer literally a die-face minimum. It becomes a pool-result Floor.

This appears to be a better foundational model than the previous Competency-specific Floor system. We should resolve the 5d4 → Floor 5 question before updating the canonical files.
