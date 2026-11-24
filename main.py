#!/usr/bin/env python3
"""Write one funny developer excuse for code breaking in production.

Reads nothing, needs no network: it just writes a single fixed line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local
testing). The line is deterministic by construction.
"""

import os
import sys

EXCUSE = "Production didn't break, it finally read the TODO I left in 2019 and gave up."


def validate(line: str) -> None:
    """Mirror the competition gate: 1-200 chars, one line, not blank."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("excuse is blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("excuse must be a single line")
    if len(stripped) > 200:
        raise ValueError(f"excuse is {len(stripped)} chars, over the 200 limit")


def main() -> int:
    validate(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
