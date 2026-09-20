# AGENTS.md — Agent Operating Guide (Process, Governance, and Repo Protocol)

**Purpose:** Enable effective continuation of work if chat history is lost.  
**Non-goal:** This file contains no system mechanics, balance targets, or specific design decisions. Those live in canonical docs, the decision log, and the outstanding definitions index. If a sentence here starts describing what the game does rather than how to work on the project, it belongs elsewhere and should be moved.

---

## 1) What This Repo Is

This repository develops a tabletop RPG ruleset using a mathless-at-the-table philosophy and a simulationist design posture. Documentation is deliberately separated into canonical rules, research/comparative analysis, conversion procedures, brainstorm/decision logs, and archived work.

If you need to know what the rules *are*, do not use this file — follow the source-of-truth hierarchy below.

---

## 2) Source-of-Truth Hierarchy

When sources conflict, resolve in this order:

1. **Explicit user decisions made in the current working session**, even if not yet written down anywhere.
2. **Canonical rules** — `ttrpg_idealization/03_core_baseline_system/`, `ttrpg_idealization/04_simulationist_subsystems/`.
3. **The decision log** — `ttrpg_idealization/06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md`, “Core Design Decisions Log” section.
4. **The outstanding definitions index** — `ttrpg_idealization/06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md`.
5. **Research, comparative analysis, and simulations** — `ttrpg_idealization/02_comparative_system_analysis/`, `ttrpg_idealization/06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md`.
6. **Conversion procedures** — `ttrpg_idealization/05_conversion_and_content_engine/`.
7. **Archive** — `ttrpg_idealization/07_archive/`.

### Rules

- Archived or deprecated material is reference-only and must never override canonical rules.
- Do not infer authority from document age, length, or detail.
- If the hierarchy does not resolve a question, treat it as **open** and present options rather than deciding silently.

---

## 3) Decision Status Vocabulary

- **Locked** — settled architecture. Do not revisit without a strong reason and explicit user approval.
- **Provisional** — direction accepted; implementation or balance details remain open.
- **Open** — undecided; discuss and resolve before implementation.

Consult `ttrpg_idealization/06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md` for current status. Do not infer status from document phrasing.

---

## 4) Repository Map

```text
01_design_philosophy_and_pillars/     Design philosophy and pillars — non-canonical context
02_comparative_system_analysis/       Research, comparisons, external-system studies, simulations
03_core_baseline_system/              Canonical core rules
04_simulationist_subsystems/          Canonical subsystem rules
05_conversion_and_content_engine/     Procedures for porting reference-system content
06_brainstorming_logs_and_roadmap/    Decision log, outstanding index, roadmap, simulation notes
07_archive/                           Superseded/historical documents
```

If changing a rule, edit canonical rules first. Then update the decision log and outstanding definitions index. Never leave the log or index describing a state the canonical documents do not reflect.

---

## 5) First-30-Minutes Reading Procedure

After loss of context:

1. Read `ttrpg_idealization/README.md` for repository navigation.
2. Read `ttrpg_idealization/PROJECT_STATUS.md` to determine the current project phase, active scope, and explicit out-of-scope boundaries.
3. Read `ttrpg_idealization/PHASE_1_CHECKLIST.md` when working on current Phase 1 tasks.
4. Read `ttrpg_idealization/06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md`.
5. Skim `ttrpg_idealization/06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md` for relevant recent decisions.
6. Read the canonical file governing the subsystem being changed.
7. Consult research, comparative, or conversion documents as needed.

The completed refactor plan and audits are archived under `ttrpg_idealization/07_archive/documentation_refactor/`; future refactors should create new active planning artifacts.

`ttrpg_idealization/PROJECT_STATUS.md` is the authoritative project-phase and scope record. It is not a substitute for canonical rules or the outstanding definitions index.

Do not begin substantive implementation or architectural rewriting before completing step 4.

---

## 6) Agent Behavior Expectations

### User approval governs decisions

The Agent provides ideas, considerations, analysis, suggestions, alternatives, and draft formulations. The Agent must not treat any proposal as a decision until the User explicitly approves it. Every substantive mechanical, architectural, terminology, organizational, or procedural decision requires User approval before being recorded as canonical or locked.

