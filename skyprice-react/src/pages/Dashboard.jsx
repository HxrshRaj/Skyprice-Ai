import { useEffect, useState } from "react";
import API from "../services/api";

function Dashboard() {

    const [forecasts, setForecasts] = useState([]);
    const [pricing, setPricing] = useState([]);
    const [profitability, setProfitability] = useState([]);
    const [optimization, setOptimization] = useState([]);
    const [network, setNetwork] = useState([]);

    useEffect(() => {

        API.get("/forecast")
            .then((res) => {
                setForecasts(res.data);
            });

        API.get("/pricing")
            .then((res) => {
                setPricing(res.data);
            });

        API.get("/profitability")
            .then((res) => {
                setProfitability(res.data);
            });

        API.get("/optimization")
            .then((res) => {
                setOptimization(res.data);
            });

        API.get("/network")
            .then((res) => {
                setNetwork(res.data);
            });

    }, []);

    const totalRevenue = profitability.reduce(
        (sum, item) => sum + Number(item.revenue || 0),
        0
    );

    const totalProfit = profitability.reduce(
        (sum, item) => sum + Number(item.profit || 0),
        0
    );

    const totalDemand = forecasts.reduce(
        (sum, item) => sum + Number(item.forecast_demand || 0),
        0
    );

    return (
        <div style={{ padding: "20px" }}>

            <h1>✈️ SkyPrice AI</h1>

            <h3>
                Airline Revenue Management Platform
            </h3>

            {/* KPI CARDS */}

            <div
                style={{
                    display: "flex",
                    gap: "20px",
                    marginTop: "20px",
                    marginBottom: "30px",
                    flexWrap: "wrap"
                }}
            >

                <div style={{
                    border: "1px solid #ddd",
                    padding: "20px",
                    minWidth: "220px"
                }}>
                    <h4>Total Forecast Demand</h4>
                    <h2>{totalDemand}</h2>
                </div>

                <div style={{
                    border: "1px solid #ddd",
                    padding: "20px",
                    minWidth: "220px"
                }}>
                    <h4>Total Revenue</h4>
                    <h2>
                        ₹{totalRevenue.toLocaleString()}
                    </h2>
                </div>

                <div style={{
                    border: "1px solid #ddd",
                    padding: "20px",
                    minWidth: "220px"
                }}>
                    <h4>Total Profit</h4>
                    <h2>
                        ₹{totalProfit.toLocaleString()}
                    </h2>
                </div>

                <div style={{
                    border: "1px solid #ddd",
                    padding: "20px",
                    minWidth: "220px"
                }}>
                    <h4>Routes Covered</h4>
                    <h2>{forecasts.length}</h2>
                </div>

            </div>

            {/* FORECASTS */}

            <h2>📈 Demand Forecasts</h2>

            <table border="1" cellPadding="10">
                <thead>
                    <tr>
                        <th>Route</th>
                        <th>Forecast Demand</th>
                    </tr>
                </thead>

                <tbody>
                    {forecasts.map((item, index) => (
                        <tr key={index}>
                            <td>{item.route}</td>
                            <td>{item.forecast_demand}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <br />

            {/* PRICING */}

            <h2>💲 Dynamic Pricing</h2>

            <table border="1" cellPadding="10">
                <thead>
                    <tr>
                        <th>Route</th>
                        <th>Current Price</th>
                        <th>Recommended Price</th>
                        <th>Price Change %</th>
                    </tr>
                </thead>

                <tbody>
                    {pricing.map((item, index) => (
                        <tr key={index}>
                            <td>{item.route}</td>
                            <td>{item.current_price}</td>
                            <td>{item.recommended_price}</td>
                            <td>{item.price_change_percent}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <br />

            {/* PROFITABILITY */}

            <h2>💰 Route Profitability</h2>

            <table border="1" cellPadding="10">
                <thead>
                    <tr>
                        <th>Route</th>
                        <th>Revenue</th>
                        <th>Profit</th>
                        <th>Margin %</th>
                    </tr>
                </thead>

                <tbody>
                    {profitability.map((item, index) => (
                        <tr key={index}>
                            <td>{item.route}</td>
                            <td>{item.revenue}</td>
                            <td>{item.profit}</td>
                            <td>{item.profit_margin_percent}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <br />

            {/* OPTIMIZATION */}

            <h2>🎯 Revenue Optimization</h2>

            <table border="1" cellPadding="10">
                <thead>
                    <tr>
                        <th>Route</th>
                        <th>Forecast Demand</th>
                        <th>Premium Protection</th>
                    </tr>
                </thead>

                <tbody>
                    {optimization.map((item, index) => (
                        <tr key={index}>
                            <td>{item.route}</td>
                            <td>{item.forecast_demand}</td>
                            <td>{item.premium_protection}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <br />

            {/* NETWORK */}

            <h2>🌐 Network Optimization</h2>

            <table border="1" cellPadding="10">
                <thead>
                    <tr>
                        <th>Route</th>
                        <th>Allocated Seats</th>
                        <th>Optimized Revenue</th>
                    </tr>
                </thead>

                <tbody>
                    {network.map((item, index) => (
                        <tr key={index}>
                            <td>{item.route}</td>
                            <td>{item.allocated_seats}</td>
                            <td>{item.optimized_revenue}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

        </div>
    );
}

export default Dashboard;