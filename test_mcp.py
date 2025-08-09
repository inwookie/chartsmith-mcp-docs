#!/usr/bin/env python3
"""
Test script to verify ChartSmith MCP functionality
"""
import json
import subprocess
import tempfile
import os

def test_chart_generation():
    """Test basic chart generation via MCP"""
    
    # Sample data for testing
    test_data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "generate_chart",
            "arguments": {
                "data": {
                    "columns": ["Product", "Sales"],
                    "rows": [
                        {"Product": "Product A", "Sales": 150},
                        {"Product": "Product B", "Sales": 120},
                        {"Product": "Product C", "Sales": 180},
                        {"Product": "Product D", "Sales": 90}
                    ]
                },
                "chart_type": "bar",
                "engine": "plotly",
                "theme": "modern"
            }
        }
    }
    
    # Write test data to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(test_data, f)
        temp_file = f.name
    
    try:
        # Test via docker run with stdin
        cmd = [
            "docker", "compose", "run", "--rm", "chartsmith-stdio",
            "python", "-m", "chart_genius_mcp", "--transport", "stdio"
        ]
        
        with open(temp_file, 'r') as f:
            result = subprocess.run(
                cmd, 
                stdin=f, 
                capture_output=True, 
                text=True,
                timeout=30
            )
        
        print("Return code:", result.returncode)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        
    except subprocess.TimeoutExpired:
        print("Command timed out")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        os.unlink(temp_file)

if __name__ == "__main__":
    test_chart_generation() 