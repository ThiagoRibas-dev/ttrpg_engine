# System Inspirations & Anchor Analysis

To build our idealized TTRPG system, we draw upon specific mechanical philosophies and structural lessons from four primary anchors: **Dungeons & Dragons 3.5e**, the **Demon Lord System (Shadow of the Demon Lord / Weird Wizard)**, **Pathfinder 2e**, and a **Bespoke Mathless System Case Study**.

---

## 1. Primary Anchor: Dungeons & Dragons 3.5e

### 1.1 What We Inherit & Celebrate
- **Unrivaled Build Diversity & Option Wealth:** D&D 3.5e remains the gold standard for high-granularity character customization. Feats, skill synergies, prestige classes, and template stacking allow players to realize distinct, hyper-specific character fantasies.
- **Concrete Simulationist Distinctions:** 3.5e introduced nuanced distinctions such as *Touch Armor Class* (defending against attacks where armor thickness is irrelevant, like magical rays) vs *Flat-Footed Armor Class* (defending when unable to react or dodge), as well as three distinct Fortitude, Reflex, and Will saving throw categories.
- **Deep Monster Ecology & Capabilities:** Monsters have distinct extraordinary (`Ex`), supernatural (`Su`), and spell-like (`Sp`) abilities that interact with physical and magical realities in detailed ways.

### 1.2 What We Strip Away & Reform
- **The $+X / -X$ Modifier Treadmill:** In 3.5e, high-level play bogs down under massive arithmetic chains (`Base Attack +14 / +9 / +4`, `+5 strength`, `+2 enhancement`, `-4 power attack`, `+1 haste`, `+2 flanking`, `-2 shaken`). We strip away the numbers entirely.
- **Linear Attack / Defense Scaling:** Instead of AC scaling from `10` to `45+` while attack bonuses scale from `+0` to `+35`, our system uses bounded **Step Dice (`d4` to `d12`)** and **Pool Volumes (`1d` to `4d`)**, ensuring every roll remains transparent and immediate.

---

## 2. Secondary Anchor: The Demon Lord System (Shadow of the Demon Lord / Weird Wizard)

### 2.1 What We Inherit & Celebrate
- **Boons & Banes as Dynamic Dice:** Robert J. Schwalb’s brilliant alternative to static modifiers (`+2 / -2`) was introducing **Boons and Banes**—rolling extra $d6$ dice alongside the $d20$ and adding/subtracting the highest $d6$ result. While SotDL still uses basic arithmetic ($d20 \pm d6$), the *concept* of situational dice canceling each other out ($1 \text{ Boon} + 1 \text{ Bane} = \text{Normal Roll}$) is mathematically clean and tactile.
- **Modular 3-Tier Path Progression:** Character growth split into **Novice Paths** (Level 1-2: Core archetype like Warrior or Rogue), **Expert Paths** (Level 3-6: Specialized profession like Berserker, Paladin, or Wizard), and **Master Paths** (Level 7-10+: High-concept mastery like Blade Dancer or Chronomancer). This provides 3.5e-level prestige class customization without dead levels or prerequisite traps.

### 2.2 Our Mathless Evolution of Boons & Banes
In our system, because we do not add a $d6$ to a $d20$, **Boons and Banes directly manipulate the Dice Pool**:
- **Boon Dice (`+B`):** Add an extra die of your skill/attribute rank ($+1d$) to your pool. When resolving the check, **you keep the highest result across the entire pool.**
- **Bane Dice (`+X`):** Add a "Bane Die" or force the drop of your highest die, effectively requiring you to **keep the second-highest (or lowest) result**, or step down your die rank for that roll.
- **Mutual Cancellation:** As in SotDL, Boons and Banes cancel each other out 1-to-1 before any dice are picked up.

---

## 3. Tactical & Architectural Anchor: Pathfinder 2e

### 3.1 What We Inherit & Celebrate
- **The 3-Action Economy:** PF2e revolutionized turn structure by giving characters exactly **3 Actions per turn** to spend flexibly between Moving, Striking, Casting, Defending (`Raise Shield`), or performing tactical maneuvers (`Demoralize`, `Feint`, `Shove`). We adopt this clean, highly tactical action budget.
- **Trait & Tag Taxonomy:** Every weapon, spell, action, and monster ability in PF2e is governed by explicit keywords (`[Agile]`, `[Forceful]`, `[Reach]`, `[Auditory]`, `[Fear]`). This modular keyword architecture allows thousands of items and abilities to interact cleanly without ambiguous natural language.
- **Degrees of Success:** Critical Success, Success, Failure, and Critical Failure produce dynamic combat where every check has four potential outcomes rather than a binary hit/miss.

