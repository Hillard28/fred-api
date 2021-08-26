'''
Early work in progress. FRED data keys can be found on the website; to find, visit:
https://fred.stlouisfed.org/
'''
# For loading data if you want to skip all the previous inputs
import requests

class Fred(object):
    
    root_url = 'https://api.stlouisfed.org/fred/'
    
    def __init__(self, api_key=None):
        self.api_key = None
        if api_key is not None:
            self.api_key = str(api_key)
        if self.api_key is None:
            raise ValueError('Please enter an API key')
        elif len(self.api_key) < 32:
            raise ValueError('Please enter a valid API key')
    
    def get_observations(self,
                         series_id,
                         observation_start,
                         observation_end,
                         **kwargs):
        
        url = (self.root_url
               + 'series/observations?series_id=' + series_id
               + '&observation_start=' + observation_start
               + '&observation_end=' + observation_end
        )
        
        if kwargs.keys():
            for arg, val in kwargs.items():
                url += '&' + str(arg) + '=' + str(val)
        
        url += ('&api_key=' + self.api_key
               + '&file_type=json'
        )
        
        request = requests.get(url).json()
        
        obs_dates = []
        obs_values = []
        
        for item in request['observations']:
            obs_dates.append(item['date'])
            obs_values.append(item['value'])
        
        data = {
            'Date': obs_dates,
            series_id: obs_values,
        }
        
        return data










