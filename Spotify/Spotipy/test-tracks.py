import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #to access authorised spotify data
from matplotlib import style
from pprint import pprint
import time
from spotipy import util

# Improve Pandas display settings
pd.set_option("display.width", 600)
pd.set_option("display.max_columns", 50)

# Change Seaborn default settings
sns.set_context('talk')
style.use('ggplot')

# Spotify API limit
API_LIMIT = 50

username = "eltechnox"
playlist_name = "Bowpi"


Client_ID= ""
Client_Secret=""

client_credential_manager = SpotifyClientCredentials(client_id=Client_ID, client_secret=Client_Secret)
#setup the login and credentials
sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)

# Get playlist ID
playlists_results = sp.user_playlists(username)
playlist_ids = [playlist['id'] for playlist in playlists_results['items'] if playlist['name'] == playlist_name]
# Print the ID for the playlist configured at the begging

#pprint(playlists_results)

for playlist in playlists_results['items']:
    #playlist = sp.user_playlist("username", )
    #songs = playlist["tracks"]["items"]
    print("NOMBRE DE LA PLAYLIST" ,playlist['name'])
    print("ID DE LA PLAYLIST", playlist['id'])
    print("TOTAL DE CANCINES" , playlist["tracks"]["total"])


if not playlist_ids:
    raise Exception("Cannot find playlist named: {}".format(playlist_name))
else:
    print(playlist_ids)


# Get tracks
tracks_results = sp.user_playlist(username, playlist_ids[0])

df_tracks = pd.DataFrame([[t["track"]["id"],
                           t["track"]["name"],
                           t["track"]["artists"][0]["id"],
                           t["track"]["artists"][0]["name"],
                           t["track"]["album"]["name"],
                           t["track"]["popularity"]]


                          for t in tracks_results['tracks']['items']],
                         columns=["id", "song_name", "artist_id", "artist_name", "album_name", "popularity"])



# Normalize popularity
df_tracks["popularity_norm"] = df_tracks["popularity"] / 100.

#print(df_tracks)