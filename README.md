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
npx -y @smithery/cli@latest connect "https://chartsmith.yourcompany.com/mcp"
```

### 🐳 Self-Deploy with Docker
```bash
curl -L https://releases.yourcompany.com/chartsmith-mcp-latest.tar.gz | tar -xz
cd chartsmith-mcp-distribution
cp env.template .env  # Add your API keys
./deploy.sh local
```

**Ready to transform your data into beautiful charts?** 📊
