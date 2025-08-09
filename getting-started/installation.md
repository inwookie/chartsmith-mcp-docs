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
git clone https://github.com/inwookie/chartsmith-mcp.git
cd chartsmith-mcp
```

### Step 2: Configure Environment
```bash
cp env.template .env
$EDITOR .env  # add your API keys
```

**Required settings:**
```bash
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=sk-proj-your-key-here
```

### Step 3: Start with Docker Compose
```bash
docker compose up -d
```

### Step 4: Connect to Cursor
Add this to your `~/.cursor/mcp.json`:

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

**Need help?** [Report an issue](https://github.com/inwookie/chartsmith-mcp-docs/issues)
