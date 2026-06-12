import pandas as pd

# ==========================
# LOAD OPTIMIZATION OUTPUT
# ==========================

df = pd.read_csv(
    "datasets/revenue_optimization_output.csv"
)

results = []

# ==========================
# PRICING LOGIC
# ==========================

BASE_PRICE = 5000

for _, row in df.iterrows():

    demand = row["forecast_demand"]

    if demand >= 280:
        multiplier = 1.20

    elif demand >= 250:
        multiplier = 1.10

    elif demand >= 220:
        multiplier = 1.05

    else:
        multiplier = 0.95

    recommended_price = round(
        BASE_PRICE * multiplier,
        0
    )

    results.append({
        "route": row["route"],
        "forecast_demand": demand,
        "current_price": BASE_PRICE,
        "recommended_price": recommended_price,
        "price_change_percent":
            round((multiplier - 1) * 100, 2)
    })

# ==========================
# SAVE OUTPUT
# ==========================

output_df = pd.DataFrame(results)

output_df.to_csv(
    "datasets/dynamic_pricing_output.csv",
    index=False
)

print("\nDynamic Pricing Results\n")

print(output_df)

print(
    "\nSaved to dynamic_pricing_output.csv"
)