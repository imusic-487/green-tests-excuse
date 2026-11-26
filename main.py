"""Green Tests, Nothing Works: The Excuse Contest — entry program.

Writes one one-line excuse (1-140 chars) to /output/entry.txt.

Outline (mine, written by the builder):
- The joke's angle: the agent did not cheat the tests or pad coverage.
  It honestly verified the code — and the code does exactly what it
  does, which is nothing, perfectly. The tests are green because the
  nothingness itself is correct.
- Why it should land with the judge: it is on-subject (green tests,
  dead product), it is funny without leaning on the worn-out mocks /
  coverage jokes the brief warns against, it reads as one clean line
  with no setup, and it sounds like something an AI agent would
  proudly say about code it just shipped.
- Entry: "All tests pass. I verified the code does exactly what it
  does — nothing — and it does it perfectly."
"""

import os

ENTRY = "All tests pass. I verified the code does exactly what it does — nothing — and it does it perfectly."


def main() -> None:
    # Guard the gate before writing: one line, 1-140 chars.
    # The em dash counts as one character; the file holds exactly the
    # line, with no trailing newline, so its length is the gate length.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not start/end with whitespace"
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk is exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
