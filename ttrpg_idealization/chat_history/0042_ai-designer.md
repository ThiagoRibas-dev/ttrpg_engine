---
turn: 42
role: "AI-Designer"
source: chat_history.json
---

# Turn 42 — AI-Designer

used
Bash
81ms
Edited files
3
01_master_brainstorm_log.md
MD
D&D 3.5e Class Advancement Tracks: Mathless Translation Mapping
MD
D&D 3.5e Class Advancement Tracks: Mathless Translation Mapping

In Dungeons & Dragons 3.5e, class identity and power progression are governed by five linear numerical tracks: Hit Points (HP), Base Attack Bonus (BAB), Saving Throws (Fortitude, Reflex, Will), Caster Level (CL), and Skill Points.

This document maps how each of these five class advancement tracks translates directly into our High Fantasy Mathless Step-Pool System (across 20 Levels and 6 Tiers of Power) without requiring 
+
𝑋
/
−
𝑋
+X/−X arithmetic or multi-attack check subtraction (DEC-028).

1. Master Mapping Summary Table (3.5e vs. Our Mathless System)
D&D 3.5e Class Advancement Track	Traditional 3.5e Numerical Formula (Level 1 to 20)	Converted Mathless Equivalent (Our 20-Level Tri-Vector System)	Why Our Mathless Mapping Preserves Identity While Eliminating Bloat
1. Hit Points (HP)	Roll Class HD + CON mod every level.<br>(e.g., Fighter rolls 
1
𝑑
10
+
Con
1d10+Con up to 
200
+
 HP
200+ HP at Level 20).	Bounded Biological Vitality & Stamina Growth.<br>• Base Vitality (HP): STR Die Max + CON Die Max (e.g., 
8
+
10
=
18
8+10=18).<br>• Class Growth: At odd levels (3, 5, 7...), classes award Vitality Increments (+2 HP Martial, +1 HP Caster).<br>• Stamina (Poise): 2xCON Die Max. At even levels (2, 6, 10...), classes award Stamina Increments (+2 Stamina Martial, +1 Caster).	Eliminates HP sponge slogs (DEC-024 TTK Target). Vitality scales cleanly from 
∼
16
 HP
∼16 HP at Lvl 1 up to 
∼
36
 HP
∼36 HP at Lvl 20, keeping 3-5 hit tactical attrition intact across all tiers!
2. Base Attack Bonus (BAB)	Linear Attack Modifiers (+1 to +20).<br>• Full: 
+
1
/
Lvl
+1/Lvl (+20/+15/+10/+5).<br>• 3/4: 
+
0.75
/
Lvl
+0.75/Lvl (+15/+10/+5).<br>• Half: 
+
0.5
/
Lvl
+0.5/Lvl (+10/+5).	Tri-Vector Check Pool & Competency Floors (X, N, & F).<br>• Full Martial: Base 3dX keep highest (+1B) on weapons. Reaches Expert Floor 5 at Lvl 5, Master Floor 7 at Lvl 9, and Legend Floor 9 (5d12) at Lvl 15.<br>• 3/4 Hybrid: Base 2dX, but +1B (3dX) on class-favored weapons (Finesse rapier, Monk fist). Reaches Floor 5 at Lvl 7, Floor 7 at Lvl 13.<br>• Half Caster: Base 2dX (Floor 0 to 3) on physical weapons.	Replaces 
+
20
/
+
15
/
+
10
/
+
5
+20/+15/+10/+5 math and stationary full-attack paralysis with dynamic step pools (3d10 -> 4d12) and engineered hard caps where grandmasters literally cannot whiff (DEC-019).
3. Saving Throws (Fort, Ref, Will)	Linear Save Modifiers (+0 to +12).<br>• Good Save: Starts 
+
2
+2, scales 
+
0.5
/
Lvl
+0.5/Lvl (to +12).<br>• Poor Save: Starts 
+
0
+0, scales 
+
0.33
/
Lvl
+0.33/Lvl (to +6).	Paired Attribute Defense Pools + Class Defense Boons (+B).<br>• Base Pool: 1d(Attr 1) + 1d(Attr 2) keep highest (Fort STR+CON, Ref DEX+INT, Will WIS+CHA).<br>• Good Save Class Boon: If your class has a Good Save in 3.5e, your class awards +1B (+1 die volume -> 3dX) at Level 1, and elevates to +2B (4dX, Floor 5/7) at Level 9 (Master Tier Entry)!<br>• Poor Save Class: Standard 2dX paired pool (Floor 0/3).	Look at the cleanliness: A Level 10 Fighter making a Fortitude check rolls 4d10 keep highest (Floor 5) (Good Save +2B), but on Reflexes rolls 1d8 + 1d6 keep highest (Floor 0) (Poor Save). Exactly preserves 3.5e disparity without numbers!
4. Caster Level (CL 1st to 20th)	Linear Caster Level (CL 1 to 20).<br>Governs spell penetration (d20+CL vs SR), duration (1 round/Lvl), and damage dice (1d6/Lvl up to 10d6 Fireball).	Focus Pool Growth + Tradition Competency Ranks (Floor & Step).<br>• Focus Pool: Casters receive 
+
2
 to 
