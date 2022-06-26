from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
from dotenv import load_dotenv
from time import sleep, time

load_dotenv()


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.get(os.environ['IG_URL'])
        self.followList = []
        sleep(8)

    def login(self):
        username = self.driver.find_element(
            By.NAME, 'username')
        username.send_keys(os.environ['IG_USER'])
        sleep(1)

        password = self.driver.find_element(
            By.NAME, 'password')
        password.send_keys(os.environ['IG_PWD'])
        password.send_keys(Keys.ENTER)
        sleep(8)

        not_now = self.driver.find_element(By.XPATH, '//*[text()="Not Now"]')
        not_now.click()
        sleep(8)

        not_now2 = self.driver.find_element(By.XPATH, '//*[text()="Not Now"]')
        not_now2.click()
        sleep(8)

    def find_followers(self):
        search = self.driver.find_element(
            By.CSS_SELECTOR, '[aria-label="Search input"]')
        search.send_keys(os.environ['IG_TARGET'])
        sleep(5)

        target = self.driver.find_element(
            By.XPATH, '//*[@role="none"]')
        target.click()
        sleep(8)

        followers = self.driver.find_element(
            By.XPATH, '//*[text()=" followers"]')
        followers.click()
        sleep(2)

        self.followList = self.driver.find_elements(
            By.XPATH, '//*[text()="Follow"]')
        sleep(5)

    def follow(self):
        timeout = time() + 60*1
        for item in self.followList:
            item.click()
            sleep(1)
            if time() > timeout:
                break


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
