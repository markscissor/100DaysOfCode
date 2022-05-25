import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


# NUTRITIONIX
API_KEY = os.getenv('API_KEY')
APP_ID = os.getenv('APP_ID')
EXERCISE_ENDPOINT = os.getenv('EXERCISE_ENDPOINT')

# SHEETY
SHEETY_POST = os.getenv('SHEETY_POST')
SHEETY_GET = os.getenv('SHEETY_GET')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_data = {
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 170,
    "age": 30,
    "query": input("What did you do? ")
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_data, headers=headers)
exer_response = response.json()
# print(exer_response['exercises'])

today = datetime.now()
t_date = today.strftime("%d/%m/%Y")
t_time = today.strftime("%X")
print(t_date, t_time)


for item in exer_response['exercises']:
    headers = {
        "Authorization": SHEETY_TOKEN
    }   
    sheety_data = {
        "workout": {
            "date": t_date,
            "time": t_time,
            "exercise": item['name'].title(),
            "duration": "{0:.0f}".format(item['duration_min']),
            "calories": "{0:.0f}".format(item['nf_calories'])
        }
    }
    print(sheety_data)
    response = requests.post(url=SHEETY_POST, json=sheety_data, headers=headers)
    print(response.status_code)