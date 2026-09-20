# Check Pool Architecture: Master Comparative Matrix of the 3 Candidate Models

To finalize how an actor (`PC, NPC, or Monster`) builds their check pool from **Race + Class + Skills (`Competency Ranks`) + Feats**, we must lock down the exact interaction between our three mechanical check pool variables:

```
[ Assembling a Check Pool: The 3 Mechanical Variables ]
  ├── Knob 1: Die Size (`X` — d4 to d12) ──────────────► Governs Capability Ceiling & Impact (`Can I clear DC 9? Damage vs Soak`)
  ├── Knob 2: Pool Volume (`N` — 1d to 5d) ─────────────► Governs Reliability, Consistency & Maneuver Token (`[SET]`) Count
  └── Knob 3: Competency Floor (`F` — 0, 3, 5, 7, 9) ──► Governs Guaranteed Minimum Face (`Investment-Driven Whiff Immunity`)
```

This document provides an exhaustive, side-by-side comparative analysis across three candidate models: **Model A (`Pure Attribute Size`)**, **Model B (`Swapped Level Size / Attr+Skill Count`)**, and **Model C (`Hybrid Tri-Vector`)**.

---

## 1. Master Comparative Matrix (`The 3 Approaches Side-by-Side`)

| Evaluation Dimension | Model A: Pure Role Separation (`Attribute Size / Skill Volume`) | Model B: Swapped Pool Engine (`Level Size / Attr+Skill Volume`) | Model C: Hybrid Tri-Vector (`Attr+Skill Size / Class Volume`) |
| :--- | :--- | :--- | :--- |
| **1. Check Pool Generation Formula (`Table-Side Synthesis`)** | • **Die Size (`X`):** Governed strictly by **Core Attribute (`STR d10`)**.<br>• **Pool Volume (`N`):** Base `2d` + **Competency Rank Boon (`+0B to +3B`)**.<br>• **Competency Floor (`F`):** `0, 3, 5, 7, 9`. | • **Die Size (`X`):** Governed strictly by **Level / Tier Band (`Lvl 1=d6, Lvl 5=d8, Lvl 9=d10, Lvl 15=d12`)**.<br>• **Pool Volume (`N`):** Governed directly by **Attribute + Skill (`say, STR 3 + Blades 2 = 5 dice -> 5d`)**.<br>• **Competency Floor (`F`):** `0, 3, 5, 7, 9`. | • **Die Size (`X`):** **Core Attribute + Competency Step Upgrades (`Untrained=Base, Trained=+1 Step, Expert=+2 Steps`)**.<br>• **Pool Volume (`N`):** Base `2d` + **Class Martial Boon (`+1B`)** + Tactical Boons (`Flanking`).<br>• **Competency Floor (`F`):** `0, 3, 5, 7, 9`. |
| **2. Cognitive Flow at the Table (`How Fast Players Grab Dice`)** | **Extremely Fast (`Attribute sets Die, Rank sets Count`).**<br>*"My Strength is d10. I'm Trained (+1B -> 3 dice). I roll `3d10`!"* | **Super Clean "Vampire/Shadowrun" Flow (`Dots = Dice`).**<br>*"I have 3 in Strength and 2 in Swords, so I grab 5 dice (`5d`). What tier am I? Veteran (`Level 5`), so I roll `5d8`!"* | **Very Fast (`Step sets Die, Class sets Count`).**<br>*"My Strength is d8, and I'm Trained (+1 Step -> d10). I'm a Fighter (`+1B -> 3 dice`). I roll `3d10`!"* |
| **3. Level 1 Actor Comparison (`Ogre Brute vs. Halfling Rogue vs. Wizard`)** | • **Ogre Brute (`STR d10, Trained`):** `3d10 keep highest (Floor 3)`.<br>• **Halfling Rogue (`AGI d8, Trained`):** `3d8 keep highest (Floor 3)`.<br>• **Wizard (`INT d8, Untrained Combat`):** `2d6 keep highest (Floor 0)`.<br>*Immediate physical size distinction! Ogre feels massive (`d10`), Rogue feels fast (`d8`), Wizard is frail (`d6`).* | • **Ogre Brute (`STR 5, Trained 1`):** `6d6 keep highest (Floor 3)`.<br>• **Halfling Rogue (`AGI 3, Trained 1`):** `4d6 keep highest (Floor 3)`.<br>• **Wizard (`STR 1, Untrained 0`):** `1d6 single roll (Floor 0)`.<br>*All three roll `d6`s at Level 1! Ogre lands vast multi-beat `[SET]` counts (`6 dice`), but cannot naturally hit DC 7 without spending Stamina or racial step overrides!* | • **Ogre Brute (`STR d10 + Trained +1 Step`):** `3d12 keep highest (Floor 3)`.<br>• **Halfling Rogue (`AGI d8 + Trained +1 Step`):** `3d10 keep highest (Floor 3)`.<br>• **Wizard (`STR d6 + Untrained +0 Steps`):** `2d6 keep highest (Floor 0)`.<br>*Strongest physical differentiation! Combines innate attribute size (`d10 vs d8`) with training steps (`+1 step`).* |
| **4. Level 10 Actor Comparison (`Expert / Master Tier Entry`)** | • **Ogre Brute (`STR d12, Master`):** `4d12 keep highest (Floor 7)`.<br>• **Halfling Rogue (`AGI d10, Master`):** `4d10 keep highest (Floor 7)`.<br>• **Wizard (`STR d6, Untrained Combat`):** `2d6 keep highest (Floor 0)`. | • **Ogre Brute (`STR 5, Master 3`):** `8d10 -> capped at 5d10 (Floor 7)`.<br>• **Halfling Rogue (`AGI 4, Master 3`):** `7d10 -> capped at 5d10 (Floor 7)`.<br>• **Wizard (`STR 1, Untrained 0`):** `1d10 single roll (Floor 0)`.<br>*Because Level dictates Die Size (`d10 at Level 10`), the Ogre and Halfling both roll `5d10`!* | • **Ogre Brute (`STR d12 + Master +2 Steps`):** `4d12 over-cap (Floor 7)`.<br>• **Halfling Rogue (`AGI d10 + Master +2 Steps`):** `4d12 keep highest (Floor 7)`.<br>• **Wizard (`STR d6 + Untrained +0 Steps`):** `2d6 keep highest (Floor 0)`. |
| **5. Target Number (`DC`) Bounding & High Fantasy Pacing** | **Natural Attribute Ceiling (`DCs 3 to 11 open from Day 1`).**<br>If a Level 1 giant has `STR d10`, they can attempt DC 9 tasks naturally (`36% chance`). High Fantasy heroes feel above common limits early. | **Rigid Level-Based DC Ceilings (`Level Dictates World Scope`).**<br>Because Level = Die Size (`Lvl 1=d6, Lvl 5=d8, Lvl 9=d10, Lvl 15=d12`), the GM has 100% rigid control over what DCs a party can tackle! Level 1 characters physically CANNOT clear DC 7 without spending Stamina (`Die Step-Up`). | **Bounded Hybrid Ceiling (`DCs 3 to 12 open via training steps`).**<br>Combining attribute size and skill steps allows characters to tackle Formidable (`DC 7`) and Heroic (`DC 9`) obstacles naturally at lower levels when specialized! |
| **6. Multi-Beat Maneuver (`[SET]`) Generation & Consistency** | **Skill-Driven `[SET]` Count.**<br>Because Competency Rank adds dice (`+1B to +3B`), masters naturally roll more dice (`4d-5d`) than novices (`2d`), generating frequent multi-beat tactical maneuvers on hits! | **Attribute+Skill `[SET]` Count.**<br>Because `Attribute + Skill` sets dice count (`4d to 8d -> capped at 5d`), high-attribute characters generate massive multi-beat `[SET]` tokens every single turn right from Level 1! | **Class+Tactics `[SET]` Count.**<br>Because martial classes start with `3dX` (`+1B`) and generalists start with `2dX`, martial fighters naturally out-maneuver civilian spellcasters in physical combat unless spellcasters expend Focus/Boons! |

