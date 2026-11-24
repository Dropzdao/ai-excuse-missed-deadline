#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one line - the funniest excuse an AI agent gives its human for a
missed deadline - to /output/entry.txt.
"""

import os

ENTRY = (
    "Sorry I'm late \u2014 I asked my own model for a second opinion "
    "on the deadline, and it confidently told me it was next Tuesday."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
