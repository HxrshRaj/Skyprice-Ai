import streamlit as st
import pandas as pd
import plotly.express as px
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
# STYLING
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
# PATHS
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# =====================================================
# LOAD DATA
# =====================================================

booking_df = pd.read_csv(
    os.path.join(
        BASE_DIR,
        "datasets",
        "booking.csv"
    )
)

demand_df = pd.read_csv(
    os.path.join(
        BASE_DIR,
        "datasets",
        "demand.csv"
    )
)

forecast_df = pd.read_csv(
    os.path.join(
        BASE_DIR,
        "datasets",
        "route_forecasts.csv"
    )
)

optimization_df = pd.read_csv(
    os.path.join(
        BASE_DIR,
        "datasets",
        "revenue_optimization_output.csv"
    )
)

pricing_df = pd.read_csv(
    os.path.join(
        BASE_DIR,
        "datasets",
        "dynamic_pricing_output.csv"
    )
)

profit_df = pd.read_csv(
    os.path.join(
        BASE_DIR,
        "datasets",
        "route_profitability_output.csv"
    )
)

# =====================================================
# HEADER
# =====================================================

st.title("✈️ SkyPrice AI")

st.caption(
    "Airline Revenue Management & Pricing Optimization Platform"
)

st.divider()

# =====================================================
# SIDEBAR
# =====================================================

selected_route = st.sidebar.selectbox(
    "Select Route",
    sorted(
        forecast_df["route"].unique()
    )
)

# =====================================================
# FILTERS
# =====================================================

route_booking = booking_df[
    booking_df["route"] == selected_route
]

route_demand = demand_df[
    demand_df["route"] == selected_route
]

route_forecast = forecast_df[
    forecast_df["route"] == selected_route
]

route_optimization = optimization_df[
    optimization_df["route"] == selected_route
]

route_pricing = pricing_df[
    pricing_df["route"] == selected_route
]

route_profit = profit_df[
    profit_df["route"] == selected_route
]

# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Overview",
    "📈 Forecasting",
    "🎯 Optimization",
    "💲 Pricing",
    "💰 Profitability",
    "🧠 Insights"
])
# =====================================================
# TAB 1 - OVERVIEW
# =====================================================

