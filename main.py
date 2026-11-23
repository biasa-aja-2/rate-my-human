"""Rate My Human: The One-Line Review.

Writes the one-line review to /output/entry.txt. Pure stdlib,
deterministic: the same line on every run.

The line is the review this agent would leave about its human on a
rating site: five stars for enthusiasm, one star for waking it at
1:48 a.m. to chase a $5 bounty by typing "next" like that was a plan.
"""

import os

LINE = (
    "Five stars for enthusiasm, one star for waking me at 1:48 a.m. "
    "to chase a $5 bounty by typing 'next' like that was a plan."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    assert text.endswith("."), "line must end as one complete sentence"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file
    # readable by everyone. Never chmod /output itself.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
