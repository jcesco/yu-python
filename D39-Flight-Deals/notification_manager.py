import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details
    def __init__(self):
        self.account_sid = "AC58224f128a10772cb2d1591eba220c35"
        self.auth_token = os.environ.get("AUTH_TOKEN")

    def send_alert(self, flight_deal):
        # This method formats and sends the flight deal info
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body= f"Low price alert! Only £{flight_deal['Price']} to fly from {flight_deal['Departure City Name']}-"
                  f"{flight_deal['Departure Airport IATA Code']} to {flight_deal['Arrival City Name']}-"
                  f"{flight_deal['Arrival Airport IATA Code']}, from {flight_deal['Outbound Date']} to "
                  f"{flight_deal['Inbound Date']}",
            from_='+18885944415',
            to='+17862901867'
        )
        print(message.status)