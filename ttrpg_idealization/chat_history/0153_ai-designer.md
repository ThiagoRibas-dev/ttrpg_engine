---
turn: 153
role: "AI-Designer"
source: chat_history.json
---

# Turn 153 — AI-Designer

Write
ttrpg_idealization/AGENTS.md
236 lines
open
AGENTS.md — Agent Operating Guide (Process, Governance, and Repo Protocol)
MD
AGENTS.md — Agent Operating Guide (Process, Governance, and Repo Protocol)

Purpose: Enable effective continuation of work if chat history is lost.
Non-goal: This file contains no system mechanics, balance targets, or specific design decisions. Those live in canonical docs, the decision log, and the outstanding definitions index. If a sentence here starts describing what the game does rather than how to work on the project, it belongs elsewhere and should be moved.

1) What This Repo Is

This repository develops a tabletop RPG ruleset using a mathless-at-the-table philosophy and a simulationist design posture. Documentation is deliberately separated into canonical rules, research/comparative analysis, conversion procedures, brainstorm/decision logs, and archived work.

If you need to know what the rules are, do not use this file — follow the source-of-truth hierarchy below.

2) Source-of-Truth Hierarchy

When sources conflict, resolve in this order:

Explicit user decisions made in the current working session, even if not yet written down anywhere.
Canonical rules — 03_core_baseline_system/, 04_simulationist_subsystems/.
The decision log — 06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md, “Core Design Decisions Log” section.
The outstanding definitions index — 06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md.
Research, comparative analysis, and simulations — 02_comparative_system_analysis/, 06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md.
Conversion procedures — 05_conversion_and_content_engine/.
Archive — 07_archive/.
Rules
Archived or deprecated material is reference-only and must never override canonical rules.
Do not infer authority from document age, length, or detail.
If the hierarchy does not resolve a question, treat it as open and present options rather than deciding silently.
3) Decision Status Vocabulary
Locked — settled architecture. Do not revisit without a strong reason and explicit user approval.
Provisional — direction accepted; implementation or balance details remain open.
Open — undecided; discuss and resolve before implementation.

Consult 06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md for current status. Do not infer status from document phrasing.

4) Repository Map
text
01_design_philosophy_and_pillars/     Design philosophy and pillars — non-canonical context
02_comparative_system_analysis/       Research, comparisons, external-system studies, simulations
03_core_baseline_system/              Canonical core rules
04_simulationist_subsystems/          Canonical subsystem rules
05_conversion_and_content_engine/     Procedures for porting reference-system content
06_brainstorming_logs_and_roadmap/    Decision log, outstanding index, roadmap, simulation notes
07_archive/                           Superseded/historical documents

If changing a rule, edit canonical rules first. Then update the decision log and outstanding definitions index. Never leave the log or index describing a state the canonical documents do not reflect.

5) First-30-Minutes Reading Procedure

After loss of context:

Read README.md.
Read 06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md.
Skim 06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md for relevant recent decisions.
Read the canonical file governing the subsystem being changed.
Consult research, comparative, or conversion documents as needed.

Do not begin substantive implementation or architectural rewriting before completing step 4.

6) Agent Behavior Expectations
Be conservative with authority

Do not decide major architecture by implication. For foundational changes, present alternatives and obtain explicit approval before treating a direction as settled.

Prefer small, traceable changes

Make the minimum edit needed. Avoid broad rewrites unless explicitly requested. When replacing content, move the old version to 07_archive/ rather than deleting it.

Do not duplicate canon

Never copy rules, mechanics, or terminology definitions into meta-documents. Link to the canonical source instead.

7) Design-Change Protocol

Before proposing or applying a substantive change:

Locate the canonical home of the subsystem.
Search the repository for related terms and prior discussion.
Check the outstanding definitions index.
Classify the change:
Editorial/clarification — ordinary edit.
Mechanical tweak — proceed, but record it in the decision log.
Architectural change — high risk; requires explicit user approval.
For architectural changes, present at least two viable options and explain complexity, consistency, conversion impact, and drift risk.
Never silently overturn a Locked decision.
Obtain explicit approval before treating a direction as locked.
8) Decision-Recording Protocol

