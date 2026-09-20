# TTRPG & Tactical Game Architectural Analysis Matrix (v4 Master Expanded)

This document serves as our definitive architectural analysis of **23 tabletop roleplaying games and hybrid tactical board games**. It expands upon our previous reference matrices by integrating our primary and secondary anchors (**D&D 3.5e**, **Pathfinder 2e**, **Shadow of the Demon Lord / Weird Wizard**), board game engines (**Gloomhaven**, **Lands of Evershade**), and our newest simulationist cornerstone: **Mythras (BRP / $d100$ System)**.

Furthermore, we expand our analysis template from 14 to **Eighteen Vectors of Analysis** across all systems, introducing: *Vector 15 (Opposed Differential & Maneuver Triggers)*, *Vector 16 (Active Defense Action Economy)*, *Vector 17 (Hit Location Granularity & Wound Severance)*, and *Vector 18 (GM Cognitive Load & Mob Scaling)*.

---

## 1. Master Category Mapping across 23 Reference Systems

| Category | Contains | Boundary Rule |
| :--- | :--- | :--- |
| **meta** | Sheet/system metadata | Would change if porting to different system/campaign |
| **identity** | Biographical, descriptive | Static description with no direct mechanical rating |
| **attributes** | Core innate stats | Fundamental ratings, rarely change through play |
| **skills** | Learned/developed capabilities | Improve through use/advancement, rolled for actions |
| **resources** | Pools, tracks, conditions | Fluctuates during play; spent/recovered |
| **features** | Discrete capabilities | You have it or you don't (though may have sub-properties) |
| **inventory** | Physical possessions | Tangible things the character owns |
| **connections** | Relationships to entities | Links to NPCs, factions, PCs, organizations |
| **narrative** | Story with mechanical hooks | Text that gets USED mechanically during play |
| **progression** | Advancement state | Tracks growth; actual gains go to their respective categories |
| **resolution_engine** | Dice/Card engine & math load | How actions are randomized and evaluated against targets |
| **defense_model** | Mitigation & armor mechanics | How attacks are avoided, deflected, or absorbed |
| **meta_currency** | Out-of-world vs in-world fuel | Whether player tokens or character stamina power abilities |
| **extensibility** | Modular content architecture | How feats, spells, and items plug into the baseline engine |
| **NEW: differential_maneuvers**| Opposed success level outcomes | How differential roll results trigger tactical maneuvers |
| **NEW: defense_economy** | Action cost of defending | Whether defense is passive or consumes active turn economy |
| **NEW: hit_locations** | Anatomical vs global damage | Whether damage targets localized limbs or a global HP pool |
| **NEW: mob_scaling** | Minion / Rabble architecture | How the engine reduces GM tracking for large enemy groups |

---

## 2. Detailed Data Schema Mappings by Category (Including Mythras)

### Meta
*   **All Games:** `system_id`, `system_version`, `schema_version`, `created_at`, `modified_at`, `player_name`, `campaign_name`.
*   **Ars Magica:** `saga_name`, `covenant_name`, `current_year`, `current_season`.
*   **Scum and Villainy:** `crew_reference` (link to shared crew sheet).
*   **Burning Wheel:** `campaign_belief_artha_log` (optional).
*   **D&D 3.5e:** `campaign_setting`, `edition_3_5`, `splatbook_sources_allowed[]`.
*   **Pathfinder 2e:** `pfs_number`, `society_faction`, `rarity_access_level`.
*   **Shadow of the Demon Lord:** `chronicle_name`, `group_patron`.
*   **Gloomhaven:** `party_name`, `campaign_sheet_reference`, `prosperity_level`.
*   **Lands of Evershade:** `chronicle_book`, `story_act`, `lead_character_slot`.
*   **NEW — Mythras:** `culture_origin`, `career_path`, `cult_brotherhood_membership`, `magic_tradition`.

