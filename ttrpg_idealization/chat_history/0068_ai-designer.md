---
turn: 68
role: "AI-Designer"
source: chat_history.json
---

# Turn 68 — AI-Designer

Edited files
13
Simulationist Defense Architecture & Damage Modeling
MD
Simulationist Defense Architecture & Damage Modeling

In our idealized system, resolving an attack does not rely on comparing a single 
𝑑
20
d20 roll against an abstract Armor Class number. Instead, combat resolution respects the physical reality of an attack’s trajectory, momentum, and impact across Four Defensive Layers.

1. The Four Defensive Layers

When an incoming attack or threat is declared against an actor, check the layer appropriate to the attack's nature:

text
                      [ Incoming Attack / Threat Declared ]
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
    [ Physical Kinetic Strike ]                 [ Magical / Internal Threat ]
              │                                         │
     ┌────────┴────────┐                       ┌────────┴────────┐
     ▼                 ▼                       ▼                 ▼
[ Reflexes Layer ] [ Parry Layer ]      [ Fort / Will ]   [ Absorption Layer ]
 (DEX+INT Dodge)    (Melee Clash)       (Paired Saving)    (Armor Step Die)
1.1 Layer 1: Reflexes (DEX+INT-Derived Dodge Pool)
Used Against: Ranged weapon projectiles (arrows, bolts, thrown spears), area explosions (Fireball, Alchemical Bomb), and sweeping environmental hazards.
Mechanic: The attacker rolls their ranged or spell check pool. The defender rolls their Reflexes Pool (1dDEX + 1dINT keep highest).
If Attacker Highest 
≥
≥ Defender Highest: The projectile/blast lands (Hit $\to$ Check Damage Absorption).
If Attacker Highest < Defender Highest: The defender dodges cleanly (Miss / 0 Impact).
1.2 Layer 2: Parry (Combat Mastery Intercept)
Used Against: Melee weapon strikes (swords, axes, polearms, unarmed brawling).
Mechanic: If the defender has Raised Guard ([1A]) or spends 1 Stamina ([1R]) to react, they make an opposed Parry Check using their Combat Mastery pool (3dX to 5dX).
If Defender Highest 
≥
≥ Attacker Highest: The weapon is deflected or parried cleanly (0 Impact). If the defender rolls 2+ Successes on Parry, they can instantly trigger Riposte or Disarm.
If Attacker Highest > Defender Highest: The attack breaks past the parry (Hit $\to$ Check Damage Absorption).
1.3 Layer 3: Damage Absorption (Armor & Physical Hide Step — ABS)
Used Against: Any physical or kinetic attack that beats Reflexes or Parry.
Mechanic: Damage Absorption is checked post-hit. Every piece of armor provides an Absorption Step Die (ABS) (d4 Cloth 
→
→ d12 Full Plate). Compare Weapon Damage Die Face vs Absorption Die Face.
2. Mathless Damage & Wound Resolution (Damage vs Absorption)

In traditional d20 games, damage resolution involves subtracting armor damage reduction (DR) from rolled HP (8 damage - 3 DR = 5 HP lost). We eliminate subtraction entirely by comparing the Attacker's Damage Die Face against the Defender's Absorption Die Face (ABS):

Impact Check: 
max
⁡
(
Weapon Damage Die Faces
)
 vs 
max
⁡
(
Absorption Die Faces
)
Impact Check: max(Weapon Damage Die Faces) vs max(Absorption Die Faces)

2.1 The Mathless Damage & Wound Matrix (DEC-034 & DEC-044)
Damage Die vs Absorption Die (ABS)	Physical Outcome (Vitality vs Wounds)
Damage Face < Absorption Face	Absorbed (0 Wounds): The armor or thick hide absorbs the kinetic impact. The defender loses 1 Stamina due to jarring vibration, but suffers zero physical tissue damage (No HP loss).
Damage Face == Absorption Face	Superficial Impact (Minor Shock): The blow bruises tissue through the armor. The defender loses 2 Stamina (or 2 Vitality if Stamina is 0), but takes zero anatomical wounds.
Damage Face > Absorption Face<br>(Normal Non-Crit Hit)	Standard Hit (Vitality Loss & Quick Disruption): The strike bludgeons through armor. The defender loses Vitality (HP) equal to the Damage Die face shown. If the attack generated 2+ Successes (Multi-Beat), can inflict a quick disruption (Trip, Disarm, Shaken). Does not inflict anatomical severe wounds.
Natural Critical Hit (d100 Check)	Natural Critical (Double Vitality + Random 1d8 Matrix): The strike penetrates deep into random vital anatomy. The defender loses Double Vitality (Max Damage Face x 2) AND immediately rolls 1d8 on our Anatomical Matrix below!
Called Shot Maneuver (Chosen Target)	Called Shot (Standard Vitality + Chosen Anatomical Wound): Executed via 3+ Successes (or +1 Bane trade-off). Does NOT deal double damage (deals normal shown/rolled Damage Face vs Absorption), BUT the attacker CHOOSES the exact anatomical body part targeted (Head, Chest, Arm, Leg) and triggers that location's severe Anatomical Wound Condition (Concussion, Dropped Weapon, Prone)!
3. Armor Taxonomy & Absorption Step Table

