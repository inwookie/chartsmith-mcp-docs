---
layout: default
title: Create Your First Chart
---

# 📊 Create Your First Chart

Let's create your first chart with ChartSmith MCP!

## ✅ Tested Working Examples

These examples have been verified to work with ChartSmith MCP (no API key required):

### **Bar Chart: Sales by Region**
```
Create a bar chart showing sales by region:
- North: 125,000
- South: 98,000  
- East: 156,000
- West: 87,000
```

### **Line Chart: Product Performance**
```
Show product performance over quarters:
Q1: Product A $45k, Q2: $52k, Q3: $48k, Q4: $55k
```

### **Pie Chart: Traffic Sources**
```
Create a pie chart of website traffic sources:
- Organic Search: 45%
- Social Media: 25%
- Direct Traffic: 20%
- Paid Ads: 8%
- Email: 2%
```

## 🤖 AI-Powered Features (API Key Required)

✅ **VERIFIED WORKING** with real OpenAI API key:

### **Auto Chart Selection**
```
"Show revenue trends over months and suggest the best visualization approach"
```
**Result**: AI analyzes your data and automatically selects the optimal chart type with detailed reasoning.

### **Smart Data Analysis**  
```
"Compare profit margins across different months and identify patterns"
```
**Result**: AI provides chart recommendations with confidence scores and explanations.

**To use AI features**: Add your OpenAI API key to the `.env` file:
```bash
OPENAI_API_KEY=sk-proj-your-actual-key-here
```

## 🚀 Quick Start Example

Once ChartSmith MCP is connected to Cursor, try this simple example:

### Example 1: Basic Bar Chart
```
Create a bar chart showing Q4 sales by region:
- North: $125,000
- South: $98,000  
- East: $156,000
- West: $87,000
```

**Result**: ChartSmith will automatically:
- ✅ Detect this is categorical data
- ✅ Choose a bar chart visualization  
- ✅ Apply professional styling
- ✅ Generate insights about regional performance

---

## 🧠 AI-Powered Chart Creation

### Natural Language Requests
ChartSmith understands natural language. Try these:

```
"Show me website traffic trends over the last 6 months"
```

```
"Create a pie chart of our marketing budget breakdown"
```

```
"I have sales data - what's the best way to visualize it?"
```

### Smart Data Detection
Upload or paste your data, and ChartSmith will:
- 🔍 **Analyze data patterns**
- 🎯 **Suggest optimal chart types**
- 🎨 **Apply appropriate styling**
- 💡 **Generate business insights**

---

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