### Identity
*   **Kids on Bikes:** name, age_bracket, trope, physical_description.
*   **Burning Wheel:** name, stock, lifepath_summary, age, appearance.
*   **Ars Magica:** name, house, birth_year, apparent_age, gender, nationality, covenant_role.
*   **Ryuutama:** name, class, type, hometown, appearance, favorite_thing, personal_item.
*   **Twilight 2000:** name, nationality, branch, rank, age, appearance, big_dream.
*   **Call of Cthulhu:** name, occupation, age, birthplace, residence, portrait, player.
*   **Sword of Serpentine:** name, ancestry, concept, appearance.
*   **Scum and Villainy:** name, alias, playbook, heritage, background, look.
*   **Fate Core:** name, description, high_concept_label.
*   **Pathfinder 1e:** name, race, class_levels[], alignment, deity, age, height, weight, appearance.
*   **Apocalypse World:** name, look, playbook.
*   **Vampire V5:** name, concept, ambition, desire, clan, generation, sire, predator_type.
*   **Cypher System:** name, descriptor, type, focus, portrait, background.
*   **Genesys:** name, species, career, portrait, notable_features.
*   **GURPS:** name, race/species, tech_level, cultural_background, appearance.
*   **Troika!:** name, background_name, appearance.
*   **Castle Falkenstein:** name, social_rank, nationality, profession, appearance, diary_title.
*   **D&D 3.5e:** name, race, class_levels_and_prestige[], alignment, deity, size_category, age, appearance.
*   **Pathfinder 2e:** name, ancestry, heritage, background, class, size, alignment/edicts, deity.
*   **Shadow of the Demon Lord:** name, ancestry, age, build, appearance, personality, background_detail.
*   **Gloomhaven:** character_name, class_archetype, personal_quest_summary.
*   **Lands of Evershade:** name, origin_story, character_archetype, personal_destiny_card.
*   **NEW — Mythras:** name, gender, age, culture (`Barbarian, Civilized, Nomadic, Primitive`), social_class, family_background.

### Attributes (Core Innate Stats)
*   **Kids on Bikes:** Brains, Brawn, Fight, Flight, Charm, Grit (`d4`-`d20`).
*   **Burning Wheel:** Will, Perception, Power, Forte, Agility, Speed (Numeric 1-8 + Shade).
*   **Ars Magica:** Int, Per, Pre, Com, Str, Sta, Dex, Qik (Numeric -3 to +5).
*   **Ryuutama:** STR, DEX, INT, SPI (`d4`-`d12`, paired for rolls).
*   **Twilight 2000:** Strength, Agility, Intelligence, Empathy (`d6`-`d12`).
*   **Call of Cthulhu:** STR, CON, SIZ, DEX, APP, INT, POW, EDU (Numeric 15-90).
*   **Sword of Serpentine:** None (uses abilities only).
*   **Scum and Villainy:** Insight, Prowess, Resolve (Derived 0-4).
*   **Fate Core:** None (Approaches in FAE: Careful, Clever, Flashy, Forceful, Quick, Sneaky).
*   **Pathfinder 1e:** Str, Dex, Con, Int, Wis, Cha (Numeric 3-18+, modifier = `floor((N-10)/2)`).
*   **Apocalypse World:** Cool, Hard, Hot, Sharp, Weird (-2 to +3).
*   **Vampire V5:** Physical, Social, Mental attributes (Dots 1-5).
*   **Cypher System:** Might, Speed, Intellect (Numeric pool max, Edge).
*   **Genesys:** Brawn, Agility, Intellect, Cunning, Willpower, Presence (1-5).
*   **GURPS:** Strength, Dexterity, Intelligence, Health (Numeric 1-20+).
*   **Troika!:** Skill, Stamina, Luck.
*   **Castle Falkenstein:** None (Abilities only).
*   **D&D 3.5e:** Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma (Numeric score 3-30+).
*   **Pathfinder 2e:** Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma (Attribute Modifiers `-1` to `+7`).
*   **Shadow of the Demon Lord:** Strength, Agility, Intellect, Will (Numeric score 8-15+).
*   **Gloomhaven:** Hand Size (Card limit), Max Hit Points (scales by class level).
*   **Lands of Evershade:** Might, Agility, Insight, Spirit (`d4` to `d12` step ratings).
*   **NEW — Mythras:** Strength (`STR`), Constitution (`CON`), Size (`SIZ`), Dexterity (`DEX`), Intelligence (`INT`), Power (`POW`), Charisma (`CHA`) (`3d6` / `2d6+6` scale 3-18+; derives Action Points, Damage Modifier, Initiative, and localized HP).

