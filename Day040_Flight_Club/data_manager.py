import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_API = os.getenv('SHEETY_API')
SHEETY_USERS = os.getenv('SHEETY_USERS')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=SHEETY_API,
            headers = {
                "Authorization": SHEETY_TOKEN
            }
        )
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
                url=f"{SHEETY_API}/{city['id']}",
                json=new_data,
                headers = {
                    "Authorization": SHEETY_TOKEN
                }
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(
            url=SHEETY_USERS,
            headers = {
                "Authorization": SHEETY_TOKEN
            }
        )
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
