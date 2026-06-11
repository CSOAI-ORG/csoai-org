#!/bin/bash
# CSOAI LAYER 0 UNIFIED RUNNER
# Instant orchestration for Enterprise API, Growth MCP, Compliance MCP, and MEOK DOME TUI.

# Colors
GOLD='\033[0;33m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GOLD}--- CSOAI LAYER 0 MASTER RUNNER (2026) ---${NC}"

# Check for Docker
if ! [ -x "$(command -v docker-compose)" ]; then
  echo -e "${RED}Error: docker-compose is not installed.${NC}" >&2
  exit 1
fi

cd layer0_tunnels

case "$1" in
  start)
    echo -e "${BLUE}Starting Enterprise Infrastructure (Docker)...${NC}"
    docker-compose up --build -d
    echo -e "${GREEN}API Running on port 8000 (Docs: http://localhost:8000/docs)${NC}"
    echo -e "${GREEN}Growth MCP on port 8001${NC}"
    echo -e "${GREEN}Compliance MCP on port 8002${NC}"
    ;;
  stop)
    echo -e "${BLUE}Stopping Infrastructure...${NC}"
    docker-compose down
    ;;
  tui)
    echo -e "${GOLD}Launching MEOK DOME TUI...${NC}"
    python3 meok_dome_tui.py
    ;;
  build)
    echo -e "${BLUE}Regenerating Industry Pages & Fragments...${NC}"
    cd ..
    python3 generate_industry_pages.py
    python3 build.py
    cd layer0_tunnels
    echo -e "${GREEN}Build Complete.${NC}"
    ;;
  distribute)
    echo -e "${GOLD}--- CSOAI 7-DAY SOCIAL BLITZ (WEEK 1) ---${NC}"
    cat ../SOCIAL_BLITZ.md
    echo -e "\n${BLUE}Next Action: Copy post for current day and publish to LinkedIn/Twitter/Reddit.${NC}"
    ;;
  test)
    echo -e "${BLUE}Running E2E API Tests...${NC}"
    python3 test_e2e.py
    ;;
  logs)
    docker-compose logs -f
    ;;
  *)
    echo "Usage: $0 {start|stop|tui|test|logs}"
    exit 1
esac
