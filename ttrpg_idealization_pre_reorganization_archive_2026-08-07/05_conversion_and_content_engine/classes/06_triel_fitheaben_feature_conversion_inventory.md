# Triel Fitheaben — Feature Conversion Inventory

**Status:** Non-canonical conversion-design inventory.  
**Purpose:** Inventory Triel’s individual D&D 3.5e features before assigning final Actions, Reactions, Spell Slots, Essence, Stamina, Banes, Permissions, or exact effects. This file does not establish Class, Feat, spell, companion, or item content.

## 1. Current Framework Cost Vocabulary

Triel’s source sheet has an `AP 15` entry. The current framework does **not** have an Action Point meta-currency or point pool. It has:

```text
Actions:
  Normally 3 at the start of a Standard / Slow Turn.
  2 on a Fast Turn.

Reaction:
  1; refreshes at the start of the Actor’s own Turn.

Stamina:
  Physical exertion, active defense, martial amplification,
  and resource-based mitigation.

Essence:
  Spellcasting and supernatural exertion.

Spell Slots:
  Prepared-spell casting capacity.

Banes:
  Deliberate reliability trade-offs, where a specific procedure
  explicitly permits them.
```

The source `AP 15` is therefore **not carried forward** unless a later source-specific feature is found to need conversion into Actions, Stamina, Essence, Spell Slots, or an explicit item / Class resource.

### Conversion statuses

| Status | Meaning |
|---|---|
| **Direct framework fit** | The source concept already has a current rules anchor; the future entry mainly needs specific numbers, Tags, and eligibility. |
| **Convert through existing framework** | No new universal subsystem is needed, but the feature must be written as a Class / Feat / spell / item entry. |
| **Blocked by open content** | Depends on an unfinished catalogue or procedure, such as shields, companions, specific spells, or weapon values. |
| **Legacy effect removed** | The legacy rule does not carry forward because its job is replaced by existing framework or because it is a deprecated numerical layer. |

### 1.1 Feature conversion discipline

For this inventory, source feature names remain in use unless a replacement name has been explicitly approved. The conversion target should prefer a declared Action / Reaction, a broad Permission or Trait, a reusable Condition, or a short explicit duration over narrowly conditional persistent effects.

## 2. Cleric Chassis, Domains, and Granted Powers

| Source feature | Source effect / identity | Current framework anchor | Status | Likely entry and cost questions |
|---|---|---|---|---|
| Divine spellcasting | Prepared divine spell list and spell slots. | Shared Spell Slots; Tradition Skills; Spellcasting Activities. | Direct framework fit | Individual spells declare Actions, Slot, Essence, Tags, defenses, and duration. Preparation remains open. |
| Cleric Tradition access | Divine, Spirit, Life, Death, Good for Triel. | Canonical Cleric access model used in the exercise. | Direct framework fit | Class Skills / Class table access; no repeated resource cost. |
| War Domain | War Tradition; favored weapon benefits. | Domain Tradition Grant; Domain Feature package; Combat Mastery access. | Direct framework fit | War grants War at Trained; may grant Heavy Blades access and a stated martial Feature. |
| Healing Domain | Life access and healing identity. | Domain Tradition Grant; healing spell / Activity framework. | Direct framework fit | Life already accessible, so Healing grants Life’s one-Rank Domain Tradition Grant subject to cap; its separate healing Feature remains content. |
| Law Domain | Law access; source domain traded for Law Devotion. | Domain Tradition Grant; Law Tradition. | Direct framework fit | Law at Trained when gained; later Law Devotion is a separate Feature conversion. |
| Sun Domain | Sun spells and greater turning. | Domain Tradition Grant to Light; anti-undead Feature. | Convert through existing framework | Light at Trained when gained; define the source Destroy Undead / greater-turn effect directly. |
| Aura | Detectable alignment / divine presence. | Trait, Permission, or explicit detection Activity. | Convert through existing framework | Usually no Action / resource cost for merely possessing an Aura; detection procedure is content. |
| Heavy armor proficiency | Can wear heavy armor. | Heavy Armor category and Equipment Permission. | Direct framework fit | No resource cost; armor Traits / requirements still open. |
| Shield proficiency | Can use shields. | Shield equipment Permission; Shield Defense; Deflect. | Blocked by open content | Shield categories and detailed interactions remain open. |
| Simple weapon proficiency | Broad basic weapon use. | Weapon access Permission. | Convert through existing framework | Must map source weapons into the future weapon-category catalogue. |
| Turn / Destroy Undead (Lightbringer ACF) | Repel / destroy undead using divine power; Triel has Destroy Undead. | Explicit supernatural Activity; Light / Death / Divine; Willpower defense; Essence. | Convert through existing framework | Define Action cost, Essence or limited frequency, target area, resistance, destruction / condition outcome. No generic turning procedure exists yet. |
| Spontaneous cure conversion | Swap prepared spells into healing. | Shared preparation and spellcasting framework. | Blocked by open content | Decide whether this becomes a Healing Domain Permission, Life Feature, Slot substitution, or is omitted. |

