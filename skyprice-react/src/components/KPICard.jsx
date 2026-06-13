function KPICard({ title, value }) {

    return (

        <div
            style={{
    background: "white",
    borderRadius: "16px",
    padding: "24px",
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
    minWidth: "240px",
    transition: "0.3s"
}}
        >
            <h4>{title}</h4>

            <h2>{value}</h2>

        </div>

    );
}

export default KPICard;