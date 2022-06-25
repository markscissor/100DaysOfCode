import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
from dotenv import load_dotenv
import time


load_dotenv()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://tinder.com/"

driver.get(URL)

time.sleep(5)


def getWeb():

    acceptCookie = driver.find_element(
        By.XPATH, '//*[@id="t1836739397"]/div/div[2]/div/div/div[1]/div[1]/button/span')
    acceptCookie.click()

    login = driver.find_element(
        By.XPATH, '//*[@id="t1836739397"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/span')
    login.click()

    time.sleep(8)
    fblogin = driver.find_element(
        By.XPATH, '//*[@id="t108358321"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
    fblogin.click()

    time.sleep(5)

    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title)

    fb_email = driver.find_element(By.NAME, 'email')
    fb_email.send_keys(os.environ['FB_EMAIL'])

    fb_pwd = driver.find_element(By.NAME, 'pass')
    fb_pwd.send_keys(os.environ['FB_PWD'])

    fb_login = driver.find_element(By.NAME, 'login')
    fb_login.click()

    time.sleep(5)

    driver.switch_to.window(base_window)
    print(driver.title)

    time.sleep(8)

    # loc_window = driver.window_handles[1]
    # driver.switch_to.window(loc_window)
    # print(driver.title)

    share_loc = driver.find_element(
        By.XPATH, '//*[@id="t108358321"]/div/div/div/div/div[3]/button[1]')
    share_loc.click()

    time.sleep(8)

    not_enable_notifs = driver.find_element(
        By.XPATH, '//*[@id="t108358321"]/div/div/div/div/div[3]/button[2]/span')
    not_enable_notifs.click()

    time.sleep(8)

    like_button = driver.find_element(
        By.XPATH, '//*[@id="t1836739397"]/div/div[1]/div/div/main/div/div/div/div/div[4]/div/div[4]/button/span/span')

    timeout = time.time() + 60*1

    while True:
        try:
            like_button.click()
            time.sleep(1)
        except NoSuchElementException:
            time.sleep(2)
            continue
        except ElementClickInterceptedException:
            time.sleep(1)
            try:
                back_to_tinder = driver.find_element(
                    By.XPATH, '//*[@id="t108358321"]/div/div/div/div/div[4]/button')
                back_to_tinder.click()
                time.sleep(2)
            except NoSuchElementException:
                home_screen_not = driver.find_element(
                    By.XPATH, '//*[@id="t108358321"]/div/div/div[2]/button[2]')
                home_screen_not.click()
                time.sleep(2)
        if time.time() > timeout:
            break


getWeb()
time.sleep(5)