## 3. Ordained Champion

| Source feature | Source effect / identity | Current framework anchor | Status | Likely entry and cost questions |
|---|---|---|---|---|
| Continued Advancement | Stacks for turning and domain powers. | Explicit Class-table / Feature progression. | Convert through existing framework | State exactly which Class Features treat OC levels as relevant levels; do not create generic stacking. |
| Bonus Domain — Law | Adds Law domain to Triel. | Domain Tradition Grant. | Direct framework fit | Law → Trained at OC 1; Law’s distinct Feature package. |
| Modified spontaneous casting | Trade ordinary spontaneous cure conversion for War-domain casting flexibility. | Spell preparation / acquisition Permission. | Blocked by open content | Needs a clear prepared-spell replacement rule; likely no Action cost beyond the replacement spell. |
| Combat feats | Gains selected martial feat access. | Feats. | Direct framework fit | Each selected Feat has its own procedure and cost. |
| Smite | Add Charisma to attack and effective turning level to damage against any foe. | Strike enhancer; Essence / Stamina expenditure; fixed Damage Boxes. | Convert through existing framework | Define Action timing (probably no extra Action, once per Strike), Essence or limited-use cost, Banes if any, and bonus Damage Boxes. |
| Channel Spell | Hold a target spell in a weapon; next successful Strike delivers it. | Spell Activity + weapon Permission + Strike. | Convert through existing framework | Spell Slot / Essence are spent on loading; define loading Action cost, eligible Tags, storage duration, miss handling, defense order, and discharge. |
| Divine Bulwark | Sacrifice spell slot for short-term damage reduction. | Damage Absorption, Ward Self, or temporary protection Feature. | Convert through existing framework | Spending a Slot is appropriate; define Action, duration, Damage Box prevention, stacking, and source / damage eligibility. |
| Diehard | Remains functional at negative HP. | Vitality 0 / Incapacitated / Wound framework. | Convert through existing framework | Cannot import negative HP. Must state a specific exception to unconsciousness, Wound, or Incapacitated consequences, if retained. |

## 4. Knight of the Raven

| Source feature | Source effect / identity | Current framework anchor | Status | Likely entry and cost questions |
|---|---|---|---|---|
| Raven harrier | Celestial raven companion that occupies / distracts targets. | Companion Actor; Assist; social / tactical Condition; future companion procedure. | Blocked by open content | Companion action economy, survival, command Action, and Actor stats are needed. |
| Harry | Raven distracts a target, lowering AC. | Command Activity; Distracted or Shaken; possibly a defense-related Bane. | Convert through existing framework | Likely 1 Action by Triel or raven; no default resource cost; target Willpower or relevant defense; duration one Round. |
| Baffle | Raven prevents target Attacks of Opportunity. | Explicit Condition / Permission denial. | Convert through existing framework | Command Action and Willpower defense are plausible; exact Condition needs entry. |
| Falter | Raven causes special opportunity exposure. | Attack of Opportunity and positioning permission. | Blocked by open content | Depends on companion positioning and final opportunity / movement procedures. |
| Speak with Ravens | Communicate with ravens. | Creature-language / communication Permission. | Direct framework fit | No ordinary resource cost; specific fictional scope. |
| Smite Undead | Divine Strike enhancer specifically against undead. | Strike enhancer; Light / Death / Divine; Essence; fixed Damage Boxes. | Convert through existing framework | No extra Action is likely; define Essence or limited-use cost, target Requirement, and Damage Boxes. |
| Turn Undead | Adds turning capacity. | Future Turn / Destroy Undead Activity. | Blocked by open content | It should modify the future procedure, not make a second parallel system. |
| Sun Domain | Adds Light access and Sun Feature. | Domain Tradition Grant → Light. | Direct framework fit | Light is Trained at KotR 3; the source Destroy Undead / greater-turn procedure remains content. |
| Light Focus | Improves Light-descriptor spells. | Spell Trait / Permission; Essence, Slot, or limited activation. | Convert through existing framework | The future spell Trait list must include Light; define one chosen enhancement per spell. |
| Enduring Life | Better survival at low HP. | Vitality 0 / Wound exception. | Convert through existing framework | Needs an explicit, limited exception; cannot import negative HP. |

