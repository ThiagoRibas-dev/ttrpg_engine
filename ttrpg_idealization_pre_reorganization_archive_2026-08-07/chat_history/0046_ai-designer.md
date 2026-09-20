---
turn: 46
role: "AI-Designer"
source: chat_history.json
---

# Turn 46 — AI-Designer

Edited files
21
01_master_brainstorm_log.md
MD
D&D 3.5e Class Advancement Tracks: Mathless 20-Level Progression Matrix
MD
D&D 3.5e Class Advancement Tracks: Mathless 20-Level Progression Matrix

In Dungeons & Dragons 3.5e, class identity and power progression are governed by five linear numerical tracks: Hit Points (HP), Base Attack Bonus (BAB), Saving Throws (Fortitude, Reflex, Will), Caster Level (CL), and Skill Points.

This document maps how each of these five class advancement tracks translates directly into our High Fantasy Mathless Step-Pool System (across 20 Levels and 6 Tiers of Power) without requiring 
+
𝑋
/
−
𝑋
+X/−X arithmetic or multi-attack check subtraction (DEC-028 & DEC-035).

1. Master Track Progression Rates (Good vs. Okay vs. Bad)

To give every class its distinct 3.5e identity (say, why a Fighter feels tanky and lethal while a Rogue feels surgical and highly skilled), each of the five tracks is assigned a progression rate: Good (Fast / High Cap), Okay (Medium / Balanced), or Bad (Poor / Low Cap).

text
[ Class Advancement Engine: The 5 Progression Tracks ]
  ├── 1. Vitality Increments (`HP`) ────► Good (+2/lvl), Okay (+1/lvl at odds), Bad (+1/lvl at evens)
  ├── 2. Check Pool & Floor (`BAB`) ────► Good (Expert Lvl 5 -> Legend Lvl 15), Okay (Lvl 7/13), Bad (Floor 3 cap)
  ├── 3. Paired Defenses (`Saves`) ─────► Good (+1B at Lvl 1, +2B at Lvl 9), Bad (+0B base paired pool)
  ├── 4. Vancian & Focus (`CL`) ────────► Good (Full 1st-9th Vancian + 3 Focus/lvl), Bad (0 Vancian, +1 Focus/lvl)
  └── 5. Domain Allocations (`Skills`) ─► Good (8+ allocations across 4 domains), Bad (2 allocations in 1 domain)
2. Master 20-Level Class Advancement Matrix (Side-by-Side Progression Rates)

Below is the exact progression awarded at every character level across the five tracks based on whether a class has a Good, Okay (Medium), or Bad (Poor) rate in that track:

Level	Scope & Tier	Track 1: Vitality Increments (HP Growth)	Track 2: Combat Pool & Floor (BAB Equivalent)	Track 3: Paired Defenses (Saving Throws)	Track 4: Vancian Magic & Focus (CL & Acuity)	Track 5: Skill Competency Allocations (Domain Ranks)
1	1 (Trained)	• Good: Base (STR+CON) + 4<br>• Okay: Base (STR+CON) + 2<br>• Bad: Base (STR+CON)	• Good: Base 3dX (Floor 3)<br>• Okay: Base 2dX (Floor 3)<br>• Bad: Base 2dX (Floor 0)	• Good: +1B (3dX keep highest)<br>• Bad: Base 2dX paired pool	• Good: 1st-Lvl Vancian Slots + 4 Focus<br>• Okay: 1st-Lvl Slots + 2 Focus<br>• Bad: 0 Vancian Slots + 2 Focus	• Good: 4 Allocations across 3-4 domains<br>• Okay: 3 Allocations across 2-3 domains<br>• Bad: 2 Allocations across 1-2 domains
2	1 (Trained)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
0
 HP
+0 HP (Stamina +2)	All tiers maintain Lvl 1 pool volume & floor.	All tiers maintain Lvl 1 defense boons.	• Good: 
+
3
 Focus
+3 Focus<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
0
 Allocations
+0 Allocations
3	1 (Trained)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
1
 HP
+1 HP	All tiers maintain Lvl 1 pool volume & floor.	All tiers maintain Lvl 1 defense boons.	• Good: 2nd-Lvl Vancian Slots 
+
3
 Focus
+3 Focus<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
0
 Allocations
+0 Allocations<br>• Bad: 
+
0
 Allocations
+0 Allocations
4	1 (Trained)	• Good: 
+
2
 HP
+2 HP (+Attr step)<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
0
 HP
