import requests
from datetime import datetime
import smtplib
import pytz
import time
from secret_codes import MY_EMAIL, MY_PASSWORD


MY_LAT = 25.204849  # Your latitude
MY_LONG = 55.270782  # Your longitude


def check_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print("ISS Location: ", iss_latitude, iss_longitude)

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

    local_time = datetime.now(pytz.timezone('Asia/Dubai'))
    hour_now = local_time.hour

    cond_1 = hour_now <= sunrise or hour_now >= sunset
    cond_2 = abs(MY_LAT - iss_latitude) <= 5
    cond_3 = abs(MY_LONG - iss_longitude) <= 5

    if cond_1 and cond_2 and cond_3:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="mcnmunoz@gmail.com",
                msg=f"Subject:Look up👆\n\nThe ISS is above you in the sky."
            )
            print("Email sent.")


while True:
    check_iss()
    time.sleep(10)
