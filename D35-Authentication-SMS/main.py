import requests

# Location Coordinates
MY_LAT = 26.589180
MY_LON = -80.172798

# OpenWeather API
# OneCall2.5 has been replaced with OneCall3.0 which requires CC info, will suffice with Current Weather Data
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
MY_KEY = "1a65456994c29f1bf8e3d52af181ae71"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": MY_KEY,
}

# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LON}&appid={MY_KEY}")
# print(response.json())

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
