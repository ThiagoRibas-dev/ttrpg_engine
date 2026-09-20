# Magic Schools, Traditions, and Spellcasting Framework

This document is the canonical home for the Magic Mastery Domain and its spellcasting framework. It references the canonical Domains, Skills, Activities, and Crafting document for the general skill architecture.

## 2E. Canonical Magic Architecture (`DEC-050`)

Magic uses several independent classification axes. These axes must not be collapsed into one list.

### Schools

The eight traditional D&D-compatible schools remain the technical classifications of spells:

- Abjuration
- Conjuration
- Divination
- Enchantment
- Evocation
- Illusion
- Necromancy
- Transmutation

A school answers: **What technical operation does this spell perform?**

### Traditions

Traditions are modular magical access and specialization packages. A spell may belong to two or more traditions. Traditions determine who can learn, prepare, and specialize in a spell, while class, path, feat, or other access features determine which traditions a character can use.

Current Magic Mastery traditions:

#### Foundational Traditions

- Arcane / Thaumaturgic
- Divine / Theurgic
- Primal / Natural
- Spirit
- Shadow

#### Specialist Traditions

- Elemental
- Rune
- War
- Dream
- Life
- Death
- Eldritch / Void

#### Advanced or Restricted Traditions

- Time
- Space
- Chaos
- Order
- Creation

The slash terms are development terminology and may be resolved during later setting and spellcasting work. Arcane describes manipulation of raw magic through study, formula, intuition, or will. Divine describes power channeled through a deity, covenant, sacred authority, cosmic principle, or higher power. Celestial may exist as a Divine specialization rather than replacing Divine as the universal category. Natural World may exist as a Primal specialization rather than replacing Primal as the formal tradition.

### Spell Traits

Traits describe practical delivery and interaction, such as:

- Fire
- Healing
- Ritual
- Area
- Projectile
- Touch
- Sustained
- Summoning
- Mind-Affecting
- Language-Dependent
- Movement
- Reaction
- Corpse

### Alchemy

Alchemy is not a Magic Mastery tradition. It is governed by Knowledge — Alchemy and Pharmacology, Craft — Alchemy, tools, reagents, equipment, and downtime. Alchemy may imitate a spell or produce pseudo-magical effects without being a spell.

- Knowledge — Alchemy and Pharmacology identifies, analyzes, and designs compounds.
- Craft — Alchemy physically produces, refines, and prepares compounds.

### Psychic/Psionic Power

Psychic/Psionic power is provisionally a separate non-Vancian supernatural system rather than a Magic Mastery tradition. It may use Focus, disciplines, augmentations, mental exertion, and strain instead of daily Vancian preparation. This remains a future subsystem decision; full Vancian magic and full Psionic flexibility must not be granted together without meaningful opportunity cost.

### Canonical Multi-Axis Spell Record

A spell may be recorded as follows:

```text
Spell: Fireball
School: Evocation
Traditions: Arcane, Elemental, War
Traits: Fire, Area, Projectile
```

```text
Spell: Cure Wounds
School: Necromancy
Traditions: Divine, Life, Primal, Spirit
Traits: Healing, Touch
```

The same School may appear across different Traditions, and the same Tradition may use multiple Schools. This overlap is intentional and supports SotDL-style specialization without sacrificing D&D-compatible spell classification.


## 2F. Unified Spellcasting and Multiclassing (`DEC-051`)

The system uses one universal spellcasting framework. Classes do not own separate spell lists, casting profiles, or spell-slot pools.

### Traditions are individual skills

Each Tradition is an individual skill using the normal Competency Rank system. Classes and modular paths grant access to Tradition skills and may automatically protect or advance a primary Tradition. General investment may specialize secondary Traditions.

A character has one rank in each Tradition, regardless of how many classes or paths grant access to it.

### Fixed Tradition spell lists

Each Tradition has one fixed spell list regardless of source. Death accessed through a Cleric and Death accessed through a Wizard are the same Death Tradition and use the same Death spell list.

A spell may belong to multiple Traditions. A character learns a spell once; if at least one currently active Tradition grants access to that spell, the character may prepare it, subject to the Tradition Competency requirement.

### Shared spell slots

All spellcasters use one shared pool of daily Vancian spell slots organized by Spell Rank. There are no separate Cleric slots, Wizard slots, or Tradition slots.

The universal preparation rule is used by all characters. Classes and paths do not create spontaneous-versus-prepared casting distinctions. Instead, class and path features change how the character acquires spells and what additional casting options they possess.

Examples of acquisition features include:

- A Wizard learns a defined number of spells per Wizard level.
- A Wizard may research, copy, transcribe, or learn spells from scrolls and other spellbooks.
- A Cleric learns a defined number of spells per Cleric level.
- A Cleric may acquire spells through prayer, revelation, religious instruction, or divine source access.
- A Prestige Path may grant specific spells, expand a Tradition list, or provide a special method of acquisition.

