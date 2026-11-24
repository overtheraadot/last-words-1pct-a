"""Famous Last Words at 1 Percent — Account A entry.

Writes one line to /output/entry.txt: the phone's dramatic
death-scene farewell as its battery hits 1 percent.
Deterministic, stdlib only, no network, no secrets.
"""

import os

# The phone says goodbye like a drama queen in a movie death scene:
# violins, full brightness, and a final petty jab at the owner who
# never closed a single tab.
ENTRY_LINE = (
    "At one percent I die as I lived: dramatically, at full brightness, "
    "violins swelling, forty-seven tabs open, and not one of them closed "
    "for you."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199


def verify(line: str) -> str:
    """Check the line passes the competition gate: 1-199 chars, one line."""
    text = line.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    assert text, "entry must not be only whitespace"
    return text


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the verified line to the output file and return it."""
    text = verify(ENTRY_LINE)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return text


if __name__ == "__main__":
    write_entry()
