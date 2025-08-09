# 🚀 EC2 Hosting Guide

Deploy ChartSmith MCP on AWS EC2 for production hosting.

## 🎯 Overview

Host ChartSmith MCP on your own AWS EC2 infrastructure to provide chart generation services to multiple users while maintaining full control over performance, security, and costs.

## 📋 Prerequisites

- AWS account with EC2 access
- Domain name (recommended)
- Basic server administration knowledge
- API keys (OpenAI, Anthropic, or Google)

## 🖥️ EC2 Instance Setup

### Recommended Instance Types

#### Development/Testing
- **Instance**: t3.medium (2 vCPU, 4 GB RAM)
- **Storage**: 20 GB gp3 SSD
- **Cost**: ~$30/month

#### Production
- **Instance**: c5.large (2 vCPU, 4 GB RAM, optimized CPU)
- **Storage**: 50 GB gp3 SSD  
- **Cost**: ~$60/month

#### High-Performance
- **Instance**: c5.xlarge (4 vCPU, 8 GB RAM)
- **Storage**: 100 GB gp3 SSD
- **Cost**: ~$120/month

### Launch EC2 Instance

1. **Choose AMI**: Ubuntu 22.04 LTS
2. **Instance Type**: Based on your needs above
3. **Security Group**: 
   - SSH (22) from your IP
   - HTTP (80) from anywhere
   - HTTPS (443) from anywhere
4. **Storage**: SSD with enough space for logs and outputs

## 🔧 Server Configuration

### Initial Setup
```bash
# Connect to your instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### Install ChartSmith MCP
```bash
# Clone the repository
git clone https://github.com/your-username/chartsmith-mcp.git
cd chartsmith-mcp

# Configure environment
cp env.template .env
nano .env
```

**Configure environment:**
```bash
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=your-openai-key-here
CHART_MAX_CONCURRENCY=16
HTTP_PORT=8000
HOST=0.0.0.0
```

### Deploy
```bash
./deploy.sh production
```

**Your ChartSmith MCP is now ready for production use!** 🚀
