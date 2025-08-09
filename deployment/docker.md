---
layout: default
title: Docker Deployment Guide
---

# 🐳 Docker Deployment Guide

Run ChartSmith MCP with Docker.

## 🚀 Option A: Use Prebuilt Docker Image (Recommended)

No repo clone required.

```bash
# Pull the image
docker pull inwookie/chartsmith-mcp:latest

# (Optional) Create .env for AI keys
cat > .env <<'EOF'
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=sk-...
EOF

# Run HTTP (SSE) server on port 8000
docker run --rm \
  -p 8000:8000 \
  --env-file .env \
  inwookie/chartsmith-mcp:latest \
  python -m chart_genius_mcp --transport sse --host 0.0.0.0 --port 8000
```

Verify:
```bash
curl http://localhost:8000/health   # -> {"status":"ok"}
```

### Compose (prebuilt image)
```yaml
# docker-compose.example.yml (see repo under deployment/)
services:
  chartsmith-http:
    image: inwookie/chartsmith-mcp:latest
    command: python -m chart_genius_mcp --transport sse --host 0.0.0.0 --port 8000
    ports:
      - "8000:8000"
    env_file: .env
  chartsmith-stdio:
    image: inwookie/chartsmith-mcp:latest
    command: python -m chart_genius_mcp --transport stdio
  redis:
    image: redis:7-alpine
```

Run:
```bash
cp deployment/docker-compose.example.yml docker-compose.yml
docker compose up -d
```

## 🧩 Option B: From Source (Clone Repo)

```bash
git clone https://github.com/inwookie/chart-mcp.git
cd chart-mcp
cp env.template .env
$EDITOR .env

docker compose --profile all up -d
```

## 🔎 Troubleshooting
- Port in use: change host port mapping (e.g., `-p 8080:8000`)
- Missing API keys (AI): set in `.env`
- Health check fails: `docker compose logs -f`

Need help? Open a discussion: https://github.com/inwookie/chart-mcp-docs/discussions
