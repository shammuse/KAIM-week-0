import streamlit as st
import pandas as pd
import plotly.express as px
from utils import preprocess_data, visualize_data

# Page configuration
st.set_page_config(
    page_title="Interactive Dashboard",
    page_icon="📊",
    layout="wide",
)

# Title and description
st.title("📊 Interactive Data Dashboard")
st.markdown("Upload your dataset, explore insights, and customize visualizations dynamically.")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Raw Data Preview", data.head())

    # Data Preprocessing
    data = preprocess_data(data)

    # Sidebar options
    st.sidebar.header("Visualization Options")
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Scatter Plot", "Bar Chart", "Line Chart"])
    x_axis = st.sidebar.selectbox("Select X-Axis", data.columns)
    y_axis = st.sidebar.selectbox("Select Y-Axis", data.columns)
    color = st.sidebar.selectbox("Select Color Column (Optional)", [None] + list(data.columns))

    # Generate visualization
    st.write("### Visualization")
    fig = visualize_data(data, chart_type, x_axis, y_axis, color)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Please upload a CSV file to get started.")



