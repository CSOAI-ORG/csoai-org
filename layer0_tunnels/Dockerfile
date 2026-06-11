FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy SDK and API server
COPY layer0_sdk.py .
COPY main.py .
COPY csoai_brand_authority_mcp.py .

# Expose port for FastAPI (8000) and FastMCP SSE (8001)
EXPOSE 8000
EXPOSE 8001

# Default command runs the Layer 0 API server.
# To run the Brand Authority MCP server instead:
# CMD ["fastmcp", "run", "csoai_brand_authority_mcp.py", "--port", "8001"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
