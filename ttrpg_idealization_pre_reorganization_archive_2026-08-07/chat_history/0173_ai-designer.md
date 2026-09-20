---
turn: 173
role: "AI-Designer"
source: chat_history.json
---

# Turn 173 — AI-Designer

Yes, the fundamental math is already substantially documented, although it is distributed across several files rather than consolidated into one mathematical framework document.

The important point is that our system is bounded by die faces, not by an ever-growing linear modifier scale.

1. Primary Mathematical Framework

The current core model is:

text
Check Pool = N dice of size X

Where:

X is primarily determined by Attribute Die Size.
N is primarily determined by Competency, Boons, Banes, class features, and tactical conditions.
The result is normally the highest rolled face.
The highest face is compared directly against a fixed DC or opposed roll.

Typical checks begin with:

text
2dX keep highest

The relevant resolution documentation is primarily in:

text
03_core_baseline_system/01_resolution_engine.md
03_core_baseline_system/06_check_pool_generation_and_class_differentiation.md
03_core_baseline_system/07_attributes_and_derived_statistics.md
06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md
2. Die-Size Ceiling

The ordinary Attribute Die progression is:

text
d4 → d6 → d8 → d10 → d12

This creates a hard ordinary face-value ceiling:

text
Maximum ordinary die face: 12

That means fixed DCs can remain within a stable range:

text
DC 2 through DC 12

The system does not need to create DCs such as:

text
DC 38
DC 52
DC 67

in order to represent higher-level challenges.

Instead, increased competency is represented through:

More dice.
Higher die size.
Competency Floors.
Boons.
Die Step-Ups.
Special permissions.
Equipment and feat effects.

This is one of the strongest mathematical differences from D&D 3.5e.

3. Comparison with D&D 3.5e

D&D 3.5e commonly produces numbers such as:

text
Attack bonus: +25
Armor Class: 38
Skill check: +42
Save DC: 31

The system’s mathematical range expands continuously through:

Base Attack Bonus.
Ability modifiers.
Skill ranks.
Enhancement bonuses.
Size modifiers.
Feats.
Circumstance modifiers.
Equipment bonuses.
Prestige-class features.
Temporary effects.

This produces powerful character-build depth, but also:

Large numerical spreads.
Significant level-based inflation.
Difficult encounter calibration.
“Rocket tag” at high levels.
Large differences between optimized and unoptimized characters.
Heavy table-side arithmetic.

Our system deliberately replaces that with bounded die sizes and discrete capability vectors.

4. Comparison with Pathfinder 2e

PF2e is a closer mathematical comparison.

PF2e uses:

Level-based proficiency.
Bounded proficiency categories.
Fixed or semi-fixed DCs.
Degree-of-success thresholds.
Four levels of proficiency.
Carefully controlled bonuses and penalties.
Strong level-based scaling.

However, PF2e still generally uses increasing numerical modifiers:

text
Level + proficiency + ability + item + circumstance/status effects

The effective target numbers and modifiers grow over the level range.

Our system is more strongly bounded at the face-value level:

text
Ordinary die faces: d4–d12
Ordinary DCs: 2–12
Pool ceiling: 5 dice

The comparison is therefore:

Feature	D&D 3.5e	Pathfinder 2e	Our System
Core resolution	d20 plus many modifiers	d20 plus bounded level modifiers	Step pools
Ordinary die ceiling	20, but modifiers expand heavily	20, with controlled modifier growth	d12 face ceiling
DC range	Expands dramatically	Expands by level	Normally 2–12
Competence scaling	Linear numerical bonuses	Proficiency and level bands	Die size, pool volume, Floors
Expertise difference	Often very large	Controlled but substantial	Strong and explicit
Table arithmetic	Heavy	Moderate	Intended to be zero
High-level behavior	Often swingy/rocket-tag	More stable	Bounded, with controlled spikes

So yes: the system is mathematically closer in spirit to PF2e’s bounded encounter calibration than to D&D 3.5e’s unbounded modifier ecosystem, but it is even more bounded at the resolution layer.

5. The Die-Pool Ceiling

The current pool-volume ceiling is:

text
Maximum normal pool: 5dX

This limits the number of dice that need to be rolled and prevents Boon stacking from producing absurd pools.

A character may therefore improve in two independent ways:

Increase the ceiling
text
d6 → d8 → d10 → d12

This determines the highest face they can naturally produce.

Increase reliability
text
2d8 → 3d8 → 4d8 → 5d8

This increases the chance of producing a high result without changing the maximum face.

This separation is mathematically important:

Attribute and Die Step-Up affect peak capability.
Competency and Boons affect reliability and multi-success potential.
6. Competency Floors

Competency Floors create deterministic lower bounds:

Rank	Floor
Untrained	0
Trained	3
Expert	5
Master	7
Legendary	9