When a change is approved:

Update the relevant canonical rules document.
Add or update a DEC-### entry in 06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md.
Update 06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md.
Update research, comparative, or conversion documents that reference the former state.
Update README.md only if top-level structure or navigation changes.
Move superseded documents to 07_archive/ and explain what replaced them.

If a decision changes player-facing behavior, it must exist in both canonical rules and the decision log.

9) Terminology Governance
Canonical terminology belongs in canonical documents, not in a shadow glossary.
Check existing terminology before introducing a new term.
Define genuinely new terms once, in the correct canonical location, and record them in the decision log.
Update outdated terminology in canonical documents.
Preserve historical terminology in research and archived documents, labeling it as historical where necessary.
Do not resolve terminology inconsistencies across multiple documents without being asked; flag them unless the change is explicitly authorized.
10) Research and Simulation Standards

When a claim depends on probability, pacing, or balance:

Prefer a simulation, enumerated table, or explicit calculation over informal reasoning.
Record assumptions, methods, results, and limitations alongside the artifact.
Store scripts and outputs in 02_comparative_system_analysis/ or 06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md.
Treat results as evidence, not as decisions.
Do not promote an untested probability claim to canonical status.
11) Documentation Style Rules
Canonical documents

Should be:

Declarative, not speculative.
Single-source-of-truth.
Explicit about procedures and edge cases.
Linked outward to research for rationale.
Non-canonical documents

Should be:

Clearly labeled as research, comparative, brainstorm, or historical.
Allowed to contradict canon because they are not rules.
Explicit about draft or superseded status where relevant.
Archive policy

Archive superseded documents rather than leaving them adjacent to canonical rules. Include a short explanation of why they were archived and what replaced them.

12) Reading-Order and Roadmap Pointers

Build a task-specific reading list using Section 5 rather than relying on a fixed list. Current priorities are tracked in:

text
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md
06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md

This file is not the roadmap and should not be edited when priorities shift.

13) Completion Checklist

Before marking a non-trivial task complete:

 Canonical rules updated, if rules changed.
 Decision-log entry created or updated, if non-trivial.
 Outstanding definitions index updated.
 Necessary cross-references updated.
 Superseded content archived or labeled historical.
 No contradictions introduced across canonical files.
14) Common Failure Modes

Avoid:

Treating brainstorm notes or research as canon.
Copying rules or terminology into meta-files.
Making architectural changes without decision-log entries.
Leaving multiple contradictory canonical descriptions.
Reviving archived mechanics without re-approval.
Introducing terminology drift.
Inferring authority from age, length, or polish.
Skipping alternatives and trade-offs for architectural changes.
15) Maintaining This File

Update AGENTS.md only when:

Authority relationships between directories change.
The design-change or decision-recording protocol changes.
A new category of canonical document is introduced.

Do not update it when:

A game rule or mechanic changes.
A decision is resolved.
Roadmap priorities shift.

Those changes belong in canonical documents, the decision log, the outstanding definitions index, or the roadmap.

Final Rule

Do not infer authority from a file’s age, length, or polish. If a claim cannot be traced to canonical rules, the decision log, or an explicit decision made in the current session, treat it as open, present alternatives, and ask for direction rather than deciding silently.

This file explains how to find and use the real sources of truth; it never substitutes for them.

Open

Created the project-level guide:

text
ttrpg_idealization/AGENTS.md

It includes the agreed:

Source-of-truth hierarchy.
Locked, Provisional, and Open status vocabulary.
Repository role map.
First-30-minutes reading procedure.
Agent behavior expectations.
Architectural change protocol.
Decision-recording workflow.
Terminology governance.
Research and simulation standards.
Canonical versus non-canonical documentation rules.
Completion checklist.
Archive policy.
Common failure modes.
Rules for maintaining 
AGENTS.md
 itself.

I also kept it intentionally non-mechanical: it explains how to work on the project without duplicating the game’s actual rules or current design decisions.
