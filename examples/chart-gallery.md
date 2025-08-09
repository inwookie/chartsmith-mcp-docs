---
layout: default
title: Chart Gallery
---

# 🖼️ Chart Gallery

Explore the stunning visualizations you can create with ChartSmith MCP.

## 🎯 Basic Charts

### 📊 Bar Charts

<iframe src="/chartsmith-mcp-docs/assets/gallery/bar.html" title="Bar Chart" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Perfect for comparing categories and showing rankings.

**Use Cases:**
- Sales by region
- Product performance comparison
- Survey responses
- Budget allocations

**Tool Input Example (`generate_bar_chart`):**
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

**Features:**
- ✅ Horizontal and vertical orientations
- ✅ Grouped and stacked bars
- ✅ Custom colors and themes
- ✅ Data labels and annotations

---

### 📈 Line Charts

<iframe src="/chartsmith-mcp-docs/assets/gallery/line.html" title="Line Chart" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Ideal for showing trends and changes over time.

**Use Cases:**
- Website traffic trends
- Stock price movements
- Temperature variations
- Growth metrics

**Tool Input Example (`generate_line_chart`):**
```json
{
  "data": {
    "rows": [
      {"month": "Jan", "users": 1200},
      {"month": "Feb", "users": 1350},
      {"month": "Mar", "users": 1420},
      {"month": "Apr", "users": 1580},
      {"month": "May", "users": 1750},
      {"month": "Jun", "users": 1890},
      {"month": "Jul", "users": 2100},
      {"month": "Aug", "users": 2280},
      {"month": "Sep", "users": 2450},
      {"month": "Oct", "users": 2600},
      {"month": "Nov", "users": 2780},
      {"month": "Dec", "users": 3000}
    ]
  },
  "x": "month",
  "y": "users"
}
```

**Features:**
- ✅ Multi-line comparisons
- ✅ Area charts and filled regions
- ✅ Trend lines and forecasting
- ✅ Interactive hover details

---

### 🥧 Pie Charts

<iframe src="/chartsmith-mcp-docs/assets/gallery/pie.html" title="Pie Chart" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Show proportions and parts of a whole.

**Use Cases:**
- Market share distribution
- Budget breakdowns
- Survey demographics
- Resource allocation

**Tool Input Example (`generate_pie_chart`):**
```json
{
  "data": {
    "rows": [
      {"channel": "Digital Ads",    "pct": 45},
      {"channel": "Content",        "pct": 25},
      {"channel": "Events",         "pct": 15},
      {"channel": "SEO/Analytics",  "pct": 10},
      {"channel": "Other",          "pct": 5}
    ]
  },
  "names": "channel",
  "values": "pct"
}
```

**Features:**
- ✅ Donut charts with center labels
- ✅ Exploded slices for emphasis
- ✅ Custom color palettes
- ✅ Percentage and value labels

---

### 🔗 Scatter Plots

<iframe src="/chartsmith-mcp-docs/assets/gallery/scatter.html" title="Scatter Plot" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Reveal correlations and relationships between variables.

**Use Cases:**
- Price vs. demand analysis
- Performance correlations
- Quality vs. satisfaction metrics
- Risk vs. return analysis

**Tool Input Example (`generate_scatter_chart`):**
```json
{
  "data": {
    "rows": [
      {"ad_spend": 5000, "sales": 125000},
      {"ad_spend": 7500, "sales": 142000},
      {"ad_spend": 6200, "sales": 135000},
      {"ad_spend": 8900, "sales": 165000},
      {"ad_spend": 4100, "sales": 118000}
    ]
  },
  "x": "ad_spend",
  "y": "sales"
}
```

**Features:**
- ✅ Bubble charts with size dimensions
- ✅ Trend lines and regression analysis
- ✅ Color coding by categories
- ✅ Statistical annotations

---

## 🎨 Advanced Visualizations

### 🔥 Heatmaps

<iframe src="/chartsmith-mcp-docs/assets/gallery/heatmap.html" title="Heatmap" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Perfect for matrix data and correlation analysis.

**Use Cases:**
- Correlation matrices
- Performance grids
- Geographic heat mapping
- Time-based activity patterns

**Tool Input Example (`generate_heatmap_chart`):**
```json
{
  "data": {
    "rows": [
      {"x": "Product A", "y": "Support",    "value": 4.5},
      {"x": "Product A", "y": "Onboarding", "value": 4.2},
      {"x": "Product B", "y": "Support",    "value": 3.8}
    ]
  },
  "x": "x",
  "y": "y",
  "value": "value"
}
```

**Features:**
- ✅ Custom color gradients
- ✅ Dendrograms for clustering
- ✅ Annotations and value overlays
- ✅ Interactive zooming

---

### 🌳 Treemaps

<iframe src="/chartsmith-mcp-docs/assets/gallery/treemap.html" title="Treemap" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Visualize hierarchical data with nested rectangles.

**Use Cases:**
- Portfolio composition
- File system visualization
- Organizational structures
- Market segment analysis

**Tool Input Example (`generate_treemap_chart`):**
```json
{
  "data": {
    "rows": [
      {"unit": "Enterprise", "category": "Security",     "value": 120},
      {"unit": "Enterprise", "category": "Analytics",    "value": 80},
      {"unit": "SMB",        "category": "Productivity", "value": 60}
    ]
  },
  "path": ["unit", "category"],
  "value": "value"
}
```

