---
turn: 277
role: "AI-Designer"
source: chat_history.json
---

# Turn 277 — AI-Designer

Most of the core Boon/Bane architecture is now resolved. What remains is mainly edge-case formalization and future conversion/content guidance.

Boon/Bane Stacking: Resolved

The following are now established:

Boons and Banes cancel one-for-one.
Boons and Banes are final-pool effects.
They are applied after ordinary pool construction and Die Steps.
Types are:
Circumstance.
Enhancement.
Morale.
Competence.
Untyped.
Same-type effects do not stack.
Use only the strongest applicable effect of a type.
Different types stack.
Untyped effects may stack with typed effects.
The same named source cannot apply the same effect multiple times to the same target or check.
Boons add same-size dice.
Banes remove dice.
A one-die pool receiving a Bane suffers one Die Step-Down.
Further Banes do not worsen the pool.
A Bane-induced Step-Down from d4 causes automatic failure.
Boons participate normally in Required Success counting.
Remaining Framework Questions
1. Exact strength comparison within a type

The current rule says:

text
Use the strongest applicable effect of a type.

We still need to define how “strongest” is determined.

Example:

text
+1B Circumstance
+2B Circumstance

The obvious result is:

text
Use +2B Circumstance.

But we should formally answer:

Is +2B always stronger than +1B?
Is a special +1B with an additional Permission stronger than a normal +2B?
Can an effect declare priority over a numerically stronger effect?
Do typed effects compare only within the same side:
Boon versus Boon.
Bane versus Bane.
Does a special effect need a Permission to override normal type stacking?
2. Same source versus different sources

The same-named-source rule is established, but examples remain useful.

Still to define:

Are two identical spells cast by different casters separate sources?
Are two identical auras from different creatures separate sources?
Are two different Feats from the same Class separate sources?
Are two different effects from the same item separate sources?
Is a spell’s repeated effect the same source if cast on different targets?

A likely rule is:

Effects with the same named effect do not stack with one another on the same target, regardless of who produced them, unless the effect explicitly permits stacking.

That would prevent three copies of the same spell from stacking merely because three different characters cast it.

3. Typed Bane vocabulary

The four types apply to both Boons and Banes, but we have not created examples for every Bane type.

We should eventually establish examples such as:

text
Circumstance Bane:
  Poor visibility, unstable footing, cover.

Enhancement Bane:
  Damaged equipment, degraded weapon quality, disrupted magical focus.

Morale Bane:
  Fear, despair, broken formation, intimidation.

Competence Bane:
  Confusing instructions, unfamiliar procedure, inadequate preparation.

Untyped Bane:
  A rare exceptional effect that explicitly stacks with typed Banes.

This is a content-guidance task rather than a new core rule.

4. Bane interaction with the Competency Floor

The current framework says:

Floors remain active.
Banes may lower the effective Floor when reducing the final pool state.

The exact conversion is still not fully specified.

Example:

text
Expert:
  3d8, Floor 5

+1 Bane:
  2d8, Floor ?

Possible models:

Floor remains 5.
Floor drops to the Trained Floor of 3.
Floor drops by one fixed step.
Floor is recalculated from the final pool volume.
Floor changes only when the Bane causes a Die Step-Down.

This is the most important unresolved core Bane question.

5. Boons and Banes with Automatic Successes

We know:

Boons add dice.
Automatic Successes are not dice.

Still to define:

Can a Bane remove or suppress an Automatic Success?
Can a Boon grant an Automatic Success?
Can a single effect grant both a Boon and an Automatic Success?
Are Automatic Successes applied before or after Bane resolution?
Can a character have more Automatic Successes than Required Successes?
Do Automatic Successes function in opposed contests?

The current likely direction is:

text
Automatic Successes are separate from the pool.
Banes do not remove them unless the specific effect says so.

But this has not yet been formally locked.

6. Boons and Banes with Required Successes

Boons are already defined as ordinary dice for Required Success purposes.

Still to clarify:

Does a Bane remove a die that would otherwise have contributed a success?
Can a Bane reduce a pool below the number of Required Successes?
Can a Bane-induced Die Step-Down change the number of available successes?
Can a typed effect directly alter Required Successes, or does that require a Permission?

Example:

text
DC 7 (3)
4d10 +1X
→ 3d10

The Bane simply removes one die. The difficulty remains DC 7 (3).

7. Boons and Banes in opposed tiebreaks

The general direction is clear:

Boon dice are ordinary dice.
Bane-removed dice do not exist.
Tiebreaking uses the final rolled pools.

Still to formalize:

Whether Boon dice participate in secondary comparisons.
Whether the final reduced pool is sorted normally.
Whether a Bane-induced Die Step-Down affects only face size or also tiebreak priority.
Whether Automatic Successes are always excluded from tiebreaking.
8. Pools beyond the normal 5dX range

The current framework says:

text
5dX is the normal natural range.

It is not an absolute universal cap.

Still to decide:

Whether typed Boons can generate pools above 5dX.
Whether excess dice remain ordinary dice.
Whether high-tier content should convert extra dice into Automatic Successes.
Whether multiple content sources can each extend pool volume.
Whether the same-type stacking rule applies to extra-dice effects.
Whether a 10d12 pool is theoretically legal or only exceptional.

This belongs partly in the High-Tier and content framework.

9. Effects that alter type rules

The base framework permits an Untyped effect to stack with typed effects.

Still to define:

Whether any effect can explicitly override normal type stacking.
Whether “stacks with another effect” is a Requirement or Permission.
Whether a special effect can allow two same-type Boons to stack.
Whether such exceptions require a unique Trait.

Likely terminology:

text
Stacking Permission

Example:

This legendary artifact may stack its Enhancement Boon with one other Enhancement Boon.

10. Conversion mapping

The current system intentionally has not yet mapped external bonus categories.

Deferred work includes:

D&D 3.5e bonus types.
PF1e bonus types.
PF2e circumstance/status/item bonuses.
5e advantage/disadvantage.
SotDL Boons/Banes.
Mythras situational modifiers.
Gloomhaven attack modifiers.

This is explicitly a later conversion task, not a remaining core-framework decision.

Current Status

The checklist item can reasonably be changed from:

text
[~] Finalize all Boon/Bane stacking and cancellation edge cases.

to something more precise:

text
[~] Finalize Boon/Bane edge cases:
  - Floor interaction.
  - Automatic Success interaction.
  - Opposed tiebreak interaction.
  - Same-source identity.
  - Exceptional pool expansion.

The basic stacking architecture is complete. The remaining work is mostly to define interactions with:

text
Competency Floors
Automatic Successes
Required Successes
Opposed tiebreaks
High-tier pools
Content-specific exceptions

The external-system conversion mapping can remain deferred until the conversion phase.
