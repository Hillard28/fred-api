"""
Early work in progress.
FRED API keys can be obtained from the website; to find, visit:
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
        """Set key used to access FRED API"""
        self.api_key = None
        if api_key is not None:
            self.api_key = str(api_key)
        if self.api_key is None:
            raise ValueError("Please enter an API key")
        elif len(self.api_key) < 32:
            raise ValueError("Please enter a valid API key")

    def search_series(self, search_text, search_type="full_text", limit=1000, **kwargs):
        """
        Search for series maintained by FRED using keywords

        Parameters
        ----------
        search_text: str
            Text used to search FRED (required)
        search_type: str
            Type of search performed (optional, default: "full_text")
        limit: int
            Maximum number of results (optional, default: 1000)
        order_by: str
            Orders results by attribute (optional, default: "search_rank")
        """
        url = (
            self.root_url
            + "series/search?search_text="
            + search_text.replace(" ", "+")
            + "&search_type="
            + search_type
            + "&limit="
            + str(limit)
        )

        if kwargs.keys():
            for arg, val in kwargs.items():
                url += "&" + str(arg) + "=" + str(val)
        url += "&api_key=" + self.api_key + "&file_type=json"

        request = requests.get(url).json()

        return request

    def get_series_info(self, series_id):
        """Get info on specific FRED series"""
        url = self.root_url + "series?series_id=" + series_id

        url += "&api_key=" + self.api_key + "&file_type=json"

        request = requests.get(url).json()

        return request

    def get_observations(
        self,
        series_id,
        observation_start="1776-07-04",
        observation_end="9999-12-31",
        **kwargs
    ):
        """
        Get series maintained by FRED using ID

        Parameters
        ----------
        series_id: str
            FRED series ID (required)
        observation_start: datetime or datetime-like str
            Earliest observation date (optional, default: "1776-07-04")
        observation_end: datetime or datetime-like str
            Latest observation date (optional, default: "9999-12-31")
            WILL NEED TO BE UPDATED FOR THE 101ST CENTURY
        units: str
            Data value transformations (optional, default: "lin")
        frequency: str
            Frequency of observations (optional, default: None)
        aggregation_method: str
            Data aggregation if frequency set (optional, default: "avg")

        Returns
        -------
        Dates: list(str)
        Series ID: str
        Series values: list(str)
        """
        url = (
            self.root_url
            + "series/observations?series_id="
            + series_id
            + "&observation_start="
            + observation_start
            + "&observation_end="
            + observation_end
        )

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
