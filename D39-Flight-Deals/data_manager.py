import requests
import os

# This class is used to interface with google sheets via sheety

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
sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
##########################################################


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # This method pulls destination data from Google Sheet

        sheet_info = requests.get(url=sheety_endpoint, headers=HEADER_AUTH)
        self.destination_data = sheet_info.json()
        return self.destination_data

    def update_destination_code(self, new_row_info):
        # This method updates the Google Sheet with new IATA code in dictionary 'new_row_info'

        for destination in self.destination_data["prices"]:
            if new_row_info['city'] == destination['city']:
                self.destination_data['iataCode'] = new_row_info['iataCode']

                new_iata_code = {
                    "price": {
                        "iataCode": self.destination_data['iataCode']
                    }
                }

                row_endpoint = f"{sheety_endpoint}/{new_row_info['id']}"
                response = requests.put(url=row_endpoint, json=new_iata_code, headers=HEADER_AUTH)

