# Core Design Pillars

This document establishes the foundational design philosophy of our idealized TTRPG system. Every mechanical rule, character feature, and conversion procedure must align with these four pillars.

---

## Pillar 1: The Mathless Resolution Engine

### 1.1 The Problem with Modifier Arithmetic
In traditional d20-based systems like D&D 3.5e or Pathfinder 2e, action resolution relies on linear equation building at the gaming table:
$$\text{Total} = d20 + \text{Base Attack Bonus} + \text{Attribute Modifier} + \text{Feat Bonus} + \text{Buffs} - \text{Penalties} + \text{Situational Modifiers}$$

While mathematically expressive, this creates significant friction:
- **Cognitive Load & Latency:** Players and Game Masters (GMs) spend valuable seconds before and after every die roll recalculating dynamic numbers.
- **Mental Math Fatigue:** Over a 4-hour session, tracking temporary +1s, -2s, and conditional modifiers leads to exhaustion and missed bonuses.
- **Abstract Detachment:** Numbers become disconnected from the physical action; a "+2 from flanking" is just an arithmetic adjustment rather than a tactile advantage.

### 1.2 The Mathless Solution: Tactile Dice Manipulation
Our system eliminates arithmetic entirely during active play. Action checks compare **raw die face values directly to a Target Number (DC)** or to an **Opponent's Defense Die/Roll**.

- **No Addition or Subtraction:** A die showing an `8` is simply an `8`. You never add your Strength or subtract an enemy's cover bonus.
- **Step Dice for Capability Ceiling ($d4 \to d12$):** Your die size dictates your absolute potential and mastery. A novice rolls $d4$ (can never naturally exceed DC 4 without special effort), while a grandmaster rolls $d12$.
- **Pool Volume for Reliability ($1d \to 4d+$):** Having multiple dice in your pool represents redundancy, training, or superior positioning. **You roll the pool and keep the highest result.**
- **Boons & Banes (Dice Swaps & Additions):** Instead of adding $+2$ or $-2$, situational advantages add **Boon Dice** (extra dice rolled into the pool where the highest is kept, or step upgrades to existing dice), while penalties introduce **Bane Dice** (dice that force you to keep lower results or cancel out high dice).

---

## Pillar 2: Grounded Simulationism & Concrete Capabilities

### 2.1 Multi-Layered Defenses Over Abstract Armor Class
In D&D 3.5e, "Armor Class" (AC) conflates dodging an attack, deflecting it with a shield, absorbing it with heavy steel plate, and magical warding into a single binary pass/fail number.

In our system, combat resolution respects the physical reality of an attack's trajectory:
1. **Evasion (Mobility & Reflexes):** Can the target completely dodge out of the path of the attack?
2. **Parry / Deflection (Weapon & Shield Mastery):** Can the target actively intercept or redirect the incoming strike?
3. **Soak / Absorption (Armor & Physical Hide):** If the strike connects, how much physical kinetic impact or cutting power is negated before tissue damage occurs?
4. **Resilience / Will (Metabolic & Mental Fortitude):** How well does the body/mind resist poison, shock, magic, or psychological trauma?

### 2.2 Skills as Generic & Specific Capabilities
Skills are not merely abstract ratings rolled once per scene. They model concrete proficiencies and specialized capabilities:
- **Capability Thresholds:** Certain complex tasks (e.g., forging a masterwork blade, picking a tumbler lock, performing surgery) cannot be attempted without specific skill ranks ($d6+$).
- **Maneuver Unlocks:** Investing in Athletics doesn't just increase your jump roll; it unlocks physical maneuvers like *Shove, Grapple, Disarm,* and *Tackle*, each operating seamlessly on the core mathless pool engine.

---

## Pillar 3: Strict Elimination of Meta-Currencies

### 3.1 Why Meta-Currencies Break Simulation
Many modern RPGs utilize out-of-world meta-currencies (e.g., Fate Points, 5e Inspiration, Savage Worlds Bennies, Burning Wheel Artha) that allow players to reroll dice, edit narrative reality, or negate damage simply by spending an abstract out-of-character token.

While great for narrative control, meta-currencies fracture immersion for simulationist players because the **character** does not know what a "Fate Point" is. Why did the warrior suddenly survive a lethal axe blow? Because the *player* spent a red poker chip.

### 3.2 In-World Resource Replacement
In our system, **every spendable resource must exist within the fiction:**
- **Stamina / Poise Pool:** Physical stamina, breath, and balance. Characters spend Stamina to execute strenuous combat maneuvers, *Die Step-Up* their dice pool for a desperate surge of power, or absorb kinetic shock. When Stamina hits zero, the character is exhausted and vulnerable.
- **Focus / Concentration:** Mental acuity used by scholars, scouts, and spellcasters to maintain spells or precision actions.
- **Equipment Durability & Wear:** Shields can be splintered (`Sacrifice Armor`) to absorb a blow that would otherwise cause a severe wound. This is an in-world physical tradeoff, not a meta-currency spend.

---

## Pillar 4: Wealth of Content & High Option-Density

### 4.1 The Option-Density Challenge
D&D 3.5e and Pathfinder 2e are beloved for their massive character customization options: thousands of feats, spells, prestige classes, character ancestries, and equipment builds. However, in those games, 80% of these options boil down to numerical modifiers (`+1 to attack with swords`, `+2 to saves vs fear`).

### 4.2 Mathless Content Architecture
To support an enormous library of character options (`Feats`, `Paths`, `Spells`, `Maneuvers`) without collapsing into mathematical bloat, every content piece in our system is built from **Discrete Mechanical Vectors**:
1. **Step Upgrades / Die Step-Up:** A trait permanently upgrades a specific die step under specific conditions (e.g., *Weapon Master (Swords): Roll $d8$ instead of $d6$ when attacking with longswords*).
2. **Pool Volume Expansion (Advantage / Boons):** A feat grants an extra die (`+1d`) to the pool in defined tactical contexts (e.g., *Pack Hunter: Add $+1d$ to your melee attack pool when an ally threatens the same target*).
3. **Dice Face Manipulation / Rerolls:** Traits allow interacting with specific dice results without math (e.g., *Cleaving Strike: If your attack die rolls its maximum face value [an 'explode' condition without addition], immediately apply your second-highest die in the pool as a separate hit against an adjacent foe*).
4. **Action Economy / Tactical Positioning:** Abilities grant unique action types, free steps, or reaction triggers.
5. **Defense Layer Modification:** Traits alter how defenses interact (e.g., *Shield Wall: You can apply your Parry die to defend an adjacent ally against ranged attacks*).

### 4.3 Low-Memory Feature Design

High option density must not require players to remember a personal catalogue of narrow, persistent, conditional modifiers. The default conversion preference is:

1. A one-time declared Action, Reaction, Strike enhancer, or explicit resource expenditure.
2. A broad Permission, Trait, or reusable named Condition with a clear scope.
3. A short, explicit duration when an ongoing effect is essential.

Avoid stacking persistent bonuses, separate conditional counters, and effects that require repeatedly checking many small triggers. A persistent conditional effect is justified only when it is central to the source identity and cannot be expressed more broadly through an Action, Permission, Trait, Condition, or clearly bounded resource use.

When converting legacy content, retain the source feature name unless and until a replacement name is explicitly approved. Do not invent flavorful substitute names merely to fill an unfinished procedure.