Different armor categories provide distinct trade-offs between physical Absorption Step Ranks (ABS), Reflexes Banes (due to bulk and weight), and Durability Slots.

Armor Category	Absorption Step Die (ABS)	Reflexes / Agility Modifier	Durability Slots	Tactical Role
Unarmored / Clothing	ABS d4	Normal (0 Banes)	0	High mobility, spellcaster baseline.
Light Armor (Leather/Hide)	ABS d6	Normal (0 Banes)	1	Skirmishers, rogues, rangers (ABS d6).
Medium Armor (Chain/Scale)	ABS d8	
+
1
 Reflexes Bane Die (‘-1 die volume‘)
+1 Reflexes Bane Die (‘-1 die volume‘)	2	Balanced infantry, warriors (ABS d8).
Heavy Plate Armor	ABS d10	
+
2
 Reflexes Bane Dice (‘Keep lowest‘)
+2 Reflexes Bane Dice (‘Keep lowest‘)	3	Frontline juggernauts; almost immune to d6 weapons without crits (ABS d10).
Adamantine / Mythic Plate	ABS d12	
+
2
 Reflexes Bane Dice (‘Keep lowest‘)
+2 Reflexes Bane Dice (‘Keep lowest‘)	4	Legendary defensive bastion (ABS d12).
4. Layer 4: Resilience (Fortitude & Willpower Paired Pools)

When targeted by non-kinetic or internal threats (poisons, disease, mind blasts, petrification, divine curses), physical Reflexes and armor Absorption are irrelevant (ABS = 0 vs Mind Blast).

Opposed Resilience Check: The caster or hazard rolls its Power Pool (3dX to 5dX) against the defender's appropriate Resilience pool:
Physical Threats (Poisons, Disease, Petrification): Defender rolls their Fortitude Pool (1dSTR + 1dCON keep highest + Class Boons).
Mental & Spiritual Threats (Mind Control, Fear, Curses): Defender rolls their Willpower Pool (1dWIS + 1dCHA keep highest + Class Boons).
Outcome:
Resilience 
≥
≥ Power: The defender shrugs off the effect (0 Conditions).
Resilience < Power: The effect takes hold (Poisoned, Charmed, Paralyzed).
Critical Failure on Resilience: The effect's duration doubles or escalates to a lethal stage (Petrified, Dying).
5. Hit Location & Anatomical Wound Severance (The 1d8 Anatomical Matrix)

When an attack achieves a Natural Critical Hit (via d100 matching Crit Profile %), roll 1d8 randomly on our Anatomical Matrix below. When executing a Called Shot maneuver (DEC-044), do not roll randomly; instead, the attacker CHOOSES the exact body part targeted and applies its condition!

5.1 The Anatomical Location Die (1d8) & Called Shot Targets
Die Face (1d8)	Hit Location	Piecemeal Armor Absorption	Severe Anatomical Wound Condition (Crits & Called Shots)
1	Head / Skull	Helm / Coif ABS	Concussion / Dazed: Target suffers an immediate mental Die Step-Down (INT/WIS/CHA step down d10 
→
→ d8) and drops all active spell concentration (0 Focus actions allowed for 1 round).
2-3	Chest / Thorax	Breastplate ABS	Winded / Bruised Rib: Target loses 3 Stamina instantly (Breath knocked out). If Natural Crit, ribs fracture (Take 2 Vitality loss every time you spend Stamina).
4	Abdomen / Gut	Belt / Faulds ABS	Internal Trauma / Bleed: Target takes 
+
1
 Bane Die (‘-1 die volume‘)
