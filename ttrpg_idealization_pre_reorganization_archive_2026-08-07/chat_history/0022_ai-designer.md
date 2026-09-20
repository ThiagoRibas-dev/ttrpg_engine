---
turn: 22
role: "AI-Designer"
source: chat_history.json
---

# Turn 22 — AI-Designer

used
Bash
83ms
Write
ttrpg_idealization/03_core_baseline_system/07_attributes_and_derived_statistics.md
131 lines
open
Core Attributes & Mathless Derived Statistics Architecture
MD
Core Attributes & Mathless Derived Statistics Architecture

To build a High Fantasy simulationist game where a creature's biological and psychological realities are modeled clearly without linear arithmetic (+X / -X), we must establish the exact architecture of our Core Attributes and how they generate Derived Passive Statistics (Defenses, Resource Pools, and Capability Ceilings).

This document evaluates three attribute models and formalizes the mathematical and simulationist linkages between attributes and derived stats across our 20-level scale.

1. Candidate Attribute Architectures (Pros & Cons)
1.1 Option A: The Classic 3.5e Set of 6 (STR, DEX, CON, INT, WIS, CHA)
Structure: 3 Physical (Strength, Dexterity, Constitution) + 3 Mental (Intelligence, Wisdom, Charisma).
Pros:
Direct 3.5e Compatibility: Converting any monster, feat, or spell prerequisite is effortless (3.5e Str 15+ -> STR d8+).
Familiar Archetypal Division: Players instantly understand what each stat represents at a glance.
Cons & Simulationist Limitations:
The "Dexterity God-Stat" Flaw: In 3.5e/PF2e, DEX governs initiative, reflex Evasion, Armor Class, ranged attacks, finesse melee strikes, and top skills (Stealth, Acrobatics). It becomes vastly more valuable than STR unless heavily bounded.
The "Wisdom / Charisma" Semantic Blur: What exactly is WIS? It conflates sensory awareness (Perception), willpower (Will saves), common sense, and divine magic. Meanwhile, CHA conflates social charm (Diplomacy) with soul identity and innate magical force (Sorcerer/Paladin power). This abstract blur hurts grounded simulationism.
1.2 Option B: The 8-Score Symmetrical Biological Matrix (4 Physical / 4 Mental)

To eliminate the "Dexterity God-Stat" and the "Wisdom Blur" while achieving perfect biological and psychological symmetry (inspired by Mythras, BRP, and Ars Magica), we can expand to 8 Core Step Dice:

text
[ 4 Physical Attributes ]                   [ 4 Mental & Spiritual Attributes ]
  ├── Strength (STR) — Kinetic Force          ├── Presence (PRE) — Social & Spiritual Force
  ├── Constitution (CON) — Metabolic Vigor    ├── Willpower (WIL) — Mental Grit & Endurance
  ├── Agility (AGI) — Whole-Body Speed/Dodge  ├── Perception (PER) — Sensory Vigilance & Reflex
  └── Dexterity (DEX) — Fine Precision/Hand   └── Logic (LOG) — Analytical Acuity & Lore
Pros:
Pure Grounded Simulationism: Whole-body mobility (AGI: dodging, jumping, sprinting) is separated from manual eye-hand precision (DEX: archery, lockpicking, surgical edge alignment). You can play a clumsy, heavy-footed dwarf (AGI d4) who is a master jeweler and archer (DEX d10).
Complete Demystification of Mental Traits: Sensory awareness (PER: spotting traps) is separated from mental fortitude (WIL: resisting fear/mind blasts).
Perfect Mirror Symmetry:
STR (Force) 
⟷
⟷ PRE (Command / Aura)
CON (Endurance) 
⟷
⟷ WIL (Grit / Resolve)
AGI (Gross Reflex) 
⟷
⟷ PER (Sensory Alertness)
DEX (Fine Precision) 
⟷
⟷ LOG (Deductive Formulae)
Cons:
8 attributes mean tracking two additional step dice on the character sheet compared to 3.5e. (However, because we do not use numeric scores or 
+
𝑋
+X modifiers, tracking 8 step dice (e.g., d6, d8, d10) is effortless at the table).
1.3 Option C: The 6-Score Biological Refinement (STR, DEX, CON | LOG, PER, WIL)
Structure: Keeps exactly 6 scores (3 Physical / 3 Mental), but redefines the mental side to remove abstract fluff:
3 Physical: Strength (STR), Dexterity / Coordination (DEX), Constitution / Endurance (CON).
3 Mental: Logic / Intellect (LOG), Perception / Acuity (PER), Willpower / Presence (WIL).
Pros:
Exactly 6 scores (preserving exact 3.5e budget size).
Solves the Wisdom blur by clearly separating PER (Senses) from WIL (Grit/Presence).
Cons:
Still merges whole-body speed/dodging with fine manual precision inside DEX (leaving DEX as a dominant stat). And merging social leadership (Charisma) into WIL (Willpower) means every stoic monk is automatically a magnetic social leader.
2. Comparative Evaluation Matrix (Evaluating the Options)
Evaluation Vector	Option A: Classic 3.5e 6 Scores	Option B: Symmetrical 8 Scores	Option C: Biological 6 Scores
Simulationist Realism	Medium (Conflates senses/will in WIS; gross/fine mobility in DEX).	Peak (100% granular division of force, endurance, speed, precision, senses, and resolve).	High (Clears mental blur, but leaves DEX conflated).
Symmetry & Balance	Medium (DEX outclasses STR/CON; WIS/CHA have uneven weight).	Exact (4 Physical vs 4 Mental; exact 1-to-1 functional mirrors).	High (3 Physical vs 3 Mental).
3.5e Conversion Speed	Instant (1-to-1 exact names)	Very Fast (Split DEX -> AGI/DEX; split WIS -> PER/WIL).	Fast (Direct mapping with clear mental renames).
Sheet Complexity	6 Step Dice (Low)	8 Step Dice (Low-Medium — clean step letters).	6 Step Dice (Low).
3. Mathless Derived Statistics Generation (How Attributes Build the Sheet)