### 3.2 Our Mathless Implementation of Degrees of Success
Instead of checking if a roll is "+10 over the DC" (which requires subtraction), degrees of success are determined directly by **Dice Faces and Pool Overflows**:
- **Critical Success:** Rolling your die's **Maximum Face Value** AND beating the DC, OR having **multiple dice in your pool** beat the DC simultaneously (e.g., rolling two `8`s against DC 6).
- **Success:** At least one die in your pool meets or exceeds the Target Number (DC).
- **Failure:** All dice in your pool roll lower than the Target Number.
- **Critical Failure:** All dice roll lower than the DC AND your highest die rolls a `1` (or multiple `1`s are rolled in the pool).

---

## 4. Case Study Anchor: Bespoke Mathless System Report

### 4.1 Key Lessons from the Developer Self-Report
An uploaded developer self-report detailing six months of open playtesting of a custom mathless step-pool system (`bespoke mathless system report.md`) provides critical real-world validation and design guardrails:

1. **The Power of "Keep Highest":**
   The developer discovered that players instinctively love picking up multiple dice and keeping the highest (`2d10 keep highest` or `3d8 keep highest`). It triggers an intuitive, "lizard-brain gut satisfaction" inherited from D&D's Advantage mechanic, zeroing out cognitive load.

2. **Why Exploding & Cascading Dice Fail (Kill Your Darlings):**
   The developer initially implemented *Cascading Step-Down Dice* (if you roll maximum on a $d10$, you pick up a $d8$ and add/roll it, down to $d4$) and *Exploding Dice* (Savage Worlds style). In thorough playtesting, this proved:
   - **Too Swingy:** Exploding dice created erratic lethal one-shots that broke grounded simulationism.
   - **Too Clunky to Explain & Execute:** Cascading step-down checks slowed play down dramatically, destroying the very intuitive speed the mathless engine was built to achieve.
   - **The Elegant Fix:** Dropping cascades entirely and setting the **base pool to two step dice (`2d6`, `2d8`, etc.) keep highest**. Adding boons increases pool volume (`3d8`, `4d8`), while glitches/banes remove a die (`1d8`) or step it down.

3. **Die Step-Up (In-World Effort vs Static Caps):**
   A major challenge of step dice (`d4` to `d12`) against fixed DCs (`2 to 12`) is that a character rolling `2d4` literally cannot beat a DC of `6`. To prevent frustration while preserving simulationist realism, the developer introduced **Die Step-Up**:
   - **Mechanic:** A character can spend an in-world stamina/resource point to **Die Step-Up** their dice pool up one die rank for a single crucial action (e.g., boosting `2d6` to `2d8`, or `2d8` to `2d10`).
   - **Our Adoption:** We adopt **Die Step-Up** (`Up-Shift`) and **Die Step-Down** (`Down-Shift`) as core mechanics driven by physical stamina and tactical positioning, allowing scrappy heroics without altering mathematical DC targets.

---

## Summary of Anchor Integration

| Anchor / Inspiration | Core Feature Adopted | Mathless / Simulationist Adaptation |
| :--- | :--- | :--- |
| **D&D 3.5e** | Massive Feat/Class options, Touch/Flat-Footed AC concepts, Monster ecologies | Converted into Step Die modifiers, Pool volume additions, and Multi-Layer Defense checks. |
| **Demon Lord System** | Boons & Banes (`+B / +X`), 3-Tier Paths (Novice/Expert/Master) | Boons add dice to the pool (`+1d`); Banes force secondary drop/keep lower results; paths grant discrete traits. |
| **Pathfinder 2e** | 3-Action Economy, Trait/Tag Architecture, 4 Degrees of Success | Actions spent flexibly; tags govern interactions; crits triggered by max faces or multi-die DC beats without math. |
| **Bespoke Mathless Report** | Step-Pools (`2dX` keep highest), Fixed DCs (2-12), Die Step-Up via Stamina | Base rolls are `2d(Rank)` keep highest; Stamina spend shifts die size up (`Up-Shift`); zero cascading or math. |
