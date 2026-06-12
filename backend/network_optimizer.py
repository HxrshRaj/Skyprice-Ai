from ortools.linear_solver import pywraplp
import pandas as pd

# ==========================
# LOAD FORECASTS
# ==========================

forecast_df = pd.read_csv(
    "datasets/route_forecasts.csv"
)

# ==========================
# SOLVER
# ==========================

solver = pywraplp.Solver.CreateSolver("SCIP")

if not solver:
    raise Exception("SCIP Solver not available")

# ==========================
# PARAMETERS
# ==========================

TOTAL_SEATS = 1000

routes = forecast_df["route"].tolist()

forecast_demand = {
    row["route"]: int(row["forecast_demand"])
    for _, row in forecast_df.iterrows()
}

# Revenue per passenger estimate

yield_per_route = {
    "DEL-BOM": 6500,
    "DEL-BLR": 6200,
    "DEL-HYD": 5800,
    "BOM-BLR": 6000,
    "BLR-HYD": 5500
}

# ==========================
# DECISION VARIABLES
# ==========================

seat_allocations = {}

for route in routes:
    seat_allocations[route] = solver.IntVar(
        0,
        TOTAL_SEATS,
        route
    )

# ==========================
# CAPACITY CONSTRAINT
# ==========================

solver.Add(
    sum(
        seat_allocations[r]
        for r in routes
    ) <= TOTAL_SEATS
)

# ==========================
# DEMAND CONSTRAINT
# ==========================

for route in routes:

    solver.Add(
        seat_allocations[route]
        <= forecast_demand[route]
    )

# ==========================
# OBJECTIVE
# ==========================

solver.Maximize(

    sum(
        seat_allocations[r]
        * yield_per_route[r]
        for r in routes
    )

)

# ==========================
# SOLVE
# ==========================

status = solver.Solve()

# ==========================
# OUTPUT
# ==========================

results = []

if status == pywraplp.Solver.OPTIMAL:

    for route in routes:

        seats = int(
            seat_allocations[route].solution_value()
        )

        revenue = (
            seats
            * yield_per_route[route]
        )

        results.append({
            "route": route,
            "allocated_seats": seats,
            "yield_per_passenger":
                yield_per_route[route],
            "optimized_revenue":
                revenue
        })

output_df = pd.DataFrame(results)

output_df.to_csv(
    "datasets/network_optimization_output.csv",
    index=False
)

print("\nNetwork Optimization Results\n")

print(output_df)

print(
    "\nSaved to network_optimization_output.csv"
)