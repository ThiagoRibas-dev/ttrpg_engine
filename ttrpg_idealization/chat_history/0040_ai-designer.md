---
turn: 40
role: "AI-Designer"
source: chat_history.json
---

# Turn 40 — AI-Designer

used
Bash
81ms
Edited files
3
01_master_brainstorm_log.md
MD
Dungeons & Dragons 3.5e: Deep Comparative Analysis & Progression
MD
Dungeons & Dragons 3.5e: Deep Comparative Analysis & Progression

Dungeons & Dragons 3.5e is our primary option-density anchor. It remains beloved for its high-granularity character customization, prestige classes, modular feats, and rich monster ecologies. However, high-level 3.5e play frequently collapses under the weight of heavy linear arithmetic ($+BAB + Str + Magic + Feats + Buffs - Penalties$), arbitrary skill point bookkeeping (Cross-Class rules), and passive binary defenses (Armor Class).

This document compares our 8-Block Universal Mathless Check Pool Ecosystem directly against D&D 3.5e across six general mechanics, contrasts their 20-level progression tables, and provides a side-by-side Level 10 combat showdown.

1. General Mechanics Comparison Matrix (D&D 3.5e vs. Our Mathless System)
Architectural Dimension	Dungeons & Dragons 3.5e (The Option Anchor)	Our Idealized Mathless System (Evolution & Upgrade)	Why Our System Elevates Simulationism & Flow
1. Resolution Formula & Table Arithmetic	
1
𝑑
20
+
𝐵
𝐴
𝐵
+
Stat Mod
+
Feats
+
Buffs
−
Penalties
1d20+BAB+Stat Mod+Feats+Buffs−Penalties.<br>Requires stacking 4 to 8 linear modifiers on every check (e.g., d20 roll [13] + BAB [+10/+5] + Str [+5] + Weapon Focus [+1] + Haste [+1] - Power Attack [-4] = 26 vs AC 24).	NdX keep highest (Step Pools with Zero Math).<br>Attribute + Competency sets Die Size (X); Class + Boons sets Pool Volume (N). You roll the pool and compare highest face directly against Target DC or opposed die (max vs max).	Zero Arithmetic Latency. Eliminates high-level modifier math ($26 \text{ vs } 24$) while maintaining exact physical distinctions between peak ceilings (d12) and tactical consistency (4 dice).
2. Core Attributes & Derived Stats	6 Ability Scores (STR, DEX, CON, INT, WIS, CHA).<br>Numeric scores (3 to 36+) generate 
+
𝑋
/
−
𝑋
+X/−X modifiers (mod = floor((score-10)/2)). Derived saving throws (Fort, Ref, Will) are isolated (Reflex = Dex only; Will = Wis only).	Same Classic 6 Ability Scores (STR, DEX, CON, INT, WIS, CHA) as Step Dice (d4 
→
→ d12+).<br>Zero modifier calculation! Paired attributes directly form check pools for our three defenses: Fortitude (STR+CON), Reflexes (DEX+INT), and Willpower (WIS+CHA) (DEC-022).	Preserves 100% 3.5e compatibility (STR d8+ = STR 15+), while solving the "Dexterity God-Stat" flaw by linking spatial logic (INT) into dodging and self-identity (CHA) into mental resolve!
3. Skill System & Competency Granularity	Skill Points & Cross-Class Penalities. Characters gain skill points per level (say, 4+Int). Class skills cost 1 point per rank (up to Level+3); Cross-Class skills cost 2 points per rank (capped at half). Creates heavy bookkeeping and dead skill sinks.	5 Action Mastery Domains (Combat, Survival, Subterfuge, Lore, Social) & 5 Competency Ranks (Untrained 0 to Legendary 9).<br>No cross-class math! Investing in a domain steps up Die Size (X+1 to X+3), increases Pool Volume (+1B to +3B), and sets Competency Floors (Fixed Die Minimums).	Eliminates point counting. Our Competency Ranks (DEC-020) give explicit, investment-driven growth where experts (Floor 5) and masters (Floor 7) literally cannot whiff on routine checks!
4. Combat Defenses & Armor Mitigation	Armor Class (AC = 10 + Armor + Shield + Dex + Deflection + Natural). Also Touch AC (no armor) and Flat-Footed AC (no Dex). Armor strictly increases target number (hit/miss binary). Only rare Damage Reduction (DR 5/magic) reduces damage post-hit.	4 Paired Defensive Layers (Reflexes DEX+INT, Parry Combat Pool, Resilience Fort/Will, and Soak Rank Armor Die).<br>We adapt Touch/Flat-Footed naturally: Touch attacks bypass Parry/Soak to check Evasion (Reflexes); Surprise attacks catch defenders before they can declare active Parry! Soak (d4 Cloth to d12 Plate) is checked post-hit (Damage vs Soak).	Solves 3.5e’s binary AC problem (where full plate just makes you harder to hit). In our system, Plate armor (Soak d12) cleanly absorbs kinetic weapon hits post-hit, forcing attackers to use [SET] tokens to Bypass Soak!
5. Action Economy & Multi-Attacks	Iterative Attacks (Base Attack Bonus +6/+1, +11/+6/+1). Full Attack action requires standing still (cannot move more than 5 ft). Making a second/third attack requires subtracting 
−
5
 and 
