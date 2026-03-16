import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("formatted_output.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

sales_by_date = df.groupby("Date", as_index=False)["Sales"].sum()
sales_by_date = sales_by_date.sort_values("Date")

fig = px.line(
    sales_by_date,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)