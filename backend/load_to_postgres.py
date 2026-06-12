import pandas as pd
from sqlalchemy import create_engine

# ==========================
# CONNECTION
# ==========================

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/skyprice_ai"
)

# ==========================
# LOAD CSV FILES
# ==========================

booking_df = pd.read_csv(
    "datasets/booking.csv"
)

forecast_df = pd.read_csv(
    "datasets/route_forecasts.csv"
)

optimization_df = pd.read_csv(
    "datasets/revenue_optimization_output.csv"
)

pricing_df = pd.read_csv(
    "datasets/dynamic_pricing_output.csv"
)

profit_df = pd.read_csv(
    "datasets/route_profitability_output.csv"
)

network_df = pd.read_csv(
    "datasets/network_optimization_output.csv"
)

elasticity_df = pd.read_csv(
    "datasets/price_elasticity_output.csv"
)

competitor_df = pd.read_csv(
    "datasets/competitor_pricing_output.csv"
)

# ==========================
# SAVE TO POSTGRES
# ==========================

booking_df.to_sql(
    "bookings",
    engine,
    if_exists="replace",
    index=False
)

forecast_df.to_sql(
    "forecasts",
    engine,
    if_exists="replace",
    index=False
)

optimization_df.to_sql(
    "optimizations",
    engine,
    if_exists="replace",
    index=False
)

pricing_df.to_sql(
    "pricing",
    engine,
    if_exists="replace",
    index=False
)

profit_df.to_sql(
    "profitability",
    engine,
    if_exists="replace",
    index=False
)

network_df.to_sql(
    "network_optimization",
    engine,
    if_exists="replace",
    index=False
)

elasticity_df.to_sql(
    "elasticity",
    engine,
    if_exists="replace",
    index=False
)

competitor_df.to_sql(
    "competitor_pricing",
    engine,
    if_exists="replace",
    index=False
)

print("\nAll tables loaded into PostgreSQL successfully.")