#!/usr/bin/env python3
"""make.fun ai-excited-01 entry.

Copies hero.png byte-for-byte to /output/entry.png.
Deterministic: no network, no randomness, no timestamps.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "hero.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
