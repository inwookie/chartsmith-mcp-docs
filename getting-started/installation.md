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

## ✅ Test Your Installation

Verify ChartSmith MCP is working:

```bash
# Test chart generation
docker compose run --rm chartsmith-stdio python -m chart_genius_mcp --test-chart
```

Expected output: `✅ Test chart generated successfully!`

### Generate a Real Chart File

Test creating an actual chart file:

```bash
# Create a test chart and save as HTML
docker compose run --rm chartsmith-stdio python -c "
import sys
sys.path.append('/app/src')
from chart_genius_mcp.server import ChartGeniusServer
import asyncio, json

async def save_chart():
    server = ChartGeniusServer()
    data = {'rows': [{'month': 'Jan', 'sales': 100}, {'month': 'Feb', 'sales': 120}]}
    
    result = await server._call_tool_handler('generate_bar_chart', {
        'data': data, 'x': 'month', 'y': 'sales', 'format': 'html'
    })
    
    response = json.loads(result[0].text)
    if response.get('success'):
        with open('/app/outputs/my_chart.html', 'w') as f:
            f.write(response['payload'])
        print('✅ Chart saved to outputs/my_chart.html')

asyncio.run(save_chart())
"
```

Then open `outputs/my_chart.html` in your browser to see the chart!

### Common Setup Issues

**“Missing API Key” or AI Features Not Working**

- ✅ All tools were tested end‑to‑end. Basic charts and utilities work without API keys
- 🔑 AI tools require a real API key in `.env` (placeholder won’t work)
- **Basic charts (no key needed)**: bar, line, pie, scatter, area, box, bubble, violin
- **Advanced charts**: work with specific parameters (e.g., heatmap needs x/y/value; sankey needs source/target/value)
- **AI tools (require key)**: `generate_chart_auto` (verified), `detect_optimal_chart` (no key needed), `analyze_and_visualize` (verified), `generate_chart_insights` (works with `chart_data` dict; parameter‑sensitive)
- Get your OpenAI key from: https://platform.openai.com/api-keys

**“No Such File or Directory: chart-mcp”**
- Make sure you cloned the correct repo: `github.com/inwookie/chart-mcp`

**Docker Compose Warnings**
- The `version` warning is harmless and can be ignored

**Need help?** [Report an issue](https://github.com/inwookie/chart-mcp-docs/issues)
