#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday, to /output/entry.txt. Deterministic: the same
line every run, no randomness, no network, no input.
"""

import os

LINE = (
    "My Monday stand-up should have been an email. "
    "Instead it was a meeting about the email "
    "\u2014 and the email was about the meeting."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
