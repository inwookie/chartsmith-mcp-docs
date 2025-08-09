---
layout: default
title: Docker Deployment Guide
---

# 🐳 Docker Deployment Guide

Run ChartSmith MCP with Docker Compose.

## Quick Start
```bash
# Clone the repo
git clone https://github.com/inwookie/chart-mcp.git
cd chart-mcp

# Configure environment
cp env.template .env
$EDITOR .env  # add your API keys

# Start services
docker compose --profile all up -d
```

## Verify
```bash
docker compose ps
docker compose logs -f
```

## Update
```bash
git pull
docker compose build --no-cache
docker compose --profile all up -d
```

## Common Issues
- Missing API keys: set in `.env`
- Port conflicts: edit `docker-compose.yml` to change ports
- Slow performance: lower `CHART_MAX_CONCURRENCY`

Need help? Open a discussion: https://github.com/inwookie/chart-mcp-docs/discussions
