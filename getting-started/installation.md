---
layout: default
title: Installation Guide
---

# 🚀 Installation Guide

Get ChartSmith MCP up and running in minutes.

## 📋 Prerequisites

- **MCP Client**: Cursor, Claude Desktop, or any MCP-compatible client
- **API Keys**: OpenAI, Anthropic, or Google (for AI features)
- **Docker** (for self-deployment): [Install Docker](https://docs.docker.com/get-docker/)

## 🔗 Option 1: Connect to Hosted Service

The fastest way to get started:

```bash
npx -y @smithery/cli@latest connect "https://<YOUR_DOMAIN>/mcp"
```

**That's it!** You now have access to all ChartSmith MCP tools.

### Verify Connection
1. Open Cursor
2. Look for ChartSmith tools in the MCP panel
3. Try: "Create a simple bar chart with sample data"

---

## 🐳 Option 2: Self-Deploy with Docker

Deploy ChartSmith MCP on your own infrastructure:

### Step 1: Clone the repository
```bash
git clone https://github.com/inwookie/chart-mcp.git
cd chart-mcp
```

### Step 2: Configure Environment
```bash
cp env.template .env
$EDITOR .env  # add your API keys
```

**Required settings (add your actual API key):**
```bash
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=sk-proj-your-actual-openai-key-here
```

**⚠️ Important**: Replace `sk-proj-your-actual-openai-key-here` with your real OpenAI API key. Without this, AI features won't work.

### Step 3: Start with Docker Compose
```bash
docker compose --profile all up -d
```

**Verify deployment:**
```bash
# Check containers are running
docker compose ps

# Test HTTP endpoint
curl http://localhost:8000/health
# Should return: {"status":"ok"}
```

### Step 4: Connect to Cursor

**Option A: HTTP Connection (Recommended)**
Your ChartSmith MCP is now running at `http://localhost:8000`. You can use any HTTP-based MCP client to connect.

**Option B: STDIO Connection**
For STDIO MCP clients, create this wrapper script:

1. Create `~/chartsmith-mcp.sh`:
```bash
#!/bin/bash
cd /path/to/your/chart-mcp
docker compose run --rm chartsmith-stdio python -m chart_genius_mcp --transport stdio
```

2. Make it executable: `chmod +x ~/chartsmith-mcp.sh`

3. Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "chartsmith-local": {
      "command": "/Users/your-username/chartsmith-mcp.sh"
    }
  }
}
```

### Step 5: Restart Cursor
Close and reopen Cursor to load the new MCP connection.

---

## 🎯 Next Steps

✅ **Installation Complete!**

**What's next?**
- 📊 [Create Your First Chart](first-chart.md)
- 🔧 [Configure Advanced Settings](../advanced/configuration.md)
- 💡 [View Chart Examples](../examples/chart-gallery.md)

---

## 🐛 Troubleshooting

### Tools Not Showing in Cursor?
1. **Restart Cursor completely** (File → Exit, then reopen)
2. **Check MCP connection** in Cursor settings
3. **Verify .cursor/mcp.json** syntax is correct

### Connection Failed?
- **Hosted service**: Contact your admin for the correct URL
- **Self-deployed**: Check containers with `docker compose ps`

### Docker Issues?
```bash
# Check if containers are running
docker compose ps

# View logs
docker compose logs -f

# Restart services
docker compose restart
```

**Need help?** [Report an issue](https://github.com/inwookie/chart-mcp-docs/issues)
