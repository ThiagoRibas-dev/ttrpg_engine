# Pathfinder 2e & General Content Conversion Guidelines

Pathfinder 2e (PF2e) revolutionized modern tactical TTRPGs through its structured **3-Action Economy** and its comprehensive **Keyword / Trait Taxonomy**. While PF2e still uses numerical modifiers (`+2 Circumstance`, `-1 Status`, `Proficiency Level + 2`), its structural architecture ports directly into our mathless engine with near-zero friction.

This document establishes the exact conversion guidelines for PF2e traits, 3-action feats, and general OSR / board game content.

---

## 1. Translating PF2e Weapon & Action Traits (`Keyword Mapping`)

In PF2e, every weapon, spell, and ability carries modular tags that dictate how it interacts with the rules (`[Agile]`, `[Reach]`, `[Forceful]`). We translate these keywords directly into **Mathless Step and Pool Interactions**:

| PF2e Trait / Keyword | Traditional PF2e Rule | Converted Mathless Mechanical Effect |
| :--- | :--- | :--- |
| **`[Agile]`** | `-4` MAP penalty instead of `-5` on second attacks. | **Stamina Efficiency:** When making a second Strike (`[1A]`) on the same turn, you can spend **1 Stamina** to ignore the `+1 Bane` multi-attack penalty entirely, rolling a full `2dX keep highest` pool. |
| **`[Finesse]`** | Use Dexterity modifier instead of Strength for attack rolls. | **Agility Substitution:** You can roll your **Agility Pool (`2dAGI`)** instead of Might (`2dMIG`) when making melee attack checks. |
| **`[Forceful]`** | Gain circumstance bonus to damage (`+2 / +4`) on subsequent attacks on the same turn. | **Momentum Step:** When you hit with a second or third attack on the same turn, the weapon's **Damage Die is stepped up one rank (`d6` $\to$ `d8` $\to$ `d10`)** against the target's Soak Rank. |
| **`[Reach]`** | Weapon can attack targets 10 feet away (`2 squares`). | **Zone Reach:** You can make melee Strikes against targets in adjacent tactical sub-zones (`up to 10-15 ft`) without needing to spend `[1A]` to Stride closer. |
| **`[Sweep]`** | Gain `+1` circumstance bonus on attacks against a different target than your last attack. | **Multi-Target Advantage:** When you Strike a different target than your previous action on the same turn, you gain **$+1\text{ Boon Die (`3dX keep highest`)}$**. |
| **`[Deadly d8/d10]`** | On a critical hit, add an extra `1d8` or `1d10` damage roll. | **Critical Severance:** When your attack achieves a **Critical Success (`Rolled Max Face or Multi-Beat`)**, your weapon automatically bypasses the target's Soak Rank entirely AND inflicts **2 Wound Conditions (`Severed Tendon or Fractured Rib`)**. |
| **`[Fatal d10/d12]`** | On a critical hit, the weapon's damage die size increases to `d10` or `d12` and rolls extra dice. | **Lethal Overdrive:** On a Critical Success, your weapon’s damage die steps up to `d12` (`Damage Die d12 vs Soak`), guaranteeing maximum structural trauma (`Mortal Wound Check triggered if Vitality < 8`). |
| **`[Parry]`** | Can spend an action to raise defense (`+1 AC`). | **Defensive Guard:** When wielding this weapon, you can declare `Raise Guard (`[1A]`)` to roll your **Parry Pool (`2dParry`)** against incoming strikes, even if you are not wielding a shield. |

---

## 2. Converting PF2e Class Feats & Action Abilities

Let's convert three signature PF2e tactical class feats into our mathless action budget (`[1A]`, `[2A]`, `[3A]`, `[R]`):

