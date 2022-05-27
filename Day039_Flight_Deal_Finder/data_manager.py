import requests
import os
from dotenv import load_dotenv

load_dotenv()

# SHEETY_PRICES_ENDPOINT = "YOUR ENDPOINT HERE"
SHEETY_API = os.environ['SHEETY_API']
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(
            url=SHEETY_API,
            headers = {
                "Authorization": SHEETY_TOKEN
            }
        )
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
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
