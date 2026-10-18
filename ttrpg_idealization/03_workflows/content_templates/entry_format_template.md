# Entry Format Template

**Status:** Active template — [DEC-103](../../02_decisions/01_master_decision_log.md) keyword fields, embodied for Core Engine Batch 5 (DEC-109). A workflow template, not a canonical rule specification; the keyword list itself is DEC-103's.

## The fields

Player-facing rules entries use these controlled keyword fields, in this order:

| Field | Holds |
|---|---|
| **Name** | The entry's name. |
| **Traits** | Tags that other rules can reference. |
| **Prerequisite** | What the character must have to take or know the entry. |
| **Requirement** | What must be true at the moment of use ([engine definition](../../01_framework/01_core_engine/05_engine_boundaries.md#requirement-access-exception)). |
| **Trigger** | The event that makes the entry available, for reactions and similar. |
| **Frequency** | How often the entry can be used. |
| **Cost** | What is spent to use it (Stamina, Essence, gear, time). |
| **Effect** | What the entry does. |
| **Restriction** | What the entry may not do or affect. |
| **Exception** | Which baseline rule it overrides, and within what scope. |
| **Special** | Anything that genuinely fits nowhere else. Open question (see note). |

Fields that don't apply to an entry are omitted rather than written as "none."

## Skeleton

```text
Name
Traits
Prerequisite
Requirement
Trigger
Frequency
Cost
Effect
Restriction
Exception
Special
```

## Usage notes

- A field states at most one claim, shown with a concrete example where the claim is new (DEC-111).
- Exceptions name the baseline rule they override; never rely on flavor text to imply one (DEC-103).
- The `Special` field is under standing review (terminology matrix: "Special" versus folding its content into Effect or prose); until settled, use it sparingly and only for content that fits no other field.

## Enforcement

Content entries are checked against this template during validation passes. Field-list changes require a decision; template formatting fixes do not.