**Features:**
- ✅ Multiple hierarchy levels
- ✅ Custom color schemes
- ✅ Interactive drill-down
- ✅ Proportional sizing

---

### 🌊 Sankey Diagrams

<iframe src="/chartsmith-mcp-docs/assets/gallery/sankey.html" title="Sankey Diagram" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Show flow and movement between stages.

**Use Cases:**
- Customer journey mapping
- Budget flow analysis
- Supply chain visualization
- Process optimization

**Tool Input Example (`generate_sankey_chart`):**
```json
{
  "data": {
    "rows": [
      {"source": "Visitors",  "target": "Leads",      "value": 27680},
      {"source": "Leads",     "target": "QL",         "value": 5520},
      {"source": "QL",        "target": "Opps",       "value": 2760},
      {"source": "Opps",      "target": "Purchases",  "value": 1380}
    ]
  },
  "source": "source",
  "target": "target",
  "value": "value"
}
```

**Features:**
- ✅ Multi-stage flow visualization
- ✅ Custom link colors and widths
- ✅ Flow quantity annotations
- ✅ Interactive highlighting

---

## 📊 Statistical Charts

### �� Box Plots

<iframe src="/chartsmith-mcp-docs/assets/gallery/boxplot.html" title="Box Plot" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Display distribution statistics and identify outliers.

**Use Cases:**
- Performance distribution analysis
- Quality control metrics
- Salary range analysis
- Test score distributions

**Tool Input Example (`generate_box_chart`):**
```json
{
  "data": {
    "rows": [
      {"region": "us-east", "response_ms": 120},
      {"region": "us-east", "response_ms": 132},
      {"region": "eu-west", "response_ms": 150},
      {"region": "eu-west", "response_ms": 141}
    ]
  },
  "x": "region",
  "y": "response_ms"
}
```

**Features:**
- ✅ Quartile and median visualization
- ✅ Outlier identification
- ✅ Grouped comparisons
- ✅ Statistical annotations

---

### 📊 Histograms

<iframe src="/chartsmith-mcp-docs/assets/gallery/histogram.html" title="Histogram" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Show frequency distributions and data patterns.

**Use Cases:**
- Age distribution analysis
- Performance benchmarking
- Quality measurements
- Risk assessment

**Tool Input Example (`generate_histogram_chart` pre-binned):**
```json
{
  "data": {
    "rows": [
      {"bin_start": 0,   "bin_end": 50,  "bin_center": 25,  "count": 12, "frequency": 0.24, "percentage": 24},
      {"bin_start": 50,  "bin_end": 100, "bin_center": 75,  "count": 22, "frequency": 0.44, "percentage": 44},
      {"bin_start": 100, "bin_end": 150, "bin_center": 125, "count": 16, "frequency": 0.32, "percentage": 32}
    ]
  },
  "x": "bin_center"
}
```

**Features:**
- ✅ Automatic and custom binning
- ✅ Density overlays
- ✅ Statistical markers
- ✅ Multiple distributions

---

## 🎯 Interactive Features

### 📊 Dashboards

<iframe src="/chartsmith-mcp-docs/assets/gallery/dashboard.html" title="Dashboard" style="width:100%;height:420px;border:1px solid #eee;border-radius:8px;"></iframe>

Combine multiple charts for comprehensive analysis.

**Tool Input Example (`create_dashboard`):**
```json
{
  "charts": [
    {"chart_type": "line", "data": {"rows": [{"month":"Jan","revenue":50000},{"month":"Feb","revenue":55000},{"month":"Mar","revenue":62000}]}},
    {"chart_type": "bar",  "data": {"rows": [{"product":"A","sales":150000},{"product":"B","sales":120000},{"product":"C","sales":98000}]}},
    {"chart_type": "heatmap", "data": {"rows": [{"x":"North","y":"Q1","value":120},{"x":"North","y":"Q2","value":135},{"x":"South","y":"Q1","value":98}]}},
    {"chart_type": "pie", "data": {"rows": [{"segment":"Organic","pct":45},{"segment":"Social","pct":25},{"segment":"Direct","pct":20},{"segment":"Paid","pct":8},{"segment":"Email","pct":2}]}, "names": "segment", "values": "pct"}
  ],
  "layout": "grid"
}
```

**Features:**
- ✅ Multiple chart layouts
- ✅ Consistent styling themes
- ✅ Cross-chart filtering
- ✅ Export capabilities

---

## 🎨 Styling Options

### 🌟 Themes
- **Modern**: Clean, professional styling
- **Dark**: Perfect for presentations
- **Colorful**: Vibrant, engaging palettes
- **Minimal**: Clean, distraction-free
- **Corporate**: Business-ready styling

### 🎯 Customization
- **Colors**: Custom palettes and brand colors
- **Fonts**: Typography that matches your brand
- **Layouts**: Flexible sizing and positioning
- **Animations**: Smooth transitions and interactions

---

## 💡 Getting Started

Ready to create these amazing visualizations?

1. **[Install ChartSmith MCP](../getting-started/installation.md)**
2. **[Try Your First Chart](../getting-started/first-chart.md)**
3. **[Explore Code Examples](code-examples.md)**

**Pro Tip**: Start with simple examples and gradually explore more advanced features. ChartSmith's AI will guide you to the best visualization for your data! 🚀
