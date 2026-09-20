# Action Economy and Turn Structure

**Status:** Canonical action-framework owner.  
**Scope:** Turns, Actions, Reactions, action costs, and action-based fatigue. Spatial distances belong to `05_spatial_and_distance_engine.md`.

## 1. Round, Turn, Initiative, and Awareness

### Round

A combat **Round** represents approximately six seconds of simultaneous fictional time. A Round contains one normal Turn for each Actor participating in the encounter, resolved in initiative order.

### Initiative Modes

Before an encounter, the group uses one Initiative Mode. All Modes use the same Round, Turn, Reaction, and awareness procedures unless their entry explicitly changes them.

#### Reflex Initiative — Fixed Order

At the start of combat, each participating Actor rolls **Reflexes** once. That result establishes its place in the initiative queue for the encounter.

- Higher results act earlier.
- When tied Players are involved without an NPC, the Players decide their order.
- When an NPC is involved in a tie, compare the tied initiative pools from highest die to lowest die. If still tied, compare DEX; then INT. If still tied, the Actor that rolled initiative first acts first.
- Delay applies only to this Mode: on its Turn, an Actor may move later in the initiative queue for the current Round. It cannot move earlier that Round and resumes its established position at the next Round.

#### Reflex Initiative — Round-by-Round Order

At the start of each Round, each participating Actor rolls Reflexes. Resolve order and ties as in Fixed Order. The resulting queue lasts only for that Round.

#### Fast-Slow Side Initiative — Fixed Choice

At the start of combat, each Actor chooses either a **Fast Turn** or a **Slow Turn** for the encounter.

Each Round resolves in this order:

1. Player Fast Turns.
2. Enemy Fast Turns.
3. Player Slow Turns.
4. Enemy Slow Turns.

A Fast Turn grants 2 Actions. A Slow Turn grants 3 Actions. Players choose the order of Player-controlled Actors within their phase; the GM chooses the order of enemy Actors within their phase.

#### Fast-Slow Side Initiative — Round-by-Round Choice

At the start of each Round, each Actor chooses either a Fast Turn or a Slow Turn for that Round. Resolve the same Player Fast, Enemy Fast, Player Slow, Enemy Slow sequence. A Fast Turn grants 2 Actions; a Slow Turn grants 3 Actions.

### Delay

Delay is available only in Reflex Initiative — Fixed Order. In a Fast-Slow Side Initiative phase, a Player-controlled Actor may choose to act later within its own phase; an enemy Actor’s phase order is determined by the GM.

### Turn

At the start of its Turn, an Actor regains one Reaction and its Actions for that Turn:

```text
Standard or Slow Turn: [A] [A] [A] + [1R]
Fast Turn:             [A] [A]       + [1R]
```

Unspent Actions and an unused Reaction do not carry into the Actor’s next Turn. A Condition may reduce an Actor’s available Actions or otherwise alter this budget when its specific entry says so.

### Awareness and Surprise

There is no separate surprise round. All relevant Actors enter the initiative queue when combat begins.

- An **aware** Actor acts normally and has its Reaction available before its first Turn.
- An **unaware** Actor cannot use a Reaction or a triggered defense before becoming aware. On its Turn, it continues its current activity or acts only as its awareness permits.
- Once an Actor becomes aware, it acts normally beginning on its next Turn.

Specific Stealth, concealment, invisibility, perception, Condition, or Permission rules may alter awareness or initiative behavior.

## 2. Three-Action Turn

The Actions regained at the start of an Actor’s Turn may be spent in any order on Single Actions, Two-Action Activities, or Three-Action activities. A Fast Turn cannot begin an Activity whose Action cost exceeds its two-Action budget.

Common action categories include:

- Strike.
- Stride.
- Interact/Use Item.
- Tactical Maneuver.
- Raise Shield or prepare a defense.
- Cast a spell.
- Aim or perform another defined Activity.
- Full Defense or another defined defensive Activity.

The exact action cost belongs to the specific action, Activity, Class, Feat, Spell, or Equipment rule. Activity Tags are defined in `09_domains_skills_activities_and_crafting.md` and may alter an Activity when another rule explicitly refers to them.

## 3. Reactions

Each actor normally has one Reaction per Turn. Interpose, Attack of Opportunity, Counterspell, and similar special interventions require that Reaction when their individual rules say so.

Deflect and Evasion are triggered Stamina defenses, not Reactions. Conditions may prevent or restrict Reactions; their specific rules belong to the Conditions subsystem.

## 4. Movement

Stride and exact movement distances are defined in:

```text
05_spatial_and_distance_engine.md
```

A standard Stride normally shifts one abstract Distance Tier or moves the actor’s listed exact Speed. Reach, movement modes, difficult terrain, and disengagement are spatial rules rather than general action-economy rules.

## 5. Multiple Attacks and Repeated Actions

Repeated attacks or strenuous checks in the same turn may impose Pool Fatigue through Banes or other explicit effects. The specific repeated-action rule defines:

- Which attempt is affected.
- The number or type of Bane.
- Whether Stamina can mitigate the effect.
- Whether the action is a Strike, Activity, or special Class/Feat Permission.

This file does not replace the universal Bane procedure in `01_resolution_engine.md`.

## 6. Action-Based Positioning

Flanking, cover, high ground, prone targets, and similar positioning effects are represented through the universal Boon/Bane system or explicit Requirements and Permissions. Their spatial definitions belong to `05_spatial_and_distance_engine.md`; their pool effects are resolved by `01_resolution_engine.md`.

## 7. Action-Cost Ownership

- General action categories: this file.
- Distance, Reach, movement, and zones: `05_spatial_and_distance_engine.md`.
- Combat maneuvers: `../04_simulationist_subsystems/04_combat_maneuvers.md` and the relevant Class/Feat rules.
- Spell casting actions: `10_magic_schools_traditions_and_spellcasting.md`.
- Item interaction: `12_equipment_durability_and_economy.md` and the relevant item rule.
- Conditions and action restrictions: `04_simulationist_subsystems/03_resources_conditions_and_wounds.md`.
