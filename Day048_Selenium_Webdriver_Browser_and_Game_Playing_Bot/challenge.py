from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "http://secure-retreat-92358.herokuapp.com/"

driver.get(URL)


def getWeb():

    fname = driver.find_element(By.NAME, 'fName')
    fname.send_keys('Mark Cezar')

    lname = driver.find_element(By.NAME, 'lName')
    lname.send_keys('Muñoz')

    email = driver.find_element(By.NAME, 'email')
    email.send_keys('mcnmunoz@gmail.com')

    button = driver.find_element(By.CSS_SELECTOR, 'form button')
    button.click()


getWeb()
