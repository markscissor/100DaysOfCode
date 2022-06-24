import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://orteil.dashnet.org/cookieclicker/"

driver.get(URL)

lang = driver.find_element(By.ID, 'langSelect-EN')
lang.click()

# Load Cookie
load = time() + 6
while True:
    if time() > load:
        break

# Click Cursor
cursor = driver.find_element(By.CSS_SELECTOR, '#product0')

# Click Grandma
grandma = driver.find_element(By.CSS_SELECTOR, '#product1')

# Click Farm
farm = driver.find_element(By.CSS_SELECTOR, '#product2')

# Click Mine
mine = driver.find_element(By.CSS_SELECTOR, '#product3')


def getWeb():

    # Click Cookie
    cookie = driver.find_element(By.ID, 'bigCookie')
    time1 = time()
    time2 = time1
    time3 = time1

    timeout1 = time1 + 20
    timeout2 = time1 + 50
    timeout = time1 + 60*5

    while True:
        if time() > timeout1:
            break
        if time() > time1:
            cursor.click()
            time1 = time() + 1
        cookie.click()

    while True:
        if time() > timeout2:
            break
        if time() > time2:
            grandma.click()
            time2 = time() + 2
        cookie.click()

    while True:
        if time() > timeout:
            break
        if time() > time3:
            farm.click()
            mine.click()
            time3 = time() + 5
        cookie.click()


getWeb()
wait_time = time() + 3
while True:
    if time() > wait_time:
        break

cookies_per_second = driver.find_element(By.ID, 'cookiesPerSecond').text

cps = re.search(r"[\d\.]+", cookies_per_second)

print(cps.group())
