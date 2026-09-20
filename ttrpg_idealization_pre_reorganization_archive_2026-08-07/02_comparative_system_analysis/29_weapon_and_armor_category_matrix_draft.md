# Weapon and Armor Category Matrix — Fixed Damage Draft

**Status:** Research and design draft; non-canonical.  
**Purpose:** Propose a compact fixed-Damage-Box weapon and armor category matrix using the current Combat Mastery Skills, Package 3 from `28_fixed_damage_and_armor_design_catalogue.md`, the uploaded weapon-design research, and D&D 3.5e weapons/armor as a compatibility sanity check.

This document does not establish weapon categories, Damage Box values, Traits, armor values, or shield rules.

## 1. Design Constraints

```text
Weapons and damaging effects use fixed Damage Boxes.
Armor uses post-hit Damage Absorption.
Weapon and armor identity should come from a compact combination of:
  Combat Mastery Skill;
  fixed Damage Box band;
  handling and reach properties;
  selected damage and weapon Traits;
  maneuver permissions.

Do not preserve a D&D 3.5e entry merely because it has a separate name.
Preserve it only when it has a distinct play pattern.
```

## 2. Proposed Damage and Armor Language

### Damage and Weapon Traits

The Tag / Trait taxonomy is canonical in the framework glossary. This draft does not select a complete physical damage-family list. Piercing is a persistent Trait that gives an Attack the Piercing Attack Tag and guarantees at least 1 Damage Box after Damage Absorption.

Possible future physical damage Traits or Tags such as Bludgeoning and Slashing remain research questions until an explicit rule requires them.

### Handling and Tactical Traits

The project already identifies these as Trait-level rather than Skill-level differentiation:

```text
Finesse
Throwable
Reach
Sweep
Forceful
Loading
Fatal
```

This draft additionally uses the following descriptive placeholders where needed:

```text
Two-Handed
Concealable
Parrying
Penetrating
Shield
Nonlethal
Entangling
Double
```

Whether each placeholder becomes a final universal Trait remains open.

## 3. Proposed Weapon Category Matrix

The Damage Box values below are a **candidate calibration range** for later simulation, not a rule.

