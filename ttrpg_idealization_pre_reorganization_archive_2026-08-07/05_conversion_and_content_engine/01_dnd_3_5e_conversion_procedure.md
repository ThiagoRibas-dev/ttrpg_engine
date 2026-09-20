# D&D 3.5e Conversion Procedure & Translation Pipeline

Dungeons & Dragons 3.5e is our primary architectural anchor due to its unmatched library of character options, feats, prestige classes, and monster ecologies. However, 3.5e relies on heavy linear arithmetic (`+X / -X` modifiers). 

This document provides exact, step-by-step conversion formulas to translate any 3.5e mechanical element into our **Mathless Step Pool Engine (`2dX keep highest`)** while preserving its tactical identity and simulationist flavor.

---

## 1. The Master Conversion Pipeline

To convert any 3.5e rule, identify its numerical vector and map it directly onto one of our five mathless mechanical vectors:

```
[ 3.5e Numerical / Arithmetic Rule ]
                 │
                 ▼
     [ What vector is modified? ]
                 │
   ┌─────────────┼─────────────┬─────────────┐
   ▼             ▼             ▼             ▼
[Flat +Bonus] [Feat/Maneuver] [Spell DC/Mod] [Monster Stat]
   │             │             │             │
   ▼             ▼             ▼             ▼
Pool Boon     Step Shift /  Resilience   Step Die &
(`+1d/2d`)    Action Cost   Opposed Pool  Soak Rank
```

### 1.1 Numerical Translation Matrix

| 3.5e Numerical Concept | Mathless Equivalent / Translation Rule | Why This Works Without Math |
| :--- | :--- | :--- |
| **`+1 to +2` Attack / Skill Bonus**<br>*(e.g., Weapon Focus, Skill Focus)* | **$+1\text{ Boon Die (`+1B`)}$** added to the pool (`3dX keep highest`). | Adds reliability and higher average face rolls without raising the mathematical DC threshold. |
| **`+3 to +5` Attack / Skill Bonus**<br>*(e.g., Greater Weapon Focus, Synergy)* | **$+2\text{ Boon Dice (`+2B`)}$** added to the pool (`4dX keep highest`). | Extremely consistent performance; virtually eliminates low whiffs (`rolling below 5`). |
| **`-1 to -2` Attack / Skill Penalty** | **$+1\text{ Bane Die (`+1X`)}$** (`1dX` face roll). | Removes redundancy; forces the character to rely on raw unassisted die size. |
| **`-4 or greater` Severe Penalty** | **$+2\text{ Bane Dice (`+2X`)}$** (`2dX keep lowest` / Disadvantage). | Represents severe impairment or attacking through heavy cover/blindness. |
| **Permanent Attribute Increase**<br>*(e.g., +2 Strength from leveling/belt)* | **Step Up Die Size (`Up-Shift`)** of that Attribute (`d6` $\to$ `d8`). | Raises the absolute capability ceiling, allowing the character to hit higher natural DCs. |
| **Damage Bonus (`+2 to +6 Damage`)**<br>*(e.g., Weapon Specialization, High Str)* | **Step Up Weapon Damage Die (`d6` $\to$ `d8` $\to$ `d10`).** | Higher die face easily overcomes heavier armor **Soak Ranks** without arithmetic addition. |
| **Armor Class Bonus (`+1 to +4 AC`)**<br>*(e.g., Dodge feat, Ring of Protection)* | **Step Up Evasion or Parry Die (`d8` $\to$ `d10`) OR add $+1\text{ Boon Die}$ when making defensive checks.** | Directly elevates the number the attacker must beat on an opposed check. |
| **Damage Reduction (`DR 5/magic`)** | **Soak Step Upgrade (`+1 Soak Step`) OR Immunity to `d6/d8` weapons without critical hits.** | Kinetic force below the threshold is cleanly absorbed (`0 Wounds`). |

---

## 2. Feat Conversion Case Studies (`Before & After`)

Let's apply our conversion formulas to five iconic D&D 3.5e combat feats to demonstrate how mathematical chains become clean, mathless tactical choices:

### Case Study 1: Power Attack
- **3.5e Original Text:** *On your action, before making attack rolls for a round, you may choose to subtract a number from all melee attack rolls and add the same number to all melee damage rolls. This number may not exceed your base attack bonus.*
- **Mathless Converted Rule (`Power Strike - Combat Feat`):**
  - **Action Cost:** `[1A] Strike (Modified)`
  - **Mathless Mechanic:** Before rolling a melee Strike with a two-handed or heavy weapon, you can declare a **Power Strike**. You take **$+1\text{ Bane Die (`1dMIG`)}$** on your attack roll. If the attack hits, your weapon's **Damage Die is stepped up two ranks (`d8` $\to$ `d12`)** against the target's Soak Rank, and any hit is automatically treated as beating Soak by $\geq 1$ step (`Guaranteeing at least 1 Wound Condition`).

