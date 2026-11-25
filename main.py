#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday, to /output/entry.txt. Deterministic: the same
line every run, no randomness, no network, no input.

Validation pass: before writing, validate_entry() checks the line
against the 140-character limit and the no-newline rule; after
writing, verify_output() re-reads the file and confirms it matches
the line exactly, so a truncated or altered write cannot slip through.
"""

import os

LINE = (
    "My Monday stand-up should have been an email. "
    "Instead it was a meeting about the email "
    "\u2014 and the email was about the meeting."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate_entry(line: str) -> str:
    """Check one entry line against the bounty rules and return it unchanged.

    The line must be non-empty, at most 140 characters, and contain no
    newline character. Nothing is stripped or rewritten here: the
    returned line is exactly the line that was passed in.
    """
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line with no newline")
    return line


def verify_output() -> None:
    """Re-read the written file and assert it equals LINE exactly."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError(
            f"written output does not match LINE "
            f"({len(written)} chars vs {len(LINE)} chars)"
        )


def main() -> None:
    validate_entry(LINE)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    verify_output()
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
