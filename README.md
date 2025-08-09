---
layout: default
title: ChartSmith MCP Documentation
---

# 📊 ChartSmith MCP Documentation

**Complete documentation for ChartSmith MCP - The high-performance chart generation server**

> 🚀 **Transform your data into stunning visualizations with AI-powered insights**

## 🎯 Quick Navigation

### 🚀 Getting Started
- [Installation Guide](getting-started/installation.md)
- [Create Your First Chart](getting-started/first-chart.md)
- [Connection Setup](getting-started/connection.md)

### 🏗️ Deployment
- [Deployment Overview](deployment/README.md)
- [EC2 Hosting](deployment/ec2-hosting.md)
- [Self-Deploy Guide](deployment/self-deploy.md)

### 💡 Examples & Tutorials
- [Chart Gallery](examples/chart-gallery.md)
- [Code Examples](examples/code-examples.md)
- [Tutorials](examples/tutorials.md)

### 🔧 Advanced
- [Configuration](advanced/configuration.md)
- [Performance Tuning](advanced/performance.md)
- [API Reference](api/README.md)

## ⚡ Quick Start

### 🔗 Connect to Hosted Service
```bash
npx -y @smithery/cli@latest connect "https://<YOUR_DOMAIN>/mcp"
```

### 🐳 Self-Deploy with Docker
```bash
# 1) Clone the repo
git clone https://github.com/inwookie/chart-mcp.git
cd chart-mcp

# 2) Configure environment
cp env.template .env
$EDITOR .env  # add your API keys

# 3) Start with Docker Compose
docker compose --profile all up -d
```

**Ready to transform your data into beautiful charts?** 📊
