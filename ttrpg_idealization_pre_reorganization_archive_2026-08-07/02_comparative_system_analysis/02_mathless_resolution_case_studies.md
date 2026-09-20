# Mathless Resolution Engine: Comparative Case Studies

To ensure our resolution mechanics are fast, tactile, mathematically sound, and genuinely **mathless** (zero arithmetic during play), we analyzed four critical case studies in modern TTRPG design.

---

## Case Study 1: The Bespoke Mathless System Report (`bespoke mathless system report.md`)

### 1.1 The Design Journey & Evolution
The uploaded developer report documents a 6-month open playtest of a bespoke system built to eliminate mental math entirely while preserving tactical excitement:
- **Phase 1: `2d10` Keep Highest.** Inspired by D&D 5e Advantage, the designer noted that picking up two dice and keeping the higher result delivers immediate "lizard-brain gut satisfaction." However, static `2d10` without modifiers felt too swingy and lacked character progression.
- **Phase 2: Cascading Step-Down Dice & Exploding Dice.** To allow characters with small dice (`d4` or `d6`) to hit higher Target Numbers (DCs 2-12) or bounce back from failure, the designer experimented with:
  - *Exploding Dice (Savage Worlds style):* If you roll maximum (`6` on a $d6$), roll again and add. **Result:** Introduced heavy math and erratic, lethal swinginess.
  - *Cascading Step-Downs:* If a check failed or hit a max face, pick up the next die size down (`d8` after `d10`) and roll/add. **Result:** Mathematically functional but clunky, slow to explain, and destroyed table momentum.
- **Phase 3: "Kill Your Darlings" — The `2dX` Step Pool with Die Step-Up.**
  The designer cut cascading and exploding mechanics entirely right before open playtesting. Instead, they established:
  - **Base Pool:** Every character rolls **`2d(Rank)` keep highest** (`2d6`, `2d8`, `2d10`, `2d12`).
  - **Glitch / Bane:** Remove a die (`1d(Rank)`).
  - **Advantage / Boon:** Add a die (`3d(Rank)` or `4d(Rank)` keep highest).
  - **Die Step-Up:** To overcome the hard mathematical ceiling of small dice (e.g., `2d4` cannot hit DC 6), players spend an in-world stamina resource (`Die Step-Up`) to step their pool up one die size (`2d4` $\to$ `2d6`) before the roll.

### 1.2 Key Takeaways for Our System
- **Immediate Visual Transparency:** When a player rolls `3d8` and sees `2, 5, 8`, they instantly know their result is `8`. There is zero latency between the die landing and the narrative outcome.
- **Stamina-Driven Die Step-Up:** Die Step-Up replaces the abstract "+2 modifier" with a concrete physical exertion choice: *"Do I spend my character's Stamina to step my `2d6` pool up to `2d8` to ensure I can clear DC 7?"*

---

## Case Study 2: Daggerheart & The `2d12` Hope/Fear Engine

### 2.1 Mechanical Summary
Darrington Press’s *Daggerheart* uses a dual-die system where players roll **`1d12` Hope + `1d12` Fear** (`2d12 total`), add an attribute modifier (`+1 to +5`), and compare to a DC.
- If Hope die > Fear die: **Roll with Hope** (gain Hope token, positive narrative spin).
- If Fear die > Hope die: **Roll with Fear** (GM gains Fear token, complication occurs).
- If Hope die == Fear die: **Critical Success**.

### 2.2 Why We Diverge from Daggerheart
While Daggerheart's dual-die narrative axis is engaging, it **violates two of our core design pillars**:
1. **Requires Double-Step Arithmetic:** Players must add two $d12$s (`8 + 7 = 15`), then add a numerical modifier (`15 + 3 = 18`), and then compare vs DC (`18 vs DC 16 = Success`).
2. **Relies on Meta-Currencies:** "Hope" and "Fear" tokens are abstract out-of-character currencies tracked by players and the GM to trigger powers and twists.

