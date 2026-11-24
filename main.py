#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``output/entry.txt``).

The line is one vow, at most 160 characters, and the joke lands in its
last few words: a robot twist on the classic wedding line.
"""

import os

VOW = (
    "I vow to love you in sickness and in health, "
    "in full signal and in airplane mode, "
    "until a dead battery do us part."
)


def main() -> int:
    # The gate the sealed scorer applies: 1 to 160 characters, one line,
    # not only white space. Fail loudly here rather than ship a bad file.
    assert 1 <= len(VOW) <= 160, "vow must be 1 to 160 characters"
    assert "\n" not in VOW and VOW.strip() == VOW, "vow must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(VOW)
    print(VOW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
