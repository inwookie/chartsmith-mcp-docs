---
layout: default
title: ChartSmith MCP Documentation
---

# 📊 ChartSmith MCP Documentation

Authoritative docs for ChartSmith MCP.

## 🚀 Start Here
- [Installation Guide](getting-started/installation.md)
- [Create Your First Chart](getting-started/first-chart.md)
- [Chart Gallery](examples/chart-gallery.md)
- [API Reference](api/README.md)

## 🐳 Deploy with Docker
```bash
git clone https://github.com/inwookie/chart-mcp.git
cd chart-mcp
cp env.template .env
$EDITOR .env  # add API keys if using AI features
docker compose --profile all up -d
```

## 🔗 Connect (Hosted or Local)
```bash
npx -y @smithery/cli@latest connect "https://<YOUR_DOMAIN>/mcp"
```

## 📎 Useful Links
- [Advanced Configuration](advanced/configuration.md)
- [Docker Deployment Guide](deployment/docker.md)
- [EC2 Hosting Guide](deployment/ec2-hosting.md)

---
Ready to transform your data into beautiful charts? 📊
