---
turn: 215
role: "AI-Designer"
source: chat_history.json
---

# Turn 215 — AI-Designer

used
Bash
68ms
Edit
ttrpg_idealization/DOCUMENTATION_REFACTOR_PLAN.md
×2
DOCUMENTATION_REFACTOR_PLAN.md
MD

Agreed. The refactor plan should not quietly become a second design phase.

I updated DOCUMENTATION_REFACTOR_PLAN.md to explicitly state:

Refactor tasks may relocate, consolidate, relabel, or cross-reference existing decisions.
Refactor tasks may not create or resolve new rules definitions.
Any TBD topic must link to:
text
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md

rather than being decided during the documentation refactor.

I also revised Phase R11.

It no longer asks us to define:

Weapon and Damage Die relationships.
Armor and shield behavior.
Durability Slots.
Magical equipment scaling.
Crafting and repair rules.
Wealth bands.
Wealth-by-level guidance.

Instead, it now asks us to:

Inventory existing references.
Consolidate them under the future equipment owner.
Mark unresolved definitions as TBD.
Link those questions to the Outstanding Definitions Index.
Avoid creating or finalizing equipment rules or content during the refactor.

This scope distinction should also apply to every other refactor phase: if a topic is mechanically unresolved, we preserve, consolidate, and cross-reference it—but do not solve it as part of R0–R13.