−
10
−5 and −10 from your attack roll total.	3-Action Economy ([A][A][A] + [1R] Free Guard).<br>Inspired by PF2e and Mythras, characters spend 3 actions flexibly (Move, Strike, Cast, Maneuver). Multi-attacks impose Stamina/Pool Fatigue (+1 Bane Die on 2nd attack, +2 Banes on 3rd) (DEC-008).	Eliminates stationary full-attack paralysis and 
−
5
/
−
10
−5/−10 subtraction. Characters move dynamically across zones and make multi-strikes using fast pool adjustments (3d10 -> 2d10 -> 2d10 low).
6. Criticals & Maneuver Execution (Feat Taxes)	Feat Chains & Attacks of Opportunity (AoO). To perform a Disarm, Trip, or Grapple without taking a free enemy counter-attack (AoO) and a 
−
4
−4 check penalty, you MUST buy 2-3 prerequisite feats (Combat Expertise -> Improved Disarm).	Differential Special Effect Tokens ([SET] Engine).<br>Universal access (DEC-007)! You roll your check pool against enemy Parry/Reflexes. If you win, extra beating dice (Multi-Beat Count) and Max Face rolls award [SET] tokens spent immediately on Impale, Bleed, Disarm, Trip, Riposte!	Eliminates 3.5e’s "feat tax" where warriors never attempt maneuvers because they lack prerequisite chains. Feats in our system give advanced action options ([1A] Power Strike), while standard maneuvers belong to everyone via [SET]!
2. Side-by-Side 20-Level Progression (Human Fighter Lvl 1 to 20)

Let's compare what a dedicated martial Fighter gains across all 20 levels in D&D 3.5e versus what our Fighter gains across our 6 High Fantasy Tiers (Trained -> Veteran -> Master -> Hero -> Legend -> Mythic):

Level & Scope	D&D 3.5e Fighter Progression (Numerical Modifiers & Iterative Attacks)	Our Mathless High Fantasy System (Tri-Vector Step Pools & Feats)	Architectural & Simulationist Comparison
1<br>(Trained)	• Base Attack Bonus: 
+
1
+1<br>• Saves: Fort +2, Ref +0, Will +0<br>• Feats: 1 Fighter Bonus Feat + 1 Human Feat + 1 General Feat (e.g., Power Attack, Cleave, Weapon Focus [+1 attack]).<br>• Skills: 2 + Int mod points (Climb +4, Jump +4).	• Die Size (X): STR d8, CON d8, AGI d6, INT d6, WIS d6, CHA d6.<br>• Check Pool: Base 2d + Martial Class (+1B) 
→
→ 3d8 keep highest (Floor 3) in Combat Mastery.<br>• Defenses: Fortitude (STR+CON 2d8), Reflexes (DEX+INT 2d6), Parry (3d8), Soak (Scale Mail d8).<br>• Feats: Power Strike [1A], Cleaving Momentum [0A], Weapon Master (Swords - Up-Shift d8->d10).	In 3.5e, Weapon Focus adds 
+
1
+1 and Power Attack forces 
−
1
 to 
+
1
−1 to +1 math. In our system, Weapon Master steps up your sword die size (d8 -> d10), and Power Strike trades 
−
1
 die volume (‘2d10‘)
