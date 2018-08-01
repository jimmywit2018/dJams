import pprint
import sys
import os
import subprocess

import spotipy

import spotipy.util as util

export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
username = "h0m596l5gz014wayiyy29p0gg"

token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
else:
    print("Can't get token for", username)