+1 Bane Die (‘-1 die volume‘) on physical checks due to gut agony and gains Bleeding Cut (1 Vitality loss/round).
5	Shield / Off-Arm	Bracer / Shield ABS	Limp Shield Arm: If holding a shield or secondary item, drop it immediately into an adjacent Close zone. You cannot wield two-handed weapons or Raise Guard until sutured.
6	Weapon / Primary Arm	Bracer / Gauntlet ABS	Limp Weapon Arm: Drop your primary weapon instantly. You suffer 
+
2
 Bane Dice (‘Keep lowest‘)
+2 Bane Dice (‘Keep lowest‘) on all attacks made with your off-hand until treated.
7-8	Legs / Feet	Greaves / Boots ABS	Buckled Knee / Prone: Target falls Prone immediately (Speed 0 until standing up via [1A]). If Natural Crit, hamstring severed (Speed permanently halved until surgery).
5.2 Piecemeal Armor Layering (Mythras Customization)

For simulationist players who want distinct armor on each body part (e.g., Plate Helm on Head [ABS d10], but Leather Tunic on Chest [ABS d6]), our 1d8 Location Matrix automatically checks the exact Absorption Die (ABS) of that specific body part when resolving the impact check!

Open
10_master_top_to_bottom_system_summary.md
MD
Core Baseline System: The Mathless Resolution Engine
MD
Core Baseline System: The Mathless Resolution Engine

This document formalizes the rules for resolving all checks, attacks, spellcasting attempts, and opposed contests in our idealized TTRPG system. Every rule below operates without table-side arithmetic.

1. The Core Check Formula (2dX Keep Highest)

Whenever a character attempts an action with a chance of failure, the Game Master (GM) assigns a Target Number (DC) from 2 to 12.

To resolve the check:

Identify the character’s Die Size (X) for the relevant Attribute or Skill (d4, d6, d8, d10, or d12).
Assemble the Base Pool of two dice (2dX).
Apply any Boons or Banes to adjust pool volume (
+
1
𝑑
/
−
1
𝑑
+1d/−1d).
Roll the assembled dice and look at the single highest face value shown.
If the highest face value is greater than or equal to the DC, the check succeeds. No addition or subtraction is performed.

Result
=
max
⁡
(
Rolled Pool Faces
)
≥
Target DC
Result=max(Rolled Pool Faces)≥Target DC

2. Target Numbers & Capability Ceiling

Because there are no numerical modifiers added to the dice, the Target Number (DC) represents an absolute physical threshold:

Target Number (DC)	Difficulty Description	Required Die Size to Succeed Naturally
DC 3	Routine / Easy: A basic task under stress.	Any (d4+)
DC 5	Challenging: Requires competence or focus.	d6+ (Or d4 with Die Step-Up)
DC 7	Formidable: Professional mastery required.	d8+ (Or d6 with Die Step-Up)
DC 9	Heroic / Severe: A feat of elite prowess.	d10+ (Or d8 with Die Step-Up)
DC 11	Legendary: Almost superhuman execution.	d12 (Or d10 with Die Step-Up)
DC 12	Mythic / Absolute Ceiling: Peak mortal limit.	d12 only
3. Boons & Banes (Pool Volume Manipulation)

Instead of numerical adjustments (+2 / -2), situational factors, spells, and equipment quality grant Boons (+B) or impose Banes (+X).

3.1 Applying Boons and Banes

Before rolling, count all applicable Boons and Banes. They cancel each other out 1-to-1:

Net Pool Shift
=
Total Boons
−
Total Banes
Net Pool Shift=Total Boons−Total Banes

3.2 Pool Resolution Table
Net Shift	Pool Rolled	How to Determine Result
+3 Boons or more (+3B)	5dX	Roll 5 dice of your rank 
→
→ Keep the Single Highest Face.
+2 Boons (+2B)	4dX	Roll 4 dice of your rank 
→
→ Keep the Single Highest Face.
+1 Boon (+1B)	3dX	Roll 3 dice of your rank 
→
→ Keep the Single Highest Face.
0 (Normal Roll)	2dX (Base)	Roll 2 dice of your rank 
→
→ Keep the Single Highest Face.
-1 Bane (+1X)	1dX	Roll 1 die of your rank 
→
→ Take the Face Value Shown.
-2 Banes (+2X)	2dX	Roll 2 dice of your rank 
→
→ Keep the Single LOWEST Face (Disadvantage).
-3 Banes or more (+3X)	3dX	Roll 3 dice of your rank 
→
→ Keep the Single LOWEST Face.
4. Die Step-Up & Step-Down (Ceiling Manipulation)

