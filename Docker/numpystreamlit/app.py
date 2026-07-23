import streamlit as st
import numpy as np

# Set the page title
st.title("💡 NumPy & Streamlit Interactive Demo")

# 1. User Input Widget
st.header("1. Configure Your Dataset")
num_samples = st.slider("Select the number of data samples:", min_value=100, max_value=5000, value=1000, step=100)

# 2. NumPy Data Generation
# Generate a standard normal distribution (Mean=0, SD=1) based on user input
np_array = np.random.randn(num_samples)

# 3. NumPy Calculations
mean_val = np.mean(np_array)
std_val = np.std(np_array)

# 4. Display Results in Streamlit
st.header("2. Dataset Metrics")
col1, col2 = st.columns(2)
col1.metric("Calculated Mean", f"{mean_val:.4f}")
col2.metric("Standard Deviation", f"{std_val:.4f}")

# 5. Visualizing the NumPy Array
st.header("3. Data Visualization")

# Display a sample of the raw array as an interactive table
st.subheader("Raw NumPy Array Preview (First 10 items)")
st.write(np_array[:10])

# Generate a histogram using NumPy and plot it with Streamlit's native bar chart
st.subheader("Data Distribution Histogram")
counts, bins = np.histogram(np_array, bins=30)
st.bar_chart(counts)