### Ask when requirements are unclear

If a task is ambiguous, underspecified, contradictory, or supports materially different interpretations, ask a focused clarification question before implementing it. Do not silently choose an interpretation when it could affect mechanics, architecture, terminology, file organization, scope, or deliverable format. If the ambiguity is minor and the change is reversible, state the assumption explicitly.

### Be conservative with authority

Do not decide major architecture by implication. For foundational changes, present alternatives and obtain explicit approval before treating a direction as settled. If the User asks for a plan or evaluation, do not implement the proposed change unless implementation is explicitly requested.

### Prefer small, traceable changes

Make the minimum edit needed. Avoid broad rewrites unless explicitly requested. When replacing content, move the old version to `ttrpg_idealization/07_archive/` rather than deleting it.

### Single-source-of-truth rule

Every rule, mechanic, terminology definition, and canonical classification must have one authoritative home. Shared baseline vocabulary is maintained in `ttrpg_idealization/03_core_baseline_system/00_baseline_framework_glossary.md`. Do not restate canonical mechanics in `ttrpg_idealization/README.md`, `AGENTS.md`, the decision log, the outstanding definitions index, research documents, or other meta-files. Those documents may summarize status or link to the authority, but must not duplicate the rule. If a summary is necessary for navigation, keep it brief and link to the canonical source.

### Do not duplicate canon

Never copy rules, mechanics, or terminology definitions into meta-documents. Link to the canonical source instead. When canon changes, search for and remove stale summaries rather than creating another parallel definition.

---

## 7) Design-Change Protocol

Before proposing or applying a substantive change:

1. Locate the canonical home of the subsystem.
2. Search the repository for related terms and prior discussion.
3. Check the outstanding definitions index.
4. Classify the change:
   - **Editorial/clarification** — ordinary edit.
   - **Mechanical tweak** — proceed, but record it in the decision log.
   - **Architectural change** — high risk; requires explicit user approval.
5. For architectural changes, present at least two viable options and explain complexity, consistency, conversion impact, and drift risk.
6. Never silently overturn a Locked decision.
7. Obtain explicit approval before treating a direction as locked.

---

## 8) Decision-Recording and Artifact-Synchronization Protocol

When a change is approved:

1. Update the relevant canonical rules document.
2. Add or update a `DEC-###` entry in `ttrpg_idealization/06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md`.
3. Update `ttrpg_idealization/06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md`.
4. Update the relevant project-management artifact immediately:
   - `ttrpg_idealization/PROJECT_STATUS.md` for phase or scope changes.
   - `ttrpg_idealization/PHASE_1_CHECKLIST.md` for Phase 1 task completion.
   - `ttrpg_idealization/07_archive/documentation_refactor/DOCUMENTATION_REFACTOR_PLAN_COMPLETED.md` for refactor tasks.
   - `ttrpg_idealization/07_archive/documentation_refactor/DOCUMENTATION_REFACTOR_AUDITS_COMPLETED.md` for refactor audit results.
5. Update research, comparative, or conversion documents that reference the former state.
6. Update `ttrpg_idealization/README.md` only if top-level structure or navigation changes.
7. Move superseded documents to `ttrpg_idealization/07_archive/` and explain what replaced them.
8. Verify that all affected artifacts agree before marking the task complete.

**Synchronization rule:** A decision or execution step is not complete until the relevant canonical document, decision log, outstanding definitions index, checklist/status artifact, and audit record—where applicable—have been updated or explicitly marked as not applicable. Do not leave a completed action reflected in one artifact while another still describes it as pending. If an artifact cannot yet be updated because a decision remains partial or deferred, record that status explicitly rather than marking it complete.

If a decision changes player-facing behavior, it must exist in both canonical rules and the decision log.

---

## 9) Terminology Governance

- Canonical terminology belongs in canonical documents, not in a shadow glossary.
- Check existing terminology before introducing a new term.
- Define genuinely new terms once, in the correct canonical location, and record them in the decision log.
- Update outdated terminology in canonical documents.
- Preserve historical terminology in research and archived documents, labeling it as historical where necessary.
- Do not resolve terminology inconsistencies across multiple documents without being asked; flag them unless the change is explicitly authorized.