This means a sufficiently trained character cannot fail below certain routine thresholds.

Examples:

text
Trained:
  Cannot fail below DC 3.

Expert:
  Cannot fail below DC 5.

Master:
  Cannot fail below DC 7.

Legendary:
  Cannot fail below DC 9.

This produces a very different mathematical feel from a d20 modifier system.

Instead of:

text
Roll 1d20 + 14

the character may have:

text
4d10 keep highest, Floor 7

The result is both:

Random within the relevant range.
Protected from implausibly poor outcomes.
7. Fixed DCs

The current fixed DC philosophy uses a small set of stable target bands.

Typical examples:

text
DC 2: Trivial
DC 3: Routine
DC 5: Challenging
DC 7: Formidable
DC 9: Heroic
DC 11: Legendary
DC 12: Extreme or near-cap

The exact labels are still subject to canonical consistency review, but the mathematical idea is stable:

The DC scale does not rise with Character Level in the same way that D&D 3.5e skill DCs and attack bonuses rise.

A Level 15 character may still roll against DC 7 for a difficult ordinary-world task. What changes is their probability of success and their ability to produce multiple successes.

8. Opposed Rolls

Opposed contests compare rolled faces rather than adding modifiers.

Example:

text
Attacker: 3d10 keep highest
Defender: 2d8 keep highest

The highest faces are compared directly.

Ties use a secondary comparison procedure.

This helps preserve uncertainty without requiring numerical attack bonuses and defense values that must remain within a narrow mathematical band.

9. Multi-Success Math

The system does not only ask whether the highest face succeeds.

Additional dice can also beat the target threshold.

Example:

text
Roll: 4, 8, 10, 12
Target: DC 7

This produces three successful faces:

text
8, 10, 12

Multi-success counts can produce:

Superior hits.
Overwhelming hits.
Maneuvers.
Called Shots.
Complex-task progress.
Faster completion.
Additional effects.

This gives higher dice pools a role beyond simply increasing the chance of one success.

10. Over-Cap and Mythic Values

There is one qualification to the “d12 ceiling” statement.

The design currently permits values beyond ordinary d12 through:

text
d12+1
d12+2

These are intended for:

Heroic.
Legendary.
Mythic.
Exceptional Attribute progression.
Over-cap capability.

This means the strict ceiling is:

text
Ordinary ceiling: d12
Exceptional ceiling: d12+

That is still much more bounded than D&D 3.5e, but the over-cap rules need careful definition.

We should decide whether d12+1 and d12+2 mean:

A literal expanded face range.
A special threshold result.
An additional die step that changes probability but not the face maximum.
A Mythic-only exception.
A controlled automatic success or multi-success effect.

Until that is defined, the mathematical ceiling is best described as:

d12 for ordinary play, with explicitly exceptional over-cap values reserved for high-tier and Mythic mechanics.

11. Equipment and Mathematical Scaling

This is one of the major areas that still needs foundational work.

The framework intends equipment to improve characters through discrete vectors such as:

Weapon Damage Die Step-Up.
Damage Absorption Die Step-Up.
Durability Slots.
Weapon Traits.
Armor Traits.
Boons or Banes in specific circumstances.
Penetration or resistance keywords.
Action permissions.
Critical-threat profiles.

Equipment should not simply provide:

text
+1 attack
+3 damage
+5 armor

The outstanding design problem is to determine how equipment progression interacts with the bounded dice framework without recreating D&D 3.5e’s escalating numerical treadmill.

This is now explicitly included in PROJECT_STATUS.md as framework work.

12. What Is Already Mathematically Stable?

The strongest established mathematical principles are:

Fixed DC range.
Bounded ordinary die sizes.
Limited pool volume.
Separate peak capability and reliability vectors.
Competency Floors.
Opposed roll comparison.
Multi-success outcomes.
No linear modifiers.
Explicit resource-driven Die Step-Ups.
Separate ordinary and Mythic escalation.
13. What Still Needs Mathematical Definition?

The major unresolved mathematical areas are:

Exact probability targets for every Attribute Die and Competency Rank.
Final interpretation of over-cap d12+ values.
Equipment scaling.
Weapon damage and Damage Absorption calibration.
Spell-slot volume and daily resource pressure.
Essence pool size and recovery.
Mediocre and Bad class advancement balance.
Mythic probabilities and capability ceilings.
Monster scaling relative to PC pools.
Wealth-by-level and equipment acquisition expectations.

So the short answer is:

Yes. The system has a bounded mathematical core more comparable to PF2e’s controlled progression than D&D 3.5e’s escalating modifier math. Its ordinary resolution ceiling is d12 against DCs up to 12, with pool volume, Floors, and discrete traits providing differentiation. The remaining work is to define how equipment, over-cap Mythic values, resources, spells, and wealth interact with that bounded foundation.
