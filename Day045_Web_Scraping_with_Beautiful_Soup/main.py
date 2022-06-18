import requests
from bs4 import BeautifulSoup
import re
# We will scrape this url
# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, 'html.parser')
# We will save the scraped data in a dictionary
# movie_dict = { int(re.split(r'[:\)]\s', title.getText())[0]):re.split(r'[:\)]\s', title.getText())[1] for title in soup.find_all(name='h3', class_='title') }
movie_dict = {int(re.split(r'[:\)]\s', title.getText())[0]): re.split(
    r'[:\)]\s', title.getText())[1] for title in soup.find_all(name='h3', class_='jsx-4245974604')}

# Save the data in a text file
with open('movies.txt', 'w') as file:
    for index in range(1, 101):
        if index in movie_dict:
            # print(index, movie_dict[index])
            raw = f"{index}) {movie_dict[index]}\n"
            file.write(raw)