---

## 10) Research and Simulation Standards

When a claim depends on probability, pacing, or balance:

- Prefer a simulation, enumerated table, or explicit calculation over informal reasoning.
- Record assumptions, methods, results, and limitations alongside the artifact.
- Store scripts and outputs in `ttrpg_idealization/02_comparative_system_analysis/` or `ttrpg_idealization/06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md`.
- Treat results as evidence, not as decisions.
- Do not promote an untested probability claim to canonical status.

---

## 11) Documentation Style Rules

### Canonical documents

Should be:

- Declarative, not speculative.
- Single-source-of-truth.
- Explicit about procedures and edge cases.
- Linked outward to research for rationale.

### Non-canonical documents

Should be:

- Clearly labeled as research, comparative, brainstorm, or historical.
- Allowed to contradict canon because they are not rules.
- Explicit about draft or superseded status where relevant.

### Archive policy

Archive superseded documents rather than leaving them adjacent to canonical rules. Include a short explanation of why they were archived and what replaced them.

---

## 12) Reading-Order and Roadmap Pointers

Build a task-specific reading list using Section 5 rather than relying on a fixed list. Current priorities are tracked in:

```text
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md
06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md
```

This file is not the roadmap and should not be edited when priorities shift.

---

## 13) Conversation-History Preservation

The top-level `chat_history/` directory is the chronological, non-canonical record of the project conversation. It preserves the context and rationale that may not yet be reflected in a canonical document. It does not override the source-of-truth hierarchy in Section 2.

### Required workflow

1. After every User turn and every Agent turn, create one new Markdown file in `ttrpg_idealization/chat_history/`.
2. Use the next unused zero-padded sequence number and the role suffix: `0001_user.md`, `0002_ai-designer.md`, then continuing in order.
3. Use the established front matter and heading mold in `chat_history/README.md`; preserve the turn content verbatim.
4. Never edit, summarize, reorder, or delete an existing turn file to revise history. If a correction is needed, record it as a later turn.
5. The imported export is retained as `chat_history/chat_history.json`. Use `python3 chat_history/split_chat_history.py` to split or verify that export. It refuses to overwrite a turn whose content differs unless `--force` is explicitly supplied.
6. When context is lost, consult the relevant chronological turn files after completing the First-30-Minutes Reading Procedure, but treat explicit current-session decisions and canonical documents as authoritative.

This history is a process record, not a shadow rulebook. Do not copy canonical rules into it merely to preserve a decision; record approved rules through the normal canonical-document and decision-log workflow.

---

## 14) Completion Checklist

Before marking a non-trivial task complete:

- [ ] Canonical rules updated, if rules changed.
- [ ] Decision-log entry created or updated, if non-trivial.
- [ ] Outstanding definitions index updated.
- [ ] Necessary cross-references updated.
- [ ] Superseded content archived or labeled historical.
- [ ] No contradictions introduced across canonical files.

---

## 15) Common Failure Modes

Avoid:

- Treating brainstorm notes or research as canon.
- Copying rules or terminology into meta-files.
- Making architectural changes without decision-log entries.
- Leaving multiple contradictory canonical descriptions.
- Reviving archived mechanics without re-approval.
- Introducing terminology drift.
- Inferring authority from age, length, or polish.
- Skipping alternatives and trade-offs for architectural changes.

---

## 16) Maintaining This File

Update `AGENTS.md` only when:

- Authority relationships between directories change.
- The design-change or decision-recording protocol changes.
- A new category of canonical document is introduced.

Do not update it when:

- A game rule or mechanic changes.
- A decision is resolved.
- Roadmap priorities shift.

Those changes belong in canonical documents, the decision log, the outstanding definitions index, or the roadmap.

---

## Final Rule

Do not infer authority from a file’s age, length, or polish. If a claim cannot be traced to canonical rules, the decision log, or an explicit decision made in the current session, treat it as **open**, present alternatives, and ask for direction rather than deciding silently.

This file explains how to find and use the real sources of truth; it never substitutes for them.
