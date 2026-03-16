import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("formatted_output.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Region"] = df["Region"].astype(str).str.lower().str.strip()

app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f4f6f8",
        "minHeight": "100vh",
        "padding": "30px"
    },
    children=[
        html.Div(
            style={
                "maxWidth": "1000px",
                "margin": "0 auto",
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "16px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.1)"
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Visualiser",
                    style={
                        "textAlign": "center",
                        "marginBottom": "20px"
                    }
                ),

                html.Label(
                    "Filter by Region:",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "18px",
                        "display": "block",
                        "marginBottom": "10px"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginBottom": "25px"},
                    labelStyle={
                        "marginRight": "20px",
                        "fontSize": "16px",
                        "cursor": "pointer"
                    }
                ),

                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["Region"] == selected_region]

    sales_by_date = (
        filtered_df.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
    )

    fig = px.line(
        sales_by_date,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time - {selected_region.title()}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)