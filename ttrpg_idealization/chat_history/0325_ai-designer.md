---
turn: 325
role: "AI-Designer"
source: chat_history.json
---

# Turn 325 — AI-Designer

used
Bash
88ms

This is a very interesting idea. It would give us a difficulty vector rather than a single Target Number plus a count of Required Successes.

Instead of:

text
DC 5 (2)

we would write:

text
DC 5,4

meaning:

The two highest applicable dice must produce one result of at least 5 and another result of at least 4.

1. How the Check Would Work

The cleanest procedure would be:

Roll the final Dice Pool.
Sort the results from highest to lowest.
Sort the DC requirements from highest to lowest.
Compare them positionally.

Example:

text
Pool:
  8, 6, 3

Difficulty:
  DC 5,4

Compare:

text
8 ≥ 5
6 ≥ 4

The check succeeds.

The third die is not needed.

Another example:

text
Pool:
  8, 3, 2

Difficulty:
  DC 5,4

Compare:

text
8 ≥ 5
3 < 4

The check fails.

2. Same-Threshold DCs

The current system becomes a special case of the vector model.

text
DC 5 (2)

becomes:

text
DC 5,5

Similarly:

text
DC 7 (3)

becomes:

text
DC 7,7,7

This is useful because it preserves the existing Required Success system as a shorthand.

text
DC 5 (2) = DC 5,5
DC 7 (3) = DC 7,7,7
3. Mixed Thresholds Create More Granularity

For a 3d8 pool:

text
DC 5,5
DC 5,4
DC 5,3
DC 4,4
DC 6,5

are all distinct difficulties.

Using raw 3d8 probabilities:

Difficulty	Probability
DC 5,5	50.00%
DC 5,4	66.41%
DC 5,3	78.13%
DC 4,4	68.75%
DC 6,5	47.46%

This creates much denser probability steps than simply choosing between:

text
DC 5 (1)
DC 5 (2)
DC 6 (1)

It also gives us a way to distinguish “one very difficult component plus one moderate component” from “two equally difficult components.”

4. Why This May Produce Smoother Curves

With ordinary DC X (Y), the difficulty changes in large chunks:

text
DC 5 (1)
DC 5 (2)
DC 6 (1)

With vectors, we get intermediate requirements:

text
DC 5,5
DC 5,4
DC 5,3
DC 4,4
DC 6,5
DC 6,4

This lets us tune tasks much more precisely.

For example, with 3d8:

text
DC 5,5  → 50.00%
DC 5,4  → 66.41%
DC 5,3  → 78.13%

Those are much more useful calibration steps than jumping directly from roughly 50% to roughly 78%.

5. Interaction with Floors

This approach interacts elegantly with the pool-size Floor.

Suppose:

text
3d8, Floor 3

Then any individual requirement of 3 or lower is automatically satisfied.

For example:

text
DC 5,3

becomes effectively:

text
DC 5

because the second requirement is guaranteed by the Floor.

That means the same difficulty vector can have very different practical difficulty depending on the character’s pool and Floor.

This may be exactly what we want:

text
Novice:
  DC 5,3 still requires two meaningful achievements.

Expert:
  DC 5,3 may only require one meaningful achievement.

Master:
  DC 5,3 may be entirely routine.
6. Your Example

Your illustrative row:

text
Trained, Level 1, d8, 3d8, Floor 3
Easy:   DC 5
Medium: DC 5,4
Hard:   DC 5,5

would mean:

Easy: One die must reach 5.
Medium: One die must reach 5 and another must reach 4.
Hard: Two dice must each reach 5.

Using raw 3d8:

text
DC 5:
  87.50%

DC 5,4:
  66.41%

DC 5,5:
  50.00%

With Floor 3, those same probabilities remain unchanged because all requirements exceed the Floor.

That is a very attractive progression.

7. Sorting and Assignment Rule

We should probably make the requirements unordered at the table.

