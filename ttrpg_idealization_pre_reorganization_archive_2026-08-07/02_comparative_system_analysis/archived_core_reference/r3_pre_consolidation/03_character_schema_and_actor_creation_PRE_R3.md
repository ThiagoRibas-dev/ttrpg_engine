# Character Schema & Core Stat Architecture

This document maps out the comprehensive data schema for player characters and NPCs in our idealized TTRPG system. Every character attribute, capability, defense, and resource is structured to operate seamlessly with our mathless `2dX` resolution engine.

---

## 1. Core Innate Attributes (`Classic 6 Step Dice`)

To facilitate seamless 3.5e compatibility while zeroing out arithmetic, every character is defined by the **Classic Six Ability Scores (`STR, DEX, CON, INT, WIS, CHA`)**, rated as **Step Dice (`d4` to `d12`)**. Shared baseline terms are defined in `00_baseline_framework_glossary.md`.

| Ability Score | Abbr. | Physical / Mental Representation | Primary Check Applications |
| :--- | :---: | :--- | :--- |
| **Strength** | `STR` | Muscular density, raw kinetic force, lifting leverage, and physical momentum. | Melee weapon strikes (`Combat Mastery`), breaking doors, athletics, carrying capacity slots. |
| **Dexterity** | `DEX` | Whole-body coordination, manual dexterity, reflexes, balance, and precision. | Finesse melee strikes, archery (`Combat Mastery`), acrobatics, stealth, lockpicking. |
| **Constitution** | `CON` | Metabolic health, tissue vitality, cardiovascular endurance, and toxin resistance. | Physical stamina checks, surviving extreme climates, resisting poisons and bleeding. |
| **Intelligence** | `INT` | Analytical logic, memory capacity, spatial geometry, and arcane formula comprehension. | Deciphering ancient lore, casting complex arcane spells, tactical battlefield analysis. |
| **Wisdom** | `WIS` | Mental discipline, sensory vigilance, emotional poise, and divine/primal connection. | Spotting hidden traps (`Perception`), resisting mind blasts, channeling divine/primal miracles. |
| **Charisma** | `CHA` | Force of personality, social magnetism, aura projection, and innate soul resonance. | Diplomacy, intimidation, leadership command, channeling innate sorcery/pact magic. |

### Attribute Step Scale
- **`d4` (Impaired / Childlike):** Below average capacity; requires *Die Step-Up* (`Stamina spend`) to accomplish standard DC 6 tasks.
- **`d6` (Standard Adult):** Normal baseline competence.
- **`d8` (Professional / Athlete):** Advanced training and innate vigor.
- **`d10` (Heroic / Elite):** Peak mortal prowess; routinely clears DC 8-9 challenges.
- **`d12` (Legendary / Paragon):** Superhuman or mythological mastery.

---

## 2. Action Mastery Domains & Specific Skills

To combine D&D 3.5e's granular skill specialization with clean organization, our system categorizes **Specific Skills** (`Stealth, Lockpicking, Athletics, Arcana, Nature, Diplomacy, Intimidation, Deception, Blades, Bows, etc.`) under five **Action Mastery Domain Umbrellas**.

### 2.1 The Five Domain Umbrellas
1. **Combat Mastery Domain (`STR / DEX`):** Specific skills: *Blades, Axes, Maces, Polearms, Bows, Crossbows, Thrown, Shields, Martial Arts, Brawling.*
2. **Survival & Athletics Domain (`STR / CON`):** Specific skills: *Climbing, Swimming, Jumping, Tracking, Foraging, Beast Handling, Climate Survival.*
3. **Subterfuge & Navigation Domain (`DEX / INT`):** Specific skills: *Stealth (Moving Silently), Camouflage (Hiding from view), Lockpicking, Trap Disarming, Acrobatics, Sailing/Piloting.*
4. **Lore & Crafting Domain (`INT / WIS`):** Specific skills: *Arcana (Draconic/Planar lore), Nature (Beasts/Flora lore), History, Medicine, Alchemy, Blacksmithing, Engineering, Deciphering Runes.*
5. **Social & Influence Domain (`WIS / CHA`):** Specific skills: *Diplomacy (Persuasion), Intimidation (Coercion), Deception (Lying/Bluffing), Leadership (Command), Insight (Empathy), Performance.*

### 2.2 Investment-Driven Competency Allocations (`Specific Skill Mastery`)
When a character levels up (`DEC-020 & DEC-029`), they allocate proficiency points into **Specific Individual Skills** (`not the broad umbrella!`). A character can reach `Expert (+1B, +1 Step, Floor 5)` in *Diplomacy*, while leaving *Deception* and *Intimidate* under the same Social umbrella at `Untrained (Floor 0)`!

---

## 3. The Four Defense Scores (`Paired Physical/Mental Derivations`)

