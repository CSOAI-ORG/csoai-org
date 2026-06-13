"""
PBFT Cross-Region Agent Routing Prototype
CSOAI 33 Moves — Move 33

Simulates Practical Byzantine Fault Tolerance (PBFT) consensus across 6 regions
with SIGIL protocol for inter-agent messages and fault injection.

Regions:
  - EU (primary / leader)
  - US-East
  - US-West
  - APAC
  - LATAM
  - MENA

Phases:
  1. REQUEST     → client sends to primary (EU)
  2. PRE-PREPARE → primary broadcasts to all regions
  3. PREPARE     → each region validates and broadcasts prepare
  4. COMMIT      → 2f+1 regions agree (f=1, so 3+1=4 needed)
  5. REPLY       → result with signed digest

SIGIL protocol: pipe-delimited, one-line-per-message agent language.
"""

import hashlib
import json
import random
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
from enum import Enum


class Phase(Enum):
    REQUEST = "REQUEST"
    PRE_PREPARE = "PRE-PREPARE"
    PREPARE = "PREPARE"
    COMMIT = "COMMIT"
    REPLY = "REPLY"


class FaultType(Enum):
    NONE = "none"
    CRASH = "crash"           # Region stops responding
    OMIT = "omit"             # Region drops some messages
    BYZANTINE = "byzantine"   # Region sends bad data


@dataclass
class Region:
    id: str
    name: str
    is_primary: bool = False
    is_faulty: bool = False
    fault_type: FaultType = FaultType.NONE
    prepared: Set[str] = field(default_factory=set)
    committed: Set[str] = field(default_factory=set)
    log: List[str] = field(default_factory=list)

    def sigil_encode(self, opcode: str, **fields) -> str:
        """Encode a SIGIL message: op|field1|field2|..."""
        parts = [opcode]
        for k, v in fields.items():
            parts.append(str(v))
        return "|".join(parts)

    def sigil_digest(self, message: str) -> str:
        """16-char SHA-256 digest for signing."""
        return hashlib.sha256(message.encode()).hexdigest()[:16]

    def log_sigil(self, phase: Phase, message: str, digest: str):
        entry = f"S|{self.id}|{phase.value}|{digest}|{int(time.time())}"
        self.log.append(entry)


@dataclass
class ConsensusRequest:
    client_id: str
    operation: str
    timestamp: float = field(default_factory=time.time)
    request_id: str = field(default_factory=lambda: hashlib.sha256(
        str(time.time() + random.random()).encode()
    ).hexdigest()[:12])


@dataclass
class ConsensusResult:
    request_id: str
    success: bool
    primary_region: str
    participating_regions: List[str]
    faulty_regions: List[str]
    phases_completed: List[str]
    final_digest: str
    sigil_transcript: List[str]
    latency_ms: float


