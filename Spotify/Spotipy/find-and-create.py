import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #to access authorised spotify data
from matplotlib import style
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
playlist_name = "ARG"
genre = "Argentine Rock"
playlist_name_new = "Ritmo Argento"


# Get token
scope = 'playlist-modify-public'
spotify_token = util.prompt_for_user_token(username, scope)

# Create client
sp = spotipy.Spotify(auth=spotify_token)



# Get playlist ID
playlists_results = sp.user_playlists(username)
playlist_ids = [playlist['id'] for playlist in playlists_results['items'] if playlist['name'] == playlist_name]

if not playlist_ids:
    raise Exception("Cannot find playlist named: {}".format(playlist_name))
else:
    print(playlist_ids)



# Get tracks
tracks_results = sp.user_playlist(username, playlist_ids[0])

df_tracks = pd.DataFrame([[t["track"]["id"], t["track"]["name"], t["track"]["artists"][0]["id"],
                           t["track"]["artists"][0]["name"], t["track"]["album"]["name"], t["track"]["popularity"]]
                          for t in tracks_results['tracks']['items']],
                         columns=["id", "song_name", "artist_id", "artist_name", "album_name", "popularity"])
# Normalize popularity
df_tracks["popularity_norm"] = df_tracks["popularity"] / 100.

df_tracks.head()



def _get_artists_df(sp, artist_ids):
    """
    This is an helper method to get artist's information with pagination from artist ids.
    It returns a Pandas dataframe
    """

    artist_list = []
    i = 0

    while artist_ids:
        print("Call #{} for artists".format(i + 1))
        artists_results = sp.artists(artist_ids[:API_LIMIT])

        artist_list += [[t["id"], t["genres"], t["popularity"]] for t in artists_results["artists"]]

        artist_ids = artist_ids[API_LIMIT:]
        i += 1

    df_artists = pd.DataFrame(artist_list, columns=["artist_id", "artist_genres", "artist_popularity"])

    df_artists["artist_popularity_norm"] = df_artists["artist_popularity"] / 100.

    return df_artists



artist_ids = df_tracks["artist_id"].unique().tolist()
df_artists = _get_artists_df(sp, artist_ids)
print(df_artists.head())



def _get_features_df(sp, track_ids):
    """
    This is an helper method to get track's features with pagination from track ids.
    It returns a Pandas dataframe
    """

    feature_list = []
    i = 0
    while track_ids:
        print("Call #{} for audio features".format(i + 1))
        features_results = sp.audio_features(track_ids[:API_LIMIT])

        feature_list += features_results

        track_ids = track_ids[API_LIMIT:]
        i += 1

    df_features = pd.DataFrame(feature_list)[["id", "analysis_url", "duration_ms", "acousticness", "danceability",
                                              "energy", "instrumentalness", "liveness", "loudness", "valence",
                                              "speechiness", "key", "mode", "tempo", "time_signature"]]
    # tempo is in range 24-200 ==> 0-176, normalize it
    df_features["tempo_norm"] = (df_features["tempo"] - 24) / 176.

    return df_features


track_ids = df_tracks["id"].unique().tolist()
df_features = _get_features_df(sp, track_ids)
print(df_features.head())


# Create a df for current playlist merging the dataframes
df_cur = df_features.merge(df_tracks, on="id")
df_cur = df_cur.merge(df_artists, on="artist_id")

# Create a new column with full name of the song
df_cur["full_name"] = df_cur["artist_name"] + " -- " + df_cur["song_name"]

# Sort by song popularity
df_cur.sort_values("popularity", inplace=True, ascending=False)

print(df_cur.head())

print(df_cur.info())

df_cur.describe()