These acquisition methods add spells to one unified learned-spell collection. A multiclass character may use all applicable acquisition methods, creating a trade-off between broader class mechanics and deeper Tradition investment.

### Tradition Rank and spell rank

Tradition Competency replaces a separate per-Tradition caster-level statistic. Tradition Rank determines the highest Spell Rank the character can use through that Tradition and determines the spell's intrinsic scaling.

| Tradition Rank | Highest usable Spell Rank |
|---|---|
| Untrained | None |
| Trained | Novice |
| Expert | Expert |
| Master | Master |
| Legendary | Heroic/Legendary, subject to the final high-tier spell framework |

The character must satisfy both requirements:

1. Have sufficient Tradition Competency for the spell.
2. Spend an available shared slot of the spell's Spell Rank.

A character may know a spell above their current Tradition Rank, but cannot currently prepare or cast it through that Tradition. If the Tradition later advances, the already-learned spell becomes usable.

### D&D 3.5e-style intrinsic scaling

Spells automatically improve according to the caster's relevant Tradition Competency. Casting a lower-rank spell in a higher-rank slot does not automatically improve it.

```text
Death: Trained  → use the Trained version of a Death spell
Death: Expert   → use the Expert version of that Death spell
Death: Master   → use the Master version of that Death spell
```

Spell Rank determines the slot consumed. Tradition Competency determines the spell's intrinsic scale and casting quality.

### Shared Traditions between classes

If both Cleric and Wizard grant Death, the character has one Death skill and one Death spell list. Both classes may contribute access and acquisition options; neither creates a separate Death version.

```text
Cleric/Wizard:
  Death: Expert
  Death spell list: one shared list
  Spell slots: one shared pool
  Spell acquisition: Cleric methods plus Wizard methods
```

The character does not track Death — Cleric, Death — Wizard, separate caster levels, or separate slot pools.

### Essence

The former Focus resource is renamed **Essence**. Essence remains separate from Stamina.

Essence powers:

- 0th-rank spells, cantrips, and orisons.
- Metamagic feats.
- Casting stability under distraction, injury, adjacency, or other interference.
- Emergency casting.
- Supernatural class features such as Turn or Rebuke Undead, Smites, and certain Devotion Feats.

### Psychic/Psionic power

Psychic/Psionic power is provisionally a separate Essence-based supernatural system rather than a Vancian Tradition. Its disciplines, augmentation rules, strain, and interaction with ordinary spellcasting remain future work.


## 2G. Spellcasting Progression and Shared Slot Table (`DEC-052`)

The system uses one shared daily Spell Slot pool. A character's **Spellcasting Progression Level** determines their position on the shared slot table. This value is distinct from Character Level, High Fantasy Tier, Tradition Competency, Spell Circle, and Essence.

### Spellcasting Progression Level

A full caster whose spellcasting advances at every class level has Spellcasting Progression Level equal to Character Level. A multiclass character may have a lower Progression Level than Character Level.

The baseline Good/Reference Spellcasting Progression uses the modified D&D 3.5e-style table below. “Good,” “Mediocre,” and “Bad” are design guidelines for comparing class advancement cadences; they are not separate player-facing resources or tracks.

| Tier | Progression Level | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Trained | 1 | 4 | — | — | — | — | — | — | — | — |
| Trained | 2 | 4 | — | — | — | — | — | — | — | — |
| Trained | 3 | 4 | 2 | — | — | — | — | — | — | — |
| Trained | 4 | 4 | 2 | — | — | — | — | — | — | — |
| Veteran | 5 | 5 | 2 | 2 | — | — | — | — | — | — |
| Veteran | 6 | 5 | 3 | 2 | — | — | — | — | — | — |
| Veteran | 7 | 5 | 3 | 2 | 2 | — | — | — | — | — |
| Veteran | 8 | 5 | 3 | 3 | 2 | — | — | — | — | — |
| Master | 9 | 5 | 4 | 3 | 2 | 2 | — | — | — | — |
| Master | 10 | 5 | 4 | 3 | 3 | 2 | — | — | — | — |
| Master | 11 | 5 | 4 | 4 | 3 | 2 | 2 | — | — | — |
| Master | 12 | 5 | 4 | 4 | 3 | 3 | 2 | — | — | — |
| Hero | 13 | 5 | 5 | 4 | 4 | 3 | 2 | 2 | — | — |
| Hero | 14 | 5 | 5 | 4 | 4 | 3 | 3 | 2 | — | — |
| Hero | 15 | 5 | 5 | 5 | 4 | 4 | 3 | 2 | 2 | — |
| Hero | 16 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 2 | — |
| Legend | 17 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 2 | 2 |
| Legend | 18 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 2 |
| Legend | 19 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 |
| Legend | 20 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 |