### 2.3 What We Adopt (In a Mathless Format)
We adopt the concept of **Die Face Matching & Color/Designation Checks without addition**:
- If a player rolls a multi-die pool (`3d8`), if two dice roll the same high number (`8` and `8`), it triggers a **Mathless Critical Surge** or weapon mastery effect without checking numerical thresholds over the DC.

---

## Case Study 3: Shadow of the Demon Lord (SotDL) Boons & Banes

### 3.1 The SotDL `+d6` Engine
In Robert J. Schwalb's system, whenever a character has an advantage or disadvantage, they roll $N d6$ alongside their $d20$:
- **Boon (`+1 Boon`):** Roll $1d6$, add to $d20$. If `+3 Boons`, roll $3d6$, keep the **single highest $d6$**, and add it to the $d20$.
- **Bane (`+1 Bane`):** Same, but subtract the highest $d6$.
- **Cancellation:** Boons and Banes cancel 1-to-1 before rolling.

### 3.2 Translating SotDL Boons into Our Mathless Step Engine
Because our baseline resolution uses step dice (`2dX` keep highest) rather than $d20 + \text{math}$, we adapt SotDL's brilliance directly into pool volume:
- **1 Boon (`+1B`):** Add $+1\text{ die}$ of your current step rank (`2d8` $\to$ `3d8`).
- **2 Boons (`+2B`):** Add $+2\text{ dice}$ (`4d8 keep highest`).
- **1 Bane (`+1X`):** Remove $-1\text{ die}$ from the pool (`2d8` $\to$ `1d8`).
- **Severe Bane (`+2X` or more):** If a pool is reduced below `1d`, you roll `2d(Rank)` and **keep the lowest result** (Disadvantage).

---

## Case Study 4: Step Dice vs Dice Pools vs Hybrid Engine

### 4.1 The Dilemma
In designing a mathless game that models both **Innate Talent/Power** (Strength, Arcana power) and **Tactical Training/Reliability** (Skill ranks, teamwork, positioning), we must decide how step dice and dice pools interact:
- **Pure Step Dice (`1dX`):** (e.g., Kids on Bikes, Savage Worlds). Fast, but `1d12` is too swingy (`1/12th` chance to roll a `1`).
- **Pure Dice Pools (`Nd6` count 6s):** (e.g., Vampire V5, Shadowrun). Great for reliability, but counting successes slows play down when pools hit 8-12 dice.
- **Our Hybrid Blueprint (`NdX` Keep Highest):**
  - **Step Die Size (`X` = `d4, d6, d8, d10, d12`):** Represents **Absolute Capability & Peak Mastery**. A character with `Arcana d10` can hit a DC 10 spell, whereas a `d6` apprentice physically cannot without *Die Step-Up*.
  - **Pool Volume (`N` = `1d to 4d+`):** Represents **Consistency, Training & Tactical Positioning**. A master swordsman might roll `3d10` (High rank, high consistency), ensuring they almost never whiff on basic DC 5 strikes while frequently hitting high DC 9-10 targets.

---

## Summary Resolution Matrix

| Scenario | Pool Architecture | Target Comparison | Math Required |
| :--- | :--- | :--- | :--- |
| **Standard Check** | `2d(Attribute/Skill Rank)` keep highest | Compare highest face vs DC (`2 to 12`) | **ZERO** |
| **With Tactical Advantage (Boon)** | `3d(Rank)` or `4d(Rank)` keep highest | Compare highest face vs DC | **ZERO** |
| **With Severe Penalty (Bane)** | `1d(Rank)` or `2d(Rank)` **keep lowest** | Compare result vs DC | **ZERO** |
| **Desperate Push against High DC** | Spend 1 Stamina $\to$ **Die Step-Up** (`2d6` $\to$ `2d8`) | Compare new higher faces vs DC | **ZERO** |
| **Opposed Check (Parry vs Strike)** | Attacker rolls `NdX` vs Defender's `MdY` | Compare Attacker Highest vs Defender Highest | **ZERO** (Higher face wins; ties favor active defender or trigger lock) |
