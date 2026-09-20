---
turn: 36
role: "AI-Designer"
source: chat_history.json
---

# Turn 36 — AI-Designer

used
Bash
87ms
Edited files
3
01_master_brainstorm_log.md
MD
Shadow of the Demon Lord & Weird Wizard: Comparative Analysis
MD
Shadow of the Demon Lord & Weird Wizard: Comparative Analysis

Robert J. Schwalb’s Shadow of the Demon Lord (SotDL) and Shadow of the Weird Wizard serve as our secondary architectural anchors. While SotDL revolutionized modern d20 design by replacing static numerical modifiers (+2 / -2) with dynamic Boons and Banes (Nd6) and introducing modular 3-Tier Paths, our system inherits its structural elegance and evolves it beyond table-side arithmetic into a full Mathless Step-Pool Engine.

This document compares our 8-Block Progression Ecosystem against SotDL across six architectural dimensions and provides exact side-by-side conversion and combat comparisons.

1. Architectural Comparison Matrix (SotDL vs. Our Mathless System)
Architectural Dimension	Shadow of the Demon Lord (SotDL / Weird Wizard)	Our Idealized Mathless System (Evolution & Upgrade)	Why Our System Elevates Simulationism & Flow
1. Resolution Formula & Table Arithmetic	
1
𝑑
20
+
Attribute Mod
±
Highest of 
𝑁
𝑑
6
1d20+Attribute Mod±Highest of Nd6 (Boons/Banes).<br>Requires table arithmetic on every check (e.g., d20 roll [14] + Str mod [+3] + highest boon d6 [+5] = 22 vs Defense 16).	NdX keep highest (Step Pools with Zero Math).<br>Attribute + Competency sets Die Size (X); Class + Boons sets Pool Volume (N). You roll the pool and compare highest face directly against Target DC or opposed die (max vs max).	Zero Arithmetic Latency. Eliminates linear addition equations completely ($d20 \pm d6$), delivering immediate visual clarity the moment dice stop spinning (DEC-001).
2. Boons & Banes Mechanism	Additive Extra Dice (Nd6). Boons add 
𝑁
𝑑
6
Nd6 (keep highest d6 and ADD to d20). Banes add 
𝑁
𝑑
6
Nd6 (keep highest d6 and SUBTRACT from d20). They cancel 1-to-1 before rolling.	Pool Volume Shifts (+1B / +1X). Boons add extra dice of the same step size directly to your check pool (+1B -> 3dX keep highest). Banes remove dice (+1X -> 1dX single roll). They cancel 1-to-1 (DEC-003).	Preserves SotDL’s brilliant 1-to-1 cancellation without reintroducing table-side arithmetic or mixing multi-size dice (DEC-017).
3. Progression & Class Structure	3-Tier Path Layering (10 Levels Total).<br>• Novice Path (Lvl 1-2): Core role (Warrior, Priest).<br>• Expert Path (Lvl 3-6): Profession (Berserker, Paladin).<br>• Master Path (Lvl 7-10): High concept (Blade Dancer).	6-Tier Path Layering across 20 Levels (and Epic 21+).<br>We expand SotDL's paths into 4-level bands across 6 High Fantasy Tiers (Trained Lvl 1-4 -> Veteran Lvl 5-8 -> Master Lvl 9-12 -> Hero Lvl 13-16 -> Legend Lvl 17-20 -> Mythic Lvl 21+). Applied universally to PCs and Monsters (DEC-011).	Combines SotDL’s modular path selection (zero dead levels or prerequisite traps) with D&D 3.5e/PF2e’s granular level-by-level growth across 20 levels (DEC-013).
4. Skill & Competency Granularity	Freeform Professions (No Skill Lists). Players list professions (e.g., Blacksmith, Sailor). If relevant to a check, GM awards 
+
1
 Boon (‘+1d6‘)
