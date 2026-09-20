# Demon Lord System (SotDL / Weird Wizard) Conversion Procedure

Robert J. Schwalb’s **Shadow of the Demon Lord (SotDL)** and **Shadow of the Weird Wizard** serve as our secondary architectural anchors. Their signature contribution—replacing flat numerical modifiers (`+2 / -2`) with dynamic **Boons and Banes (`Nd6`)**—and their **3-Tier Modular Path Architecture** (`Novice -> Expert -> Master`) provide the exact modular blueprint needed to build a high-content, option-rich mathless system.

This document details the exact procedures for translating SotDL/Weird Wizard content into our **Mathless Step Pool Engine**.

---

## 1. Translating Boons & Banes Without $d6$ Addition

In SotDL, when a character has a situational advantage, they roll $1d20 + \text{Attribute Modifier} + \text{Highest of } Nd6$. While vastly cleaner than 3.5e, **this still requires table-side addition ($d20 \pm d6$).**

We port the SotDL boon/bane engine into our system by converting the extra $d6$ into **Step Pool Volume Adjustments (`+1d / -1d of your base step die`)**:

| SotDL / Weird Wizard Mechanic | Mathless Converted Pool Shift | Tactical & Mathematical Equivalent |
| :--- | :--- | :--- |
| **`+1 Boon` (Roll $+1d6$, add highest)** | **$+1\text{ Boon Die (`+1B`)}$:** Add $+1\text{ die}$ of your current step rank to the pool (`2dX` $\to$ `3dX keep highest`). | Increases your average rolled face by $\approx 20\%$, virtually eliminating critical fumbles without changing the max ceiling. |
| **`+2 Boons` (Roll $+2d6$, add highest)** | **$+2\text{ Boon Dice (`+2B`)}$:** Roll `4dX keep highest`. | Represents overwhelming advantage; standard DC 5-7 checks become almost guaranteed successes. |
| **`+3 Boons or more`** | **$+3\text{ Boon Dice (`+3B`)}$:** Roll `5dX keep highest`. | Maximum pool volume cap. |
| **`-1 Bane` (Roll $+1d6$, subtract highest)** | **$+1\text{ Bane Die (`+1X`)}$:** Remove $-1\text{ die}$ from your check pool (`2dX` $\to$ `1dX` single die roll). | Strips away safety net; forces the character to rely purely on raw die size (`X`). |
| **`-2 Banes` (Roll $+2d6$, subtract highest)** | **$+2\text{ Bane Dice (`+2X`)}$:** Roll `2dX keep LOWEST` (`Disadvantage`). | Represents severe tactical impairment (blindness, heavy cover, physical restraint). |
| **`-3 Banes or more`** | **$+3\text{ Bane Dice (`+3X`)}$:** Roll `3dX keep LOWEST`. | Extreme tactical jeopardy; clearing anything above DC 4 requires extreme luck or *Die Step-Up*. |

---

## 2. Converting the 3-Tier Path Architecture (`Novice, Expert, Master`)

In place of 20-level linear classes or rigid prestige class prerequisite chains, our system adopts SotDL's 3-Tier Path architecture. A character's identity is constructed by layering three modular **Paths** chosen at specific milestones.

```
[ Character Build: Modular Path Layering ]
  ├── Novice Path (Chosen at Milestone 1: Core Archetype)
  │     └── Grants baseline step dice, core domain proficiencies, and basic combat recovery.
  ├── Expert Path (Chosen at Milestone 3: Professional Specialization)
  │     └── Grants domain `+2B` mastery, specialized maneuvers, or intermediate spell traditions.
  └── Master Path (Chosen at Milestone 6: High-Concept Paragon)
        └── Grants legendary capability unlocks, free `Die Step-Up`, and mythic powers.
```

### 2.1 Sample Converted Path: The Berserker (`Expert Path`)
Let's convert the iconic SotDL Berserker path into our mathless mechanics:

- **Path Tier:** Expert Combat Path
- **Entry Requirement:** `Trained (`+1B`)` in `Combat Mastery` and `MIG d8+`.
- **Level 3 Talent: Berserk Fury (`Stamina Surge`)**
  - *Mathless Mechanic:* As a `[0A] Free Trigger` on your turn, you can spend `2 Stamina` to enter a **Berserk Fury**. For the next round, all of your melee Strikes gain **$+2\text{ Boon Dice (`4dX keep highest`)}$** and your **Soak Rank steps up one step (`d8` $\to$ `d10`)**. However, your blind aggression leaves you exposed: all incoming attacks targeting your **Evasion or Parry gain $+1\text{ Boon Die (`3dX`)}$**.
- **Level 6 Talent: Unstoppable Juggernaut (`Wound Resistance`)**
  - *Mathless Mechanic:* While in a Berserk Fury, you are completely immune to the **Shaken**, **Prone**, and **Muddled** status conditions. Furthermore, when an enemy strike inflicts a **Severe Lethal Wound (`0 Vitality or Critical Hit`)**, you can make a **Resilience Check (`DC 7`)**. On a success, you ignore the wound condition entirely and stabilize at `1 Vitality`, continuing your onslaught.

---

## 3. Translating Spell Traditions & Dark Fantasy Tracks

SotDL organizes magic into discrete **Traditions** (`Fire`, `Shadow`, `Time`, `Forbidden`, `Necromancy`) rather than massive generic spell lists. We adopt this directly: each Tradition operates as a distinct **Action Mastery Domain** linked to `Intellect` or `Will`.

### 3.1 The Corruption & Insanity Tracks (`Zero Math Degradation`)
To capture SotDL’s gritty dark fantasy atmosphere without numerical tracking (`Tracking 1 to 20 Insanity points`), we implement them as **In-World Step Degradation Tracks**:

#### The Insanity Clock (`6-Step Mental Stress`)
Whenever a character witnesses cosmic horror, reads forbidden tomes, or experiences immense psychological trauma, the GM requires a **Will Resilience Check (`2dWIL keep highest vs Horror DC 6-9`)**.
- **On a Failure:** Check off **1 Step** on your personal **Insanity Clock** (`[●] [○] [○] [○] [○] [○]`).
- **Mechanical Effect:** When your clock reaches **3 Steps (`Halfway`)**, your `Intellect` and `Will` step dice suffer a permanent **Die Step-Down (`d10` $\to$ `d8`)** during social and analytical tasks. When all **6 Steps** fill, your character suffers a **Permanent Quirky Madness / Mania** (or rolls on the Weird Wizard Quirks table) and the clock resets to zero.

#### The Corruption Track (`Dark Magic & Moral Decay`)
Whenever a character casts a spell from the `Forbidden` or `Necromancy` traditions, or commits an unspeakable act of cruelty, they gain a **Corruption Mark**.
- **Mathless Effect:** Each Corruption Mark grants **$+1\text{ Boon Die (`+1B`)}$** when rolling intimidation or casting dark magic, BUT imposes **$+1\text{ Bane Die (`+1X`)}$** when interacting with natural beasts, holy sanctuaries, or healing miracles. At `3 Corruption Marks`, the character develops a physical **Gothic Deformity** (`Horns`, `Pale eyes`, `Necrotic scent`).