### Skills (Learned/Developed Capabilities)
*   **Kids on Bikes:** None.
*   **Burning Wheel:** Flat list with roots (Exponent 1-10 + Shade, 200+ skills).
*   **Ars Magica:** Abilities (0-10+), Techniques + Forms (Arts; 0-40+).
*   **Ryuutama:** Fixed list (~12 skills).
*   **Twilight 2000:** Grouped under attributes (`d6`-`d12`, 12 total).
*   **Call of Cthulhu:** Flat list (Percentile 0-99, 60+ skills).
*   **Sword of Serpentine:** Investigative + General (Pool points, ~20 skills).
*   **Scum and Villainy:** Actions under attributes (Dots 0-4, 12 actions total).
*   **Fate Core:** Flat or pyramidal list (Ladder +0 to +4, 18 skills).
*   **Pathfinder 1e:** Flat list (Ranks 0 to level, 35 skills).
*   **Apocalypse World:** None (uses moves instead).
*   **Vampire V5:** Flat list (Dots 0-5, 27 skills).
*   **Cypher System:** Flat list (Trained/Specialized binary tiers).
*   **Genesys:** Flat list linked to attributes (Ranks 0-5, ~30 skills).
*   **GURPS:** Flat list (Numeric, cost based on difficulty and attribute; 100+ skills).
*   **Troika!:** Freeform + background-granted (Numeric 1-6+).
*   **Castle Falkenstein:** Abilities (Card rank Poor to Extraordinary, 20+ abilities).
*   **D&D 3.5e:** Class & Cross-class skill list (Skill Ranks up to `Level + 3`).
*   **Pathfinder 2e:** Core Skill List (Proficiency Tiers: Untrained `+0`, Trained `+2+Lvl`, Expert `+4+Lvl`, Master `+6+Lvl`, Legendary `+8+Lvl`).
*   **Shadow of the Demon Lord:** Professions instead of fixed skills (`+Boon` on attribute checks).
*   **Gloomhaven:** None (Actions are determined by specific ability cards in hand).
*   **Lands of Evershade:** Action Mastery domains (`Combat, Navigation, Social, Crafting`).
*   **NEW — Mythras:** Standard Skills (`Athletics, Evade, Perception, Stealth, Brawn`) + Professional Skills (`Lore, Commerce, Mechanisms, Crafting`) + **Combat Styles (`Sword & Shield 65%, Spearmanship 70%`)**. All rated as percentile numbers (`0% to 100%+`).

