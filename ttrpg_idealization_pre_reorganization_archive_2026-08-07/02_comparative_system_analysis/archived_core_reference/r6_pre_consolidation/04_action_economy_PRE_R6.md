# Action Economy & Turn Structure

To achieve the tactical depth and combat fluidity of Pathfinder 2e without tracking numerical modifiers across multiple turns, our system adopts a streamlined **3-Action Economy** supported by **Mathless Tactical Positioning** and **Dynamic Reactions**.

---

## 1. Initiative & Round Structure

Combat is divided into **Rounds**, each representing roughly 6 seconds of intense tactical exchange. Within a round, characters take **Turns** based on initiative order.

### 1.1 Mathless Initiative Check
At the start of a combat encounter, every participant makes an **Initiative Check**:
- **Physical Ambush / Quick Reflexes:** Roll your base **Agility Pool (`2dAGI`)**.
- **Tactical Assessment / Prepared Trap:** Roll your base **Intellect Pool (`2dINT`)**.

Instead of writing down numbers (`24`, `18`, `12`), initiative order is sorted directly by the **Highest Rolled Face Value** from highest (`12`) to lowest (`2`). 
- **Ties:** Break ties by checking the second die in the pool (`Secondary Tiebreaker`). If still tied, player characters act before NPCs.

---

## 2. The 3-Action Economy (`[A] [A] [A]`)

On their turn, every character has exactly **Three Action Points (`3 Actions`)** to spend. They can spend these points in any order, choosing from **Single Actions (`[1A]`)**, **Two-Action Activities (`[2A]`)**, or **Three-Action Surges (`[3A]`)**.

```
[ Character Turn Budget: 3 Action Points ]
  ├── [1A] Move / Stride (Move 1 zone / 30 ft)
  ├── [1A] Strike (Melee/Ranged weapon attack pool)
  ├── [1A] Tactical Maneuver (Shove, Disarm, Feint, Demoralize)
  ├── [1A] Raise Shield / Prepare Parry (Activate Parry Defense pool)
  ├── [2A] Cast Standard Spell (Channel arcane/divine magic)
  └── [3A] Devastating Flourish (Special attack + movement surge)
```

### 2.1 Why No Multiple Attack Penalty (MAP) Arithmetic?
In Pathfinder 2e, making a second attack on the same turn imposes a `-5` penalty (`-4` with agile weapons), and a third attack imposes `-10`. While effective for balancing actions, **this requires heavy numerical subtraction every round.**

### 2.2 Our Mathless Multi-Action Solution: Pool Fatigue (`Banes`)
Instead of subtracting numbers (`-5 / -10`), making multiple physical attacks or strenuous checks within the same turn imposes **Stamina / Pool Fatigue**:
- **First Attack / Check (`[1A]`):** Rolled with normal pool (`2dX keep highest`).
- **Second Attack on Same Turn (`[1A]`):** Rolled with **$+1\text{ Bane Die}$** (`1dX` face roll, or spend `1 Stamina` to Die Step-Up back to `2dX`).
- **Third Attack on Same Turn (`[1A]`):** Rolled with **$+2\text{ Bane Dice}$** (`2dX keep lowest` / Disadvantage, representing physical exhaustion and overextension).

---

## 3. Core Action Catalog

### Single Actions (`[1A]`)
- **Stride / Move (`[1A]`):** Move up to your character's Speed (`Standard: 30 feet` or `1 Combat Zone`).
- **Strike (`[1A]`):** Make a melee or ranged attack against a target within reach/range using your `Combat Mastery` pool against their **Evasion** or **Parry**.
- **Raise Shield / Active Defense (`[1A]`):** Position your shield or weapon defensively until the start of your next turn. While active, you can roll your **Parry Pool (`2dParry`)** to intercept any incoming melee or ranged physical attacks without spending Stamina.
- **Tactical Maneuver (`[1A]`):** Attempt an opposed check (`Shove`, `Grapple`, `Trip`, `Disarm`, or `Demoralize`).
  - *Grapple / Trip vs Evasion:* If successful, the target is `Prone` or `Restrained`.
  - *Demoralize vs Will:* If successful, the target takes $+1\text{ Bane Die}$ on their next action due to fear/shaken poise.
