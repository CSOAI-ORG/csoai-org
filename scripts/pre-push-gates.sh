#!/bin/bash
# Pre-push content gate for CSOAI-ORG/csoai-org.
#
# WHY. The global pre-push hook (core.hooksPath = ~/.config/git/hooks) refuses
# any push to a repo that has neither scripts/run-meok-proxy-tests.sh nor
# scripts/pre-push-gates.sh. csoai-org had neither, so EVERY push to this repo
# was blocked and the only way through was --no-verify. That is the worst
# possible shape for the repository that renders the GitHub profile of the
# organisation: the one repo where a stale number is most visible was the one
# repo nobody could push to safely.
#
# This file satisfies the hook for this repo with a gate that checks what this
# repo can actually break:
#
#   profile-gate.py  board counts in the text must equal the live board; no
#                    certification overclaim; no internal codename; no
#                    credential material; the doctrine line must be present
#
# It is fast (one HTTPS GET) and dependency-free (python3 + stdlib), because a
# gate that takes 12 minutes to run is a gate people bypass.
#
# The gate must be provably working before its verdict means anything, so the
# selftest runs first and a broken gate blocks the push.
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)" || exit 1

fail=0
echo "pre-push: profile/content gates …"

if ! python3 scripts/profile-gate.py --selftest; then
  echo "  ✖ profile-gate SELFTEST failed — the gate itself is broken; push blocked." >&2
  fail=1
fi

if [ "$fail" -eq 0 ]; then
  out=$(python3 scripts/profile-gate.py 2>&1)
  if [ $? -ne 0 ]; then
    echo "  ✖ profile-gate — its verdict:" >&2
    printf '%s\n' "$out" | tail -20 | sed 's/^/      /' >&2
    fail=1
  fi
fi

if [ "$fail" -ne 0 ]; then
  echo >&2
  echo "  Push blocked. The live board is the record:" >&2
  echo "    GET https://councilof.ai/api/gspc" >&2
  echo "  If the file and the API disagree, the API is right — fix the file." >&2
  exit 1
fi
echo "  ✓ profile-gate: clean"
exit 0
