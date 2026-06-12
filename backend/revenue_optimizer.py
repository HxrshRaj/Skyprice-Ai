import sys
import os
import numpy as np
import pandas as pd

# ==========================
# LOAD REVPY
# ==========================

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "revpy_core"
    )
)

from revpy.optimizers import calc_EMSRb

# ==========================
# LOAD FORECASTS
# ==========================

forecast_df = pd.read_csv(
    "datasets/route_forecasts.csv"
)

results = []

# ==========================
# RUN EMSRb FOR EACH ROUTE
# ==========================

for _, row in forecast_df.iterrows():

    route = row["route"]
    forecast_demand = int(row["forecast_demand"])

    fares = np.array([
        12000,
        8000,
        5000,
        3000
    ])

    demands = np.array([
        max(10, int(forecast_demand * 0.10)),
        max(20, int(forecast_demand * 0.20)),
        max(40, int(forecast_demand * 0.30)),
        max(60, int(forecast_demand * 0.40))
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

    results.append({
        "route": route,
        "forecast_demand": forecast_demand,
        "business_protection": int(protection_levels[0]),
        "premium_protection": int(protection_levels[1]),
        "economy_protection": int(protection_levels[2]),
        "saver_protection": int(protection_levels[3])
    })

# ==========================
# SAVE OUTPUT
# ==========================

output_df = pd.DataFrame(results)

output_df.to_csv(
    "datasets/revenue_optimization_output.csv",
    index=False
)

print("\nRevenue Optimization Results\n")
print(output_df)

print("\nSaved to revenue_optimization_output.csv")