Instead of calculating a single abstract "Armor Class" (`AC = 10 + Dex + Armor + Shield`), characters possess four distinct defensive ranks. When an incoming attack or threat is declared, the GM or player checks which layer is targeted:

```
                          [ Incoming Attack / Threat Declared ]
                                           │
                    ┌──────────────────────┴──────────────────────┐
                    ▼                                             ▼
        [ Physical Kinetic Strike ]                     [ Magical / Internal Threat ]
                    │                                             │
         ┌──────────┴──────────┐                       ┌──────────┴──────────┐
         ▼                     ▼                       ▼                     ▼
Layer 1: Reflexes       Layer 2: Parry          Layer 3: Fort / Will   Layer 4: Soak Rank
 (DEX+INT Dodge Pool)  (Combat Mastery Pool)     (Paired Saving Pool)   (Armor Step Die)
```

| Defense Layer | Derivation Source | Target Comparison & Mechanics |
| :--- | :--- | :--- |
| **1. Reflexes (`Evasion`)** | **`DEX + INT` Paired Pool**<br>*(e.g., `1dDEX + 1dINT keep highest`)* | Used when dodging ranged projectiles, traps, and area blasts (`AoE Fireball`). In `Mode 2/3 Contests`, target rolls Reflexes vs Attacker check pool. |
| **2. Parry (`Active Intercept`)**| **`Combat Mastery` Domain Pool**<br>*(e.g., `3d10 keep highest`)* | Used when actively deflecting melee strikes (`costs 1 Reaction [1R] or 1 Stamina`). Opposed roll vs Attacker combat pool. |
| **3. Resilience (`Fort / Will`)**| **Fortitude:** `STR + CON` Pool<br>**Willpower:** `WIS + CHA` Pool | Replaces 3.5e Fortitude/Will saves. `Fortitude` (`1dSTR + 1dCON`) opposes poison and disease. `Willpower` (`1dWIS + 1dCHA`) opposes mind blasts and curses. |
| **4. Soak Rank (`Armor Reduction`)**| Exclusively **Equipped Armor & Hide**<br>*(e.g., `d4 Cloth` $\to$ `d12 Plate`)* | **Checked post-hit.** Compare `Attacker Damage Die Face vs Defender Soak Die Face`. If `Damage <= Soak`, kinetic shock absorbed (`0 Wounds`). |

---

## 4. In-World Resource Tracks (Zero Meta-Currencies)

All spendable resources exist strictly within the fictional reality of the character. There are no out-of-character tokens (`Inspiration`, `Fate Points`).

### 4.1 Vitality Pool & Wound Conditions (`HP & Injury`)
- **Vitality (`HP`):** Represents minor scrapes, cuts, physical shock, and luck. Starting Vitality equals `STR Die Max + CON Die Max` (`e.g., d8 + d10 = 18 Vitality`).
- **Wound Conditions (Concrete Injuries):** When an attack beats a character's **Soak Rank** (`Damage Die > Soak Die`), or when Vitality drops to `0`, the character takes a **Wound Condition** (`Bleeding Cut`, `Fractured Arm`, `Concussion`). Each Wound imposes a specific mechanical **Die Step-Down** or **Bane** on relevant physical tasks until treated.

### 4.2 Stamina & Poise Pool (`Exertion & Heroics`)
- **Stamina Pool:** Represents aerobic capacity, breath, muscle glucose, and tactical balance. Starting Stamina equals `2 x CON Die Max` (`or CON Max + DEX Max`).
- **Stamina Expenditures:**
  - **Die Step-Up Action (`1 Stamina`):** Step your check pool up one die rank (`2d6` $\to$ `2d8`) before rolling.
  - **Emergency Reflexes / Surge (`2 Stamina`):** Take an immediate out-of-turn reaction to dodge or move 5 feet when targeted by an attack.
  - **Absorb Kinetic Shock (`1 Stamina per point`):** When an attack beats your Soak, you can burn Stamina to absorb the excess impact and prevent a severe Wound Condition.

### 4.3 Focus Track & Vancian Spellcasting (`Arcane / Divine Engine`)
- **Vancian Spell Slots (`Daily Preparations`):** Just like D&D 3.5e, spellcasters prepare daily **Vancian Spell Slots by Spell Level (`1st to 9th level slots`)**. Casting a prepared spell (`e.g., Fireball from a 3rd-level slot`) **consumes the Vancian slot (`Daily Resource`) without costing Focus by default!**
- **Focus Pool (`WIS Die Max + INT Die Max`):** Focus is a short-rest mental acuity pool (`DEC-006 & Section 4`) reserved strictly for secondary magical/mental exertions:
  - **Spell Concentration (`1 Focus/round`):** Sustaining active ongoing spells after taking damage or disruption.
  - **Arcane Die Step-Up (`1 Focus`):** Performing an on-demand Die Step-Up (`Up-Shift: d8 -> d10`) on a spell's check pool.
  - **Metamagic Channeling (`1 to 3 Focus`):** Channeling Metamagic Feats (`Quicken, Empower, Silent Spell`) without consuming higher-level Vancian slots!

