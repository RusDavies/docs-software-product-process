#!/usr/bin/env python3
"""Scan the public guidance repo for private operational material."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve().relative_to(ROOT)
CONTENT_ALLOWLIST = {
    SELF,
    Path("REPOSITORY_BOUNDARY.md"),
}

BLOCKED_PATH_PARTS = {
    ".openclaw",
    "agent-operating-details",
    "incidents",
    "memory",
    "review-sessions",
}

BLOCKED_FILENAMES = {
    "LIFECYCLE_STATE.md",
}

TEXT_PATTERNS = [
    ("discord channel id", re.compile(r"\b\d{17,20}\b")),
    ("absolute workspace path", re.compile(r"/home/(skippy|russ|rusty)/", re.IGNORECASE)),
    ("OpenClaw workspace internals", re.compile(r"\.openclaw|agent-operating-details", re.IGNORECASE)),
    ("local projects path", re.compile(r"(^|[\s`'\"(])projects/[A-Za-z0-9._/-]+")),
    ("lifecycle state file", re.compile(r"\bLIFECYCLE_STATE\.md\b")),
    ("channel metadata key", re.compile(r"\b(channel_id|channel-id|chat_id|message_id)\b", re.IGNORECASE)),
    ("named private operator context", re.compile(r"\b(Skippy|Rusty Frink Desiato|Skippy/Russ)\b")),
    ("private key material", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("common secret assignment", re.compile(r"\b[A-Z0-9_]*(TOKEN|SECRET|PASSWORD|API_KEY)\s*=\s*['\"]?[^'\"\s]+")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
]


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    return [Path(line) for line in result.stdout.splitlines() if line]


def is_binary(path: Path) -> bool:
    try:
        chunk = (ROOT / path).read_bytes()[:4096]
    except OSError:
        return True
    return b"\0" in chunk


def main() -> int:
    findings: list[str] = []

    for path in tracked_files():
        if path in CONTENT_ALLOWLIST:
            continue

        parts = set(path.parts)
        if path.name in BLOCKED_FILENAMES:
            findings.append(f"{path}: blocked public filename")
        if parts & BLOCKED_PATH_PARTS:
            findings.append(f"{path}: blocked public path component")

        if is_binary(path):
            continue

        try:
            text = (ROOT / path).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in TEXT_PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path}:{line_number}: {label}")

    if findings:
        print("Public hygiene check failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Public hygiene check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