# Convert time_signature and key to category
df_cur["time_signature"] = df_cur["time_signature"].astype(pd.api.types.CategoricalDtype(categories=[1, 2, 3, 4, 5]))
df_cur["key"] = df_cur["key"].astype(pd.api.types.CategoricalDtype(categories=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

def _distplot(df, key, label, x_limits):
    """
    This is an helper method to plot distribution charts
    """
    ax = sns.distplot(df[[key]], bins=30, label=label)
    if x_limits is not None:
        ax.set_xlim(*x_limits)
    plt.title(key)
    plt.legend()
    #plt.show()

x_limits = {"duration_ms": None, "loudness": (-60, 0), "tempo": (24, 200), "popularity": (0, 100),
            "artist_popularity": (0, 100)}

for key in ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness",
                    "loudness", "valence", "speechiness", "tempo", "popularity", "artist_popularity"]:
    _distplot(df_cur, key, label="My Playlist", x_limits=x_limits.get(key, (0, 1)))

def _countplot(df, key, label):
    """
    This is an helper method to plot count charts
    """
    ax = sns.countplot(data=df, x=key, palette="tab20")
    ax.set_title(label)
    #plt.show()



for key in ["key", "time_signature", "mode"]:
    _countplot(df_cur, key, label="My Playlist")


ax = sns.boxplot(data=df_cur[["acousticness", "danceability", "energy", "instrumentalness", "liveness",
                              "valence", "speechiness", "artist_popularity_norm", "popularity_norm", "tempo_norm"]])
ax.set_title("My Playlist")
#plt.show() #eliminamos las graficas de la playlist



#number_of_tracks = 5000

#search_runs = int(number_of_tracks / API_LIMIT)

search_list = []
for i in range(40):
    print("Call #{} for tracks".format(i+1))
    search_results = sp.search('genre:"{}"'.format(genre), type="track", limit=API_LIMIT, offset=API_LIMIT*i)
    #print(search_results)

    search_list += [[t["id"], t["name"], t["artists"][0]["id"], t["artists"][0]["name"],
                            t["album"]["name"], t["popularity"]]
                            for t in search_results['tracks']['items']]
#print(search_list)
df_search = pd.DataFrame(search_list, columns=["id", "song_name", "artist_id", "artist_name", "album_name", "popularity"])
df_search["popularity_norm"] = df_search["popularity"] / 100.
print(df_search)






track_ids = df_search["id"].unique().tolist()
df_features = _get_features_df(sp, track_ids)
df_features.head()

artist_ids = df_search["artist_id"].unique().tolist()
df_artists = _get_artists_df(sp, artist_ids)
df_artists.head()

df_sample = df_features.merge(df_search, on="id")
df_sample = df_sample.merge(df_artists, on="artist_id")

df_sample["full_name"] = df_sample["artist_name"] + " -- " + df_sample["song_name"]
df_sample.sort_values("popularity", inplace=True, ascending=False)

df_sample.head()

# Convert time_signature and key to category
df_sample["time_signature"] = df_sample["time_signature"].astype(pd.api.types.CategoricalDtype(categories=[1, 2, 3, 4, 5]))
df_sample["key"] = df_sample["key"].astype(pd.api.types.CategoricalDtype(categories=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

print(df_sample.info())

df_sample.describe()



def _distplot2(df, df_other, key, labels, x_limits):
    ax = sns.distplot(df[[key]], bins=30, label=labels[0])
    if x_limits is not None:
        ax.set_xlim(*x_limits)
    ax = sns.distplot(df_other[[key]], bins=30, label=labels[1])
    if x_limits is not None:
        ax.set_xlim(*x_limits)
    plt.title(key)
    plt.legend()
    #plt.show()

def _countplot2(df, df_other, key, labels):
    fig, ax = plt.subplots(1, 2)
    sns.countplot(data=df, x=key, ax=ax[0], palette="tab20")
    ax[0].set_title(labels[0])
    sns.countplot(data=df_other, x=key, ax=ax[1], palette="tab20")
    ax[1].set_title(labels[1])
    #plt.show()

for key in ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness",
            "loudness", "valence", "speechiness", "tempo", "popularity", "artist_popularity"]:
    _distplot2(df_cur, df_sample, key,
              labels=["My Playlist", "5000 Indie rock songs"],
              x_limits=x_limits.get(key, (0, 1)))

for key in ["key", "time_signature", "mode"]:
    _countplot2(df_cur, df_sample, key, labels=["My Playlist", "5000 Indie rock songs"])





fig, ax = plt.subplots(2, 1)
sns.boxplot(data=df_cur[["acousticness", "danceability", "energy", "instrumentalness", "liveness",
                         "valence", "speechiness", "artist_popularity_norm", "popularity_norm",
                         "tempo_norm"]], ax=ax[0])
ax[0].set_title("My Playlist")
sns.boxplot(data=df_sample[["acousticness", "danceability", "energy", "instrumentalness", "liveness",
                           "valence", "speechiness", "artist_popularity_norm", "popularity_norm",
                           "tempo_norm"]], ax=ax[1])
ax[1].set_title("5000 Indie rock songs")
#plt.show()






def _apply_condition(df, condition, label):
    before = len(df)
    dropped_songs = df[~condition]["full_name"].head().tolist()
    df = df[condition]
    print("\ncondition [{}]: {}-{}={}".format(label, before, before - len(df), len(df)))
    print("first 10 dropped songs: {}".format(dropped_songs))
    return df

df_new = df_sample.drop_duplicates(["full_name"], keep="first")

###################################################################################################################
##############################################Filtros #############################################################

df_new = _apply_condition(df_new,
                          condition=~(df_new["full_name"]).isin((df_cur["full_name"]).tolist()),
                          label="name")

df_new = _apply_condition(df_new,
                          condition=(df_new["acousticness"] < 0.5),
                          label="acousticness")

df_new = _apply_condition(df_new,
                          condition=(df_new["energy"] > 0.75),
                          label="energy")

df_new = _apply_condition(df_new,
                          condition=(df_new["loudness"] > -7),
                          label="loudness")

df_new = _apply_condition(df_new,
                          condition=(df_new["valence"].between(0.3, 0.9)),
                          label="valence")

df_new = _apply_condition(df_new,
                          condition=(df_new["tempo"] > 120),
                          label="tempo")

df_new = _apply_condition(df_new,
                          condition=(df_new["key"].isin([9, 0, 1, 6])),
                          label="key")

df_new = _apply_condition(df_new,
                          condition=(df_new["duration_ms"].between(*df_cur["duration_ms"].quantile([0.1, 0.9]))),
                          label="duraton_ms")

df_new.head()


###################################################################################################################
##############################################Filtros #############################################################



playlists = sp.user_playlists(username)

playlist_ids = [playlist['id'] for playlist in playlists['items'] if playlist['name'] == playlist_name_new]

if not playlist_ids:
    playlists = sp.user_playlist_create(username, playlist_name_new)
    playlist_id = playlists["id"]

else:
    playlist_id = playlist_ids[0]

    results = sp.user_playlist(username, playlist_id)
    track_ids = [t["track"]["id"] for t in results["tracks"]["items"]]
    results = sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, track_ids)
    print(results)

track_ids = df_new["id"].unique().tolist()

while track_ids:
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids[:API_LIMIT])
    print(results)
    track_ids = track_ids[API_LIMIT:]