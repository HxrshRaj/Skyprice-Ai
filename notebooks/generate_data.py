import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

routes = [
    "DEL-BOM",
    "DEL-BLR",
    "BOM-BLR",
    "DEL-HYD",
    "BLR-HYD"
]

fare_classes = ["Economy", "Premium", "Business"]

# -----------------------
# BOOKINGS DATA
# -----------------------

records = []

start_date = datetime(2024, 1, 1)

for day in range(365):

    current_date = start_date + timedelta(days=day)

    for route in routes:

        for fare_class in fare_classes:

            tickets = np.random.randint(20, 200)

            price = {
                "Economy": np.random.randint(3000, 6000),
                "Premium": np.random.randint(6000, 10000),
                "Business": np.random.randint(10000, 20000)
            }[fare_class]

            revenue = tickets * price

            records.append([
                current_date,
                route,
                fare_class,
                tickets,
                price,
                revenue
            ])

bookings = pd.DataFrame(
    records,
    columns=[
        "date",
        "route",
        "fare_class",
        "tickets_sold",
        "price",
        "revenue"
    ]
)

bookings.to_csv("../datasets/booking.csv", index=False)

# -----------------------
# ROUTES
# -----------------------

routes_df = pd.DataFrame({
    "route": routes,
    "distance_km": [1150, 1750, 850, 1250, 500],
    "capacity": [180, 180, 180, 180, 180],
    "fuel_cost": [120000, 180000, 90000, 140000, 60000],
    "airport_fee": [50000, 60000, 45000, 55000, 35000]
})

routes_df.to_csv("../datasets/routes.csv", index=False)

# -----------------------
# FARES
# -----------------------

fares_df = bookings[
    ["route", "fare_class", "price"]
].drop_duplicates()

fares_df.to_csv("../datasets/fares.csv", index=False)

# -----------------------
# DEMAND
# -----------------------

demand_df = bookings.groupby(
    ["date", "route"]
)["tickets_sold"].sum().reset_index()

demand_df.rename(
    columns={"tickets_sold": "expected_demand"},
    inplace=True
)

demand_df.to_csv("../datasets/demand.csv", index=False)

print("Datasets generated successfully.")