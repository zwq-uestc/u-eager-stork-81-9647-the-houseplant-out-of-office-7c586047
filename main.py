#!/usr/bin/env python3
"""The houseplant's out-of-office auto-reply, one line, at most 120 chars.

Writes the reply to entry.txt in the output directory named by
MAKEFUN_OUTPUT_DIR (default /output). The file holds the line only:
no trailing newline, no second line.
"""

import os

REPLY = (
    "I'm out of office — the fern has been ignored since March and is now "
    "taking your emails hostage. Water me first."
)


def write_reply() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as out:
        out.write(REPLY)
    return target


if __name__ == "__main__":
    write_reply()
