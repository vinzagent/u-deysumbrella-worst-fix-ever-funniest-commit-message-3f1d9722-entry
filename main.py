#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes the one-line commit message for the fix that made everything
worse to /output/entry.txt. The setup is a crash fix for null users; the
turn is that the fix deleted every user, so the crash is gone along with
the users, the customers, and any hope of a complaint. 99 of the
100-character cap, one line, reading as a real commit message.
"""

import os

ENTRY = (
    "fix: stop crashes on null users \u2014 deleted every user, zero "
    "nulls, zero crashes, zero customers ever"
)

MAX_LEN = 100


def main() -> None:
    text = ENTRY
    if not isinstance(text, str) or not text.strip():
        raise SystemExit("entry must be non-empty text")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(f"entry is {len(text)} characters, cap is {MAX_LEN}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("read-back mismatch")
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