To allow characters to overcome hard mathematical caps (such as a 2d6 character attempting a DC 7 check) or push beyond normal limits through sheer physical exertion, characters can perform a Die Step-Up (Stepping Up the pool).

4.1 Die Step-Up (Stepping Up the Pool)
Cost: Spend 1 point of physical Stamina (or mental Focus).
Effect: Step up the size of every die in your check pool by one rank for this single roll (d4 
→
→ d6 
→
→ d8 
→
→ d10 
→
→ d12).
Limit: A pool can normally only be stepped up once per action unless a special mastery feat or tier awakening allows a Double Step-Up (Up-Shift x2).
4.2 Die Step-Down (Stepping Down the Pool)
Trigger: Certain severe conditions (Exhausted, Muddled, Suppressed) or enemy curses impose a Die Step-Down (Stepping Down the pool) rather than a Bane.
Effect: Step down the size of every die in your check pool by one rank (d10 
→
→ d8). If a d4 pool suffers a Die Step-Down, the check automatically fails unless the character spends Stamina to perform a Die Step-Up back to d4.
5. Opposed Rolls (Zero-Math Contests)

When two characters directly oppose one another (e.g., an attacker swinging a sword against a defender attempting to parry, or a grappler wrestling an opponent), no static DC is used.

Both characters assemble their pools (Attacker Pool vs Defender Pool), applying their respective Boons, Banes, and Stamina shifts.
Both roll simultaneously.
Compare the Highest Face Value of the Attacker against the Highest Face Value of the Defender:
Attacker Highest > Defender Highest: Attacker wins and achieves their action.
Attacker Highest < Defender Highest: Defender wins and completely intercepts/avoids the action.
Tie (Equal Highest Faces): Look at the Second-Highest Face Value in each pool (if available). The higher second face wins the tie (Secondary Tiebreaker). If still tied or neither has a second die, the Defender / Active Reactor wins the clash.
6. Degrees of Success, 
𝑑
100
d100 Weapon Criticals & Wounds

To ensure that weapons of all sizes (d4 daggers to d12 greatswords) crit with balanced, explicit probability without higher dice penalizing critical frequency (DEC-034), our system uses Weapon Critical Threat Profiles (% Chance) checked via a single 
𝑑
100
d100 percentile roll alongside the step pool.

6.1 The 
𝑑
100
d100 Critical Threat Check

Every weapon, spell, or martial action has a Critical Threat Profile (Crit Profile %):

Standard Weapons (Maces, Clubs, Longswords): 10% Crit Profile (Roll 01-10 on d100).
Keen / Finesse Weapons (Rapiers, Scimitars, Daggers): 15% to 20% Crit Profile (Roll 01-15 or 01-20 on d100).
Heavy Picks / Siege (Deadly Weapons): 5% Crit Profile (Roll 01-05 on d100), but inflicts x3 or x4 Vitality multiplier.

How to Roll: When making an attack check (or damage roll), the player rolls their step pool (say, 3d10) and 1 percentile die (
𝑑
100
d100) simultaneously.

If the step check Succeeds (Highest face beats DC or Defender) AND the 
𝑑
100
d100 roll falls within the weapon's Crit Profile (say, rolling 07 on a 10% weapon), it is a Critical Hit!
6.2 Wounds vs. Minor Disruptions (DEC-034 & DEC-044)
Wounds Happen ONLY on a Critical Hit (or Called Shot):
Natural Critical Hit (via d100 matching Crit Profile %): Inflicts Double Vitality loss (Max Damage Face x 2) AND triggers an Anatomical Wound Condition (Roll 1d8 Location Matrix randomly).
The Called Shot Maneuver (Forcing a Wound without a Crit): A character can declare a Called Shot maneuver (spending [1A] + taking +1 Bane Die on attack, OR spending 2 Multi-Successes post-hit). If successful, it does NOT deal double damage (inflicts standard shown/rolled Damage Face vs Absorption), BUT the attacker chooses the exact anatomical body part targeted (Head, Chest, Arm, Leg) and triggers that location's severe Anatomical Wound Condition (Concussion, Dropped Weapon, Prone)!
Standard Hits (Damage > Absorption): Standard hits deal normal Vitality (HP) loss, and can inflict Quick Minor Disruptions (Off-balance, Shaken, Minor Bleeding Cut: -1 HP/round) resolved instantly via Class Abilities, Feats, or Multi-Success triggers, but never inflict permanent anatomical structural impairment or limb severance.
7. Multi-Success Maneuvers & Pool Trade-offs (No Tokens — DEC-042 & DEC-043)

