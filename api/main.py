from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from api.database import engine

# =====================================================
# APP
# =====================================================

app = FastAPI(
    title="SkyPrice AI API"
)

# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# FORECAST
# =====================================================

@app.get("/forecast")
def forecast():

    df = pd.read_sql(
        "SELECT * FROM forecasts",
        engine
    )

    return df.to_dict(
        orient="records"
    )

# =====================================================
# PRICING
# =====================================================

@app.get("/pricing")
def pricing():

    df = pd.read_sql(
        "SELECT * FROM pricing",
        engine
    )

    return df.to_dict(
        orient="records"
    )

# =====================================================
# PROFITABILITY
# =====================================================

@app.get("/profitability")
def profitability():

    df = pd.read_sql(
        "SELECT * FROM profitability",
        engine
    )

    return df.to_dict(
        orient="records"
    )

# =====================================================
# OPTIMIZATION
# =====================================================

@app.get("/optimization")
def optimization():

    df = pd.read_sql(
        "SELECT * FROM optimizations",
        engine
    )

    return df.to_dict(
        orient="records"
    )

# =====================================================
# NETWORK OPTIMIZATION
# =====================================================

@app.get("/network")
def network():

    df = pd.read_sql(
        "SELECT * FROM network_optimization",
        engine
    )

    return df.to_dict(
        orient="records"
    )

# =====================================================
# ELASTICITY
# =====================================================

@app.get("/elasticity")
def elasticity():

    df = pd.read_sql(
        "SELECT * FROM elasticity",
        engine
    )

    return df.to_dict(
        orient="records"
    )

# =====================================================
# COMPETITOR PRICING
# =====================================================

@app.get("/competitor")
def competitor():

    df = pd.read_sql(
        "SELECT * FROM competitor_pricing",
        engine
    )

    return df.to_dict(
        orient="records"
    )

# =====================================================
# HEALTH CHECK
# =====================================================

@app.get("/")
def home():

    return {
        "message": "SkyPrice AI API Running"
    }