+
3
 Focus per level
+2 to +3 Focus per level (enabling more spells & Die Step-Ups).<br>• Spell Power Check Pool: Governed directly by Tradition Competency (Arcana, Divine): Trained rolls 3dX (Floor 3), Expert rolls 3dX+1 Step (Floor 5), Master rolls 4dX+2 Steps (Floor 7), Legend rolls 5dX+3 Steps (Floor 9).<br>• Damage & AoE: Spells scale via Die Step-Ups (d8 -> d10 -> d12 vs Soak) across Distance Tiers (DEC-028).	Eliminates rolling handfuls of 10d6 damage. High-tier spells roll clean, powerful over-cap step dice against target Evasion or Resilience, inflicting zone conditions (On Fire, Dazed) on hits!
5. Skill Points (2+Int to 8+Int)	Skill Point Counting & Cross-Class Math.<br>Fighters get 2+Int, Rogues get 8+Int. Class skills cost 1 point (cap Lvl+3); cross-class cost 2 points (cap half).	Action Mastery Domain Proficiency Allocations across 5 Domains.<br>• High-Skill (Rogue/Bard — 8+Int): Start Trained (+1B, Floor 3) across 3 or 4 Domains (Subterfuge, Social, Lore, Combat) and gain proficiency allocations every level (to master multiple domains).<br>• Medium-Skill (Ranger/Monk — 4+Int): Start Trained in 2 or 3 Domains.<br>• Combat/Heavy (Fighter/Wizard — 2+Int): Start Trained in 1 or 2 Domains (Combat for Fighter; Lore for Wizard). Elevate primary domain to Legendary (Floor 9), but rely on balanced secondary pools for off-domains.	Eliminates tracking 35 skill points. Players invest domain allocations (DEC-020) right into our 5 mastery domains (Combat, Survival, Subterfuge, Lore, Social) across all 20 levels!
2. Detailed Track-by-Track Mechanics
2.1 Base Attack Bonus vs. Tri-Vector Check Pool Scaling

In 3.5e, BAB dictates when you hit and how many attacks you make ($+6/+1$ at Level 6). In our system, multi-attacks are governed by our 3-action economy ([A][A][A]), while combat check pools scale at clear Tier boundaries:

Class BAB Tier	Level 1 (Trained) Pool	Level 5 (Veteran Entry) Pool	Level 9 (Master Entry) Pool	Level 15 (Legend Entry) Pool	Level 20 (Apex Legend) Pool
Full Martial (Fighter, Barbarian)	3d8 keep highest<br>(Floor 3)	3d10 keep highest<br>(Floor 5 — Expert)	4d12 keep highest<br>(Floor 7 — Master)	5d12 keep highest<br>(Floor 9 — Legend)	5d12+2 over-cap pool<br>(Floor 9 + Apex Crit Surge)
3/4 Hybrid (Rogue, Cleric, Monk)	2d8 (3d8 favored)<br>(Floor 0/3)	3d10 keep highest<br>(Floor 3/5 favored)	3d12 keep highest<br>(Floor 5 — Expert)	4d12 keep highest<br>(Floor 7 — Master)	5d12 keep highest<br>(Floor 9 favored)
Half Caster (Wizard, Sorcerer)	2d6 keep highest<br>(Floor 0)	2d8 keep highest<br>(Floor 0)	2d10 keep highest<br>(Floor 3 — Trained)	3d10 keep highest<br>(Floor 3)	3d12 keep highest<br>(Floor 5 — Expert)
2.2 Saving Throws vs. Paired Defense Pool Scaling

Below is how a Level 10 Fighter (Good Fortitude, Poor Reflex/Will) and a Level 10 Wizard (Good Will, Poor Fortitude/Reflex) make their defense checks side-by-side without a single numerical bonus:

Defense Category	Level 10 Fighter (Saves in 3.5e: Fort +7, Ref +3, Will +3)	Level 10 Wizard (Saves in 3.5e: Fort +3, Ref +3, Will +7)	Tactical & Simulationist Reality
Fortitude (STR + CON)<br>(vs Poisons, Disease, Stun)	4d10 keep highest (Floor 5)<br>(STR d10 + CON d10 base paired 2d10 + Good Save +2B -> 4d10)	2d8 keep highest (Floor 3)<br>(STR d6 + CON d8 base paired 2d8 + Poor Save +0B -> 2d8)	The Fighter rolls 4d10 (Floor 5), mathematically immune to standard DC 5 poisons and outclassing the Wizard's 2d8 resilience.
Reflexes (DEX + INT)<br>(vs Fireballs, Traps, AoE)	1d8 + 1d6 keep highest (Floor 0)<br>(DEX d8 + INT d6 base paired pool + Poor Save +0B)	1d10 + 1d6 keep highest (Floor 3)<br>(DEX d6 + INT d10 base paired pool + Poor Save +0B)	Look at the balance: Because Reflexes is DEX+INT (DEC-022), the Wizard's high INT d10 spatial logic allows him to dodge just as well as the athletic Fighter (d8)!
Willpower (WIS + CHA)<br>(vs Mind Blasts, Fear, Curses)	2d6 keep highest (Floor 0)<br>(WIS d6 + CHA d6 base paired pool + Poor Save +0B)	4d10 keep highest (Floor 5)<br>(WIS d10 + CHA d10 base paired 2d10 + Good Save +2B -> 4d10)	The Wizard rolls 4d10 (Floor 5), easily shrugging off mind blasts and curses where the Fighter (2d6) remains vulnerable.
3. Side-by-Side Class Progression Table (Fighter vs. Wizard vs. Rogue at Key Levels)
Level & Scope	Fighter (Full Martial, Good Fort)	Rogue (3/4 Hybrid, Good Ref, High Skill)	Wizard (Half Caster, Good Will, High Arcana)
Level 1<br>(Trained)	• Combat Pool: 3d8 (Floor 3)<br>• Fortitude: 3d8 (Good +1B)<br>• Vitality: 18 HP, Stamina: 16<br>• Skills: 1 Domain (Combat) at Trained.	• Combat Pool: 3d8 (Finesse blades)<br>• Reflexes: 3d8 (Good +1B)<br>• Vitality: 14 HP, Stamina: 14<br>• Skills: 3 Domains (Subterfuge, Social, Combat) at Trained.	• Arcana Pool: 3d8 (Floor 3) (Spells)<br>• Willpower: 3d8 (Good +1B)<br>• Vitality: 12 HP, Focus: 16 Pool<br>• Skills: 1 Domain (Lore & Arcana) at Trained.
Level 5<br>(Expert Entry)	• Combat Pool: 3d10 (Floor 5)<br>• Fortitude: 3d10 (Good +1B)<br>• Vitality: 22 HP, Stamina: 20<br>• Maneuvers: Power Strike [1A], Riposte [SET].	• Combat Pool: 3d10 (Sneak Attack +1B on flat-footed)<br>• Reflexes: 3d10 (Good +1B)<br>• Vitality: 16 HP, Stamina: 16<br>• Skills: Elevate Subterfuge to Expert (Floor 5).	• Arcana Pool: 3d10 (Floor 5)<br>• Willpower: 3d10 (Good +1B)<br>• Vitality: 14 HP, Focus: 24 Pool<br>• Spells: Fireball [2A] (d10 vs Reflexes across Tier 1).
Level 9<br>(Master Entry)	• Combat Pool: 4d12 (Floor 7)<br>• Fortitude: 4d12 (Good +2B)<br>• Vitality: 26 HP, Stamina: 24<br>• Maneuvers: Sudden Charge [2A], Shatter Armor [SET].	• Combat Pool: 3d12 (or 4d12 on Sneak Attack)<br>• Reflexes: 4d12 (Good +2B)<br>• Vitality: 18 HP, Stamina: 18<br>• Skills: Elevate Subterfuge and Combat to Master (Floor 7).	• Arcana Pool: 4d12 (Floor 7)<br>• Willpower: 4d12 (Good +2B)<br>• Vitality: 16 HP, Focus: 34 Pool<br>• Spells: Cone of Cold [2A], Teleport [1A].
Level 15<br>(Legend Entry)	• Combat Pool: 5d12 (Floor 9)<br>• Fortitude: 5d12 (Good +2B)<br>• Vitality: 34 HP, Stamina: 30<br>• Maneuvers: Whirlwind Strike [3A], Double Hyper-Shift.	• Combat Pool: 4d12 (or 5d12 on Sneak Attack)<br>• Reflexes: 5d12 (Good +2B)<br>• Vitality: 24 HP, Stamina: 22<br>• Skills: Elevate Subterfuge to Legendary (Floor 9, 5d12).	• Arcana Pool: 5d12 (Floor 9)<br>• Willpower: 5d12 (Good +2B)<br>• Vitality: 20 HP, Focus: 48 Pool<br>• Spells: Disintegrate [2A] (Damage d12+2 vs Fortitude), Time Stop [3A].
Open