+1 Boon (‘+1d6‘) (or +2 Boons).	5 Action Mastery Domains (Combat, Survival, Subterfuge, Lore, Social) & 5 Competency Ranks (Untrained 0 to Legendary 9).<br>Advancing competency steps up Die Size (X+1 to X+3), increases Pool Volume (+1B to +3B), and sets Competency Floors (Fixed Die Minimums).	SotDL professions lack advancement (a Blacksmith at Lvl 1 gets +1 Boon; at Lvl 10 still gets +1 Boon). Our Competency Ranks give explicit, investment-driven growth where experts literally cannot whiff on routine checks (DEC-019).
5. Defense & Mitigation Model	Single Passive Defense Score (10 to 18). If light/unarmored, Defense = Agility. Heavy armor (Plate = Defense 17) completely overrides and replaces Agility. Damage drains a single linear Health bar.	4 Paired Defensive Layers (Reflexes DEX+INT, Parry Combat Pool, Resilience Fort/Will, and Soak Rank Armor Die).<br>Soak is checked post-hit (Damage vs Soak). Active parrying burns Stamina (Parry Fatigue). Severe hits trigger our 1d8 Anatomical Matrix (DEC-009).	Solves SotDL’s armor flaw (where heavy armor makes agility irrelevant). In our system, Plate armor does not prevent getting hit; it provides a massive Soak d12 step that absorbs kinetic damage cleanly post-hit!
6. Criticals & Maneuver Access	Pre-Roll Penalty Trap. To perform maneuvers (Called Shot, Disarm, Shove), players must accept 
−
1
 or 
−
2
 Banes (‘-1d6/-2d6‘)
−1 or −2 Banes (‘-1d6/-2d6‘) before rolling. Crits trigger on total 
≥
20
≥20 over Defense (dealing +2d6 damage).	Post-Roll Differential Tokens ([SET] Engine). Players roll their full check pool without pre-roll penalties! If your highest die wins and extra dice beat the opponent's roll (Multi-Beat Differential), you earn Special Effect Tokens ([SET]) spent instantly on maneuvers (Impale, Bleed, Disarm, Riposte).	Eliminates SotDL’s pre-roll penalty trap (where players avoid maneuvers for fear of missing). In our system, every solid hit naturally generates tactical maneuver choices (DEC-007).
2. Side-by-Side Combat Walkthrough (Level 6 Berserker Clash)

To see how our system translates and elevates a classic SotDL encounter in real time, let's trace a Level 6 Human Berserker (Expert Path) attacking an Ogre Brute (Large Giant) across both systems side-by-side:

Scenario Setup
The Player Character: Level 6 Human Berserker (Strength high, wielding a Greatsword).
The Target: Ogre Brute (Large size, thick hide + leather apron).
Tactical Context: The Berserker enters Berserk Rage (gaining offensive boons at the cost of defensive vulnerability) and charges the Ogre!
Phase 1: SotDL Resolution (The Arithmetic Engine)
SotDL Character Stats: Strength 14 (+4 modifier), Berserker Rage (+1 Boon on attacks), Greatsword (3d6 damage). Ogre has Defense 13, Health 40.
Declaring the Attack: The Berserker charges and declares a standard attack.
Rolling the Check: The player rolls 
1
𝑑
20
+
Str Mod (+4)
+
1
𝑑
6
 (Boon)
