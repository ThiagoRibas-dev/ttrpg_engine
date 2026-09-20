---
turn: 16
role: "AI-Designer"
source: chat_history.json
---

# Turn 16 — AI-Designer

used
Bash
89ms
Edited files
3
01_master_brainstorm_log.md
MD
Check Pool Generation & Class Differentiation Across 20 Levels
MD
Check Pool Generation & Class Differentiation Across 20 Levels

To ensure our mathless 2dX keep highest baseline is meaningful, granular, and tactile across all 20 levels (and 6 Tiers of Power), we must clearly define how Attributes (MIG, AGI, INT, WIL), Class / Archetype, Skill Proficiency, and Equipment Choice interact when generating a check pool.

This document evaluates three architectural models and tests them against four distinct character archetypes to establish our definitive check pool formula.

1. The Core Architectural Dilemma (Separating Ceiling vs Reliability)

When a character declares an action (e.g., a Melee Strike), the Game Master must instantly know:

What is the Die Size (X — 
𝑑
4
→
𝑑
12
+
d4→d12+)? Governs the Absolute Capability Ceiling and kinetic impact (Can they hit DC 9? How much damage vs Soak?).
What is the Pool Volume (N — 
1
𝑑
→
5
𝑑
1d→5d)? Governs Reliability & Multi-Beat Count (How often do they whiff? How many [SET] tokens do they earn on a hit?).

If both Attribute and Skill simply add dice (or simply change die size), a dedicated Fighter and a battle-trained Wizard end up rolling identical dice. We must separate their mechanical identities across Three Concrete Vectors.

2. Model Evaluation (Testing the Four Archetypes)

Let's test four Level 5 (Tier 2 - Veteran) characters across three candidate models:

Char 1 (Strong Melee + Proficient): Human Greatsword Fighter (High Might, Trained in Swords, Martial Class).
Char 2 (Weak Melee + Proficient): Elven Rapier Swashbuckler (Low Might/High Agility, Trained in Swords, Martial Class).
Char 3 (Strong Melee + NOT Proficient): Ogre Barbarian swinging an exotic spiked chain (High Might, Untrained in Chain, Martial Class).
Char 4 (Strong Non-Melee + Proficient): Dwarven War Cleric swinging a mace (High Might, Trained in Maces, Civilian/Caster Class).
2.1 Model A: Pure Separation (Attribute = Die Size | Proficiency = Pool Volume | Class = Feats Only)
Formula: Die Size = Attribute Die. Pool Volume = 2d (Base) + Proficiency Boons (+0B to +3B).
Test Results at Level 5 (Trained +1B):
Char 1 (Fighter): 3d10 keep highest (MIG d10 + 1B).
Char 2 (Swashbuckler): 3d6 keep highest (MIG d6 + 1B). Note: If using Finesse/Agility, becomes 3d10.
Char 3 (Barbarian Untrained): 2d10 keep highest (MIG d10 + 0B).
Char 4 (Cleric): 3d10 keep highest (MIG d10 + 1B).
Analysis of Model A: Failed differentiation. The Cleric (Char 4) rolls the exact same physical check pool (3d10) as the dedicated Fighter (Char 1). The only difference is that the Fighter has martial feats (Cleave), while the Cleric has divine spells. While functional, it leaves martial classes feeling less physically dominant on base attacks.
2.2 Model B: The Dual-Axis Step & Volume Model (Attribute + Skill = Die Step | Class/Stance = Pool Volume)
Formula: Die Size = Attribute Die + Skill Step Upgrades (Untrained = +0 steps, Trained = +1 step, Master = +2 steps). Pool Volume = Class Baseline (Martial = 3d, Civilian = 2d) + Tactical Boons.
Test Results at Level 5 (Trained = +1 Die Step-Up):
Char 1 (Fighter): Base MIG d8 + +1 Step (Trained) 
→
→ 3d10 keep highest (3d Martial baseline).
Char 2 (Swashbuckler): Base MIG d6 + +1 Step (Trained) 
→
→ 3d8 keep highest (3d Martial baseline).
Char 3 (Barbarian Untrained): Base MIG d8 + +0 Steps (Untrained) 
→
→ 3d8 keep highest (3d Martial baseline).
Char 4 (Cleric): Base MIG d8 + +1 Step (Trained) 
→
→ 2d10 keep highest (2d Civilian baseline).
Analysis of Model B: Exceptional physical differentiation! Look at how every character occupies a distinct tactical niche:
The Fighter (3d10) has both peak ceiling (d10) and peak reliability (3 dice).
The Swashbuckler (3d8) and Barbarian (3d8) share high reliability (3 dice), but require Finesse or Rage feats to reach d10 kinetic ceilings.
The Cleric (2d10) can hit formidable targets off sheer strength and weapon familiarity (d10 ceiling), but lacks the multi-beat [SET] token generation and consistency of the 3-die martial baseline (3d10 vs 2d10).
2.3 Model C: The Definitive Tri-Vector Matrix (Our Selected Baseline)

