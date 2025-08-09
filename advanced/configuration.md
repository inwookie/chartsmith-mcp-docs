---
layout: default
title: Advanced Configuration
---

# ⚙️ Advanced Configuration

Configure ChartSmith MCP for optimal performance and customization.

## 🔧 Environment Variables

### Core Settings
```bash
# AI Configuration
CHART_AI_FEATURES=true              # Enable AI-powered features
CHART_AI_PROVIDER=openai            # Primary AI provider (openai, anthropic, google)

# Performance Settings
CHART_MAX_CONCURRENCY=8             # Concurrent chart generations (1-16)
CHART_TOOL_TIMEOUT_MS=60000         # Tool timeout in milliseconds
CHART_MAX_ROWS=200000               # Maximum rows to process

# Network Settings
PORT=8000                           # HTTP server port
HOST=0.0.0.0                        # Server host (0.0.0.0 for external access)
```

### AI Provider Keys
```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-proj-your-key-here

# Anthropic Configuration  
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Google Gemini Configuration
GOOGLE_API_KEY=your-google-key-here
```

### Advanced Performance
```bash
# High-performance setup
CHART_MAX_CONCURRENCY=16            # Higher concurrency for powerful servers
CHART_TOOL_TIMEOUT_MS=120000        # Extended timeout for complex charts
CHART_MAX_ROWS=500000               # Process larger datasets

# Caching Configuration
REDIS_URL=redis://redis:6379        # Redis cache backend
CHART_CACHE_TTL=3600                # Cache time-to-live in seconds

# Monitoring
CHART_PERFORMANCE_MONITORING=true   # Enable performance tracking
LOG_LEVEL=INFO                      # Logging level (DEBUG, INFO, WARNING, ERROR)
```

---

## 🚀 Performance Tuning

### Hardware Recommendations

#### Local Development
```bash
# Minimal setup (2-4 GB RAM)
CHART_MAX_CONCURRENCY=2
CHART_MAX_ROWS=100000
CHART_PERFORMANCE_MONITORING=false
```

#### Production Server (8+ GB RAM)
```bash
# High-performance setup
CHART_MAX_CONCURRENCY=16
CHART_MAX_ROWS=500000
CHART_TOOL_TIMEOUT_MS=120000
CHART_PERFORMANCE_MONITORING=true
```

#### Enterprise Deployment
```bash
# Maximum performance
CHART_MAX_CONCURRENCY=32
CHART_MAX_ROWS=1000000
CHART_TOOL_TIMEOUT_MS=180000
REDIS_URL=redis://redis-cluster:6379
```

### Resource Optimization

#### Memory Management
- **Concurrency vs Memory**: Lower concurrency for limited memory systems
- **Data Size Limits**: Use `CHART_MAX_ROWS` to prevent memory overflow
- **Garbage Collection**: Python automatically manages memory cleanup

#### CPU Optimization
- **Worker Threads**: Match `CHART_MAX_CONCURRENCY` to CPU cores
- **Chart Complexity**: Complex visualizations require more CPU time
- **Batch Processing**: Use `generate_chart_batch` for multiple charts

---

## 🎨 Chart Customization

### Default Themes
```bash
# Available themes
CHART_DEFAULT_THEME=modern          # modern, dark, colorful, minimal, corporate

# Theme-specific settings
CHART_COLOR_PALETTE=default         # default, viridis, plasma, cool, warm
CHART_FONT_FAMILY=Arial             # Font family for all text
CHART_FONT_SIZE=12                  # Base font size
```

### Custom Styling
```bash
# Brand customization
CHART_BRAND_PRIMARY=#007bff         # Primary brand color
CHART_BRAND_SECONDARY=#28a745       # Secondary brand color
CHART_BRAND_ACCENT=#ffc107          # Accent color

# Layout settings
CHART_DEFAULT_WIDTH=800             # Default chart width
CHART_DEFAULT_HEIGHT=600            # Default chart height
CHART_DPI=300                       # Resolution for image exports
```

---

## 🔒 Security Configuration

### Access Control
```bash
# Authentication (if deploying publicly)
CHART_AUTH_ENABLED=false            # Enable authentication
CHART_AUTH_TOKEN=your-secret-token  # API authentication token

# CORS settings
CHART_CORS_ENABLED=true             # Enable CORS for web access
CHART_CORS_ORIGINS=*                # Allowed origins (* for all)
```

### Rate Limiting
```bash
# Request limits
CHART_RATE_LIMIT_ENABLED=true       # Enable rate limiting
CHART_RATE_LIMIT_REQUESTS=100       # Requests per minute per IP
CHART_RATE_LIMIT_WINDOW=60          # Rate limit window in seconds
```