1d20+Str Mod (+4)+1d6 (Boon).
Rolled: 
𝑑
20
d20 shows 11. Boon 
𝑑
6
d6 shows 5.
Table Arithmetic: 11 (d20) + 4 (Str Mod) + 5 (Boon d6) = 20 total vs Defense 13.
Evaluating Outcome: Total 20 beats Defense 13 by 7 (Hit!). Because total is 
≥
20
≥20 AND beats Defense, it is a Critical Hit (+2d6 damage).
Damage & Health Depletion: Player rolls 3d6 (Greatsword) + 2d6 (Crit) = 5d6 total damage.
Rolled Damage: 4 + 5 + 3 + 6 + 2 = 20 damage.
Table Arithmetic: Ogre subtracts 20 from Health (Health 40 - 20 = 20 Health remaining). The Ogre is bruised, but suffers zero anatomical impairment.
Phase 2: Our Mathless Resolution (The Tri-Vector & [SET] Engine)
Our Converted Character Stats:
Die Size (X): Base STR d10 (upgraded at Lvl 4) + Expert in Combat Mastery (+1 Step-Up) 
→
→ d12 (Competency Floor 5).
Pool Volume (N): Base 2d + Martial Class (+1B) + Berserk Rage (+1B) 
→
→ 4d12 keep highest check pool.
Greatsword: Damage Die d10 vs Soak, 3 Durability Slots.
Ogre Profile: Parry Pool 3d10, Soak Rank d10 (Thick Hide+Apron), Vitality 24.
Declaring the Attack: The Berserker charges ([2A] Sudden Charge) and rolls 4d12 keep highest directly against the Ogre's opposed Parry Pool (3d10).
Rolling the Opposed Check (Zero Math):
Berserker Rolls (4d12): 4, 7, 9, 12. Highest Face = 12 (Floor 5 guaranteed).
Ogre Parry Rolls (3d10): 3, 6, 8. Highest Face = 8.
Evaluating Outcome (Max vs Max & [SET] Generation):
Winner Check: Berserker Highest (12) > Ogre Highest (8) 
→
→ Hit!
Token Generation (Multi-Beat Differential): Look at the Berserker's remaining dice (4, 7, 9). Die 9 beats the Ogre's 8 (+1 [SET]). Furthermore, the Berserker rolled his Maximum Face Value (12 on d12) (+1 [SET]).
Total Earned: Standard Hit + 2 Special Effect Tokens ([SET]) to spend instantly!
Damage vs Soak & Anatomical Severance (Zero Math):
Soak Check: Because the Berserker rolled Max Face (12), the hit is automatically a Critical Damage Hit against the Ogre's Soak d10.
Vitality Loss: Ogre takes Double Vitality loss (Max Face 10 x 2 = 20 Vitality lost -> 4 Vitality remaining).
Anatomical 1d8 Location Roll: Player rolls 1d8 Anatomical Matrix and gets 6 (Weapon Arm Hit). The Ogre's massive Greatclub drops to the ground instantly (Limp Weapon Arm condition).
Spending [SET] Tokens: The Berserker spends his 2 [SET] tokens on Riposte Guard (1 [SET]) (preparing a free un-parriable counter-strike) and Trip (1 [SET]) (sweeping the crippled Ogre Prone into the dirt)!
3. Summary of Simulationist Superiority

Notice the profound difference in the two play experiences:

In SotDL, the player did three linear addition equations (11+4+5 = 20, 4+5+3+6+2 = 20, 40-20 = 20), and the Ogre simply lost half its HP bar while standing still.
In Our Mathless System, the player did zero addition (comparing faces 12 vs 8), generated 2 tactical maneuver tokens right off his rolled dice, shattered the Ogre's primary arm (forcing it to drop its weapon via our 1d8 matrix), and knocked the monster sprawling Prone into the dirt!
Open

We have conducted a direct, 6-dimension structural comparison between our 8-Block Universal Mathless Check Pool Ecosystem and Robert J. Schwalb’s Shadow of the Demon Lord (SotDL / Shadow of the Weird Wizard), now archived in 02_comparative_system_analysis/05_sotdl_and_weird_wizard_comparative_analysis.md (presented above) and recorded under decision DEC-026.

While SotDL serves as one of our core inspirations (specifically for Boons/Banes and 3-Tier Paths), our system inherits its strengths while solving its table-side arithmetic and passive defense limitations:

