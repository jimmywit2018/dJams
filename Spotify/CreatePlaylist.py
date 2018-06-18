import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
#fix code so the class can be used to be called by a main class

scope = 'playlist-modify-private'
spotify = spotipy.Spotify()
playlistName = input("What is the name of the playlist you wish to create? : ")
playlistDescription = input("Short description of the playlist? : ")
userID = "h0m596l5gz014wayiyy29p0gg"
client_id = "b7642ea152d44cbf95e9d7efd223cc49"
client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b"

#once get create to work work on adding to it
token = util.prompt_for_user_token(username, scope, client_id="b7642ea152d44cbf95e9d7efd223cc49", client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b" , redirect_uri="http://google.com/")

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)
sp.user_playlist_create(userID, playlistName, public=True)
