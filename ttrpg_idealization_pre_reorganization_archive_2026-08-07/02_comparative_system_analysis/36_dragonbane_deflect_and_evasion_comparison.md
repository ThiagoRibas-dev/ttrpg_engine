# Dragonbane Dodge / Parry Compared to Current Deflect / Evasion

**Status:** Research comparison; non-canonical.  
**Purpose:** Compare Dragonbane’s defensive procedures to the project’s current Deflect and Evasion procedures. No procedure changes are proposed or adopted here.

## 1. Procedure Comparison

| Question | Dragonbane Dodge | Dragonbane Parry | Current Evasion | Current Deflect |
|---|---|---|---|---|
| Trigger | After an Attack hits, before damage. | After an Attack hits, before damage. | Eligible avoidable Attack during defense selection. | Eligible physical Attack during defense selection. |
| Defense roll | Evade roll-under check. | Weapon-skill roll-under check. | Reflexes opposed to Attack. | Suitable Strike opposed to Attack. |
| Core cost | Uses the defender’s one Action for the Round; the defender gives up their own action if it was unused. | Same. | 1 Stamina. Does not use Reaction. | 1 Stamina. Does not use Reaction. |
| Basic success | Cancels the hit / damage. | Cancels the hit / damage. | Defeats the Attack through the ordinary opposed procedure. | Defeats the Attack through the ordinary opposed procedure. |
| Equipment requirement | None. | Drawn weapon or shield; shield supports particular attacks. | None, but Heavy Armor applies 1 Bane. | Suitable weapon / Strike; shield grants 1 Boon. |
| Added positioning | Successful Dodge may move the defender 1 square / 2 meters. | No default movement benefit. | None by default. | None by default. |
| Item strain | None. | If the incoming damage exceeds the parrying weapon / shield’s Durability, it breaks. | None by default. | None by default; routine Durability expenditure is deferred. |
| Special critical result | No universal extra on ordinary success. | A critical Parry can create an immediate counterattack. | No universal extra result. | No universal extra result. |
| Monster exceptions | Dodge generally remains possible. | Most monster attacks cannot be parried unless stated. | Attack eligibility is explicit. | Physical-Attack eligibility and explicit exceptions govern. |

## 2. Main Structural Difference: Action Reservation versus Stamina Pressure

Dragonbane gives each combatant one primary Action. A combatant may spend it on their own attack / spell / maneuver, or preserve it to reactively Dodge or Parry an earlier enemy attack. Once a defensive reaction is taken, that character has no ordinary Action remaining in the Round.

The current framework deliberately uses another pressure model:

```text
Own Turn:
  3 Actions plus 1 Reaction.

Deflect / Evasion:
  Triggered self-defense, each costing 1 Stamina.
  They do not spend the Reaction.

Reaction:
  Reserved for explicit special interventions such as
  Interpose, Attack of Opportunity, and Counterspell.
```

### Consequence in play

| Situation | Dragonbane | Current framework |
|---|---|---|
| A foe attacks before your Turn | Decide whether to sacrifice your pending Action to stop the hit. | Spend Stamina if the defense is eligible; own Actions remain available. |
| You attack early in the Round | Usually lose later Dodge / Parry access because the Action is spent. | Retain Deflect / Evasion access until Stamina runs out. |
| Several enemies attack | Normally only one defensive Action can be spent. | Multiple eligible defenses are possible, but each consumes Stamina. |
| Shield / weapon defense | Avoid damage but risk item breakage on a strong hit. | Shield gives Deflect a Boon; item-strain procedure is intentionally deferred. |

Both systems make active defense consequential. Dragonbane makes it a **tempo and opportunity** decision; the current framework makes it an **endurance and attrition** decision.

## 3. Why the Current Split Remains Coherent

The current Deflect / Evasion model better serves the established three-Action economy and current resource roles:

```text
Stamina:
  Represents repeated physical defense, exertion, and mitigation.

Reaction:
  Represents exceptional intervention, not ordinary self-protection.

Actions:
  Remain the actor’s own Turn budget.
```

Moving Deflect / Evasion onto the Reaction would make an actor choose between their ordinary self-defense and Interpose, Attack of Opportunity, or Counterspell. Moving them onto ordinary Actions would make the current three-Action turn operate more like Dragonbane’s one-Action reservation game. Either would be a foundational combat-economy change rather than a small Dragonbane-inspired adjustment.

## 4. Useful Dragonbane References Without Direct Import

| Dragonbane pattern | Possible future reference | Current boundary |
|---|---|---|
| Dodge grants a small reposition on success | A future Feat, maneuver, or mobility Trait could grant a stated follow-up Step after a successful Evasion. | Do not add it to baseline Evasion without spatial / opportunity testing. |
| Parry tests equipment Durability | A future shield / weapon Durability procedure could make a successful Deflect impose stated item strain in particular circumstances. | Do not create routine Durability expenditure before the deferred item-strain procedure is designed. |
| Clear defensive timing: hit, then defense, then damage | Reinforces clear timing windows in the combat sequence. | Current sequence already places triggered defense before Damage Absorption and damage. |
| One defensive choice creates a tactical cost | Confirms the value of making defense non-free. | Current cost is Stamina, not sacrificed Action. |
| Monster attacks have explicit parry exceptions | Supports explicit Attack Tags / Permissions. | Current eligibility is already Tag / source / effect-specific. |

## 5. Explicit Non-Imports

```text
Do not make baseline Deflect / Evasion spend the Reaction.
Do not make baseline Deflect / Evasion consume an ordinary Action.
Do not give baseline Evasion a free move.
Do not give baseline Deflect a critical counterattack.
Do not add routine weapon / shield breakage before Durability strain is designed.
Do not make ordinary monster attacks immune to Deflect by default.
```

## 6. Sources Consulted

- Dragonbane defensive summary: <https://alchemyrpg.squarespace.com/dragonbane>
- Dragonbane Parry / Dodge analysis: <https://gypsywagon.com/2025/06/01/dragonbane-parrying-and-dodging/>
- Dragonbane action / defense cheat sheet: <https://cheatography.com/tangobreaker/cheat-sheets/dragonbane-actions/pdf/>

## 7. Scope Boundary

This is comparison only. Dragonbane does not alter the current canonical Deflect, Evasion, Reaction, Stamina, shield, Durability, or Attack-eligibility procedures.
