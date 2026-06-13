from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Dict, Any, List
import uuid

# Import the Enterprise-ready SDK
from layer0_sdk import (
    CSOAIAgentIdentity,
    CSOAIWatchdogCertificate,
    CSOAIPolicyEngine,
    CSOAICrossRegionalHandoff,
    CSOAIPaymentLayer,
    CSOAIAuditLayer,
    CSOAIHumanInTheLoop,
    CSOAILegacyBridge
)

app = FastAPI(
    title="CSOAI Layer 0 Trust Infrastructure",
    description="The missing compliance, identity, and policy foundation for the Agentic Economy (A2A, MCP, x402).",
    version="1.0.0"
)

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    # In a real enterprise system, verify OIDC / SPIFFE / WIMSE token here
    if not credentials.credentials:
        raise HTTPException(status_code=401, detail="Invalid authorization token")
    return credentials.credentials

# Initialize SDK components
policy_engine = CSOAIPolicyEngine()
cross_regional = CSOAICrossRegionalHandoff()
payment_layer = CSOAIPaymentLayer()
audit_layer = CSOAIAuditLayer()
hitl_layer = CSOAIHumanInTheLoop()
legacy_bridge = CSOAILegacyBridge()

# Request Models
class PolicyEvalRequest(BaseModel):
    agent_did: str
    action_type: str
    payload: Dict[str, Any]

class PaymentPrecheckRequest(BaseModel):
    payer_did: str
    payee_did: str
    amount: float
    currency: str

class HandoffRequest(BaseModel):
    source_did: str
    target_did: str
    payload: Dict[str, Any]

# Endpoints
@app.get("/health")
async def health_check():
    return {"status": "Operational", "layers": "L0-A through L0-H active"}

@app.post("/v1/identity/register", response_model=CSOAIAgentIdentity)
async def register_agent_identity(public_key: str, controlling_entity: str):
    """Register a new W3C DID / IETF AIP compliant Agent Identity."""
    identity = CSOAIAgentIdentity(
        public_key=public_key,
        controlling_entity=controlling_entity
    )
    return identity

@app.post("/v1/policy/evaluate")
async def evaluate_policy(request: PolicyEvalRequest, token: str = Depends(verify_token)):
    """Evaluate an agent action against 30+ frameworks in sub-millisecond latency."""
    decision = policy_engine.evaluate(
        agent_action={"type": request.action_type},
        context=request.payload
    )
    
    # Anchor to audit layer
    audit_record = audit_layer.anchor_event({
        "event_type": "policy_evaluation",
        "agent": request.agent_did,
        "decision": decision
    })
    
    return {"decision": decision, "audit": audit_record}

@app.post("/v1/payment/pre-check")
async def payment_precheck(request: PaymentPrecheckRequest, token: str = Depends(verify_token)):
    """Compliance pre-check BEFORE x402, Stripe ACP, or Google AP2 execution."""
    # Mocking identities for the pre-check
    payer = CSOAIAgentIdentity(public_key="mock", controlling_entity="mock_payer")
    payee = CSOAIAgentIdentity(public_key="mock", controlling_entity="mock_payee")
    
    decision = payment_layer.pre_check_payment(
        payer=payer,
        payee=payee,
        amount=request.amount,
        currency=request.currency
    )
    
    if decision["action"] == "BLOCK":
        raise HTTPException(status_code=403, detail=decision["reason"])
        
    return decision

@app.post("/v1/handoff/cross-regional")
async def cross_regional_handoff(request: HandoffRequest, token: str = Depends(verify_token)):
    """Strictest-wins logic across jurisdictions for A2A protocols."""
    source = CSOAIAgentIdentity(public_key="mock", controlling_entity="mock")
    target = CSOAIAgentIdentity(public_key="mock", controlling_entity="mock")
    
    result = cross_regional.initiate_handoff(source, target, request.payload)
    return result

@app.post("/v1/legacy/bridge")
async def create_legacy_bridge(system_type: str, capabilities: List[str], token: str = Depends(verify_token)):
    """Bridge legacy COBOL/Mainframe to AI Agents."""
    return legacy_bridge.bridge_agent(legacy_system=system_type, capabilities=capabilities)
