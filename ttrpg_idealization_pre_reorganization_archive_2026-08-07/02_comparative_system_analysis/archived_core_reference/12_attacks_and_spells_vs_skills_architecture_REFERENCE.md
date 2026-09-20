# Attacks & Spellcasting: Skill-Unified vs. Class-Split Architecture

To finalize our baseline resolution rules across our **Model A Check Engine (`Attribute = Die Size X | Competency Rank = Pool Volume N and Floor F — DEC-038`)**, we must decide whether physical attacks (`Blades, Bows, Brawling`) and spellcasting (`Arcane/Divine checks`) exist inside our **5 Action Mastery Domains (`as specific skills`)** or separate **Class Advancement Tracks (`like D&D 3.5e BAB and Caster Level`)**.

This document evaluates three architectural models, analyzes their interaction with class identity and our four paired defenses, and establishes our definitive baseline.

---

## 1. Candidate Architectural Models (`Pros & Cons`)

### 1.1 Option 1: The Skill-Unified Engine (`Attacks & Spells ARE Specific Skills`)
- **Structure (The *Mythras / BRP / Year Zero* approach):** There is no separate `Base Attack Bonus (BAB)` or `Caster Level check pool` track on the class table. Instead, **Combat Mastery** (`Blades, Axes, Bows, Shields`) and **Lore & Arcana** (`Arcana, Divine, Primal traditions`) are specific skills listed under our 5 Action Mastery Domain umbrellas (`DEC-030`). When a character levels up and spends general **Skill Allocations (`Track 5`)**, they can invest directly in *Longswords*, *Pyromancy*, *Stealth*, or *Diplomacy*.
- **🟢 Major Pros:**
  - **100% Universal Check Rule:** Zero mechanical distinction between swinging a sword, picking a lock, negotiating a treaty, or casting a fireball! Every single check is: `Attribute Die Size (X) + Skill Competency Volume & Floor (N & F)`.
  - **Total Player Freedom:** A player can build a battle-mage who invests equally in *Longswords* and *Arcana*, or a noble knight who invests in *Polearms* and *Diplomacy*, without being forced into linear class BAB jackets.
- **🔴 Major Cons:**
  - **The "Skill Allocation Tax" Dilemma:** If a Fighter only receives 1 skill allocation every 2 levels (`Bad/Combat track progression — DEC-035 Track 5`), but *must* spend those allocations just to raise his sword skill from `Trained -> Expert -> Master` to keep up with enemy Parry/Reflex defenses, then the Fighter has **zero skill allocations left over to invest in Athletics, Survival, or Perception!** His entire skill budget becomes a mandatory weapon skill tax.

---

### 1.2 Option 2: The D&D / Pathfinder Split Engine (`Attacks & Spells are Dedicated Class Tracks Apart from Skills`)
- **Structure (The *D&D 3.5e / PF2e* approach):** Your ability to hit with a weapon (`Base Attack Bonus / Combat Pool`) and your ability to land a spell (`Caster Level / Spell Power Pool`) exist on **dedicated Class Advancement Tracks (`DEC-035 Track 2 & Track 4`)**, completely separate from your general **Skill Competency Allocations (`Track 5: Stealth, Lockpicking, Arcana Lore, Diplomacy`)**.
- **🟢 Major Pros:**
  - **No Skill Tax (`Protects General Competence`):** Fighters and Wizards don't have to sacrifice their skill allocations just to buy basic attack or spell proficiency. A Fighter automatically hits hard with his weapons (`reaching Expert Floor 5 at Lvl 5, Master Floor 7 at Lvl 9`) via his class track (`DEC-029`), allowing him to spend his 9 to 14 General Skill Allocations on becoming a master mountaineer (`Athletics`), a wilderness scout (`Survival`), or a military commander (`Leadership`).
  - **Immediate 3.5e Familiarity:** Preserves the exact structural separation of `HP, BAB, Saves, CL, and Skills` that our 20-Level Class Advancement Matrix (`DEC-035`) is built upon.
- **🔴 Major Cons:**
  - **Mechanical Bifurcation:** Creates two parallel mechanisms for how pools and floors advance (`one automatic by class level for attacks/spells, one purchased via skill allocations for out-of-combat skills`).

---

### 1.3 Option 3: The Hybrid "Class-Granted Domain Allocations" Engine (`Recommended Baseline`)
To combine the elegant universality of Option 1 (`Attacks and Spells ARE specific skills under our 5 domains`) with the zero-skill-tax protection of Option 2 (`distinct class identity and automatic core role mastery`), we establish **Option 3: The Hybrid Class-Granted Allocations Engine**:

