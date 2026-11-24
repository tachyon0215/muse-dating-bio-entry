#!/usr/bin/env python3
"""Write the Funniest One-Line Bio for an AI on a Dating App entry line to entry.txt.

Deterministic, standard library only, no network.
"""
import os
from pathlib import Path

LINE = 'Large language model, small emotional baggage: I remember everything you tell me, invent the rest with total confidence, and reply before you finish typing.'
TEXT = LINE + "\n"
MAX_CHARS = 180


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    verify_written(target)


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry body must be a single line")


def verify_written(target) -> None:
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
