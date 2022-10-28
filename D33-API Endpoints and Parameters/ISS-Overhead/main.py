import requests
from datetime import datetime
import smtplib

MY_EMAIL = "GeeTester696@gmail.com"
MY_PASSWORD = "wdbijimadlgmkehp"
LETTERS = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]

MY_LAT = 26.589180
MY_LONG = -80.172800

def iss_nearby():
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_latitude - MY_LONG < 5):
        return True

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = str(datetime.now())
time_rn = int(time_now.split(" ")[1].split(":")[0])


if iss_nearby() and (time_rn > sunset or time_rn < sunrise):
    print("overhead")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: ISS OVERHEAD!\n\nGo look outside!")


