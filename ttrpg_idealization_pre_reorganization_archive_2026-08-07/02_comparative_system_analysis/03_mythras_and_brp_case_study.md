# Case Study 5: Mythras & The $d100$ Differential Special Effects Engine

To expand our research template and uncover foundational mechanics that can elevate our idealized mathless system, we conducted a deep structural analysis of **Mythras** (formerly *RuneQuest 6*, developed by Lawrence Whitaker and Pete Nash at The Design Mechanism). 

Mythras represents the pinnacle of grounded, simulationist d100 combat design. It proves that tactical depth and dramatic stakes do not require class-locked feat trees, escalating $HP$ bloat, or mathematical modifier inflation.

---

## 1. Core Architectural Pillars of Mythras

### 1.1 The $d100$ Opposed Check & Differential Levels of Success
Unlike passive combat engines where an attacker rolls against a static Armor Class ($AC$), combat in Mythras is **actively opposed**.
- Both attacker and defender roll simultaneously ($d100$ percentile roll under their respective `Combat Style %` or `Evade %`).
- Every roll achieves one of four **Levels of Success**:
  1. **Critical Success:** Rolling $\le 1/10\text{th}$ of the skill rating (e.g., Skill $65\% \to$ Crit on $1\text{-}7$).
  2. **Standard Success:** Rolling between critical threshold and the skill rating ($\le 65\%$).
  3. **Standard Failure:** Rolling above skill rating ($66\text{-}98\%$).
  4. **Fumble:** Rolling $99\text{-}00$.

Instead of merely checking who hit or missed, **Mythras compares the difference in success levels between the combatants.** If my attack is a Critical Success (`Level 4`) and your parry is a Standard Failure (`Level 2`), I win by **Two Levels of Success ($4 - 2 = 2$)**.

```
[ Attacker: Critical Success (Level 4) ]  vs  [ Defender: Standard Failure (Level 2) ]
                                    │
                                    ▼
                [ Differential: +2 Levels of Success ]
                                    │
               ┌────────────────────┴────────────────────┐
               ▼                                         ▼
   [ Spend Level 1: Impale ]                 [ Spend Level 2: Bleed ]
(Drive spear deep; weapon stuck)         (Sever artery; rapid blood loss)
```

### 1.2 Universal Special Effects (Maneuvers Without Class Walls)
The "secret sauce" of Mythras is what you do with those differential levels of success: **Special Effects**.
- Whenever a combatant wins an opposed roll by 1 or 2 levels of success, they immediately **spend those differential levels** to choose from a universal catalog of **Special Effects**.
- **No Class Restrictions or Level Gates:** A starting character on turn one has access to the exact same pool of maneuvers as a seasoned veteran. If you achieve a critical hit over a failed parry, you don't need a level 12 "Impaling Feat"; you simply choose `Impale` right at the table.
- **Active Defense Turns the Tables:** If the attacker misses (`Failure`) and the defender succeeds (`Critical Success or Success`), **the defender gains Special Effects against the attacker.** A parrying warrior can instantly `Disarm`, `Overextend`, `Trip`, or `Riposte` their attacker out-of-turn.

---

## 2. Mythras Special Effects Catalog (Offensive vs Defensive)

Every maneuver is succinctly defined in a paragraph or less, allowing rapid table execution:

### 2.1 Sample Offensive Special Effects
- **Impale:** Drives a piercing weapon deep into the target. Deals maximum weapon damage or rolls twice, and the weapon remains wedged inside, inflicting agonizing pain (`penalties to all actions`) until wrenched free (`causing secondary damage`).
- **Bleed:** Severs a major blood vessel. The target loses $1$ or $2$ Fatigue/HP at the start of every turn until medically sutured or coagulated.
- **Bypass Armor:** The strike slips through a gap in plate armor or thick hide (`e.g., eye slit, armpit`). The target's armor Damage Reduction ($DR$) is completely ignored for this hit.
- **Compel Surrender:** Instead of striking a lethal blow, the victor holds their blade to the opponent's throat or eye, forcing an immediate morale/surrender check before blood is shed.
- **Maximize Damage:** The kinetic blow strikes squarely on bone. All weapon damage dice automatically yield their maximum face value.
- **Stun / Bash:** A heavy blunt strike rattles the brain or nervous system. Target must pass a Endurance check or drop incapacitated for $1d4$ rounds.

### 2.2 Sample Defensive Special Effects (`Earned via Successful Parry/Evade over Attack`)
- **Overextend Opponent:** The defender redirects the attacker’s momentum off-balance. The attacker suffers an immediate penalty on their next defensive roll or loses an Action Point ($AP$).
- **Disarm:** The defender catches the attacker’s blade with a crossguard or shield rim, wrenching it out of their hands (`opposed Brawn/Strength check to retain`).
- **Trip / Drop Foe:** A quick foot-sweep or shield bash sends the attacker sprawling `Prone`.
- **Riposte:** If the parry was a Critical Success against a Failure, the defender gets a free, immediate counter-attack strike that cannot be parried.
- **Damage Weapon:** The defender angles their heavy shield or hardened blade to catch the opponent's weapon shaft, inflicting direct structural damage (`Hardness/Hit Points`) to break the incoming weapon.

---

## 3. Hit Locations & The 3-Tier Anatomical Wound System

While most games track a single abstract bar of $100+$ Hit Points, Mythras uses **Localized Hit Locations** (`Head 13-20`, `Chest 09-12`, `Abdomen 07-08`, `Left Arm 04-06`, `Right Arm 01-03`, `Left Leg/Right Leg`).

