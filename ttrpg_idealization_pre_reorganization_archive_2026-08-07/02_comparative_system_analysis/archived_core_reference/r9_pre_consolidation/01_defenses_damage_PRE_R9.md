# Simulationist Defense Architecture & Damage Modeling

In our idealized system, resolving an attack does not rely on comparing a single $d20$ roll against an abstract Armor Class number. Instead, combat resolution respects the physical reality of an attack’s trajectory, momentum, and impact across **Four Defensive Layers**.

---

## 1. The Four Defensive Layers

When an incoming attack or threat is declared against an actor, check the layer appropriate to the attack's nature:

```
                      [ Incoming Attack / Threat Declared ]
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
    [ Physical Kinetic Strike ]                 [ Magical / Internal Threat ]
              │                                         │
     ┌────────┴────────┐                       ┌────────┴────────┐
     ▼                 ▼                       ▼                 ▼
[ Reflexes Layer ] [ Parry Layer ]      [ Fort / Will ]   [ Absorption Layer ]
 (DEX+INT Dodge)    (Melee Clash)       (Paired Saving)    (Armor Step Die)
```

### 1.1 Layer 1: Reflexes (`DEX+INT`-Derived Dodge Pool)
- **Used Against:** Ranged weapon projectiles (arrows, bolts, thrown spears), area explosions (`Fireball`, `Alchemical Bomb`), and sweeping environmental hazards.
- **Mechanic:** The attacker rolls their ranged or spell check pool. The defender rolls their **Reflexes Pool (`1dDEX + 1dINT keep highest`)**.
  - If **Attacker Highest $\geq$ Defender Highest**: The projectile/blast lands (`Hit $\to$ Check Damage Absorption`).
  - If **Attacker Highest < Defender Highest**: The defender dodges cleanly (`Miss / 0 Impact`).

### 1.2 Layer 2: Parry (`Combat Mastery` Intercept)
- **Used Against:** Melee weapon strikes (swords, axes, polearms, unarmed brawling).
- **Mechanic:** If the defender has `Raised Guard (`[1A]`)` or spends `1 Stamina (`[1R]`)` to react, they make an opposed **Parry Check** using their `Combat Mastery` pool (`3dX to 5dX`).
  - If **Defender Highest $\geq$ Attacker Highest**: The weapon is deflected or parried cleanly (`0 Impact`). If the defender rolls `2+ Successes` on Parry, they can instantly trigger `Riposte` or `Disarm`.
  - If **Attacker Highest > Defender Highest**: The attack breaks past the parry (`Hit $\to$ Check Damage Absorption`).

### 1.3 Layer 3: Damage Absorption (`Armor & Physical Hide Step — ABS`)
- **Used Against:** Any physical or kinetic attack that beats Reflexes or Parry.
- **Mechanic:** **Damage Absorption is checked post-hit.** Every piece of armor provides an **Absorption Step Die (`ABS`)** (`d4` Cloth $\to$ `d12` Full Plate). Compare **Weapon Damage Die Face vs Absorption Die Face**.

---

## 2. Mathless Damage & Wound Resolution (`Damage vs Absorption`)

In traditional d20 games, damage resolution involves subtracting armor damage reduction (`DR`) from rolled HP (`8 damage - 3 DR = 5 HP lost`). We eliminate subtraction entirely by comparing the **Attacker's Damage Die Face** against the **Defender's Absorption Die Face (`ABS`)**:

$$\text{Impact Check: } \max(\text{Weapon Damage Die Faces}) \text{ vs } \max(\text{Absorption Die Faces})$$

### 2.1 The Mathless Damage & Wound Matrix (`DEC-034 & DEC-044`)

| Damage Die vs Absorption Die (`ABS`) | Physical Outcome (`Vitality vs Wounds`) |
| :--- | :--- |
| **Damage Face < Absorption Face** | **Absorbed (`0 Wounds`):** The armor or thick hide absorbs the kinetic impact. The defender loses **1 Stamina** due to jarring vibration, but suffers zero physical tissue damage (`No HP loss`). |
| **Damage Face == Absorption Face** | **Superficial Impact (`Minor Shock`):** The blow bruises tissue through the armor. The defender loses **2 Stamina** (or 2 Vitality if Stamina is 0), but takes zero anatomical wounds. |
| **Damage Face > Absorption Face**<br>*(Normal Non-Crit Hit)* | **Standard Hit (`Vitality Loss & Quick Disruption`):** The strike bludgeons through armor. The defender loses **Vitality (`HP`) equal to the Damage Die face shown**. If the attack generated `2+ Successes` (`Multi-Beat`), can inflict a quick disruption (`Trip, Disarm, Shaken`). *Does not inflict anatomical severe wounds.* |
| **Natural Critical Hit (`d100 Check`)** | **Natural Critical (`Double Vitality + Random 1d8 Matrix`):** The strike penetrates deep into random vital anatomy. The defender loses **Double Vitality (`Max Damage Face x 2`)** AND immediately rolls `1d8` on our Anatomical Matrix below! |
| **Called Shot Maneuver (`Chosen Target`)**| **Called Shot (`Standard Vitality + Chosen Anatomical Wound`):** Executed via `3+ Successes` (`or +1 Bane trade-off`). **Does NOT deal double damage (`deals normal shown/rolled Damage Face vs Absorption`)**, BUT the attacker **CHOOSES the exact anatomical body part targeted (`Head, Chest, Arm, Leg`) and triggers that location's severe Anatomical Wound Condition (`Concussion, Dropped Weapon, Prone`)!** |

