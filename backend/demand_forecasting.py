import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
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

# Route Encoding
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
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# MODEL
# ==========================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# PREDICTIONS
# ==========================

predictions = model.predict(X_test)

# ==========================
# EVALUATION
# ==========================

mae = mean_absolute_error(
    y_test,
    predictions
)

print(f"\nMAE: {mae:.2f}")

# ==========================
# SAMPLE RESULTS
# ==========================

results = pd.DataFrame({
    "Actual": y_test.values[:10],
    "Predicted": predictions[:10]
})

print("\nSample Predictions")
print(results)

# ==========================
# SAVE FORECAST OUTPUT
# ==========================

forecast_df = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

forecast_df.to_csv(
    "datasets/demand_forecast_output.csv",
    index=False
)

print("\nForecast saved successfully.")