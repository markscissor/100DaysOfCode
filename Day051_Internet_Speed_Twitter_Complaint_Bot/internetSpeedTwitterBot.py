import imp
from mimetypes import init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(os.environ['URL1'])
        sleep(8)

        go_button = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        sleep(40)

        self.down = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get(os.environ['URL2'])
        sleep(12)

        try:
            signin = self.driver.find_element(
                By.XPATH, '//*[text()="Sign in"]')
            signin.click()
            sleep(8)
        except NoSuchElementException:
            signin = self.driver.find_element(
                By.XPATH, '//*[text()="Log in"]')
            signin.click()
            sleep(8)

        email_input = self.driver.find_element(By.NAME, 'text')
        email_input.send_keys(os.environ['TWITTER_EMAIL'])
        email_input.send_keys(Keys.ENTER)
        sleep(8)

        try:
            password_input = self.driver.find_element(By.NAME, 'password')
            password_input.send_keys(os.environ['TWITTER_PWD'])
            password_input.send_keys(Keys.ENTER)
            sleep(10)
        except NoSuchElementException:
            password_input = self.driver.find_element(By.NAME, 'text')
            password_input.send_keys(os.environ['TWITTER_USER'])
            password_input.send_keys(Keys.ENTER)
            sleep(5)
            password_input = self.driver.find_element(By.NAME, 'password')
            password_input.send_keys(os.environ['TWITTER_PWD'])
            password_input.send_keys(Keys.ENTER)
            sleep(10)

        if float(self.down) < float(os.environ['PROMISED_DOWN']) or float(self.up) < float(os.environ['PROMISED_UP']):
            msg = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {os.environ['PROMISED_DOWN']}down/{os.environ['PROMISED_UP']}up."
        else:
            msg = f"Good work Internet Provider, my internet speed is {self.down}down/{self.up}up even if I pay for {os.environ['PROMISED_DOWN']}down/{os.environ['PROMISED_UP']}up."

        tweetbtn = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweetbtn.click()
        sleep(3)

        tweet_box = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(msg)
        sleep(1)

        tweet_send = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div')
        tweet_send.click()
        sleep(10)