### 3.1 Static HP & Armor Soak per Location
- Each location has its own static pool of Hit Points based on character Size and Constitution (`e.g., Head = 5 HP, Chest = 7 HP, Arm = 4 HP`). **These points do NOT scale with character advancement.** A veteran warrior has roughly the same anatomical HP as a novice.
- Armor applies local Damage Reduction ($DR$) only to the location it covers (`e.g., Steel breastplate = +6 DR on Chest; Leather bracers = +2 DR on Arms`).

### 3.2 The Three Wound Levels
When damage overcomes armor $DR$, it depletes the local Hit Points and triggers one of three concrete wound states:

| Wound Level | Local HP Formula | Anatomical Consequence & Narrative Reality |
| :--- | :--- | :--- |
| **1. Minor Wound** | `Local HP > 0` | Standard cuts, bruises, and kinetic shock. Causes pain and minor bleeding, but no structural impairment. |
| **2. Serious Wound** | `Local HP <= 0`<br>*(but `> -Starting HP`)* | Structural failure of the limb or organ. If an **Arm**, the limb goes limp (`Drop weapon/shield`). If a **Leg**, target falls `Prone` (`Cannot stand/run`). If **Head, Chest, or Abdomen**, target collapses `Unconscious` and must make Endurance rolls to avoid bleeding out. |
| **3. Major Wound** | `Local HP <= -Starting HP`<br>*(Negative local max)* | **Catastrophic Severance & Destruction.** An **Arm or Leg** is cleanly severed or crushed beyond repair (`Instant shock, permanent loss`). If **Head, Chest, or Abdomen**, the skull is crushed or heart punctured $\to$ **Instant Death**. |

---

## 4. Action Points (`AP`) & Defensive Action Economy

In Mythras, survival is governed by the **Action Point ($AP$) Budget**:
- Characters typically possess **2 or 3 Action Points ($AP$)** per combat round.
- **Active Defense Costs $AP$:** Every offensive strike costs $1 AP$. Crucially, every active **Parry** or **Evade** also costs $1 AP$.
- **The Outnumbering Dilemma:** If you are attacked by three foes and spend all your $AP$ parrying the first two strikes, **you have zero $AP$ left when the third strike arrives.** You cannot actively parry or evade; you must rely entirely on passive armor $DR$ and luck (`Automatic hit against your location`). This makes tactical positioning, shield walls, and outnumbering enemies matter deeply without artificial math.

---

## 5. Rabble & Underlings (`Scaling GM Workload`)

To prevent the GM from getting bogged down tracking Hit Locations for a mob of 15 goblins, Mythras categorizes non-iconic enemies into two streamlined tiers:

| Enemy Tier | Hit Location Tracking? | Special Effect Access? | Morale & Defeat Threshold |
| :--- | :---: | :---: | :--- |
| **Rabble (Minions)** | **NO (`Single Pool`)** | **NO** | Unskilled mobs. They die, flee, or scream upon taking **1 single wound** (`Any hit past armor drops them`). |
| **Underlings (Soldiers)** | **NO (`Single Pool`)** | **YES (`Can use & suffer Special Effects`)** | Competent soldiers. They track a simplified 2-wound threshold and automatically check morale (`Flee/Surrender`) upon taking a Serious wound or losing half their squad. |
| **Iconic Foes (Bosses)** | **YES (`Full Hit Locations`)**| **YES (`Full Mastery`)** | Major villains, dragons, and rival champions. Built with full anatomical hit locations, armor layers, and high $AP$ pools. |

---

## 6. How We Adapt Mythras into Our Mathless `2dX` Engine

Mythras’s brilliance provides four direct structural upgrades for our idealized mathless system (`2dX keep highest`):

1. **Mathless Differential Special Effects (`Maneuver Tokens`):**
   Instead of checking $d100$ math differentials, we measure success differentials directly from our **Step Pool Faces**:
   - **Trigger 1 (`Multi-Beat Differential`):** If your check pool (`3d8`) rolls `5, 7, 8` against a Target DC 6 (or against an opponent's parry face of `6`), you have **two dice (`7 and 8`)** that beat the target. **Each extra beating die awards 1 Mathless Special Effect Token (`[SET]`)** (`2 beating dice = 1 standard hit + 1 Special Effect`).
   - **Trigger 2 (`Max Face Surge`):** Rolling the maximum face value (`8` on $d8$) automatically awards **+1 Special Effect Token (`[SET]`)**.
   - These tokens (`[SET]`) are spent instantly from our universal table (`Impale`, `Bleed`, `Disarm`, `Overextend`, `Riposte`) without checking class prerequisites!

2. **The Active Defense Economy (`Stamina / Reaction Trade-off`):**
   We adopt Mythras's defensive tension: every character has **1 free Reaction slot (`[1R]`)** per round (`Raise Shield`). If targeted by additional attacks beyond that slot, they must **burn 1 Stamina per active parry/evade** (`Parry Fatigue`). If they run out of Stamina, they cannot parry, leaving their physical **Soak Rank** as their only line of defense.

3. **Hit Location Integration (`Anatomical Step Matrix`):**
   We integrate Mythras's anatomical locations into our wound model. When an attack beats Soak by $\ge 1$ step (`Severe Wound`), the player or GM rolls a single **Anatomical Location Die ($1d8$)** (`1-2 Head, 3-4 Chest, 5 Abdomen, 6-7 Arms, 8 Legs`) to apply localized structural impairments (`Dropped weapon`, `Prone`, `Concussion`) without adding numerical HP bookkeeping.

4. **Rabble & Underling Mob Management:**
   We adopt exact Mythras mob tiers for GMs: `Rabble` die on any hit exceeding Soak; `Underlings` use Special Effects but collapse after 1 severe wound; `Iconic Bosses` use full multi-layer defenses and anatomical wound clocks.
