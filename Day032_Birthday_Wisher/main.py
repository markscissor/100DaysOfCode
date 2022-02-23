import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "corroro001@gmail.com"
MY_PASSWORD = "pass1324"


# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

data = pd.read_csv("birthdays.csv")
birthday_list = data.to_dict(orient='records')

now = dt.datetime.now()
month = now.month
day = now.day
# print(month, day)

# Manual input of date
month = 2
day = 17
email_list = []
for person in birthday_list:
    if person['month'] == month and person['day'] == day:
        email_list.append(person)

for person in email_list:
    letter_num = random.randint(1, 3)
    letter_file = f"letter_templates/letter_{letter_num}.txt"

    with open(letter_file, "r") as temp:
        msg = temp.readlines()

    msg[0] = f'Dear {person["name"]},\n'
    email_body = "".join(msg)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="corroro_001@yahoo.com",
            msg=f"Subject:Happy Birthday {person['name']}\n\n{email_body}"
        )
        print("Email sent.")
