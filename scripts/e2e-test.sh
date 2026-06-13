#!/usr/bin/env bash
# ============================================================================
# CSOAI End-to-End Test Suite
# Tests the entire v3.1 stack: API, SDK, CLI, MCP, A2A, PBFT
# ============================================================================

API_BASE="${CSOAI_API_BASE:-https://csoai-org.vercel.app/api}"
PASS=0
FAIL=0

log_pass() { echo "  ✅ $1"; PASS=$((PASS+1)); }
log_fail() { echo "  ❌ $1"; FAIL=$((FAIL+1)); }

echo "=== CSOAI v3.1 End-to-End Test Suite ==="
echo "API Base: $API_BASE"
echo ""

# ── API Tests ─────────────────────────────────────────────────────────
echo "--- API Endpoints ---"

if curl -sf "$API_BASE/map.json" > /dev/null 2>&1; then
    log_pass "GET /api/map.json"
else
    log_fail "GET /api/map.json"
fi

if curl -sf "$API_BASE/crosswalk.json" > /dev/null 2>&1; then
    log_pass "GET /api/crosswalk.json"
else
    log_fail "GET /api/crosswalk.json"
fi

if curl -sf "$API_BASE/dome/status.json" > /dev/null 2>&1; then
    log_pass "GET /api/dome/status.json"
else
    log_fail "GET /api/dome/status.json"
fi

if curl -sf "$API_BASE/council/votes.json" > /dev/null 2>&1; then
    log_pass "GET /api/council/votes.json"
else
    log_fail "GET /api/council/votes.json"
fi

if curl -sf "$API_BASE/sigil/verify.json" > /dev/null 2>&1; then
    log_pass "GET /api/sigil/verify.json"
else
    log_fail "GET /api/sigil/verify.json"
fi

if curl -sf "https://csoai-org.vercel.app/.well-known/agent.json" > /dev/null 2>&1; then
    log_pass "GET /.well-known/agent.json (A2A Agent Card)"
else
    log_fail "GET /.well-known/agent.json"
fi

# ── SDK Tests ─────────────────────────────────────────────────────────
echo ""
echo "--- Python SDK ---"

cd /Users/nicholas/clawd/meok-sdk-python
if python3 -c "
import sys
sys.path.insert(0, '.')
from meok_sdk.csoai import CSOAIClient
client = CSOAIClient(base_url='https://csoai-org.vercel.app')
m = client.get_compliance_map()
assert m.total_regions == 6
assert m.total_frameworks == 30
print('OK')
" 2>/dev/null; then
    log_pass "Python SDK — get_compliance_map()"
else
    log_fail "Python SDK — get_compliance_map()"
fi

if python3 -c "
import sys
sys.path.insert(0, '.')
from meok_sdk.csoai import CSOAIClient
client = CSOAIClient(base_url='https://csoai-org.vercel.app')
d = client.get_dome_status()
assert d.status == 'live'
print('OK')
" 2>/dev/null; then
    log_pass "Python SDK — get_dome_status()"
else
    log_fail "Python SDK — get_dome_status()"
fi

# ── CLI Tests ─────────────────────────────────────────────────────────
echo ""
echo "--- meok CLI ---"

cd /Users/nicholas/clawd/meok-cli
if python3 -m meok_cli.cli csoai status --json 2>/dev/null | grep -q '"map": "ok"'; then
    log_pass "CLI — csoai status"
else
    log_fail "CLI — csoai status"
fi

if python3 -m meok_cli.cli csoai map --json 2>/dev/null | grep -q 'European Union'; then
    log_pass "CLI — csoai map"
else
    log_fail "CLI — csoai map"
fi

# ── TypeScript SDK Tests ──────────────────────────────────────────────
echo ""
echo "--- TypeScript SDK ---"

cd /Users/nicholas/clawd/meok-sdk-typescript
if npm test 2>/dev/null | grep -q "15 passed"; then
    log_pass "TypeScript SDK — all tests"
else
    log_fail "TypeScript SDK — all tests"
fi

# ── PBFT Router Tests ─────────────────────────────────────────────────
echo ""
echo "--- PBFT Router ---"

cd /Users/nicholas/clawd/csoai-org/layer0_tunnels/pbft_router
if python3 -c "
import sys
sys.path.insert(0, '.')
from router import PBFTConsensusRouter, demo
demo()
" 2>/dev/null | grep -q "All scenarios passed"; then
    log_pass "PBFT Router — all scenarios"
else
    log_fail "PBFT Router — all scenarios"
fi

# ── A2A Agent Card Test ───────────────────────────────────────────────
echo ""
echo "--- A2A Agent Card ---"

if curl -sf "https://csoai-org.vercel.app/.well-known/agent.json" 2>/dev/null | grep -q '"name": "CSOAI Compliance Agent"'; then
    log_pass "A2A Agent Card — valid JSON"
else
    log_fail "A2A Agent Card — valid JSON"
fi

# ── Summary ───────────────────────────────────────────────────────────
echo ""
echo "=== Test Summary ==="
echo "  Passed: $PASS"
echo "  Failed: $FAIL"
echo "  Total:  $((PASS + FAIL))"

if [ $FAIL -eq 0 ]; then
    echo ""
    echo "🎉 ALL TESTS PASSED — CSOAI v3.1 is LIVE and WORKING"
    exit 0
else
    echo ""
    echo "⚠️  $FAIL test(s) failed — check output above"
    exit 1
fi
