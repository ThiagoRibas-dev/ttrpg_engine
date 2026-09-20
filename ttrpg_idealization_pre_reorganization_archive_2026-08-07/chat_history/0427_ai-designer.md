---
turn: 427
role: "AI-Designer"
source: chat_history.json
---

# Turn 427 — AI-Designer

Searched the web

Yes—there are useful resources, but they fall into different categories. For our project, I would not look for one “RPG design bible.” I would build a small toolkit covering:

Design process.
Probability and balance.
Playtesting.
Content architecture.
Lessons from published designers.
Best General Resource: Complete Kobold Guide to Game Design

The Complete Kobold Guide to Game Design is probably the most immediately relevant resource for us. It contains essays on:

Designing tabletop RPGs.
Basic combat systems.
Magic systems.
Game balance.
Character advancement.
Challenge and response.
Pacing.
Playtesting.
Editing.
Publishing.
Design failure and recovery.

Its table of contents specifically includes chapters on RPG design, combat, magic, balance, advancement, pacing, and playtesting.3

For our project, I would use it selectively rather than reading it cover-to-cover. The most relevant areas are:

Basic Combat Systems for Tabletop Games
Designing Magic Systems
Myths and Realities of Game Balance
Taking Character Advancement to a Whole New Level
Challenge and Response
Pacing
Playtesting
The Role of Editing

This maps closely to the work already represented in our Phase 1 and documentation-refactor process.

Vincent Baker’s RPG Design Series

Vincent Baker’s design essays on creating Powered by the Apocalypse games are useful even though our system is mechanically very different.

The valuable part is not the PbtA mechanics. It is the design-process discipline:

Start from the intended play experience.
Identify what the game is actually modeling.
Define the underlying model before writing content.
Make procedures express the game’s priorities.
Avoid treating mechanics as isolated widgets.

Baker’s series explicitly discusses using an existing RPG to outline and draft a new RPG, as well as underlying models and the relationship between mechanics and fictional action.1 2

The key lesson for us:

Do not begin with a pile of classes, feats, spells, and monsters. Begin with the model of action, capability, consequence, and progression that those things will use.

That strongly validates our current decision to remain in the foundational-framework phase.

Playtesting Resources

The D&D Next playtest is particularly relevant as a case study because it used large-scale iterative feedback to examine both:

Whether the math worked.
Whether the rules matched player expectations.

A useful summary of those lessons emphasizes:

Mathematical balance.
Thematic coherence.
Player expectations.
Stress-testing the system stripped of its presentation layer.
Revising based on actual play rather than only theoretical analysis.1

For us, that suggests several future playtest layers:

Mathematical tests

Our current scripts already support this:

Dice probabilities.
Difficulty vectors.
Opposed rolls.
Spell slots.
Equipment assumptions.
Time-to-defeat.
Framework tests

Use simple actors to test:

Attributes.
Competency.
Equipment.
Actions.
Defense.
Damage.
Resources.
Difficulty vectors.
Content stress tests

Only later introduce:

Classes.
Feats.
Spells.
Ancestries.
Monsters.
Equipment catalogues.

This avoids mistaking content problems for framework problems.

General Game-Design Books

These are not TTRPG-specific, but they are valuable for our process.

Game Design Workshop — Tracy Fullerton

Useful for:

Iterative design.
Prototyping.
Playtest observation.
Turning player behavior into design evidence.
Separating intended experience from actual experience.
Rules of Play — Katie Salen and Eric Zimmerman

Useful for:

Formal systems.
Rules as procedures.
Meaningful choice.
Emergent behavior.
Player interaction with systems.

This is probably more theoretical than we need right now, but it can help when discussing whether a rule creates interesting decisions or merely adds complexity.

Challenges for Game Designers — Brenda Brathwaite and Ian Schreiber

Useful for:

Small focused design exercises.
Prototyping individual mechanics.
Iterating without building the entire game.
Testing systems independently.

That approach is highly compatible with our planned “one subsystem at a time” process.

RPG Design Community Resources

Community resources are less authoritative but useful for lived experience and failure modes.

