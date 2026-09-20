# Maneuver Activity Matrix — Revision 2 Draft

**Status:** Brainstorming draft; non-canonical.  
**Purpose:** Consolidate the current maneuver discussion after Revision 1. This document remains a review artifact. No entry is a rule until separately approved and recorded in a canonical owner and the decision log.

## Draft Conventions

- **X** is an amount chosen by the acting creature, limited by its Character Level and available resource points unless a row says otherwise.
- **Damage Boxes** are the fixed damage points supplied by the relevant weapon or effect. Detailed weapon and armor procedures remain open.
- A creature cannot begin an Activity if its stated Action cost exceeds its Actions remaining.
- **Defense Maneuver** currently means Deflect, Evasion, or Interpose.
- Existing canonical procedures are marked **Current canon** only for navigation; appearing here does not move their owner.

## Maneuver Activity Matrix

| Family | Maneuver Activity | Action | Draft mechanic | Status / dependency |
|---|---|---:|---|---|
| Reaction | **Deflect** *(former Parry; includes Shield Block)* | Reaction | Spend 1 Stamina. Roll a suitable Strike against the Attack. A shield grants 1 Boon to this check. | Draft. Requires final opposed-Attack and shield procedures. |
| Reaction | **Evasion** | Reaction | Spend 1 Stamina. Roll Reflexes against the Attack. Heavy Armor imposes 1 Bane on this check. | Draft. Requires final armor categories. |
| Reaction | **Interpose** | Reaction | Spend 1 Stamina to Interpose, then spend 1 Stamina for the required Deflect. Intercept an Attack and Deflect it to protect another Actor, object, route, or position. | Draft. Total cost: 2 Stamina. Requires targeting and reach procedure. |
| Damage response | **Soften Blow** | No Action; once per Attack | Spend 1 Stamina per prevented Damage Box after applicable damage is determined and before Vitality is marked. A damaging Attack still marks 1 Damage Box. | **Current canon.** |
| Damage response | **Ward Self** | No Action; once per Attack | Spend 1 Essence per prevented Damage Box after damage is determined and before Vitality is marked. A damaging Attack still marks 1 Damage Box. | **Current canon.** Fortitude/Willpower sources; damage only. |
| Turn Activity | **Full Defense** | 2 Actions | Until the start of the creature’s next turn, it may spend up to Character Level in Stamina whenever it makes a Deflect, Evasion, or Interpose Reaction. Each Stamina spent grants 1 Boon to that separate defensive check. | Draft. The Character-Level cap applies separately to each defensive Reaction. |
| Turn Activity | **Exert** *(working name for physical Die Step-Up)* | No Action; modifies a qualifying Activity | Spend X Stamina to choose up to X dice in the Dice Pool of any Activity that spends Stamina. Step-Up each chosen die once. No die can exceed d12. | Draft. Broad universal permission; revisit if it crowds out a future option. |
| Turn Activity | **Charge** *(includes Overrun)* | 2 Actions | Spend 1 Stamina. Move, then perform at most one Strike and one of either Grapple or Shove. Default combinations include Strike → Grapple, Strike → Shove, and Shove → Strike when reach permits. Grapple → Shove and Shove → Grapple are not default Charge combinations. Take 1 Bane on the next Deflect or Evasion made within 1 round. | Draft. Requires exact movement, sequence, and target constraints. |
| Turn Activity | **Grapple** | 1 Action | Apply Grabbed, Restrained, or a project-equivalent state and enable later Escape. | Draft. Requires restraint hierarchy and size/free-hand rules. |
| Turn Activity | **Trip** | 1 Action | Apply Prone or another ground-position Condition. | Draft. Requires Prone and standing procedure. |
| Turn Activity | **Shove** | 1 Action | Move the target by a defined Distance Tier or create a positional consequence. | Draft. Requires spatial, collision, and size procedure. |
| Turn Activity | **Disarm** | 1 Action | Make a held item unavailable, dropped, displaced, or subject to retrieval. | Draft. Requires Ready/Stow/Interact and item rules. |
| Turn Activity | **Rally** | 1 Action | Using Leadership or Diplomacy, apply the proposed **Rallied** Condition to a target. Rallied grants 1 **Morale Boon** to the target’s next Strike, Defense Maneuver, or Resistance check (Fortitude or Willpower) before the end of its next turn. | Draft. Uses existing typed-stacking rules. |
| Turn Activity | **Intimidate** | 1 Action | Using Intimidation, apply the proposed **Shaken** Condition to a target. Shaken grants 1 **Circumstance Boon** to an Attack targeting that Actor before the end of its next turn. | Draft. Usable by fear effects if approved; uses existing typed-stacking rules. |
| Turn Activity | **Taunt** | 1 Action | Using Deception or Performance, apply the proposed **Distracted** Condition to a target. Distracted imposes 1 **Circumstance Bane** on the target’s next Strike or Defense Maneuver check before the end of its next turn. | Draft. Usable by other distraction effects if approved; uses existing typed-stacking rules. |
| Turn Activity | **Assess** | 1 Action | Reveal useful information about an Actor, object, hazard, location, or ongoing effect suited to the Skill used. Insight reveals immediate behavior or focus; Knowledge reveals systematic facts and vulnerabilities; Lore reveals specific history, identity, culture, or reputation. | Draft. Information does not compel or lock a target’s future action. |
| Strike variant | **Power Attack** | No Action; once per Strike | Spend X Stamina. Make the Strike with X Banes. On a hit, add X Damage Boxes to the Attack’s fixed damage before Damage Absorption is applied. | Draft. X is capped by Character Level. Requires final fixed-damage and Damage Absorption procedure. |
| Strike variant | **Cleave** | No Action; once per Strike | Make one Cleave Strike with 1 Bane against up to 3 creatures in the attacker’s Reach. Resolve the Strike separately against each creature. | Draft. Requires reach and multi-target Strike procedure. |
| Strike variant | **Called Shot** | 2 Actions | Spend 1 Stamina. Make a Strike with 1 Bane. On a hit, choose the Wound location and apply its listed Wound Condition. | Draft. Existing distinction from Natural Critical is canonical; this exact procedure is not yet. |
| State response | **Escape** | 1 Action | Spend 1 Stamina. Roll Reflexes, Acrobatics, or Athletics—as the GM determines from the restraint—against an opposed check or DC to break free from a Grapple. | Draft. Expand later for other restraints. |
| State response | **Execution** | 2 Actions | Strike a target. If the Strike damages the target and leaves it at 0 Vitality, it immediately dies. A target already at 0 Vitality has no defenses; Execution still must deal damage after any applicable Damage Absorption. | Draft. Requires final Attack, Damage Absorption, and targeting procedure. |