−1 die volume (‘2d10‘) to step up your Damage Die (d8 -> d10 vs Soak)!
2<br>(Trained)	• BAB: 
+
2
+2<br>• Fort +3, Ref +0, Will +0<br>• Fighter Bonus Feat (e.g., Combat Reflexes).	• +2 Stamina OR +2 Focus.<br>• Gain 1 Skill Proficiency in a Trained domain (+1B).<br>• Class Feat (Lvl 2): Active Guard / Shield Intercept [1R].	3.5e gives a flat 
+
1
+1 to BAB and Fortitude. Our system expands your Stamina pool (allowing more Die Step-Ups) and unlocks reactive shield interception without numbers.
3<br>(Trained)	• BAB: 
+
3
+3<br>• Fort +3, Ref +1, Will +1<br>• General Feat (e.g., Iron Will [+2 Will]).	• +2 Vitality (HP).<br>• Unlock Domain Maneuver Level 1 (Shove, Trip, Feint).<br>• General Feat (Lvl 3): Iron Will (+1B on WIS+CHA Willpower checks).	Notice how Iron Will transforms from a linear 
+
2
+2 modifier into a clean Pool Volume Boon (+1B -> 3 dice) on your WIS+CHA Willpower checks (DEC-022)!
4<br>(Trained Capstone)	• BAB: 
+
4
+4<br>• Fort +4, Ref +1, Will +1<br>• Attribute Increase: 
+
1
 Str (‘Str 16 -> +3 mod‘)
+1 Str (‘Str 16 -> +3 mod‘)<br>• Fighter Bonus Feat (e.g., Weapon Specialization [+2 damage]).	• Attribute Step Upgrade #1 (STR d8 -> d10) 
→
→ Combat Die Size becomes d12 (Floor 3).<br>• Choose 1 additional domain at Trained Rank (+1B, Floor 3).<br>• Class Feat (Lvl 4): Weapon Specialization (Damage Die stepped up d10 -> d12 vs Soak).	At Level 4 (Tier 1 Capstone), 3.5e adds 
+
1
+1 to Str and 
+
2
+2 to damage. Our system performs an Attribute Die Step-Up (d8 -> d10), pushing the Fighter's sword check pool to 3d12 keep highest, while Weapon Specialization steps up the physical Damage Die (d10 -> d12 vs Soak)!
5<br>(Veteran)	• BAB: 
+
5
+5<br>• Fort +4, Ref +1, Will +1	• Veteran Tier Awakening: Elevate Combat Mastery to Expert Rank (+1B, +1 Step, Floor 5) 
→
→ Pool becomes 4d12 keep highest (Floor 5).<br>• +2\text{ Stamina & Focus}.<br>• Level 5 Milestone Feature (Regional Champion Status Unlocked).	Look at our Level 5 Veteran Tier Entry: The Fighter reaches Expert Rank (Floor 5), mathematically immune to failing standard DC 5 checks (DEC-019). In 3.5e, Level 5 is a "dead level" (only +1 BAB).
6<br>(Veteran)	• BAB: 
+
6
/
+
1
+6/+1 (Unlocks 2nd iterative attack with -5 penalty).<br>• Fort +5, Ref +2, Will +2<br>• Fighter Bonus Feat (e.g., Improved Disarm). + General Feat.	• 
+
2
 Vitality (‘HP‘)
+2 Vitality (‘HP‘).<br>• Gain 1 Skill Proficiency across any domain (+1B).<br>• Class Feat (Lvl 6): Sudden Charge [2A] (Double Stride + Strike with +1B).<br>• General Feat (Lvl 6).	In 3.5e, Level 6 unlocks 
+
6
/
+
1
+6/+1 iterative attacks that require standing still to use. In our system, Sudden Charge [2A] lets the Fighter charge across 2 zones (60 ft) and deliver a massive momentum strike (4d12 + 1B = 5d12 keep highest)!
8<br>(Veteran Capstone)	• BAB: 
+
8
/
+
3
+8/+3<br>• Fort +6, Ref +2, Will +2<br>• Attribute Increase: 
+
1
 Str (‘Str 17 -> +3 mod‘)
