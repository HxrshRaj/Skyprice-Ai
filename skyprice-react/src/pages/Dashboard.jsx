import RouteRanking from "../components/RouteRanking";
import InsightsPanel from "../components/InsightsPanel";
import { useEffect, useState } from "react";
import API from "../services/api";
import Sidebar from "../components/Sidebar";
import NetworkChart from "../components/NetworkChart";

import KPICard from "../components/KPICard";
import DemandChart from "../components/DemandChart";
import ProfitChart from "../components/ProfitChart";

function Dashboard() {

    const [forecasts, setForecasts] = useState([]);
    const [pricing, setPricing] = useState([]);
    const [profitability, setProfitability] = useState([]);
    const [optimization, setOptimization] = useState([]);
    const [network, setNetwork] = useState([]);
    const [elasticity, setElasticity] = useState([]);
    const [competitor, setCompetitor] = useState([]);
    const [activeSection, setActiveSection] = useState("Overview");

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
            API.get("/elasticity")
    .then((res) => {
        setElasticity(res.data);
    });

API.get("/competitor")
    .then((res) => {
        setCompetitor(res.data);
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

    <div
        style={{
            display: "flex"
        }}
    >

        <Sidebar
            activeSection={activeSection}
            setActiveSection={setActiveSection}
        />

        <div
            style={{
                flex: 1,
                padding: "20px"
            }}
        >

            {activeSection === "Overview" && (
<>

<h1>✈️ SkyPrice AI</h1>

<h3>
    Airline Revenue Management Platform
</h3>

<div
    style={{
        display: "flex",
        gap: "20px",
        marginTop: "20px",
        marginBottom: "30px",
        flexWrap: "wrap"
    }}
>

    <KPICard
        title="Total Forecast Demand"
        value={totalDemand}
    />

    <KPICard
        title="Total Revenue"
        value={`₹${totalRevenue.toLocaleString()}`}
    />

    <KPICard
        title="Total Profit"
        value={`₹${totalProfit.toLocaleString()}`}
    />

    <KPICard
        title="Routes Covered"
        value={forecasts.length}
    />

</div>

<h2>📊 Demand Forecast Analytics</h2>

<DemandChart
    data={forecasts}
/>

<br />

<h2>💰 Profit Analytics</h2>

<ProfitChart
    data={profitability}
/>

<br />

</>
)}
<RouteRanking
    forecasts={forecasts}
    profitability={profitability}
/>

<br />

            {/* FORECASTING */}

{activeSection === "Forecasting" && (
<>

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

</>
)}

{/* PRICING */}

{activeSection === "Pricing" && (
<>

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

</>
)}

{/* PROFITABILITY */}

{activeSection === "Profitability" && (
<>

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

</>
)}

{/* OPTIMIZATION */}

{activeSection === "Optimization" && (
<>
<h2>🌐 Network Revenue Analytics</h2>

<NetworkChart
    data={network}
/>

<br />

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

<br />

</>
)}

{/* ELASTICITY */}

{activeSection === "Elasticity" && (
<>

<h2>📊 Price Elasticity Analysis</h2>

<table border="1" cellPadding="10">

    <thead>
        <tr>
            <th>Route</th>
            <th>Elasticity Score</th>
            <th>Pricing Strategy</th>
        </tr>
    </thead>

    <tbody>

        {elasticity.map((item, index) => (

            <tr key={index}>

                <td>{item.route}</td>

                <td>
                    {item.elasticity_score}
                </td>

                <td>
                    {item.pricing_strategy}
                </td>

            </tr>

        ))}

    </tbody>

</table>

<br />

</>
)}

{/* COMPETITORS */}

{activeSection === "Competitors" && (
<>

<h2>🏁 Competitor Pricing Intelligence</h2>

<table border="1" cellPadding="10">

    <thead>
        <tr>
            <th>Route</th>
            <th>Our Price</th>
            <th>Competitor Price</th>
            <th>Recommendation</th>
        </tr>
    </thead>

    <tbody>

        {competitor.map((item, index) => (

            <tr key={index}>

                <td>{item.route}</td>

                <td>{item.our_price}</td>

                <td>{item.competitor_price}</td>

                <td>{item.recommendation}</td>

            </tr>

        ))}

    </tbody>

</table>

<br />

</>
)}

{/* INSIGHTS */}

{activeSection === "Overview" && (
<>
    <InsightsPanel />
</>
)}

        </div>

    </div>

);
}

export default Dashboard;