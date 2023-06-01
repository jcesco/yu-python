import requests

# Location Coordinates
MY_LAT = 26.589180
MY_LONG = -80.172798

# OpenWeather API
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_KEY = "f404737043415fdcbdfe549cd4d9200f"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_KEY,
}

# response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&appid={MY_KEY}")
# print(response)

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)

# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=London&appid=f404737043415fdcbdfe549cd4d9200f")
# print(response.json())