+0 HP (Stamina +1)	• Good: +1 Boon (4dX)<br>• Okay/Bad: Maintain Lvl 1 pool.	• Good: +1B (+Attr step)<br>• Bad: Base paired pool	• Good: 
+
3
 Focus
+3 Focus (+Attr step)<br>• Okay: 1st-Lvl Hybrid Slots 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
1
 Allocation
+1 Allocation
5	2 (Veteran)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
1
 HP
+1 HP	• Good: Expert Rank (+1 Step, Floor 5) (Immune DC 5)<br>• Okay: 3dX (Floor 3)<br>• Bad: 2dX (Floor 3)	All tiers maintain defense boons across Veteran tier entry.	• Good: 3rd-Lvl Vancian Slots 
+
3
 Focus
+3 Focus<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
0
 Allocations
+0 Allocations
6	2 (Veteran)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
0
 HP
+0 HP	All tiers maintain Lvl 5 pool volume & floor.	All tiers maintain defense boons.	• Good: 
+
3
 Focus
+3 Focus<br>• Okay: 2nd-Lvl Hybrid Slots 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
0
 Allocations
+0 Allocations<br>• Bad: 
+
0
 Allocations
+0 Allocations
7	2 (Veteran)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
1
 HP
+1 HP	• Good: 4dX+1 Step (Floor 5)<br>• Okay: Expert Rank (+1 Step, Floor 5)<br>• Bad: Maintain 2dX (Floor 3)	All tiers maintain defense boons.	• Good: 4th-Lvl Vancian Slots 
+
3
 Focus
+3 Focus<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
1
 Allocation
+1 Allocation
8	2 (Veteran)	• Good: 
+
2
 HP
+2 HP (+Attr step)<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
0
 HP
+0 HP	All tiers maintain Lvl 7 pool volume & floor.	• Good: +1B (+Attr step)<br>• Bad: Base paired pool	• Good: 
+
3
 Focus
+3 Focus (+Attr step)<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
0
 Allocations
+0 Allocations<br>• Bad: 
+
0
 Allocations
+0 Allocations
9	3 (Master)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
1
 HP
+1 HP	• Good: Master Rank (+2B, +2 Steps, Floor 7) (Immune DC 7)<br>• Okay: 3dX+1 Step (Floor 5)<br>• Bad: 3dX (Floor 3)	• Good: Master Defense Boon (+2B -> 4dX) (Floor 5/7)<br>• Bad: Base paired pool	• Good: 5th-Lvl Vancian Slots 
+
3
 Focus
+3 Focus<br>• Okay: 3rd-Lvl Hybrid Slots 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
0
 Allocations
+0 Allocations
10	3 (Master)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
0
 HP
+0 HP	All tiers maintain Lvl 9 pool volume & floor.	All tiers maintain Lvl 9 defense boons.	• Good: 
+
3
 Focus
+3 Focus<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
1
 Allocation
+1 Allocation
11	3 (Master)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
1
 HP
+1 HP	All tiers maintain Lvl 9 pool volume & floor.	All tiers maintain Lvl 9 defense boons.	• Good: 6th-Lvl Vancian Slots 
+
3
 Focus
+3 Focus<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
0
 Allocations
+0 Allocations<br>• Bad: 
+
0
 Allocations
+0 Allocations
12	3 (Master)	• Good: 
+
2
 HP
+2 HP (+Attr step)<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
0
 HP
+0 HP	• Good: 5d Max Pool (+2 Steps, Floor 7)<br>• Okay/Bad: Maintain Lvl 9 pool.	• Good: +2B (+Attr step)<br>• Bad: Base paired pool	• Good: 
+
3
 Focus
+3 Focus (+Attr step)<br>• Okay: 4th-Lvl Hybrid Slots 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
0
 Allocations
+0 Allocations
13	4 (Hero)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
1
 HP
+1 HP	All tiers maintain Lvl 12 pool volume & floor.	All tiers maintain Lvl 9 defense boons.	• Good: 7th-Lvl Vancian Slots 
+
3
 Focus
+3 Focus<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
1
 Allocation
+1 Allocation
14	4 (Hero)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
0
 HP
+0 HP	All tiers maintain Lvl 12 pool volume & floor.	All tiers maintain Lvl 9 defense boons.	• Good: 
+
3
 Focus
+3 Focus<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
0
 Allocations
+0 Allocations<br>• Bad: 
+
0
 Allocations
+0 Allocations
15	4 (Hero)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
1
 HP