### Resources (Depletable Pools, Tracks, & Conditions)
*   **Kids on Bikes:** Adversity Tokens.
*   **Burning Wheel:** Artha, Tax (magic fatigue), Wounds track.
*   **Ars Magica:** Fatigue levels, Wounds track, Confidence pool, Warping total, Vis.
*   **Ryuutama:** HP, MP, Conditions, Carrying Capacity slots.
*   **Twilight 2000:** Hit Capacity, Stress, Radiation exposure, Critical Injuries, Ammo.
*   **Call of Cthulhu:** HP, MP, Sanity, Luck.
*   **Sword of Serpentine:** Health, Morale, Sway, Investigative Pools.
*   **Scum and Villainy:** Stress (0-9), Trauma boxes, Harm slots, Armor uses.
*   **Fate Core:** Physical Stress, Mental Stress, Consequences slots, Fate Points.
*   **Pathfinder 1e:** HP, Nonlethal damage, Spell Slots, Class Resources, Conditions flags.
*   **Apocalypse World:** Harm clock, Barter units, Hold points.
*   **Vampire V5:** Health, Willpower, Hunger (0-5), Humanity, Stains.
*   **Cypher System:** Might Pool, Speed Pool, Intellect Pool, Recovery Rolls.
*   **Genesys:** Wounds threshold, Strain threshold, Critical Injuries, Story Points.
*   **GURPS:** HP, FP (Fatigue), Conditions flags.
*   **Troika!:** Stamina, Luck, Provisions.
*   **Castle Falkenstein:** Wounds track, Cards in hand.
*   **D&D 3.5e:** Hit Points, Vancian Spell Slots, Daily Use class features, Temporary HP, Exhaustion/Fatigue flags.
*   **Pathfinder 2e:** Hit Points, Focus Points (Max 3), Spell Slots, Hero Points (0-3), Condition levels (`Clumsy 1-3`, `Frightened 1-4`).
*   **Shadow of the Demon Lord:** Health, Damage taken, Insanity, Corruption, Fortune token, Daily spell/talent castings.
*   **Gloomhaven:** Current HP, Active Hand Cards, Discarded Cards, Lost/Burned Cards, Active Conditions (`Poison`, `Stun`, `Muddle`).
*   **Lands of Evershade:** Vitality (HP), Stamina (Effort spend), Fate tokens, Exhaustion counters.
*   **NEW — Mythras:** Action Points (`AP: 2 to 3`), Magic Points (`MP`), Fatigue levels (`Fresh to Exhausted/Debilitated`), Luck Points (`2 to 3`), **7 Localized Hit Location Tracks (`Head, Chest, Abdomen, Left/Right Arm, Left/Right Leg`)** each with `Minor, Serious, Major` thresholds.

### Features (Discrete Binary Capabilities)
*   *(Same 17 base reference systems + 3.5e Feats, PF2e Feats, SotDL Paths, Gloomhaven Ability Cards, Lands of Evershade Talents).*
*   **NEW — Mythras:** Cult / Brotherhood Gifts, Magic Traditions (`Folk Magic, Animism, Mysticism, Sorcery, Theism` spells/miracles), Combat Style Traits (`Shield Wall, Skirmisher, Mounted Combat`). Crucially: **Combat Maneuvers (`Special Effects`) are NOT listed under Features** because every character possesses full universal access to them by default!

---

## 3. The Four Core Analytical Vectors (`Vectors 11 to 14`)

*(Summary comparison across key systems including Mythras)*

| System | Vector 11: Resolution Engine & Arithmetic Load | Vector 12: Defense & Mitigation Model | Vector 13: Meta-Currency Dependency | Vector 14: Content Extensibility |
| :--- | :--- | :--- | :--- | :--- |
| **D&D 3.5e** | $1d20 + \sum(\text{Modifiers})$ (**High Math**) | Single Armor Class ($AC$). DR is rare post-hit reduction. | Low (`Action Points` optional). | Hyper-Modular Feats & 10-level Prestige Classes (`Numerical bloat`). |
| **Pathfinder 2e**| $1d20 + \text{Prof} + \text{Mods}$ (**Medium-High Math**) | Single $AC$. Active Shield Block absorbs damage (`Hardness`). | Medium (`Hero Points 0-3` for rerolls/stabilize). | Keyword-tagged Feats by level (`Clean modular traits`). |
| **Shadow of the Demon Lord**| $1d20 + \text{Mod} \pm Nd6 \text{ Boons/Banes}$ (**Low-Medium Math**) | Agility-based or fixed heavy armor Defense score. | Low (`Fortune Tokens` rare). | 3-Tier Paths (`Novice/Expert/Master` with clean talents). |
| **Gloomhaven** | Card base attack $\pm$ Modifier draw (`+1, -1, 2x`) (**Low Math**) | Active card Shields reduce flat damage; card burning prevents death. | Zero (`Card management is lifespan`). | 10-15 Action Cards per class; checkmark perks. |
| **Mythras** | **Percentile Roll-Under ($d100 \le \text{Skill}\%$)** (**Minimal Math**) | **Active Opposed Roll (`Parry/Evade vs Attack`) + Localized Armor DR.** | Low (`Luck Points` to reroll or downgrade wound). | Combat Styles, Cults, and 5 distinct Magic traditions (`Modular skill groupings`). |
| **Our Mathless Engine** | **Step Pools (`2dX keep highest`)** (**ZERO Table Math**) | **4-Layer Defense Steps (`Evasion, Parry, Soak, Resilience`)**. Soak is post-hit reduction. | **Strictly ZERO.** All heroics powered by in-world `Stamina`, `Focus`, & `Item Sacrifice`. | Mathless Vector Traits (`+1Boon pool, Up-Shift die, Action cost, Keyword tag`). |