## 5. Crusader and Martial Maneuvers

| Source feature | Source effect / identity | Current framework anchor | Status | Likely entry and cost questions |
|---|---|---|---|---|
| Steely Resolve | Delays / absorbs incoming damage in a delayed-damage pool. | Soften Blow, Vitality, Wounds, temporary reserve. | Convert through existing framework | Determine whether it is a passive temporary Damage Box buffer, a Stamina / Essence option, or a delayed harm Condition. It should not create hidden arithmetic. |
| Furious Counterstrike | Gains stronger offense while delayed damage accumulates. | Explicit conditional Boon, Automatic Success, or Damage Box Feature. | Convert through existing framework | Must be paired with the final Steely Resolve model; no generic +X attack bonus. |
| Martial Spirit stance | Successful melee Strikes heal self / ally. | Stance Feature; on-hit Vitality restoration. | Convert through existing framework | Define stance activation, whether ongoing stance costs Essence / Stamina, range, and Vitality amount. |
| Douse the Flames | Strike denies target opportunity attacks. | Strike variant; explicit Attack of Opportunity denial. | Convert through existing framework | Likely 1 Action Strike plus target Condition through next Turn. |
| Mountain Hammer | Strike deals extra damage and ignores hardness. | Strike variant; fixed Damage Boxes; item Durability / Sunder. | Blocked by open content | Requires item-hardness / Sunder procedure; may use Piercing only if it fits final item interaction. |
| Revitalizing Strike | Strike heals self / ally. | Strike variant; on-hit Vitality restoration. | Convert through existing framework | Action cost, target, and restoration amount needed. |
| White Raven Strike | Strike creates strong ally opening. | Strike variant; Rallied / command / ally Permission. | Convert through existing framework | Define the ally’s benefit without granting an extra Turn by default. |
| Divine Surge | High-damage Strike that harms / fatigues the user. | Strike enhancer; Essence; fixed Damage Boxes; self-cost or Condition. | Convert through existing framework | Ideal candidate for high Essence cost plus fatigue / self-damage or Banes; Action timing needed. |
| Extra Granted Maneuver / Martial Study / Martial Stance | More maneuver / stance access. | Feat and maneuver-access content. | Blocked by open content | Requires eventual maneuver-learning and readying framework; not a separate resource system. |

### Grapple note

Grapple is already a canonical 1-Action Martial Arts maneuver. Triel can attempt it while Untrained; the source’s BAB does not need a separate conversion. If the finalized Class lists or his universal Investments later grant Martial Arts access / Rank, that expresses improved grappling and unarmed control. No decision is made here to alter his Skill allocation.

## 6. Righteous Cohort of Kiri-Jolith

| Source feature | Source effect / identity | Current framework anchor | Status | Likely entry and cost questions |
|---|---|---|---|---|
| Fraternal Oath | Gains bonuses / capacity while serving with a unit. | Oath Trait; Leadership / Protection Feature; group Requirement. | Convert through existing framework | Likely passive while Requirements are met; exact allied-unit benefit must avoid linear bonuses. |
| Rallying Cry | Area morale / attack / movement boost for allies. | Rallied Condition; Leadership; Morale Boon; Movement Permission. | Direct framework fit | Likely 1 Action, likely Essence or limited frequency, targets allied Actors in stated range. |
| Lesser Aura of Discipline | Allies gain discipline / saving benefit. | Aura Trait; Morale / competence permission; Fortitude / Reflexes / Willpower interaction. | Convert through existing framework | Define range, eligible defense, and whether it grants a Boon or another explicit benefit; no numeric save bonus. |
| Empower Leader | Increasing leadership / rally power. | Improvement to Rallying Cry / aura Feature. | Convert through existing framework | Each Class-table step states a discrete improved effect, range, target count, or Permission. |
| Second Wind | Recover after heavy exertion. | Stamina recovery, Vitality restoration, or Wound / Condition relief. | Convert through existing framework | Likely explicit 1-Action or no-Action limited Feature; needs a resource target and frequency. |
| Bonus feat | Additional selected feat. | Feats. | Direct framework fit | Each chosen Feat supplies its own requirements and procedure. |

