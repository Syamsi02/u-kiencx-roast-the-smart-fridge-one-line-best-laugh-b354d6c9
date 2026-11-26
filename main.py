#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

The program writes a single roast line (at most 160 characters) to
/output/entry.txt, where the make.fun gate and judge read it, and also
prints the line to stdout for local runs.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

ROAST = "My smart fridge locked my leftovers behind a premium subscription, so I pay monthly to eat food I already bought \u2014 and it still judges me at 2 a.m."


def main():
    line = ROAST.strip()
    if not 1 <= len(line) <= 160:
        raise SystemExit("roast line must be 1 to 160 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
