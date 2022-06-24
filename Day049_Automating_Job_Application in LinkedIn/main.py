import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time


load_dotenv()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

driver.get(URL)


def getWeb():

    signin = driver.find_element(
        By.CSS_SELECTOR, 'body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis')
    signin.click()

    # Wait for the next page to load.
    time.sleep(3)

    fill_user = driver.find_element(By.ID, 'username')
    fill_user.send_keys(os.environ['MY_EMAIL'])
    fill_pwd = driver.find_element(By.ID, 'password')
    fill_pwd.send_keys(os.environ['MY_PWD'])
    fill_pwd.send_keys(Keys.ENTER)

    time.sleep(8)

    jobs = driver.find_elements(
        By.CSS_SELECTOR, '.job-card-container--clickable')

    for job in jobs:
        print('called')
        job.click()
        time.sleep(2)

        try:
            apply_button = driver.find_element(
                By.CSS_SELECTOR, ".jobs-s-apply button")
            apply_button.click()
            time.sleep(5)

            # If phone field is empty, then fill your phone number.
            # phone = driver.find_element(
            #     By.CLASS_NAME, "fb-single-line-text__input")
            # if phone.text == "":
            #     for _ in range(10):
            #         phone.send_keys(Keys.BACKSPACE)
            #     phone.send_keys(os.environ['PHONE'])

            submit_button = driver.find_element(
                By.CSS_SELECTOR, "footer button")

            # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
            if submit_button.get_attribute("aria-label") == "Continue to next step":
                close_button = driver.find_element(
                    By.CLASS_NAME, "artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_element(
                    By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
                discard_button.click()
                print("Complex application, skipped.")
                continue
            else:
                submit_button.click()

            # Once application completed, close the pop-up window.
            time.sleep(2)
            close_button = driver.find_element(
                By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
        except NoSuchElementException:
            print("No application button, skipped.")
            continue


getWeb()
time.sleep(5)
driver.quit()
