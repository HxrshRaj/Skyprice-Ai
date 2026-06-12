import pandas as pd

# ==========================
# LOAD BOOKING DATA
# ==========================

df = pd.read_csv(
    "datasets/booking.csv"
)

# ==========================
# ROUTE ANALYSIS
# ==========================

results = []

for route in df["route"].unique():

    route_df = df[
        df["route"] == route
    ]

    avg_price = route_df["price"].mean()

    avg_demand = route_df["tickets_sold"].mean()

    elasticity_score = round(
        avg_demand / avg_price,
        4
    )

    if elasticity_score > 0.03:
        strategy = "Highly Sensitive"

    elif elasticity_score > 0.02:
        strategy = "Moderately Sensitive"

    else:
        strategy = "Low Sensitivity"

    results.append({
        "route": route,
        "avg_price": round(avg_price, 2),
        "avg_demand": round(avg_demand, 2),
        "elasticity_score": elasticity_score,
        "pricing_strategy": strategy
    })

# ==========================
# SAVE OUTPUT
# ==========================

output_df = pd.DataFrame(results)

output_df.to_csv(
    "datasets/price_elasticity_output.csv",
    index=False
)

print("\nPrice Elasticity Results\n")

print(output_df)

print(
    "\nSaved to price_elasticity_output.csv"
)