To integrate Model B seamlessly into our 20-level advancement table across the 6 Tiers of Power (Trained -> Mythic [21+]), we formalize Model C: The Tri-Vector Matrix:

text
[ Assembling a Check Pool: The Tri-Vector Formula ]
  ├── 1. Die Size (`Capability Ceiling`) = Core Attribute (`d4 to d12`) + Weapon/Domain Proficiency Step (`+0 to +2 Steps`)
  ├── 2. Pool Volume (`Reliability & [SET] Count`) = Base Pool (`2d`) + Class Martial Boon (`+0B or +1B`) + Tactical Boons (`Flanking, High Ground`)
  └── 3. Action Economy & Feats = Class/General Feats (`Power Strike [1A], Cleave [0A], Riposte [SET]`)
3. The Tri-Vector Generation Rules (Explicit Specification)
Vector 1: Die Size (The Capability Ceiling — X)

Your check pool's Die Size (X) is determined by combining your Core Attribute (MIG, AGI, INT, WIL) with your Skill / Domain Proficiency Tier:

Final Die Size (‘X‘)
=
Attribute Step
+
Domain Proficiency Step Shift
Final Die Size (‘X‘)=Attribute Step+Domain Proficiency Step Shift

Proficiency Tier	Step Shift Applied to Attribute	Example (Base Attribute d8)	What This Represents Physically
0. Untrained	+0 Steps (Base Die)	d8	Raw innate physical/mental potential without technical technique.
1. Trained (Tier 1+)	+1 Die Step-Up	d10	Professional competence; proper leverage, edge alignment, or footwork.
2. Mastered (Tier 2+)	+2 Die Step-Ups	d12	Elite specialization; striking anatomical weak points with effortless grace.
3. Legendary (Tier 4+)	+3 Die Step-Ups	d12+1 (Pooled overflow)	Grandmastery; surpassing mortal physical limits through legendary discipline.
Vector 2: Pool Volume (Reliability & [SET] Generation — N)

Your check pool's Volume (N) starts at 2dX and grows via your Class Baseline and immediate Tactical Boons (+B):

Class / Archetype Category	Base Check Pool Volume	Why This Differentiates Classes
Martial Archetypes<br>(Fighter, Barbarian, Ranger, Rogue, Paladin)	3dX (Base +1 Martial Boon)	Martial training grants built-in tactical consistency (3 dice). Martial characters roll fewer whiffs (below 5) and naturally earn more Special Effect Tokens ([SET]) via multi-beat face counts!
Civilian / Caster Archetypes<br>(Wizard, Sorcerer, Cleric, Bard, Alchemist)	2dX (Standard Base Pool)	Spellcasters channel their class power into Focus Pools and spell domain boons (3d/4d on Arcana checks). When making physical weapon strikes, they roll the standard 2dX baseline unless assisted by magic or tactical flanking.
Vector 3: Class Feats & Exertion Options (What You Can DO With the Pool)

While Attributes and Proficiency set the pool size, Class Feats and Exertions dictate how the character manipulates the rules during combat:

Power Strike (Martial Class Feat): Take $+1\text{ Bane Die (-1 die volume: 3d10 
→
→ 2d10)}$ on your attack check. If you hit, perform a Die Step-Up on your weapon's Damage Die (d8 
→
→ d10) vs target Soak.
Berserk Rage (Barbarian Class Feat): Spend 2 Stamina to step up your Might die (d10 
→
→ d12) and gain 
+
1
 Boon Die (‘+1B‘)
