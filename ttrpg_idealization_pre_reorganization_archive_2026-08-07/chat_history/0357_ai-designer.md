---
turn: 357
role: "AI-Designer"
source: chat_history.json
---

# Turn 357 — AI-Designer

Partially, but not explicitly enough.

AGENTS.md
 currently says:

If the source hierarchy does not resolve a question, treat it as open and present options.
Do not decide major architecture by implication.
Obtain explicit User approval for substantive decisions.
Plans and evaluations should not be implemented without explicit authorization.

Those rules imply clarification-seeking, but there is no direct instruction saying:

When a task is ambiguous, underspecified, or has multiple materially different interpretations, ask the User for clarification before proceeding.

I recommend adding an explicit rule under Agent Behavior Expectations, such as:

Markdown
### Ask when requirements are unclear

If a task is ambiguous, underspecified, internally contradictory, or supports multiple materially different interpretations, ask the User a focused clarification question before implementing it. Do not silently choose an interpretation when the choice could affect mechanics, architecture, terminology, file organization, scope, or deliverable format.

If clarification is not necessary to make progress, state the assumption explicitly and keep the change reversible. If the ambiguity affects a major decision, stop and request direction.

This would complement the existing User-approval rule without duplicating it.