---

## 2. Deep Comparative Breakdown (`Pros vs. Cons of Each Model`)

### 2.1 Model A: Pure Role Separation (`Attribute = Size X | Competency = Volume N + Floor F`)
- **How it feels:** Clean, transparent 3.5e-style separation. Your **Attribute (`STR d10`)** measures how hard you hit (`capability ceiling & damage vs Soak`). Your **Skill Rank (`Trained +1B -> 3 dice, Floor 3`)** measures how reliably you hit and how high your minimum floor is.
- **🟢 Major Pros:**
  - **Zero Concept Blur:** Every stat on the sheet has exactly one job.
  - **Immediate High Fantasy Scope:** A Level 1 Barbarian with `STR d10` can smash down a heavy iron door (`DC 9`) that a frail Wizard (`STR d6`) cannot naturally dent, while the trained brawler (`3d10, Floor 3`) lands consistent hits over untrained monsters (`2d10, Floor 0`).
- **🔴 Major Cons:**
  - **Lower Volume at Level 1:** Most characters roll `2d` or `3d` at Level 1, meaning multi-beat `[SET]` tokens occur slightly less often (`~28% of hits`) until characters reach Expert/Master tiers (`4d-5d`).

---

### 2.2 Model B: Swapped Pool Engine (`Level = Size X | Attribute + Skill = Volume N`)
- **How it feels:** Classic *Vampire: The Masquerade (v5)*, *Shadowrun*, and *Year Zero Engine (`Forbidden Lands/Alien`)* flow combined with rigid level tiers.
- **🟢 Major Pros:**
  - **Incredible Table Simplicity:** *"I have 3 in Strength and 2 in Swords, so I grab 5 dice (`5d`). What tier am I? Veteran (`Level 5`), so I roll `5d8`!"* That zero-friction counting is universally beloved across pool-based RPGs!
  - **100% Rigid Level Pacing:** Because your Level literally dictates your Die Size (`Lvl 1=d6, Lvl 5=d8, Lvl 9=d10, Lvl 15=d12`), the Game Master knows with absolute certainty what DCs a party can tackle across the campaign. Leveling up (`d6 -> d8 -> d10 -> d12 across 20 levels`) feels like unlocking a brand new dimension of reality!
  - **Frequent Early Maneuvers:** Because characters grab `4d to 6d` right at Level 1 (`STR 3 + Skill 2 = 5d`), they land multi-beat `[SET]` tokens (`Impale, Bleed, Trip`) constantly from turn one!