---

## 4. The Four New Simulationist & Tactical Vectors (`Vectors 15 to 18`)

### Vector 15: Opposed Resolution & Differential Maneuver Triggers
How systems handle contested rolls and how differential outcomes generate tactical maneuvers.

| System | Contested Roll Mechanic | Maneuver / Special Effect Access | How Outcomes Are Evaluated |
| :--- | :--- | :--- | :--- |
| **D&D 3.5e** | Rare opposed rolls (`Grapple = d20 + BAB + Str vs d20 + BAB + Str`). Attacks target static $AC$. | **Strictly Class/Feat Gated:** You cannot attempt complex maneuvers (`Disarm, Trip, Cleave`) effectively without specific feats (`Improved Disarm`) to avoid Attacks of Opportunity. | Binary Hit/Miss against $AC$. No differential effect beyond rolling a Natural 20 (`x2 or x3 critical multiplier`). |
| **Pathfinder 2e**| Attacks vs static $AC$. Maneuvers (`Shove, Trip`) are Athletics vs static Fortitude/Reflex DC. | **Universal Basic Maneuvers:** Anyone can attempt `Shove, Trip, Grapple` (`[1A]`), but advanced maneuvers (`Knockdown, Whirlwind Strike`) are gated behind Class Feats. | **4 Degrees of Success:** Beating or failing DC by $\pm 10$ triggers Critical Success / Critical Failure (`e.g., Crit Trip inflicts 1d6 damage + Prone`). |
| **Mythras** | **Continuous Opposed $d100$ Rolls:** Both attacker (`Combat Style %`) and defender (`Parry/Evade %`) roll simultaneously. | **100% Universal Special Effects:** Whenever the winner beats the loser by 1 or 2 **Levels of Success (`Crit vs Fail, Success vs Fail`)**, they instantly spend those levels to select maneuvers (`Impale, Bleed, Overextend, Disarm, Trip, Riposte`). Zero feat prerequisites. | **Differential Level Comparison:** The exact difference in success tiers dictates how many maneuvers are executed, making every single contested roll dynamic for *both* sides. |
| **Our Mathless Engine (`Blueprint`)**| **Opposed Step Pools (`Attacker NdX vs Defender MdY`):** Compare Highest Face Value (`Max vs Max`). | **Universal Mathless Maneuver Tokens (`[SET]`):** When your highest die beats the defender's highest die, **every additional die in your pool that also beats their roll** (or rolls max face) awards **1 Special Effect Token (`[SET]`)** spent on universal maneuvers (`Impale, Cleave, Disarm, Riposte`) without math or class gates! | **Face Differential & Multi-Beat Count:** `1 beating die = Standard Hit`; `2+ beating dice or Max Face = Hit + Special Effect Tokens`. |

---

### Vector 16: Active Defense Action Economy
Whether defending yourself is a passive background stat (`Armor Class`) or actively consumes your turn's action budget.

