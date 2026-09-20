---
turn: 177
role: "AI-Designer"
source: chat_history.json
---

# Turn 177 — AI-Designer

Phase 1 — Fundamental Math
Pending Definitions and Current Decisions

Phase 1 should establish the mathematical behavior of the universal resolution engine before we expand combat, equipment, magic, or content.

The following is the current inventory.

1. Attribute Die Ladder
Status: Provisional / Mostly Established

Current ordinary Attribute Die ladder:

text
d4 → d6 → d8 → d10 → d12

Attributes determine the base die size of a check.

Current Attributes:

text
STR, DEX, CON, INT, WIS, CHA
Existing decisions
Attributes determine Die Size, not linear modifiers.
The ordinary maximum die is d12.
Attributes are independent from Competency Ranks.
Background Primary Attribute begins at d8.
Primary Attribute automatically advances at Levels 5, 9, 15, and 20.
Secondary Attribute Step Points are awarded at Levels 4, 8, 12, 16, and 20.
Still pending
Exact meaning of d12+1 and d12+2.
Whether over-cap dice use literal expanded faces or special resolution rules.
Whether d4 should be the minimum for all actors or whether some checks can use an absolute floor of zero.
Whether all six Attributes use identical mathematical scaling.
Whether monster Attributes may begin above d12.
2. Base Check Pool
Status: Locked in principle

Current baseline:

text
2dX keep highest

Where:

X comes from the relevant Attribute Die.
The highest face is normally compared against the DC or opposing result.
Existing decisions
Base checks use step pools.
No arithmetic modifiers are added to the result.
The default pool is two dice.
The highest face normally determines the check result.
The same core engine applies to skills, attacks, spells, defenses, and other checks.
Still pending
Whether every check begins at 2dX, or whether some systems begin at 1dX.
How damage rolls differ from ordinary action checks.
Whether certain large or small creatures use different base pool volumes.
Whether opposed checks compare only the highest face or also use secondary dice in a formal order.
3. Pool Volume
Status: Mostly locked

Pool volume represents reliability, training, Boons, and tactical advantages.

Current model:

text
2dX base pool
3dX with +1B
4dX with +2B
5dX with +3B
Existing decisions
Boons add dice of the same size.
Maximum normal pool is 5dX.
Pool volume is separate from Die Size.
Pool volume is separate from Competency Floor.
Classes, feats, tactics, positioning, and equipment may affect pool volume through discrete Boons.
Still pending
Exact conversion when Boons exceed the 5dX ceiling.
Whether excess Boons cause a Die Step-Up, secondary action, automatic multi-success, or another effect.
Exact stacking limits for class, feat, equipment, and situational Boons.
Whether different check categories have different pool ceilings.
Whether Banes can reduce a pool below 1dX.
4. Competency Ranks
Status: Locked in principle

Current Competency Ranks:

Rank	Pool/Floor Effect
Untrained	Base pool, Floor 0
Trained	+1B, Floor 3
Expert	+1B, +1 Die Step-Up, Floor 5
Master	+2B, +2 Die Steps-Up, Floor 7
Legendary	+3B, +3 Die Steps-Up, Floor 9
Existing decisions
Competency Ranks are:
Untrained.
Trained.
Expert.
Master.
Legendary.
Competency is independent from Character Level.
Competency determines:
Pool volume.
Competency Floor.
Skill reliability.
Spell Tradition scaling.
Skills are individually ranked.
Classes may automatically advance primary combat or magical skills.
General investment can advance other Skills and Traditions.
Still pending
Exact interpretation of multiple Die Step-Ups at or beyond d12.
Whether every Skill uses the same rank-to-pool formula.
Whether attacks, defenses, Traditions, and Craft specialties use identical Competency Rank effects.
Whether monsters use the same five ranks or simplified equivalents.
Whether Legendary is the true maximum for mortal characters.
5. Competency Floors
Status: Locked in principle; calibration still needed

Current Floors:

text
Untrained: 0
Trained: 3
Expert: 5
Master: 7
Legendary: 9
Existing decisions
A Floor replaces results below the character’s minimum guaranteed result.
Floors prevent trained characters from failing routine tasks.
Floors are separate from Attribute Die Size.
Floors are separate from pool volume.
Still pending
Whether Floors apply to:
All ordinary checks.
Opposed checks.
Damage rolls.
Initiative.
Defense rolls.
Spellcasting.
How Floors interact with natural failures.
Whether conditions can temporarily lower or suppress a Floor.
Whether an opponent’s Floor affects opposed contests symmetrically.
How Floors interact with d12+ values.
6. Fixed DC Scale
Status: Framework locked; labels and calibration open

Current DC range:

text
DC 2 through DC 12

Approximate working categories:

text
DC 2: Trivial
DC 3: Routine
DC 5: Challenging
DC 7: Formidable
DC 9: Heroic
DC 11: Legendary
DC 12: Extreme
Existing decisions
DCs remain within a bounded range.
The ordinary die ceiling is d12.
Challenges do not scale into D&D 3.5e-style DCs of 30, 45, or 60.
Difficulty is represented through:
DC.
Required Successes.
Opposed pools.
Conditions.
Time pressure.
Resource costs.
Still pending
Final names for DC bands.
Whether DC 12 is achievable without d12 or d12+.
Whether DC 2 is the universal minimum or merely the lowest normal DC.
Whether special Mythic challenges can exceed DC 12.
Exact GM guidance for assigning DCs.
Whether task difficulty should use DC + required successes rather than additional DC values.
7. Opposed Rolls
Status: Mostly established; procedure needs formalization

Opposed checks compare rolled faces directly.

Example:

text
Attacker: 3d10 keep highest
Defender: 2d8 keep highest
Existing decisions
No attack bonus or defense modifier is added.
The higher opposed face wins.
Ties require a secondary tiebreaking procedure.
Active defenses can consume Stamina.
Opposed checks can generate multi-success outcomes.
Still pending
Exact tie-break procedure.
Whether the secondary die is always compared or only when highest faces tie.
How Floors function in opposed rolls.
How multi-success counts are calculated in opposed contests.
Whether the winner’s margin matters in addition to success count.
How opposed social, magical, and physical checks differ, if at all.
8. Boons and Banes
Status: Mostly locked; stacking rules open

Current terminology:

text
+1B, +2B, +3B
+1X, +2X, +3X
Existing decisions
Boons add dice of the same size.
Banes remove dice or force worse results.
Mixed-size Boon dice are rejected.
Mixed-size Step-Up/Step-Down pools are rejected.
Maximum pool volume is normally 5dX.
Still pending
Exact Banes procedure at each level.
Whether:
2d8 +1X becomes 1d8.
2d8 +2X becomes 2d8 keep lowest.
What happens with 3+ Banes.
Whether Boons and Banes cancel one-for-one before rolling.
Whether some effects impose a Die Step-Down instead of a Bane.
How advantage-like effects interact with Floors.
9. Die Step-Up and Die Step-Down
Status: Terminology locked; mechanical boundaries partly open

Current terminology:

text
Die Step-Up
Die Step-Down

Up-Shift: d8 → d10
Down-Shift: d10 → d8
Existing decisions
The old “Hyper-Shift” terminology is deprecated.
Die Step-Up increases the Die Size.
Die Step-Down decreases the Die Size.
Die Step-Up is a discrete alternative to numerical bonuses.
Stamina may fuel physical Die Step-Ups.
Essence may fuel magical or supernatural Die Step-Ups.
The ordinary Attribute ladder ends at d12.
Still pending
Exact cost of each Stamina-driven Die Step-Up.
Exact cost of Essence-driven Die Step-Ups.
Maximum number of Step-Ups in one action.
Whether a Step-Up applies to:
One die.
The whole pool.
Damage only.
An attribute for the duration of a scene.
Exact handling of d12+.
Whether a Die Step-Up can overcome a condition-imposed Step-Down.
Whether multiple Step-Ups can cancel multiple Step-Downs.
10. Stamina and Essence as Mathematical Modifiers
Status: Resource distinction established; costs open
Stamina

Used for:

Physical exertion.
Active defense.
Martial surges.
Physical Die Step-Ups.
Forced movement or overextension.
Essence

Used for:

0th-Circle spells.
Metamagic.
Casting stability.
Emergency casting.
Supernatural class features.
Future Psychic/Psionic disciplines.
Existing decisions
Stamina and Essence are separate.
Neither is a meta-currency.
Both are in-world character resources.
They may alter the check procedure without adding numerical modifiers.
Still pending
Exact Stamina derivation and recovery.
Exact Essence derivation and recovery.
Cost for each type of Die Step-Up.
Whether Essence can be used for ordinary skill checks.
Whether resource expenditure changes pool volume, Die Size, Floor, action cost, or consequence.
What happens when Stamina or Essence reaches zero.
11. Multi-Success Resolution
Status: Framework established; calibration open

Current structure:

text
1 Success:
  Standard result.

2 Successes:
  Superior result or one maneuver.

3+ Successes:
  Overwhelming result, two maneuvers, or Called Shot.
