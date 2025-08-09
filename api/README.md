---
layout: default
title: API Reference
---

# 📡 API Reference

Complete technical documentation for ChartSmith MCP tools and resources.

## 🛠️ Available Tools

ChartSmith MCP provides 20+ powerful tools for chart generation and data analysis.

### Chart Generation Tools

#### `generate_chart_auto`
**Description**: Automatically detects the best chart type for your data and generates it.

**Parameters**:
- `data` (required): The dataset to visualize
- `title` (optional): Chart title
- `theme` (optional): Visual theme (modern, dark, colorful, minimal, corporate)
- `format` (optional): Output format (png, svg, pdf, html, json)

**Example**:
```json
{
  "data": {
    "columns": ["region", "sales"],
    "rows": [
      {"region": "North", "sales": 125000},
      {"region": "South", "sales": 98000},
      {"region": "East", "sales": 156000},
      {"region": "West", "sales": 87000}
    ]
  },
  "title": "Q4 Sales by Region",
  "theme": "modern"
}
```

---

#### `generate_bar_chart`
**Description**: Creates horizontal or vertical bar charts for categorical data comparison.

**Parameters**:
- `data` (required): Dataset with categorical and numerical columns
- `x_column` (required): Column name for x-axis (categories)
- `y_column` (required): Column name for y-axis (values)
- `orientation` (optional): "vertical" or "horizontal" (default: vertical)
- `color_scheme` (optional): Color palette name
- `title` (optional): Chart title
- `x_label` (optional): X-axis label
- `y_label` (optional): Y-axis label

**Example**:
```json
{
  "data": {...},
  "x_column": "product",
  "y_column": "revenue",
  "orientation": "horizontal",
  "title": "Product Revenue Comparison",
  "color_scheme": "viridis"
}
```

---

#### `generate_line_chart`
**Description**: Creates line charts for time series data and trend analysis.

**Parameters**:
- `data` (required): Dataset with time/sequential data
- `x_column` (required): Column for x-axis (usually time/date)
- `y_column` (required): Column for y-axis (values)
- `group_column` (optional): Column for multiple lines
- `show_markers` (optional): Boolean to show data point markers
- `line_style` (optional): Line style (solid, dashed, dotted)
- `fill_area` (optional): Boolean to fill area under line

**Example**:
```json
{
  "data": {...},
  "x_column": "date",
  "y_column": "users",
  "show_markers": true,
  "fill_area": false,
  "title": "Monthly Active Users"
}
```

---

#### `generate_pie_chart`
**Description**: Creates pie charts for showing proportions and parts of a whole.

**Parameters**:
- `data` (required): Dataset with categories and values
- `category_column` (required): Column with category names
- `value_column` (required): Column with values
- `chart_type` (optional): "pie" or "donut" (default: pie)
- `show_percentages` (optional): Boolean to display percentages
- `explode_slice` (optional): Index of slice to separate
- `hole_size` (optional): Size of hole for donut charts (0.0-0.9)

**Example**:
```json
{
  "data": {...},
  "category_column": "department",
  "value_column": "budget",
  "chart_type": "donut",
  "show_percentages": true,
  "hole_size": 0.4
}
```

---

#### `generate_scatter_plot`
**Description**: Creates scatter plots for correlation analysis and relationship visualization.

**Parameters**:
- `data` (required): Dataset with numerical columns
- `x_column` (required): X-axis column
- `y_column` (required): Y-axis column
- `size_column` (optional): Column for bubble size
- `color_column` (optional): Column for color coding
- `show_trendline` (optional): Boolean to show trend line
- `alpha` (optional): Point transparency (0.0-1.0)

**Example**:
```json
{
  "data": {...},
  "x_column": "advertising_spend",
  "y_column": "sales_revenue",
  "size_column": "market_size",
  "show_trendline": true,
  "alpha": 0.7
}
```

---

#### `generate_heatmap`
**Description**: Creates heatmaps for matrix data and correlation visualization.

**Parameters**:
- `data` (required): Matrix data or correlation data
- `x_column` (optional): X-axis categories
- `y_column` (optional): Y-axis categories
- `value_column` (optional): Values for color intensity
- `color_scale` (optional): Color scale (viridis, plasma, coolwarm)
- `show_values` (optional): Boolean to display values in cells
- `annotation_format` (optional): Format for cell annotations

**Example**:
```json
{
  "data": {...},
  "x_column": "month",
  "y_column": "product",
  "value_column": "sales",
  "color_scale": "viridis",
  "show_values": true
}
```

---

### AI-Powered Analysis Tools

#### `detect_optimal_chart`
**Description**: Uses AI to analyze your data and recommend the best chart type.

**Parameters**:
- `data` (required): Dataset to analyze
- `goal` (optional): Visualization goal (comparison, trend, distribution, correlation)
- `audience` (optional): Target audience (executives, analysts, general)

**Returns**: Recommendations with confidence scores

**Example**:
```json
{
  "data": {...},
  "goal": "comparison",
  "audience": "executives"
}
```

---

#### `analyze_and_visualize`
**Description**: Natural language interface for creating charts from text descriptions.

**Parameters**:
- `description` (required): Natural language description of desired chart
- `data` (optional): Dataset to use
- `context` (optional): Additional context about the data

**Example**:
```json
{
  "description": "Show me how our quarterly sales have changed over the past year",
  "data": {...},
  "context": "This is for a board presentation"
}
```

