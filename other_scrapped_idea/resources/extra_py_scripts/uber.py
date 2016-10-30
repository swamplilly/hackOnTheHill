import requests
# https://github.com/kennethreitz/requests/releases
import json
import math

with open('config.json') as f:
    config = json.load(f)

url = 'https://api.uber.com/v1/estimates/price'
parameters = {
    'server_token': 'PsKCCYj7acmk9o4yM8KncXBVsGvdo7LVQ7ZBoo_X',
    'start_latitude': 37.775818,
    'start_longitude': -122.418028,
    'end_latitude': 37.575818,
    'end_longitude': -122.428028,
}

response = requests.get(url, params=parameters)

data = response.json()
uberx=data['prices'][0]

hi=uberx['high_estimate']
low=uberx['low_estimate']

estimate=int(math.sqrt(hi*low))
estimate_str="$"+str(estimate)
