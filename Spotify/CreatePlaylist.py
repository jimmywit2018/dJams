import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util

scope = 'playlist-modify-private'
spotify = spotipy.Spotify()
playlist_name = input("What is the name of the playlist you wish to create? : ")
playlist_description = input("Short description of the playlist? : ")
username = "h0m596l5gz014wayiyy29p0gg"
client_id = "b7642ea152d44cbf95e9d7efd223cc49"
client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b"
public = True

token = util.prompt_for_user_token(username, scope="playlist-modify-private", client_id="b7642ea152d44cbf95e9d7efd223cc49", client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b")

sp = spotipy.Spotify(auth=token)
sp.trace = False
playlists = self sp.user_playlist_create(username, playlist_name, public, playlist_description)
#pprint.pprint(playlists)