text
DC 5,4

and:

text
DC 4,5

should mean the same thing.

The procedure would sort both:

text
Highest die ↔ Highest requirement
Second-highest die ↔ Second-highest requirement

This avoids asking players to choose which die satisfies which requirement.

8. How Many Requirements Can a Difficulty Have?

The difficulty vector can have as many requirements as the task needs:

text
DC 5
DC 5,4
DC 5,5
DC 6,5,4
DC 7,6,5
DC 8,7,6,5

The character needs at least as many relevant dice as requirements.

A pool of 3d8 cannot fully resolve:

text
DC 6,5,4,3

unless the system allows extra dice from equipment, Boons, or other effects.

That creates a natural interaction between:

Pool Size.
Equipment.
Competency.
Task complexity.
Difficulty vectors.
9. Equipment Interaction

This model makes equipment Boons especially interesting.

Suppose:

text
Unmodified:
  3d8

Equipped:
  5d8

The equipment does not merely increase the chance of one success. It allows the character to satisfy more requirements simultaneously.

text
3d8:
  Can attempt DC 6,5,4

5d8:
  Can attempt DC 6,5,4,3,3

This lets equipment represent:

Better precision.
Better tools.
Better reach.
More reliable execution.
Ability to handle complex tasks.
More simultaneous successes.
10. Relationship to Existing DC X (Y)

We could retain both notations:

text
DC 5 (2)

as shorthand for:

text
DC 5,5

and use mixed vectors for more precise tasks:

text
DC 5,4
DC 6,5,4

This gives us a simple default and a more granular advanced notation.

Alternatively, we could replace the old notation entirely:

text
DC 5,5
DC 5,4
DC 6,5,4

I would initially retain the shorthand because it is easier to read for ordinary challenges.

11. Important Difference from “Keep Highest N”

This should not be called:

text
3d8 keep highest 2

because that normally means “roll three dice and keep the two highest,” not “compare two kept dice against two different thresholds.”

The more precise procedure is:

text
Roll 3d8.
Sort the results.
Compare the highest two results to the difficulty vector.

The mechanic is better described as:

text
Difficulty Vector
Threshold Vector
Multi-Threshold Difficulty

My preferred notation is still:

text
DC 5,4

with the rule that the values are sorted from highest to lowest.

12. Main Advantages

This system would provide:

More granular probability control.
Better modeling of complex tasks.
Natural support for multiple objectives.
Strong interaction with pool size.
Better equipment differentiation.
A more expressive use of Required Successes.
A way for higher pools to matter beyond simple pass/fail reliability.
A natural bridge between fixed DCs and multi-success challenges.
13. Main Risks

The main risks are:

More complicated difficulty notation.
More difficult GM adjudication.
More complex probability matrices.
Potential confusion about automatic Floors.
More difficult opposed-roll implementation.
A large number of possible vectors.
Potential for difficulty vectors to become “secret modifier math” if overused.

We should probably reserve mixed vectors for:

Complex tasks.
Multi-stage activities.
High-tier challenges.
Combat maneuvers.
Spells with multiple components.
Equipment or crafting procedures.
Recommendation

I think this is worth exploring seriously.

The next research artifact should contain matrices for:

text
3d8:
  DC A,B probabilities

4d8:
  DC A,B probabilities

5d8:
  DC A,B probabilities

6d10:
  DC A,B probabilities

8d10:
  DC A,B probabilities

9d12:
  DC A,B probabilities

10d12:
  DC A,B probabilities

Then we can compare whether the vectors produce smoother Easy/Medium/Hard bands than the existing DC X (Y) model.

The most promising provisional structure is:

text
DC X:
  One threshold.

DC X (Y):
  Shorthand for Y identical thresholds.

DC X,Y:
  Two possibly different thresholds.

DC X,Y,Z:
  Three possibly different thresholds.

This may provide the granularity we were looking for without abandoning the bounded die and pool framework.
