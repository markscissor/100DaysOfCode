import smtplib
import os
from dotenv import load_dotenv


load_dotenv()


class NotificationManager:

    def __init__(self):
        self.smtp = os.getenv('EMAIL_PROVIDER_SMTP_ADDRESS')
        self.email = os.getenv('MY_EMAIL')
        self.pwd = os.getenv('MY_PASSWORD')
        self.port = os.getenv('SMTP_PORT')
        self.from_email = os.getenv('FROM_EMAIL')

    def send_emails(self, emails, subject, message, url):
        with smtplib.SMTP(self.smtp, self.port) as connection:
            # connection.set_debuglevel(2)
            connection.ehlo()
            connection.starttls()
            connection.ehlo()
            connection.login(self.email, self.pwd)
            for email in emails:
                connection.sendmail(
                    from_addr=self.from_email,
                    to_addrs=email,
                    msg=f"Subject:{subject}\n\n{message}\n{url}".encode(
                        'utf-8')
                )
            print('email sent')