### Level-by-level class advancement

Every Base Class and Prestige Class includes a **Spellcasting Advancement** column in its level-by-level table. The table explicitly marks each level that grants one advancement. Class descriptions may summarize the cadence, but the level-by-level table is authoritative.

Examples:

- Wizard: `+1` advancement at every Wizard level.
- Paladin: `+1` advancement at selected levels, such as levels 2, 4, 6, 8, and 10.
- Eldritch Knight: `+1` advancement at selected levels, such as levels 3, 6, and 9.
- Fighter: no Spellcasting Advancement unless a specific class feature grants one.

Prestige Classes use exactly the same procedure as Base Classes. Their entry requirements, not a different multiclassing system, distinguish them.

### Multiclassing

Add all completed Spellcasting Advancements from all Base Classes and Prestige Classes. The total is the character’s Spellcasting Progression Level, and the character uses that row of the shared slot table.

```text
Wizard 4 / Fighter 4:
  4 + 0 = Spellcasting Progression Level 4

Wizard 4 / Paladin 4:
  4 + 2 = Spellcasting Progression Level 6

Wizard 4 / Eldritch Knight 3:
  4 + 1 = Spellcasting Progression Level 5

Wizard 4 / Cleric 4:
  4 + 4 = Spellcasting Progression Level 8
```

The arithmetic occurs during advancement or character creation, not during ordinary action resolution. During play, the sheet simply records the final Progression Level and shared slot quantities.

### Tradition Competency does not gate slot access

Spellcasting Progression determines daily slot volume. Tradition Competency determines spell access, casting quality, and intrinsic spell scaling. A character may possess a high Spellcasting Progression Level while having only shallow investment in a particular Tradition.

Using a higher-Circle slot does not automatically improve a lower-Circle spell. A spell improves only when its entry explicitly provides a Heightened version. Its normal intrinsic scaling comes from the relevant Tradition Competency.

### Mythic advancement

Mythic advancement does not automatically add new ordinary Spell Slots beyond the Level 20 table. It grants access to Epic Traditions and Epic Spells that use the existing shared slot framework, potentially alongside Essence, rituals, rare components, or other in-world requirements.


### Derived cadence tables

The Reference Good Slot Progression is the only universal slot table. The Mediocre and Bad examples are derived views, not separate player-facing tracks:

- **Full cadence:** advance to the next Reference row every class level.
- **Mediocre cadence:** advance to the next Reference row every two class levels.
- **Bad cadence:** advance to the next Reference row every four class levels.

The derived CSV catalogue records these views by **Character Level**. The Reference table is indexed by **Spell Slot Progression Level**; the derived views show which Reference row each class level currently uses.

The design principle is that every Reference row should differ meaningfully from the preceding row, so every Spell Slot Advancement produces a visible change in slot volume or Spell Circle access.

## 3. The 5 Competency Ranks (`Investment-Driven Step, Volume & Floor`)

