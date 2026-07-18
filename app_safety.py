import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Campus Safety App", page_icon="🚨", layout="centered")
st.title("🚨 Smart Campus Personal Safety Alert System")
st.markdown("---")

st.subheader("📍 Geofence Monitoring Framework")
st.markdown("Your profile is synchronized with the college emergency network node.")

# Mocking location coordinates around campus boundaries
campus_lat, campus_lon = 13.9351, 75.6025  # Standard region coordinates
df_loc = pd.DataFrame({
    'lat': [campus_lat],
    'lon': [campus_lon],
    'Label': ['Your Current Synced Node Location']
})

st.map(df_loc, zoom=14)

st.markdown("---")
st.subheader("⚠️ Panic Control Portal")
trigger_alert = st.button("🚨 TRIGGER EMERGENCY PANIC BROADCAST ALERT", type="primary", use_container_width=True)

if trigger_alert:
    st.error("🚨 EMERGENCY PROTOCOL INITIALIZED!")
    st.warning("⚠️ Dispatching your live coordinate array to security nodes...")
    
    m1, m2 = st.columns(2)
    m1.metric(label="Simulated GPS Coordinates Sent", value=f"{campus_lat:.4f} N, {campus_lon:.4f} E")
    m2.metric(label="Automated SOS Message Dispatch", value="Active Status: PUSHED")
    st.success("📩 An automated SMS alert tracking link has been routed via Twilio proxy simulations.")