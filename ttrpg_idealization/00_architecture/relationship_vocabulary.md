# Registry Relationship Vocabulary

**Status:** Approved — [DEC-106](../02_decisions/01_master_decision_log.md) (2026-08-29).  
**Purpose:** Define the controlled relationship terms used by `framework_registry.yaml`.

## Approved vocabulary

| Relationship | Meaning |
|---|---|
| `requires` | The source rule cannot function without the target rule. |
| `uses` | The source resolves through or invokes the target procedure. |
| `grants` | The source gives access, a Feature, a Rank, a Trait, or stated capability. |
| `modifies` | The source explicitly changes a stated baseline part in its own scope. |
| `limits` | The source restricts or prohibits target use. |
| `tests` | The source experiment or research artifact validates, calibrates, or stress-tests the target. |
| `replaces` | The source supersedes the target historically. |
| `contains` | Structural parent / child placement only. |
| `related` | Informational association only; no hard dependency. |

## Scope rules

- This vocabulary is registry-internal, not player-facing. Player-facing keyword vocabulary is governed by DEC-103.
- Software-engineering terms remain **rejected** for registry use: `interface`, `implements`, `extends`, `extension point`, `constrains`, `permission`.
- Directional principle (DEC-105, reorg model §8.4): canonical procedures have one-way ownership. Later spine layers may `uses` / `modifies` earlier procedures; earlier layers must not `requires` later layers; a hard `requires` cycle is a validation warning.

## Change control

Adding, removing, or redefining a term requires a new `DEC-###` decision and an update to this file. The registry must never use a relationship term outside this list.
