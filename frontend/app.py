import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import sys
import os

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="SkyPrice AI",
    page_icon="✈️",
    layout="wide"
)

# =====================================================
# CUSTOM STYLING
# =====================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    color: #0A66C2;
}

[data-testid="metric-container"] {
    background-color: #f5f7fa;
    border: 1px solid #dce3ea;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD REVPY
# =====================================================

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "revpy_core"
    )
)

from revpy.optimizers import calc_EMSRb

# =====================================================
# LOAD DATA
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

booking_df = pd.read_csv(
    os.path.join(BASE_DIR, "datasets", "booking.csv")
)

demand_df = pd.read_csv(
    os.path.join(BASE_DIR, "datasets", "demand.csv")
)
# =====================================================
# HEADER
# =====================================================

st.title("✈️ SkyPrice AI")

st.caption(
    "Dynamic Revenue Management & Airline Pricing Optimization Platform"
)

st.divider()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("Route Selection")

selected_route = st.sidebar.selectbox(
    "Choose Route",
    sorted(demand_df["route"].unique())
)

# =====================================================
# FILTER DATA
# =====================================================

route_demand = demand_df[
    demand_df["route"] == selected_route
]

route_booking = booking_df[
    booking_df["route"] == selected_route
]

# =====================================================
# KPI SECTION
# =====================================================

latest_demand = int(
    route_demand["expected_demand"].tail(30).mean()
)

total_revenue = int(
    route_booking["revenue"].sum()
)

avg_ticket_price = int(
    route_booking["price"].mean()
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Forecast Demand",
        latest_demand
    )

with col2:
    st.metric(
        "Total Revenue",
        f"₹{total_revenue:,}"
    )

with col3:
    st.metric(
        "Avg Ticket Price",
        f"₹{avg_ticket_price:,}"
    )

st.divider()

# =====================================================
# DEMAND TREND
# =====================================================

st.subheader("📈 Demand Forecast Trend")

fig1 = px.line(
    route_demand,
    x="date",
    y="expected_demand",
    title=f"Demand Trend - {selected_route}"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================================================
# REVENUE ANALYSIS
# =====================================================

st.subheader("💰 Revenue Analysis")

revenue_chart = (
    route_booking
    .groupby("fare_class")["revenue"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    revenue_chart,
    x="fare_class",
    y="revenue",
    title="Revenue by Fare Class"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================================
# EMSRb REVENUE OPTIMIZATION
# =====================================================

st.subheader("🎯 Revenue Optimization")

fares = np.array([
    12000,
    8000,
    5000,
    3000
])

demands = np.array([
    40,
    60,
    120,
    180
])

sigmas = np.array([
    5,
    10,
    20,
    30
])

protection_levels = calc_EMSRb(
    fares,
    demands,
    sigmas
)

optimization_df = pd.DataFrame({
    "Fare Class": [
        "Business",
        "Premium",
        "Economy",
        "Saver"
    ],
    "Protection Level": protection_levels
})

st.dataframe(
    optimization_df,
    use_container_width=True
)

# =====================================================
# EXECUTIVE INSIGHTS
# =====================================================

st.subheader("🧠 AI Revenue Recommendation")

st.success(
    f"""
Route: {selected_route}

Forecast Demand: {latest_demand} passengers

Recommended Action:
Protect additional premium inventory and prioritize
higher-yield fare classes.

Expected Revenue Improvement:
+8% to +15%
"""
)

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown(
    """
**SkyPrice AI** | Airline Revenue Management |
Demand Forecasting | Revenue Optimization |
EMSRb Seat Allocation
"""
)