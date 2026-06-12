import pandas as pd

# ==========================
# LOAD BOOKING DATA
# ==========================

booking_df = pd.read_csv(
    "datasets/booking.csv"
)

# ==========================
# ROUTE REVENUE
# ==========================

route_revenue = (
    booking_df
    .groupby("route")["revenue"]
    .sum()
    .reset_index()
)

# ==========================
# REALISTIC COST MODEL
# ==========================

route_revenue["operating_cost"] = (
    route_revenue["revenue"] * 0.72
).round()

# ==========================
# PROFIT
# ==========================

route_revenue["profit"] = (
    route_revenue["revenue"]
    - route_revenue["operating_cost"]
)

route_revenue["profit_margin_percent"] = (
    route_revenue["profit"]
    / route_revenue["revenue"]
    * 100
).round(2)

# ==========================
# SAVE OUTPUT
# ==========================

route_revenue.to_csv(
    "datasets/route_profitability_output.csv",
    index=False
)

print("\nRoute Profitability Results\n")

print(route_revenue)

print(
    "\nSaved to route_profitability_output.csv"
)