To eliminate token counting currencies ([SET]) while preserving dynamic, universal combat maneuvers (Mythras tradition), maneuvers are executed directly using Multi-Success Counts (Required Successes S) and Check Pool Trade-offs (+1 Bane Die).

7.1 Multi-Success Combat Triggers (Zero Tokens)

When making an opposed attack check (Attacker Pool vs Defender Parry/Reflexes Pool), compare how many of your rolled dice equal or exceed the defender's highest face (Multi-Beat Count):

1 Success (Highest face beats defender): Standard Hit (Damage vs Absorption). Can inflict quick minor disruptions (Bleeding Cut, Shaken). Does not force Prone, Disarm, or Anatomical Wounds.
2 Successes (Two dice independently equal/exceed defender's highest face): Superior Hit (Standard Hit + 1 Universal Maneuver). You automatically execute 1 universal maneuver (Trip, Disarm, Shove, Overextend) right off the dice!
3+ Successes (Three dice equal/exceed defender's highest face): Overwhelming Hit (Standard Hit + Major Maneuver OR 2 Maneuvers). You execute 2 maneuvers (say, Disarm AND Trip) OR force a Called Shot Anatomical Wound (chosen body part condition)!
text
[ Attacker Pool (4d10): 5, 7, 8, 10 ]  vs  [ Defender Parry Pool (3d8): 4, 6, 7 ]
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
Winner: Attacker Highest (10) > Defender Highest (7) $\to$ STANDARD HIT
            │
            ▼
Multi-Success Check: How many other attacker dice equal or exceed '7'?
  ├── Die 1 (10) -> Success #1 (Highest Winner -> Standard Hit)
  ├── Die 2 (8)  -> Success #2 (+1 Universal Maneuver Triggered!)
  ├── Die 3 (7)  -> Success #3 (+2nd Maneuver OR Called Shot Triggered!)
  └── Die 4 (5)  -> Below 7 (No extra effect)
            │
            ▼
TOTAL OUTCOME: Overwhelming Hit! Attacker deals normal Damage vs Absorption AND immediately trips the target Prone AND disarms their weapon instantly without counting tokens!
7.2 Universal Default Maneuvers (Belong to Everyone)

Universal default maneuvers are not hardcoded to specific weapons; they exist for all actors (PCs, NPCs, Monsters). Martial classes and feats can unlock new maneuvers (Whirlwind Strike, Riposte) or expand default ones (e.g., Expert Disarm throws weapon 2 zones away):

Maneuver Name	Multi-Success Requirement	Mathless Mechanical Outcome	How Class/Feats Can Upgrade Maneuver
Trip / Knockdown	2 Successes	Foot-sweep or shield bash sends target Prone (Melee strikes against them roll +2 Boons [4dX]).	Shattering Sweep Feat: Target also takes 1 Durability Slot loss on their leg greaves.
Disarm Weapon	2 Successes	Catch opponent's weapon shaft or crossguard. Opponent’s weapon flies into an adjacent Close zone (Unarmed).	Expert Disarm Feat: Weapon flies 2 zones (Medium range) away, or is caught in your free hand.
Shove / Push	2 Successes	Push target back 1 zone (Near range), forcing them out of melee reach.	Juggernaut Push Feat: Target pushed back and knocked off-balance (takes +1 Bane on next action).
Overextend	2 Successes	Redirect attacker’s momentum off-balance. Target loses 1 Action Point ([1A]) on next turn OR takes 
+
1
 Bane Die
+1 Bane Die.	Defensive Stance Feat: You immediately gain 
+
1
 Boon Die (‘+1B‘)
+1 Boon Die (‘+1B‘) on your next check vs target.
Bypass Absorption	2 Successes	Strike slips through armor gap. Target’s Damage Absorption is stepped down two ranks (d10 
→
→ d6) for this hit.	Surgical Strike Feat: Armor Absorption is bypassed completely (Soak 0) for this hit.
Called Shot (Wound)	3 Successes (or +1 Bane trade-off)	Surgical strike (DEC-044). Inflicts normal Damage vs Absorption + you CHOOSE exact anatomical body part (Head, Arm, Leg) to trigger its severe wound condition! (No double damage).	Suture Master Feat: You can execute a Called Shot with only 2 Successes when wielding scalpel/finesse blades.
7.3 The Three Tactical Knobs for Executing Maneuvers

If a player knows they need a specific maneuver (say, a Called Shot or Disarm), they do not have to rely purely on rolling 2 or 3 Successes naturally. They can choose from three distinct tactical trade-off knobs:

Knob A (Multi-Success Free Trigger): Roll normal attack ([1A] Strike). If your check pool yields 2+ Successes, the maneuver happens for free!
Knob B (Pool Volume Trade-off / +1 Bane Die): Declare the maneuver before rolling (say, [1A] Disarm Strike). You accept $+1\text{ Bane Die (-1 die volume: 4d10 
→
→ 3d10)}$ on your check. If your highest face wins (just 1 Success required), the maneuver happens automatically!
Knob C (Dedicated Action Check): Spend a dedicated action point ([1A] Maneuver check like an opposed Athletics shove/disarm without damage) OR make a 2-action sure-strike activity ([2A] Precision Maneuver).
8. The Three Check Modes (Fixed DC vs Pure Opposed vs Hybrid DC Floor)

To ensure resolution is always ground-in reality and intuitive for the Game Master, our system natively supports All Three Modes of Resolution. The GM applies each where it makes sense from an intuition standpoint:

text
                  [ What is the nature of the challenge? ]
                                     │
           ┌─────────────────────────┼─────────────────────────┐
           ▼                         ▼                         ▼
[ Static Obstacle / Crafting ] [ Active Melee / Social ] [ Long Range / Technical Spell ]
           │                         │                         │
           ▼                         ▼                         ▼
  Mode 1: Fixed DC            Mode 2: Pure Opposed      Mode 3: Hybrid DC Floor
 (Roll vs Static Number)     (Attacker vs Defender)    (Attacker vs Defender AND DC)
8.1 Mode Taxonomy & Intuitive Application Rules
Check Mode	Core Comparison Formula	When to Apply (Intuitive Trigger)	Typical Action Examples
Mode 1: Fixed DC	
max
⁡
(
Pool
)
≥
Static DC
max(Pool)≥Static DC	Static obstacles, environmental hazards, downtime crafting clocks, and uncontested physical/mental feats.	Climbing a sheer cliff (DC 7), picking an unattended master lock (DC 8), deciphering ancient runes (DC 6), forging an iron blade (DC 5).
Mode 2: Pure Opposed	
max
⁡
(
Attacker
)
>
max
⁡
(
Defender
)
max(Attacker)>max(Defender)	Dynamic, chaotic clashing between two active opponents where the baseline difficulty is purely the opponent's immediate effort.	Melee combat strikes where the defender actively parries/evades (Combat Pool vs Parry Pool), wrestling/grappling contests, active stealth vs active searching.
Mode 3: Hybrid (DC Floor)	
max
⁡
(
Attacker
)
>
max
⁡
(
Defender
)
max(Attacker)>max(Defender)<br>AND 
max
⁡
(
Attacker
)
≥
DC Floor
max(Attacker)≥DC Floor	Complex, technical actions that carry an intrinsic physical/spatial difficulty floor, OR acting against passive obstacles actively defended.	Ranged attacks at extreme distance / heavy cover (Must beat Evasion AND clear Distance DC Floor), channeling high-tier spells against target Resilience (Must beat Resilience AND clear Spell Complexity DC Floor).
8.2 Mode 3 Deep Dive (Why Hybrid DC Floors Prevent Absurdities)

In a pure opposed check, if an archer shoots at a target 200 feet away (Tier 4 Extreme Distance) and the target slips on mud, rolling a 2 on Evasion, should a rolled 3 by the archer hit? No. Intuition dictates that hitting a target at 200 feet has an intrinsic ballistic spatial difficulty (e.g., Distance Floor DC 7).

Even if the target rolls a 2, if the archer rolls a 5, the arrow falls short or drifts due to wind (Failed vs DC Floor 7).
To hit, the archer must roll at least a 7 OR higher than the target's Evasion face (whichever is higher)!
9. The Competency Floor (Investment-Driven Mastery & Engineered Hard Caps)

To give players granular control over mastery and establish engineered hard caps where grandmasters literally cannot whiff on routine checks, our system incorporates Competency Floors (Fixed Die Minimums).

9.1 Decoupling Competency Ranks from Character Level

Crucially, Competency Ranks (Untrained, Trained, Expert, Master, Legendary) measure direct player investment in a specific Action Mastery Domain (Combat, Lore, Subterfuge, etc.), regardless of overall Character Level (1 to 20+).

A Level 20 Archmage with zero investment in Combat Mastery (Physical weapon fighting) falls strictly under the Untrained (Rank 0) competency level when swinging a sword (2d6, Floor 0).
Conversely, a Level 6 dedicated Fighter who has invested all their domain points and class feats into Combat Mastery can reach Master (Rank 3) or temporarily step into Legendary (Rank 4) during a heroic surge!

When rolling a check pool, your Proficiency Tier (Untrained to Legendary) sets a guaranteed minimum floor (F) on your highest die:

Final Check Result
=
max
⁡
(
max
⁡
(
Rolled Pool Faces
)
,
Competency Floor
)
Final Check Result=max(max(Rolled Pool Faces),Competency Floor)

9.2 The 5 Competency Levels (Investment-Driven Step & Floor Scaling)
0. Untrained (Zero Investment at ANY Character Level): 2dX keep highest, Floor = 0 (Pure random roll)
1. Trained (Basic Professional Investment): 3dX keep highest (+1B), Floor = 3 (Guaranteed minimum face of 3)
2. Expert (Dedicated Specialization): 3dX keep highest + 1 Die Step-Up, Floor = 5 (Guaranteed minimum face of 5)
3. Master (Elite Domain Grandmastery): 4dX keep highest (+2B) + 2 Die Step-Ups, Floor = 7 (Guaranteed minimum face of 7)
4. Legendary (Mythic Domain Apex / Surge): 5dX keep highest (+3B) + 3 Die Step-Ups, Floor = 9 (Guaranteed minimum face of 9)
9.3 Engineered Mastery Guarantees (Fixed DC Checks)

Because of this engineered floor, characters achieve absolute mathematical immunity to failing challenges below their competency tier without table-side arithmetic:

Trained (Floor 3): Immune to failing DC 3 Routine tasks (100% success rate).
Expert (Floor 5): Immune to failing DC 5 Challenging tasks (100% success rate).
Master (Floor 7): Immune to failing DC 7 Formidable tasks (100% success rate).
Legendary (Floor 9): Immune to failing DC 9 Heroic tasks (100% success rate).
10. Multi-Success Complex Checks (Threshold T + Required Beats S — DEC-036)

To achieve smooth, fine-grained difficulty scaling without introducing numbers outside our 5 fixed DCs (2 to 12), our check engine supports Multi-Success Complex Checks.

Target Difficulties can specify both a DC Threshold (T = 3, 5, 7, 9, 11) AND a Required Number of Successes (S = 1 to 4+ dice meeting/exceeding T simultaneously).

10.1 Multi-Success Resolution Mechanics

When attempting a complex task (e.g., picking a masterwork clockwork lock, forging adamantine, or casting a multi-zone ritual spell):

Assemble your check pool (say, 4d10 keep highest).
Roll the pool and apply your Competency Floor (F) to the highest face.
Count how many total dice in your pool show a value greater than or equal to the DC Threshold (T).
If your count equals or exceeds the Required Successes (S), the complex task succeeds! Any extra beating dice beyond S award Special Effect Tokens ([SET]).
10.2 Finer Probability Granularity (Atomic Stepping)

As proved in our mathematical simulations (sim_multi_success_granularity.py), requiring multiple successes (S = 2 or 3) allows the GM to dial in exact intermediate difficulty percentages (say, 35% vs 48% vs 58% vs 78%) without ever changing the core T threshold (say, DC 7):

Level 5 Expert (3d10, Floor 5) vs DC 7: 1 beat (Standard Formidable) = 78.4%. 2 beats (Complex Formidable) = 35.2%.
Level 9 Master (4d12, Floor 7) vs DC 9: 1 beat (Standard Heroic) = 80.2%. 2 beats (Complex Heroic) = 40.7%. 3 beats (Grand Heroic) = 11.1%.
Open
used
Bash
101ms
Edited files
4
01_master_brainstorm_log.md
MD
used
Bash
90ms

Your distinction between Natural Critical Hits and Called Shots is 100% spot-on.

It separates chaotic, well-placed kinetic force from surgical tactical precision. We have officially locked this distinction (DEC-044) into our simulationist combat modeling (04_simulationist_subsystems/01_defenses_and_damage_modeling.md Section 2.1 & Section 5, presented above), our check engine (01_resolution_engine.md Section 6.2), and our master executive briefing.

⚔️ Natural Crits vs. Called Shots (The Exact Distinction — DEC-044)
Combat Action Type	Damage & Vitality (HP) Outcome	Anatomical Wound Condition Triggered (1d8 Matrix)	Tactical & Simulationist Rationale
Natural Critical Hit<br>(Step Check Succeeds AND 
𝑑
100
d100 falls within Crit Profile %)	Double Vitality Loss<br>(Max Damage Face x 2)	Random Anatomical Wound<br>(Roll 1d8 on our Location Matrix)	Represents a devastating, chaotic, well-placed blow that penetrates deep into random vital anatomy. You get massive kinetic damage AND the 1d8 roll determines what snapped!
The Called Shot Maneuver<br>(Executed via 3+ Successes OR declaring +1 Bane Die trade-off)	Standard Vitality Loss<br>(Normal shown/rolled Damage Face vs. Absorption — NO double damage)	Player's Chosen Anatomical Wound<br>(Player CHOOSES exactly which body part is struck — Head, Chest, Arm, or Leg — and forces that specific condition immediately!)	Represents surgical, deliberate tactical precision (aiming specifically for a kneecap or weapon hand). You trade away double damage (or accept a +1 Bane check trade-off) to dictate the exact anatomical impairment inflicted on the enemy!
📋 How This Plays Out at the Table (Zero Tokens, Zero Math)
Example A (A Natural Critical Hit): A Fighter swings his Longsword (10% Crit Profile -> 01-10 on d100). He rolls 4d10 keep highest and 1d100 simultaneously. His highest step die (9) beats the enemy's parry (Hit!), AND his 
𝑑
100
d100 reads 04 (Critical Hit!).
Outcome: Longsword deals double Vitality loss (10 x 2 = 20 HP), AND the GM rolls 1d8 (gets 1 — Head Hit!), inflicting a severe Concussion (mental step-down and broken spell concentration)!
Example B (A Called Shot to the Weapon Hand): A Rogue wants to disarm/cripple a dangerous Ogre's primary arm without hoping for a lucky 10% crit roll. She declares a Called Shot to the Weapon Arm (Face 6 on matrix), accepting 
+
1
 Bane Die (‘3d10 -> 2d10 keep highest‘)
+1 Bane Die (‘3d10 -> 2d10 keep highest‘) on her attack. Her highest die (8) beats the Ogre's parry (7).
Outcome: Rogue deals standard shown weapon damage vs. Absorption (no double damage), BUT instantly forces the chosen Limp Weapon Arm condition (Ogre drops its massive Greatclub immediately!)!
🚀 Where Shall We Direct Our Creative Focus Next?

With all 44 decisions across our 33 files completely aligned, where would you like to take our design work next?

Design the Core Feat Compendium (General, Combat, and Racial Feats): Convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into clean 1-sentence mathless vector traits across our 6 tiers.
Flesh out the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Detail all 5 domains (Combat, Survival, Subterfuge, Lore, Social), building out specific individual skills (Stealth, Lockpicking, Arcana, Diplomacy) and multi-success maneuvers across all 5 competency ranks (Untrained to Legendary).
Build the Magic & Spellcasting Engine (Traditions & Vancian Grimoire): Define Vancian daily preparation across our 5 Traditions (Arcana, Divine, Primal, Shadow, Time), detail metamagic Focus costs, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Complete Step-by-Step Character & Monster Walkthrough: Build a Tier 2 Veteran (Level 6) PC (say, a Human Greatsword Fighter or Elven Finesse Rogue) and a Tier 3 Master (Level 10) Boss monster (Ogre Mage or Lich King) from scratch to show the exact mathless formulas in action.

Which of these would you like to explore right now?
