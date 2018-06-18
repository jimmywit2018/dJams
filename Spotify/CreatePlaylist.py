import pprint
import sys
import os
import subprocess
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy



scope = 'playlist-modify-private'
spotify = spotipy.Spotify()
playlist_name = input("What is the name of the playlist you wish to create? : ")
username = "h0m596l5gz014wayiyy29p0gg"
client_id = "b7642ea152d44cbf95e9d7efd223cc49"
client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b"

token = util.prompt_for_user_token(username, scope="playlist-modify-private", client_id="b7642ea152d44cbf95e9d7efd223cc49", client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b")

sp = spotipy.Spotify(auth=token)
sp.trace = False
sp.user_playlist_create(username, playlist_name, public=False)

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
track = input("Name of track you would like to add to playlist: ")
artist = input("Who is the artist of the track? ")
track_id= sp.search(q='artist' + artist + 'track:' + track, type='track')
pprint.pprint(track_id)