Existing decisions
[SET] tokens were removed.
Multi-success results replace token accumulation.
Additional successful faces in the pool can matter.
Combat maneuvers are universal.
Called Shots are distinct from Natural Crits.
Still pending
Exact definition of a “success” in opposed checks.
Whether every die exceeding a fixed DC counts.
How many successes complex noncombat tasks require.
Whether required-success thresholds are always 1–4+.
How multi-success results interact with Floors.
Whether Boons increase success count or merely success probability.
12. Probability Calibration
Status: Open / Active Phase 1 work

Existing target ranges include:

Routine actions should be highly reliable for trained characters.
Equal-tier checks should not be automatic.
Expert and Master characters should dominate lower-tier tasks.
Crits should remain meaningful but not constant.
Combat should average roughly 3–5 rounds.
Underlings should resolve faster.
Existing research

Probability and combat simulations exist in:

text
06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md
06_brainstorming_logs_and_roadmap/sim_*.py
02_comparative_system_analysis/04_mathematical_calibration_and_ttk_vectors.md
Still pending
A consolidated probability table for:
2d4 through 5d12.
Each Floor.
Each DC.
Each Boon/Bane level.
Each Die Step-Up.
Exact target probabilities for every competency rank.
Equal-tier opposed-roll win rates.
Multi-success probability curves.
Probability of automatic failure or success.
Probability impact of d12+ values.
13. Critical Probability
Status: Framework established; exact calibration open

Current system:

Weapons have a d100 Critical Threat Profile.
Standard, Keen/Finesse, and Heavy weapon profiles differ.
Natural Crits deal increased Vitality loss.
Natural Crits roll on a random anatomical matrix.
Called Shots do not deal double damage.
Still pending
Final Critical Threat Profile percentages.
Whether criticals are checked on every attack or only successful attacks.
Whether spell attacks use the same critical system.
How criticals interact with multi-success results.
Whether equipment can modify threat profiles.
Whether monsters use the same profiles.
14. Damage and Combat Math
Status: Phase 3; framework exists, calibration pending

Current concepts:

Vitality.
Damage Dice.
Damage Absorption Dice.
Wound conditions.
Critical damage.
Called Shots.
Armor and shield defenses.
Weapon Traits.
Existing decisions
Damage Absorption is not a linear reduction value.
Damage is compared against an Absorption Die or defensive result.
Wounds and conditions replace some abstract HP consequences.
Equipment should not scale through flat +1, +2, or +5 bonuses.
Still pending
Exact damage-versus-Absorption procedure.
Whether damage uses the same pool engine as attacks.
Weapon Damage Die progression.
Armor/Damage Absorption progression.
How damage interacts with multiple successes.
Exact equipment scaling.
High-level damage and defense calibration.

This is adjacent to Phase 1 but probably belongs primarily in Phase 3 after the core check math is stable.

15. Equipment Math
Status: Open; Phase 2/3

The framework intends equipment to improve capability through discrete vectors:

Damage Die.
Damage Absorption Die.
Durability Slots.
Weapon Traits.
Armor Traits.
Critical Threat Profiles.
Penetration.
Action permissions.
Special materials.
Still pending
Exact relationship between equipment and Attribute Die Size.
Whether equipment can cause Die Step-Ups.
Whether equipment can grant Boons.
How magical enhancement works without linear bonuses.
Expected equipment progression by level.
Wealth-by-level guidance.
Equipment replacement and repair assumptions.
16. Mathematical Ceiling and d12+
Status: Ordinary ceiling established; over-cap rules open

Current ordinary ceiling:

text
d12

Current exceptional values:

text
d12+1
d12+2
Existing decisions
Ordinary play is bounded by d12.
DCs normally remain between 2 and 12.
Mythic and exceptional characters may exceed ordinary limits.
Still pending
Whether d12+ values are:
Expanded face ranges.
Automatic success thresholds.
Additional success effects.
Mythic-only exceptions.
Whether d12+ changes damage and defense identically.
Whether d12+ is available before Mythic advancement.
How probability tables handle over-cap values.
Phase 1 Priority Order

The most useful order for resolving these questions is:

Finalize the ordinary die ladder and d12+ policy.
Finalize the base pool and pool ceiling.
Finalize Boon and Bane procedures.
Finalize Die Step-Up and Die Step-Down boundaries.
Finalize Competency Floors.
Formalize opposed-roll ties and multi-success counting.
Build consolidated probability tables.
Validate DC categories and competency target probabilities.
Record the mathematical assumptions that Phase 2 and Phase 3 must use.

The most important unresolved Phase 1 issues are therefore:

text
What exactly do d12+ values mean?

How exactly do Banes work?

How are opposed ties and multi-success results resolved?

What are the final probability targets?

What is the exact cost and limit of resource-driven Die Step-Ups?

How do all of these interact without exceeding the intended bounded math?
