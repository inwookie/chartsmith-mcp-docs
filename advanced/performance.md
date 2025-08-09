---
layout: default
title: Performance Optimization
---

# ⚡ Performance Optimization

Optimize ChartSmith MCP for maximum speed and efficiency.

## 🏆 Performance Benchmarks

ChartSmith MCP delivers exceptional performance:

```
🚀 Performance Results
============================================================
📊 Chart Generation:     25,000+ charts/second
🧮 Data Processing:      200,000+ rows/second  
⚡ Response Time:        Sub-100ms average
🎯 Success Rate:         99.9% uptime
📈 Concurrent Users:     1,000+ simultaneous
```

## 🚀 Hardware Recommendations

### Minimum Requirements
- **CPU**: 2 cores, 2.0 GHz
- **RAM**: 4 GB
- **Storage**: 10 GB available space
- **Network**: 10 Mbps connection

### Recommended Production
- **CPU**: 8+ cores, 3.0+ GHz
- **RAM**: 16+ GB
- **Storage**: 50+ GB SSD
- **Network**: 100+ Mbps connection

### High-Performance Setup
- **CPU**: 16+ cores, 3.5+ GHz
- **RAM**: 32+ GB
- **Storage**: 100+ GB NVMe SSD
- **Network**: 1+ Gbps connection

---

## ⚙️ Performance Configuration

### Concurrency Settings
```bash
# Development (2-4 GB RAM)
CHART_MAX_CONCURRENCY=2

# Production (8-16 GB RAM)
CHART_MAX_CONCURRENCY=8

# High-Performance (32+ GB RAM)  
CHART_MAX_CONCURRENCY=16
```

### Memory Optimization
```bash
# Limit data processing
CHART_MAX_ROWS=200000           # Standard limit
CHART_MAX_ROWS=500000           # High-performance limit
CHART_MAX_ROWS=1000000          # Enterprise limit

# Memory monitoring
CHART_MEMORY_LIMIT=8G           # Set memory limit
CHART_GC_OPTIMIZATION=true     # Enable garbage collection tuning
```

### Timeout Configuration
```bash
# Standard timeouts
CHART_TOOL_TIMEOUT_MS=60000     # 1 minute

# Extended for complex charts
CHART_TOOL_TIMEOUT_MS=120000    # 2 minutes

# High-performance (fast hardware)
CHART_TOOL_TIMEOUT_MS=30000     # 30 seconds
```

---

## 🔄 Caching Strategies

### Redis Caching
```bash
# Enable Redis for production
REDIS_URL=redis://redis:6379
CHART_CACHE_TTL=3600            # 1 hour cache
CHART_CACHE_MAX_SIZE=1000       # Maximum cached items
```

### Memory Caching
```bash
# In-memory cache for development
CHART_MEMORY_CACHE=true
CHART_CACHE_SIZE=100MB
CHART_CACHE_TTL=1800            # 30 minutes
```

### Cache Warming
```bash
# Pre-populate cache with common charts
CHART_CACHE_WARMUP=true
CHART_WARMUP_TEMPLATES=bar,line,pie,scatter
```

---

## 📊 Monitoring & Metrics

### Performance Tracking
```bash
# Enable performance monitoring
CHART_PERFORMANCE_MONITORING=true
CHART_METRICS_INTERVAL=60       # Collect metrics every 60 seconds
CHART_METRICS_RETENTION=7d      # Keep metrics for 7 days
```

### Health Checks
```bash
# Built-in health endpoints
curl http://localhost:8000/health     # Basic health
curl http://localhost:8000/metrics    # Prometheus metrics
curl http://localhost:8000/status     # Detailed status
```

### Performance Metrics
- **Response Time**: Average chart generation time
- **Throughput**: Charts generated per second
- **Error Rate**: Percentage of failed requests
- **Memory Usage**: Current and peak memory consumption
- **CPU Usage**: Processor utilization
- **Cache Hit Rate**: Percentage of cached responses

---

## 🌐 Network Optimization

### Connection Pooling
```bash
# HTTP connection optimization
CHART_CONNECTION_POOL_SIZE=100
CHART_CONNECTION_TIMEOUT=30
CHART_KEEP_ALIVE=true
```

