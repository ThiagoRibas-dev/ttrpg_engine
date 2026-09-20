# Mathematical Calibration, Success vs. Failure Curves & TTK Design Vectors

When designing and tuning a tabletop role-playing game (TTRPG), the underlying mathematical engine must be carefully calibrated to ensure that **Success vs. Failure curves**, **Time to Kill (TTK)**, and **Resource Depletion rates** align with the desired game tone and pacing.

This document identifies the seven master design decision vectors related to TTRPG mathematical calibration, analyzes how classical systems handle them, and formalizes our target curves for our **High Fantasy Mathless Step-Pool System**.

---

## 1. The 7 Master Design Decision Vectors

```
[ TTRPG Mathematical Calibration Engine ]
  ├── 1. Baseline Task Competency Curve (`What % chance to pass a standard task?`)
  ├── 2. Critical Hit / Surge Frequency (`How often do spiky highlights / [SET] maneuvers occur?`)
  ├── 3. Time to Kill (`TTK`) & Encounter Pacing (`How many rounds/hits to defeat an enemy?`)
  ├── 4. Offensive vs. Defensive Scaling Ratio (`Does damage outpace mitigation at high levels?`)
  ├── 5. Action Economy Depletion & Outnumbering (`How fast does defense consume stamina under swarm?`)
  ├── 6. Resource Recovery vs. Daily Attrition (`What resets in 10 mins vs 8 hours camp?`)
  └── 7. Competency Floor Dominance Ratio (`How often does a higher rank beat a lower rank?`)
```

---

### Vector 1: Baseline Task Competency Curve (`Success vs. Failure %`)
- **Core Design Question:** For a character attempting a standard, challenging task (`DC 5` or equal-tier opposed check), what should be their exact probability (`%`) of success based on their competency rank?
- **Comparative System Philosophies:**
  - *Gritty / Horror (`Call of Cthulhu, OSR B/X`):* Baseline success is **35% - 50%**. Even trained professionals fail half the time. Every roll is desperate.
  - *Pulp / Super-Heroic (`Savage Worlds, D&D 5e Advantage`):* Baseline success is **75% - 85%**. Characters routinely succeed; failure only happens on bad rolls.
  - *Tactical High Fantasy (`D&D 3.5e, Pathfinder 2e`):* Baseline success for a trained/expert character against equal-tier challenges is **60% - 70%**.
- **Our System Target Calibration:**
  We adopt the **Tactical High Fantasy (`65% - 75% Baseline`)** curve for equal-tier challenges, while leveraging our **Competency Floors (`Untrained 0 -> Trained 3 -> Expert 5 -> Master 7 -> Legend 9`)** to provide 100% guaranteed success on routine/challenging tasks within a character's specialized domain:

| Competency Rank | Check Pool & Floor | Routine (`DC 3`) | Challenging (`DC 5`) | Formidable (`DC 7`) | Heroic (`DC 9`) | Target Design Rationale |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **0. Untrained (`Civilian`)**| `2d6 keep highest, Floor 0` | **88.9%** | **55.6%** | *0.0%* | *0.0%* | Coin-flip on DC 5 (`55.6%`); impossible to hit DC 7 without *Die Step-Up*. |
| **1. Trained (`Basic Hero`)**| `3d8 keep highest, Floor 3` | **100.0%** | **87.5%** | **57.8%** | *0.0%* | Reliable professional (`87.5% on DC 5`); solid chance on formidable (`~58%`). |
| **2. Expert (`Specialist`)** | `3d10 keep highest, Floor 5`| **100.0%** | **100.0%** | **78.4%** | **48.8%** | **Engineered Immunity to DC 5 (`100%`).** ~78% on DC 7; ~49% on heroic checks. |
| **3. Master (`Grandmaster`)**| `4d12 keep highest, Floor 7`| **100.0%** | **100.0%** | **100.0%** | **80.2%** | **Engineered Immunity to DC 7 (`100%`).** ~80% on heroic checks. |
| **4. Legendary (`Paragon`)** | `5d12 keep highest, Floor 9`| **100.0%** | **100.0%** | **100.0%** | **100.0%** | **Engineered Immunity to DC 9 (`100%`).** Demigod capability ceiling. |

---

