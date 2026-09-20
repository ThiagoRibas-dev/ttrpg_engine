---
turn: 60
role: "AI-Designer"
source: chat_history.json
---

# Turn 60 — AI-Designer

used
Bash
88ms
Edited files
3
01_master_brainstorm_log.md
MD
Attacks & Spellcasting: Skill-Unified vs. Class-Split Architecture
MD
Attacks & Spellcasting: Skill-Unified vs. Class-Split Architecture

To finalize our baseline resolution rules across our Model A Check Engine (Attribute = Die Size X | Competency Rank = Pool Volume N and Floor F — DEC-038), we must decide whether physical attacks (Blades, Bows, Brawling) and spellcasting (Arcane/Divine checks) exist inside our 5 Action Mastery Domains (as specific skills) or separate Class Advancement Tracks (like D&D 3.5e BAB and Caster Level).

This document evaluates three architectural models, analyzes their interaction with class identity and our four paired defenses, and establishes our definitive baseline.

1. Candidate Architectural Models (Pros & Cons)
1.1 Option 1: The Skill-Unified Engine (Attacks & Spells ARE Specific Skills)
Structure (The Mythras / BRP / Year Zero approach): There is no separate Base Attack Bonus (BAB) or Caster Level check pool track on the class table. Instead, Combat Mastery (Blades, Axes, Bows, Shields) and Lore & Arcana (Arcana, Divine, Primal traditions) are specific skills listed under our 5 Action Mastery Domain umbrellas (DEC-030). When a character levels up and spends general Skill Allocations (Track 5), they can invest directly in Longswords, Pyromancy, Stealth, or Diplomacy.
🟢 Major Pros:
100% Universal Check Rule: Zero mechanical distinction between swinging a sword, picking a lock, negotiating a treaty, or casting a fireball! Every single check is: Attribute Die Size (X) + Skill Competency Volume & Floor (N & F).
Total Player Freedom: A player can build a battle-mage who invests equally in Longswords and Arcana, or a noble knight who invests in Polearms and Diplomacy, without being forced into linear class BAB jackets.
🔴 Major Cons:
The "Skill Allocation Tax" Dilemma: If a Fighter only receives 1 skill allocation every 2 levels (Bad/Combat track progression — DEC-035 Track 5), but must spend those allocations just to raise his sword skill from Trained -> Expert -> Master to keep up with enemy Parry/Reflex defenses, then the Fighter has zero skill allocations left over to invest in Athletics, Survival, or Perception! His entire skill budget becomes a mandatory weapon skill tax.
1.2 Option 2: The D&D / Pathfinder Split Engine (Attacks & Spells are Dedicated Class Tracks Apart from Skills)
Structure (The D&D 3.5e / PF2e approach): Your ability to hit with a weapon (Base Attack Bonus / Combat Pool) and your ability to land a spell (Caster Level / Spell Power Pool) exist on dedicated Class Advancement Tracks (DEC-035 Track 2 & Track 4), completely separate from your general Skill Competency Allocations (Track 5: Stealth, Lockpicking, Arcana Lore, Diplomacy).
🟢 Major Pros:
No Skill Tax (Protects General Competence): Fighters and Wizards don't have to sacrifice their skill allocations just to buy basic attack or spell proficiency. A Fighter automatically hits hard with his weapons (reaching Expert Floor 5 at Lvl 5, Master Floor 7 at Lvl 9) via his class track (DEC-029), allowing him to spend his 9 to 14 General Skill Allocations on becoming a master mountaineer (Athletics), a wilderness scout (Survival), or a military commander (Leadership).
Immediate 3.5e Familiarity: Preserves the exact structural separation of HP, BAB, Saves, CL, and Skills that our 20-Level Class Advancement Matrix (DEC-035) is built upon.
🔴 Major Cons:
Mechanical Bifurcation: Creates two parallel mechanisms for how pools and floors advance (one automatic by class level for attacks/spells, one purchased via skill allocations for out-of-combat skills).
1.3 Option 3: The Hybrid "Class-Granted Domain Allocations" Engine (Recommended Baseline)

To combine the elegant universality of Option 1 (Attacks and Spells ARE specific skills under our 5 domains) with the zero-skill-tax protection of Option 2 (distinct class identity and automatic core role mastery), we establish Option 3: The Hybrid Class-Granted Allocations Engine:

text
[ Universal Skill Ecosystem: How Competency Ranks Advance ]
  ├── 1. Class-Granted Primary Allocations (`Automatic Role Mastery — Zero Tax`)
  │     └── At Levels 1, 5, 9, and 15 (`Tier Boundaries`), your Class automatically elevates ONE primary class skill (`e.g., Longswords for Fighter; Pyromancy for Wizard`) to the next Competency Rank (`Trained -> Expert Floor 5 -> Master Floor 7 -> Legend Floor 9`).
  │
  └── 2. General Skill Allocations (`Track 5 — Universal Out-of-Combat Customization`)
        └── At Levels 1, 2, 4, 6, 7, 10, 12, 14, 17, 18, you receive general skill allocations to invest freely in ANY specific skill (`Stealth, Lockpicking, Diplomacy, Medicine, Athletics, OR even a second weapon/spell style like Bows or Necromancy`)!
Why Option 3 is the Ultimate High Fantasy Standard:
100% Universal Rule (Option 1 Benefit): Everything on the sheet (Swords, Spells, Diplomacy, Stealth) uses the exact same 5 Competency Ranks (Untrained 0 -> Trained 3 -> Expert Floor 5 -> Master Floor 7 -> Legend Floor 9) and exact same Model A check pool engine (Die Size X from Attribute, Pool Volume N and Floor F from Competency Rank — DEC-038)!
Zero Skill Tax (Option 2 Benefit): Because Classes award dedicated primary skill rank upgrades at Tier boundaries (Levels 1, 5, 9, 15), Fighters and Wizards automatically hit their required Expert, Master, and Legend attack/spell floors in their core vocation (no skill allocation tax!), while retaining their full budget of General Skill Allocations to customize their out-of-combat identities!
2. How Option 3 Interacts with Classes (Does Class Dictate Ability to Hit?)

Under Option 3, Class dictates your baseline automatic mastery and what specific skills you can elevate for free, while your total capability ceiling (Die Size X) remains bound to your Attributes:

Class Archetype	Class-Granted Primary Skill (Automatic Growth at Lvl 1, 5, 9, 15)	General Skill Allocations (Track 5 — Free Allocation Budget)	What Happens When Attacking vs. Spellcasting at Level 10 (Master Tier)
Fighter (Martial Anchor)	1 Primary Weapon Skill (e.g., Heavy Blades / Greatswords) under Combat Mastery. Reaches Master Rank (4d12 keep highest, Floor 7) at Lvl 9 automatically (STR d12).	9 Total Allocations (Bad Track) across 1-2 domains (e.g., Athletics, Intimidate, Shields).	When Swinging Greatsword: Rolls 4d12 keep highest (Floor 7). Automatic Master striker.<br>When Casting Arcane Spell: Because he invested 0 points in Pyromancy, rolls Untrained (2d6, Floor 0).
Rogue (Skill & Finesse Anchor)	1 Primary Finesse/Subterfuge Skill (e.g., Finesse Blades OR Stealth). Reaches Master Rank (4d10, Floor 7) at Lvl 9 (DEX d10).	16 Total Allocations (Good Track) across 3-4 domains (e.g., Stealth, Lockpicking, Acrobatics, Deception, Bows).	When Swinging Finesse Blade: Rolls 4d10 keep highest (Floor 7) (or 5d10 on Sneak Attack +1B). Matches Fighter precision!<br>When Picking Lock: Rolls Master Rank (4d10, Floor 7), surgically reliable.
Wizard (Arcane Caster Anchor)	1 Primary Magic Tradition (e.g., Arcana / Pyromancy) under Lore & Arcana. Reaches Master Rank (4d12 keep highest, Floor 7) at Lvl 9 automatically (INT d12).	13 Total Allocations (Okay Track) across 2 domains (e.g., History, Arcana Lore, Medicine, Diplomacy).	When Casting Fireball: Rolls 4d12 keep highest (Floor 7) (or 5d12 on Focus Step-Up). Automatic Master spellcaster.<br>When Swinging Greatsword: Rolls Untrained (2d6, Floor 0), completely outclassed by Fighter.
3. How the Math Works Against Defenses (Opposed Combat & Magic Math)