+1 HP	• Good: Legendary Rank (+3B, +3 Steps, Floor 9) (Immune DC 9)<br>• Okay: Master Rank (+2B, +2 Steps, Floor 7)<br>• Bad: 3dX+1 Step (Floor 5)	All tiers maintain Lvl 9 defense boons across Hero tier exit.	• Good: 8th-Lvl Vancian Slots 
+
3
 Focus
+3 Focus<br>• Okay: 5th-Lvl Hybrid Slots 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
0
 Allocations
+0 Allocations
16	4 (Hero)	• Good: 
+
2
 HP
+2 HP (+Attr step)<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
0
 HP
+0 HP	All tiers maintain Lvl 15 pool volume & floor.	• Good: +2B (+Attr step)<br>• Bad: Base paired pool	• Good: 
+
3
 Focus
+3 Focus (+Attr step)<br>• Okay: 
+
2
 Focus
+2 Focus<br>• Bad: 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
1
 Allocation
+1 Allocation
17	5 (Legend)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
1
 HP
+1 HP	All tiers maintain Lvl 15 pool volume & floor.	All tiers maintain Lvl 9 defense boons across Legend entry.	• Good: 9th-Lvl Vancian Slots $+3\text{ Focus**<br>• Okay:$+2\text{ Focus}$<br>•Bad:` 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
0
 Allocations
+0 Allocations
18	5 (Legend)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
0
 HP
+0 HP	All tiers maintain Lvl 15 pool volume & floor.	All tiers maintain defense boons.	• Good: $+3\text{ Focus**<br>• Okay:**6th-Lvl Hybrid Slots** $+2\text{ Focus}$<br>•Bad:` 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
0
 Allocations
+0 Allocations<br>• Bad: 
+
0
 Allocations
+0 Allocations
19	5 (Legend)	• Good: 
+
2
 HP
+2 HP<br>• Okay: 
+
1
 HP
+1 HP<br>• Bad: 
+
1
 HP
+1 HP	All tiers maintain Lvl 15 pool volume & floor.	All tiers maintain defense boons.	• Good: $+3\text{ Focus**<br>• Okay:$+2\text{ Focus}$<br>•Bad:` 
+
1
 Focus
+1 Focus	• Good: 
+
1
 Allocation
+1 Allocation<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
1
 Allocation
+1 Allocation
20	5 (Legend Apex)	• Good: 
+
4
 HP
+4 HP<br>• Okay: 
+
2
 HP
+2 HP<br>• Bad: 
+
2
 HP
+2 HP	• Good: Apex Legend Pool (5d12+2 over-cap, Floor 9)<br>• Okay: Legendary Rank (Floor 9)<br>• Bad: Master Rank (Floor 7)	• Good: Apex Defense (+3B)<br>• Bad: +1B Apex paired pool	• Good: Apex Arcane Mastery (Double 9th-Lvl Slots) 
+
6
 Focus
+6 Focus<br>• Okay: 
+
4
 Focus
+4 Focus<br>• Bad: 
+
2
 Focus
+2 Focus	• Good: 
+
2
 Allocations
+2 Allocations<br>• Okay: 
+
1
 Allocation
+1 Allocation<br>• Bad: 
+
1
 Allocation
+1 Allocation
3. Side-by-Side Class Application (Fighter vs. Rogue vs. Wizard)

Let's see how our three classic archetypes map directly to the 5 tracks across the 20-level matrix above:

Class Archetype	Track 1: Vitality (HP)	Track 2: Combat Pool (BAB)	Track 3: Paired Defenses (Saves)	Track 4: Vancian & Focus (CL)	Track 5: Skill Allocations (Domains)	Tactical & Simulationist Identity
Fighter (Martial Anchor)	Good (+2 HP/lvl)	Good (Expert Lvl 5, Master Lvl 9, Legend Lvl 15)	Good Fortitude (STR+CON)<br>Bad Reflex (DEX+INT), Bad Will (WIS+CHA)	Bad (0 Vancian Slots, +1 Focus/lvl)	Bad (2 allocations at Lvl 1, +1 at evens)	The ultimate kinetic tank and weapon master (Floor 7 at Lvl 9).
Rogue (Skill & Finesse Anchor)	Okay (+1 HP/lvl)	Okay (3dX Lvl 1, Expert Lvl 7, Master Lvl 15)	Good Reflexes (DEX+INT)<br>Bad Fortitude, Bad Will	Bad (0 Vancian Slots, +1 Focus/lvl)	Good (4 allocations at Lvl 1, +1 every level)	The ultimate skill specialist across Subterfuge, Social, and Finesse Combat.
Wizard (Arcane Caster Anchor)	Bad (+1 HP at odds)	Bad (Base 2dX, Floor 3 cap on physical)	Good Willpower (WIS+CHA)<br>Bad Fortitude, Bad Reflex	Good (Full 1st-9th Vancian Slots, +3 Focus/lvl)	Okay (3 allocations at Lvl 1, +1 at odds)	The ultimate master of Lore & Arcana (5d12 pool on spells, Floor 9 at Lvl 15).
Open
01_defenses_and_damage_modeling.md
MD
01_resolution_engine.md
MD
02_character_schema_and_stats.md
MD
04_spatial_and_distance_engine.md
MD
used
Bash
97ms

We have integrated and verified all seven of your structural calibrations across our core rules, spatial engine, and character schema (DEC-030 through DEC-035).

Furthermore, I have created our definitive 20-Level Good / Okay (Medium) / Bad (Poor) Class Advancement Matrix in 03_core_baseline_system/09_dnd_3_5e_class_advancement_tracks_mapping.md (presented above).

🏛️ Summary of What We Updated & Calibrated
1. Specific Skills Under 5 Domain Umbrellas (DEC-030)
Competency Ranks (Untrained 0 -> Trained 3 -> Expert 5 -> Master 7 -> Legend 9) apply directly to Specific Individual Skills (Stealth vs. Camouflage, Arcana vs. Nature, Diplomacy vs. Deception), rather than broad domain buckets!
Our 5 Action Mastery Domains (Combat, Survival, Subterfuge, Lore, Social) act cleanly as categorical Domain Umbrellas.
2. Exact Distance Tier Terminology (DEC-031)

We updated all spatial mechanics to your exact nomenclature:

Tier 0: Close (0-5 ft / Melee Reach)
Tier 1: Near (10-30 ft / 1 Zone / Standard Stride)
Tier 2: Medium (35-60 ft / 2 Zones)
Tier 3: Far (65-120 ft / 3 Zones)
Tier 4: Distant (125-300+ ft / Horizon / Artillery)
3. Vancian Spellcasting & Focus Division (DEC-032)
Vancian Daily Slots: Spellcasters prepare and cast spells using daily Vancian Spell Slots (1st to 9th level). Casting a standard prepared spell consumes the Vancian slot without costing Focus by default!
Focus Pool (WIS+INT): Reserved for short-rest arcane/divine exertions:
Sustaining spell concentration (1 Focus/round after taking damage).
On-demand Die Step-Ups (Up-Shifting d8 -> d10) on a spell check (1 Focus).
Channeling Metamagic Feats (Quicken, Empower, Silent Spell) without consuming higher-level Vancian slots (1 to 3 Focus).
4. Item Hardness Step Die & Durability (DEC-033)
An item's material sets its Hardness Step Die (d6 Wood, d8 Iron, d10 Steel, d12 Adamantine) and its Durability Slots (1 to 4).
Mathless Sunder & Item Sacrifice: Compare Attacker Damage Die Face vs Item Hardness Die Face. If Damage > Hardness, item loses 1 Durability Slot. If Critical Sunder (Max Face OR 2+ steps over Hardness), item shatters (loses 2 slots).
5. The 
𝑑
100
d100 Weapon Crit Profile Engine & Called Shots (DEC-034)
Crit Profile %: Every weapon has a Critical Threat Profile (Standard 10% [01-10 on d100], Keen/Finesse 15-20% [01-20 on d100], Heavy Pick 5% [01-05 on d100 / x3 multiplier]). When attacking, roll your step pool (3d10) and 1 percentile die (
𝑑
100
d100) simultaneously. If the check succeeds and 
𝑑
100
d100 falls within profile, it crits!
Wounds Happen ONLY on Crits (or Called Shots): Severe anatomical structural trauma (1d8 Location Matrix: severed tendon, broken rib) triggers ONLY when a Critical Hit connects (or via Called Shot maneuver)! Standard hits (Damage > Soak) deal normal Vitality loss and quick minor disruptions (Bleed, Off-balance, Shaken).
Called Shot Maneuver: A character can force an Anatomical Wound (and its local 1d8 impairment) on a standard hit without rolling a natural crit by declaring a Called Shot maneuver (spending [1A] + taking +1 Bane Die on attack, OR spending 2 [SET] tokens post-hit).
📊 The 20-Level Good / Okay / Bad Class Advancement Matrix (DEC-035)

In 03_core_baseline_system/09_dnd_3_5e_class_advancement_tracks_mapping.md (Section 2), we mapped how our 5 tracks scale every single level (Levels 1 through 20) across Good, Okay (Medium), and Bad (Poor) rates:

Class Track	Good Progression (High Cap / Fast)	Okay Progression (Medium / Balanced)	Bad Progression (Poor / Low Cap)
1. Vitality Increments (HP Growth)	Base (STR+CON) + 4 at Lvl 1.<br>Gains 
+
2
 HP every single level
+2 HP every single level (Level 2 through 20).	Base (STR+CON) + 2 at Lvl 1.<br>Gains 
+
1
 HP every single level
+1 HP every single level.	Base (STR+CON) at Lvl 1.<br>Gains 
+
1
 HP at odd levels only
+1 HP at odd levels only (Levels 3, 5, 7, 9...).
2. Check Pool & Floor (BAB Equivalent)	Base 3dX (Floor 3) at Lvl 1.<br>• Lvl 5: Expert (3dX+1 Step, Floor 5).<br>• Lvl 9: Master (4dX+2 Steps, Floor 7).<br>• Lvl 15: Legend (5dX+3 Steps, Floor 9).	Base 2dX (Floor 3) at Lvl 1.<br>• Lvl 7: Expert (Floor 5).<br>• Lvl 13: Master (Floor 7).<br>• Lvl 18: Legend (Floor 9).	Base 2dX (Floor 0) at Lvl 1.<br>• Lvl 4: +1B (3dX keep highest) on favored weapons.<br>• Lvl 9: Floor 3 (Trained cap).
3. Paired Defenses (Saving Throws)	Starts with +1B (3dX keep highest) paired pool at Lvl 1.<br>• Lvl 9: Elevates to +2B (4dX keep highest, Floor 5/7)!	Starts with Base 2dX paired pool.<br>• Lvl 7: Gains +1B (3dX keep highest, Floor 3).	Base 2dX paired pool across all levels (Floor 0/3).
4. Vancian & Focus (CL & Acuity)	• Vancian: Full 1st-to-9th level slots.<br>• Focus: 
+
3
 Focus every level
+3 Focus every level (+60 total at Lvl 20).<br>• Spell Power Pool: Reaches Floor 5 at Lvl 5, Floor 7 at Lvl 9, Floor 9 (5dX) at Lvl 15.	• Vancian: Hybrid 1st-to-6th level slots (Bard/Alchemist).<br>• Focus: 
+
2
 Focus every level
+2 Focus every level.<br>• Spell Power: Reaches Floor 5 at Lvl 7, Floor 7 at Lvl 13.	• Vancian: 
0
0 slots.<br>• Focus: 
+
1
 Focus every level
+1 Focus every level (for martial surges/reactions).
5. Domain Allocations (Specific Skills)	4 Allocations at Lvl 1, plus 
+
1
 Allocation every level
+1 Allocation every level (Level 2 through 20 — 23 total allocations to master 3-4 domains).	3 Allocations at Lvl 1, plus 
+
1
 Allocation across 13 levels
+1 Allocation across 13 levels (16 total allocations to master 2 domains).	2 Allocations at Lvl 1, plus 
+
1
 Allocation across 7 levels
+1 Allocation across 7 levels (9 total allocations — masters 1 domain).
🚀 Where Shall We Focus Our Energy Next?

Our core resolution engine, spatial terminology, 20-level class tracks, and simulationist combat matrix are fully established and verified. What specific expansion or compendium would you like to build next?

Design the Core Feat Compendium (General, Combat, and Racial Feats): Let's convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into clean 1-sentence mathless vector traits across our 6 tiers.
Flesh out the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Let's build out the specific skill proficiencies (Stealth, Lockpicking, Arcana, Diplomacy) and combat maneuvers (Shove, Trip, Grapple, Disarm, Feint) across all 5 competency ranks (Untrained to Legendary).
Build the Magic & Spellcasting Engine (Traditions & Vancian Grimoire): Let's define Vancian preparation across our 5 Traditions (Arcana, Divine, Primal, Shadow, Time), detail metamagic Focus costs, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Step-by-Step Character & Monster Walkthrough: Let's create a Tier 2 Veteran (Level 6) PC and a Tier 3 Master (Level 10) Boss monster from scratch to show the exact mathless formulas in action.

Which of these would you like to explore next?
