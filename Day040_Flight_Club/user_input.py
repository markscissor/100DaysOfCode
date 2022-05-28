import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_API = os.getenv('SHEETY_USERS')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

class UserInput():

    def ask_details(self):
        print("Welcome to Corroro's Flight Club.\n" \
            "We find the best deals and email you.")
        first_name = input("What is your first name?\n").title()
        last_name = input("What is your last name?\n").title()
        email = input("What is your email?\n")
        email2 = input("Type your email again.\n")

        if first_name == "" or last_name == "" or email == "":
            print("Missing input details. Try again.\n\n")
            self.ask_details()
        elif not email == email2:
            print("Email did not match. Try again.\n\n")
            self.ask_details()
        else:
            print("Saving info:\n" \
                f"First name: {first_name}\n" \
                f"Last name: {last_name}\n" \
                f"Email: {email}\n" \
                "Please wait.\n"
            )
            headers = {
                "Authorization": SHEETY_TOKEN
            }
            query = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email
                }
            }
            response = requests.post(url=SHEETY_API, headers=headers, json=query)
            print(response.json())

user = UserInput()
user.ask_details()