---

#### `generate_chart_insights`
**Description**: Generates AI-powered insights and observations about your data.

**Parameters**:
- `data` (required): Dataset to analyze
- `chart_type` (optional): Type of chart to focus insights on
- `business_context` (optional): Business context for relevant insights

**Returns**: List of insights, trends, and recommendations

---

### Advanced Features

#### `create_dashboard`
**Description**: Creates multi-chart dashboards with consistent styling.

**Parameters**:
- `charts` (required): Array of chart configurations
- `layout` (optional): Dashboard layout (grid, vertical, horizontal)
- `theme` (optional): Consistent theme across all charts
- `title` (optional): Dashboard title

**Example**:
```json
{
  "charts": [
    {"type": "bar", "data": {...}, "title": "Sales by Region"},
    {"type": "line", "data": {...}, "title": "Monthly Trends"}
  ],
  "layout": "grid",
  "theme": "corporate",
  "title": "Q4 Performance Dashboard"
}
```

---

#### `generate_chart_batch`
**Description**: Processes multiple datasets and creates charts in batch.

**Parameters**:
- `datasets` (required): Array of datasets with chart configurations
- `common_theme` (optional): Theme to apply to all charts
- `output_format` (optional): Format for all outputs

**Example**:
```json
{
  "datasets": [
    {"data": {...}, "type": "bar", "title": "Chart 1"},
    {"data": {...}, "type": "line", "title": "Chart 2"}
  ],
  "common_theme": "modern",
  "output_format": "png"
}
```

---

### Utility Tools

#### `get_performance_stats`
**Description**: Returns server performance metrics and statistics.

**Returns**:
- Uptime
- Charts generated
- Average response time
- Memory usage
- Cache hit rate

**Example Response**:
```json
{
  "uptime": "7d 14h 32m",
  "charts_generated": 15420,
  "avg_response_time": "145ms",
  "memory_usage": "2.1GB",
  "cache_hit_rate": "87%",
  "performance_grade": "A+"
}
```

---

## 🧾 Data Formats

### Supported Input Formats

#### JSON Format
```json
{
  "columns": ["date", "revenue", "costs"],
  "rows": [
    {"date": "2024-01", "revenue": 125000, "costs": 75000},
    {"date": "2024-02", "revenue": 132000, "costs": 78000},
    {"date": "2024-03", "revenue": 118000, "costs": 72000}
  ]
}
```

#### CSV Format
```csv
date,revenue,costs
2024-01,125000,75000
2024-02,132000,78000
2024-03,118000,72000
```

#### Array Format
```json
[
  ["date", "revenue", "costs"],
  ["2024-01", 125000, 75000],
  ["2024-02", 132000, 78000],
  ["2024-03", 118000, 72000]
]
```

### Output Formats

- **PNG**: High-quality raster images
- **SVG**: Scalable vector graphics
- **PDF**: Print-ready documents
- **HTML**: Interactive web charts
- **JSON**: Chart configuration and data

---

## 🎨 Themes & Styling

### Available Themes
- **modern**: Clean, contemporary design
- **dark**: Dark background for presentations
- **colorful**: Vibrant, engaging colors
- **minimal**: Clean, distraction-free
- **corporate**: Professional business styling

### Color Schemes
- **default**: Balanced, accessible colors
- **viridis**: Purple to yellow gradient
- **plasma**: Purple to pink gradient
- **coolwarm**: Blue to red gradient
- **custom**: User-defined color palette

### Chart Dimensions
- **Default**: 800x600 pixels
- **Square**: 600x600 pixels
- **Wide**: 1200x600 pixels
- **Tall**: 600x1200 pixels
- **Custom**: User-specified dimensions

---

## 🔧 Configuration Options

### Global Settings
```json
{
  "theme": "modern",
  "color_scheme": "default",
  "font_family": "Arial",
  "font_size": 12,
  "dpi": 300,
  "background_color": "#ffffff",
  "grid_enabled": true,
  "legend_position": "right"
}
```

### Performance Settings
```json
{
  "max_data_points": 10000,
  "timeout_ms": 60000,
  "cache_enabled": true,
  "compression": true
}
```

---

## 📈 Response Format

### Success Response
```json
{
  "success": true,
  "chart_data": "base64_encoded_image_or_svg",
  "metadata": {
    "chart_type": "bar",
    "data_points": 156,
    "generation_time": "245ms",
    "format": "png",
    "dimensions": "800x600"
  },
  "insights": [
    "Sales increased 15% compared to previous quarter",
    "East region shows strongest growth at 23%"
  ]
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "INVALID_DATA",
    "message": "Data format not recognized",
    "details": "Expected JSON object with 'columns' and 'rows' properties"
  }
}
```

---

## 🔗 Integration Examples

### Cursor Integration
```json
{
  "mcpServers": {
    "chartsmith": {
      "command": "docker",
      "args": ["exec", "-i", "chartsmith-mcp", "python", "-m", "chart_genius_mcp", "--transport", "stdio"]
    }
  }
}
```

### HTTP API Usage
```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "generate_bar_chart",
    "parameters": {
      "data": {...},
      "title": "Sales Report"
    }
  }'
```

**Need more technical details?** [Open a GitHub discussion](https://github.com/inwookie/chart-mcp-docs/discussions) 🚀
