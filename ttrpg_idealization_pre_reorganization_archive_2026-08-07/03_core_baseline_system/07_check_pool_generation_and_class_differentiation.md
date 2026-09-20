# Check-Pool Generation and Class Differentiation

**Status:** Canonical statistical relationship framework.  
**Scope:** Explains which progression vectors affect Die Size, pool volume, Floors, and permissions. The universal rolling procedure belongs to `01_resolution_engine.md`.

## 1. Core Pool Variables

A final check is described by three primary variables:

```text
Die Size (X)
Baseline Dice Pool Size
Final Dice Pool Size
```

### Die Size

Die Size represents the relevant Attribute’s capability ceiling:

```text
d4 → d6 → d8 → d10 → d12
```

Attribute advancement, relevant Competency Step-Ups, equipment, spells, or specific Permissions may affect Die Size. Ordinary resolution does not exceed d12.

### Pool Volume

Pool Volume represents the number of dice rolled. It is affected by Competency Rank, Boons, Banes, Class features, Feats, Equipment, tactics, and other explicit effects.

The ordinary natural pool is generally `1dX` to `6dX`, with `6dX` representing Legend Competency or equivalent content. Content may exceed the natural range through explicit high-tier effects, but such effects are controlled by their granting content.

### Final Dice Pool

Competency Rank establishes baseline Dice Pool Size. Boons, Banes, Equipment, Feats, Spells, tactics, and other explicit effects modify the final Dice Pool. The final Dice Pool is used directly by the Difficulty Vector or opposed procedure. There is no separate Competency Floor mechanic.

### Paired Defense Class Tracks

A Class defense track uses the same Good, Medium, and Bad Rank cadence as protected Skill progression. A paired defense uses the highest of its two paired Attribute Dice as die size and the assigned defense track’s Rank as baseline Dice Pool size. The cadence is owned by `06_leveling_and_tier_progression.md`.


## 2. Progression-Vector Separation

| Source | Primary mathematical job |
|---|---|
| Attribute | Die Size and capability ceiling |
| Competency Rank | Baseline Dice Pool |
|---|---:|
| Untrained | 1dX |
| Trained | 2dX |
| Veteran | 3dX |
| Master | 4dX |
| Hero | 5dX |
| Legend | 6dX |
| Class/Prestige Class | Class features, protected primary competency, Spell Slot Advancement, and permissions |
| Feat | Discrete permissions, actions, traits, and specialized effects |
| Equipment | Material capability, Damage Absorption, Traits, durability, and explicit permissions |
| Tactics and circumstances | Boons, Banes, actions, positioning, and conditions |
| Stamina/Essence | Content-specific exertion and supernatural permissions |

No source should silently duplicate another source’s job through linear modifiers.

## 3. Universal Resolution Reference

For the actual procedure for assembling and resolving a pool, see:

```text
01_resolution_engine.md
```

That document owns:

- Natural Dice Pool and Enhanced Dice Pool.
- Boons and Banes.
- Die Step-Up and Die Step-Down.
- Competency Floors.
- Difficulty Classes.
- Required Successes.
- Opposed rolls and Defender Wins Ties.
- Automatic Successes.

## 4. Class and Actor Differentiation

Classes, Prestige Classes, Ancestries, Feats, Equipment, and Monsters differentiate actors through the progression vectors above rather than through incompatible resolution engines.

A Fighter, Wizard, Ogre, and Dragon may have different Attributes, Skills, Traditions, Equipment, and Permissions, but their uncertain actions still use the same universal pool procedure.

## 5. Current Scope Boundary

This file describes the statistical model only. Final probability targets, equipment scaling, high-tier pool expansion, and detailed class/content effects remain tracked in the Phase 1 Checklist and Outstanding Definitions Index.
