# In-World Resources, Conditions & Injury Modeling

In strict accordance with our design philosophy, our system contains **zero out-of-character meta-currencies**. All survivability, stamina depletion, tactical trade-offs, and physical injuries are tracked using concrete in-world biological, psychological, and material tracks.

---

## 1. Master In-World Resource Tracks

Every character sheet tracks five physical/mental pools:

| Resource Track | Maximum Capacity | Depleted By | Recovered By |
| :--- | :--- | :--- | :--- |
| **1. Vitality (`HP`)** | `MIG Die Max + WIL Die Max`<br>*(e.g., $8 + 6 = 14$)* | Weapon strikes that beat **Soak Rank**, environmental hazards, falling, blood loss. | Medical bandaging, natural rest, or divine miracles. |
| **2. Stamina (`Poise`)** | `2 x MIG Die Max`<br>*(e.g., $2 \times 8 = 16$)* | *Die Step-Up* checks (`1 Stamina`), physical surges/reactions (`1-2 Stamina`), absorbing minor kinetic impacts (`1 Stamina/wound`). | **Short Breather / Rally (`10 minutes`):** Recover 100% Stamina instantly once out of immediate danger. |
| **3. Focus (`Acuity`)** | `2 x INT or WIL Die Max`<br>*(e.g., $2 \times 10 = 20$)* | Casting complex spells (`1-3 Focus`), sustaining arcane concentration (`1 Focus/round`), *Die Step-Up* mental/social checks. | **Short Breather / Meditation (`10 minutes`):** Recover 100% Focus when resting quietly without distraction. |
| **4. Durability Slots** | `1 to 4 Slots per Item`<br>*(Based on item material)* | **Heroic Item Sacrifice (`Absorb Critical Hit`)**, critical parry clashes, acid/rust hazards. | Blacksmith repair at a forge (`Downtime project clock`). |
| **5. Provisions (`Rations`)** | `Encumbrance Slots`<br>*(Typically `6 to 10` slots)* | Daily wilderness travel, forced marches, surviving harsh climates (`1 Provision per day/shift`). | Foraging (`Survival & Athletics check`) or purchasing supplies in towns. |

---

## 2. The Physiological Injury Model (`Wound Conditions`)

When a character takes damage that exceeds their **Soak Rank** (`Damage Die > Soak Die`), or when their **Vitality (`HP`) reaches `0`**, they sustain a concrete **Wound Condition**. 

Unlike abstract HP loss, every Wound Condition represents physical trauma that imposes specific **Die Step-Downs** or **Banes** on relevant physical systems until treated.

### 2.1 Wound Taxonomy & Mechanical Effects

| Wound Condition | Severity | Trigger / Source | Mathless Mechanical Penalty |
| :--- | :---: | :--- | :--- |
| **Bleeding Cut** | Minor | Slashing/piercing weapons exceeding Soak by 1 step. | **Blood Loss:** At the start of your turn, lose **1 Vitality**. Removed immediately by a quick bandaging `Interact (`[1A]`)` action. |
| **Sprained / Strained Joint** | Minor | Bludgeoning weapons, falls, forced grapples. | **Impaired Mobility:** Your Speed is reduced by 10 feet. All `Subterfuge & Navigation` checks roll with **$+1\text{ Bane Die (`1dX`)}$**. |
| **Concussion / Head Trauma** | Moderate | Bludgeoning critical hits, psychic blasts, explosions. | **Sensory Disruption:** Your `Intellect` and `Will` step dice suffer an immediate **Die Step-Down (`d10` $\to$ `d8`)**. You cannot sustain concentration spells (`Focus lock`). |
| **Fractured Rib / Cracked Armor**| Moderate | Crushing blows beating Soak by $\geq 2$ steps. | **Respiratory Pain:** Every time you spend Stamina to *Die Step-Up*, you take **2 Vitality damage** due to physical agony. Your armor loses `1 Durability Slot`. |
| **Severed / Punctured Tendon**| Severe | Critical hits with bludgeoning/piercing weapons at `0 Vitality`. | **Lethal Impairment:** One limb is rendered non-functional. If an arm, drop what you hold (`Cannot wield 2-handed weapons or shields`). If a leg, fall **Prone** (`Cannot Stride normally`). |
| **Mortal Wound / Bleeding Out** | Critical | Taking ANY damage while sitting at `0 Vitality`. | **Death Timer (`3 Round Clock`):** You fall unconscious (`Speed 0`, zero actions). At the end of each round, make a `Resilience Check (DC 6)`. On 3 successes, you stabilize at `1 Vitality` with a severe injury. On 3 failures, your character expires. |

---

## 3. Core Status Conditions (`Binary & Step Flags`)

To ensure clean tactical play, temporary status effects operate as binary flags or step overrides without modifier math:

- **Blinded:** You cannot see. All checks relying on sight automatically fail. Melee and ranged attacks targeting you gain **$+2\text{ Boon Dice (`4dX keep highest`)}$**. Your attacks against others roll with **$+2\text{ Bane Dice (`2dX keep lowest`)}$**.
- **Deafened:** You cannot hear auditory cues or verbal spell commands. You roll with **$+1\text{ Bane Die}`** on perception checks and cannot cast spells requiring vocal pitch precision without `Will d8+`.
- **Exhausted / Fatigued:** Your aerobic resources are completely spent (`Stamina hit 0` after strenuous labor). **All check pools suffer an immediate Die Step-Down (`d8` $\to$ `d6`)**. You cannot *Die Step-Up* until you complete a Long Rest.
- **Muddled / Confused:** Your thoughts are clouded by toxins or illusions. You cannot spend `Focus` or cast spells requiring more than `[1A]`.
- **Prone:** You are lying on the ground. You gain $+1\text{ Boon Die}` vs ranged attacks (`Smaller target`), but enemies making melee strikes against you gain **$+2\text{ Boon Dice (`4dX`)}$**. You can spend `[1A]` to `Stand Up`.
- **Restrained / Grappled:** You are bound or held fast (`Speed 0`). You cannot use physical movement or two-handed weapons. Attacks against you roll with **$+1\text{ Boon Die (`3dX`)}$**.
- **Shaken / Frightened:** Your poise is broken by fear. You roll with **$+1\text{ Bane Die (`1dX`)}$** on all attack and check pools as long as the source of your fear is within line of sight.

---

## 4. Rest & Recovery Mechanics (`In-World Healing`)

Because our system rejects magical meta-currencies, recovering from injuries requires time, rest, and concrete medical or magical intervention.

```
[ Character Sustains Injury & Depletion ]
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
[ Short Breather / Rally ] [ Long Rest / Sleep ]
 (10 Minutes Out of Combat) (8 Hours Camp / Inn)
         │                   │
         ▼                   ▼
 Recover 100% Stamina      Recover 100% Vitality
 Recover 100% Focus        Heal 1 Minor Wound Condition
 (Does NOT heal Wounds)    (Requires Medical Care for Severe Wounds)
```

### 4.1 Short Breather / Rally (`10 Minutes`)
- **Requirement:** The party stops resting, binds minor scrapes, and catches their breath in a secure area (`0 combat activity`).
- **Effect:** Every character recovers **100% of their Stamina and Focus pools** immediately.
- **Limit:** Does **not** restore lost Vitality (`HP`) or cure concrete Wound Conditions.

### 4.2 Long Rest / Encampment (`8 Hours`)
- **Requirement:** 8 hours of uninterrupted sleep or light watch duties, consuming **1 Provision Unit (`Rations`)** per character.
- **Effect:**
  - Recover **100% of maximum Vitality (`HP`)**.
  - Automatically cure **all Minor Wound Conditions (`Bleeding Cut`, `Sprained Joint`)**.
  - If treated by a character with `Trained/Mastered in Medicine (`Lore & Crafting`)`, cure **one Moderate or Severe Wound Condition**. Without medical treatment, severe injuries (`Fractured Rib`, `Severed Tendon`) persist across days until treated or magically healed.

---

## 5. Active Defense Economy & Parry Fatigue (`Mythras Tension`)

To make outnumbering foes tactically decisive without introducing modifier penalties, active defense consumes physical Stamina when under heavy assault:

- **Free Reaction Slot (`[1R]`):** Every character gets exactly **One Free Defensive Reaction (`[1R]`)** per round (`Raise Guard, Active Parry, or Shield Block`).
- **Parry Fatigue (`Stamina Burn`):** If targeted by multiple attacks beyond your single `[1R]` slot in the same round, every subsequent active `Parry` or `Evade` check requires spending **1 Stamina (`Active Defense Expenditure`)**.
- **Defense Collapse (`Stamina Zero`):** If your Stamina pool hits `0` (or you choose to conserve Stamina), you can no longer actively roll your Evasion or Parry pools (`Defense Pool = 0`). The incoming attack automatically connects, leaving your **Soak Rank (`Armor Step Die`)** as your sole defense (`Damage vs Soak`).

---

## 6. GM Mob Management (`Rabble & Underlings Architecture`)

To ensure Game Masters can run massive combat encounters (`15+ goblins or undead`) without getting bogged down by Hit Location rolls or multiple resource tracks, all non-iconic enemies fall into two streamlined tiers:

### 6.1 Rabble (`Minion Fodder`)
- **Zero HP & Zero Location Tracking:** Rabble do not have Hit Locations or Vitality pools.
- **Mathless Defeat Threshold:** Any attack that connects and rolls a **Damage Die face higher than their Soak Rank (`Damage > Soak`)** instantly defeats or routs the Rabble unit (`Killed, knocked out, or flees screaming`).
- **Maneuver Restriction:** Rabble roll basic pools (`2dX`) and **cannot earn or spend Special Effect Tokens (`[SET]`)**.

### 6.2 Underlings (`Squad Soldiers`)
- **Simplified Two-Hit / Morale Threshold:** Underlings track a simple 2-box checkmark (`[○] [○]`).
  - Standard hit (`Damage > Soak`) checks **1 Box (`[●] [○]`)**.
  - Critical hit (`Max face OR 2+ steps over Soak`) checks **2 Boxes (`[●] [●] -> Defeated/Surrenders`)**.
- **Maneuver Capability:** Underlings can earn and spend up to **1 Special Effect Token (`[SET]`)** per round, allowing them to form shield walls, trip PCs, or execute basic maneuvers without GM overload.