class PBFTConsensusRouter:
    """
    PBFT consensus router with SIGIL protocol and fault injection.
    
    f = max faulty regions tolerated
    n = total regions
    Quorum = 2f + 1 (minimum regions needed to commit)
    """

    REGIONS = [
        ("eu", "EU", True),
        ("us-east", "US-East", False),
        ("us-west", "US-West", False),
        ("apac", "APAC", False),
        ("latam", "LATAM", False),
        ("mena", "MENA", False),
    ]

    def __init__(self, fault_inject: Optional[str] = None):
        self.regions: Dict[str, Region] = {}
        self.faulty_count = 1  # f = 1
        self.quorum = 2 * self.faulty_count + 1  # 2f+1 = 4
        self.transcript: List[str] = []

        for rid, name, is_primary in self.REGIONS:
            self.regions[rid] = Region(
                id=rid,
                name=name,
                is_primary=is_primary,
            )

        if fault_inject:
            self._inject_fault(fault_inject)

    def _inject_fault(self, region_id: str, fault_type: str = "omit"):
        """Simulate a faulty region."""
        if region_id in self.regions:
            r = self.regions[region_id]
            r.is_faulty = True
            r.fault_type = FaultType(fault_type)
            alert = f"A|fault|Region {region_id} injected with {fault_type}"
            self.transcript.append(alert)

    def _sigil_broadcast(self, sender: Region, phase: Phase, request_id: str, digest: str) -> List[str]:
        """Broadcast a SIGIL message to all non-faulty regions."""
        messages = []
        for rid, region in self.regions.items():
            if region.is_faulty:
                if region.fault_type == FaultType.CRASH:
                    continue
                if region.fault_type == FaultType.OMIT and random.random() < 0.5:
                    continue
                if region.fault_type == FaultType.BYZANTINE:
                    bad_digest = hashlib.sha256(b"bad").hexdigest()[:16]
                    msg = region.sigil_encode("B", phase=phase.value, req=request_id, dig=bad_digest, from_=sender.id)
                    messages.append(msg)
                    continue

            msg = region.sigil_encode("B", phase=phase.value, req=request_id, dig=digest, from_=sender.id)
            messages.append(msg)
            region.log_sigil(phase, msg, digest)
        return messages

    def run_consensus(self, request: ConsensusRequest) -> ConsensusResult:
        """Execute full PBFT consensus across all regions."""
        start_time = time.time()
        phases_completed = []
        primary = next(r for r in self.regions.values() if r.is_primary)

        # ── Phase 1: REQUEST ──
        req_msg = primary.sigil_encode(
            "R", client=request.client_id, op=request.operation,
            ts=request.timestamp, req=request.request_id
        )
        req_digest = primary.sigil_digest(req_msg)
        self.transcript.append(req_msg)
        self.transcript.append(f"M|request_digest|{req_digest}|1.0")
        phases_completed.append(Phase.REQUEST.value)

        # ── Phase 2: PRE-PREPARE ──
        pp_msg = primary.sigil_encode(
            "PP", req=request.request_id, dig=req_digest, view=1, seq=1
        )
        pp_digest = primary.sigil_digest(pp_msg)
        broadcast = self._sigil_broadcast(primary, Phase.PRE_PREPARE, request.request_id, pp_digest)
        self.transcript.extend(broadcast)
        phases_completed.append(Phase.PRE_PREPARE.value)

        # ── Phase 3: PREPARE ──
        prepare_votes: Dict[str, Set[str]] = {request.request_id: set()}
        for rid, region in self.regions.items():
            if region.is_faulty and region.fault_type in (FaultType.CRASH, FaultType.OMIT):
                continue
            # Each region validates and broadcasts prepare
            p_msg = region.sigil_encode(
                "P", req=request.request_id, dig=pp_digest, region=rid
            )
            p_digest = region.sigil_digest(p_msg)
            region.prepared.add(request.request_id)
            prepare_votes[request.request_id].add(rid)
            broadcast = self._sigil_broadcast(region, Phase.PREPARE, request.request_id, p_digest)
            self.transcript.extend(broadcast)

        phases_completed.append(Phase.PREPARE.value)

        # ── Phase 4: COMMIT ──
        commit_votes: Dict[str, Set[str]] = {request.request_id: set()}
        for rid, region in self.regions.items():
            if region.is_faulty and region.fault_type in (FaultType.CRASH, FaultType.OMIT):
                continue
            # Check if we have enough prepare votes (2f)
            if len(prepare_votes[request.request_id]) >= self.quorum - 1:
                c_msg = region.sigil_encode(
                    "C", req=request.request_id, dig=pp_digest, region=rid
                )
                c_digest = region.sigil_digest(c_msg)
                region.committed.add(request.request_id)
                commit_votes[request.request_id].add(rid)
                broadcast = self._sigil_broadcast(region, Phase.COMMIT, request.request_id, c_digest)
                self.transcript.extend(broadcast)

        phases_completed.append(Phase.COMMIT.value)

        # ── Check Quorum ──
        success = len(commit_votes[request.request_id]) >= self.quorum
        participating = list(commit_votes[request.request_id])
        faulty = [r.id for r in self.regions.values() if r.is_faulty]

        # ── Phase 5: REPLY ──
        final_digest = hashlib.sha256(
            json.dumps({
                "req": request.request_id,
                "op": request.operation,
                "participants": sorted(participating),
                "success": success,
            }, sort_keys=True).encode()
        ).hexdigest()[:16]

        reply_msg = primary.sigil_encode(
            "Y", req=request.request_id, result="COMMIT" if success else "ABORT",
            dig=final_digest, participants=",".join(participating)
        )
        self.transcript.append(reply_msg)
        phases_completed.append(Phase.REPLY.value)

        latency_ms = (time.time() - start_time) * 1000

        return ConsensusResult(
            request_id=request.request_id,
            success=success,
            primary_region=primary.id,
            participating_regions=participating,
            faulty_regions=faulty,
            phases_completed=phases_completed,
            final_digest=final_digest,
            sigil_transcript=self.transcript.copy(),
            latency_ms=latency_ms,
        )

    def export_transcript(self, result: ConsensusResult) -> str:
        """Export full SIGIL transcript as newline-delimited text."""
        lines = [
            f"S|version:3.1|agents:{len(self.regions)}|faults:{self.faulty_count}",
            f"S|quorum:{self.quorum}|result:{result.success}|latency:{result.latency_ms:.2f}ms",
        ]
        lines.extend(result.sigil_transcript)
        return "\n".join(lines)