+1 Str (‘Str 17 -> +3 mod‘)<br>• Fighter Bonus Feat (e.g., Greater Weapon Focus [+1 attack]).	• Attribute Step Upgrade #2 (CON d8 -> d10) 
→
→ Fortitude Pool becomes 1d10 STR + 1d10 CON keep highest.<br>• Elevate a 2nd domain (Athletics) to Expert Rank (Floor 5).<br>• Class Feat (Lvl 8): Greater Weapon Mastery (Attacks ignore 1st enemy Parry Boon).	At Level 8, 3.5e gives 
+
1
+1 attack (Greater Weapon Focus). Our system steps up Constitution (d8 -> d10), instantly expanding Fortitude resilience and Stamina reserves (DEC-021) while giving tactical bypass against enemy parry pools!
9<br>(Master)	• BAB: 
+
9
/
+
4
+9/+4<br>• Fort +6, Ref +3, Will +3<br>• General Feat (e.g., Improved Critical).	• Master Tier Awakening: Once per combat, your check pool automatically performs a Die Step-Up (Hyper-Shift) for free without spending Stamina.<br>• Elevate Combat Mastery to Master Rank (+2B, +2 Steps, Floor 7) 
→
→ 4d12 keep highest (Floor 7).<br>• General Feat (Lvl 9): Lethal Severance (Crits inflict 2 Wound Conditions).	At Level 9 (Master Tier Entry), our Fighter reaches Master Rank (Floor 7), guaranteeing 100% immunity to failing Formidable DC 7 challenges. In 3.5e, Level 9 gives 
+
1
+1 BAB and a feat.
11<br>(Master)	• BAB: 
+
11
/
+
6
/
+
1
+11/+6/+1 (Unlocks 3rd iterative attack with -10 penalty).<br>• Fort +7, Ref +3, Will +3<br>• Strike requires standing still for full round.	• 
+
2
 Vitality (‘HP‘)
+2 Vitality (‘HP‘).<br>• Unlock Domain Maneuver Level 3 (Whirlwind Strike [3A], Spell Penetration).<br>• General Feat (Lvl 11): Shatter Armor [SET] (Spend 1 token to destroy enemy Durability Slot).	Look at the difference at Level 11: 3.5e gives a 3rd stationary attack (at -10 penalty). Our system gives Whirlwind Strike ([3A] AoE check vs all adjacent Evasion pools without penalty) and Shatter Armor [SET] tokens!
12<br>(Master Capstone)	• BAB: 
+
12
/
+
7
/
+
2
+12/+7/+2<br>• Attribute Increase: 
+
1
 Str (‘Str 18 -> +4 mod‘)
+1 Str (‘Str 18 -> +4 mod‘)<br>• Fighter Bonus Feat (e.g., Greater Weapon Specialization [+2 damage]). + General Feat.	• Attribute Step Upgrade #3 (STR d10 -> d12) 
→
→ Combat Die Size reaches over-cap d12+1 pool.<br>• Elevate a 2nd domain to Master Rank (Floor 7).<br>• Class Feat (Lvl 12): Devastating Impact (Damage Die d12 automatically bypasses 1st Soak step).	At Level 12, the Fighter steps Strength to d12, turning his check pool into an over-cap master pool (Floor 7), where standard hits easily overcome heavy monster Soak ranks.
16<br>(Hero Capstone)	• BAB: 
+
16
/
+
11
/
+
6
/
+
1
+16/+11/+6/+1 (4th iterative attack with -15 penalty).<br>• Fort +10, Ref +5, Will +5<br>• Attribute Increase: 
+
1
 Str (‘Str 19 -> +4 mod‘)
+1 Str (‘Str 19 -> +4 mod‘)<br>• Fighter Bonus Feat.	• Attribute Step Upgrade #4 (STR d12 -> d12+2 over-cap pool).<br>• Unlock Mythic Maneuver Level 4 (Instant Severance).<br>• Class Feat (Lvl 16): Unstoppable Juggernaut (Immune to Prone, Shaken, and Bleed conditions).	By Level 16 (Hero Tier Capstone), 3.5e gives a 4th attack (at -15 penalty that almost never hits). Our system makes the Fighter a physical Juggernaut immune to common crowd control, rolling massive 5d12 check pools (Floor 7)!
20<br>(Legend Apex)	• BAB: 
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
+20/+15/+10/+5<br>• Fort +12, Ref +6, Will +6<br>• Attribute Increase: 
+
1
 Str (‘Str 20 -> +5 mod‘)
