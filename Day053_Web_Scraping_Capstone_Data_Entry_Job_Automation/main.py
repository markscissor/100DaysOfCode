from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import requests
from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv
from time import sleep, time


load_dotenv()


r = requests.get(os.environ['ZIL_URL'],
                 headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
})

soup = BeautifulSoup(r.text, 'html.parser')

info = soup.find_all(name='div', class_='list-card-info')

houses = []

for item in info:
    print()
    for child in item.children:
        # print(child)
        if child.name == 'a':
            link = f"{os.environ['ZIL_BASE_URL']}{child['href']}"
            # print(link)

            address = child.address.contents[0]
            # print(address)

            for gchild in child.next_sibling.next_sibling.children:
                if gchild.name == 'div':
                    search_price = re.search(r"[\d]+,[\d]+",
                                             gchild.contents[0]).group()
                    price = int(re.sub(r",", "", search_price))
                    # print(price)

            listing = {
                'link': link,
                'address': address,
                'price': price
            }

            houses.append(listing)
            print(listing)


options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get(os.environ['FORM_URL'])
sleep(8)

for house in houses:

    add_input = driver.find_element(
        By.XPATH, '//*[@aria-labelledby="i1"]')
    add_input.send_keys(house['address'])

    price_input = driver.find_element(
        By.XPATH, '//*[@aria-labelledby="i5"]')
    price_input.send_keys(house['price'])

    link_input = driver.find_element(
        By.XPATH, '//*[@aria-labelledby="i9"]')
    link_input.send_keys(house['link'])

    try:
        button_send = driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        button_send.click()
        sleep(5)
        post_another = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        post_another.click()
        sleep(3)

    except NoSuchElementException:

        no_login = driver.find_element(
            By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[1]/span/span')
        no_login.click()
        sleep(3)

        button_send = driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        button_send.click()
        sleep(5)
        post_another = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        post_another.click()
        sleep(3)
