#!/usr/bin/env bash
# ============================================================================
# CSOAI Domain Fix — MANUAL STEPS REQUIRED
# ============================================================================
# 
# PROBLEM: csoai.org is assigned to a DIFFERENT Vercel project
# SOLUTION: Transfer domain from old project to new csoai-org project
#
# ============================================================================

echo "=== CSOAI.org Domain Transfer Guide ==="
echo ""
echo "❌ csoai.org is assigned to another Vercel project"
echo "✅ csoai-org.vercel.app is live with v3.1"
echo ""

# Check current state
echo "Current DNS:"
dig csoai.org A +short 2>/dev/null | sed 's/^/  A: /'
echo ""

cat <<'EOF'
=== STEP-BY-STEP FIX ===

STEP 1: Find the old project
----------------------------
1. Go to https://vercel.com/dashboard
2. Look for a project that might be the old csoai.org site
   (Could be named: csoai, csoai-org-v2, csoai-old, etc.)
3. Click on that project

STEP 2: Remove domain from old project
--------------------------------------
1. In the old project, go to Settings → Domains
2. Find csoai.org in the list
3. Click the "..." menu next to it
4. Select "Remove Domain"
5. Confirm removal

STEP 3: Add domain to new project
---------------------------------
1. Go to the NEW csoai-org project
2. Settings → Domains
3. Click "Add Domain"
4. Enter: csoai.org
5. Click "Add"

STEP 4: Configure DNS (if needed)
---------------------------------
Vercel will show you DNS instructions. Typically:
- Type: A
- Host: @
- Value: 76.76.21.21
- OR CNAME: cname.vercel-dns.com

In Namecheap (or your DNS provider):
1. Go to Domain List → Manage → Advanced DNS
2. Delete old A records
3. Add new A records from Vercel

STEP 5: Verify
--------------
Run:
  curl -s -I https://csoai.org | grep last-modified
Should show today's date.

Test API:
  curl -s https://csoai.org/api/map.json | head -5
Should return JSON.

=== ALTERNATIVE: If you can't find the old project ===

Contact Vercel Support:
  https://vercel.com/help

Or use Vercel CLI with the correct team:
  vercel teams ls
  vercel switch <team-with-old-project>
  vercel domains rm csoai.org
  vercel switch <your-team>
  cd /Users/nicholas/clawd/csoai-org
  vercel --prod

EOF

echo ""
echo "=== Quick Verification Commands ==="
echo "  curl -s https://csoai.org/api/map.json | python3 -m json.tool"
echo "  curl -s https://csoai.org/.well-known/agent.json | python3 -m json.tool"
echo ""
