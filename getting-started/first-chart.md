---
layout: default
title: Create Your First Chart
---

# 📊 Create Your First Chart

Let’s create your first chart with ChartSmith MCP!

## ✅ Tool Input Examples (Copy/Paste)

Use these inputs with the corresponding tools in your MCP client. They are minimal, tested, and work without API keys.

### Bar (generate_bar_chart)
```json
{
  "data": {
    "rows": [
      {"region": "North", "sales": 125000},
      {"region": "South", "sales": 98000},
      {"region": "East",  "sales": 156000},
      {"region": "West",  "sales": 87000}
    ]
  },
  "x": "region",
  "y": "sales",
  "format": "html"
}
```

### Line (generate_line_chart)
```json
{
  "data": {"rows": [
    {"month": "Jan", "value": 45},
    {"month": "Feb", "value": 52},
    {"month": "Mar", "value": 48},
    {"month": "Apr", "value": 55}
  ]},
  "x": "month",
  "y": "value"
}
```

### Pie (generate_pie_chart)
```json
{
  "data": {"rows": [
    {"source": "Organic", "pct": 45},
    {"source": "Social",  "pct": 25},
    {"source": "Direct",  "pct": 20},
    {"source": "Paid",    "pct": 8},
    {"source": "Email",   "pct": 2}
  ]},
  "names": "source",
  "values": "pct"
}
```

### Scatter (generate_scatter_chart)
```json
{
  "data": {"rows": [
    {"x": 1, "y": 3}, {"x": 2, "y": 2}, {"x": 3, "y": 4},
    {"x": 4, "y": 3.5}, {"x": 5, "y": 5}
  ]},
  "x": "x",
  "y": "y"
}
```

### Heatmap (generate_heatmap_chart)
```json
{
  "data": {"rows": [
    {"x": "Mon", "y": "Morning", "value": 2},
    {"x": "Mon", "y": "Evening", "value": 3},
    {"x": "Tue", "y": "Morning", "value": 4}
  ]},
  "x": "x",
  "y": "y",
  "value": "value"
}
```

### Sankey (generate_sankey_chart)
```json
{
  "data": {"rows": [
    {"source": "A", "target": "B", "value": 5},
    {"source": "B", "target": "C", "value": 3},
    {"source": "A", "target": "C", "value": 2}
  ]},
  "source": "source",
  "target": "target",
  "value": "value"
}
```

### Treemap (generate_treemap_chart)
```json
{
  "data": {"rows": [
    {"cat1": "Food",    "cat2": "Fruits",     "value": 50},
    {"cat1": "Food",    "cat2": "Vegetables", "value": 30},
    {"cat1": "Staples", "cat2": "Grains",     "value": 20}
  ]},
  "path": ["cat1", "cat2"],
  "value": "value"
}
```

### Histogram (generate_histogram_chart)
Pre-binned example (required by the engine):
```json
{
  "data": {"rows": [
    {"bin_start": 0,  "bin_end": 10, "bin_center": 5,  "count": 3, "frequency": 0.3, "percentage": 30},
    {"bin_start": 10, "bin_end": 20, "bin_center": 15, "count": 5, "frequency": 0.5, "percentage": 50},
    {"bin_start": 20, "bin_end": 30, "bin_center": 25, "count": 2, "frequency": 0.2, "percentage": 20}
  ]},
  "x": "bin_center"
}
```

### Box Plot (generate_box_chart)
```json
{
  "data": {"rows": [
    {"group": "A", "value": 10},
    {"group": "A", "value": 12},
    {"group": "A", "value": 9},
    {"group": "B", "value": 15},
    {"group": "B", "value": 14}
  ]},
  "x": "group",
  "y": "value"
}
```

> Tip: If your MCP client shows a parameters form for a tool, just fill these same fields instead of pasting JSON.

## 🤖 AI Tool Inputs (API Key Required)

These require a valid API key. Provide both your data and text input.

### Auto Chart (generate_chart_auto)
```json
{
  "data": {"rows": [
    {"month": "Jan", "revenue": 50000, "costs": 30000},
    {"month": "Feb", "revenue": 55000, "costs": 32000},
    {"month": "Mar", "revenue": 48000, "costs": 35000}
  ]},
  "user_text": "Show revenue trends over months and suggest the best visualization"
}
```