---

## 3. Armor Taxonomy & Absorption Step Table

Different armor categories provide distinct trade-offs between physical **Absorption Step Ranks (`ABS`)**, **Reflexes Banes** (due to bulk and weight), and **Durability Slots**.

| Armor Category | Absorption Step Die (`ABS`) | Reflexes / Agility Modifier | Durability Slots | Tactical Role |
| :--- | :---: | :---: | :---: | :--- |
| **Unarmored / Clothing** | `ABS d4` | **Normal (`0 Banes`)** | `0` | High mobility, spellcaster baseline. |
| **Light Armor (Leather/Hide)** | `ABS d6` | **Normal (`0 Banes`)** | `1` | Skirmishers, rogues, rangers (`ABS d6`). |
| **Medium Armor (Chain/Scale)** | `ABS d8` | **$+1\text{ Reflexes Bane Die (`-1 die volume`)}$** | `2` | Balanced infantry, warriors (`ABS d8`). |
| **Heavy Plate Armor** | `ABS d10` | **$+2\text{ Reflexes Bane Dice (`Keep lowest`)}$** | `3` | Frontline juggernauts; almost immune to `d6` weapons without crits (`ABS d10`). |
| **Adamantine / Mythic Plate**| `ABS d12` | **$+2\text{ Reflexes Bane Dice (`Keep lowest`)}$** | `4` | Legendary defensive bastion (`ABS d12`). |

---

## 4. Layer 4: Resilience (`Fortitude & Willpower Paired Pools`)

When targeted by non-kinetic or internal threats (poisons, disease, mind blasts, petrification, divine curses), physical Reflexes and armor Absorption are irrelevant (`ABS = 0 vs Mind Blast`).

- **Opposed Resilience Check:** The caster or hazard rolls its **Power Pool (`3dX to 5dX`)** against the defender's appropriate Resilience pool:
  - **Physical Threats (`Poisons, Disease, Petrification`):** Defender rolls their **Fortitude Pool (`1dSTR + 1dCON keep highest + Class Boons`)**.
  - **Mental & Spiritual Threats (`Mind Control, Fear, Curses`):** Defender rolls their **Willpower Pool (`1dWIS + 1dCHA keep highest + Class Boons`)**.
- **Outcome:**
  - **Resilience $\geq$ Power:** The defender shrugs off the effect (`0 Conditions`).
  - **Resilience < Power:** The effect takes hold (`Poisoned`, `Charmed`, `Paralyzed`).
  - **Critical Failure on Resilience:** The effect's duration doubles or escalates to a lethal stage (`Petrified`, `Dying`).

---

## 5. Hit Location & Anatomical Wound Severance (`The 1d8 Anatomical Matrix`)

When an attack achieves a **Natural Critical Hit (`via d100 matching Crit Profile %`)**, roll **`1d8` randomly** on our Anatomical Matrix below. When executing a **Called Shot maneuver (`DEC-044`)**, do not roll randomly; instead, the attacker **CHOOSES the exact body part targeted** and applies its condition!

### 5.1 The Anatomical Location Die (`1d8`) & Called Shot Targets

| Die Face (`1d8`) | Hit Location | Piecemeal Armor Absorption | Severe Anatomical Wound Condition (`Crits & Called Shots`) |
| :---: | :--- | :---: | :--- |
| **`1`** | **Head / Skull** | Helm / Coif ABS | **Concussion / Dazed:** Target suffers an immediate mental **Die Step-Down (`INT/WIS/CHA step down d10` $\to$ `d8`)** and drops all active spell concentration (`0 Focus actions allowed for 1 round`). |
| **`2-3`** | **Chest / Thorax** | Breastplate ABS | **Winded / Bruised Rib:** Target loses **3 Stamina** instantly (`Breath knocked out`). If Natural Crit, ribs fracture (`Take 2 Vitality loss every time you spend Stamina`). |
| **`4`** | **Abdomen / Gut** | Belt / Faulds ABS | **Internal Trauma / Bleed:** Target takes **$+1\text{ Bane Die (`-1 die volume`)}$** on physical checks due to gut agony and gains **Bleeding Cut** (`1 Vitality loss/round`). |
| **`5`** | **Shield / Off-Arm** | Bracer / Shield ABS | **Limp Shield Arm:** If holding a shield or secondary item, **drop it immediately into an adjacent Close zone**. You cannot wield two-handed weapons or Raise Guard until sutured. |
| **`6`** | **Weapon / Primary Arm**| Bracer / Gauntlet ABS | **Limp Weapon Arm:** **Drop your primary weapon instantly.** You suffer **$+2\text{ Bane Dice (`Keep lowest`)}$** on all attacks made with your off-hand until treated. |
| **`7-8`** | **Legs / Feet** | Greaves / Boots ABS | **Buckled Knee / Prone:** Target falls **Prone immediately (`Speed 0 until standing up via [1A]`)**. If Natural Crit, hamstring severed (`Speed permanently halved until surgery`). |

### 5.2 Piecemeal Armor Layering (`Mythras Customization`)
For simulationist players who want distinct armor on each body part (`e.g., Plate Helm on Head [ABS d10], but Leather Tunic on Chest [ABS d6]`), our `1d8 Location Matrix` automatically checks the **exact Absorption Die (`ABS`) of that specific body part** when resolving the impact check!
