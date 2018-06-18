import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
#fix code so the class can be used to be called by a main class

spotify = spotipy.Spotify()
#something is going on with the user id where it is not accepted need
#to fix
playlistName = input("What is the name of the playlist you wish to create")
playlistDescription = input("Short description of the playlist")
userID = "h0m596l5gz014wayiyy29p0gg"
client_id = "b7642ea152d44cbf95e9d7efd223cc49"
client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b"

#once get create to work work on adding to it
user_playlist_create(userID, playlistName, public=True)
