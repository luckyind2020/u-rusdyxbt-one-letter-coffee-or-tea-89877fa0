#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry runner.

The bounty asks for exactly one letter: A means coffee, B means tea.
This runner reads the chosen letter from entry.txt, drops it into
/output/entry.txt where the sealed scorer looks for it, and echoes it.
"""

import os
import sys


def pick_letter():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    try:
        with open(path, "r", encoding="utf-8") as handle:
            letter = handle.read().strip()
    except FileNotFoundError:
        print("entry.txt is missing next to main.py", file=sys.stderr)
        return ""
    if letter not in ("A", "B"):
        print("entry must be A for coffee or B for tea", file=sys.stderr)
        return ""
    return letter


def main():
    letter = pick_letter()
    if len(letter) != 1:
        print("entry must be exactly one letter", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(letter)
    print(letter)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
