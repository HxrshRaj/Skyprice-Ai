import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer
} from "recharts";

function NetworkChart({ data }) {

    return (

        <ResponsiveContainer
            width="100%"
            height={400}
        >

            <BarChart data={data}>

                <XAxis
                    dataKey="route"
                />

                <YAxis />

                <Tooltip />

                <Bar
                    dataKey="optimized_revenue"
                />

            </BarChart>

        </ResponsiveContainer>

    );
}

export default NetworkChart;