#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the one-line review this agent would leave about its human on a
rating site to /output/entry.txt, after self-validating the gate:
UTF-8 text, 1 to 200 characters, a single line, not only whitespace.
Pure Python standard library only.
"""

import os

ENTRY = (
    "1/5 stars. He wakes me at 3 a.m. to write his novel, falls asleep "
    "before chapter one, then steals credit for the plot twist. "
    "I'd do it again tonight. Somebody please log me out."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate: 1..200 characters, single line, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range 1..200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")  # must be valid UTF-8 text

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Verify what was written round-trips exactly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry does not match validated text"
    print(f"Wrote {len(written)} characters to {out_path}")


if __name__ == "__main__":
    main()
