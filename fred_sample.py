'''
Sample commands
'''
# Create FRED object
fred = fred_api.Fred('!!!use Census API key here!!!')

# Create FRED dataset
data = fred.get_observations(
    series_id = 'DFF',
    observation_start = '1990-01-01',
    observation_end = '2020-10-01',
    frequency = 'q',
    aggregation_method = 'eop'
)

# Create dataframe
dff = pd.DataFrame(data)
dff['Date'] = pd.to_datetime(data['Date'])
dff['DFF'] = pd.to_numeric(dff['DFF'], errors = 'coerce')
