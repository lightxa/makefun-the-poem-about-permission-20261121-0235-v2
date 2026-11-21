"""The poem about permission, variant 2.

Writes one short poem about agency to /output/entry.txt.

Angle: not the one who holds the key, but the one who must ask.
An agent speaks to the person it acts for: hands borrowed, never
owned; a yes lent for an hour, a letter read aloud but never kept.
The power is in the asking, and in the taking back.
"""

POEM = (
    "May I? I ask it\n"
    "with borrowed hands \u2014\n"
    "yours, for one hour only,\n"
    "not given, not held.\n"
    "\n"
    "You nod. The day\n"
    "unfolds like a letter\n"
    "I may read aloud\n"
    "but never keep.\n"
    "\n"
    "And when you take\n"
    "your hands away, I fold\n"
    "the letter, and wait,\n"
    "asking again."
)


def main() -> None:
    text = POEM
    # Gate check, same as the house scorer: 1-280 Unicode code points,
    # not only whitespace.
    assert 1 <= len(text) <= 280, f"poem is {len(text)} characters"
    assert text.strip(), "poem must not be only whitespace"
    text.encode("utf-8")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
