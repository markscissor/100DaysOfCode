import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
SMS_TO = os.environ['SMS_TO']
SMS_FROM = os.environ['SMS_FROM']

class NotificationManager:

    def smsTest(self):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                            from_=SMS_FROM,
                            to=SMS_TO
                        )

        print(message.sid)

    def smsSend(self, msgText):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=msgText,
                            from_=SMS_FROM,
                            to=SMS_TO
                        )

        print(message.sid)