- **🔴 Major Cons:**
  - **The "Giant vs. Halfling at Level 1" Simulation Dilemma:** If Level strictly dictates Die Size (`say, all Level 1 characters roll d6s`), a **Level 1 Ogre Brute (`STR 5`)** and a **Level 1 Halfling Rogue (`STR 2`)** both roll `d6`s! The Ogre rolls `5d6` (`Max Face = 6`), and the Halfling rolls `2d6` (`Max Face = 6`). Because both share the exact same `d6` ceiling, the Ogre hits vastly more often (`5 dice vs 2 dice`), but physically CANNOT hit a higher DC or deal a higher single damage number than the Halfling without spending Stamina (`Up-Shift`) or needing a heavy racial override (`Giant Size = +1 die step`).
  - **Early DC 7 Ceiling:** Because Level 1 characters roll `d6`s, `DC 7 Formidable` challenges are completely locked off at Level 1 unless players spend Stamina for a Die Step-Up (`d6 -> d8`).

---

### 2.3 Model C: Hybrid Tri-Vector (`Attr+Skill = Size X | Class+Tactics = Volume N + Floor F`)
- **How it feels:** Our highly granular simulationist baseline from `03_core_baseline_system/07_check_pool_generation_and_class_differentiation.md`.
- **🟢 Major Pros:**
  - **Peak Physical Differentiation:** Combines innate attribute size (`STR d8 vs d10`) with training step upgrades (`Trained = +1 Step, Expert = +2 Steps`). A Level 5 Expert Fighter with `STR d10` steps up to **`3d12 (Floor 5)`**, while an untrained brawler rolls `3d10 (Floor 0)`.
  - **Strong Class Identity:** Martial classes (`Fighter, Rogue`) start with Base `3dX` check pool (`+1B Martial Boon`), ensuring physical dominance over civilian/caster baselines (`2dX`).
- **🔴 Major Cons:**
  - Slightly more calculation steps when allocating proficiency steps compared to Model A's pure separation or Model B's clean `Dots = Dice` addition.

---

## 3. Executive Decision Guide (`Which Architecture Best Fits Our Vision?`)

When deciding which check pool architecture to officially lock into our system vault across all 20 levels (`DEC-038`), use these three clear guiding questions:

```
[ Which check engine should we officially lock in? ]
  │
  ├── Choose Model A (`Pure Role Separation`) if you want:
  │     └── Exact 3.5e-style physical ceilings where `STR d10` hits hard on Day 1, and Competency Rank (`Trained/Master`) purely dictates pool reliability (`3d to 5d`) and whiff immunity (`Floor 3 to 9`).
  │
  ├── Choose Model B (`Swapped Level Size / Attr+Skill Count`) if you want:
  │     └── Ultra-fast "Vampire/Shadowrun" table counting (`STR 3 + Swords 2 = 5 dice`), rigid level-based world scope where leveling steps your dice (`Lvl 1=d6, Lvl 5=d8, Lvl 9=d10, Lvl 15=d12`), and frequent early `[SET]` maneuvers!
  │
  └── Choose Model C (`Hybrid Tri-Vector`) if you want:
        └── Maximum biological and training granularity where skill training both steps up your die size (`X+1`) AND sets your floor (`Floor 3 to 9`), while class selection governs your dice count (`3d Martial vs 2d Caster`).
```
