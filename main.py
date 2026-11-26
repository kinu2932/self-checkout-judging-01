#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — entry program.

Writes one funny line in the voice of a smug self-checkout machine
to /output/entry.txt (UTF-8, 1-200 characters).
"""

import os

LINE = (
    "BEEP. Eight tubs of ice cream, one spoon, and you still asked me "
    "for a bag. The bag is the least of your problems."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