+1 Str (‘Str 20 -> +5 mod‘)<br>• Fighter Bonus Feat.	• Apex Legend Capstone: Once per combat, automatically convert any check into a Critical Success (Rolled Max Face + 2 [SET]).<br>• 
+
4
 Vitality, Stamina, and Focus
+4 Vitality, Stamina, and Focus.<br>• Level 20 Apex Feat (Absolute Martial Supremacy).	At Level 20, the 3.5e Fighter gets 
+
1
+1 BAB and a feat. Our Level 20 Legend Fighter (Tier 5 Apex) commands Absolute Martial Supremacy, guaranteed Floor 9 (never rolling below 9), before ascending to Level 21+ Mythic Demigod Status (Tier 6)!
3. Side-by-Side Level 10 Combat Showdown (Fighter vs. Ogre Mage)

To see exactly how our mathless mechanics eliminate arithmetic while delivering superior tactical action, let's trace a Level 10 Human Fighter attacking an Ogre Mage (Large Giant Caster) side-by-side:

Scenario Setup
The Player Character: Level 10 Human Greatsword Fighter (Master in Swords, high Strength).
The Target: Ogre Mage (Large size, AC 21 in 3.5e / Soak d10 + Evasion d8 in our system, 50 HP).
Tactical Context: The Fighter is standing 15 feet away (Tier 1 Near zone) and wants to close the distance and deliver a massive, armor-shattering strike.
Phase 1: D&D 3.5e Resolution (The Arithmetic & Stationary Full-Attack Dilemma)
The Problem of Movement: In 3.5e, the Fighter has BAB +10/+5. But because the Ogre Mage is 15 feet away, the Fighter cannot take a Full Attack action! He can only move 15 feet (Move Action) and make one single attack at 
+
10
+10 (Standard Action), completely wasting his 
+
5
+5 iterative attack!
Applying Modifiers: The player declares Power Attack (taking -3 on attack to add +6 damage).
Attack Calculation: 
𝑑
20
 roll (13)
+
𝐵
𝐴
𝐵
(
+
10
)
+
Str Mod (+4)
+
Weapon Focus (+1)
+
Magic (+1)
−
Power Attack (-3)
=
26
 total
d20 roll (13)+BAB(+10)+Str Mod (+4)+Weapon Focus (+1)+Magic (+1)−Power Attack (-3)=26 total.
Evaluating Outcome: Total 26 beats Armor Class 21 (Hit!). Not a natural 19-20, so no crit.
Damage Math: Player rolls 2d6 (Greatsword) + Str x 1.5 (+6) + Weapon Spec (+2) + Magic (+1) + Power Attack (+6).
Rolled: 
𝑑
6
(
4
)
+
𝑑
6
(
5
)
=
9
d6(4)+d6(5)=9.
Table Arithmetic: 9 + 6 + 2 + 1 + 6 = 24 damage.
Ogre Mage subtracts 24 from HP (50 - 24 = 26 HP remaining). The Ogre stands still and casts Cone of Cold on its next turn.
Phase 2: Our Mathless Resolution (The 3-Action & [SET] Engine)
Our Converted Fighter Stats (Level 10 Master Tier):
Check Pool (X & N): Base STR d10 + Master in Combat (+2 Steps) 
→
→ d12 (Floor 7). Volume = Base 2d + Martial Class (+1B) + Master Rank (+2B) 
→
→ 5d12 keep highest (Floor 7).
Greatsword: Damage Die d12 vs Soak, 3 Durability Slots.
Ogre Mage Profile: Parry Pool 3d10, Soak Rank d10 (Chain & Hide), Evasion Pool 2d8, Vitality 36.
Declaring the 3-Action Budget ([A][A][A]):
Action 1 ([1A] Stride): The Fighter effortlessly Strides 15 feet into Tier 0 (Melee reach).
Action 2 ([1A] Power Strike): The Fighter declares Power Strike, trading 
−
1
 die volume (‘4d12‘)
