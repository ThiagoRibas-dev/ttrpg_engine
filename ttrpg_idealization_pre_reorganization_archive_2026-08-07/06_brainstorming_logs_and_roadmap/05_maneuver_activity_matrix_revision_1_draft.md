# Maneuver Activity Matrix — Revision 1 Draft

**Status:** Brainstorming draft; non-canonical.  
**Purpose:** Revise the maneuver matrix with the current discussion decisions. This document is for review and adjustment only. It does not establish a rule unless separately approved, recorded in the decision log, and placed in a canonical owner.

## Draft Conventions

- **Attack** means the initiating offensive check or effect being answered by a defense.
- **Damage Boxes** are fixed damage points supplied by the relevant weapon or effect. The detailed weapon and armor framework remains to be finalized.
- **X** is an amount chosen by the acting creature, limited by its Character Level and available resource points unless a row says otherwise.
- An Activity cannot begin if its stated Action cost exceeds the creature’s Actions remaining.
- Existing canonical procedures are marked **Current canon** only for navigation; their appearance here does not move their owner.

## Baseline Maneuver Activity Matrix

| Family | Maneuver Activity | Action | Draft mechanic | Status / dependency |
|---|---|---:|---|---|
| Reaction | **Deflect** *(former Parry; includes Shield Block)* | Reaction | Spend 1 Stamina. Roll a suitable Strike against the Attack. A shield grants 1 Boon to this check. | Draft. Requires final opposed-attack and shield procedures. |
| Reaction | **Evasion** | Reaction | Spend 1 Stamina. Roll Reflexes against the Attack. Heavy Armor imposes 1 Bane on this check. | Draft. Requires final armor categories. |
| Reaction | **Interpose** | Reaction | Spend 1 Stamina to Interpose, then spend 1 Stamina for the required Deflect. Intercept an Attack and Deflect it to protect another Actor, object, route, or position. | Draft. Total cost: 2 Stamina. Requires targeting and reach procedure. |
| Damage response | **Soften Blow** | No Action; once per Attack | Spend 1 Stamina per prevented Damage Box after applicable damage is determined and before Vitality is marked. A damaging Attack still marks 1 Damage Box. | **Current canon.** |
| Damage response | **Ward Self** | No Action; once per Attack | Spend 1 Essence per prevented Damage Box after damage is determined and before Vitality is marked. A damaging Attack still marks 1 Damage Box. | **Current canon.** Fortitude/Willpower sources; damage only. |
| Turn Activity | **Full Defense** | 2 Actions | Until the start of the creature’s next turn, it may spend Stamina when it makes a Deflect, Evasion, or Interpose Reaction. Each Stamina spent grants 1 Boon to that check. The total Stamina spent through Full Defense cannot exceed Character Level. | Draft. Confirm whether the Character-Level cap applies across the entire duration, as written. |
| Turn Activity | **Exert** *(working name for physical Die Step-Up)* | No Action; modifies a qualifying Activity | Spend X Stamina to choose up to X dice in the Dice Pool of an Activity that spends Stamina. Step-Up each chosen die once. No die can exceed d12. | Draft. Confirm whether every qualifying Activity may use Exert or whether individual Activities must explicitly permit it. |
| Turn Activity | **Charge** *(includes Overrun)* | 2 Actions | Spend 1 Stamina. Move, then use any combination of Strike, Grapple, and Shove. Take 1 Bane on the next Deflect or Evasion made within 1 round. | Draft. Requires a precise sequence and spatial constraints. |
| Turn Activity | **Grapple** | 1 Action | Apply Grabbed, Restrained, or a project-equivalent state and enable later Escape. | Draft. Requires restraint hierarchy and size/free-hand rules. |
| Turn Activity | **Trip** | 1 Action | Apply Prone or another ground-position Condition. | Draft. Requires Prone and standing procedure. |
| Turn Activity | **Shove** | 1 Action | Move the target by a defined Distance Tier or create a positional consequence. | Draft. Requires spatial, collision, and size procedure. |
| Turn Activity | **Disarm** | 1 Action | Make a held item unavailable, dropped, displaced, or subject to retrieval. | Draft. Requires Ready/Stow/Interact and item rules. |
| Turn Activity | **Rally** | 1 Action | Using Leadership or Diplomacy, grant a temporary tactical Permission, remove or limit a suitable morale state, or organize allied positioning. | Draft. Requires morale-state and ally-permission procedure. |
| Turn Activity | **Intimidate** | 1 Action | Using Intimidation, apply a fear or pressure Condition, or impose a defined tactical restriction. | Draft. Requires fear-condition and repeated-use procedure. |
| Turn Activity | **Taunt** | 1 Action | Using Deception or Performance, create a defined opening against a target without predicting or compelling its future choice. | Draft. Requires opening/off-guard procedure. |
| Turn Activity | **Assess** | 1 Action | Reveal useful information about an Actor, object, hazard, location, or ongoing effect suited to the Skill used. Insight reveals immediate behavior or focus; Knowledge reveals systematic facts and vulnerabilities; Lore reveals specific history, identity, culture, or reputation. | Draft. Information does not compel or lock a target’s future action. |
| Strike variant | **Power Attack** | No Action; once per Strike | Spend X Stamina. Make the Strike with X Banes. On a hit, add X **Damage Boxes** to the Attack’s fixed damage before Damage Absorption is applied. | Draft. X is capped by Character Level. Requires final weapon fixed-damage and Damage Absorption procedure. |
| Strike variant | **Cleave** | No Action; once per Strike | Make one Cleave Strike with 1 Bane against each eligible creature within reach that forms a contiguous straight line of adjacent creatures. Resolve the Strike separately against each creature. | Draft. Uses a line of adjacent creatures instead of facing or an Arc. Requires reach and adjacency procedure. |
| Strike variant | **Called Shot** | 2 Actions | Spend 1 Stamina. Make a Strike with 1 Bane. On a hit, choose the Wound location and apply its listed Wound Condition. | Draft. Existing distinction from Natural Critical is canonical; this exact procedure is not yet. |
| State response | **Escape** | 1 Action | Spend 1 Stamina. Roll Reflexes, Acrobatics, or Athletics—as the GM determines from the restraint—against an opposed check or DC to break free from a Grapple. | Draft. Expand later for other restraints. |
| State response | **Execution** | 2 Actions | Strike a target. If the Strike reduces the target to 0 Vitality, it immediately dies. It can also kill a downed target already at 0 Vitality. | Draft. Requires an explicit answer for whether ordinary Damage Absorption and defense procedures apply normally. |

