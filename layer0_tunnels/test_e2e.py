import asyncio
from fastapi.testclient import TestClient
import uuid

# Suppress warnings for testing purposes
import warnings
warnings.filterwarnings("ignore")

# Import the FastAPI app
try:
    from main import app
    client = TestClient(app)
    print("✅ FastAPI application loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load FastAPI app: {e}")
    exit(1)

def run_tests():
    print("\n--- Starting E2E API Tests ---")
    
    # 1. Health Check
    try:
        response = client.get("/health")
        assert response.status_code == 200
        print("✅ Health Check passed.")
    except Exception as e:
        print(f"❌ Health Check failed: {e}")

    # 2. Register Agent Identity (L0-A)
    agent_did = None
    try:
        response = client.post(
            "/v1/identity/register",
            params={"public_key": "test_pub_key", "controlling_entity": "test_entity"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "agent_id" in data
        agent_did = f"did:csoai:{data['agent_id']}"
        print(f"✅ Agent Identity registered. DID: {agent_did}")
    except Exception as e:
        print(f"❌ Agent Registration failed: {e}")

    # 3. Policy Evaluation (L0-C)
    try:
        headers = {"Authorization": "Bearer test_token"}
        payload = {
            "agent_did": agent_did or f"did:csoai:{uuid.uuid4()}",
            "action_type": "data_transfer",
            "payload": {"region": "EU", "data_type": "PII"}
        }
        response = client.post("/v1/policy/evaluate", json=payload, headers=headers)
        assert response.status_code == 200
        print("✅ Policy Evaluation passed.")
    except Exception as e:
        print(f"❌ Policy Evaluation failed: {e}")

    # 4. Payment Pre-Check (L0-E)
    try:
        headers = {"Authorization": "Bearer test_token"}
        payload = {
            "payer_did": agent_did or f"did:csoai:{uuid.uuid4()}",
            "payee_did": f"did:csoai:{uuid.uuid4()}",
            "amount": 100.50,
            "currency": "GBP"
        }
        response = client.post("/v1/payment/pre-check", json=payload, headers=headers)
        assert response.status_code in [200, 403] # Depending on mock data
        print("✅ Payment Pre-check passed.")
    except Exception as e:
        print(f"❌ Payment Pre-check failed: {e}")
        
    print("--- Tests Complete ---\n")

if __name__ == "__main__":
    run_tests()