🏛️ The 6-Dimension Comparison (Where We Inherit vs. Where We Evolve)
Architectural Dimension	Shadow of the Demon Lord (SotDL / Weird Wizard)	Our Idealized Mathless System (Evolution & Upgrade)	Why Our System Elevates Simulationism & Flow
1. Resolution Formula & Table Arithmetic	
1
𝑑
20
+
Attribute Mod
±
Highest of 
𝑁
𝑑
6
1d20+Attribute Mod±Highest of Nd6 (Boons/Banes).<br>Requires table arithmetic on every check (e.g., d20 roll [14] + Str mod [+3] + highest boon d6 [+5] = 22 vs Defense 16).	NdX keep highest (Step Pools with Zero Math).<br>Attribute + Competency sets Die Size (X); Class + Boons sets Pool Volume (N). You roll the pool and compare highest face directly against Target DC or opposed die (max vs max).	Zero Arithmetic Latency. Eliminates linear addition equations completely ($d20 \pm d6$), delivering immediate visual clarity the moment dice stop spinning (DEC-001).
2. Boons & Banes Mechanism	Additive Extra Dice (Nd6). Boons add 
𝑁
𝑑
6
Nd6 (keep highest d6 and ADD to d20). Banes add 
𝑁
𝑑
6
Nd6 (keep highest d6 and SUBTRACT from d20). They cancel 1-to-1 before rolling.	Pool Volume Shifts (+1B / +1X). Boons add extra dice of the same step size directly to your check pool (+1B -> 3dX keep highest). Banes remove dice (+1X -> 1dX single roll). They cancel 1-to-1 (DEC-003).	Preserves SotDL’s brilliant 1-to-1 cancellation without reintroducing table-side arithmetic or mixing multi-size dice (DEC-017).
3. Progression & Class Structure	3-Tier Path Layering (10 Levels Total).<br>• Novice Path (Lvl 1-2): Core role (Warrior, Priest).<br>• Expert Path (Lvl 3-6): Profession (Berserker, Paladin).<br>• Master Path (Lvl 7-10): High concept (Blade Dancer).	6-Tier Path Layering across 20 Levels (and Epic 21+).<br>We expand SotDL's paths into 4-level bands across 6 High Fantasy Tiers (Trained Lvl 1-4 -> Veteran Lvl 5-8 -> Master Lvl 9-12 -> Hero Lvl 13-16 -> Legend Lvl 17-20 -> Mythic Lvl 21+). Applied universally to PCs and Monsters (DEC-011).	Combines SotDL’s modular path selection (zero dead levels or prerequisite traps) with D&D 3.5e/PF2e’s granular level-by-level growth across 20 levels (DEC-013).
4. Skill & Competency Granularity	Freeform Professions (No Skill Lists). Players list professions (e.g., Blacksmith, Sailor). If relevant to a check, GM awards 
+
1
 Boon (‘+1d6‘)
+1 Boon (‘+1d6‘) (or +2 Boons).	5 Action Mastery Domains (Combat, Survival, Subterfuge, Lore, Social) & 5 Competency Ranks (Untrained 0 to Legendary 9).<br>Advancing competency steps up Die Size (X+1 to X+3), increases Pool Volume (+1B to +3B), and sets Competency Floors (Fixed Die Minimums).	SotDL professions lack advancement (a Blacksmith at Lvl 1 gets +1 Boon; at Lvl 10 still gets +1 Boon). Our Competency Ranks give explicit, investment-driven growth where experts literally cannot whiff on routine checks (DEC-019).
5. Defense & Mitigation Model	Single Passive Defense Score (10 to 18). If light/unarmored, Defense = Agility. Heavy armor (Plate = Defense 17) completely overrides and replaces Agility. Damage drains a single linear Health bar.	4 Paired Defensive Layers (Reflexes DEX+INT, Parry Combat Pool, Resilience Fort/Will, and Soak Rank Armor Die).<br>Soak is checked post-hit (Damage vs Soak). Active parrying burns Stamina (Parry Fatigue). Severe hits trigger our 1d8 Anatomical Matrix (DEC-009).	Solves SotDL’s armor flaw (where heavy armor makes agility irrelevant). In our system, Plate armor does not prevent getting hit; it provides a massive Soak d12 step that absorbs kinetic damage cleanly post-hit!
6. Criticals & Maneuver Access	Pre-Roll Penalty Trap. To perform maneuvers (Called Shot, Disarm, Shove), players must accept 
−
1
 or 
−
2
 Banes (‘-1d6/-2d6‘)