−1 die volume (‘4d12‘) to step up his physical Greatsword Damage Die (d12 
→
→ over-cap d12+1 vs Soak).
Action 3 ([1A] Secondary Strike): The Fighter reserves his 3rd action to follow up immediately if needed (taking +1 Bane due to multi-attack -> 3d12).
Rolling the First Opposed Check (Zero Math):
Fighter Rolls (4d12): 5, 8, 10, 12. Highest Face = 12 (Floor 7 guaranteed).
Ogre Mage Parry (3d10): 4, 6, 9. Highest Face = 9.
Evaluating Outcome (Max vs Max & [SET] Generation):
Winner Check: Fighter Highest (12) > Ogre Highest (9) 
→
→ Hit!
Token Generation (Multi-Beat Differential): Look at the Fighter's remaining dice (5, 8, 10). Die 10 beats the Ogre's 9 (+1 [SET]). Furthermore, the Fighter rolled his Maximum Face Value (12 on d12) (+1 [SET]).
Total Earned: Standard Hit + 2 Special Effect Tokens ([SET]) spent instantly!
Damage vs Soak & Anatomical Severance (Zero Math):
Soak Check: Because the Fighter rolled Max Face (12), the hit is automatically a Critical Damage Hit against the Ogre's Soak d10.
Vitality Loss: Ogre takes Double Vitality loss (Max Face 12 x 2 = 24 Vitality lost -> 12 Vitality left).
Anatomical 1d8 Location Roll: Player rolls 1d8 Anatomical Matrix and gets 1 (Head / Skull Hit). The Ogre Mage suffers a Concussion (dazed condition), dropping its mental INT d10 step die to d8 and destroying all ability to cast concentration spells on its next turn (0 Focus actions allowed)!
Spending [SET] Tokens: The Fighter spends his 2 [SET] tokens on Trip (1 [SET]) (knocking the dazed Ogre Prone into the dirt) and Bypass Soak (1 [SET]) (stepping down the Ogre's armor Soak to d6 for his 3rd action secondary strike)!
4. Summary of Simulationist & Tactical Superiority

Look at the profound contrast between the two systems at Level 10:

In 3.5e, the Fighter was crippled by stationary full-attack rules (wasting half his attacks just to walk 15 feet), did two linear math equations (13+10+4+1+1-3=26 and 9+6+2+1+6=24), and left the Ogre completely unimpaired to cast a deadly spell on its turn.
In Our Mathless System, the Fighter used his 3-action budget to close the distance ([1A]), landed a crushing Power Strike ([1A]) with zero arithmetic (comparing faces 12 vs 9), generated 2 tactical maneuver tokens ([SET]), cracked the Ogre Mage's skull via our 1d8 matrix (preventing it from casting spells!), and swept the monster Prone into the dirt!
Open

We have completed a side-by-side, 6-dimension comparative analysis and 20-level progression walkthrough against our primary option-density anchor: Dungeons & Dragons 3.5e, now archived in 02_comparative_system_analysis/07_dnd_3_5e_comparative_analysis_and_progression.md (presented above) and recorded under decision DEC-028.

While 3.5e remains our gold standard for build customization (feats, prestige classes, bestiaries), our system inherits its option wealth while solving its stationary full-attack paralysis, cross-class skill bookkeeping, and 
+
26
 vs 
24
+26 vs 24 modifier arithmetic:

🏛️ 6-Dimension General Mechanics Matrix (D&D 3.5e vs. Our Mathless System)
Architectural Dimension	Dungeons & Dragons 3.5e (The Option Anchor)	Our Idealized Mathless System (Evolution & Upgrade)	Why Our System Elevates Simulationism & Flow
1. Resolution Formula & Table Arithmetic	
1
𝑑
20
+
𝐵
𝐴
𝐵
+
Stat Mod
+
Feats
+
Buffs
−
Penalties
1d20+BAB+Stat Mod+Feats+Buffs−Penalties.<br>Requires stacking 4 to 8 linear modifiers (e.g., d20 [13] + BAB [+10/+5] + Str [+5] + Weapon Focus [+1] + Haste [+1] - Power Attack [-4] = 26 vs AC 24).	NdX keep highest (Step Pools with Zero Math).<br>Attribute + Competency sets Die Size (X); Class + Boons sets Pool Volume (N). You roll the pool and compare highest face directly (max vs max).	Zero Arithmetic Latency. Eliminates high-level modifier math ($26 \text{ vs } 24$) while maintaining exact physical distinctions between peak ceilings (d12) and tactical consistency (4 dice).
2. Core Attributes & Derived Stats	6 Ability Scores (STR, DEX, CON, INT, WIS, CHA).<br>Numeric scores generate 
+
𝑋
/
−
𝑋
+X/−X modifiers. Derived saving throws (Fort, Ref, Will) are isolated (Reflex = Dex only; Will = Wis only).	Same Classic 6 Ability Scores (STR, DEX, CON, INT, WIS, CHA) as Step Dice (d4 
→
→ d12+).<br>Zero modifier calculation! Paired attributes directly form check pools for our three defenses: Fortitude (STR+CON), Reflexes (DEX+INT), and Willpower (WIS+CHA) (DEC-022).	Preserves 100% 3.5e compatibility (STR d8+ = STR 15+), while solving the "Dexterity God-Stat" flaw by linking spatial logic (INT) into dodging and self-identity (CHA) into mental resolve!
3. Skill System & Competency Granularity	Skill Points & Cross-Class Penalities. Class skills cost 1 point (up to Level+3); Cross-Class skills cost 2 points per rank (capped at half). Creates heavy bookkeeping and dead skill sinks.	5 Action Mastery Domains (Combat, Survival, Subterfuge, Lore, Social) & 5 Competency Ranks (Untrained 0 to Legendary 9).<br>No cross-class math! Investing in a domain steps up Die Size (X+1 to X+3), increases Pool Volume (+1B to +3B), and sets Competency Floors (Fixed Die Minimums).	Eliminates point counting. Our Competency Ranks (DEC-020) give explicit, investment-driven growth where experts (Floor 5) and masters (Floor 7) literally cannot whiff on routine checks!
4. Combat Defenses & Armor Mitigation	Armor Class (AC = 10 + Armor + Shield + Dex + Deflection + Natural). Also Touch AC (no armor) and Flat-Footed AC (no Dex). Armor strictly increases target number (hit/miss binary). Only rare DR (DR 5/magic) reduces damage post-hit.	4 Paired Defensive Layers (Reflexes DEX+INT, Parry Combat Pool, Resilience Fort/Will, and Soak Rank Armor Die).<br>Touch/Flat-Footed adapt naturally: Touch attacks bypass Parry/Soak to check Evasion (Reflexes); Surprise attacks catch defenders before active Parry! Soak (d4 Cloth to d12 Plate) is checked post-hit (Damage vs Soak).	Solves 3.5e’s binary AC problem (where full plate just makes you harder to hit). In our system, Plate armor (Soak d12) cleanly absorbs kinetic weapon hits post-hit, forcing attackers to use [SET] tokens to Bypass Soak!
5. Action Economy & Multi-Attacks	Iterative Attacks (Base Attack Bonus +6/+1, +11/+6/+1). Full Attack action requires standing still (cannot move more than 5 ft). Making a second/third attack requires subtracting 
−
5
 and 
−
10
−5 and −10 from your attack roll total.	3-Action Economy ([A][A][A] + [1R] Free Guard).<br>Inspired by PF2e and Mythras, characters spend 3 actions flexibly (Move, Strike, Cast, Maneuver). Multi-attacks impose Stamina/Pool Fatigue (+1 Bane Die on 2nd attack, +2 Banes on 3rd) (DEC-008).	Eliminates stationary full-attack paralysis and 
−
5
/
−
10
−5/−10 subtraction. Characters move dynamically across zones and make multi-strikes using fast pool adjustments (3d10 -> 2d10 -> 2d10 low).
6. Criticals & Maneuver Execution (Feat Taxes)	Feat Chains & Attacks of Opportunity (AoO). To perform a Disarm, Trip, or Grapple without taking a free enemy counter-attack (AoO) and a 
−
4
−4 check penalty, you MUST buy 2-3 prerequisite feats (Combat Expertise -> Improved Disarm).	Differential Special Effect Tokens ([SET] Engine).<br>Universal access (DEC-007)! You roll your check pool against enemy Parry/Reflexes. If you win, extra beating dice (Multi-Beat Count) and Max Face rolls award [SET] tokens spent immediately on Impale, Bleed, Disarm, Trip, Riposte!	Eliminates 3.5e’s "feat tax" where warriors never attempt maneuvers because they lack prerequisite chains. Feats in our system give advanced action options ([1A] Power Strike), while standard maneuvers belong to everyone via [SET]!
⚔️ Side-by-Side Combat Showdown (Level 10 Fighter vs. Ogre Mage)

Look at what happens during a real combat turn when a Level 10 Greatsword Fighter attacks an Ogre Mage standing 15 feet away (Tier 1 Near zone):

In D&D 3.5e (Stationary Full-Attack Paralysis):
The Problem of Movement: Because the Ogre Mage is 15 feet away, the Fighter cannot take a Full Attack action! He can only move 15 feet (Move Action) and make one single attack at 
+
10
+10 (Standard Action), completely wasting his 
+
5
+5 iterative attack!
Player Math: Declares Power Attack (-3 attack, +6 damage). Rolls 
𝑑
20
 (13)
+
10
+
4
+
1
+
1
−
3
=
26
 vs AC 21
d20 (13)+10+4+1+1−3=26 vs AC 21 (Hit!).
Damage Math: Rolls 2d6 (Greatsword) + 6 + 2 + 1 + 6 
→
→ 9 + 15 = 24 damage. Ogre Mage subtracts 24 from HP (50 - 24 = 26 HP left).
The Experience: The Fighter was paralyzed by stationary full-attack rules, did two linear math equations (13+10+4+1+1-3=26 and 9+6+2+1+6=24), and left the Ogre completely unimpaired to cast Cone of Cold on its turn.
In Our Mathless System (3-Action Dynamic Flow):
Action 1 ([1A] Stride): The Fighter effortlessly Strides 15 feet into Tier 0 (Melee reach).
Action 2 ([1A] Power Strike): Declares Power Strike, trading 
−
1
 die volume (‘4d12‘ -> ‘3d12‘)
−1 die volume (‘4d12‘ -> ‘3d12‘) to step up his Greatsword Damage Die (d12 
→
→ over-cap d12+1 vs Soak).
Action 3 ([1A] Secondary Strike): Reserves his 3rd action to follow up immediately if needed.
Rolling the Check (Zero Math): Rolls 4d12 keep highest directly vs Ogre Parry 3d10. Fighter rolls 5, 8, 10, 12 (Highest = 12, Floor 7 guaranteed). Ogre rolls 4, 6, 9 (Highest = 9).
Evaluating Outcome (Max vs Max): 12 > 9 
→
→ Hit! Because 10 also beats 9 (Multi-beat), and 12 is Max Face, the Fighter earns 2 Special Effect Tokens ([SET])!
Damage vs Soak (Zero Math): Max Face (12) automatically triggers a Critical Damage Hit against Ogre Soak d10. Ogre takes double Vitality loss (12 x 2 = 24 Vitality lost -> 12 left).
Anatomical Severance (1d8 Location): Rolls 1 (Head / Skull Hit). The Ogre Mage suffers a Concussion (dazed condition), dropping INT d10 to d8 and destroying all ability to cast concentration spells on its next turn (0 Focus actions allowed)!
Spending [SET] Tokens: Spends his 2 [SET] tokens on Trip (1 [SET]) (knocking the dazed Ogre Prone into the dirt) and Bypass Soak (1 [SET]) (stepping down the Ogre's armor Soak to d6 for his 3rd action secondary strike)!
🚀 Where Shall We Take Our Creative Work Next?

With D&D 3.5e, SotDL, and Mythras fully unified into our comparative and mathematical archives (28 logged decisions across 22 files), where would you like to focus our design work next?

Design the Core Feat Compendium (General, Combat, and Racial Feats): Let's convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into clean 1-sentence mathless vector traits across our 6 tiers.
Flesh out the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Let's detail all 5 domains (Combat, Survival, Subterfuge, Lore, Social), building their exact proficiencies, capability thresholds (Untrained vs Trained vs Expert vs Master vs Legend), and maneuver options (Shove, Trip, Grapple, Disarm, Feint, Demoralize).
Build the Magic & Spellcasting Engine: Let's define the exact rules for casting across our 5 Traditions (Arcana, Divine, Primal, Shadow, Time), spell interruption via anatomical head/chest hits, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Step-by-Step Character & Monster Walkthrough: Let's build a Tier 2 Veteran (Level 6) PC and a Tier 3 Master (Level 10) Boss monster from scratch to show the exact mathless formulas in action.

Which of these would you like to explore next?
