import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize API
client_credentials_manager = SpotifyClientCredentials(client_id='',
                                                      client_secret='')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Generate list of songs to query metadata for
track_uri_toquery = pd.read_csv("track_api_query.csv")
list_to_query = list(track_uri_toquery['Track_uri'])
unique_tracks = list(set(list_to_query))

# Query metadata 50 songs at a time
start = 0
end = len(list_to_query)
for i in range(start, end, 50):
    temp_list = list_to_query[i:i+50]
    playlists = sp.audio_features(temp_list)

    if "itemlist" in locals():
        itemlist = itemlist + playlists # append new data
    else:
        itemlist = playlists

    if len(itemlist) == 600: # save partial data into 600 chunks in case of error
        temp_filename = "audio_features" + str(i) + ".txt"

        with open(temp_filename,"wb") as fp: # write updated new data
            pickle.dump(itemlist, fp)
            del itemlist
    time.sleep(np.random.randint(2,5))