```
[ Universal Skill Ecosystem: How Competency Ranks Advance ]
  ├── 1. Class-Granted Primary Allocations (`Automatic Role Mastery — Zero Tax`)
  │     └── At Levels 1, 5, 9, and 15 (`Tier Boundaries`), your Class automatically elevates ONE primary class skill (`e.g., Longswords for Fighter; Pyromancy for Wizard`) to the next Competency Rank (`Trained -> Expert Floor 5 -> Master Floor 7 -> Legend Floor 9`).
  │
  └── 2. General Skill Allocations (`Track 5 — Universal Out-of-Combat Customization`)
        └── At Levels 1, 2, 4, 6, 7, 10, 12, 14, 17, 18, you receive general skill allocations to invest freely in ANY specific skill (`Stealth, Lockpicking, Diplomacy, Medicine, Athletics, OR even a second weapon/spell style like Bows or Necromancy`)!
```

- **Why Option 3 is the Ultimate High Fantasy Standard:**
  - **100% Universal Rule (`Option 1 Benefit`):** Everything on the sheet (`Swords, Spells, Diplomacy, Stealth`) uses the exact same **5 Competency Ranks (`Untrained 0 -> Trained 3 -> Expert Floor 5 -> Master Floor 7 -> Legend Floor 9`)** and exact same **Model A check pool engine (`Die Size X from Attribute, Pool Volume N and Floor F from Competency Rank — DEC-038`)**!
  - **Zero Skill Tax (`Option 2 Benefit`):** Because Classes award dedicated primary skill rank upgrades at Tier boundaries (`Levels 1, 5, 9, 15`), Fighters and Wizards automatically hit their required `Expert, Master, and Legend` attack/spell floors in their core vocation (`no skill allocation tax!`), while retaining their full budget of General Skill Allocations to customize their out-of-combat identities!

---

## 2. How Option 3 Interacts with Classes (`Does Class Dictate Ability to Hit?`)

Under Option 3, **Class dictates your baseline automatic mastery and what specific skills you can elevate for free, while your total capability ceiling (`Die Size X`) remains bound to your Attributes**:

| Class Archetype | Class-Granted Primary Skill (`Automatic Growth at Lvl 1, 5, 9, 15`) | General Skill Allocations (`Track 5 — Free Allocation Budget`) | What Happens When Attacking vs. Spellcasting at Level 10 (`Master Tier`) |
| :--- | :--- | :--- | :--- |
| **Fighter (`Martial Anchor`)** | **1 Primary Weapon Skill (`e.g., Heavy Blades / Greatswords`)** under `Combat Mastery`. Reaches **`Master Rank (4d12 keep highest, Floor 7)`** at Lvl 9 automatically (`STR d12`). | **9 Total Allocations (`Bad Track`)** across 1-2 domains (`e.g., Athletics, Intimidate, Shields`). | **When Swinging Greatsword:** Rolls **`4d12 keep highest (Floor 7)`**. Automatic Master striker.<br>**When Casting Arcane Spell:** Because he invested 0 points in *Pyromancy*, rolls **Untrained (`2d6, Floor 0`)**. |
| **Rogue (`Skill & Finesse Anchor`)**| **1 Primary Finesse/Subterfuge Skill (`e.g., Finesse Blades OR Stealth`)**. Reaches **`Master Rank (4d10, Floor 7)`** at Lvl 9 (`DEX d10`). | **16 Total Allocations (`Good Track`)** across 3-4 domains (`e.g., Stealth, Lockpicking, Acrobatics, Deception, Bows`). | **When Swinging Finesse Blade:** Rolls **`4d10 keep highest (Floor 7)`** (`or 5d10 on Sneak Attack +1B`). Matches Fighter precision!<br>**When Picking Lock:** Rolls **`Master Rank (4d10, Floor 7)`**, surgically reliable. |
| **Wizard (`Arcane Caster Anchor`)** | **1 Primary Magic Tradition (`e.g., Arcana / Pyromancy`)** under `Lore & Arcana`. Reaches **`Master Rank (4d12 keep highest, Floor 7)`** at Lvl 9 automatically (`INT d12`). | **13 Total Allocations (`Okay Track`)** across 2 domains (`e.g., History, Arcana Lore, Medicine, Diplomacy`). | **When Casting *Fireball*:** Rolls **`4d12 keep highest (Floor 7)`** (`or 5d12 on Focus Step-Up`). Automatic Master spellcaster.<br>**When Swinging Greatsword:** Rolls **Untrained (`2d6, Floor 0`)**, completely outclassed by Fighter. |