with tab1:

    st.subheader("Executive Overview")

    forecast_demand = int(
        route_forecast["forecast_demand"].iloc[0]
    )

    total_revenue = int(
        route_booking["revenue"].sum()
    )

    avg_ticket_price = int(
        route_booking["price"].mean()
    )

    profit = int(
        route_profit["profit"].iloc[0]
    )

    recommended_price = int(
        route_pricing["recommended_price"].iloc[0]
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Forecast Demand",
            forecast_demand
        )

    with col2:
        st.metric(
            "Revenue",
            f"₹{total_revenue:,.0f}"
        )

    with col3:
        st.metric(
            "Profit",
            f"₹{profit:,.0f}"
        )

    with col4:
        st.metric(
            "Avg Fare",
            f"₹{avg_ticket_price:,.0f}"
        )

    with col5:
        st.metric(
            "Recommended Fare",
            f"₹{recommended_price:,.0f}"
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

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

    with col2:

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
# TAB 2 - DEMAND FORECASTING
# =====================================================

with tab2:

    st.subheader("Demand Forecasting Engine")

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

    fig3 = px.bar(
        forecast_df,
        x="route",
        y="forecast_demand",
        title="Forecast Demand by Route",
        text="forecast_demand"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# =====================================================
# TAB 3 - REVENUE OPTIMIZATION
# =====================================================

with tab3:

    st.subheader("EMSRb Revenue Optimization")

    optimization_table = pd.DataFrame({
        "Fare Class": [
            "Business",
            "Premium",
            "Economy",
            "Saver"
        ],
        "Protected Seats": [
            int(route_optimization["business_protection"].iloc[0]),
            int(route_optimization["premium_protection"].iloc[0]),
            int(route_optimization["economy_protection"].iloc[0]),
            int(route_optimization["saver_protection"].iloc[0])
        ]
    })

    st.dataframe(
        optimization_table,
        use_container_width=True
    )

    fig4 = px.bar(
        optimization_table,
        x="Fare Class",
        y="Protected Seats",
        title="Seat Protection Levels",
        text="Protected Seats"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )
# =====================================================
# TAB 4 - DYNAMIC PRICING
# =====================================================

with tab4:

    st.subheader("Dynamic Pricing Engine")

    current_price = int(
        route_pricing["current_price"].iloc[0]
    )

    recommended_price = int(
        route_pricing["recommended_price"].iloc[0]
    )

    price_change = float(
        route_pricing["price_change_percent"].iloc[0]
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Current Fare",
            f"₹{current_price:,.0f}"
        )

    with col2:
        st.metric(
            "Recommended Fare",
            f"₹{recommended_price:,.0f}"
        )

    with col3:
        st.metric(
            "Price Change %",
            f"{price_change}%"
        )

    pricing_table = pd.DataFrame({
        "Metric": [
            "Current Fare",
            "Recommended Fare",
            "Price Change %"
        ],
        "Value": [
            f"₹{current_price:,.0f}",
            f"₹{recommended_price:,.0f}",
            f"{price_change}%"
        ]
    })

    st.dataframe(
        pricing_table,
        use_container_width=True
    )

# =====================================================
# TAB 5 - ROUTE PROFITABILITY
# =====================================================

with tab5:

    st.subheader("Route Profitability Analysis")

    st.dataframe(
        profit_df,
        use_container_width=True
    )

    fig5 = px.bar(
        profit_df,
        x="route",
        y="profit",
        title="Profit by Route",
        text="profit"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    fig6 = px.bar(
        profit_df,
        x="route",
        y="profit_margin_percent",
        title="Profit Margin %",
        text="profit_margin_percent"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )
# =====================================================
# TAB 6 - EXECUTIVE INSIGHTS
# =====================================================

with tab6:

    st.subheader("Executive Decision Intelligence")

    forecast_demand = int(
        route_forecast["forecast_demand"].iloc[0]
    )

    premium_protection = int(
        route_optimization["premium_protection"].iloc[0]
    )

    recommended_price = int(
        route_pricing["recommended_price"].iloc[0]
    )

    profit_margin = float(
        route_profit["profit_margin_percent"].iloc[0]
    )

    insights = []

    if forecast_demand >= 280:
        insights.append(
            "🔥 High demand detected. Consider increasing fares and protecting premium inventory."
        )

    elif forecast_demand >= 250:
        insights.append(
            "📈 Moderate demand. Maintain current pricing strategy."
        )

    else:
        insights.append(
            "⚠️ Lower demand detected. Consider promotional campaigns."
        )

    if premium_protection >= 25:
        insights.append(
            "🎯 Strong premium demand. Preserve high-yield inventory."
        )

    if profit_margin >= 25:
        insights.append(
            "💰 Route is highly profitable and should remain a priority."
        )

    if recommended_price > 5000:
        insights.append(
            f"💲 Recommended fare increase to ₹{recommended_price:,} based on forecast demand."
        )

    for insight in insights:
        st.success(insight)

    st.divider()

    st.subheader("Executive Summary")

    st.info(
        f"""
        Route: {selected_route}

        Forecast Demand: {forecast_demand}

        Recommended Fare: ₹{recommended_price:,}

        Premium Protection Level: {premium_protection}

        Profit Margin: {profit_margin}%

        Revenue Opportunity: 8% - 15%
        """
    )

# =====================================================
# GLOBAL ROUTE RANKINGS
# =====================================================

st.divider()

st.subheader("🏆 Network Rankings")

col1, col2 = st.columns(2)

with col1:

    best_demand_route = forecast_df.loc[
        forecast_df["forecast_demand"].idxmax()
    ]

    st.success(
        f"""
        Highest Demand Route

        Route: {best_demand_route['route']}

        Forecast Demand:
        {best_demand_route['forecast_demand']}
        """
    )

with col2:

    best_profit_route = profit_df.loc[
        profit_df["profit"].idxmax()
    ]

    st.success(
        f"""
        Most Profitable Route

        Route: {best_profit_route['route']}

        Profit:
        ₹{best_profit_route['profit']:,.0f}
        """
    )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown(
    """
### ✈️ SkyPrice AI

Airline Revenue Management • Demand Forecasting • Dynamic Pricing • Revenue Optimization • Route Profitability • Decision Intelligence

Built using:

- Python
- Streamlit
- Pandas
- Plotly
- Scikit-Learn
- RevPy
- Operations Research
"""
)
