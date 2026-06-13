#!/usr/bin/env bash
set -euo pipefail

# Manual one-off deployment to Vercel for local use.
# Requires: vercel CLI installed (npm i -g vercel)
# Override defaults by setting env vars or passing arguments.

VERCEL_TOKEN="${VERCEL_TOKEN:-}"
VERCEL_ORG_ID="${VERCEL_ORG_ID:-team_4IkNIyYl7TtEOi9aoz17SUO7}"
VERCEL_PROJECT_ID="${VERCEL_PROJECT_ID:-prj_T9nqKwDGm0FHrq8nF6m9LcuwELh2}"

if [ -z "$VERCEL_TOKEN" ]; then
  echo "Error: VERCEL_TOKEN is not set."
  echo "Usage: VERCEL_TOKEN=<token> ./deploy.sh"
  exit 1
fi

echo "→ Checking if project ${VERCEL_PROJECT_ID} exists..."
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" \
  "https://api.vercel.com/v9/projects/${VERCEL_PROJECT_ID}?teamId=${VERCEL_ORG_ID}" \
  -H "Authorization: Bearer ${VERCEL_TOKEN}")

if [ "$HTTP_STATUS" = "404" ]; then
  echo "→ Project not found. Creating project 'csoai-org'..."
  curl -s -X POST "https://api.vercel.com/v9/projects?teamId=${VERCEL_ORG_ID}" \
    -H "Authorization: Bearer ${VERCEL_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{"name":"csoai-org","framework":null}'
  echo ""
  echo "→ Project created."
elif [ "$HTTP_STATUS" != "200" ]; then
  echo "⚠ Warning: Unexpected status ${HTTP_STATUS} when checking project."
else
  echo "→ Project exists."
fi

echo "→ Pulling Vercel environment info..."
vercel pull --yes --environment=production \
  --token="$VERCEL_TOKEN" \
  --scope="$VERCEL_ORG_ID"

echo "→ Building project artifacts..."
vercel build --prod \
  --token="$VERCEL_TOKEN" \
  --scope="$VERCEL_ORG_ID"

echo "→ Deploying to Vercel..."
vercel deploy --prebuilt --prod \
  --token="$VERCEL_TOKEN" \
  --scope="$VERCEL_ORG_ID"

echo "✅ Deployed successfully."
