from pprint import pprint
import requests
import os

##########################################################
# Sheety Sheet Management
# APIs, Constants and Endpoints
##########################################################
USERNAME = os.environ.get("USERNAME")
PROJECT_NAME = os.environ.get("PROJECT_NAME")
SHEET_NAME = os.environ.get("SHEET_NAME")
HEADER_AUTH = {
    "Authorization": f"Bearer {os.environ.get('HEADER_AUTH')}"
}
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
##########################################################

# SHEETY_PRICES_ENDPOINT = YOUR SHEETY PRICES ENDPOINT


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADER_AUTH)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, headers=HEADER_AUTH
            )
            print(response.text)
