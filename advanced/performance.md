---
layout: default
title: Performance Optimization
---

# ⚡ Performance Optimization (Quick Tips)

Keep it simple. Start with defaults, then tune only if needed.

## ✅ Recommended Settings
```bash
# Development (laptops)
CHART_MAX_CONCURRENCY=2
CHART_MAX_ROWS=100000

# Production (8–16 GB RAM)
CHART_MAX_CONCURRENCY=8
CHART_TOOL_TIMEOUT_MS=60000
REDIS_URL=redis://redis:6379
```

## 🧪 Monitor
```bash
docker compose logs -f
curl http://localhost:8000/health
```

## 🐛 If Slow
- Lower `CHART_MAX_CONCURRENCY`
- Reduce input size; aggregate before charting
- Prefer JSON/HTML over image formats during iteration

## 🧰 When Scaling
- Enable Redis cache (`REDIS_URL`)
- Increase CPU/RAM before tuning timeouts
- Horizontal scale HTTP service if needed

For advanced tuning, see `advanced/configuration.md`.
