import requests
import os
from twilio.rest import Client

account_sid = os.environ['AC5632086aff04f94936e20bb928b29d35']
auth_token = os.environ['e20ed599a77c06710ddce47fd8dfe87b']

api_key = '5502ba3082ad1af6603ce80e3379776d'
MY_LAT = '40.615639'
MY_LONG = '-73.755959'
url = 'https://api.openweathermap.org/data/2.5/forecast'
params = {'lat': MY_LAT,
          'lon': MY_LONG,
          'appid': api_key,
          'cnt': 4}

response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring umbrella",
        from_='+18557252984',
        to='+5164390176'
    )
    print(message.status)