Regardless of whether we select Option B (8 Scores — Recommended Baseline) or Option A/C (6 Scores), derived statistics are generated using Direct Step Max Faces and Step Ranks, completely eliminating table-side multiplication or addition equations!

3.1 In-World Resource Tracks (Base Capacity Formulas)
Resource Track	Derivation Formula (Option B: 8-Score Baseline)	Derivation Formula (Option A: Classic 6-Score Baseline)	Why This Works Without Table Arithmetic
1. Vitality (HP)	STR Die Max + CON Die Max<br>(e.g., 
𝑆
𝑇
𝑅
 
𝑑
8
+
𝐶
𝑂
𝑁
 
𝑑
10
→
8
+
10
=
18
 Base Vitality
STR d8+CON d10→8+10=18 Base Vitality)	STR Die Max + CON Die Max<br>(e.g., 
8
+
10
=
18
8+10=18)	Directly represents physical tissue density (CON) and skeletal/muscular bulk (STR). Scales naturally when attributes step up!
2. Stamina (Poise)	2 x CON Die Max<br>(e.g., 
2
×
10
=
20
 Base Stamina
2×10=20 Base Stamina)	2 x CON Die Max<br>(e.g., 
2
×
10
=
20
2×10=20)	Represents aerobic endurance and muscle glucose. Simple doubling of a single die face (or CON Max + AGI Max).
3. Focus (Acuity)	WIL Die Max + LOG (or PER) Die Max<br>(e.g., 
𝑊
𝐼
𝐿
 
𝑑
8
+
𝐿
𝑂
𝐺
 
𝑑
10
→
18
 Base Focus
WIL d8+LOG d10→18 Base Focus)	WIS Die Max + INT Die Max<br>(e.g., 
8
+
10
=
18
8+10=18)	Represents mental discipline and magical energy channeling capacity.
4. Durability Slots	Governed strictly by Equipped Item Material & Quality (1 to 4 Slots).	Governed strictly by Equipped Item Material & Quality.	Material properties (Steel vs Adamantine) dictate structural integrity independently of character stats.
3.2 The Four Passive Defenses (Mathless Mitigation Layers)

Instead of calculating 10 + Armor + Shield + Dex + Size, our 4 Defense Layers are derived directly from attribute step sizes and equipment ranks:

text
[ Incoming Attack / Threat Declared ]
                 │
                 ├─────────────────────────────────────────────────┐
                 ▼                                                 ▼
      [ Physical Kinetic Strike ]                     [ Magical / Internal Threat ]
                 │                                                 │
       ┌─────────┴─────────┐                             ┌─────────┴─────────┐
       ▼                   ▼                             ▼                   ▼
Layer 1: Evasion    Layer 2: Parry               Layer 3: Resilience  Layer 4: Soak Rank
 (AGI Step Die)    (Combat Mastery Pool)          (CON / WIL Step Pool) (Armor Step Die)