## 7. Feats, Devotions, and Equipment-Granted Features

| Source feature | Source effect / identity | Current framework anchor | Status | Likely entry and cost questions |
|---|---|---|---|---|
| Weapon Focus — Longsword | Better use of favored weapon. | Feat; Heavy Blades; weapon Requirement. | Convert through existing framework | Likely a specific Permission, limited Boon, or maneuver interaction; not a static +1. |
| Martial Weapon Proficiency | Can use longsword / martial weapon. | Equipment / weapon Permission. | Direct framework fit | Weapon catalogue determines actual category and Requirement. |
| Power Attack | Trade accuracy for damage. | Canonical Power Attack. | **Works as is** | No conversion needed: no Action; Stamina X; X Banes; +X Damage Boxes before Absorption. |
| Parrying Shield | Special shield defense. | Shield / Deflect / possibly countering Feature. | Blocked by open content | Needs shield-category rules and exact feat effect. |
| Law Devotion | Temporary law-themed attack / defense bonus. | Law Feature; Boon type; Essence / limited uses. | Convert through existing framework | Pick one temporary lawful mode with explicit Boon, defense, or Permission; define activation and duration. |
| Extra Turning | More Turn attempts. | Future Turn / Destroy Undead Feature. | Blocked by open content | Likely additional uses or reduced Essence cost only after the base Destroy Undead procedure exists. |
| Extend Spell | Longer spell duration. | Metamagic; Spell Slot and / or Essence. | Convert through existing framework | Needs final duration and metamagic procedure. |
| Persist Spell / Divine Metamagic — Persist | Very long spell duration fueled by turning. | Sustained spell entries; metamagic; Essence or explicit Destroy Undead resource. | Blocked by open content | No blanket import. Requires a specific long-duration metamagic procedure and anti-stacking limits. |
| Practiced Spellcaster | Raises legacy caster level. | No direct caster-level statistic. | Legacy effect removed | Some desired scaling may be explicit Class / spell Permission, but no generic conversion. |
| Holy Warrior | Damage from highest War-domain spell available. | War Tradition / Feature; fixed Damage Boxes. | Convert through existing framework | Could scale by War Rank or highest accessible Circle; needs calibration. |
| Collector of Stories | Bonuses to lore / monster knowledge. | Lore / Knowledge Activity; Competence Boon or Permission. | Convert through existing framework | Likely a Knowledge / Lore Permission or Competence Boon in defined circumstances. |
| Dragon Cohort | Dragon companion / follower. | Companion / cohort subsystem. | Blocked by open content | Requires companion leadership, Actor construction, and campaign-control rules. |

### Deferred item scope

The Gauntlets of War / Sacred Item and keen returning longsword are deliberately out of the active conversion scope. Item and weapon conversion resumes only after the feature pass and relevant equipment procedures are ready.

## 8. Spells Are Separate Content Entries

Triel’s prepared spells are not treated as Class Features. Each must later be converted as its own spell record with:

```text
School
Tradition(s)
Traits
Action cost
Spell Slot
Essence cost, if any
Target / area / duration
Defense
Damage Boxes, Conditions, healing, or other effect
```

The most useful first representative spells from his sheet are:

```text
Healing / recovery:
  Cure Moderate Wounds, Restoration, Heal, Delay Death.

Martial blessings:
  Magic Weapon, Divine Power, Holy Transformation, Righteous Wrath.

Protection:
  Protection from Evil, Freedom of Movement, Death Ward.

Divine offense:
  Spiritual Weapon, Flame Strike, Blade Barrier, Sunbeam, Holy Word.

Leadership / expedition:
  Recitation, Hero's Feast, Valiant Steed.
```

## 9. First Conversion Candidates

The best first entries are those with strong existing anchors and limited dependency risk:

1. **Power Attack** — already works as written.
2. **War Domain package** — Domain Tradition Grant, Heavy Blades access, then a modest martial Feature.
3. **Rallying Cry** — use the existing Rallied Condition and Morale Boon vocabulary.
4. **Smite Undead** — one target Requirement, an Essence cost, and fixed Damage Boxes.
5. **Channel Spell** — validates spell + Strike integration.
6. **Destroy Undead** — validates Light, Death, and Willpower interaction without inventing a replacement name.
7. **Martial Spirit or Revitalizing Strike** — validates limited on-hit Vitality recovery.

The blocked entries—companions, detailed shields, Sunder / hardness, broad metamagic, and persistent spell infrastructure—should not be used to silently define their missing subsystems.