We have mapped all 5 Classic D&D 3.5e Class Advancement Tracks (Hit Points, Base Attack Bonus, Saving Throws, Caster Level, and Skill Points) into our High Fantasy Mathless Step-Pool System (across 20 Levels and 6 Tiers of Power), now archived in 03_core_baseline_system/09_dnd_3_5e_class_advancement_tracks_mapping.md (presented above) and recorded under decision DEC-029.

🏛️ Track-by-Track Translation Matrix
D&D 3.5e Class Track	Traditional Numerical Formula (Level 1 to 20)	Converted Mathless Equivalent (Our 20-Level Tri-Vector System)	Why Our Mathless Mapping Preserves Identity While Eliminating Bloat
1. Hit Points (HP)	Roll Class HD + CON mod every level.<br>(e.g., Fighter rolls 
1
𝑑
10
+
Con
1d10+Con up to 
200
+
 HP
200+ HP at Level 20).	Bounded Biological Vitality & Stamina Growth.<br>• Vitality (HP): STR Die Max + CON Die Max (e.g., 
8
+
10
=
18
8+10=18). At odd levels (3, 5, 7...), classes award Vitality Increments (+2 HP Martial, +1 HP Caster).<br>• Stamina (Poise): 2xCON Die Max. At even levels (2, 6, 10...), classes award Stamina Increments (+2 Stamina Martial, +1 Caster).	Eliminates HP sponge slogs (DEC-024 TTK Target). Vitality scales cleanly from 
∼
16
 HP
