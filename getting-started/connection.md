---
layout: default
title: ChartSmith MCP - User Guide
---

# 🎯 ChartSmith MCP - User Guide

Connect to ChartSmith MCP and start creating amazing charts with AI-powered insights.

## ⚡ Connection Methods

### Option 1: Connect to Hosted Service
If your organization provides a hosted ChartSmith MCP:

```bash
npx -y @smithery/cli@latest connect "https://<YOUR_DOMAIN>/mcp"
```

### Option 2: Connect to Self-Deployed Instance
If you deployed ChartSmith MCP locally:

Add this to your `~/.cursor/mcp.json`:
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

### Step 2: Restart Cursor
Close and reopen Cursor to load the ChartSmith MCP tools.

### Step 3: Start Creating Charts! 🎉
You now have access to **20+ powerful chart generation tools** with AI capabilities.

---

## 🛠️ Available Tools

### **📊 Chart Generation**
- `generate_chart_auto` - Smart auto-detection and generation
- `generate_bar_chart` - Bar and column charts  
- `generate_pie_chart` - Pie and donut charts
- `generate_line_chart` - Time series and trend charts
- `generate_scatter_plot` - Correlation and scatter analysis
- `generate_heatmap` - Matrix and correlation heatmaps

### **🧠 AI-Powered Analysis** 
- `detect_optimal_chart` - AI suggests best chart type for your data
- `analyze_and_visualize` - Natural language to chart conversion
- `generate_chart_insights` - AI-generated business insights

### **📈 Advanced Features**
- `create_dashboard` - Multi-chart dashboards
- `generate_chart_batch` - Bulk chart processing
- `get_performance_stats` - Server performance metrics

---

## 💡 Usage Examples

### Basic Chart Creation
```
Create a bar chart showing sales by region:
- North: $125,000
- South: $98,000  
- East: $156,000
- West: $87,000
```

### AI-Powered Chart Selection
```
I have this sales data - what's the best way to visualize it?
[Paste your CSV data or table here]
```

### Natural Language Charting
```
Show me a chart of our website traffic trends over the last 6 months, 
highlighting the peak in December and the dip in February.
```

### Advanced Analytics
```
Create a dashboard showing:
1. Monthly revenue trends
2. Top 10 products by sales  
3. Customer acquisition by channel
4. Regional performance comparison
```

---

## 🎨 Chart Types Supported

- **Bar Charts**: Vertical and horizontal bars
- **Line Charts**: Time series, multi-line, area charts
- **Pie Charts**: Pie, donut, nested pie charts
- **Scatter Plots**: Correlation analysis, bubble charts
- **Heatmaps**: Correlation matrices, pivot tables
- **Histograms**: Distribution analysis
- **Box Plots**: Statistical distributions
- **Treemaps**: Hierarchical data
- **Sankey Diagrams**: Flow visualization
- **Choropleth Maps**: Geographic data

---

## 🔧 Troubleshooting

### Tools Not Showing in Cursor?
1. **Restart Cursor completely** (File → Exit, then reopen)
2. **Check MCP connection** in Cursor settings
3. **Verify connection URL** is correct
4. **Check server status** if self-deployed

### Connection Failed?
- **Hosted service**: Contact your admin for the correct URL
- **Self-deployed**: Check if containers are running with `docker compose ps`
- **Network issues**: Verify firewall settings and port access

### Charts Not Generating?
1. **Test with simple data** first
2. **Check API keys** are configured (for AI features)
3. **Verify data format** is supported
4. **Try different chart types**

### AI Features Not Working?
- **Check API configuration**: AI features require valid API keys
- **Contact admin**: If using hosted service, admin needs to configure keys
- **Self-deployed**: Verify your `.env` file has correct API keys

---

## 📊 Data Formats Supported

### CSV Data
```csv
Region,Sales,Profit
North,125000,25000
South,98000,19600
East,156000,31200
West,87000,17400
```

### JSON Data
```json
[
  {"region": "North", "sales": 125000, "profit": 25000},
  {"region": "South", "sales": 98000, "profit": 19600},
  {"region": "East", "sales": 156000, "profit": 31200},
  {"region": "West", "sales": 87000, "profit": 17400}
]
```

### Table Format
```
| Product | Q1 | Q2 | Q3 | Q4 |
|---------|----|----|----|----|
| Product A | 100 | 120 | 110 | 135 |
| Product B | 80 | 95 | 88 | 102 |
| Product C | 150 | 165 | 172 | 180 |
```

---

## 🚀 Pro Tips

### Getting Better Results
1. **Be specific**: "Monthly sales trends" vs "sales data"
2. **Include context**: "Q4 holiday impact on retail sales"
3. **Specify preferences**: "Use a dark theme for presentation"
4. **Ask for insights**: "What patterns do you see in this data?"

### Using AI Features
- **Natural language**: Describe what you want to see
- **Ask questions**: "Which product is performing best?"
- **Request analysis**: "Identify any concerning trends"
- **Get recommendations**: "What chart type works best here?"

### Dashboard Creation
- **Plan layout**: Describe how charts should be arranged
- **Set themes**: Consistent colors and styling
- **Include context**: Titles, descriptions, and key insights
- **Export options**: Specify format (PNG, PDF, HTML)

---

## 🎉 You're Ready!

ChartSmith MCP is now connected and ready to transform your data into stunning visualizations with AI-powered insights.

### Quick Start Checklist
- ✅ Connected to ChartSmith MCP
- ✅ Restarted Cursor
- ✅ Tools showing in MCP panel
- ✅ Ready to create charts!

**Start with a simple chart and explore from there. Happy charting! 📊** 