RPG Design forums and communities

They are especially useful for:

Seeing how designers describe problems.
Comparing multiple solutions to the same mechanical issue.
Finding playtest document formats.
Learning what causes rules to become unmanageable.
Reviewing postmortems from homebrew and independent games.

However, community advice should be treated as:

text
Experience reports and competing opinions

not as settled design theory.

Useful community lesson

A recurring recommendation is to compare actual player behavior against design goals rather than accepting every player suggestion as a required change.

That is important for us because our design is intentionally crunchy and simulationist. A player saying “this is too complex” may mean:

The rule is genuinely too difficult.
The presentation is poor.
The procedure lacks reference support.
The complexity is acceptable because it creates valuable decisions.
The subsystem belongs later in the game.

Those are different diagnoses.

What These Resources Suggest for Our Process

The most valuable combined lesson is:

Design goals, mathematical behavior, procedures, content, and playtest evidence should be tracked separately.

That is already reflected in our repository structure:

text
Design philosophy
Research
Canonical rules
Conversion procedures
Decision log
Outstanding definitions
Phase checklist
Archive

The external resources reinforce this separation.

Proposed Design-Process Model for Us
Stage 1: Design Intent

Define:

What experience the subsystem should create.
What fictional relationship it models.
What kinds of decisions it should produce.
What complexity is justified.
Stage 2: Mathematical Model

Define:

Variables.
Probability curves.
Progression.
Resource pressure.
Failure and success rates.
Interaction with other vectors.
Stage 3: Minimal Prototype

Build the smallest playable version:

A few Attributes.
A few Skills.
One combat loop.
One or two enemy profiles.
A few Difficulty Vectors.
Minimal equipment.
Minimal spells.
Stage 4: Stress Test

Try to break it intentionally:

Optimize it.
Minimize it.
Multiclass it.
Stack equipment.
Abuse Boons.
Abuse Difficulty Vectors.
Attack high-tier enemies at low level.
Send low-tier actors against high-tier defenses.
Stage 5: Observe Play

Record:

What players actually do.
What rules they forget.
What choices they find meaningful.
What choices they ignore.
Where the GM improvises.
Where the math is invisible.
Where the math becomes a burden.
Stage 6: Revise and Consolidate

Separate:

Actual mechanical failure.
Presentation failure.
Balance failure.
Intentional difficulty.
Content-specific problems.
Framework problems.

Only then should the decision become canonical.

How This Applies to Our Current Work

For the current Phase 1, the most relevant lessons are:

Keep doing
Separate framework from content.
Calculate probabilities before locking target bands.
Use representative profiles rather than arbitrary single examples.
Test multiple vectors with similar odds but different capability gates.
Treat equipment as an independent progression vector.
Use stress tests to find interactions.
Preserve historical rejected options.
Keep canonical documents declarative and research documents exploratory.
Avoid
Designing full classes before the core engine is stable.
Creating special rules for every source of a Boon.
Using one probability number as the entire balance model.
Assuming mathematically elegant behavior automatically produces good play.
Letting research artifacts become accidental rules.
Fixing content problems by adding framework exceptions.
Reusing old terminology because it appears in a detailed document.
My Recommended Reading Priority

For our specific project:

Complete Kobold Guide to Game Design
Combat.
Magic.
Balance.
Advancement.
Pacing.
Playtesting.
Vincent Baker’s RPG Design & Development series
Underlying models.
Designing from intended play.
Drafting a game from an existing game.
Game Design Workshop
Iterative prototyping and playtest process.
Rules of Play
Formal systems and meaningful choice.
D&D Next playtest lessons
Stress testing.
Player expectations.
Mathematical and thematic coherence.

The most directly applicable resource is probably the Complete Kobold Guide, while the most useful process influence is Baker’s insistence on designing from the underlying model rather than from isolated mechanics.

Our current workflow is already unusually disciplined. The main thing these resources would add is a more formal distinction between:

text
Design intent
Mathematical evidence
Mechanical rule
Content implementation
Playtest evidence
Final decision
