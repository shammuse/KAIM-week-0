import pandas as pd
import plotly.express as px

def preprocess_data(data):
    """Preprocess the dataset: handle missing values and clean columns."""
    data = data.dropna() 
    return data

def visualize_data(data, chart_type, x, y, color=None):
    """Generate visualizations based on user input."""
    if chart_type == "Scatter Plot":
        return px.scatter(data, x=x, y=y, color=color)
    elif chart_type == "Bar Chart":
        return px.bar(data, x=x, y=y, color=color)
    elif chart_type == "Line Chart":
        return px.line(data, x=x, y=y, color=color)
