"""
Early work in progress. FRED data keys can be found on the website; to find, visit:
https://fred.stlouisfed.org/

Observation arguments

Units
lin: Levels
chg: Change
ch1: Change from a year ago
pch: Percent change
pc1: Percent change from a year ago
pca: Compounded annual rate of change
cch: Continuously compounded rate of change
cca: Continuously compounded annual rate of change
log: Natural log

Frequency
d: Daily
w: Weekly
bw: Biweekly
m: Monthly
q: Quarterly
sa: Semiannual
a: Annual
wef: Weekly, ending Friday
weth: Weekly, ending Thursday
wew: Weekly, ending Wednesday
wetu: Weekly, ending Tuesday
wem: Weekly, ending Monday
wesu: Weekly, ending Sunday
wesa: Weekly, ending Saturday
bwew: Biweekly, ending Wednesday
bwem: Bieekly, ending Monday

Aggregation method
avg: Average
sum: Sum
eop: End of period
"""

# For loading data if you want to skip all the previous inputs
import requests


class Fred(object):

    root_url = "https://api.stlouisfed.org/fred/"

    def __init__(self, api_key=None):
        self.api_key = None
        if api_key is not None:
            self.api_key = str(api_key)
        if self.api_key is None:
            raise ValueError("Please enter an API key")
        elif len(self.api_key) < 32:
            raise ValueError("Please enter a valid API key")

    def search_series(self, search_text, **kwargs):

        url = (
            self.root_url + "series/search?search_text=" + search_text.replace(" ", "+")
        )

        if kwargs.keys():
            for arg, val in kwargs.items():
                url += "&" + str(arg) + "=" + str(val)
        url += "&api_key=" + self.api_key + "&file_type=json"

        request = requests.get(url).json()

        return request

    def get_observations(self, series_id, **kwargs):

        url = self.root_url + "series/observations?series_id=" + series_id

        if kwargs.keys():
            for arg, val in kwargs.items():
                url += "&" + str(arg) + "=" + str(val)
        url += "&api_key=" + self.api_key + "&file_type=json"

        request = requests.get(url).json()

        obs_dates = []
        obs_values = []

        for item in request["observations"]:
            obs_dates.append(item["date"])
            obs_values.append(item["value"])
        data = {
            "date": obs_dates,
            "id": series_id,
            "value": obs_values,
        }

        return data
