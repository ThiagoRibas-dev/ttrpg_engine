# Dual-Mode Spatial & Distance Engine

To accommodate both miniature/VTT grid tacticians and theater-of-the-mind players without splitting the core resolution rules, our system natively supports **Dual-Mode Spatial Resolution**: exact, specific measurements (`Feet / Meters / Grid Squares`) and **5-Tier Abstracted Distances (`Zones / Tiers`)**. 

Both modes operate seamlessly with our 3-action economy (`[1A] Stride`) and weapon reach mechanics, linked by precise conversion formulas.

---

## 1. The 5-Tier Abstracted Distance Model (`Mode B`)

When playing without a grid or using zone-based combat maps, distances are classified into five concrete spatial tiers:

```
[ Tier 0: Close ] ◄──► [ Tier 1: Near ] ◄──► [ Tier 2: Medium ] ◄──► [ Tier 3: Far ] ◄──► [ Tier 4: Distant ]
 (0-5 ft / Melee)     (10-30 ft / Zone 1)   (35-60 ft / Zone 2)    (65-120 ft / Zone 3)  (125-300+ ft / Artillery)
```

| Distance Tier | Name / Label | Specific Measurement Equivalent | Typical Combat & Tactical Interaction |
| :---: | :--- | :--- | :--- |
| **Tier 0** | **Close / Melee Reach** | `0 to 5 Feet` (`1 Grid Square`) | Grappling, unarmed brawling, daggers, swords, touch spells, and immediate shield clashes. |
| **Tier 1** | **Near / Short Range (`1 Zone`)** | `10 to 30 Feet` (`2 to 6 Squares`) | Polearms (`10 ft`), thrown axes, pistol volleys, short-range spells (`Cone of Cold, Color Spray`), standard single-action Stride (`[1A]`). |
| **Tier 2** | **Medium / Tactical (`2 Zones`)** | `35 to 60 Feet` (`7 to 12 Squares`) | Standard archery, crossbow volleys, medium-range spells (`Fireball, Lightning Bolt`), charge attacks (`[2A] double Stride`). |
| **Tier 3** | **Far / Long Range (`3 Zones`)** | `65 to 120 Feet` (`13 to 24 Squares`) | Longbows, heavy siege crossbows, long-range sniper spells (`Dimension Door, Fireball max range`). Requires two Strides (`[2A]`) just to enter Near range. |
| **Tier 4** | **Distant / Horizon (`4+ Zones`)** | `125 to 300+ Feet` (`25+ Squares`) | Artillery, catapults, mythic dragon flight, horizon scouting. Ranged attacks beyond weapon max range roll with $-2\text{ Banes (`2dX keep lowest`)}$. |

---

## 2. Mode A: Specific Distance Mechanics (`Grid & Exact Measurements`)

For tables using 5-foot grid squares or exact measurements (`VTTs, miniatures`):
- **Standard Stride (`[1A]`):** Move up to **30 feet (`6 Squares`)**. Heavy armor (`Plate`) reduces speed to **20 feet (`4 Squares`)** unless mitigated by racial feats (`e.g., Dwarf/Ogre Vigor`).
- **Weapon Reach:**
  - *Standard Melee:* `5 feet (`1 Square`)` (`Swords, Axes, Maces`).
  - *Long Reach Melee (`[Reach]` trait):* `10 feet (`2 Squares`)` (`Spears, Halberds, Whips`).
  - *Giant / Large Creature Reach:* `10 to 15 feet (`2-3 Squares`)`.
- **Area of Effect (`Exact Shapes`):** Spells and hazards specify exact radii (`20-foot radius sphere for Fireball`, `30-foot cone for Breath Weapon`, `60-foot line for Lightning Bolt`).

---

## 3. Seamless Conversion Guidelines (`Exact <-> 5-Tier`)

Game Masters and players can instantly convert rules, spells, and movement across both modes using these three rules of thumb:

### 3.1 Movement Conversion (`Striding Across Tiers`)
$$\text{1 Standard Stride ([1A] Action) = Move 30 Feet = Shift Exactly 1 Distance Tier}$$
- **Moving Closer (`Tier Shift Down`):** If an enemy is at **Tier 2 (`Medium Range`)**, spending `[1A] Stride` moves you to **Tier 1 (`Near Range`)**. Spending a second `[1A] Stride` moves you into **Tier 0 (`Intimate / Melee Reach`)**.
- **Disengaging (`Tier Shift Up`):** To leave Tier 0 (`Melee`) without triggering an **Attack of Opportunity (`[R]`)**, a character must spend `[1A]` on a careful **Step / Disengage** action (`Moving 5 feet / remaining in Tier 1`). If they simply `Stride (`[1A]`)` away to Tier 1, adjacent enemies get an immediate reaction strike.

### 3.2 Area of Effect (`AoE`) Conversion Table
When converting specific D&D/PF2e spell dimensions into 5-Tier zones without measuring squares:

| Traditional 3.5e / PF2e AoE Shape | Exact Grid Measurement | Converted 5-Tier Zone Equivalent |
| :--- | :--- | :--- |
| **Small Burst / Sphere** | `5 to 10 Foot Radius` | **Sub-Zone / Melee Cluster:** Affects all creatures currently inside **Tier 0 (`Close reach`)** of the target point. |
| **Standard Blast / Sphere** | `15 to 20 Foot Radius`<br>*(e.g., Fireball, Web)* | **Full Zone (`1 Tier Span`):** Affects all creatures currently occupying the target **Distance Tier (`e.g., everyone inside Tier 1 Near`)**. |
| **Massive Storm / Explosion** | `30+ Foot Radius`<br>*(e.g., Earthquake, Meteor Swarm)* | **Multi-Tier Wipe (`2+ Tiers`):** Affects all creatures across both **Tier 0 and Tier 1 simultaneously**, forcing Reflexes checks from everyone across the battlefield. |
| **Cone Attack** | `15 to 30 Foot Cone`<br>*(e.g., Burning Hands, Dragon Breath)* | **Directional Zone Sweep:** Affects all creatures inside **Tier 1 (`Near`)** within a 90-degree arc in front of the caster. |
| **Line Attack** | `30 to 60 Foot Line`<br>*(e.g., Lightning Bolt)* | **Linear Penetration:** Affects all targets standing in a straight line across **Tier 0 (`Close`), Tier 1 (`Near`), and Tier 2 (`Medium`)** simultaneously. |

### 3.3 Ranged Weapon Range & Penalty Conversion
Instead of calculating specific range increment penalties (`-2 per 30 feet`), ranged attacks check the target's distance tier against the weapon's **Effective Range Tier**:

| Weapon Category | Effective Range Tier (`Normal Roll`) | Maximum Range Tier (`Roll with +1 Bane`) | Beyond Max Range (`Roll with +2 Banes`) |
| :--- | :---: | :---: | :---: |
| **Thrown Weapons** (`Daggers, Axes`) | **Tier 1 (`Near - 30 ft`)** | **Tier 2 (`Medium - 60 ft`)** | **Tier 3 (`Far - 120 ft`)** |
| **Shortbows & Crossbows** | **Tier 2 (`Medium - 60 ft`)** | **Tier 3 (`Far - 120 ft`)** | **Tier 4 (`Distant - 240+ ft`)** |
| **Longbows & Heavy Crossbows** | **Tier 3 (`Far - 120 ft`)** | **Tier 4 (`Distant - 300+ ft`)** | **Horizon (`600+ ft`)** |
| **Siege Engines & Spells** | **Tier 4 (`Distant - 300+ ft`)** | **Horizon (`600+ ft`)** | *N/A* |
