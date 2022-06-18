from pprint import pprint
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

while True:
    target_date = input(
        "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    m = re.search(r"(\d+)-(\d+)-(\d+)", target_date)

    if m:
        try:
            date = m.group(0)
            year = m.group(1)
            d = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))

        except ValueError:
            print('Enter a valid date.')
            continue

        target_date = m[0]
        break

URL = f"https://www.billboard.com/charts/hot-100/{target_date}"

response = requests.get(URL)

billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, 'html.parser')

song_names = [title.getText().strip() for title in soup.select(
    ".c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021.lrv-u-font-size-16.u-line-height-125.a-truncate-ellipsis")]

# Make a Spotify Playlist
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=os.environ['SPOTIPY_CLIENT_ID'],
        client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
song_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

pprint(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)