| System | Passive vs Active Defense | Action Budget Cost to Defend | Outnumbering / Tactical Pressure Impact |
| :--- | :--- | :--- | :--- |
| **D&D 3.5e** | **100% Passive $AC$:** Characters stand still; attackers roll against static $AC$. | Zero action cost during enemy turns (`except 1 Reaction per round for Attack of Opportunity or Shield Block`). | Low-to-Medium (`Flanking gives +2 attack to enemies`). A high-$AC$ character can passively deflect 10 attacks in a round without getting tired. |
| **Pathfinder 2e**| **Hybrid Passive/Active:** $AC$ is baseline passive, but `Raise a Shield (`[1A]`)` increases $AC$ by $+2$, and `Shield Block (`[R]`)` absorbs damage. | Requires spending **1 Action (`[1A]`) on your turn** to raise your shield, plus **1 Reaction (`[R]`)** out-of-turn to block. | Medium (`Flanking gives Flat-Footed -2 AC`). You only get 1 Reaction per round, so you can only Shield Block once per round regardless of how many enemies attack you. |
| **Gloomhaven** | **Active Card Preparation:** Players play Shield/Retaliate cards during their turn (`Shield 1 this round`). | Consumes card top/bottom actions during turn planning. Emergency defense requires **burning/losing cards from hand**. | High (`Every attack absorbed by burning cards permanently shortens your character's lifespan/timer`). |
| **Mythras** | **100% Active Defense Economy:** Defenders must declare active `Parry` or `Evade` rolls against incoming attacks. | Every single active `Parry` or `Evade` attempt **consumes 1 Action Point ($AP$)** from your pool (`typically 2-3 AP per round`). | **Extreme Tactical Pressure:** Once your $AP$ pool hits $0$, you **cannot actively parry or evade**. You must absorb incoming strikes purely with armor $DR$. Outnumbering a warrior ($3v1$) forces them to burn all $AP$ defending, leaving them helpless to strike back! |
| **Our Mathless Engine (`Blueprint`)**| **Hybrid Mathless Tension:** Free initial guard slot (`[1R]`), then Stamina depletion (`Stamina Burn`). | Every character gets **1 Free Defensive Reaction (`[1R]`)** per round (`Parry or Shield Intercept`). Additional parries/evasions in the same round **cost 1 Stamina per attempt (`Parry Fatigue`)**. | **Realistic Exhaustion:** Outnumbering a fighter forces them to spend Stamina on every incoming blow. When Stamina hits $0$, their active defense collapses (`Parry Pool = 0`), forcing them to rely entirely on their physical **Soak Rank (`Armor Die`)**. |

---

### Vector 17: Hit Location Granularity & Wound Severance
How systems track structural injury, anatomical targeting, and lethal thresholds.