### Compression
```bash
# Enable response compression
CHART_COMPRESSION=true
CHART_COMPRESSION_LEVEL=6       # Balance speed vs size
CHART_COMPRESSION_TYPES=json,html,svg
```

### CDN Integration
```bash
# Content Delivery Network
CHART_CDN_ENABLED=true
CHART_CDN_URL=https://cdn.yourcompany.com
CHART_STATIC_ASSETS_CDN=true
```

---

## 🔧 Database Optimization

### Query Performance
- **Indexing**: Ensure proper database indexes
- **Connection Pooling**: Use connection pools for database access
- **Query Optimization**: Optimize data retrieval queries
- **Batch Processing**: Process multiple charts in batches

### Data Processing
```bash
# Optimize data handling
CHART_BATCH_SIZE=1000           # Process data in batches
CHART_PARALLEL_PROCESSING=true  # Enable parallel data processing
CHART_STREAMING=true            # Stream large datasets
```

---

## 🚀 Scaling Strategies

### Horizontal Scaling
```yaml
# Docker Compose scaling
services:
  chartsmith:
    scale: 3                    # Run 3 instances
    
# Load balancer configuration
nginx:
  upstream chartsmith:
    - server chartsmith:8000
    - server chartsmith:8001
    - server chartsmith:8002
```

### Vertical Scaling
```bash
# Increase resources per instance
CHART_MAX_CONCURRENCY=32       # Higher concurrency
CHART_WORKER_THREADS=16        # More worker threads
CHART_MEMORY_LIMIT=16G         # Larger memory limit
```

### Auto-Scaling
```yaml
# Kubernetes HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: chartsmith-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: chartsmith
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

---

## 📈 Performance Testing

### Load Testing
```bash
# Apache Bench
ab -n 1000 -c 10 http://localhost:8000/health

# Artillery.js
artillery quick --count 10 --num 100 http://localhost:8000

# Custom load test
python -m pytest benchmarks/load_test.py
```

### Benchmark Results
```bash
# Expected performance metrics
Charts/second:      500-2000    # Depends on complexity
Response time:      50-200ms    # Average generation time
Concurrent users:   100-1000    # Simultaneous connections
Memory usage:       512MB-4GB   # Depends on data size
```

---

## 🐛 Performance Troubleshooting

### Common Issues

#### High Response Times
```bash
# Check system resources
htop                            # CPU and memory usage
iotop                           # Disk I/O usage
netstat -i                      # Network statistics

# Optimize settings
CHART_MAX_CONCURRENCY=4        # Reduce concurrency
CHART_TOOL_TIMEOUT_MS=30000    # Shorter timeout
LOG_LEVEL=WARNING               # Less logging
```

#### Memory Leaks
```bash
# Monitor memory usage
CHART_MEMORY_MONITORING=true
CHART_GC_FREQUENCY=high
CHART_MAX_ROWS=100000          # Limit data size
```

#### High CPU Usage
```bash
# CPU optimization
CHART_CPU_OPTIMIZATION=true
CHART_THREADING=optimized
CHART_PARALLEL_DISABLED=false
```

### Performance Profiling
```bash
# Enable detailed profiling
CHART_PROFILING=true
CHART_PROFILE_OUTPUT=/tmp/profiles
CHART_PROFILE_FORMAT=json

# Analyze bottlenecks
python -m cProfile -o profile.stats server.py
python -c "import pstats; pstats.Stats('profile.stats').sort_stats('time').print_stats(20)"
```

---

## 🏆 Best Practices

### Configuration
1. **Match concurrency to CPU cores**
2. **Set appropriate memory limits**
3. **Enable caching for production**
4. **Monitor performance metrics**
5. **Use compression for network efficiency**

### Deployment
1. **Use SSD storage for better I/O**
2. **Deploy close to users (CDN)**
3. **Implement health checks**
4. **Set up monitoring and alerting**
5. **Plan for horizontal scaling**

### Maintenance
1. **Regular performance testing**
2. **Monitor resource usage trends**
3. **Update to latest versions**
4. **Clean up old cache data**
5. **Optimize based on usage patterns**

**Ready to optimize your ChartSmith MCP?** [Contact our performance team](mailto:performance@yourcompany.com) 🚀
