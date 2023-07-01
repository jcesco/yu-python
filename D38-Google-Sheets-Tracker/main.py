import requests
import os
from datetime import datetime

# Nutritionix Constants
APP_ID = os.environ.get("APP_ID") # "d44c3ebd"
API_KEY = os.environ.get("API_KEY") # "f43f5dad03e66736c83628457ce2642c"

# Sheety Constants
USERNAME = os.environ.get("USERNAME") #"f4f24be2cdc2f5b9c827a12010051dea"
PROJECT_NAME = os.environ.get("PROJECT_NAME") #"myWorkouts"
SHEET_NAME = os.environ.get("SHEET_NAME") #"workouts"
HEADER_AUTH = {
    "Authorization": f"Bearer {os.environ.get('HEADER_AUTH')}" #fw906!#N71n0"
}

# Nutritionix User Info
GENDER = "female"
WEIGHT_KG = "70"
HEIGHT_CM = "165"
AGE = "24"

# Nutritionix and Sheety endpoints
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

# Nutrixionix header
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
# Exercise params
exercise_parameters = {
    "query": input("What workout did you do today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Get data from Nutritionix
exercise_response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
exercise_data = exercise_response.json()

# Post data to Sheet via Sheety
today_date = datetime.now().strftime("%d%m%Y")
time_now = datetime.now().strftime("%X")

for exercise in exercise_data['exercises']:
    new_row = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=new_row, headers=HEADER_AUTH)
    print(sheety_response.text)

# Environment variables reference
# https://www.geeksforgeeks.org/python-os-environ-object/#