−1 or −2 Banes (‘-1d6/-2d6‘) before rolling. Crits trigger on total 
≥
20
≥20 over Defense (dealing +2d6 damage).	Post-Roll Differential Tokens ([SET] Engine). Players roll their full check pool without pre-roll penalties! If your highest die wins and extra dice beat the opponent's roll (Multi-Beat Differential), you earn Special Effect Tokens ([SET]) spent instantly on maneuvers (Impale, Bleed, Disarm, Riposte).	Eliminates SotDL’s pre-roll penalty trap (where players avoid maneuvers for fear of missing). In our system, every solid hit naturally generates tactical maneuver choices (DEC-007).
⚔️ Side-by-Side Combat Showdown (Level 6 Berserker vs. Ogre Brute)

Notice what happens at the table during a real combat turn when a Level 6 Berserker charges an Ogre Brute:

In Shadow of the Demon Lord (SotDL):
Player Math: The player rolls 
𝑑
20
 (11)
+
Str Mod (+4)
+
Boon d6 (5)
=
20
 total
d20 (11)+Str Mod (+4)+Boon d6 (5)=20 total.
Outcome: 20 beats Defense 13 (Hit!). Because total is 
≥
20
≥20, it crits (+2d6 damage).
Damage Math: Player rolls 3d6 (Greatsword) + 2d6 (Crit) 
→
→ 4+5+3+6+2 = 20 damage. Ogre subtracts 20 from Health (40 - 20 = 20 Health remaining).
The Experience: The player did three linear addition equations (11+4+5=20, 4+5+3+6+2=20, 40-20=20). The Ogre stood still and lost half its HP bar.
In Our Mathless System:
Player Action (Zero Math): The Berserker charges ([2A] Sudden Charge) and rolls 4d12 keep highest (STR d10 + Expert step -> d12; Base 2d + Martial Class 1B + Berserk Rage 1B -> 4d) against the Ogre's opposed Parry Pool (3d10).
Rolled Faces: Berserker rolls 4, 7, 9, 12 (Highest = 12, guaranteed Floor 5). Ogre rolls 3, 6, 8 (Highest = 8).
Outcome (Max vs Max): 12 > 8 
→
→ Hit! Because 9 also beats 8 (Multi-beat), and 12 is the Max Face, the Berserker earns 2 Special Effect Tokens ([SET])!
Damage vs Soak (Zero Math): Because he rolled Max Face (12), the hit is automatically a Critical Damage Hit against the Ogre's Soak d10. Ogre loses double Vitality (10 x 2 = 20 Vitality lost -> 4 Vitality left).
Anatomical Severance (1d8 Location): Player rolls 1d8 Anatomical Matrix and gets 6 (Weapon Arm Hit). The Ogre's massive Greatclub drops instantly to the dirt (Limp Weapon Arm).
Spending [SET] Tokens: The Berserker spends his 2 [SET] tokens on Riposte Guard (1 [SET]) (preparing an un-parriable counter-strike) and Trip (1 [SET]) (sweeping the crippled Ogre sprawling Prone)!

Look at the difference: Zero arithmetic, instant tactical maneuver generation ([SET]), localized limb severance (dropped weapon), and dynamic prone control right off the rolled dice!

🚀 Where Shall We Focus Our Energy Next?

With SotDL fully analyzed and integrated into our comparative archives (26 logged decisions across 21 files), what would you like to build next?

Design the Core Feat Compendium (General, Combat, and Racial Feats): Convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into clean 1-sentence mathless vector traits across our 6 tiers.
Flesh out the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Detail all 5 domains (Combat, Survival, Subterfuge, Lore, Social), building their exact proficiencies, capability thresholds (Untrained vs Trained vs Expert vs Master vs Legend), and maneuver options (Shove, Trip, Grapple, Disarm, Feint, Demoralize).
Build the Magic & Spellcasting Engine: Define Focus channeling across our 5 Traditions (Arcana, Divine, Primal, Shadow, Time), spell interruption via anatomical head/chest hits, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Complete Step-by-Step Character & Monster Walkthrough: Build a Tier 2 Veteran (Level 6) PC and a Tier 3 Master (Level 10) Boss monster from scratch to show the exact mathless formulas in action.

Which direction shall we take right now?