### Tool Restrictions
```bash
# Disable specific tools
DISABLED_TOOLS=generate_3d_chart,create_animated_chart

# Allowed file formats
CHART_ALLOWED_FORMATS=png,svg,pdf,json,html
```

---

## 📊 Monitoring & Logging

### Health Checks
```bash
# Health check endpoints
CHART_HEALTH_ENABLED=true           # Enable /health endpoint
CHART_METRICS_ENABLED=true          # Enable /metrics endpoint (Prometheus)
```

### Logging Configuration
```bash
# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL=INFO

# Log format
LOG_FORMAT=json                     # json or text
LOG_FILE=/var/log/chartsmith.log    # Log file path (optional)

# Request logging
CHART_LOG_REQUESTS=true             # Log all API requests
CHART_LOG_PERFORMANCE=true          # Log performance metrics
```

### Metrics Collection
```bash
# Prometheus metrics
CHART_PROMETHEUS_ENABLED=true       # Enable Prometheus metrics
CHART_METRICS_PORT=9090             # Metrics endpoint port

# Custom metrics
CHART_TRACK_USAGE=true              # Track tool usage statistics
CHART_TRACK_PERFORMANCE=true        # Track generation times
```

---

## 🌐 Deployment Configurations

### Docker Environment
```yaml
# docker-compose.yml environment
environment:
  - CHART_AI_FEATURES=true
  - CHART_AI_PROVIDER=openai
  - OPENAI_API_KEY=${OPENAI_API_KEY}
  - CHART_MAX_CONCURRENCY=8
  - REDIS_URL=redis://redis:6379
  - LOG_LEVEL=INFO
```

### Kubernetes Configuration
```yaml
# ConfigMap for Kubernetes
apiVersion: v1
kind: ConfigMap
metadata:
  name: chartsmith-config
data:
  CHART_AI_FEATURES: "true"
  CHART_MAX_CONCURRENCY: "16"
  LOG_LEVEL: "INFO"
  CHART_PERFORMANCE_MONITORING: "true"
```

### Cloud Deployment
```bash
# AWS/GCP/Azure optimized
CHART_MAX_CONCURRENCY=12            # Cloud instance optimized
CHART_CLOUD_STORAGE=s3://bucket     # Cloud storage for outputs
CHART_CDN_ENABLED=true              # Use CDN for static assets
```

---

## 🔧 Troubleshooting

### Common Issues

#### High Memory Usage
```bash
# Reduce memory footprint
CHART_MAX_CONCURRENCY=4
CHART_MAX_ROWS=100000
CHART_CACHE_ENABLED=false
```

#### Slow Response Times
```bash
# Optimize for speed
CHART_TOOL_TIMEOUT_MS=30000
CHART_PERFORMANCE_MONITORING=true
LOG_LEVEL=WARNING
```

#### Connection Issues
```bash
# Network troubleshooting
HOST=0.0.0.0                        # Allow external connections
CHART_CORS_ENABLED=true             # Enable CORS
CHART_AUTH_ENABLED=false            # Disable auth for testing
```

### Performance Diagnostics
```bash
# Enable detailed logging
LOG_LEVEL=DEBUG
CHART_LOG_PERFORMANCE=true
CHART_LOG_REQUESTS=true

# Monitor with metrics
curl http://localhost:8000/metrics   # Prometheus metrics
curl http://localhost:8000/health    # Health status
```

---

## 📝 Configuration Templates

### Development Environment
```bash
# .env for development
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=your-dev-key
CHART_MAX_CONCURRENCY=4
LOG_LEVEL=DEBUG
CHART_PERFORMANCE_MONITORING=true
```

### Production Environment
```bash
# .env for production
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=your-prod-key
CHART_MAX_CONCURRENCY=16
CHART_MAX_ROWS=500000
LOG_LEVEL=WARNING
CHART_PERFORMANCE_MONITORING=true
REDIS_URL=redis://redis:6379
CHART_RATE_LIMIT_ENABLED=true
```

### High-Availability Setup
```bash
# .env for enterprise
CHART_AI_FEATURES=true
CHART_AI_PROVIDER=openai
OPENAI_API_KEY=your-enterprise-key
CHART_MAX_CONCURRENCY=32
CHART_MAX_ROWS=1000000
REDIS_URL=redis://redis-cluster:6379
CHART_PROMETHEUS_ENABLED=true
CHART_CLOUD_STORAGE=s3://charts-bucket
```

**Need help with configuration?** [Open a GitHub discussion](https://github.com/inwookie/chartsmith-mcp-docs/discussions) 🚀