∼16 HP at Lvl 1 up to 
∼
36
 HP
∼36 HP at Lvl 20, keeping 3-5 hit tactical attrition intact across all tiers!
2. Base Attack Bonus (BAB)	Linear Attack Modifiers (+1 to +20).<br>• Full: 
+
1
/
Lvl
+1/Lvl (+20/+15/+10/+5).<br>• 3/4: 
+
0.75
/
Lvl
+0.75/Lvl (+15/+10/+5).<br>• Half: 
+
0.5
/
Lvl
+0.5/Lvl (+10/+5).	Tri-Vector Check Pool & Competency Floors (X, N, & F).<br>• Full Martial: Base 3dX keep highest (+1B) on weapons. Reaches Expert Floor 5 at Lvl 5, Master Floor 7 at Lvl 9, and Legend Floor 9 (5d12) at Lvl 15.<br>• 3/4 Hybrid: Base 2dX, but +1B (3dX) on class-favored weapons (Finesse rapier, Monk fist). Reaches Floor 5 at Lvl 7, Floor 7 at Lvl 13.<br>• Half Caster: Base 2dX (Floor 0 to 3) on physical weapons.	Replaces 
+
20
/
+
15
/
+
10
/
+
5
+20/+15/+10/+5 math and stationary full-attack paralysis with dynamic step pools (3d10 -> 4d12) and engineered hard caps where grandmasters literally cannot whiff (DEC-019).
3. Saving Throws (Fort, Ref, Will)	Linear Save Modifiers (+0 to +12).<br>• Good Save: Starts 
+
2
+2, scales 
+
0.5
/
Lvl
+0.5/Lvl (to +12).<br>• Poor Save: Starts 
+
0
+0, scales 
+
0.33
/
Lvl
+0.33/Lvl (to +6).	Paired Attribute Defense Pools + Class Defense Boons (+B).<br>• Base Pool: 1d(Attr 1) + 1d(Attr 2) keep highest (Fort STR+CON, Ref DEX+INT, Will WIS+CHA).<br>• Good Save Class Boon: If your class has a Good Save in 3.5e, your class awards +1B (+1 die volume -> 3dX) at Level 1, and elevates to +2B (4dX, Floor 5/7) at Level 9 (Master Tier Entry)!<br>• Poor Save Class: Standard 2dX paired pool (Floor 0/3).	Look at the cleanliness: A Level 10 Fighter making a Fortitude check rolls 4d10 keep highest (Floor 5) (Good Save +2B), but on Reflexes rolls 1d8 + 1d6 keep highest (Floor 0) (Poor Save). Exactly preserves 3.5e disparity without numbers!
4. Caster Level (CL 1st to 20th)	Linear Caster Level (CL 1 to 20).<br>Governs spell penetration (d20+CL vs SR), duration (1 round/Lvl), and damage dice (1d6/Lvl up to 10d6 Fireball).	Focus Pool Growth + Tradition Competency Ranks (Floor & Step).<br>• Focus Pool: Casters receive 
+
2
 to 
+
3
 Focus per level
