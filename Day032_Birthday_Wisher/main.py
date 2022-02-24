import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "USER@gmail.com"
MY_PASSWORD = "PASSWORD"


data = pd.read_csv("birthdays.csv")
birthday_list = data.to_dict(orient='records')

now = dt.datetime.now()
month = now.month
day = now.day

email_list = []
for person in birthday_list:
    if person['month'] == month and person['day'] == day:
        email_list.append(person)

for person in email_list:
    letter_num = random.randint(1, 3)
    letter_file = f"letter_templates/letter_{letter_num}.txt"

    with open(letter_file, "r") as temp:
        msg = temp.readlines()
    dear_msg = msg[0].split()
    dear_msg[1] = f"{person['name']},\n"
    msg[0] = " ".join(dear_msg)
    email_body = "".join(msg)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday {person['name']}\n\n{email_body}"
        )
        print("Email sent.")
