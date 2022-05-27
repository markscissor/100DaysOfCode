from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
# notification_manager.smsTest()
# print(sheet_data)

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if not flight == None:
        notif_msg = f"Low price alert! Only £{flight.price} to fly " \
            f"from {flight.origin_city}-{flight.origin_airport} " \
            f"to {flight.destination_city}-{flight.destination_airport}, " \
            f"from {flight.out_date} to {flight.return_date}."
        notification_manager.smsSend(notif_msg)