---

## 3. How the Math Works Against Defenses (`Opposed Combat & Magic Math`)

With Option 3 locked in, combat and spellcasting checks against our four defenses operate with complete mathematical symmetry across both modes (`Opposed Contests Mode 2/3` and `Fixed DCs Mode 1/3`):

### 3.1 Melee Strikes vs. Parry (`Active Martial Clash`)
- **Attacker Pool:** `Weapon Specific Skill Pool` (`e.g., Master Fighter rolls 4d12 keep highest, Floor 7`).
- **Defender Pool:** `Weapon/Shield Specific Skill Pool` (`e.g., Veteran Knight rolls 3d10 keep highest, Floor 5`).
- **Resolution (`Zero Math`):** Compare Highest Face vs Highest Face (`12 vs 9`). Attacker wins! Extra attacker dice (`say, rolling 8 and 10`) beat the Knight's `9`, awarding **+1 Special Effect Token (`[SET]`)** (`or +2 if Max Face 12`) to execute `Impale`, `Trip`, or `Bypass Soak` (`DEC-034`)!

### 3.2 Ranged Strikes & Area Spells vs. Reflexes (`DEX+INT Dodge Pool`)
- **Attacker Pool:** `Ranged Weapon OR Spell Tradition Pool` (`e.g., Master Wizard rolls Pyromancy 4d12 keep highest, Floor 7`).
- **Defender Pool:** **`Reflexes Paired Defense Pool (`1dDEX + 1dINT keep highest + Good Save Boons`)`** (`DEC-022 — e.g., Rogue rolls DEX d10 + INT d8 + Good Save +2B -> 4d10 keep highest, Floor 5`).
- **Resolution (`Zero Math`):** Compare `Pyromancy Highest Face vs Reflexes Highest Face`. If `Spell > Reflexes`, spell hits! If `Reflexes >= Spell`, target dodges cleanly (`0 Wounds`).

### 3.3 Internal / Metabolic Spells vs. Resilience (`Fortitude STR+CON | Willpower WIS+CHA`)
- **Attacker Pool:** `Spell Tradition Pool` (`e.g., Necromancy 4d12, Floor 7`).
- **Defender Pool:** **`Fortitude Pool (`1dSTR + 1dCON`)`** vs. Poison/Death; OR **`Willpower Pool (`1dWIS + 1dCHA`)`** vs. Mind Blasts/Curses (`DEC-022`).
- **Resolution (`Zero Math`):** Compare `Spell Highest Face vs Resilience Highest Face`. If `Spell > Resilience`, target suffers the internal spell condition (`Dazed, Paralyzed, Charmed`).

### 3.4 Post-Hit Impact vs. Soak Rank (`Armor Die vs Damage Die`)
- When any physical attack or spell blast beats `Reflexes` or `Parry`, it checks **Soak Rank (`Armor Die: d4 Cloth -> d12 Plate — DEC-005`)**:
  $$\text{Impact Check: } \max(\text{Damage Die Face}) \text{ vs } \max(\text{Soak Die Face})$$
- If `Damage <= Soak`: Kinetic shock absorbed (`0 Wounds`).
- If `Damage > Soak`: Target loses normal Vitality (`HP`). Can inflict quick minor disruptions (`Bleed, Off-balance`).
- If **Critical Hit (`d100 Threat Profile OR Called Shot [2 SET] — DEC-034`)**: Double Vitality loss + **Severe Anatomical Wound Condition (`Roll 1d8 Location Matrix`)**!


## Canonical Magic Classification Cross-Reference (`DEC-050`)

Spells use separate axes: the eight technical Schools, modular Traditions for access and specialization, and practical Traits. Alchemy is governed by Knowledge and Craft rather than Magic Mastery. Psychic/Psionic power remains a provisional separate non-Vancian system.


## Unified Spellcasting Cross-Reference (`DEC-051`)

The former separate Spellcasting Profile and Preparation Provenance concepts are superseded. Classes and paths grant Tradition access, acquisition methods, shared slot progression, and class features; they do not own separate spell lists, casting methods, or slot pools. All characters use one universal preparation system and one shared spell-slot pool. Tradition Competency determines spell-rank access and intrinsic spell scaling.