With Option 3 locked in, combat and spellcasting checks against our four defenses operate with complete mathematical symmetry across both modes (Opposed Contests Mode 2/3 and Fixed DCs Mode 1/3):

3.1 Melee Strikes vs. Parry (Active Martial Clash)
Attacker Pool: Weapon Specific Skill Pool (e.g., Master Fighter rolls 4d12 keep highest, Floor 7).
Defender Pool: Weapon/Shield Specific Skill Pool (e.g., Veteran Knight rolls 3d10 keep highest, Floor 5).
Resolution (Zero Math): Compare Highest Face vs Highest Face (12 vs 9). Attacker wins! Extra attacker dice (say, rolling 8 and 10) beat the Knight's 9, awarding +1 Special Effect Token ([SET]) (or +2 if Max Face 12) to execute Impale, Trip, or Bypass Soak (DEC-034)!
3.2 Ranged Strikes & Area Spells vs. Reflexes (DEX+INT Dodge Pool)
Attacker Pool: Ranged Weapon OR Spell Tradition Pool (e.g., Master Wizard rolls Pyromancy 4d12 keep highest, Floor 7).
Defender Pool: Reflexes Paired Defense Pool (1dDEX + 1dINT keep highest + Good Save Boons) (DEC-022 — e.g., Rogue rolls DEX d10 + INT d8 + Good Save +2B -> 4d10 keep highest, Floor 5).
Resolution (Zero Math): Compare Pyromancy Highest Face vs Reflexes Highest Face. If Spell > Reflexes, spell hits! If Reflexes >= Spell, target dodges cleanly (0 Wounds).
3.3 Internal / Metabolic Spells vs. Resilience (Fortitude STR+CON | Willpower WIS+CHA)
Attacker Pool: Spell Tradition Pool (e.g., Necromancy 4d12, Floor 7).
Defender Pool: Fortitude Pool (1dSTR + 1dCON) vs. Poison/Death; OR Willpower Pool (1dWIS + 1dCHA) vs. Mind Blasts/Curses (DEC-022).
Resolution (Zero Math): Compare Spell Highest Face vs Resilience Highest Face. If Spell > Resilience, target suffers the internal spell condition (Dazed, Paralyzed, Charmed).
3.4 Post-Hit Impact vs. Soak Rank (Armor Die vs Damage Die)
When any physical attack or spell blast beats Reflexes or Parry, it checks Soak Rank (Armor Die: d4 Cloth -> d12 Plate — DEC-005):

Impact Check: 
max
⁡
(
Damage Die Face
)
 vs 
max
⁡
(
Soak Die Face
)
Impact Check: max(Damage Die Face) vs max(Soak Die Face)
If Damage <= Soak: Kinetic shock absorbed (0 Wounds).
If Damage > Soak: Target loses normal Vitality (HP). Can inflict quick minor disruptions (Bleed, Off-balance).
If Critical Hit (d100 Threat Profile OR Called Shot [2 SET] — DEC-034): Double Vitality loss + Severe Anatomical Wound Condition (Roll 1d8 Location Matrix)!
Open
used
Bash
97ms

We have evaluated the three architectural models for physical attacks and spellcasting against our baseline design (Model A check pools, Competency Floors, 6-Tier High Fantasy Scale, and 4 Paired Defenses) and formalized our definitive baseline in 03_core_baseline_system/12_attacks_and_spells_vs_skills_architecture.md (presented above), recorded under decision DEC-041.

