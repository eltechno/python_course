import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import pandas as pd

client_credentials_manager = SpotifyClientCredentials(client_id='',
                                                      client_secret='')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#spotify playlist info demo
playlists = sp.user_playlists('eltechnox')

offset = 0
while playlists:
    for i, playlist_item in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist_item['uri'],  playlist_item['name']))
        response = sp.playlist_tracks(playlist_item['uri'],
                                      offset=offset,
                                      fields='items.track.id, items.track.name')
        #print(response['items'])


        #tracks_results = sp.user_playlist('eltechnox', playlist_item['uri'])
        #print(tracks_results)



    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None


