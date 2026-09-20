---
turn: 199
role: "AI-Designer"
source: chat_history.json
---

# Turn 199 — AI-Designer

We should define Difficulty Class before Required Successes, but design them together as two independent dimensions of difficulty.

The order should be:

Target Number
Difficulty Class
Required Successes
Complex Difficulty Notation
1. Target Number

The numeric threshold a die face must meet or exceed.

text
Target Number 5

A die showing 5 or higher succeeds against that threshold.

2. Difficulty Class

A named or contextual difficulty expressed through a Target Number.

text
DC 5

In our system, the DC is normally a fixed bounded value from 2 to 12.

A Difficulty Class answers:

How high must each successful die face be?

Possible working categories:

text
DC 2 — Trivial
DC 3 — Routine
DC 5 — Challenging
DC 7 — Formidable
DC 9 — Heroic
DC 11 — Legendary
DC 12 — Extreme

The labels should remain provisional until we finalize GM guidance.

3. Required Successes

Required Successes answer a different question:

How many dice must meet or exceed the DC?

Examples:

text
DC 5 (1)
DC 5 (2)
DC 5 (3)

All three use the same Target Number, but demand different quantities of successful faces.

4. Complex Difficulty

The complete notation is:

text
DC X (Y)

Where:

X is the Difficulty Class / Target Number.
Y is the number of Required Successes.

Example:

text
DC 5 (2)

Means:

text
Each successful die must show 5 or higher.
At least two dice must succeed.
Why They Should Be Separate

This gives us two independent axes of difficulty:

Difficulty Axis	Controls
DC	How high a successful die must be
Required Successes	How many successful dice are needed

This is mathematically useful because it avoids creating a large number of DC values.

For example:

text
DC 7 (1)

Could represent a difficult but quick task.

text
DC 5 (3)

Could represent a less individually difficult but sustained or complex task.

That distinction is especially useful for:

Crafting.
Research.
Climbing.
Rituals.
Social negotiations.
Combat maneuvers.
Multi-stage objectives.
Long-term projects.
Recommended Glossary Order

The glossary should be reorganized to use this sequence:

text
Target Number
Difficulty Class
Required Successes
Complex Difficulty
Automatic Success

Automatic Success should come after Required Successes because it interacts directly with the required-success total.

Example:

text
DC 9 (3)
5d12 + 1 Automatic Success

The automatic success counts toward the three required successes, but is not a die and does not interact with Boons, Banes, or tiebreaking.

Recommended Definitions
Target Number

The face value a die must meet or exceed to produce one success.

Difficulty Class

A bounded Target Number assigned to a task, defense, effect, or obstacle. Ordinary DCs normally range from 2 to 12.

Required Successes

The number of dice that must meet or exceed the Difficulty Class for a task or effect to succeed.

Complex Difficulty

A difficulty written as DC X (Y), requiring each successful die to meet or exceed Target Number X and requiring Y successful dice in total.

So the answer is:

Define Difficulty Class first, but finalize it alongside Required Successes because the two form the core two-axis difficulty system.
