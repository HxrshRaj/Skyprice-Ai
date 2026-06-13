function RouteRanking({
    forecasts,
    profitability
}) {

    const highestDemand =
        forecasts.length > 0
            ? forecasts.reduce(
                (a, b) =>
                    a.forecast_demand >
                    b.forecast_demand
                        ? a
                        : b
            )
            : null;

    const highestProfit =
        profitability.length > 0
            ? profitability.reduce(
                (a, b) =>
                    a.profit > b.profit
                        ? a
                        : b
            )
            : null;

    return (

        <div
            style={{
                display: "flex",
                gap: "20px",
                marginBottom: "30px",
                flexWrap: "wrap"
            }}
        >

            <div
                style={{
                    padding: "20px",
                    border: "1px solid #ddd",
                    borderRadius: "12px",
                    minWidth: "280px"
                }}
            >
                <h3>
                    🏆 Highest Demand Route
                </h3>

                {highestDemand && (
                    <>
                        <p>
                            Route:
                            {highestDemand.route}
                        </p>

                        <p>
                            Demand:
                            {
                                highestDemand.forecast_demand
                            }
                        </p>
                    </>
                )}

            </div>

            <div
                style={{
                    padding: "20px",
                    border: "1px solid #ddd",
                    borderRadius: "12px",
                    minWidth: "280px"
                }}
            >
                <h3>
                    💰 Most Profitable Route
                </h3>

                {highestProfit && (
                    <>
                        <p>
                            Route:
                            {highestProfit.route}
                        </p>

                        <p>
                            Profit:
                            ₹
                            {
                                Number(
                                    highestProfit.profit
                                ).toLocaleString()
                            }
                        </p>
                    </>
                )}

            </div>

        </div>

    );
}

export default RouteRanking;