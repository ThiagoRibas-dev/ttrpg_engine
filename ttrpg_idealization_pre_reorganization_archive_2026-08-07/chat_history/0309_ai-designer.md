---
turn: 309
role: "AI-Designer"
source: chat_history.json
---

# Turn 309 — AI-Designer

I think the second progression is the stronger framework.

It creates a very intuitive alignment:

High Fantasy Tier	Full-investment Competency Rank	Baseline Pool	Base Floor
Trained	Trained	2 dice	2
Veteran	Veteran	3 dice	3
Master	Master	4 dice	4
Hero	Hero	5 dice	5
Legend	Legend	6 dice	6

That makes the natural progression immediately understandable:

text
Tier of play ≈ expected maximum Competency Rank

A character can still be lower-ranked in secondary Skills, but the framework’s “ideal investment” benchmark aligns with the character’s current Tier.

Comparison of the Two Models
Model A: Existing Rank Names and Delayed Breakpoints
text
Level 1: Trained
Level 6: Expert
Level 11: Master
Level 16: Legendary
Advantages
Preserves familiar terminology.
Keeps Competency Rank clearly distinct from High Fantasy Tier.
Produces fewer rank transitions.
Leaves more room between rank breakpoints.
Disadvantages
Rank names do not intuitively correspond to the character’s Tier.
A Veteran character with full investment is still only Expert.
A Hero character with full investment is only Master until Level 16.
The relationship between Tier, Skill investment, and pool size requires explanation.
It creates a potential sense that full skill investment is lagging behind the narrative tier.
Model B: Tier-Aligned Competency Names and Breakpoints
text
Level 1: Trained
Level 5: Veteran
Level 9: Master
Level 13: Hero
Level 17: Legend
Advantages
Very intuitive.
Matches the four-level High Fantasy bands.
Provides a clear full-investment benchmark.
Makes pool-size progression easy to remember.
Makes the probability-calibration tables easier to organize.
Produces a clean relationship between:
Character Tier.
Ideal Competency Rank.
Baseline Dice Pool.
Base Floor.
Disadvantages
Changes our existing rank names:
Expert → Veteran.
Legendary → Legend.
Tier and Competency Rank will use the same vocabulary.
We need to state clearly that Competency Rank remains independent from Character Level.
“Legend” and “Legendary” may need careful differentiation if both appear in older material.
A Level 20 character can still be Trained in a secondary Skill, which may initially confuse readers.
The Symmetry Is Valuable

The second model gives us a clean ideal progression:

text
Level 1:
  Trained Tier
  Trained Competency
  2dX
  Floor 2

Level 5:
  Veteran Tier
  Veteran Competency
  3dX
  Floor 3

Level 9:
  Master Tier
  Master Competency
  4dX
  Floor 4

Level 13:
  Hero Tier
  Hero Competency
  5dX
  Floor 5

Level 17:
  Legend Tier
  Legend Competency
  6dX
  Floor 6

This is extremely useful for probability calibration because it gives us five representative full-investment profiles.

Important Clarification: Competency Still Remains Independent

The symmetry should describe the ideal full-investment progression, not a universal level gate.

For example:

text
Level 17 Wizard:
  Character Tier: Legend
  Arcane Competency: Legend
  Heavy Blades Competency: Untrained
  Diplomacy Competency: Trained
  Craft — Scribing Competency: Veteran

The character’s Tier does not automatically make every Skill Legendary.

Likewise:

text
Level 6 character:
  Character Tier: Veteran
  Primary Skill: Veteran Competency
  Secondary Skill: Trained Competency

This is exactly the distinction you described.

Recommended Terminology

If we adopt the second model, I suggest using:

text
Character Tier:
  Trained, Veteran, Master, Hero, Legend, Mythic

Competency Rank:
  Untrained, Trained, Veteran, Master, Hero, Legend

This is understandable but has one ambiguity: “Trained” is both a Tier and a Competency Rank.

That may be acceptable because the context is usually clear:

text
Trained Tier
Trained Competency

Veteran Tier
Veteran Competency

Alternatively, we could call the second category:

text
Competency Tier

rather than Competency Rank:

text
Character Tier: Veteran
Competency Tier: Veteran

But Competency Rank is useful terminology because it emphasizes investment rather than level. I would retain it unless playtesting shows the shared vocabulary causes confusion.

Pool and Floor Consequences

Under the new model:

text
Untrained:
  1dX, Floor 1

Trained:
  2dX, Floor 2

Veteran:
  3dX, Floor 3

Master:
  4dX, Floor 4

Hero:
  5dX, Floor 5

Legend:
  6dX, Floor 6

The final Floor remains capped by the final Die Size:

text
Floor = min(number of dice, die size − 1)

Examples:

text
Legendary Competency with d12:
  6d12, Floor 6

Legendary Competency with d4:
  6d4, Floor 3

This is a clean result:

Pool volume determines the base Floor.
Die Size determines the maximum possible Floor.
Equipment and Boons may increase pool volume.
Banes reduce pool volume and therefore Floor.
Die Step-Downs reduce the Floor cap by reducing Die Size.
My Recommendation

I recommend adopting the second, Tier-aligned model:

text
Untrained: 1dX, Floor 1
Trained: 2dX, Floor 2
Veteran: 3dX, Floor 3
Master: 4dX, Floor 4
Hero: 5dX, Floor 5
Legend: 6dX, Floor 6

with full-investment breakpoints at:

text
Levels 1, 5, 9, 13, and 17

This gives us:

Better nomenclature symmetry.
Better probability-calibration benchmarks.
Simpler explanations.
A natural connection between Tier, investment, pool volume, and Floor.
A clear reason for a character to specialize in certain Skills while remaining mediocre or untrained elsewhere.

The main decision still requiring explicit approval is whether we should officially rename the existing competency ranks:

text
Expert → Veteran
Legendary → Legend

and adopt the Tier-aligned progression as the canonical Competency framework.