### Case Study 1: Sudden Charge (Barbarian / Fighter Feat)
- **PF2e Original Rule:** `[2 Actions]` *You Stride twice. If you end your movement within melee reach of at least one enemy, you can make a melee Strike against that enemy.*
- **Mathless Converted Rule (`Sudden Charge - Combat Maneuver`):**
  - **Action Cost:** `[2A] Activity`
  - **Mathless Mechanic:** You Stride (`Move up to 2 Combat Zones / 60 ft`) in a straight line toward an enemy. Upon stopping within reach, you immediately make a melee Strike (`[0A] free`) against them. Due to the built-up kinetic velocity, **your attack pool gains $+1\text{ Boon Die (`3dX keep highest`)}$** AND your **Damage Die is stepped up one rank (`d8` $\to$ `d10`)** vs their Soak Rank.

### Case Study 2: Flurry of Blows (Monk Class Feature)
- **PF2e Original Rule:** `[1 Action]` *Make two unarmed Strikes. If both hit the same monster, combine their damage.*
- **Mathless Converted Rule (`Flurry of Blows - Monk Talent`):**
  - **Action Cost:** `[1A] Activity (`Cost: 1 Stamina`)`
  - **Mathless Mechanic:** You unleash a rapid volley of martial strikes. Make two separate unarmed Strikes against a target within reach. **Neither attack suffers the multi-attack Bane penalty (`Both roll base `2dAGI` or `2dMIG` keep highest`)**. If both attacks hit, the target’s **Soak Rank is stepped down one rank (`Soak d8` $\to$ `Soak d6`)** against the second hit due to cumulative physical shock.

### Case Study 3: Shield Block (General Reaction Feat)
- **PF2e Original Rule:** `[Reaction]` *Trigger: While you have your shield raised, you take physical damage. You snap your shield in place to deflect a blow. Your shield prevents damage equal to your shield’s Hardness. You and the shield each take any remaining damage.*
- **Mathless Converted Rule (`Active Shield Block - Defense Reaction`):**
  - **Action Cost:** `[1R] Reaction (`Trigger: An attack beats your Evasion/Parry`)`
  - **Mathless Mechanic:** You interpose your raised shield to absorb the kinetic brunt of the blow. You make an immediate **Soak Check using your Shield's Die (`d8` or `d10`) instead of your armor**. If the attack still beats your Shield Die, you can declare a **Heroic Item Sacrifice**, absorbing 100% of the remaining impact by splintering **1 Durability Slot** off your shield (`0 HP lost, 0 Wounds`).

---

## 3. General OSR / d20 & Board Game Porting Guidelines

Our mathless engine is designed to act as a **Universal Translation Layer** for tabletop content. When porting content from Old School Renaissance (OSR) adventures, *Gloomhaven*, or *Lands of Evershade*, apply these simple heuristics:

### 3.1 OSR Adventures (`OSRIC, B/X, Old-School Essentials`)
- **Target DCs & Saving Throws:** Convert old-school target numbers (`Save vs Poison 14`, `Open Doors 1-2 on d6`) into mathless DCs:
  - Easy/Routine task = `DC 3 to 5`
  - Standard/Challenging task = `DC 6 to 7`
  - Hard/Severe task = `DC 8 to 9`
- **Lethality & Traps:** OSR traps (`Pit Trap - 2d6 damage`) directly test vs **Evasion (`2dAGI vs DC 7`)**. If failed, the fall inflicts a `Sprained Joint` or `Fractured Rib` Wound Condition plus `d8 Damage vs Soak`.

### 3.2 Board Game Card Abilities (`Gloomhaven / Lands of Evershade`)
- When adapting a tactical card ability (`e.g., Gloomhaven: Attack 4, Range 3, Pull 2`), convert the card into a **Mathless Action Option (`[1A]` or `[2A]`)** with a concrete Stamina cost:
  - *Converted Ability:* `[2A] Grappling Harpoon (`Cost: 1 Stamina`)`. Make a ranged Strike (`3 Zones`). If hit (`Damage Die d8 vs Soak`), you immediately pull the target **1 Combat Zone closer to you** without an opposed check.
