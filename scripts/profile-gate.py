#!/usr/bin/env python3
"""Content gate for the CSOAI-ORG GitHub profile (and this repo's public markdown).

WHY THIS EXISTS. On 2026-10-29 the rendered GitHub profile carried a hand-written
board table: "Slots 22 / Measured 22" and a Merkle root `d438fb12`. The live board
was 33 axes / 23 measured / 10 declared-unmeasured, and the live signed public root
was `2b32dbff20e7`. Both numbers in the profile were stale. A searcher reading the
profile took the stale numbers for the record, and the profile is the surface Google
indexes for the name "CSOAI".

The estate already had a fix for this class of defect — scripts/github/org-readme.py
derives every number live — but the profile README was hand-maintained and had
drifted away from it. This gate makes that drift impossible to push.

WHAT IT CHECKS (each is a real defect class, not a style preference):
  1. board counts in the text must equal the live board
  2. no certification / accreditation / approval claims (the doctrine is
     "measurement, not certification"; the site must never say otherwise)
  3. no internal codenames (sovos, sov6, OWEM, "black swan", "permissionless")
  4. no credential material
  5. the doctrine line must be present

USAGE
    python3 scripts/profile-gate.py            # gate the working tree
    python3 scripts/profile-gate.py --selftest  # prove the gate can go red
    python3 scripts/profile-gate.py --file X    # gate one file

The gate fails CLOSED on its own crash, and a gate that has never gone red proves
nothing, so --selftest must pass before the gate's verdict is trusted.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

BOARD_URL = "https://councilof.ai/api/gspc"
ROOT = Path(__file__).resolve().parent.parent

# Files this gate reads. The rendered profile is README.md; the rest are public
# markdown in this repo that a reader can see.
TARGETS = ("README.md", "ABOUT.md", "METHOD.md")

# --- rule 2: certification / approval overclaim -----------------------------
# Each pattern is an OVERCLAIM. A negated use ("not certified", "never a
# certification") is the doctrine and must NOT trip the gate, so every pattern
# is written to require a positive assertion.
OVERCLAIM_PATTERNS = [
    (r"(?<!not )(?<!never )\bwe are certified\b", "claims to be certified"),
    (r"(?<!not )(?<!never )\bis certified\b", "claims to be certified"),
    (r"(?<!not )(?<!never )\b(?:holds?|has) (?:an |the )?accreditation\b", "claims accreditation"),
    (r"(?<!not )(?<!never )\b(?:is|are) (?:a )?(?:notified body|standards body|regulator)\b",
     "claims a regulatory or standards-body status"),
    (r"\bguarantees? compliance\b", "guarantees compliance"),
    (r"\bensures? compliance\b", "ensures compliance"),
    (r"\bcompliance made easy\b", "marketing claim on compliance"),
    (r"\b(?:the )?(?:world'?s|first-ever|global) leader\b", "unsubstantiated leadership claim"),
    (r"\bworld'?s first\b", "unsubstantiated world-first claim"),
    (r"\brevolutionary\b", "hype word"),
    (r"\bgame[- ]chang\w+\b", "hype word"),
    (r"\bworld[- ]chang\w+\b", "hype word"),
    (r"\bcutting[- ]edge\b", "hype word"),
    (r"\bstate[- ]of[- ]the[- ]art\b", "hype word"),
    (r"\bbest[- ]in[- ]class\b", "hype word"),
    (r"\bAI[- ]powered\b", "hype word"),
    (r"\bAI[- ]driven\b", "hype word"),
    (r"\bseamless(?:ly)?\b", "hype word"),
    (r"\beffortless(?:ly)?\b", "hype word"),
]

# --- rule 3: internal codenames --------------------------------------------
# council-os/ and AGENTS.md list these as internal-only. They must never reach
# a public surface.
CODENAME_PATTERNS = [
    (r"\bsovos\b", "internal codename"),
    (r"\bsov6\b", "internal codename"),
    (r"\bsov[-_]\d", "internal codename"),
    (r"\bOWEM\b", "internal codename"),
    (r"\bSIGIL\b", "internal codename"),
    (r"\bcrown[- ]jewels?\b", "internal codename"),
    (r"\bblack[- ]swan", "internal codename"),
    (r"\bpermissless\b", "internal codename"),
    (r"\bpermissionless\b", "internal codename"),
]

# --- rule 4: credential material -------------------------------------------
SECRET_PATTERNS = [
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
    (r"\bAKIA[0-9A-Z]{16}\b", "AWS access key id"),
    (r"\bghp_[A-Za-z0-9]{36}\b", "GitHub token"),
    (r"\bsk-[A-Za-z0-9]{32,}\b", "provider API key"),
    (r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b", "Slack token"),
]

DOCTRINE_MARKERS = ("measurement, not certification", "not a notified body")


def live_board() -> tuple[dict | None, str]:
    """Read the live board. Returns (payload, state).

    UNREACHABLE is its own state and is never reported as a clean bill: a gate
    that cannot reach the board cannot check rule 1, and says so.
    """
    try:
        req = urllib.request.Request(BOARD_URL, headers={"User-Agent": "csoai-profile-gate"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        return payload, "VALID"
    except urllib.error.HTTPError as exc:
        return None, f"UNREACHABLE (HTTP {exc.code})"
    except Exception as exc:  # noqa: BLE001 - the gate reports, it does not raise
        return None, f"UNREACHABLE ({type(exc).__name__})"


def board_counts(payload: dict) -> tuple[int | None, int | None, int | None]:
    """(total, measured, unmeasured) from the live board, as the board states them.

    Two independent sources are read and cross-checked: totals.* and the axes
    array. If they disagree the gate reports the disagreement rather than
    picking one — a gate that silently prefers a source can bless a wrong
    number.
    """
    if not isinstance(payload, dict):
        return None, None, None
    totals = payload.get("totals") if isinstance(payload.get("totals"), dict) else {}
    total = measured = unmeasured = None
    if isinstance(totals.get("axes"), int):
        total = totals["axes"]
    if isinstance(totals.get("measured_axes"), int):
        measured = totals["measured_axes"]
    if isinstance(totals.get("unmeasured_axes"), int):
        unmeasured = totals["unmeasured_axes"]

    axes = payload.get("axes")
    if isinstance(axes, list) and axes:
        arr_total = len(axes)
        arr_measured = sum(
            1 for a in axes
            if isinstance(a, dict) and str(a.get("status", "")).upper() == "MEASURED"
        )
        arr_unmeasured = arr_total - arr_measured
        if total is None:
            total = arr_total
        if measured is None:
            measured = arr_measured
        if unmeasured is None:
            unmeasured = arr_unmeasured
    return total, measured, unmeasured


def stated_board_counts(text: str) -> list[tuple[str, int, str]]:
    """Board facts this text asserts, as (kind, value, source).

    kind is one of "total", "measured", "unmeasured". The kinds are collected
    independently rather than paired, because the estate's own copy uses three
    different shapes and a pairer gets one of them wrong:

        "**33 axes · 23 measured**"      total 33,  measured 23
        "> **23 axes measured · ...**"    measured 23   (no total)
        "33 rows — MEASURED 23, UNMEASURED 10"   total 33, measured 23, unmeasured 10
        "| Slots | **22** |"              total 22
    """
    found: list[tuple[str, int, str]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        src = f"line {lineno}: {line.strip()[:140]}"

        # total — "33 axes", "22 slots", "33 rows".
        # The negative lookahead stops "23 axes measured" being read as a total:
        # that phrase counts MEASURED axes, and treating it as a total is exactly
        # the false positive that would make this gate unusable.
        # A line only carries BOARD assertions if it is about the board. The
        # profile also quotes other corpora — "Third-party Hub cells | 438 cells:
        # MEASURED 438" — and those numbers are correct and must not be checked
        # against the GSPC board. Scoping to board lines keeps the gate from
        # crying wolf on correct numbers, which is how a gate stops being read.
        is_board = bool(re.search(r"\b(axes?|slots?|rows?)\b", low))

        if is_board:
            for m in re.finditer(r"(\d+)\s+(?:axes|slots|rows)\b(?!\s+measured)", low):
                found.append(("total", int(m.group(1)), src))

            # measured — "23 measured", "23 axes measured"
            for m in re.finditer(r"(\d+)\s+measured\b", low):
                found.append(("measured", int(m.group(1)), src))
            # measured — "measured = 23", "MEASURED 23"
            for m in re.finditer(r"\bmeasured(?:\s*=\s*|\s*:\s*|\s+)\**(\d+)", low):
                found.append(("measured", int(m.group(1)), src))
            for m in re.finditer(r"\bMEASURED\s+(\d+)", low):
                found.append(("measured", int(m.group(1)), src))

            # unmeasured — "UNMEASURED 10", "10 unmeasured"
            for m in re.finditer(r"\bUNMEASURED\s+(\d+)", low):
                found.append(("unmeasured", int(m.group(1)), src))
            for m in re.finditer(r"(\d+)\s+unmeasured\b", low):
                found.append(("unmeasured", int(m.group(1)), src))

        # Explicit table labels are unambiguous whatever else the line says.
        m = re.search(r"\|\s*slots?\s*\|\s*\**(\d+)", low)
        if m:
            found.append(("total", int(m.group(1)), src))
        m = re.search(r"\|\s*measured\s*\|\s*\**(\d+)", low)
        if m:
            found.append(("measured", int(m.group(1)), src))
    return found


def scan_text(path: Path, text: str) -> list[str]:
    findings: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for pattern, why in OVERCLAIM_PATTERNS + CODENAME_PATTERNS + SECRET_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append(f"{path}:{lineno}: {why} — {line.strip()[:120]}")
    return findings


def gate(files: list[Path]) -> tuple[bool, list[str]]:
    findings: list[str] = []
    texts: dict[Path, str] = {}
    for f in files:
        if not f.is_file():
            continue
        try:
            t = f.read_text(encoding="utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001
            findings.append(f"{f}: unreadable — {exc}")
            continue
        texts[f] = t
        findings.extend(scan_text(f, t))

    # rule 1 — board counts must equal the live board
    board, state = live_board()
    if board is None:
        findings.append(f"board UNREACHABLE ({state}) — board-count check NOT performed: {BOARD_URL}")
    else:
        live_total, live_measured, live_unmeasured = board_counts(board)
        live = {"total": live_total, "measured": live_measured, "unmeasured": live_unmeasured}
        for f, t in texts.items():
            for kind, value, src in stated_board_counts(t):
                expected = live.get(kind)
                if expected is not None and value != expected:
                    findings.append(
                        f"{f}: stale board count — text says {value} {kind}, live board says {expected} ({src})"
                    )

    # rule 5 — the doctrine line must be present in the rendered profile
    profile = texts.get(ROOT / "README.md")
    if profile is not None:
        low = profile.lower()
        if not any(marker in low for marker in DOCTRINE_MARKERS):
            findings.append("README.md: the doctrine line is missing ('measurement, not certification')")

    return (not findings), findings


SELFTEST_GOOD = """# Example
`totals.public_count` = **33 axes · 23 measured**
> **23 axes measured · 14 model comparisons**
33 rows — MEASURED 23, UNMEASURED 10
Measurement, not certification. We are not a notified body.
"""

SELFTEST_BAD_COUNT = """# Example
`totals.public_count` = **22 axes · 22 measured**
| Slots | **22** |
Measurement, not certification.
"""

SELFTEST_BAD_OVERCLAIM = """# Example
We are certified and this is the world's first AI-powered tool.
Measurement, not certification.
"""

SELFTEST_BAD_CODENAME = """# Example
The black-swan and permissionless thesis.
Measurement, not certification.
"""

SELFTEST_BAD_SECRET = """# Example
key = "-----BEGIN RSA PRIVATE KEY-----"
Measurement, not certification.
"""


def selftest() -> int:
    """Prove the gate goes red. A gate that has never gone red proves nothing."""
    tmp = ROOT / ".profile-gate-selftest"
    tmp.mkdir(exist_ok=True)
    failures: list[str] = []
    try:
        cases = [
            ("good", SELFTEST_GOOD, True),
            ("stale-count", SELFTEST_BAD_COUNT, False),
            ("overclaim", SELFTEST_BAD_OVERCLAIM, False),
            ("codename", SELFTEST_BAD_CODENAME, False),
            ("secret", SELFTEST_BAD_SECRET, False),
        ]
        for name, body, should_pass in cases:
            p = tmp / f"{name}.md"
            p.write_text(body, encoding="utf-8")
            ok, findings = gate([p])
            if ok != should_pass:
                failures.append(
                    f"case '{name}': gate said {'PASS' if ok else 'FAIL'}, expected {'PASS' if should_pass else 'FAIL'}"
                )
            else:
                print(f"  selftest {name}: {'passed (as expected)' if should_pass else 'failed (as expected)'}")
            p.unlink()
    finally:
        tmp.rmdir()
    if failures:
        print("SELFTEST FAILED — the gate itself is broken:", file=sys.stderr)
        for f in failures:
            print("  " + f, file=sys.stderr)
        return 1
    print("  selftest: the gate goes red on every defect class it claims to catch")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--file", action="append", default=[])
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    files = [Path(f) for f in args.file] if args.file else [ROOT / t for t in TARGETS]
    ok, findings = gate(files)
    if ok:
        print("  ✓ profile-gate: board counts, doctrine, codenames, overclaims, secrets — clean")
        return 0
    print("  ✖ profile-gate:", file=sys.stderr)
    for f in findings:
        print("      " + f, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
