---
turn: 253
role: "AI-Designer"
source: chat_history.json
---

# Turn 253 — AI-Designer

Ran commands
2
Write
ttrpg_idealization/DOCUMENTATION_REFACTOR_R13_REPORT.md
73 lines
open
Phase R13 Audit Report
MD
Phase R13 Audit Report

Status: Audit performed; cleanup findings remain.
Date: 2026-07-24
Changes made during audit: None to canonical rules.

Checks Performed
Scanned active canonical files for deprecated terminology and mechanics.
Checked Markdown links outside the archive.
Searched canonical files for unresolved option language and stale status language.
Compared current canonical ownership against the refactor plan.
Link Results

All scanned active Markdown links resolved successfully.

text
Missing active links: 0
Findings
Intentional historical/deprecation references

These are not necessarily errors because they explicitly explain deprecated terminology:

The glossary mentions the former Hyper-Shift terminology as deprecated.
The Resolution Engine references [SET] to state that it is no longer used.
The Defense document references Soak to state that Damage Absorption is the canonical replacement.
Attribute and Magic documents mention Focus to explain the rename to Essence.

These may remain if the project wants the canonical documents to preserve migration notes, or may be removed later for stricter terminology purity.

Actual stale canonical examples

04_simulationist_subsystems/02_skills_and_generic_capabilities.md still uses obsolete Attribute abbreviations and old threshold notation:

AGI
MIG
WIL
d10+
+1 Bane phrased through old pool assumptions
Older tactical procedure examples

These examples should be normalized to the current Attribute names and current Resolution Engine references during a later approved cleanup.

Potential ownership issue

04_simulationist_subsystems/02_skills_and_generic_capabilities.md still contains detailed Activity and maneuver procedures. The current canonical owner for the general Skill/Activity framework is:

text
03_core_baseline_system/09_domains_skills_activities_and_crafting.md

R8 established the ownership direction, but this file still needs a focused content reduction or cross-reference pass.

Status language

The following are acceptable because they explicitly describe deferred work:

Psychic/Psionic mechanics remain future work.
Equipment definitions remain TBD.
Historical reference material is labeled as historical.

No active canonical file was found presenting a resolved architectural option as an unmarked open alternative during this scan.

Result

R13 audit checks are complete, but the documentation refactor is not yet fully clean. The main remaining cleanup item is the generic skill-capabilities file, followed by a choice about whether deprecation notes should remain in canonical files.

No mechanics were changed during this audit. The findings should be reviewed before cleanup edits are applied.

Open
used
Bash
182ms

Phase R13 has been executed as an audit.

Created
text
DOCUMENTATION_REFACTOR_R13_REPORT.md
Checks completed
Deprecated terminology scan.
Obsolete-mechanics scan.
Canonical ownership scan.
Open/status-language scan.
Active Markdown link validation.
Cross-reference validation.
Link result
text
Missing active Markdown links: 0
Remaining findings

The main unresolved cleanup issue is:

text
04_simulationist_subsystems/02_skills_and_generic_capabilities.md

It still contains:

Obsolete Attribute abbreviations:
AGI
MIG
WIL
Old threshold notation such as d10+.
Older tactical procedure examples.
Detailed Activity and maneuver procedures that overlap with the canonical owner:
text
03_core_baseline_system/09_domains_skills_activities_and_crafting.md

There are also intentional deprecation references in canonical documents explaining:

Hyper-Shift as deprecated.
Soak as replaced by Damage Absorption.
Focus as renamed Essence.
[SET] as removed.

The report leaves those as a review choice rather than silently deleting them.

Tracking updated
Marked R13 scan tasks complete in DOCUMENTATION_REFACTOR_PLAN.md.
Recorded the audit result in DOCUMENTATION_REFACTOR_AUDITS.md.
Left R13.11 and R13.12 pending because the remaining cleanup findings need to be addressed before the refactor can be marked fully complete.

No canonical mechanics were changed during the audit.
