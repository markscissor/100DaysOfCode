from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://en.wikipedia.org/wiki/Main_Page"

events = []
dates = []
driver.get(URL)


def getWeb():

    # articles = driver.find_element(
    #     by=By.XPATH,
    #     value='//*[@id="articlecount"]/a[1]'
    # )

    # articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
    # print(articles.text)

    # all_portals = driver.find_element(By.LINK_TEXT, 'Content portals')
    # all_portals.click()

    search = driver.find_element(By.NAME, 'search')
    search.send_keys('Python')
    search.send_keys(Keys.ENTER)


getWeb()
