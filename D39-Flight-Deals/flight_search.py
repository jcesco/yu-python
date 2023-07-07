import requests
import os

##########################################################
# APIs, Constants and Endpoints
##########################################################
API_KEY = os.environ.get("API_KEY")
TEQUILA_QUERY_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
header = {
    'apikey': API_KEY
}


class FlightSearch:
    # This class interacts with Kiwi/Tequila API
    def __init__(self):
        self.name = ""

    def iata_code_lookup(self, city_name):
        # This method returns an airport IATA code for a given city name
        query_params = {
            'term': city_name,
            'location_types': 'airport',
            'limit': 1
        }

        query_response = requests.get(url=TEQUILA_QUERY_ENDPOINT, params=query_params, headers=header)
        query_data = query_response.json()
        iata_code = query_data['locations'][0]['code']
        return iata_code

    def find_price(self, origin_IATA_code, destination_IATA_code, from_date, to_date):
        # This method returns price and flight information given the above parameters and returns necessary info
        search_params = {
            'fly_from': origin_IATA_code,
            'fly_to': destination_IATA_code,
            'date_from': from_date,
            'date_to': to_date,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': 'GBP',
            'max_stopovers': 0,
            'sort': 'price',
            'limit': 1
        }

        search_response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=search_params, headers=header)
        search_data = search_response.json()

        flight_search_result = {
            'Price': search_data['data'][0]['price'],
            'Departure City Name': search_data['data'][0]['cityFrom'],
            'Departure Airport IATA Code': search_data['data'][0]['flyFrom'],
            'Arrival City Name': search_data['data'][0]['cityTo'],
            'Arrival Airport IATA Code': search_data['data'][0]['flyTo'],
            'Outbound Date': search_data['data'][0]['route'][0]['local_departure'].split("T")[0],
            'Inbound Date': search_data['data'][0]['route'][1]['local_arrival'].split("T")[0]
        }

        return flight_search_result