### Analyze + Visualize (analyze_and_visualize)
```json
{
  "data": {"rows": [
    {"month": "Jan", "sales": 15000, "profit": 3000},
    {"month": "Feb", "sales": 18000, "profit": 3600},
    {"month": "Mar", "sales": 22000, "profit": 4400}
  ]},
  "question": "Create a visualization showing the relationship between sales and profit"
}
```

### Insights (generate_chart_insights)
1) First, generate any chart with `format: "json"` and copy its `chart` object.
2) Then call:
```json
{
  "chart_data": { /* paste the chart object here (JSON), not HTML */ },
  "data": {"rows": [
    {"month": "Jan", "sales": 15000, "profit": 3000},
    {"month": "Feb", "sales": 18000, "profit": 3600},
    {"month": "Mar", "sales": 22000, "profit": 4400}
  ]},
  "insight_types": ["trends", "outliers", "correlations"]
}
```

> Note: `detect_optimal_chart` can run with only `data` (no API key required). 

## 📊 Chart Types Available

### Basic Charts
- **Bar Charts**: Compare categories
- **Line Charts**: Show trends over time
- **Pie Charts**: Display proportions
- **Scatter Plots**: Reveal correlations

### Advanced Charts
- **Heatmaps**: Matrix visualizations
- **Treemaps**: Hierarchical data
- **Sankey Diagrams**: Flow visualization
- **Choropleth Maps**: Geographic data

### Statistical Charts
- **Box Plots**: Distribution analysis
- **Histograms**: Frequency distributions
- **Violin Plots**: Density distributions

---

## 🔧 Available Tools

When you type in Cursor, you'll see these ChartSmith tools:

### Core Generation
- `generate_chart_auto` - Let AI choose the best chart type
- `generate_bar_chart` - Create bar/column charts
- `generate_line_chart` - Time series and trends
- `generate_pie_chart` - Pie and donut charts
- `generate_scatter_chart` - Correlation analysis
- `generate_heatmap_chart` - Matrix visualizations

### AI Analysis
- `detect_optimal_chart` - Get AI recommendations
- `analyze_and_visualize` - Natural language to chart
- `generate_chart_insights` - Business intelligence

### Advanced Features
- `create_dashboard` - Multi-chart dashboards
- `generate_chart_batch` - Process multiple datasets

---

## 💡 Data Format Examples

### CSV Format
```csv
Region,Sales,Profit
North,125000,25000
South,98000,19600
East,156000,31200
West,87000,17400
```

### JSON Format
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

## 🎯 Pro Tips for Better Results

### 1. Be Specific
❌ "sales data"  
✅ "monthly sales trends for Q4 2024"

### 2. Include Context
❌ "make a chart"  
✅ "create a chart showing the impact of our holiday marketing campaign"

### 3. Ask for Insights
❌ "show the numbers"  
✅ "what patterns do you see in our customer acquisition data?"

### 4. Request Styling
❌ "basic chart"  
✅ "professional chart with dark theme for presentation"

---

## 💾 Chart Outputs & File Saving

ChartSmith MCP returns chart data that can be displayed in your MCP client or saved as files:

### **Output Formats Available:**
- **HTML**: Complete standalone HTML files with embedded Plotly
- **JSON**: Plotly JSON specification for developers
- **SVG**: Scalable vector graphics
- **PNG**: Raster images

### **How Outputs Work:**
1. **In MCP Clients** (like Cursor): Charts display inline automatically
2. **For File Saving**: The client receives chart data as payload
3. **Manual Saving**: You can save the HTML/JSON payload to files

### **File Saving Example:**
When you request `format: 'html'`, ChartSmith returns a complete HTML file that you can:
- Copy and save as `.html` 
- Open in any web browser
- Embed in websites
- Share with others

**Tip**: HTML output includes the full Plotly library (~4.6MB) so charts work offline!

## 🎉 What's Next?

Great job! You've created your first chart. Now explore:

- 📈 [Chart Gallery with Examples](../examples/chart-gallery.md)
- 🔧 [Advanced Configuration](../advanced/configuration.md)
- 📚 [Tutorials and Use Cases](../examples/tutorials.md)
- 🚀 [Dashboard Creation](../examples/code-examples.md)

**Ready to become a ChartSmith expert?** 🚀
