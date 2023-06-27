import requests
from datetime import datetime

USERNAME = "jcpixela"
TOKEN = "my_pixela_token_01"
GRAPH_ID = "graph1"

# Pixela new user endpoint
pixela_endpoint = "https://pixe.la/v1/users"

pixela_user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Generate a new user on Pixela
# pixela_response = requests.post(url=pixela_endpoint, json=pixela_user_params)
# print(pixela_response.text)

# Pixela graph endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Mile",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Creates new graph per parameters above
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# Pixela Post Pixel Engpoint
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you cycle today? "),
}

# Post (ie create) a pixel per the parameters above
pixel_post_response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)
print(pixel_post_response.text)

# Pixela update pixel

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_update_params = {
    'quantity': str(2)
}

# Updates an existing pixel with quantities per above
# pixel_update_response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(pixel_update_response.text)

delete_date = datetime(year=2023, month=6, day=26)

# Delete a pixel endpoint
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date.strftime('%Y%m%d')}"

# Deletes a pixel at date delete_date
# pixel_delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(pixel_delete_response.text)
