import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer
} from "recharts";

function DemandChart({ data }) {

    return (

        <ResponsiveContainer
            width="100%"
            height={400}
        >

            <BarChart data={data}>

                <XAxis dataKey="route" />

                <YAxis />

                <Tooltip />

                <Bar
                    dataKey="forecast_demand"
                />

            </BarChart>

        </ResponsiveContainer>

    );
}

export default DemandChart;