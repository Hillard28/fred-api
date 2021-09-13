"""
Sample commands
"""
import pandas as pd
import plotly.express as px

# Create FRED object
fred = Fred("!!!USE FRED API KEY!!!")

# Search FRED for effective federal funds rate time series
search = fred.search_series(search_text="treasury constant maturity rate")

# Create FRED datasets
data = fred.get_observations(
    series_id="DGS10",
    observation_start="1999-12-31",
    observation_end="2021-08-30",
    frequency="m",
    aggregation_method="eop",
)
dgs10 = pd.DataFrame(data)
dgs10["date"] = pd.to_datetime(dgs10["date"])
dgs10["value"] = pd.to_numeric(dgs10["value"], errors="coerce")

data = fred.get_observations(
    series_id="DGS3MO",
    observation_start="1999-12-31",
    observation_end="2021-08-30",
    frequency="m",
    aggregation_method="eop",
)
dgs3mo = pd.DataFrame(data)
dgs3mo["date"] = pd.to_datetime(dgs3mo["date"])
dgs3mo["value"] = pd.to_numeric(dgs3mo["value"], errors="coerce")

df = pd.concat([dgs10, dgs3mo])


# Plot data with Plotly
fig = px.line(
    df,
    x="date",
    y="value",
    color="id",
    title="United States Treasury Yields",
    # width=800,
    # height=600,
    labels={"date": "Date", "value": "Yield (%)", "id": "ID"},
    template="simple_white",
)

fig.update_layout(  # customize font and legend orientation & position
    font_family="Times New Roman",
    title=dict(xref="paper", x=0.5, xanchor="center", font=dict(size=32)),
    legend=dict(
        title=dict(text=None),
        font=dict(size=20),
        orientation="h",
        y=1.0,
        yanchor="bottom",
        x=0.5,
        xanchor="center",
    ),
    margin=dict(l=75, r=25, t=75, b=75),
)

fig.update_xaxes(
    title=dict(text=None, standoff=5, font=dict(size=24)),
    tickfont=dict(size=18),
    tickangle=-45,
    dtick="M24",
)

fig.update_yaxes(title=dict(standoff=5, font=dict(size=24)), tickfont=dict(size=18))

for id in fig.data:
    if id.name == "DGS10":
        id.name = "10-Year"
    elif id.name == "DGS3MO":
        id.name = "3-Month"
fig.show()

fig.write_image("united_states_treasury_yields_px.svg", width=800, height=600)
fig.write_html("united_states_treasury_yields_interactive.html", auto_open=True)
