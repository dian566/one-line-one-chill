#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry (program/v1).

Writes a single horror sentence to /output/entry.txt.
Deterministic: the same bytes on every run — no randomness, no clock,
no network, no input files.
"""

import os

ENTRY = "The baby monitor whispered my name in my dead grandmother's voice — and I live alone."

OUTPUT_PATH = os.environ.get("ONE_CHILL_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
