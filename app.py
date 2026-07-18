import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Expense Analyzer", layout="wide")
st.title("📊 Smart Personal Expense Analyzer")
st.markdown("---")

# 2. Sidebar File Uploader
st.sidebar.header("Upload Portal")
uploaded_file = st.sidebar.file_uploader("Upload your expense CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded data
    df = pd.read_csv(uploaded_file)
    
    # Show data table
    with st.expander("🔍 View Uploaded Data Table"):
        st.dataframe(df, use_container_width=True)
        
    # Split screen into two columns for charts
    col1, col2 = st.columns(2)
    
    # Identify necessary columns dynamically
    cat_col = 'Category' if 'Category' in df.columns else df.columns[0]
    amt_col = 'Amount' if 'Amount' in df.columns else df.columns[-1]
    
    with col1:
        st.subheader("Spending Category Distribution")
        fig_pie = px.pie(df, names=cat_col, values=amt_col, hole=0.3)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col2:
        st.subheader("Transaction Volumes")
        fig_bar = px.bar(df, x=cat_col, y=amt_col, color=cat_col)
        st.plotly_chart(fig_bar, use_container_width=True)
        
    # 3. Predictive Analysis Block
    st.markdown("---")
    st.subheader("🔮 Predictive Evaluation")
    
    if st.button("Predict Next Month's Budget"):
        try:
            historical_mean = df[amt_col].mean()
            predicted_increase = historical_mean * 1.05  # Adds a 5% inflation factor
            
            m1, m2 = st.columns(2)
            m1.metric(label="Current Monthly Average", value=f"₹{historical_mean:,.2f}")
            m2.metric(label="Predicted Next Month Budget", value=f"₹{predicted_increase:,.2f}", delta="+5%")
        except Exception as e:
            st.error("Make sure your dataset has numerical values in the Amount column.")
else:
    st.info("💡 Please upload an expense CSV file from the left sidebar to populate your visual dashboard.")