Defense Layer	Derivation Formula (Option B: 8-Score Baseline)	Derivation Formula (Option A: 6-Score Baseline)	Tactical & Simulationist Mechanics
1. Evasion (Dodge Pool)	Derived directly from AGI Step Die (e.g., AGI d8 
→
→ Evasion Pool 2d8 keep highest).	Derived directly from DEX Step Die (e.g., DEX d8 
→
→ 2d8 keep highest).	Used when dodging ranged projectiles or area blasts (AoE). In Mode 2/3 Contests, target rolls Evasion vs Attacker check pool.
2. Parry (Active Intercept)	Derived directly from Combat Mastery Domain Pool (e.g., Mastered 4d10).	Derived directly from Combat Mastery Domain Pool.	Used when actively deflecting melee strikes (costs 1 Reaction [1R] or 1 Stamina). Opposed roll vs Attacker pool.
3. Soak Rank (Armor Reduction)	Derived exclusively from Equipped Armor & Physical Hide (d4 Cloth 
→
→ d12 Plate).	Derived exclusively from Equipped Armor & Physical Hide.	Checked post-hit. Compare Attacker Damage Die Face vs Defender Soak Die Face. If Damage <= Soak, kinetic shock absorbed (0 Wounds).
4. Resilience (Fortitude/Will)	Physical Fortitude: 2dCON keep highest<br>Mental/Spiritual Will: 2dWIL keep highest	Physical Fortitude: 2dCON keep highest<br>Mental/Spiritual Will: 2dWIS keep highest	Replaces saving throws. When targeted by poisons, disease, mind blasts, or death curses, defender rolls Resilience vs Caster Power Pool.
4. Initiative, Speed & Carrying Capacity (Tactical Parameters)
4.1 Initiative & Reflex Speed (Combat Action Order)
Mathless Initiative Roll: At the start of combat, actors make an opposed check based on situational readiness:
Physical Reflex Ambush: Roll base AGI Pool (Option B: 2dAGI | Option A: 2dDEX).
Tactical Assessment / Prepared Guard: Roll base PER or LOG Pool (Option B: 2dPER | Option A: 2dINT/WIS).
Turn Order: Sort combatants from Highest Single Face Rolled down to lowest (12 to 2). Ties broken by second die in pool (Secondary Tiebreaker).
4.2 Tactical Movement Speed (Grid & Zone Stride)
Standard Base Speed: Every character of Medium or Small size has a base [1A] Stride of 30 feet (1 Distance Tier shift / 6 Grid Squares).
Agility / Reflex Speed Modifier:
AGI d4 (Impaired/Heavy Sluggish): Speed 20 ft (4 Squares).
AGI d6 / d8 (Standard/Athletic): Speed 30 ft (6 Squares).
AGI d10 / d12 (Elite/Legendary Runner): Speed 40 ft (8 Squares / can cross a full zone with excess momentum).
4.3 Carrying Capacity (Encumbrance Slots via STR/MIG)

To avoid tracking exact pounds (142.5 lbs), characters have a concrete budget of Encumbrance Slots:

Max Encumbrance Slots
=
STR Die Max Face
+
4
 Slots
Max Encumbrance Slots=STR Die Max Face+4 Slots

STR d6: 6 + 4 = 10 Slots (Light armor 1, sword 1, shield 1, rations/gear 7).
STR d10: 10 + 4 = 14 Slots (Heavy plate 3, greatsword 2, backup weapons, heavy loot).
Overburdened (Exceeding Slot Limit): All AGI and Evasion check pools immediately suffer $-1\text{ Die Step-Down (d8 
→
→ d6)}$.
Open
used
Bash
78ms

We have brainstormed the pros, cons, and derived statistic linkages for your attribute architecture across three models and formalized them in 03_core_baseline_system/07_attributes_and_derived_statistics.md (presented above).

🧠 Brainstorming the Attribute Architectures (Pros vs. Cons)
Option A: The Classic 3.5e Set of 6 (STR, DEX, CON | INT, WIS, CHA)
The Structure: 3 Physical + 3 Mental.
Pros:
1-to-1 3.5e Conversion Ease: Any 3.5e prerequisite (Str 13+, Dex 15+) converts directly into our step dice (STR d6+, DEX d8+).
Proven Physical Symmetry: Clearly separates active force (Strength), coordination/speed (Dexterity), and biological endurance (Constitution).
Cons & Traditional Flaws:
The "Dexterity God-Stat" Problem: In D&D, DEX governs Initiative, Evasion/Reflexes, Armor Class, Ranged Attacks, Finesse Melee, and top skills (Stealth, Acrobatics). It outclasses STR and CON unless strictly bounded.
The "Wisdom / Charisma" Semantic Blur: What is WIS? It conflates sensory perception (Spot/Listen), willpower/sanity (Will saves), common sense, and divine magic. Meanwhile, CHA conflates social charm (Diplomacy) with soul identity and innate magical force (Sorcerers/Paladins). This abstract blur hurts grounded simulationism.
Option B: The 8-Score Symmetrical Biological Matrix (4 Physical / 4 Mental — Recommended Baseline)

To eliminate the "Dexterity God-Stat" and the "Wisdom Blur" while achieving perfect biological and psychological symmetry (inspired by Mythras, BRP, and Ars Magica), we expand to 8 Core Step Dice:

text
[ 4 Physical Attributes ]                   [ 4 Mental & Spiritual Attributes ]
  ├── Strength (STR) — Kinetic Force          ├── Presence (PRE) — Social & Spiritual Force
  ├── Constitution (CON) — Metabolic Vigor    ├── Willpower (WIL) — Mental Grit & Endurance
  ├── Agility (AGI) — Whole-Body Speed/Dodge  ├── Perception (PER) — Sensory Vigilance & Reflex
  └── Dexterity (DEX) — Fine Precision/Hand   └── Logic (LOG) — Analytical Acuity & Lore
Pros:
Pure Grounded Simulationism: Whole-body mobility (AGI: dodging, jumping, sprinting) is completely separated from manual precision (DEX: archery, lockpicking, surgical edge alignment). You can play a heavy-footed, clumsy dwarf (AGI d4) who is a master jeweler and deadly archer (DEX d10).
Complete Demystification of Mental Traits: Sensory awareness (PER: spotting traps) is separated from mental grit (WIL: resisting fear/mind blasts).
Exact Mirror Symmetry (4 vs 4): Every physical trait has an exact functional mental counterpart (STR Force <-> PRE Force, CON Endurance <-> WIL Endurance, AGI Reflex <-> PER Reflex, DEX Precision <-> LOG Precision).
Cons:
8 attributes instead of 6 on the sheet. (However, because we do not use numeric scores or 
+
𝑋
/
−
𝑋
+X/−X math, tracking 8 lettered step dice (e.g., d6, d8, d10) is effortless).
Option C: The 6-Score Biological Refinement (STR, DEX, CON | LOG, PER, WIL)
The Structure: Keeps exactly 6 scores (3 Physical / 3 Mental), but renames the mental side to remove abstract fluff (Logic, Perception, Willpower).
Pros: Exact 6-stat budget; demystifies WIS into PER and WIL.
Cons: Still merges whole-body speed with manual hand precision inside DEX (leaving DEX as a dominant stat).
📐 How Attributes Derive Passive Statistics Mathlessly

Whether we use Option B (8 Scores) or Option A (Classic 6 Scores), derived statistics are generated using Direct Step Max Faces and Ranks, zeroing out arithmetic:

1. In-World Resource Tracks (Base Capacity)
Vitality (HP): STR Die Max + CON Die Max (e.g., 
𝑆
𝑇
𝑅
 
𝑑
8
+
𝐶
𝑂
𝑁
 
𝑑
10
→
8
+
10
=
18
 Base Vitality
STR d8+CON d10→8+10=18 Base Vitality). Directly represents physical skeletal/muscular bulk and tissue density. Scales naturally as attributes step up!
Stamina (Poise): 2 x CON Die Max (e.g., 
2
×
10
=
20
 Base Stamina
2×10=20 Base Stamina). Represents aerobic capacity and muscle glucose.
Focus (Acuity): WIL Die Max + LOG (or PER) Die Max. Represents mental discipline and magical energy channeling capacity.
2. The Four Passive Defense Layers

Instead of calculating 10 + Armor + Shield + Dex, incoming threats check the appropriate physical or mental layer directly:

Layer 1: Evasion (Dodge Pool): Derived directly from AGI Step Die (Option B: 2dAGI) or DEX (Option A). Used against ranged projectiles and area blasts.
Layer 2: Parry (Active Intercept): Derived directly from Combat Mastery Domain Pool (3dX to 5dX). Used against melee strikes.
Layer 3: Resilience (Fortitude / Will Saves):
Physical Fortitude: 2dCON keep highest vs poison, disease, and metabolic shock.
Mental/Spiritual Will: 2dWIL keep highest vs fear, mind blasts, and death curses.
Layer 4: Soak Rank (Armor Step Die): Derived exclusively from Equipped Armor & Hide (d4 Cloth -> d12 Plate). Checked post-hit (Damage Die vs Soak Die).
3. Initiative, Speed & Carrying Capacity
Initiative (Turn Order): Roll opposed 2dAGI (Physical Reflex/Ambush) OR 2dPER / 2dLOG (Tactical Readiness). Sort from highest face (12) down to (2).
Tactical Speed: Base 30 feet ([1A] Stride = 1 Tier shift). AGI d10/d12 increases base speed to 40 feet.
Carrying Capacity (Encumbrance Slots): 
Max Slots
=
STR Die Max Face
+
4
 Slots
Max Slots=STR Die Max Face+4 Slots (e.g., STR d8 = 8 + 4 = 12 Slots for weapons, armor, and gear).
⚖️ Which Option Do You Prefer?

Do you want to lock in Option B (The 8-Score Symmetrical Biological Matrix: STR, CON, AGI, DEX | LOG, PER, WIL, PRE) as our official baseline for maximum simulationist precision and symmetry, or would you prefer to stick with Option A (The Classic 3.5e 6 Scores: STR, DEX, CON, INT, WIS, CHA) for 1-to-1 D&D nostalgia?
