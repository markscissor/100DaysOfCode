import requests
import smtplib
from secret_codes import MY_EMAIL, MY_PASSWORD

# Weather
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "6047c726eaf69f7ab5e3eb826fd29467"


weather_params = {
    "lat": 36.8466,
    "lon": -76.2855,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}


def check_weather():
    response = requests.get(url=OWM_Endpoint, params=weather_params)
    response.raise_for_status()
    data = response.json()
    return data['hourly']


bring_umbrella = False
hourly_data = check_weather()
for hour in range(12):
    weather_id = hourly_data[hour]['weather'][0]['id']
    # print(weather_id)
    if weather_id < 700:
        bring_umbrella = True

if bring_umbrella:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="mcnmunoz@gmail.com",
            msg=f"Subject:Rain Check\n\nRemember to bring an umbrella."
        )
        print("Email sent.")
