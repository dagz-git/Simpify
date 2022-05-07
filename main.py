import spotipy
from os import environ as env
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = env.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = env.get("SPOTIPY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(CLIENT_ID,CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('spotify')










