import streamlit as st
import pandas as pd
from data_loader.mis_loader import load_mis

st.title("📊 MIS Overview")

df = load_mis()

# Sidebar filter
st.sidebar.header("Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["date"].min(), df["date"].max()]
)

# Filter data
df_filtered = df[
    (df["date"] >= pd.to_datetime(date_range[0])) &
    (df["date"] <= pd.to_datetime(date_range[1]))
]

# KPIs
revenue = df_filtered[df_filtered["type"] == "revenue"]["amount"].sum()
direct_cost = df_filtered[df_filtered["type"] == "direct_cost"]["amount"].sum()
indirect_cost = df_filtered[df_filtered["type"] == "indirect_cost"]["amount"].sum()

ebitda = revenue - direct_cost - indirect_cost

# Display KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", f"{revenue:,.0f}")
col2.metric("Direct Cost", f"{direct_cost:,.0f}")
col3.metric("Indirect Cost", f"{indirect_cost:,.0f}")
col4.metric("EBITDA", f"{ebitda:,.0f}")

# Chart
st.subheader("Revenue Trend")

trend = df_filtered[df_filtered["type"] == "revenue"].groupby("date")["amount"].sum().reset_index()

st.line_chart(trend.set_index("date"))