When a character levels up and allocates their **Class Skill Allocations (`DEC-035 Track 5`)**, they invest points directly into **Specific Individual Skills** (`e.g., investing into *Diplomacy* to reach `Expert (+1B, +1 Step, Floor 5)`, while leaving *Deception* under the same Social umbrella at `Untrained (Floor 0)`!).

Advancing a specific skill rank transforms your check pool across all three check variables (`Die Size X, Pool Volume N, and Competency Floor F`):

| Competency Rank (`Investment Level`) | Check Pool Modification (`Die Size X & Pool Volume N`) | Competency Floor (`F`) | Multi-Success Maneuver Permissions (`DEC-043`) | What This Represents Physically & Conceptually |
| :--- | :--- | :---: | :--- | :--- |
| **0. Untrained** (`Zero Investment`) | **Base Pool `2dX keep highest`**<br>*(Attribute Die only — $+0B, +0 Steps*)* | **Floor = 0**<br>*(Pure random roll)* | Can execute `1 Success` Standard Hits (`Damage vs ABS`). *No multi-success maneuver triggers (`Prone, Disarm, Wounds`).* | Raw, unassisted civilian capability without technical technique (`11.1% whiff rate on 2d6 vs routine DC 3`). |
| **1. Trained** (`Basic Focus — 1 Allocation`) | **Pool Volume `3dX` (`+1B`)**<br>*(Rolls 3 dice of base Attribute size)* | **Floor = 3**<br>*(Guaranteed min face 3)* | **Immune to failing `DC 3 Routine` checks (`100%`).** Can trigger standard default maneuvers on `2+ Successes` (`Trip, Disarm, Shove`). | Professional competence (`e.g., proper edge alignment, basic diplomatic etiquette, or silent footwork`). |
| **2. Expert** (`Specialist — 2 Allocations`) | **Pool Volume `3dX` (`+1B`) + `1 Die Step-Up` (`X+1`)**<br>*(e.g., Attribute d8 $\to$ rolls `3d10`)* | **Floor = 5**<br>*(Guaranteed min face 5)* | **Immune to failing `DC 5 Challenging` checks (`100%`).** Can execute `Called Shot Anatomical Wounds` (`3 Successes`). | Dedicated specialization (`e.g., veteran regional champion, master surgeon, or elite spy`). Surpasses basic physical limits via technique! |
| **3. Master** (`Grandmaster — 3 Allocations`) | **Pool Volume `4dX` (`+2B`) + `2 Die Step-Ups` (`X+2`)**<br>*(e.g., Attribute d8 $\to$ rolls `4d12`)* | **Floor = 7**<br>*(Guaranteed min face 7)* | **Immune to failing `DC 7 Formidable` checks (`100%`).** Unlocks `Whirlwind Strike [3A]` and `Shatter Absorption` multi-beats. | Realm-renowned grandmastery. The character's technique is so precise they literally never miss formidable obstacles (`Floor 7`). |
| **4. Legendary** (`Mythic Apex — 4 Allocations`)| **Pool Volume `5dX` (`+3B`) + `3 Die Step-Ups` (`X+3`)**<br>*(e.g., Attribute d8 $\to$ rolls `5d12 over-cap`)* | **Floor = 9**<br>*(Guaranteed min face 9)* | **Immune to failing `DC 9 Heroic` checks (`100%`).** All standard hits in this specific skill automatically gain `+1 Multi-Success beat` for free! | Mythic mortal apex (`DEC-014`). Multiversal legends whose skills reshape physical, social, or arcane reality across the planes. |

---

## 4. Concrete Examples (`Specific Skill Checks in Action`)

To see how our 5-Block high fantasy setup (`Race + Background + Class + Skills + Feats`) and specific skill competency ranks operate without arithmetic, look at these four real-time checks across our domains:

### 4.1 Subterfuge Check (`Level 6 Expert Rogue vs. DC 7 Formidable Mechanical Lock`)
- **Character Setup:** Level 6 Elven Rogue (`AGI d10, DEX d10, INT d8`). Background: `Street Urchin (`Primary DEX d10`)`. Class: `Rogue (`Okay BAB, Good Skill Allocations — DEC-035`)`.
- **Specific Skill Investment:** Invested 2 skill allocations into **`Lockpicking`** $\to$ **`Expert Rank (+1B, +1 Die Step-Up, Floor 5)`**. *(Note: She left `Trap Disarming` at `Trained Floor 3` and `Sailing` at `Untrained Floor 0`!)*
- **Rolling the Check (`Zero Math`):** Her base `DEX` is `d10`. Because she is an `Expert` in *Lockpicking*, her die size steps up (`d10` $\to$ `d12`), and she gains `+1B` volume (`2d` $\to$ `3d`). She rolls **`3d12 keep highest (Floor 5)` vs `DC 7`**.
- **Outcome:** She rolls `4, 8, 11`. Highest face is `11` (`11 >= DC 7 -> Success!`). Furthermore, because `8` also beats `7`, she achieves **2 Successes (`Multi-Beat Complex Check — DEC-036`)**, picking the complex lock in half the time without making a sound!

### 4.2 Social Check (`Level 10 Master Paladin vs. Hostile King's Willpower Defense Pool`)
- **Character Setup:** Level 10 Human Paladin (`STR d10, CON d10, WIS d8, CHA d10`). Background: `High Noble (`Primary CHA d10, stepped up to d12 at Lvl 9`)`. Class: `Paladin (`Full Martial, Good Fort/Will`)`.
- **Specific Skill Investment:** Invested 3 allocations into **`Diplomacy`** $\to$ **`Master Rank (+2B, +2 Die Step-Ups, Floor 7)`**.
- **Rolling the Check (`Zero Math`):** His base `CHA` is `d12`. Because he is a `Master` in *Diplomacy*, his die steps twice (`d12` $\to$ `over-cap d12`), and he gains `+2B` volume (`2d` $\to$ `4d`). He rolls **`4d12 keep highest (Floor 7)`** directly against the King's opposed **Willpower Pool (`1dWIS + 1dCHA keep highest -> 2d10`)**.
- **Outcome:** The Paladin rolls `6, 9, 12, 14`. Because his Competency Floor is `7`, his `6` becomes `7`. The King rolls `4, 8`. The Paladin's `14` crushes the King's `8` (`Success!`). Because `12` and `9` *also* beat the King's `8`, the Paladin scores **3 Successes (`Overwhelming Social Dominance`)**, forging an immediate binding treaty and rallying the King's army to his cause right at the table!