### 4.4 Durability Slots vs. Item Hardness & Sundering (`3.5e Upgrade`)
- **Material Hardness Step Die:** Every item's raw material dictates its **Hardness Step Die (`d6 Wood, d8 Iron, d10 Steel, d12 Adamantine`)** and its **Durability Slots (`1 to 4 Slots`)**.
- **Mathless Sunder & Item Sacrifice (`Damage vs Hardness`):** When an attacker attempts a Sunder maneuver (`[1A]`) OR when a defender declares a Heroic Item Sacrifice to absorb 100% of a critical hit, compare:
  $$\text{Attacker Damage Die Face vs Item Hardness Die Face (`Damage vs Hardness`)}$$
  - If `Damage Face <= Hardness Face`: Item absorbs or deflects shock (`0 Slots lost`).
  - If `Damage Face > Hardness Face`: Item bends/cracks (`loses 1 Durability Slot`).
  - If `Critical Sunder (`Max Face OR 2+ steps over Hardness`)`: Item shatters (`loses 2 Slots or breaks completely`).

---

## 5. Universal Actor Architecture (`Race + Class + Skills + Feats`)

To surpass D&D 3.5e in structural transparency and consistency, our system enforces a **Universal Actor Schema**. Every single entity in the game world—whether a Player Character (`PC`), a human blacksmith NPC, an Ogre Brute, a Red Dragon, or an Undead Lich—is built using the exact same four foundational building blocks:

```
[ Universal Actor Building Blocks (PC, NPC, or Monster) ]
  ├── 1. Race / Ancestry / Species
  │        └── Grants Base Size, Speed, Baseline Attribute Steps (`d6/d8`), & Racial Feats/Traits.
  ├── 2. Class Levels (`Up to 20 Levels across 4 Tiers of Play`)
  │        └── Grants Vitality/Stamina growth, Action Mastery Domain Boons (`+B`), & Class Feats.
  ├── 3. Skills (`Action Mastery Domain Proficiencies`)
  │        └── Governs pool volume reliability across Combat, Survival, Subterfuge, Lore, & Social.
  └── 4. Feats (`General, Combat, Racial, Class, Metamagic`)
           └── Modular mathless vector traits (`Up-Shift`, `[SET]` triggers, Maneuvers, & Immunities).
```

### 5.1 Why This Universal Schema Elevates Simulationism
In traditional d20 games, monsters often follow arbitrary rules (`Monster Hit Dice`, ad-hoc attack bonuses, unlisted skill DCs). In our system, **if a Red Dragon performs a Tail Sweep or a Breath Weapon, it uses the exact same `2dX keep highest` mathless check and action point (`[2A]`) rules as a PC warrior performing a Cleave or a Wizard casting Fireball.**

### 5.2 Universal Actor Comparison (`PC vs Monster Example`)

| Architectural Block | Player Character (`Elf Blade Dancer Lvl 6`) | Monster / Creature (`Ogre Brute Lvl 6`) |
| :--- | :--- | :--- |
| **1. Race / Ancestry** | **High Elf:** Size Medium, Speed 30 ft, Base `AGI d8, INT d8`, Racial Feats: `Low-Light Vision`, `Elven Footwork`. | **Ogre Giant:** Size Large (`+1 Reach Zone`), Speed 35 ft, Base `MIG d10, CON d8`, Racial Feats: `Giant Reach`, `Thick Hide (Soak +1 step)`. |
| **2. Class Levels** | **Expert Warrior (`Level 6 - Tier 2`)** | **Expert Brute (`Level 6 - Tier 2`)** |
| **3. Skills (Domains)** | **Combat Mastery:** `Mastered (+2B)` (`4d8 keep highest`).<br>**Subterfuge:** `Trained (+1B)` (`3d8`). | **Combat Mastery:** `Mastered (+2B)` (`4d10 keep highest`).<br>**Athletics:** `Trained (+1B)` (`3d10`). |
| **4. Feats & Maneuvers** | `Sudden Charge [2A]`, `Defensive Stance`, `Riposte [SET]`, `Weapon Master (Swords - Up-Shift d8->d10)`. | `Power Strike [1A]`, `Cleaving Momentum [0A]`, `Impale [SET]`, `Weapon Master (Greatclub - Up-Shift d10->d12)`. |

*Note: For detailed progression across the 20 levels and 4 Tiers of Play, see `03_core_baseline_system/06_leveling_and_tier_progression.md`.*
