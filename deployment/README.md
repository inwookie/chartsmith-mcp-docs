---
layout: default
title: ChartSmith MCP Deployment Guide
---

# 🚀 ChartSmith MCP Deployment Guide

Complete guide for deploying ChartSmith MCP - whether you're hosting for users or deploying for yourself.

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Scenario 1: Host for Users (EC2)](#scenario-1-host-for-users-ec2)
- [Scenario 2: User Self-Deploy](#scenario-2-user-self-deploy)
- [Configuration](#configuration)
- [Management](#management)
- [Troubleshooting](#troubleshooting)

## ⚡ Quick Start

### For Hosting Providers
```bash
# Deploy on EC2 for your users
git clone https://github.com/inwookie/chartsmith-mcp.git
cd chartsmith-mcp
cp env.template .env  # Add your API keys
./deploy.sh production
```

### For End Users
```bash
# Self-deploy ChartSmith MCP
# (Optional) Download prebuilt distribution if available
# curl -L https://releases.example.com/chartsmith-mcp-latest.tar.gz | tar -xz
# cd chartsmith-mcp-distribution

# Recommended: clone the repository
git clone https://github.com/inwookie/chartsmith-mcp.git
cd chartsmith-mcp
cp env.template .env  # Add your API keys
./deploy.sh local
```

---

## Scenario 1: Host for Users (EC2)

**You want to host ChartSmith MCP on your infrastructure for multiple users to connect to.**

### 🔧 Prerequisites

- **AWS EC2 instance** (t3.large or larger recommended)
- **Domain name** (e.g., charts.yourdomain.com)
- **API keys** (OpenAI, Anthropic, or Google)
- **Basic server admin skills**

### 📦 Step 1: Server Setup

```bash
# On your EC2 instance
sudo apt update
sudo apt install -y docker.io docker-compose-plugin git

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
# Log out and back in for group changes
```

### 🚀 Step 2: Deploy ChartSmith

```bash
# Clone repository
git clone https://github.com/inwookie/chartsmith-mcp.git
cd chartsmith-mcp

# Configure environment
cp env.template .env
nano .env  # Add your API keys
```

**Required `.env` settings:**
```bash
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=sk-proj-your-key-here
CHART_MAX_CONCURRENCY=16  # Higher for multiple users
```

```bash
# Deploy for production
./deploy.sh production
```

### 🌐 Step 3: Domain & SSL

```bash
# Point your domain to EC2 IP in DNS
# Install Let's Encrypt certificates
sudo apt install certbot
sudo certbot certonly --standalone -d charts.yourdomain.com

# Update SSL certificates
cp /etc/letsencrypt/live/charts.yourdomain.com/fullchain.pem ssl/chartsmith.crt
cp /etc/letsencrypt/live/charts.yourdomain.com/privkey.pem ssl/chartsmith.key
docker compose restart nginx
```

### 👥 Step 4: User Access

**Users connect with:**
```bash
npx -y @smithery/cli@latest connect "https://<YOUR_DOMAIN>/mcp"
```

---

## Scenario 2: User Self-Deploy

**Individual users want to deploy ChartSmith MCP on their own infrastructure.**

### 📦 Distribution Package

Create a distribution package for users:

```bash
# Create user distribution
./create-distribution.sh v1.0 yourcompany
```

This creates `chartsmith-mcp-distribution-v1.0.tar.gz` for users.

### 👤 User Installation

**Users download and deploy:**

```bash
# Download distribution (optional)
# curl -L https://releases.example.com/chartsmith-mcp-latest.tar.gz | tar -xz
# cd chartsmith-mcp-distribution

# Or clone the repository
git clone https://github.com/inwookie/chartsmith-mcp.git
cd chartsmith-mcp

# Configure with their API keys
cp env.template .env
nano .env  # User adds their own API keys

# Deploy locally
./deploy.sh local
```

**Users add to `~/.cursor/mcp.json`:**
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

---

## ⚙️ Configuration

### Essential Settings

```bash
# AI Configuration
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=your-key-here

# Performance
CHART_MAX_CONCURRENCY=8        # Concurrent chart generations
CHART_TOOL_TIMEOUT_MS=60000    # Tool timeout
CHART_MAX_ROWS=200000          # Max data rows

# Network
HTTP_PORT=8000                 # HTTP server port
```

### Advanced Settings

```bash
# High-performance setup (for hosting)
CHART_MAX_CONCURRENCY=16
CHART_MAX_ROWS=500000
CHART_PERFORMANCE_MONITORING=true

# Redis caching
REDIS_URL=redis://redis:6379

# Security
DISABLED_TOOLS=dangerous_tool1,dangerous_tool2
```

---

## 🔧 Management

### View Logs
```bash
docker compose logs -f                    # All services
docker compose logs chartsmith-http       # HTTP service only
```

### Health Checks
```bash
curl https://your-domain.com/health       # Health endpoint
curl https://your-domain.com/metrics      # Prometheus metrics
```

### Updates
```bash
git pull
docker compose build --no-cache
docker compose up -d
```

### Scaling
```bash
# Scale HTTP service for more users
docker compose up --scale chartsmith-http=3 -d
```

### Stop/Restart
```bash
docker compose down                       # Stop all
docker compose restart                    # Restart all
docker compose restart chartsmith-http    # Restart HTTP only
```

---

## 🐛 Troubleshooting

### Common Issues

#### Connection Timeouts
```bash
# Check if service is running
docker compose ps

# Check logs for errors
docker compose logs chartsmith-http

# Restart if needed
docker compose restart chartsmith-http
```

#### API Key Issues
```bash
# Verify API keys are loaded
docker compose exec chartsmith-http env | grep API_KEY

# Check AI functionality
curl -X POST https://your-domain.com/health
```

#### High Memory Usage
```bash
# Monitor resource usage
docker stats

# Reduce concurrency if needed
echo "CHART_MAX_CONCURRENCY=4" >> .env
docker-compose restart
```

#### SSL Certificate Issues
```bash
# Check certificate validity
openssl x509 -in ssl/chartsmith.crt -text -noout

# Renew Let's Encrypt certificates
sudo certbot renew
cp /etc/letsencrypt/live/your-domain.com/* ssl/
docker compose restart nginx
```

### Performance Optimization

#### For High Load (Hosting)
```bash
# Increase resources
CHART_MAX_CONCURRENCY=16
CHART_TOOL_TIMEOUT_MS=120000

# Enable caching
REDIS_URL=redis://redis:6379

# Monitor metrics
curl https://your-domain.com/metrics
```

#### For Limited Resources (Self-Deploy)
```bash
# Reduce resource usage
CHART_MAX_CONCURRENCY=2
CHART_MAX_ROWS=100000
CHART_PERFORMANCE_MONITORING=false
```

---

## 🎯 Deployment Comparison

| Aspect | EC2 Hosting | User Self-Deploy |
|--------|-------------|------------------|
| **Target** | Multiple users | Single user/team |
| **Setup** | Once (by you) | Each user |
| **Resources** | Your server | User's infrastructure |
| **API Keys** | Your keys | User's keys |
| **Updates** | You manage | User manages |
| **Cost** | Your hosting cost | User's infrastructure |
| **Control** | Full control | User control |

---

## 🎉 Success!

Your ChartSmith MCP is now deployed and ready!

### Next Steps
- **For Hosting**: Share connection URL with users
- **For Users**: Add to Cursor and start creating charts
- **Monitoring**: Set up alerts and backups
- **Scaling**: Monitor usage and scale as needed

**Happy charting! 📊** 