- **Interact / Use Item (`[1A]`):** Draw a weapon, drink an elixir, open a door, or pull a lever.

### Two-Action Activities (`[2A]`)
- **Cast a Spell (`[2A]`):** Channel arcane, divine, or primal energy to manifest a standard spell (`Fireball`, `Cure Wounds`).
- **Charge / Pounce (`[2A]`):** Stride up to double your Speed in a straight line and immediately make a melee Strike with $+1\text{ Boon Die}$ (`3dX keep highest`) due to built-up kinetic momentum.
- **Aim / Careful Shot (`[2A]`):** Spend `[1A]` aiming and `[1A]` firing. Your ranged Strike gains **$+2\text{ Boon Dice}$** (`4dX keep highest`), almost guaranteeing a high face hit on distant targets.

### Three-Action Surges (`[3A]`)
- **Full Defense Stance (`[3A]`):** Forfeit all offensive actions to brace yourself. Until your next turn, all attacks targeting your Evasion or Parry roll with **$+2\text{ Bane Dice}$** (`2dX keep lowest`), and your Soak Rank is stepped up (`d6` $\to$ `d8`).

---

## 4. Tactical Positioning Without Numerical Modifiers (`No +2s`)

In 3.5e, tactical positioning adds small conditional bonuses (`+2 Flanking`, `+4 Cover`, `-2 High Ground`). We convert these directly into **Pool Volume Boons and Banes**:

| Tactical Situation | Traditional d20 Modifier | Our Mathless Pool Interaction |
| :--- | :---: | :--- |
| **Flanking / Surrounding** | `+2 to Attack` | **Attacker gains $+1\text{ Boon Die}$ (`3dX keep highest`).** The defender’s attention is split across multiple threat angles. |
| **Partial Cover (Obstacle / Trees)** | `+4 to AC` | **Attacker takes $+1\text{ Bane Die}$ (`1dX`).** The obstacle breaks line of sight or deflects projectiles. |
| **Heavy Cover / Arrow Slit** | `+8 to AC` | **Attacker takes $+2\text{ Bane Dice}$ (`2dX keep lowest`).** Hitting the exposed area requires incredible luck. |
| **High Ground / Elevated Strike** | `+1 to Attack` | **Attacker gains $+1\text{ Boon Die}$ (`3dX`).** Gravity and reach favor the downward strike. |
| **Prone Target (Melee Attack)** | `+4 to Attack` | **Melee Attacker gains $+2\text{ Boon Dice}$ (`4dX`).** Target cannot easily evade on the ground. |
| **Prone Target (Ranged Attack)** | `-4 to Attack` | **Ranged Attacker takes $+1\text{ Bane Die}$ (`1dX`).** Target presents a significantly smaller profile. |

---

## 5. Reactions & Out-of-Turn Interventions (`[R]`)

Every character gets exactly **One Reaction Slot (`[1R]`) per round**, which resets at the start of their turn. Reactions allow out-of-turn tactical counter-play without requiring meta-currencies.

### 5.1 Standard Reactions
- **Attack of Opportunity (`[R]`):** Triggered when an adjacent enemy leaves your melee reach without using a careful `Step/Disengage` action (`[1A]`), or when they cast a spell without defensive casting. You make an immediate single melee Strike (`[1A]`) against them.
- **Active Parry Intercept (`[R]`):** If you did not `Raise Shield (`[1A]`)` on your turn, you can spend your `[1R]` slot and **1 Stamina** to instantly make an opposed **Parry Check** against an incoming strike.
- **Shield Block / Armor Sacrifice (`[R]`):** When an attack hits and beats your Soak Rank, you can spend your `[1R]` to absorb the blow using your shield/armor's Hardness, potentially splintering `1 Durability Slot` to prevent a severe Wound Condition entirely (`Sacrifice Item`).
