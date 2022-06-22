import requests
from bs4 import BeautifulSoup
import re
from notification import NotificationManager


notification_manager = NotificationManager()
URL = 'https://www.amazon.com/EVGA-GeForce-12G-P5-3657-KR-Dual-Fan-Backplate/dp/B08WM28PVH/ref=sr_1_20?qid=1655874173&rnid=16225007011&s=computers-intl-ship&sr=1-20'
# TARGET_PRICE = 390
TARGET_PRICE = 430

r = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
)

soup = BeautifulSoup(r.text, 'lxml')

item_price_text = soup.select_one(".a-offscreen").getText()

item_price = float(re.sub(r'[^0-9.]', '', item_price_text))

print(item_price)

item_name = soup.select_one("#productTitle").getText().strip()

print(item_name)

if item_price < TARGET_PRICE:
    SUBJECT = "Amazon Price Alert!"
    MESSAGE = f"{item_name} is now at ${item_price}!"
    notification_manager.send_emails(
        ['corroro_001@yahoo.com'],
        SUBJECT,
        MESSAGE,
        URL
    )
