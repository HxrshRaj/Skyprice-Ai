import pandas as pd
import random

# ==========================
# LOAD PRICING DATA
# ==========================

df = pd.read_csv(
    "datasets/dynamic_pricing_output.csv"
)

# ==========================
# COMPETITOR ANALYSIS
# ==========================

results = []

for _, row in df.iterrows():

    our_price = row["recommended_price"]

    competitor_price = round(
        our_price * random.uniform(0.90, 1.10),
        0
    )

    difference = round(
        our_price - competitor_price,
        0
    )

    if difference > 200:
        recommendation = "Reduce Price"

    elif difference < -200:
        recommendation = "Increase Price"

    else:
        recommendation = "Competitive"

    results.append({
        "route": row["route"],
        "our_price": our_price,
        "competitor_price": competitor_price,
        "price_difference": difference,
        "recommendation": recommendation
    })

# ==========================
# SAVE OUTPUT
# ==========================

output_df = pd.DataFrame(results)

output_df.to_csv(
    "datasets/competitor_pricing_output.csv",
    index=False
)

print("\nCompetitor Pricing Results\n")

print(output_df)

print(
    "\nSaved to competitor_pricing_output.csv"
)