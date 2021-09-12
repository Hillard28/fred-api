"""
Sample commands
"""
# Create FRED object
fred = Fred("c3b3e00ffe43945cf9995e4c00a4d1aa")

# Search FRED for effective federal funds rate time series
search = fred.search_series(search_text = 'effective federal funds rate')

# Create FRED dataset
data = fred.get_observations(
    series_id = "DFF",
    observation_start = "1990-01-01",
    observation_end = "2020-10-01",
    frequency = "q",
    aggregation_method = "eop"
)

# Create dataframe
dff = pd.DataFrame(data)
dff["Date"] = pd.to_datetime(data["Date"])
dff["DFF"] = pd.to_numeric(dff["DFF"], errors = "coerce")


