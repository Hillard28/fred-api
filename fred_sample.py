"""
Sample commands
"""
import pandas as pd
import matplotlib.pyplot as plt

# Create FRED object
fred = Fred("!!!USE REQUESTED FRED API KEY!!!")

# Search FRED for effective federal funds rate time series
search = fred.search_series(search_text="effective federal funds rate")

# Create FRED dataset
data = fred.get_observations(
    series_id="DFF",
    observation_start="1990-01-01",
    observation_end="2020-10-01",
    frequency="q",
    aggregation_method="eop",
)

# Create dataframe
dff = pd.DataFrame(data)
dff["Date"] = pd.to_datetime(dff["Date"])
dff["DFF"] = pd.to_numeric(dff["DFF"], errors="coerce")

data = fred.get_observations(
    series_id="UNRATE",
    observation_start="1990-01-01",
    observation_end="2020-10-01",
    frequency="q",
    aggregation_method="eop",
)

# Create dataframe
unrate = pd.DataFrame(data)
unrate["Date"] = pd.to_datetime(unrate["Date"])
unrate["UNRATE"] = pd.to_numeric(unrate["UNRATE"], errors="coerce")

# Plot data
plt.plot(dff["Date"], dff["DFF"], label="EFFR")
plt.plot(unrate["Date"], unrate["UNRATE"], label="Unemployment")
plt.title(
    "Effective Federal Funds Rate vs. Unemployment",
    fontname="Times New Roman",
    fontsize=14,
)
plt.xlabel(None, fontname="Times New Roman", fontsize=12)
plt.ylabel("Rate (%)", fontname="Times New Roman", fontsize=12)

plt.xticks(fontname="Times New Roman", fontsize=10, rotation=45)
plt.yticks(fontname="Times New Roman", fontsize=10)

plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)

plt.margins(x=0)

plt.legend(
    bbox_to_anchor=(0.5, -0.2),
    loc="lower center",
    borderaxespad=0,
    ncol=2,
    fontsize=9,
    frameon=False,
)

plt.show()