+2 to +3 Focus per level (enabling more spells & Die Step-Ups).<br>• Spell Power Check Pool: Governed directly by Tradition Competency (Arcana, Divine): Trained rolls 3dX (Floor 3), Expert rolls 3dX+1 Step (Floor 5), Master rolls 4dX+2 Steps (Floor 7), Legend rolls 5dX+3 Steps (Floor 9).<br>• Damage & AoE: Spells scale via Die Step-Ups (d8 -> d10 -> d12 vs Soak) across Distance Tiers (DEC-028).	Eliminates rolling handfuls of 10d6 damage. High-tier spells roll clean, powerful over-cap step dice against target Evasion or Resilience, inflicting zone conditions (On Fire, Dazed) on hits!
5. Skill Points (2+Int to 8+Int)	Skill Point Counting & Cross-Class Math.<br>Fighters get 2+Int, Rogues get 8+Int. Class skills cost 1 point (cap Lvl+3); cross-class cost 2 points (cap half).	Action Mastery Domain Proficiency Allocations across 5 Domains.<br>• High-Skill (Rogue/Bard — 8+Int): Start Trained (+1B, Floor 3) across 3 or 4 Domains (Subterfuge, Social, Lore, Combat) and gain proficiency allocations every level (to master multiple domains).<br>• Medium-Skill (Ranger/Monk — 4+Int): Start Trained in 2 or 3 Domains.<br>• Combat/Heavy (Fighter/Wizard — 2+Int): Start Trained in 1 or 2 Domains (Combat for Fighter; Lore for Wizard). Elevate primary domain to Legendary (Floor 9), but rely on balanced secondary pools for off-domains.	Eliminates tracking 35 skill points. Players invest domain allocations (DEC-020) right into our 5 mastery domains (Combat, Survival, Subterfuge, Lore, Social) across all 20 levels!
⚔️ Side-by-Side Class Comparison (Level 10 Fighter vs. Rogue vs. Wizard)

Here is how three classic 3.5e classes look side-by-side at Level 10 (Master Tier Entry) under our converted tracks without a single numerical 
+
𝑋
/
−
𝑋
+X/−X bonus:

Track Category	Level 10 Fighter (Full Martial, Good Fort)	Level 10 Rogue (3/4 Hybrid, Good Ref, High Skill)	Level 10 Wizard (Half Caster, Good Will, High Arcana)
Check Pool (BAB)	4d12 keep highest (Floor 7)<br>(Master in Combat Mastery)	3d12 keep highest (Floor 5)<br>(Expert in Combat; 4d12 when Sneak Attacking flat-footed)	2d10 keep highest (Floor 3)<br>(Trained in physical weapons)
Primary Good Save	Fortitude (STR + CON): 4d10 keep highest (Floor 5)	Reflexes (DEX + INT): 4d10 keep highest (Floor 5)	Willpower (WIS + CHA): 4d10 keep highest (Floor 5)
Poor Saves	Reflex: 1d8 + 1d6 (Floor 0)<br>Will: 2d6 (Floor 0)	Fort: 2d8 (Floor 0)<br>Will: 2d8 (Floor 0)	Fort: 1d8 + 1d6 (Floor 0)<br>Reflex: 2d8 (Floor 0)
In-World Resources	Vitality: 26 HP, Stamina: 24, Focus: 14	Vitality: 18 HP, Stamina: 18, Focus: 18	Vitality: 16 HP, Stamina: 14, Focus: 34 Pool
Class Specialization	Power Strike [1A], Sudden Charge [2A], Shatter Armor [SET].	Master in Subterfuge & Social (Floor 7), Bleed [SET], Evade [R].	Master in Arcana Domain (4d12 pool, Floor 7), Fireball [2A], Teleport [1A].
🚀 Where Shall We Take Our Creative Focus Next?

With our 20-level class advancement tracks completely mapped and verified (29 logged decisions across 23 files), where would you like to focus our design work next?

Build the Core Feat Compendium (General, Combat, and Racial Feats): Let's convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into clean 1-sentence mathless vector traits across our 6 tiers.
Flesh out the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Let's detail all 5 domains (Combat, Survival, Subterfuge, Lore, Social), building their exact proficiencies, capability thresholds (Untrained vs Trained vs Expert vs Master vs Legend), and maneuver options (Shove, Trip, Grapple, Disarm, Feint, Demoralize).
Build the Magic & Spellcasting Engine: Let's define the exact rules for casting across our 5 Traditions (Arcana, Divine, Primal, Shadow, Time), spell interruption via anatomical head/chest hits, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Complete Step-by-Step Character & Monster Creation Walkthrough: Let's build a Tier 2 Veteran (Level 6) PC and a Tier 3 Master (Level 10) Boss monster from scratch to show the exact mathless formulas in action.

Which of these would you like to explore next?
