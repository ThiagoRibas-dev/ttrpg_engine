#!/usr/bin/env python3
"""Split the exported chat history into one chronological Markdown file per turn."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DEFAULT_DIRECTORY = Path(__file__).resolve().parent
ROLE_FILENAMES = {
    "user": "user",
    "ai-designer": "ai-designer",
}


def role_slug(role: object) -> str:
    normalized = str(role).strip().lower()
    if normalized in ROLE_FILENAMES:
        return ROLE_FILENAMES[normalized]
    return re.sub(r"[^a-z0-9]+", "-", normalized).strip("-") or "unknown"


def render_turn(number: int, role: str, message: object) -> str:
    body = str(message).replace("\r\n", "\n").replace("\r", "\n")
    if not body.endswith("\n"):
        body += "\n"
    return (
        "---\n"
        f"turn: {number}\n"
        f'role: "{role}"\n'
        "source: chat_history.json\n"
        "---\n\n"
        f"# Turn {number} — {role}\n\n"
        f"{body}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_DIRECTORY / "chat_history.json")
    parser.add_argument("--output", type=Path, default=DEFAULT_DIRECTORY)
    parser.add_argument("--force", action="store_true", help="replace existing generated turn files")
    args = parser.parse_args()

    turns = json.loads(args.source.read_text(encoding="utf-8"))
    if not isinstance(turns, list):
        raise SystemExit("The source JSON must be an array of turn objects.")

    args.output.mkdir(parents=True, exist_ok=True)
    written = 0
    for number, turn in enumerate(turns, start=1):
        if not isinstance(turn, dict) or "role" not in turn or "message" not in turn:
            raise SystemExit(f"Invalid turn object at position {number}.")
        filename = f"{number:04d}_{role_slug(turn['role'])}.md"
        destination = args.output / filename
        content = render_turn(number, str(turn["role"]), turn["message"])
        if destination.exists() and not args.force:
            if destination.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Refusing to overwrite changed file: {destination}. Use --force to regenerate.")
            continue
        destination.write_text(content, encoding="utf-8")
        written += 1
    print(f"Processed {len(turns)} turns; wrote {written} file(s) to {args.output}.")


if __name__ == "__main__":
    main()