+1 Boon Die (‘+1B‘) for 1 round, but take $+1\text{ Bane Die}` on incoming Evasion/Parry checks.
Arcane Channeling (Caster Class Feat): Spend 1 Focus to substitute your Intellect Pool (2dINT) in place of Might/Agility when striking with an attuned bound weapon (Spellblade).
4. 20-Level Scaling (Side-by-Side Archetype Progression)

Let's trace how the Fighter (Char 1), Swashbuckler (Char 2), Barbarian (Char 3), and Cleric (Char 4) advance across the 20 levels and tier boundaries:

Level & Tier	Char 1: Greatsword Fighter (Strong Martial + Trained)	Char 2: Rapier Swashbuckler (Weak MIG/High AGI Martial + Trained)	Char 3: Spiked Chain Barbarian (Strong Martial + Untrained)	Char 4: Mace War Cleric (Strong Caster + Trained)
Level 1<br>(Tier 1: Trained)	3d10 keep highest<br>(Base MIG d8 + 1 Step Trained + 1 Martial Boon)	3d10 keep highest<br>(Base AGI d8 [Finesse] + 1 Step Trained + 1 Martial Boon)	3d8 keep highest<br>(Base MIG d8 + 0 Steps Untrained + 1 Martial Boon)	2d10 keep highest<br>(Base MIG d8 + 1 Step Trained + 0 Civilian Boon)
Level 5<br>(Tier 2: Veteran)	3d12 keep highest<br>(MIG stepped to d10 at Lvl 4 + 1 Step Trained)	3d12 keep highest<br>(AGI stepped to d10 at Lvl 4 + 1 Step Trained)	3d10 keep highest<br>(MIG stepped to d10 at Lvl 4 + 0 Steps Untrained)	2d12 keep highest<br>(MIG stepped to d10 at Lvl 4 + 1 Step Trained)
Level 9<br>(Tier 3: Master)	4d12 keep highest<br>(Domain elevated to Mastered (+2 Steps) at Lvl 6 + Martial Boon + Flanking/Stance)	4d12 keep highest<br>(Domain elevated to Mastered (+2 Steps) at Lvl 6 + Martial Boon)	3d12 keep highest<br>(MIG stepped to d12 at Lvl 8 + 0 Steps Untrained + Martial Boon)	2d12 keep highest<br>(MIG at d10 + 2 Steps Mastered + 0 Civilian Boon)
Level 16<br>(Tier 4: Hero)	4d12+ keep highest<br>(MIG d12 + 2 Steps Mastered + Martial Boon + Free Hyper-Shift)	4d12+ keep highest<br>(AGI d12 + 2 Steps Mastered + Martial Boon + Riposte Mastery)	4d12 keep highest<br>(MIG d12 + 0 Steps Untrained + Martial Boon + Berserk Rage)	3d12 keep highest<br>(MIG d12 + 2 Steps Mastered + Divine Blessing Boon)
4.1 Summary of Tactical & Simulationist Success

By combining Model C (Tri-Vector Matrix) with our 6 Tiers of Power, every archetype feels mechanically and tactilely distinct across all 20 levels:

The Fighter is the ultimate kinetic juggernaut (peak die step + peak volume).
The Swashbuckler matches the Fighter in precision and volume using agility/finesse, but relies on Bleed/Disarm [SET] tokens rather than raw crushing weight.
The Barbarian hits hard (3 dice) even with unfamiliar weapons, and reaches titanic damage ceilings when entering Berserk Rage.
The Cleric/Battle Caster can stand on the front lines and deliver crushing hits (d10/d12 die ceiling), but naturally generates fewer multi-beat [SET] tokens than dedicated martial masters unless expending divine Focus!
Open
used
Bash
99ms

We have evaluated the exact interaction of Attributes, Class, Proficiency, and Equipment across all four of your test scenarios and locked in our definitive check pool formula in 03_core_baseline_system/06_check_pool_generation_and_class_differentiation.md (presented above), recorded under decision DEC-018.

🏛️ The Tri-Vector Matrix (Separating Ceiling vs. Reliability)

When a character declares an action (e.g., a Melee Strike), the game must determine two separate axes without table math:

The Die Size (X — 
𝑑
4
→
𝑑
12
+
d4→d12+): Governs the Capability Ceiling and kinetic power (Can they clear DC 9? How much impact vs Soak?).
The Pool Volume (N — 
1
𝑑
→
5
𝑑
1d→5d): Governs Reliability & Multi-Beat Count (How often do they whiff? How many [SET] tokens do they earn on a hit?).

To prevent a dedicated Fighter and a battle-trained Wizard from rolling identical dice, our check pool is built from Three Concrete Vectors:

text
[ Assembling a Check Pool: The Tri-Vector Formula ]
  ├── 1. Die Size (`Capability Ceiling — X`) = Core Attribute (`d4 to d12`) + Domain Proficiency Step Shift (`+0 to +3 Steps`)
  ├── 2. Pool Volume (`Reliability & [SET] Count — N`) = Base Pool (`2dX`) + Class Martial Baseline (`+0B or +1B`) + Tactical Boons
  └── 3. Action Economy & Feats = Class/General Feats (`Power Strike [1A], Cleave [0A], Riposte [SET]`)
🧪 Testing Your Four Scenarios at Level 5 (Tier 2: Veteran)

Let's see how our Tri-Vector Matrix distinctly separates your four test characters (assuming Lvl 5, where Trained = +1 Die Step-Up):

Character Scenario	Tri-Vector Breakdown (Attribute + Proficiency + Class)	Final Rolled Check Pool	What This Represents Physically
1. Strong Melee + Proficient<br>(Human Greatsword Fighter)	• Die Size: Base MIG d8 + +1 Step (Trained) 
→
→ d10<br>• Pool Volume: Base 2d + +1B Martial Baseline 
→
→ 3d	3d10 keep highest	The Peak Martial Juggernaut. Maximum physical ceiling (d10) and maximum consistency (3 dice). Generates frequent multi-beat [SET] tokens (Cleave, Impale, Shatter).
2. Weak Melee + Proficient<br>(Elven Rapier Swashbuckler)	• Die Size: Base MIG d6 + +1 Step (Trained) 
→
→ d8<br>• Pool Volume: Base 2d + +1B Martial Baseline 
→
→ 3d<br>(Note: If using Finesse/AGI d10, steps to d12!)	3d8 keep highest<br>(or 3d12 on Finesse)	The Technical Duelist. If forced to use pure raw strength (heavy club), rolls very consistently (3 dice) but with a lower kinetic ceiling (d8). When using agility/finesse, matches or exceeds the giant Fighter (3d12) via surgical precision.
3. Strong Melee + NOT Proficient<br>(Ogre Barbarian with Spiked Chain)	• Die Size: Base MIG d8 + +0 Steps (Untrained) 
→
→ d8<br>• Pool Volume: Base 2d + +1B Martial Baseline 
→
→ 3d	3d8 keep highest	The Raw Martial Brawler. Hits very reliably (3 dice) off pure martial reflex and muscle memory (d8), but lacks the high edge-alignment step (d10) of a trained master. Can enter Berserk Rage (Stamina spend) to force his die up to d10.
4. Strong Non-Melee + Proficient<br>(Dwarven War Cleric with Mace)	• Die Size: Base MIG d8 + +1 Step (Trained) 
→
→ d10<br>• Pool Volume: Base 2d + 0B Civilian Baseline 
→
→ 2d	2d10 keep highest	The Heavy Civilian/Spellcaster. Can strike formidable targets off sheer strength and weapon familiarity (d10 ceiling), but lacks the 3-die martial consistency and multi-beat [SET] token generation of the dedicated Fighter (2d10 vs 3d10).
📈 How This Scales Across the 20 Levels (and 6 Tiers)

Because Attributes and Skill Proficiencies step up at clear tier boundaries, characters naturally grow across all 20 levels:

Level 1 (Tier 1: Trained): Fighter rolls 3d10 (Base MIG d8 + 1 Step Trained + Martial Boon). Cleric rolls 2d10.
Level 5 (Tier 2: Veteran): Fighter steps up MIG to d10 
→
→ 3d12.
Level 9 (Tier 3: Master): Fighter elevates proficiency to Mastered (+2 Steps) 
→
→ 4d12 keep highest.
Level 16 (Tier 4: Hero): Fighter steps MIG to d12 
→
→ 4d12+ keep highest (plus free Hyper-Shifts and 4th-degree maneuvers).
🎯 Where Should We Direct Our Focus Next?

Now that the check pool formulas and class differentiations are completely defined, which subsystem or content expansion should we tackle next?

Design the Core Feat Compendium (General, Combat, and Racial Feats): Let's convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into 1-sentence mathless vector traits across our 6 tiers.
Flesh out the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Let's detail all 5 domains (Combat, Survival, Subterfuge, Lore, Social), building their exact proficiencies, capability thresholds (Untrained vs Trained vs Master vs Legend), and maneuver options (Shove, Trip, Grapple, Disarm, Feint, Demoralize).
Build the Magic & Spellcasting Engine: Let's define the exact rules for casting across our 5 Traditions (Arcana, Divine, Primal, Shadow, Time), spell interruption via anatomical head/chest hits, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Complete Character & Monster Creation Walkthrough: Let's go step-by-step through creating a Tier 2 Veteran (Level 6) PC and a Tier 3 Master (Level 10) Boss monster from scratch to show the exact mathless formulas in action.

Which of these would you like to explore next?
