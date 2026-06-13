function Sidebar({ activeSection, setActiveSection }) {

    const menuItems = [
        "Overview",
        "Forecasting",
        "Pricing",
        "Profitability",
        "Optimization",
        "Elasticity",
        "Competitors"
    ];

    return (

        <div
            style={{
                width: "250px",
                minHeight: "100vh",
                background: "#111827",
                color: "white",
                padding: "20px"
            }}
        >

            <h2>✈️ SkyPrice AI</h2>

            <hr />

            {menuItems.map((item) => (

                <div
                    key={item}
                    onClick={() =>
                        setActiveSection(item)
                    }
                    style={{
                        padding: "12px",
                        marginTop: "10px",
                        cursor: "pointer",
                        borderRadius: "8px",
                        background:
                            activeSection === item
                                ? "#2563EB"
                                : "transparent"
                    }}
                >
                    {item}
                </div>

            ))}

        </div>

    );
}

export default Sidebar;