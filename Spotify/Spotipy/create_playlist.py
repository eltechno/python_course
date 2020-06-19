import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #to access authorised spotify data
from matplotlib import style
import time
from spotipy import util


username = "eltechnox"
playlist_name = "EDM"


Client_ID= ""
Client_Secret=""

client_credential_manager = SpotifyClientCredentials(client_id=Client_ID, client_secret=Client_Secret)
sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)

# Get playlist ID
playlists_results = sp.user_playlists(username)
playlist_ids = [playlist['id'] for playlist in playlists_results['items'] if playlist['name'] == playlist_name]
print(playlists_results)



playlist_name_new = "NEWPLAY"
desc= "this is a test"

playlists = sp.user_playlist_create(username, playlist_name_new, public=False, description=desc)
#playlist_recs = sp.user_playlist_create(username, playlist_name_new, desc)
