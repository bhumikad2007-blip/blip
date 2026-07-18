import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Asset Portfolio Tracker", page_icon="📈", layout="wide")
st.title("📈 Real-Time Multi-Asset Portfolio Dashboard Tracker")
st.markdown("---")

col_side, col_main = st.columns([1, 2])

with col_side:
    st.header("Transaction Inputs")
    asset_type = st.selectbox("Select Target Ledger Type", ["Cryptocurrency Token", "Indian Equities Stock"])
    asset_name = st.text_input("Enter Asset Ticker Symbol Name", "BTC" if asset_type == "Cryptocurrency Token" else "RELIANCE")
    buy_price = st.number_input("Enter Your Purchase Entry Price (₹)", min_value=1.0, value=100.0)
    quantity = st.number_input("Enter Volume Quantity Purchased", min_value=0.1, value=5.0)

with col_main:
    st.header("Active Portfolio Market Evaluation Metrics")
    
    # Simulate a dynamic market feed price drift using random percentages
    simulated_live_price = buy_price * np.random.uniform(0.92, 1.15)
    total_cost = buy_price * quantity
    current_value = simulated_live_price * quantity
    total_pnl = current_value - total_cost
    pnl_percentage = (total_pnl / total_cost) * 100
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Invested Cost Basis", f"₹{total_cost:,.2f}")
    m2.metric("Simulated Live Spot Price", f"₹{simulated_live_price:,.2f}")
    m3.metric("Net Profit / Loss Return", f"₹{total_pnl:,.2f}", delta=f"{pnl_percentage:.2f}%")
    
    # Generate historical baseline visualization data framework
    st.markdown("---")
    st.subheader("Historical Trajectory Performance Evaluation")
    time_series = pd.DataFrame({
        "Day Timeline": [f"Day {i}" for i in range(1, 11)],
        "Market Valuation Spot Price Index": np.linspace(buy_price * 0.9, simulated_live_price, 10)
    })
    
    fig_line = px.line(time_series, x="Day Timeline", y="Market Valuation Spot Price Index", title=f"Price Performance Track For {asset_name}")
    st.plotly_chart(fig_line, use_container_width=True)