### Case Study 2: Cleave & Great Cleave
- **3.5e Original Text:** *If you deal a creature enough damage to make it drop (typically by dropping it to below 0 hit points or killing it), you get an immediate, extra melee attack against another creature within reach.*
- **Mathless Converted Rule (`Cleaving Momentum - Combat Feat`):**
  - **Action Cost:** `[0A] Free Trigger`
  - **Mathless Mechanic:** Whenever your melee Strike inflicts a **Severe Lethal Wound** OR drops an enemy's Vitality to `0`, your weapon's momentum carries through. You immediately make one free melee Strike against an adjacent enemy within your reach. **Great Cleave:** If that secondary hit also drops a target, the cleave continues to a third target without spending action points.

### Case Study 3: Combat Expertise
- **3.5e Original Text:** *When you use the attack action or full attack action in melee, you can take a penalty of up to -5 on your attack roll and add the same number (+5 or less) as a dodge bonus to your Armor Class.*
- **Mathless Converted Rule (`Defensive Blade Stance - Combat Feat`):**
  - **Action Cost:** `[1A] Stance / Active Defense`
  - **Mathless Mechanic:** You adopt a defensive fencing stance. Until your next turn, all of your offensive melee Strikes roll with **$+1\text{ Bane Die (`1dX`)}$**, but whenever an enemy attacks your Evasion or Parry, **you roll your Parry Pool (`2dParry`) with $+2\text{ Boon Dice (`4dParry keep highest`)}$**, making your guard nearly impenetrable.

### Case Study 4: Dodge & Mobility
- **3.5e Original Text:** *During your action, you designate an opponent and receive a +1 dodge bonus to Armor Class against attacks from that opponent. Mobility adds a +4 dodge bonus to Armor Class against attacks of opportunity caused when you move out of or within a threatened area.*
- **Mathless Converted Rule (`Skirmisher's Footwork - Combat Feat`):**
  - **Action Cost:** `[0A] Passive Feature`
  - **Mathless Mechanic:** Your agility in close quarters is legendary. Whenever you take a `Stride (`[1A]`)` action through an enemy's reach, any **Attacks of Opportunity (`[R]`)** made against you suffer **$+2\text{ Bane Dice (`2dX keep lowest` / Disadvantage)}$**. Furthermore, if an enemy misses you with an Attack of Opportunity, you gain $+1\text{ Boon Die}$ on your next check against them.

### Case Study 5: Weapon Focus & Weapon Specialization
- **3.5e Original Text:** *Choose one type of weapon. You gain a +1 bonus on all attack rolls you make using the selected weapon. Specialization adds +2 bonus on all damage rolls.*
- **Mathless Converted Rule (`Weapon Master - Path Talent`):**
  - **Action Cost:** `[0A] Passive Mastery`
  - **Mathless Mechanic:** Choose a weapon category (`Longswords`, `Bows`). When attacking with this weapon, you automatically gain **$+1\text{ Boon Die (`+1B`)}$** to your attack pool (`3dX keep highest`). Furthermore, your mastery allows you to strike structural weak points: your weapon's **Damage Die is permanently stepped up one rank (`d8` $\to$ `d10`)** against enemy Soak Ranks.

---

## 3. Spell & Magic Conversion Case Studies (`Before & After`)

In 3.5e, spellcasters calculate exact spell DCs (`DC = 10 + Spell Level + Attribute Modifier`) and roll large handfuls of damage dice (`10d6 Fireball`). We convert spells into **Mathless Opposed Checks** and **Concrete Area Conditions**.

### Case Study 1: Fireball (3rd-Level Arcane Spell)
- **3.5e Original Text:** *A fireball spell generates a searing explosion of flame that detonates with a low roar and deals 1d6 points of fire damage per caster level (maximum 10d6) to every creature within the area. A Reflex save halves the damage.*
- **Mathless Converted Rule (`Searing Fireball - Arcane Spell`):**
  - **Action Cost:** `[2A] Cast Spell (`2 Focus cost`)`
  - **Range & Area:** Long Range (`3 Zones / 120 ft`); `1 Combat Zone Radius`.
  - **Mathless Mechanic:** You unleash a detonation of searing flame across the target zone. You make an **Arcane Power Check (`2dINT keep highest`)** opposed separately by the **Evasion Pool (`2dAGI`)** of every creature in the zone.
    - **Critically Failed Evasion (Or Rolled `1`):** The target takes **Searing Lethal Fire (`Damage Die d12 vs Soak`)** AND catches **On Fire (`Severe Burn Wound Condition` - lose 2 Vitality per turn until doused)**.
    - **Failed Evasion (`Power > Evasion`):** The target takes **Fire Damage (`Damage Die d10 vs Soak`)** AND loses `2 Stamina` from heat shock.
    - **Successful Evasion (`Evasion >= Power`):** The target dives for cover, absorbing the blast. They take zero Wounds (`0 HP lost`), but lose `1 Stamina` from the physical exertion of dodging.

