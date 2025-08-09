---
layout: default
title: Self-Deploy Guide
---

# 🚀 Self-Deploy Guide

Follow these steps to run ChartSmith MCP on your own machine or server.

## ✅ Prerequisites
- Docker Desktop (macOS/Windows) or Docker Engine (Linux)
- API key for your AI provider (OpenAI, Anthropic, or Google)

## 1) Clone the repository
```bash
git clone https://github.com/inwookie/chartsmith-mcp.git
cd chartsmith-mcp
```

## 2) Configure environment
```bash
cp env.template .env
$EDITOR .env  # add your API keys
```

Minimum required settings:
```bash
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=sk-proj-your-key-here
```

## 3) Start with Docker Compose
```bash
docker compose up -d
```

Verify containers are running:
```bash
docker compose ps
```

## 4) Connect from Cursor (local)
Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "chartsmith-local": {
      "command": "docker",
      "args": ["exec", "-i", "chartsmith-mcp", "python", "-m", "chart_genius_mcp", "--transport", "stdio"]
    }
  }
}
```

Restart Cursor, then open the MCP tools panel to see ChartSmith tools.

## Troubleshooting
- Check logs: `docker compose logs -f`
- Restart services: `docker compose restart`
- Verify API key is set: `docker compose exec chartsmith-http env | grep API_KEY`

Need help? Open a discussion: https://github.com/inwookie/chartsmith-mcp-docs/discussions