| Category | Combat Mastery Skill | Draft Damage Boxes | Core Tags / permissions | D&D 3.5e sanity-check examples | Folded redundancy |
|---|---|---:|---|---|---|
| Unarmed | Martial Arts | 1 | Bludgeoning, Nonlethal by default; may Grapple | Unarmed strike, gauntlet, spiked gauntlet, kama, nunchaku | All basic fist/gauntlet variants; special versions become Traits or Feats |
| Dagger | Light Blades | 1 | Piercing or Slashing, Finesse, Throwable, Concealable | Dagger, punching dagger, sai, siangham, shuriken | Darts and small thrown knives become ranged/Throwable variants |
| Light Blade | Light Blades | 2 | Piercing or Slashing, Finesse, Parrying | Shortsword, rapier, scimitar, kukri, sickle | D&D critical-range differences become later Critical/Trait content |
| Sword | Heavy Blades | 2 | Slashing, Parrying; optional Piercing mode for a suitable weapon | Longsword, bastard sword, waraxe-like sword equivalents | Longsword/bastard sword/arming sword distinctions become one-handed/Two-Handed or exotic permissions |
| Greatblade | Heavy Blades | 3 | Slashing, Two-Handed, Forceful | Greatsword, falchion, two-bladed sword used as one weapon | Most two-handed sword variants; Double is a separate Trait if retained |
| Spear | Polearms and Spears | 2 | Piercing, Reach or Throwable configuration; may Set against Charge later | Shortspear, spear, trident, javelin | Short/long/thrown spear variants become Reach, Throwable, hand, and range configurations |
| Polearm | Polearms and Spears | 3 | Two-Handed, Reach, Sweep; may have Piercing or Slashing Tag | Glaive, guisarme, halberd, ranseur, longspear | Individual hook/trip/disarm distinctions become optional weapon Traits |
| Axe | Axes and Picks | 2 | Slashing, Forceful; optional Throwable configuration | Handaxe, battleaxe, throwing axe | Hand/battle/throwing distinctions become hand use, Two-Handed, and Throwable Traits |
| Pick | Axes and Picks | 2 | Piercing, Penetrating, Forceful | Light pick, heavy pick, war pick | Critical multiplier differences become Penetrating / Critical content |
| Mace or Hammer | Hammers, Maces, and Flails | 2 | Bludgeoning, Forceful | Club, light/heavy mace, warhammer, light hammer | Club/mace/hammer differences become material, hand use, and Forceful variants |
| Maul | Hammers, Maces, and Flails | 3 | Bludgeoning, Two-Handed, Forceful | Greatclub, maul, heavy hammer | Greatclub/maul differences become material and Trait variations |
| Flail | Hammers, Maces, and Flails | 2 | Bludgeoning, Flexible; later Disarm/Trip permission | Flail, heavy flail, dire flail | One/two-handed and double versions become handling/Double variants |
| Staff | Polearms and Spears or Martial Arts | 1 | Bludgeoning, Parrying, Double; optional Reach | Quarterstaff, bo staff | Staff variants; exact Skill assignment remains open |
| Bow | Archery | 2 | Piercing, Two-Handed, Loading; range configuration | Shortbow, longbow, composite bows | Short/long/composite distinctions become range, Strength/Forceful, and material variations |
| Crossbow | Archery | 3 | Piercing, Two-Handed, Loading; range configuration | Light, heavy, hand, repeating crossbows | Hand/repeating distinctions become one-hand, magazine, and loading Traits |
| Sling | Archery | 1 | Bludgeoning, Loading, range configuration | Sling | Distinct category remains because its ammunition and damage type differ from bow/crossbow |
| Shield Bash | Shield Defense | 1 | Bludgeoning, Shield; uses shield as a weapon under its own later procedure | Light/heavy/spiked shields | Shield size becomes defensive category; spikes become Piercing Trait |
| Exotic weapon | Exotic Weapons | Varies | Explicit special Trait package | Whip, spiked chain, net, bolas, double weapons | Only retain a separate entry when the Trait package cannot be built from baseline categories |

## 4. D&D 3.5e Compatibility Compression

The following D&D 3.5e distinctions should usually survive as properties rather than individual weapon entries.

| D&D 3.5e distinction | Project compression |
|---|---|
| Simple / Martial / Exotic proficiency | Combat Mastery Skill access, Class/Feat Permission, or Exotic Weapons Skill |
| Light / one-handed / two-handed | Handling Traits and Action / Manipulate requirements |
| Weapon damage die | Fixed Damage Box band |
| Critical threat range / multiplier | Future Critical Threat Profile or weapon Trait |
| Bludgeoning / piercing / slashing | Damage Tags |
| Reach weapon | Reach Trait |
| Thrown weapon | Throwable Trait plus range configuration |
| Trip / disarm weapon | Explicit maneuver permission Trait |
| Double weapon | Double Trait, if later retained |
| Nonlethal weapon | Nonlethal Trait |
| Special monk weapon | Martial Arts Permission or Class feature |
| Weapon finesse eligibility | Finesse Trait |
| Set against charge | Future Set Trait / Charge interaction |

## 5. Armor Category Matrix

### Proposed armor bands

