import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("datasets/demand.csv")

# ==========================
# FEATURE ENGINEERING
# ==========================

df["date"] = pd.to_datetime(df["date"])

df["day"] = df["date"].dt.day
df["month"] = df["date"].dt.month
df["weekday"] = df["date"].dt.weekday

df["route_code"] = df["route"].astype("category").cat.codes

# ==========================
# FEATURES & TARGET
# ==========================

X = df[
    [
        "day",
        "month",
        "weekday",
        "route_code"
    ]
]

y = df["expected_demand"]

# ==========================
# MODEL
# ==========================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# ==========================
# FORECAST LATEST DEMAND
# ==========================

latest_rows = df.groupby("route").tail(1).copy()

future_df = latest_rows.copy()

future_df["day"] = future_df["day"] + 1

future_X = future_df[
    [
        "day",
        "month",
        "weekday",
        "route_code"
    ]
]

future_predictions = model.predict(future_X)

# ==========================
# SAVE FORECAST
# ==========================

forecast_output = pd.DataFrame({
    "route": future_df["route"].values,
    "forecast_demand": future_predictions.round().astype(int)
})

forecast_output.to_csv(
    "datasets/route_forecasts.csv",
    index=False
)

# ==========================
# EVALUATION
# ==========================

predictions = model.predict(X)

mae = mean_absolute_error(
    y,
    predictions
)

print(f"\nMAE: {mae:.2f}")

print("\nRoute Forecasts")

print(forecast_output)

print("\nForecast saved to route_forecasts.csv")