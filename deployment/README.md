---
layout: default
title: ChartSmith MCP Deployment Guide
---

# 🚀 Deployment

Simple ways to run ChartSmith MCP.

## ✅ Recommended
- [Docker Deployment](docker.md) — quickest path, works on any machine

## ☁️ Cloud
- [EC2 Hosting Guide](ec2-hosting.md) — production on AWS

## 🔑 Prerequisites
- Docker and Docker Compose plugin
- API key for AI features (optional for basic charts)

## 🧪 Verify
```bash
docker compose ps
docker compose logs -f
curl http://localhost:8000/health
```

Need help? Open a discussion: https://github.com/inwookie/chart-mcp-docs/discussions 