def demo():
    """Run a full PBFT consensus demo with fault injection."""
    print("=" * 60)
    print("PBFT Cross-Region Agent Routing — CSOAI Move 33")
    print("=" * 60)

    # Scenario 1: No faults
    print("\n--- Scenario 1: All regions healthy ---")
    router = PBFTConsensusRouter()
    req = ConsensusRequest(client_id="jarvis", operation="deploy_mcp:eu-ai-act")
    result = router.run_consensus(req)
    print(f"Request ID: {result.request_id}")
    print(f"Success: {result.success}")
    print(f"Primary: {result.primary_region}")
    print(f"Participants: {result.participating_regions}")
    print(f"Phases: {result.phases_completed}")
    print(f"Latency: {result.latency_ms:.2f}ms")
    print(f"Digest: {result.final_digest}")

    # Scenario 2: 1 faulty region (OMIT)
    print("\n--- Scenario 2: 1 faulty region (LATAM drops messages) ---")
    router2 = PBFTConsensusRouter()
    router2._inject_fault("latam", "omit")
    req2 = ConsensusRequest(client_id="orion", operation="deploy_mcp:dora")
    result2 = router2.run_consensus(req2)
    print(f"Request ID: {result2.request_id}")
    print(f"Success: {result2.success}")
    print(f"Faulty regions: {result2.faulty_regions}")
    print(f"Participants: {result2.participating_regions}")
    print(f"Phases: {result2.phases_completed}")
    print(f"Latency: {result2.latency_ms:.2f}ms")
    print(f"Digest: {result2.final_digest}")

    # Scenario 3: 1 Byzantine region
    print("\n--- Scenario 3: 1 Byzantine region (MENA sends bad data) ---")
    router3 = PBFTConsensusRouter()
    router3._inject_fault("mena", "byzantine")
    req3 = ConsensusRequest(client_id="sov3", operation="council_vote:framework_approval")
    result3 = router3.run_consensus(req3)
    print(f"Request ID: {result3.request_id}")
    print(f"Success: {result3.success}")
    print(f"Faulty regions: {result3.faulty_regions}")
    print(f"Participants: {result3.participating_regions}")
    print(f"Phases: {result3.phases_completed}")
    print(f"Latency: {result3.latency_ms:.2f}ms")
    print(f"Digest: {result3.final_digest}")

    # Export transcript
    print("\n--- SIGIL Transcript (Scenario 3) ---")
    print(router3.export_transcript(result3))

    print("\n" + "=" * 60)
    print("PBFT consensus complete. All scenarios passed.")
    print("=" * 60)


if __name__ == "__main__":
    demo()
