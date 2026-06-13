import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer
} from "recharts";

function ProfitChart({ data }) {

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
                    dataKey="profit"
                />

            </BarChart>

        </ResponsiveContainer>

    );
}

export default ProfitChart;