| System | Anatomical Targeting | Damage Reduction ($DR$) Integration | Wound & Severance Thresholds |
| :--- | :--- | :--- | :--- |
| **D&D 3.5e** | **Global HP Bar:** Zero anatomical hit locations (`150 HP = full fighting capacity until 0 HP`). | Rare post-hit reduction (`DR 5/magic`). Armor strictly increases $AC$ (hit/miss binary). | Zero wound penalties above $0 HP$. At $\le 0 HP$, character falls unconscious (`bleeding out -1/round down to -10 death`). |
| **Pathfinder 2e**| **Global HP Bar + Wounded/Dying Conditions:** No localized limb damage. | Armor gives item bonus to $AC$. Shield Hardness absorbs flat damage on a Shield Block reaction. | At $0 HP$, gain `Dying 1-4` condition. If healed, gain `Wounded 1-3` flag (making future dying thresholds lower). |
| **Mythras** | **7 Localized Hit Locations:** (`Head, Chest, Abdomen, Left/Right Arm, Left/Right Leg`). | Armor applies **Localized $DR$** specific to each limb (`e.g., Helm = +5 DR Head; Cloth tunic = +1 DR Chest`). | **3 Anatomical Wound Levels per location:**<br>1. `Minor Wound (`HP > 0`)`: Cuts/bruises (`No penalty`).<br>2. `Serious Wound (`HP <= 0`)`: Limb useless/dropped weapon (`Arm`), Prone (`Leg`), Unconscious (`Head/Chest`).<br>3. `Major Wound (`HP <= -Max HP`)`: **Instant Limb Severance / Pulped Organ / Immediate Death.** |
| **Our Mathless Engine (`Blueprint`)**| **Mathless Anatomical Step Check (`1d8 Location Matrix`) triggered on Severe Hits.** | **Soak Rank (`d4 to d12`) checked post-hit:** Compare `Damage Die Face vs Soak Die Face`. If `Damage <= Soak`, kinetic force absorbed (`0 Wounds`). | **Wound Condition Escalation:** When `Damage Die > Soak Die`, roll **1d8 Location Die (`1-2 Head, 3-4 Chest, 5 Abdomen, 6-7 Arms, 8 Legs`)**. Apply immediate anatomical **Down-Shift** or **Bane** (`Arm = Drop item; Leg = Prone/Speed cut; Head = Muddled`). Critical Hits (`Damage rolled Max OR 2+ steps over Soak`) inflict **Severed Tendon / Fractured Rib / Mortal Wound** without calculating HP subtraction! |

---

### Vector 18: GM Cognitive Load & Mob Scaling (`Minion vs Rabble Architecture`)
How the ruleset manages game master tracking when running large groups of enemies ($10\text{-}20+$ monsters).

| System | Mob / Minion Tiering | Tracking Required per Mob Unit | Special Ability / Maneuver Access |
| :--- | :--- | :--- | :--- |
| **D&D 3.5e** | **No Formal Minion Rules:** Every monster (`even a Goblin`) has full Hit Dice (`HP 5`), $AC$, attack bonus, and saving throws. | High tracking during mass combat (`Tracking individual HP across 15 goblins creates massive GM bookkeeping`). | Full access to feats and racial traits (`e.g., Orc Ferocity, Goblin Stealth`). |
| **Pathfinder 2e**| **Troop Rules (`Swarm/Unit blocks`):** Groups of low-level enemies combine into a single massive "Troop" creature (`Gargantuan size`). | Single unified HP bar, area attacks, and shared saving throws for the entire 16-man squad. | Troop uses unified area maneuvers (`Form Phalanx, Volley Fire`) rather than individual actions. |
| **Mythras** | **3-Tier Enemy Architecture:**<br>1. `Rabble (Minions)`<br>2. `Underlings (Soldiers)`<br>3. `Iconic Foes (Bosses)` | **Rabble & Underlings eliminate Hit Locations:** They track only a single unified HP threshold (`Rabble die on 1st wound; Underlings die on 2nd wound/Serious wound`). | `Rabble` cannot use Special Effects (`pure cannon fodder`). `Underlings` use full Special Effects but flee when half their squad drops. `Iconic Foes` use full 7-location anatomical tracking. |
| **Our Mathless Engine (`Blueprint`)**| **3-Tier Mathless Mob Architecture:**<br>1. `Rabble (Minions)`<br>2. `Underlings (Soldiers)`<br>3. `Iconic Champions` | **Zero HP Bookkeeping for Rabble/Underlings:**<br>• `Rabble:` Defeated/routed on ANY strike that beats their **Soak Rank** (`Damage > Soak = Instant Kill/Flight`).<br>• `Underlings:` Defeated on any **Critical Hit** OR upon taking 2 standard hits (`Checkmark box [○][○]`). | `Rabble` roll base pool (`2dX`) with zero Boon/Maneuver access. `Underlings` can earn and spend 1 Maneuver Token (`[SET]`). `Iconic Champions` utilize full multi-layer defenses, Die Step-Up, and anatomical wound clocks. |