### Vector 2: Critical Hit / Surge Frequency (`Drama & Maneuver Generation`)
- **Core Design Question:** How frequently should a check generate dramatic highlights (`Critical Hits, Double Damage, or Special Effect Tokens [SET]`)?
- **Comparative System Philosophies:**
  - *D&D 3.5e:* Critical hits occur on a `20` (`5%`) up to `15-20` (`30% with Keen Rapier`), but require a confirmation roll (`cutting actual crit frequency in half`).
  - *Pathfinder 2e:* Crits occur when beating the DC by $+10$. Against weak foes (`minions`), crits happen **40-50%** of the time; against Bosses, **~5%**.
  - *Mythras (`BRP $d100$`):* Crits occur on $\le 1/10\text{th}$ of skill (`6-8%`). But **Special Effects (`Maneuvers`)** occur whenever winner beats loser by $\ge 1$ level of success (`happening on 40-60% of all opposed combat rolls`).
- **Our System Target Calibration:**
  To make combat deeply tactical without requiring complex math, our engine splits **Critical Hits (`Lethal Severance`)** from **Maneuver Generation (`[SET] Tokens`)**:
  - **Critical Hit (`Condition A: Rolled Max Die Face OR Condition B: Multi-Beat DC by 2+ dice`):** Occurs on **~15% - 22%** of successful hits. Inflicts double Vitality (`HP`) loss and triggers an immediate **Anatomical Wound Condition (`Severed Tendon / Fractured Rib`)**.
  - **Special Effect Tokens (`[SET] — Multi-Beat Differential`):** Occurs on **~35% - 50%** of successful hits (`whenever two or more dice in your pool independently beat the opponent's highest roll`). Allows immediate table spend (`Impale, Bleed, Disarm, Trip, Riposte`).

---

### Vector 3: Time to Kill (`TTK`) & Encounter Pacing (`Combat Rounds per Enemy`)
- **Core Design Question:** Exactly how many **Combat Rounds (`and successful hits`)** should it take for a character or monster to go from full health to defeated across different enemy tiers?
- **Comparative System Philosophies:**
  - *Lightning Lethal (`Mythras, Cyberpunk, OSR`):* **TTK = 1 to 2 Rounds.** One solid hit past armor severs a limb or kills. Fights are terrifying and over in 3 minutes.
  - *Tactical Attrition (`PF2e, D&D 3.5e Mid-Levels`):* **TTK = 3 to 5 Rounds.** Standard monsters take 3-4 hits; Bosses take 6-10 hits. Fights feel like structured tactical chess matches.
  - *HP Sponge / Slog (`5e High Levels, 3.5e Epic Bloat`):* **TTK = 7 to 12+ Rounds.** Enemies have massive HP pools (`300+ HP`); combat drags for hours.
- **Our System Target Calibration (`Tiered TTK Target`):**
  We engineer our combat math around a **Tactical Attrition Baseline (`TTK 3-5 hits for Standard actors`) with High-Stakes Spiky Lethality (`TTK 1-2 hits when Critical Hits or Severe Anatomical Wounds occur`)**:

| Enemy Tier | Health & Mitigation Architecture | Desired Successful Hits to Kill (`TTK Target`) | Typical Table Time per Encounter |
| :--- | :--- | :---: | :--- |
| **1. Rabble (`Minion Swarms`)** | Zero HP & Zero Location tracking. Soak Rank only (`d4 to d8`). | **1 Hit > Soak (`Instant Kill / Rout`)** | `1 - 2 Rounds total (`5-10 mins table time`)` |
| **2. Underlings (`Squad Soldiers`)**| 2-Hit Checkbox (`[○] [○]`). Soak Rank (`d6 to d10`). | **2 Standard Hits OR 1 Critical Hit** | `2 - 3 Rounds total (`15-20 mins table time`)` |
| **3. Standard PCs & Elites** | Vitality `HP` = `STR + CON` (`16 to 26 HP`). Soak `d6 to d12`. | **3 to 5 Standard Hits (`or 1-2 Crits`)** | `3 - 5 Rounds total (`30-45 mins table time`)` |
| **4. Iconic Champions (`Bosses`)** | Vitality `HP` (`24 to 40 HP`). Soak `d10/d12 Adamantine` + 7 Locations. | **6 to 8 Standard Hits (`or 3-4 Crits`)** | `4 - 6 Rounds total (`45-60 mins table time`)` |

---