| Armor band | Draft Damage Absorption | Existing / proposed trade-offs | D&D 3.5e sanity-check entries | Folded redundancy |
|---|---:|---|---|---|
| Unarmored | 0 | Full Evasion access | No armor | — |
| Light Armor | 2 | No inherent Evasion Bane | Padded, leather, studded leather, chain shirt | Specific material, stealth, cost, and body-coverage distinctions stay content-level |
| Medium Armor | 3 | May carry selected Manipulate, Movement, stealth, or environmental trade-offs | Hide, scale mail, chainmail, breastplate | Specific material and body-coverage distinctions stay content-level |
| Heavy Armor | 4 | Heavy Armor: 1 Bane to Evasion; may add other specific trade-offs later | Splint mail, banded mail, half-plate, full plate | Full plate is a foremost example; distinguish entries through materials, Durability, and special Traits |
| Natural Armor | 1–3+ | Uses the same Damage Absorption interface but states its own tags, vulnerabilities, and exceptions | Creature hide, scales, shell, chitin | Creature-specific content |

### Shield categories

| Shield category | Draft role | D&D 3.5e sanity-check examples | Open decision |
|---|---|---|---|
| Buckler | Shield Deflect Boon with minimal hand commitment | Buckler | Can it support Manipulate or a two-handed weapon? |
| Light Shield | Shield Deflect Boon; possible Shield Bash | Light wooden/steel shield | Does it add Damage Absorption, and under what trigger? |
| Heavy Shield | Shield Deflect Boon; stronger Interpose / cover / bash identity | Heavy wooden/steel shield | What differentiates it from a light shield without changing Deflect’s universal +1 Boon? |
| Tower Shield | Cover and position-control item, not merely a stronger Deflect source | Tower shield | Exact cover, Movement, Manipulate, and attack restrictions |

## 6. Candidate Package 3 Implementation

The current best-fit package is:

```text
Core:
  Fixed weapon Damage Boxes.
  Flat post-hit armor Damage Absorption.
  Shield Boon to Deflect.
  Heavy Armor Bane to Evasion.

Selective differentiation:
  Damage Tags.
  Reach, Finesse, Throwable, Forceful, Loading, Sweep, and similar Traits.
  Selective Penetrating / Armor-Piercing effects.
  Explicit maneuver permissions.
  Creature-specific natural armor and vulnerability clauses.

Deferred:
  Routine Durability attrition.
  Comprehensive damage-type matchup tables.
  Full body-location armor coverage.
```

## 7. Calibration Questions

1. Are the proposed 1/2/3 Damage Box bands correct for ordinary weapons, with 4+ reserved for exceptional effects, siege weapons, or large monsters?
2. Are 0/1/2/3 Absorption bands correct for unarmored, soft, reinforced, and heavy armor?
3. Can Damage Absorption reduce an Attack to 0 Damage Boxes? The current draft assumes yes; Soften Blow’s one-Box floor applies only after an Attack has remaining damage.
4. Which of Penetrating, Armor-Piercing, Forceful, Flexible, Parrying, Double, Nonlethal, and Entangling should become baseline Traits?
5. Does Shield category alter only positioning and permissions, or does it alter Damage Absorption as well?
6. Should crossbows deal 3 Boxes because Loading balances them, or should all ordinary ranged weapons remain at 2 Boxes?
7. Is Staff best governed by Polearms and Spears, Martial Arts, or a Class/Feat Permission?
8. Which D&D 3.5e weapons deserve individual exceptions after category compression: whip, net, spiked chain, double weapons, bolas, lance, and shield spikes?

## 8. Inputs and Sources

- Current Combat Mastery Skills: `../03_core_baseline_system/09_domains_skills_activities_and_crafting.md`
- Fixed damage and armor research: `28_fixed_damage_and_armor_design_catalogue.md`
- Uploaded weapon-design research: `../uploads/TTRPG Weapon Design.md`
- Uploaded D&D 3.5e weapon/armor reference: `../uploads/D&D 3.5e Weapons and Armor.md`
- PF2e item Hardness: <https://2e.aonprd.com/Rules.aspx?ID=195>
- Mythras armor-point reference: <https://www.reddit.com/r/Mythras/comments/126wm3i/equipment_hp/>
- Dragonbane Armor Rating: <https://anyflip.com/ksvio/rnah/basic/51-100>
- Year Zero fixed weapon ratings: <https://www.weylan-yutani.com/year_zero_engine>
