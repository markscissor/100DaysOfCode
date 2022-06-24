from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://www.python.org/"

events = []
dates = []

driver.get(URL)
# event = driver.find_elements(
#     by=By.XPATH,
#     value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a'
# )

event = driver.find_elements(
    by=By.CSS_SELECTOR,
    value='.event-widget li a'
)

for element in event:
    events.append(element.text)

# date = driver.find_elements(
#     by=By.XPATH,
#     value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time'
# )

date = driver.find_elements(
    by=By.CSS_SELECTOR,
    value='.event-widget time'
)

for element in date:

    date_str = element.get_attribute('datetime')
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
    dates.append(date_obj.strftime("%Y-%m-%d"))

final = {}

for k in range(len(dates)):
    final[k] = {'time': dates[k], 'name': events[k]}

print(final)

driver.quit()
