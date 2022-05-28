import smtplib
import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()
SMS_TO = os.getenv('SMS_TO')
SMS_FROM = os.getenv('SMS_FROM')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
EMAIL_PROVIDER_SMTP_ADDRESS = os.getenv('EMAIL_PROVIDER_SMTP_ADDRESS')
MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD')

class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, msgText):
        message = self.client.messages.create(
            body=msgText,
            from_=SMS_FROM,
            to=SMS_TO
        )

        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )