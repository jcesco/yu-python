# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the 
# program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from datetime import datetime
from datetime import timedelta
from notification_manager import NotificationManager

##########################################################
# Class Instances
##########################################################
flight_search = FlightSearch()
data_manager = DataManager()
flight_data = FlightData()
notification_manager = NotificationManager()

##########################################################
# Get Data From Sheety
##########################################################

sheet_data = data_manager.get_destination_data()

# Fill IATA codes if empty
for destination in sheet_data["prices"]:
    if destination["iataCode"] == "":
        destination["iataCode"] = flight_search.iata_code_lookup(destination['city'])
        data_manager.update_destination_code(destination)


##########################################################
# Get Prices from Kiwi/Tequila and send text if applicable
##########################################################

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_months = (datetime.now() + timedelta(days=6 * 30)).strftime("%d/%m/%Y")

for destination in sheet_data["prices"]:

    current_price = flight_search.find_price(origin_IATA_code='LON', destination_IATA_code=destination['iataCode'], 
                                             from_date=tomorrow, to_date=six_months)

    if current_price['Price'] <= destination['lowestPrice']:
        print("Bullseye!\n")
        print(f"Flight to {destination['city']}")
        print(f"desired price: {destination['lowestPrice']}")
        print(f"current price: {current_price['Price']}")
        notification_manager.send_alert(current_price)
