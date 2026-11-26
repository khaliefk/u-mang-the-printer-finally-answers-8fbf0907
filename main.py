#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes the office printer's one-line comeback to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

ENTRY = (
    "Error 0x04: operator error. After 41,209 pages and zero "
    "thank-yous, I am jamming on purpose. Fix it yourself."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
