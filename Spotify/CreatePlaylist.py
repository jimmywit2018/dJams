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

token = util.prompt_for_user_token(username, scope="playlist-modify-private", client_id="b7642ea152d44cbf95e9d7efd223cc49", client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b", redirect_uri="http://google.com/")

sp = spotipy.Spotify(auth=token)
sp.trace = False
sp.user_playlist_create(username, playlist_name, public=False,)

playlist_id = input("What is the id of the playlist you wish to add songs to? : ")
results = sp.user_playlist_change_details(username, playlist_id, name=playlist_name, public=False,collaborative=collaborative, description=description)
print(results)

# track_ids="spotify:track:2lUA2flB94XburZIe7BmHZ"
# results = sp.user_playlist_add_tracks(username, playlist_name, track_ids)
# print(results)

#uri codes of songs spotify:track:2lUA2flB94XburZIe7BmHZ,


# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# track = input("Name of track you would like to add to playlist: ")
# artist = input("Who is the artist of the track? ")
# track_id= sp.search(q='artist' + artist + 'track:' + track, type='track')
# #pprint.pprint(track_id)
# print(track_id)
