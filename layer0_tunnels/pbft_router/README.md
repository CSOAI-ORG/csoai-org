# PBFT Cross-Region Agent Routing Prototype

> **Move 33** — PBFT Consensus + SIGIL Protocol for CSOAI v3.1

## Overview

This prototype simulates **Practical Byzantine Fault Tolerance (PBFT)** consensus across 6 global regions, using the **SIGIL** inter-agent protocol for all message passing.

**Regions:**
| ID | Name | Role |
|----|------|------|
| `eu` | EU | Primary (leader) |
| `us-east` | US-East | Replica |
| `us-west` | US-West | Replica |
| `apac` | APAC | Replica |
| `latam` | LATAM | Replica |
| `mena` | MENA | Replica |

**Fault Model:**
- `f = 1` (max faulty regions tolerated)
- Quorum = `2f + 1 = 4` regions needed to commit
- Fault types: `crash`, `omit`, `byzantine`

## Architecture

```
Client → REQUEST → Primary (EU)
  Primary → PRE-PREPARE → All Regions
    Each Region → PREPARE → All Regions
      2f+1 Regions → COMMIT → All Regions
        Primary → REPLY → Client (signed digest)
```

## SIGIL Protocol

All messages use SIGIL v0.1 pipe-delimited format:

```
R|jarvis|deploy_mcp:eu-ai-act|1718112000.0|a3f7b2d9e8c1
PP|a3f7b2d9e8c1|8cc4a6002bb8201a|1|1
P|a3f7b2d9e8c1|8cc4a6002bb8201a|us-east
C|a3f7b2d9e8c1|8cc4a6002bb8201a|us-east
Y|a3f7b2d9e8c1|COMMIT|f2e8d1c9b7a3|eu,us-east,us-west,apac
```

| Op | Meaning |
|----|---------|
| `R` | REQUEST from client |
| `PP` | PRE-PREPARE from primary |
| `P` | PREPARE from replica |
| `C` | COMMIT from replica |
| `Y` | REPLY (result) |
| `B` | BROADCAST envelope |
| `A` | ALERT (fault injection) |
| `S` | STATE / audit log |
| `M` | MEMORY (digest record) |

## Quick Start

```bash
cd /Users/nicholas/clawd/csoai-org/layer0_tunnels/pbft_router

# No dependencies needed (stdlib only)
python3 router.py
```

## Demo Output

The demo runs 3 scenarios:
1. **All healthy** — 6 regions, 0 faults, consensus in ~4ms
2. **1 omit fault** — LATAM drops 50% of messages, still reaches quorum
3. **1 Byzantine fault** — MENA sends bad digests, detected and excluded

## API Usage

```python
from router import PBFTConsensusRouter, ConsensusRequest

# Create router with 1 faulty region
router = PBFTConsensusRouter()
router._inject_fault("latam", "omit")

# Submit request
req = ConsensusRequest(client_id="jarvis", operation="deploy_mcp:eu-ai-act")
result = router.run_consensus(req)

print(result.success)           # True
print(result.participating_regions)  # ['eu', 'us-east', 'us-west', 'apac']
print(result.final_digest)      # 16-char SHA-256

# Export full SIGIL transcript
print(router.export_transcript(result))
```

## Integration with CSOAI

This router is designed to plug into:
- `/council` page — visualize consensus rounds
- `/api/council/votes.json` — expose voting state
- `meok-sigil` — use SIGIL encode/decode for wire format
- `csoai-gateway-mcp` — route MCP calls through PBFT consensus

## Fault Injection Reference

| Type | Behavior | Detection |
|------|----------|-----------|
| `crash` | Region stops responding entirely | Timeout after 3s |
| `omit` | Region drops 50% of messages | Missing prepare/commit votes |
| `byzantine` | Region sends invalid digests | Digest mismatch on validation |

## Performance

- **Latency:** ~2–5ms for 6-region consensus (simulated)
- **Throughput:** ~200 consensus rounds/second (single-threaded)
- **Message complexity:** O(n²) per round (n = number of regions)

## Next Steps

1. Wire to real network transport (WebSocket / gRPC)
2. Add persistent state + crash recovery
3. Integrate with `meok-sigil` for full encode/decode
4. Add view-change protocol for primary failure
5. Deploy as `csoai.org/layer0/pbft` service

---
*CSOAI 33 Moves | Move 33 — PBFT Cross-Region Agent Routing*
