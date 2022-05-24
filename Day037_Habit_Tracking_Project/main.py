import requests
from datetime import datetime

USERNAME = "corroro"
TOKEN = "SidX%Xnuge6?EZx"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

entry_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

entry_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2.82",
}

# response = requests.post(url=entry_endpoint, json=entry_data, headers=headers)
# print(response.text)

date_to_edit = "20211207"

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{date_to_edit}"

update_data = {
    "quantity": "3.5"
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{date_to_edit}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)