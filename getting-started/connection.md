---
layout: default
title: ChartSmith MCP - User Guide
---

# 🎯 Connect to ChartSmith MCP

Connect and start creating charts in minutes.

## ⚡ Connection Methods

### Option 1: Hosted Service
```bash
npx -y @smithery/cli@latest connect "https://<YOUR_DOMAIN>/mcp"
```

### Option 2: Local (Docker)
- HTTP (recommended): `http://localhost:8000`
- STDIO wrapper (optional):
```bash
#!/bin/bash
cd /path/to/your/chart-mcp
docker compose run --rm chartsmith-stdio python -m chart_genius_mcp --transport stdio
```
Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "chartsmith-local": { "command": "/Users/your-username/chartsmith-mcp.sh" }
  }
}
```

## ✅ Try It
Paste into Cursor:
```
Create a bar chart showing sales by region:
- North: $125,000
- South: $98,000  
- East: $156,000
- West: $87,000
```

- More examples: `examples/code-examples.md`
- Tool reference: `api/README.md`

## 🐛 Troubleshooting
- Restart Cursor after adding a connection
- If local: `docker compose ps` then `docker compose logs -f`
- For AI tools: set real API keys in `.env` 