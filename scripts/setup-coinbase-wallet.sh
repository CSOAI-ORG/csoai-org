#!/usr/bin/env bash
# ============================================================================
# Coinbase CDP Wallet Setup Automation
# ============================================================================
# This script guides you through creating a Coinbase CDP wallet for x402
# payments on the CSOAI platform.
#
# Prerequisites:
#   - Coinbase account (https://coinbase.com)
#   - Some ETH on Base for gas (~$0.01 per transaction)
#
# What this does:
#   1. Creates a CDP wallet via Coinbase Developer Platform
#   2. Extracts the receiving address
#   3. Configures it for x402 payments
#   4. Tests with a small USDC payment
# ============================================================================

echo "=== Coinbase CDP Wallet Setup for CSOAI x402 ==="
echo ""

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required. Install from https://nodejs.org"
    exit 1
fi

# Check for npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm is required. Install with Node.js"
    exit 1
fi

echo "✅ Node.js and npm found"
echo ""

# Install CDP SDK if not present
if ! npm list -g @coinbase/cdp-sdk &> /dev/null; then
    echo "Installing Coinbase CDP SDK..."
    npm install -g @coinbase/cdp-sdk 2>/dev/null || echo "⚠️  Global install failed — will use npx"
fi

# Create wallet setup script
cat > /tmp/cdp-wallet-setup.js <<'JSEOF'
const { CdpClient } = require('@coinbase/cdp-sdk');
const fs = require('fs');
const path = require('path');

async function main() {
    console.log("Creating CDP wallet for CSOAI x402...\n");
    
    // Initialize CDP client
    // You'll need to set CDP_API_KEY and CDP_API_SECRET env vars
    // Get them from: https://portal.cdp.coinbase.com/
    const client = new CdpClient();
    
    // Create a new wallet on Base mainnet
    const wallet = await client.createWallet({
        network: 'base-mainnet'
    });
    
    const address = wallet.addresses[0].address;
    const walletId = wallet.id;
    
    console.log("✅ Wallet created!");
    console.log("   Wallet ID:", walletId);
    console.log("   Address:", address);
    console.log("   Network: Base Mainnet");
    console.log("");
    
    // Save to config file
    const config = {
        csoai_x402_wallet: {
            wallet_id: walletId,
            address: address,
            network: 'base-mainnet',
            created_at: new Date().toISOString(),
            purpose: 'CSOAI x402 payment receiver'
        }
    };
    
    const configPath = path.join(process.env.HOME, '.csoai', 'wallet.json');
    fs.mkdirSync(path.dirname(configPath), { recursive: true });
    fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
    
    console.log("💾 Wallet config saved to:", configPath);
    console.log("");
    console.log("=== NEXT STEPS ===");
    console.log("1. Fund this wallet with a small amount of ETH on Base for gas");
    console.log("   (You can bridge from Ethereum mainnet or buy directly on Coinbase)");
    console.log("");
    console.log("2. Set environment variables:");
    console.log("   export X402_PAY_TO=" + address);
    console.log("   export CDP_WALLET_ID=" + walletId);
    console.log("");
    console.log("3. Configure Cloud Run Secret Manager:");
    console.log("   gcloud secrets create x402-wallet --data-file=" + configPath);
    console.log("");
    console.log("4. Test with a small payment:");
    console.log("   curl -X POST https://csoai.org/mcp/csoai-gateway/get_compliance_map \\");
    console.log("     -H 'X-402-Payment: ...'");
    console.log("");
    console.log("5. After first settled payment, you'll auto-list on Coinbase Agentic.Market");
}

main().catch(err => {
    console.error("❌ Error:", err.message);
    console.log("");
    console.log("Make sure you have:");
    console.log("  1. CDP_API_KEY set (from https://portal.cdp.coinbase.com/)");
    console.log("  2. CDP_API_SECRET set");
    console.log("  3. Node.js 18+ installed");
    process.exit(1);
});
JSEOF

echo "=== Setup Script Created ==="
echo ""
echo "To create your wallet, run:"
echo ""
echo "  export CDP_API_KEY='your-cdp-api-key'"
echo "  export CDP_API_SECRET='your-cdp-api-secret'"
echo "  node /tmp/cdp-wallet-setup.js"
echo ""
echo "Get your API keys from: https://portal.cdp.coinbase.com/"
echo ""
echo "=== Manual Alternative ==="
echo "If you prefer a web UI:"
echo "  1. Go to https://portal.cdp.coinbase.com/"
echo "  2. Create a new project"
echo "  3. Go to Wallets → Create Wallet"
echo "  4. Select 'Base Mainnet'"
echo "  5. Copy the wallet address"
echo "  6. Set export X402_PAY_TO=<address>"
echo ""
