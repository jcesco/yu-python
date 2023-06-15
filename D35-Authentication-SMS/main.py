import requests
import os
from twilio.rest import Client

# Virtual Environments/Environment Keys
# https://codingnomads.co/blog/python-environment-variables-set-a-variable-in-bash/
# https://intellij-support.jetbrains.com/hc/en-us/community/posts/9865478654866-How-to-ACTUALLY-set-environment-variables-in-PyCharm-

# This worked
account_sid = "AC58224f128a10772cb2d1591eba220c35"
auth_token = os.environ.get("AUTH_TOKEN")

# Location Coordinates
MY_LAT = 26.589180
MY_LON = -80.172798

# OpenWeather API
# OneCall2.5 has been replaced with OneCall3.0 which requires CC info, will suffice with Current Weather Data
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_KEY = os.environ.get("OWM_API_KEY")
# 1a65456994c29f1bf8e3d52af181ae71
UNITS = "imperial"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": MY_KEY,
    "units": UNITS,
}

# Obtain weather data from OWM
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Tester code
# print(f"{OWM_Endpoint}?lat={MY_LAT}&lon={MY_LON}&appID={MY_KEY}&units={UNITS}")
# print(weather_data['list'][0]["weather"][0]["id"])

# Store weather data for the next 12 hours
# Every data block covers 3 hours of data so only 4 datapoints will be stored
weather_code = []
will_rain = False

for i in range(4):
    weather_code.append(weather_data['list'][i]["weather"][0]["id"])
    if weather_code[i] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Bring an umbrella, it gon rain ☔",
            from_='+18885944415',
            to='+17862901867'
        )
    print(message.status)
