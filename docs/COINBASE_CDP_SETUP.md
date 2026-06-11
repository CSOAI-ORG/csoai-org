# Coinbase CDP Wallet Setup for x402 Monetization

This guide walks you through creating a Coinbase CDP (Coinbase Developer Platform) wallet, getting your receiving address, and configuring the x402 payment wrap for the CSOAI Gateway MCP.

---

## Step 1: Create a CDP Wallet

### Option A: Coinbase Developer Platform (Web UI)

1. Go to [https://portal.cdp.coinbase.com](https://portal.cdp.coinbase.com)
2. Sign in with your Coinbase account (or create one)
3. Navigate to **Wallets** → **Create Wallet**
4. Select **Base** as the network (Base mainnet = `eip155:8453`)
5. Choose **Server-Signer** (recommended for automated MCP billing) or **User-Managed**
6. Save the **Wallet ID** and **Seed** (if user-managed) in your password manager

### Option B: CDP SDK (Programmatic)

```bash
# Install the CDP SDK
npm install -g @coinbase/cdp

# Or via Python
pip install cdp-sdk
```

```python
from cdp import Cdp, Wallet

Cdp.configure("your-api-key-name", "your-api-key-private-key")

# Create a wallet on Base mainnet
wallet = Wallet.create(network="base-mainnet")
print("Wallet ID:", wallet.id)
print("Address:", wallet.default_address.address_id)
```

---

## Step 2: Get Your Receiving Address

Your receiving address is the Base mainnet address where USDC payments will land.

```bash
# Via CDP CLI
cdp wallet list
cdp wallet address --wallet-id <WALLET_ID>
```

The address looks like: `0xAbC123...dEf456`

**This is your `X402_PAY_TO` value.**

---

## Step 3: Fund the Wallet with a Small Amount of ETH (for gas)

x402 payments are USDC, but the facilitator needs a tiny amount of ETH on Base for gas. Send ~$1-2 worth of ETH to your wallet address via:

- Coinbase exchange (withdraw to Base)
- Any Base bridge

---

## Step 4: Configure the x402 Gateway Wrap

Set these environment variables on your Cloud Run services (or local `.env`):

```bash
# Required
export X402_ENABLED=1
export X402_PAY_TO=0xYOUR_CDP_WALLET_ADDRESS

# Optional (defaults shown)
export X402_NETWORK=eip155:8453          # Base mainnet
export X402_FACILITATOR_URL=https://x402.org/facilitator
export X402_TIMEOUT=300                  # Payment expiry in seconds
```

For Cloud Run, use secrets:

```bash
gcloud secrets create x402-wallet \
  --data-file=- <<< '{"pay-to":"0xYOUR_ADDRESS"}' \
  --project meok-498012

# Reference in your cloudrun-*.yaml:
# env:
#   - name: X402_PAY_TO
#     valueFrom:
#       secretKeyRef:
#         name: x402-wallet
#         key: pay-to
```

---

## Step 5: Test with a Small USDC Payment

### 5.1 Get Test USDC (Base Sepolia)

For testing on Base Sepolia testnet (`eip155:84532`):

```bash
export X402_NETWORK=eip155:84532
```

Get test USDC from the [Base Sepolia Faucet](https://www.coinbase.com/faucets/base-sepolia-faucet) or [Alchemy Faucet](https://basefaucet.com/).

### 5.2 Send a Test Payment

Use the x402 client SDK:

```bash
npm install x402
```

```javascript
import { createPaymentClient } from "x402";

const client = createPaymentClient({
  wallet: yourCdpWallet,  // CDP wallet instance
  network: "eip155:84532", // or 8453 for mainnet
});

// Call a paywalled tool — the client auto-handles the 402 challenge
const result = await client.fetch("https://your-gateway.run.app/mcp", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    jsonrpc: "2.0",
    id: 1,
    method: "tools/call",
    params: {
      name: "get_compliance_map",
      arguments: { region: "eu" },
    },
  }),
});

console.log(await result.json());
```

### 5.3 Verify Payment Settlement

Check your CDP wallet balance:

```bash
cdp wallet balance --wallet-id <WALLET_ID>
```

Or view on [BaseScan](https://basescan.org) by searching your wallet address.

---

## Step 6: Go Live on Mainnet

1. Switch `X402_NETWORK` to `eip155:8453` (Base mainnet)
2. Ensure your wallet has a small ETH balance for gas
3. The first real USDC payment will auto-list your endpoint in the x402 Bazaar

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "Payment required" loop | Client not sending `_meta["x402/payment"]` — verify x402 client version |
| "verification failed" | Wrong network or insufficient USDC balance |
| "settle failed" | Wallet lacks ETH for gas; fund with $1-2 ETH on Base |
| Cloud Run 500 | Check `X402_PAY_TO` is set and valid Base address |

---

**CSOAI LTD (UK CH 16939677) · MIT**