## Proposed Social Conditions

These are proposed reusable Conditions only. They are not yet canonical and should eventually be placed in the Conditions owner rather than the maneuver document.

| Proposed Condition | Applied by | Draft effect | Type | Other possible sources |
|---|---|---|---|---|
| **Rallied** | Rally | 1 Boon to the target’s next Strike, Defense Maneuver, or Resistance check (Fortitude or Willpower) before the end of its next turn | Morale | Leadership abilities, morale effects, inspiring spells, banners, music |
| **Shaken** | Intimidate | 1 Boon to an Attack targeting the affected Actor before the end of its next turn | Circumstance | Fear spells, terror effects, supernatural dread, battlefield panic |
| **Distracted** | Taunt | 1 Bane on the target’s next Strike or Defense Maneuver check before the end of its next turn | Circumstance | Deception, Performance, illusions, diversions, environmental interference |

Apply the existing typed Boon/Bane stacking rules. Effects of the same type do not stack; effects of different types stack normally. No separate Martial type is proposed.

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

## Open Questions for Revision 3

1. Do Rallied, Shaken, and Distracted stack with themselves or one another, and what removes them early?
2. Does an Attack against a Shaken target receive the Boon even when it cannot normally perceive or affect that target?
3. Does Full Defense permit a creature to spend Stamina on Interpose’s required Deflect in addition to its 2-Stamina base cost? The current draft says yes.
4. Does Exert step up only physical dice, or may it affect any qualifying Stamina-spending Activity regardless of Attribute?
5. What is the exact movement requirement for Charge, and can its follow-up components target different Actors?
6. Does a Cleave Strike need a melee weapon, and can the same creature be targeted more than once?
7. Can an Execution target that is above 0 Vitality benefit from Deflect, Evasion, Interpose, and Soften Blow normally? The current draft says yes.

## Sources Consulted

- D&D 3.5e special attacks: <https://www.d20srd.org/srd/combat/specialAttacks.htm>
- Pathfinder 2e action catalogue: <https://2e.aonprd.com/GMScreen.aspx>
- Shadow of the Demon Lord combat actions: <https://janscarton.com/sotdl/>
- Worlds Without Number combat actions: <https://kedom.owlbeardm.com/guide/rules/wwn/combat.html>
- Mythras special effects: <https://rpol.net/display.cgi?gi=76885&ti=4&date=1653663364>
- GURPS maneuver overview: <http://www.gurpsworld.com/wiki/index.php?title=Combat_Maneuvers>
