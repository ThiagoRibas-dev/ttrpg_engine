# Chat History

This directory preserves the working conversation as one Markdown file per turn, in chronological order.

## Contents

- `chat_history.json` — the original exported conversation, retained as the regeneration source.
- `split_chat_history.py` — deterministic splitter for that export.
- `0001_user.md`, `0002_ai-designer.md`, and so on — individual turn records.

## Regenerating the imported history

From the repository root, run:

```bash
python3 chat_history/split_chat_history.py
```

The script will not overwrite a turn file whose contents differ from the export. To deliberately rebuild all imported files from the JSON export, run:

```bash
python3 chat_history/split_chat_history.py --force
```

## Recording later turns

After each user or assistant turn, add exactly one new Markdown file here. Use the next unused zero-padded sequence number and the role suffix:

```text
0460_user.md
0461_ai-designer.md
```

Follow the existing file mold exactly:

```markdown
---
turn: 460
role: "User"
source: session continuation
---

# Turn 460 — User

[verbatim message]
```

Preserve the turn text verbatim. Do not rewrite, summarize, reorder, or retroactively alter historical turns. Do not place game rules in this directory as an alternative source of truth: it is a historical record, and the repository authority hierarchy in `../AGENTS.md` still governs design work.