🏛️ The Three Candidate Models (Pros & Cons)
Option 1: The Skill-Unified Engine (Attacks & Spells ARE Specific Skills)
How it works (Mythras / BRP / Year Zero approach): No separate BAB or Caster Level pool track on the class table. Instead, Combat Mastery (Blades, Bows, Shields) and Lore & Arcana (Arcana, Divine traditions) are specific skills listed under our 5 Action Mastery Domain umbrellas (DEC-030). When you level up and spend general Skill Allocations (Track 5), you invest right in Longswords, or Pyromancy, or Diplomacy.
🟢 Major Pros:
100% Universal Check Rule: Zero mechanical distinction between swinging a sword, picking a lock, negotiating a treaty, or casting a fireball! Every single check is: Attribute Die Size (X) + Skill Competency Volume & Floor (N & F).
Total Player Freedom: You can build a battle-mage who invests equally in Longswords and Arcana, or a noble knight who invests in Polearms and Diplomacy. You don't get arbitrary 
+
𝐵
𝐴
𝐵
+BAB stats just from your class name; you get good at what you actively practice!
🔴 Major Cons:
The "Skill Allocation Tax" Dilemma: If a Fighter only receives 1 skill allocation every 2 levels (Bad/Combat track progression), but must spend those allocations just to raise his sword skill from Trained -> Expert -> Master to keep up with enemy Parry/Reflex defenses, then the Fighter has zero skill allocations left over to invest in Athletics, Survival, or Perception! His entire skill budget becomes a mandatory weapon skill tax.
Option 2: The D&D / Pathfinder Split Engine (Separate Class Tracks Apart from Skills)
How it works (D&D 3.5e / PF2e approach): Your ability to hit (Combat Pool) and your ability to cast (Spell Power Pool) exist on dedicated Class Advancement Tracks (DEC-035 Track 2 & Track 4), completely separate from your general Skill Competency Allocations (Track 5: Stealth, Lockpicking, Arcana Lore, Diplomacy).
🟢 Major Pros:
No Skill Tax (Protects General Competence): Fighters automatically hit hard with their weapons (reaching Expert Floor 5 at Lvl 5, Master Floor 7 at Lvl 9) via their class track (DEC-029), allowing them to spend their 9 to 14 General Skill Allocations on becoming a master mountaineer (Athletics), a wilderness scout (Survival), or a military commander (Leadership).
Immediate 3.5e Familiarity: Preserves the exact structural separation of HP, BAB, Saves, CL, and Skills (DEC-029).
🔴 Major Cons:
Mechanical Bifurcation: Creates two parallel mechanisms for how check pools advance (one automatic by class level for attacks/spells, one purchased via skill allocations for out-of-combat skills).
Option 3: The Hybrid "Class-Granted Domain Allocations" Engine (Locked Baseline — DEC-041)

To combine the elegant universality of Option 1 (Attacks and Spells ARE specific skills under our 5 domains) with the zero-skill-tax protection of Option 2 (distinct class identity and automatic core role mastery), we establish Option 3: The Hybrid Class-Granted Allocations Engine:

text
[ Universal Skill Ecosystem: How Competency Ranks Advance ]
  ├── 1. Class-Granted Primary Allocations (`Automatic Role Mastery — Zero Tax`)
  │     └── At Levels 1, 5, 9, and 15 (`Tier Boundaries`), your Class automatically elevates ONE primary class skill (`e.g., Longswords for Fighter; Pyromancy for Wizard`) to the next Competency Rank (`Trained -> Expert Floor 5 -> Master Floor 7 -> Legend Floor 9`).
  │
  └── 2. General Skill Allocations (`Track 5 — Universal Out-of-Combat Customization`)
        └── At Levels 1, 2, 4, 6, 7, 10, 12, 14, 17, 18, you receive general skill allocations to invest freely in ANY specific skill (`Stealth, Lockpicking, Diplomacy, Medicine, Athletics, OR even a second weapon/spell style like Bows or Necromancy`)!
Why Option 3 is our definitive baseline:
100% Universal Rule (Option 1 Benefit): Everything on the sheet (Swords, Spells, Diplomacy, Stealth) uses the exact same 5 Competency Ranks (Untrained 0 -> Trained 3 -> Expert Floor 5 -> Master Floor 7 -> Legend Floor 9) and exact same Model A check pool engine (Die Size X from Attribute, Pool Volume N and Floor F from Competency Rank — DEC-038)!
Zero Skill Tax (Option 2 Benefit): Because Classes award dedicated primary skill rank upgrades at Tier boundaries (Levels 1, 5, 9, 15), Fighters and Wizards automatically hit their required Expert, Master, and Legend attack/spell floors in their core vocation (no skill allocation tax!), while retaining their full budget of General Skill Allocations to customize their out-of-combat identities!
⚔️ How the Math Works Against All 4 Defenses (Zero Math)

