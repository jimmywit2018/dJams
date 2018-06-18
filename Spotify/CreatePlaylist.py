import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util
#fix code so the class can be used to be called by a main class

scope = 'playlist-modify-private'
spotify = spotipy.Spotify()
playlistName = input("What is the name of the playlist you wish to create? : ")
playlistDescription = input("Short description of the playlist? : ")
username = "h0m596l5gz014wayiyy29p0gg"
client_id = "b7642ea152d44cbf95e9d7efd223cc49"
client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b"

#once get create to work work on adding to it
token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name,
                                        playlist_description)
    pprint.pprint(playlists)
else:
    print("Can't get token for", username)