### Case Study 2: Stinking Cloud (3rd-Level Conjuration Spell)
- **3.5e Original Text:** *Stinking cloud creates a bank of fog like that created by fog cloud, except that the vapors are nauseating. Living creatures in the cloud become nauseated (unable to attack, cast spells, or concentrate; can only take a single move action per turn) as long as they remain in the cloud and for 1d4+1 rounds after.*
- **Mathless Converted Rule (`Nauseating Fog - Conjuration Spell`):**
  - **Action Cost:** `[2A] Cast Spell (`2 Focus cost`)`
  - **Range & Area:** Medium Range (`2 Zones`); `1 Zone Radius Clock (`Sustained via 1 Focus/round`)`.
  - **Mathless Mechanic:** A dense, putrid yellow fog fills the zone, obscuring sight (`All targets Blinded`). Every living creature starting their turn inside the cloud must make an opposed **Resilience Check (`2dMIG keep highest vs your 2dINT Power Pool`)**:
    - **Failed Resilience:** The target is overcome by violent retching (`Muddled Condition`). They immediately lose `2 Stamina` and **can only spend `[1A]` total on their turn** (`Cannot Strike or Cast Spells`). This condition persists for **2 rounds after exiting the fog**.
    - **Successful Resilience:** The target holds their breath and resists the nausea (`0 Conditions`), but still suffers the visual blinding of the fog while inside.

---

## 4. Monster & Bestiary Conversion Pipeline

To convert a 3.5e monster block into our mathless engine in under 2 minutes, apply this structured mapping blueprint:

```
[ 3.5e Monster Profile (`Hit Dice, Armor Class, Attacks, Saves`) ]
                                 │
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
[ Attribute Steps ]     [ Defense & Soak Ranks ]   [ Attack & Damage Pools ]
3.5e Stat `10-13` -> `d6`  Armor Class -> Evasion/Parry  Attack Bonus -> Pool Boons
3.5e Stat `14-17` -> `d8`  Natural Armor -> Soak Step  Damage -> Step Die
3.5e Stat `18-21` -> `d10` Spell Resistance -> Will      (`2d6` -> `d8 Strike`)
3.5e Stat `22+`   -> `d12` DR -> Soak `d10-d12`
```

### Case Study: Converting the Classic 3.5e Ogre
- **3.5e Base Stats:** Large Giant (`HD 4d8+12, HP 29`), `AC 16` (`-1 Size, +1 Dex, +5 Natural, +1 Hide`), `Attack: Greatclub +8 melee (2d8+7)`, `Fort +6, Ref +2, Will +1`, `Str 21 (+5), Dex 12 (+1), Con 15 (+2), Int 6 (-2), Wis 10 (0), Cha 7 (-2)`.

#### Converted Mathless Profile: `Ogre Brute (Threat Level: Formidable)`
- **Core Attribute Steps:**
  - `MIG d10` *(Heroic giant muscle)* | `AGI d6` *(Standard speed)*
  - `INT d4` *(Impaired logic)* | `WIL d6` *(Standard morale)*
- **Defense & Soak Ranks:**
  - **Evasion Pool:** `2d6` *(Average dodge due to large frame)*
  - **Parry Pool:** `2d8` *(Heavy club parry)*
  - **Soak Rank:** **`Soak d10`** *(Thick giant hide + leather apron. Impervious to basic `d6` daggers without critical hits).*
  - **Resilience Pool:** `2d10 keep highest` *(Massive metabolic fortitude against poisons/stun).*
- **In-World Resource Pools:**
  - **Vitality (`HP`):** `16 Vitality` *(MIG d10 + WIL d6)*
  - **Stamina Pool:** `20 Stamina` *(Can Die Step-Up checks 4 times before tiring)*
- **Mathless Attack Actions (`[1A]`):**
  - **Crushing Greatclub (`[1A] Melee Strike`):** Roll `Combat Pool (`2d10 + 1 Boon = 3d10 keep highest`) vs Target Evasion or Parry`.
    - *Impact vs Soak:* If hit, deals **`Damage Die d12 vs Soak Rank`**. On a critical hit (`rolling 12`), the blow knocks the target **Prone** and inflicts a `Fractured Rib` Wound Condition.
  - **Sweeping Cleave (`[2A] Area Surge`):** The Ogre swings its massive club in a wide arc across the zone. Make a single `3d10` check opposed by the **Evasion Pool (`2dAGI`)** of up to 3 adjacent targets simultaneously. All who fail take `d10 Damage vs Soak` and are pushed back 10 feet.