With Option 3 locked in, combat and spellcasting checks operate with complete mathematical symmetry across both modes (Opposed Contests Mode 2/3 and Fixed DCs Mode 1/3):

Melee Strikes vs. Parry (Active Martial Clash):
Attacker Pool: Weapon Specific Skill Pool (e.g., Master Fighter rolls 4d12 keep highest, Floor 7).
Defender Pool: Weapon/Shield Specific Skill Pool (e.g., Veteran Knight rolls 3d10 keep highest, Floor 5).
Resolution: Compare Highest Face vs Highest Face (12 vs 9). Extra attacker dice (say, rolling 8 and 10) beat the Knight's 9, awarding +1 Special Effect Token ([SET]) (or +2 if Max Face 12) to execute Impale, Trip, or Bypass Soak (DEC-034)!
Ranged Strikes & Area Spells vs. Reflexes (DEX+INT Dodge Pool):
Attacker Pool: Ranged Weapon OR Spell Tradition Pool (e.g., Master Wizard rolls Pyromancy 4d12 keep highest, Floor 7).
Defender Pool: Reflexes Paired Defense Pool (1dDEX + 1dINT keep highest + Good Save Boons) (DEC-022 — e.g., Rogue rolls DEX d10 + INT d8 + Good Save +2B -> 4d10 keep highest, Floor 5).
Resolution: Compare Pyromancy Highest Face vs Reflexes Highest Face. If Spell > Reflexes, spell hits! If Reflexes >= Spell, target dodges cleanly (0 Wounds).
Internal / Metabolic Spells vs. Resilience (Fortitude STR+CON | Willpower WIS+CHA):
Attacker Pool: Spell Tradition Pool (e.g., Necromancy 4d12, Floor 7).
Defender Pool: Fortitude Pool (1dSTR + 1dCON) vs. Poison/Death; OR Willpower Pool (1dWIS + 1dCHA) vs. Mind Blasts/Curses (DEC-022).
Resolution: Compare Spell Highest Face vs Resilience Highest Face. If Spell > Resilience, target suffers the internal spell condition (Dazed, Paralyzed, Charmed).
Post-Hit Impact vs. Soak Rank (Armor Die vs Damage Die):
When any physical attack or spell blast beats Reflexes or Parry, check Soak Rank (Armor Die: d4 Cloth -> d12 Plate — DEC-005):

Impact Check: 
max
⁡
(
Damage Die Face
)
 vs 
max
⁡
(
Soak Die Face
)
Impact Check: max(Damage Die Face) vs max(Soak Die Face)
If Damage <= Soak: Kinetic shock absorbed (0 Wounds).
If Damage > Soak: Target loses normal Vitality (HP). Can inflict quick minor disruptions (Bleed, Off-balance).
If Critical Hit (d100 Threat Profile OR Called Shot [2 SET] — DEC-034): Double Vitality loss + Severe Anatomical Wound Condition (Roll 1d8 Location Matrix)!
🚀 Where Shall We Take Our Creative Focus Next?

With our check pool engine (DEC-038 Model A), attribute growth (DEC-039 / DEC-040), paired defenses (DEC-022), spatial tiers (DEC-031), and Option 3 hybrid attacks/spells architecture (DEC-041) completely locked in across 41 decisions, what would you like to explore next?

Design the Core Feat Compendium (General, Combat, and Racial Feats): Let's convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into clean 1-sentence mathless vector traits across our 6 tiers.
Flesh out the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Let's detail all 5 domains (Combat, Survival, Subterfuge, Lore, Social), building their exact specific skills (Stealth, Lockpicking, Arcana, Diplomacy) and maneuver options across all 5 competency ranks (Untrained to Legendary).
Build the Magic & Spellcasting Engine (Traditions & Vancian Grimoire): Let's define Vancian daily preparation across our 5 Traditions (Arcana, Divine, Primal, Shadow, Time), detail metamagic Focus costs, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Step-by-Step Character & Monster Walkthrough: Let's create a Tier 2 Veteran (Level 6) PC (say, a Human Greatsword Fighter or Elven Finesse Rogue) and a Tier 3 Master (Level 10) Boss monster (Ogre Mage or Lich King) from scratch to show the exact mathless formulas in action.

Which of these would you like to tackle right now?