### Vector 4: Offensive vs. Defensive Scaling Ratio (`Maintaining Bounded Equilibrium`)
- **Core Design Question:** As characters level from 1 to 20 (`Trained to Legend`), does offensive damage outpace defensive armor/HP (`leading to "Rocket Tag" one-shots`), or does defense outpace attack (`leading to whiff walls`)?
- **Our System Target Calibration (`Exact 1-to-1 Step Equilibrium`):**
  Because our **Check Pools (`2d8 -> 4d12`)**, **Weapon Damage Dice (`d6 -> d12`)**, and **Soak Ranks (`d6 Leather -> d12 Plate`)** all advance across the exact same bounded step scale (`d4 to d12`), our offensive-to-defensive ratio remains at a perfect **1-to-1 equilibrium across all 20 levels**:
  $$\frac{\text{Mean Weapon Damage Die Face (`e.g., d10 = 5.5`)}}{\text{Mean Armor Soak Die Face (`e.g., d10 = 5.5`)}} \approx 1.0\text{ across all Tiers}$$

---

### Vector 5: Action Economy Depletion & Outnumbering Pressure (`The Stamina Burn Clock`)
- **Core Design Question:** How fast should a character's **Stamina (`Poise`)** deplete when defending against multiple attacks (`outnumbering swarms`) or performing strenuous *Die Step-Up* heroics?
- **Our System Target Calibration (`The 4-Round Endurance Clock`):**
  - **Base Stamina Pool:** `2 x CON Die Max Face` *(e.g., `CON d8` = `16 Stamina`; `CON d10` = `20 Stamina`)*.
  - **Expenditure Rates:**
    - `Die Step-Up (`Stepping Up the pool`):` **1 Stamina per check.**
    - `Parry Fatigue (`Active Defense beyond 1st free [1R] slot`):` **1 Stamina per incoming attack.**
  - **Pacing Calibration:** If a character performs 1 Die Step-Up on their turn (`-1 Stamina`) and parries 2 extra enemy attacks (`-2 Stamina`), they burn **3 Stamina per round**. With `16 Stamina`, their aerobic endurance clock lasts **exactly 5 combat rounds** before reaching exhaustion (`Stamina 0 -> Defense pool collapses to 0 -> Soak only`). This forces decisive tactical play within our 3-5 round TTK window!

---

### Vector 6: Resource Recovery vs. Daily Attrition (`The Dual-Frequency Pacing Model`)
- **Core Design Question:** What resources reset quickly after every fight (`allowing high-energy tactical play`), versus what resources carry over across the day (`forcing strategic resource conservation and camp tension`)?
- **Our System Target Calibration (`Dual-Frequency Architecture`):**

```
[ Encounter Ends ]
        │
        ├─────────────────────────────────────────────────┐
        ▼                                                 ▼
[ Short Breather (`10 Minutes`) ]                 [ Long Camp (`8 Hours + 1 Ration`) ]
  ├── 100% Stamina Recovered (`Aerobic breath`)     ├── 100% Vitality (`HP`) Recovered
  ├── 100% Focus Recovered (`Mental/Arcane reset`)  ├── All Minor Wounds Cured automatically
  └── Does NOT heal Vitality (`HP`) or Wounds!      └── 1 Severe/Anatomical Wound Cured (`via Surgery`)
```

- **Why This Pacing Works:** Players enter *every single encounter* with full Stamina and Focus (`allowing them to cast top spells and perform dynamic martial maneuvers without hoarding slots for fight #5`). But **Vitality (`HP`), Anatomical Wound Conditions (`Bleeding Cut, Severed Tendon`), and Equipment Durability Slots (`Armor Sacrifices`)** carry over across the entire expedition, creating intense strategic camp tension!

---

### Vector 7: Competency Floor Dominance Ratio (`Opposed Check Dominance`)
- **Core Design Question:** In an opposed check (`say, Master Floor 7 vs Expert Floor 5`), precisely how often should the superior character win, and how often does exact tie-breaking (`Secondary Die comparison`) come into play?
- **Our System Target Calibration (`70% - 75% Dominance Target`):**
  Our Python simulations (`sim_competency_floors.py`) confirm our target ratios across the 5 competency tiers:
  - **1 Rank Superior (`e.g., Expert vs Trained`):** Superior actor wins **~70%** of the time.
  - **2 Ranks Superior (`e.g., Master vs Trained`):** Superior actor wins **~85%** of the time.
  - **3+ Ranks Superior (`e.g., Legendary vs Untrained`):** Superior actor wins **100%** of the time (`Total Dominance`).
  - **Mirror Matches (`e.g., Expert vs Expert`):** 40% Attacker / 40% Defender / **20% Exact Tie (`broken by secondary die face or active defense priority`)**.
