# python library for the HTTP requests
import requests
# python library for the spotify
import spotipy
# python library to scrape information from web pages
from bs4 import BeautifulSoup
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth

global song_date

# spotify credential
Client_ID = CLIENT_ID
Client_Secret = CLIENT_SECRET


# checking if user date has correct format and is from the past
def check_date(selected_date):
    global song_date
    todat_date = str(datetime.today()).split()[0]

    # check if date has correct format:
    if len(selected_date) != 10:
        selected_date = input("The date needs to have 10 characters.Select new date:")
    elif selected_date[4] != "-" or selected_date[7] != "-":
        selected_date = input("The date has incorrect format.Select new date:")
    elif selected_date >= todat_date:
        selected_date = input("The date cannot be in future.Select new date:")
    elif selected_date <= "1901-01-01":
        selected_date = input("There aren't any list before 1901-01-01. Select new date: ")
    else:
        song_date = selected_date
        return song_date

    check_date(selected_date)


# select period for which you want generated songs list
# song_date:
time_period = check_date(input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: "))
year = song_date[:4]

URL = f"https://www.billboard.com/charts/hot-100/{song_date}"
data = requests.get(URL)
songs_list = data.text

# prepare a list of songs and artists
soup = BeautifulSoup(songs_list, "html.parser")
soup_songs = soup.find_all(name="span", class_="chart-element__information__song")
soup_artist = soup.find_all(name="span", class_="chart-element__information__artist")

list_of_songs = [song.getText() for song in soup_songs]
list_of_artists = [artist.getText() for artist in soup_artist]

# connecting to spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                    scope="playlist-modify-private",
                                    redirect_uri="http://example.com",
                                    client_id=Client_ID,
                                    client_secret=Client_Secret,
                                    show_dialog=True,
                                    cache_path="token.txt"))

user_id = sp.current_user()["id"]
song_uri =[]

for song in list_of_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# creating new private playlist
playlist = sp.user_playlist_create(user=user_id,  name=f"{song_date} Happy Birthday Łukasz!", public=False)

# adding songs to created playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)