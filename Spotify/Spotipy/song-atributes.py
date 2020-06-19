import pandas as pd
import spotipy
sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint


Client_ID= ""
Client_Secret=""

client_credentials_manager = SpotifyClientCredentials(client_id=Client_ID, client_secret=Client_Secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False
playlist = sp.user_playlist("eltechnox", "4K8eCXMWKZM2g6hQe8U8Vf") ##playlist ID
songs = playlist["tracks"]["items"]
##pprint(songs) ###
ids = []
for i in range(len(songs)):
    ids.append(songs[i]["track"]["id"])

features = sp.audio_features(ids)

name = []
for i in range(len(songs)):
    name.append(songs[i]["track"]["name"])


df = pd.DataFrame(features)
df['Name'] = name

pprint (df) ###