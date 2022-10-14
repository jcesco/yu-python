import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

# References
# 1. ISS API Documentation: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# 2. HTTP Status Codes: https://www.webfx.com/web-development/glossary/http-status-codes/
# 3. Pypi Requests Project Page: https://pypi.org/project/requests/
