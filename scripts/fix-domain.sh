#!/usr/bin/env bash
# ============================================================================
# CSOAI Domain Fix Script
# Fixes csoai.org custom domain to serve the new v3.1 site
# ============================================================================
#
# PROBLEM:
#   csoai.org serves old white/green site (last-modified: 03:33)
#   csoai-org.vercel.app serves new v3.1 site (last-modified: 14:27)
#
# ROOT CAUSE:
#   csoai.org A record points to 76.76.21.21 (old Vercel deployment)
#   Need to point to current csoai-org.vercel.app deployment
#
# FIX OPTIONS (in order of preference):
# ============================================================================

echo "=== CSOAI Domain Fix Diagnostic ==="
echo ""

# Check current state
echo "1. Checking csoai.org..."
curl -s -I https://csoai.org | grep -E "last-modified|x-vercel-id" | sed 's/^/   /'

echo ""
echo "2. Checking csoai-org.vercel.app..."
curl -s -I https://csoai-org.vercel.app | grep -E "last-modified|x-vercel-id" | sed 's/^/   /'

echo ""
echo "3. DNS Records for csoai.org..."
dig csoai.org A +short 2>/dev/null | sed 's/^/   A: /'
dig csoai.org CNAME +short 2>/dev/null | sed 's/^/   CNAME: /'

echo ""
echo "=== FIX INSTRUCTIONS ==="
echo ""

cat <<'EOF'
OPTION A: Vercel Dashboard (Recommended — 5 minutes)
----------------------------------------------------
1. Go to https://vercel.com/dashboard
2. Select the "csoai-org" project
3. Go to Settings → Domains
4. If csoai.org is listed:
   - Click "Refresh" or "Verify"
   - If it shows "Invalid Configuration", remove and re-add
5. If csoai.org is NOT listed:
   - Click "Add Domain"
   - Enter: csoai.org
   - Vercel will show DNS instructions
6. In Namecheap (or your DNS provider):
   - Remove A record: 76.76.21.21
   - Add CNAME record:
     - Type: CNAME
     - Host: @
     - Value: cname.vercel-dns.com
     - TTL: Automatic
   - OR use Vercel's recommended A records:
     - 76.76.21.21 (this is what you currently have — but may be stale)
     - 76.76.21.98

OPTION B: Vercel CLI (if you have auth)
----------------------------------------
  cd /Users/nicholas/clawd/csoai-org
  npx vercel --prod
  npx vercel domains add csoai.org

OPTION C: GitHub Actions (Already working)
------------------------------------------
  The GitHub Actions workflow is already deploying successfully.
  The issue is purely DNS/domain configuration, not the build.

OPTION D: Force Rebuild + Redeploy
----------------------------------
  If the domain IS configured correctly in Vercel but serving stale content:
  1. Go to Vercel Dashboard → csoai-org → Deployments
  2. Find the latest deployment (should be commit 1e92cf1)
  3. Click "Promote to Production"
  4. Or run: cd /Users/nicholas/clawd/csoai-org && npx vercel --prod

VERIFICATION:
-------------
  After fix, run:
    curl -s -I https://csoai.org | grep last-modified
  Should show: Thu, 11 Jun 2026 14:27:XX GMT (or newer)

  Test API:
    curl -s https://csoai.org/api/map.json | head -5
  Should return JSON, not 404.

EOF

echo ""
echo "=== Quick Test Commands ==="
echo "  curl -s https://csoai.org/api/map.json | python3 -m json.tool"
echo "  curl -s https://csoai.org/.well-known/agent.json | python3 -m json.tool"
echo "  curl -s https://csoai.org/api/dome/status.json | python3 -m json.tool"
echo ""
