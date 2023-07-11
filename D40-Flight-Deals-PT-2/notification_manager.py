import os
from twilio.rest import Client

TWILIO_SID = "AC58224f128a10772cb2d1591eba220c35"
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "18885944415"
TWILIO_VERIFIED_NUMBER = "17862901867"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.status)