## Deliberately Deferred Candidates

| Candidate | Future owner or dependency |
|---|---|
| Bleed | Wound, weapon Trait, or Critical procedure |
| Sunder / Damage Equipment | Equipment Durability and item-damage framework |
| Pin Weapon | Weapon Traits and item/restraint procedure |
| Entangle | Weapon, spell, terrain, or effect procedure |
| Reposition / Pull / Drag | Revisit after Charge, Grapple, and Shove testing |
| Compel Surrender | Morale and social-conflict framework |
| Aim / Take Cover / Ready | General Action Economy or spatial framework |
| Mounted maneuvers | Mount/vehicle framework |

## Open Questions for Revision 2

1. Does the Full Defense Character-Level cap apply across all defensive Reactions until the creature’s next turn, or separately to each Reaction?
2. Does Exert apply to every Activity that spends Stamina, or only if the Activity explicitly permits Exert?
3. What sequence and maximum number of follow-ups does Charge permit when it combines Strike, Grapple, and Shove?
4. Does Execution use ordinary defenses and Damage Absorption, or is it a specialized finishing procedure?
5. What defines an eligible creature in Cleave’s contiguous line: adjacency only, reach only, or both?
6. Which Conditions and procedures define an opening for Taunt, a morale state for Rally, and a fear/pressure state for Intimidate?

## Sources Consulted

- D&D 3.5e special attacks: <https://www.d20srd.org/srd/combat/specialAttacks.htm>
- Pathfinder 2e action catalogue: <https://2e.aonprd.com/GMScreen.aspx>
- Shadow of the Demon Lord combat actions: <https://janscarton.com/sotdl/>
- Worlds Without Number combat actions: <https://kedom.owlbeardm.com/guide/rules/wwn/combat.html>
- Mythras special effects: <https://rpol.net/display.cgi?gi=76885&ti=4&date=1653663364>
- GURPS maneuver overview: <http://www.gurpsworld.com/wiki/index.php?title=Combat_Maneuvers>
