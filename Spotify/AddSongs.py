import pprint
import sys

import spotipy
import spotipy.util as util

username = "h0m596l5gz014wayiyy29p0gg"
playlist_id = "spotify:user:h0m596l5gz014wayiyy29p0gg:playlist:3b6zyg3kZnWE18tTP04C0U"
#track_ids = ["spotify:track:6oYkwjI1TKP9D0Y9II1GT7"]

track_ids = input("enter list of track ids").split(",")
print (track_ids)

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope="playlist-modify-private", client_id="b7642ea152d44cbf95e9d7efd223cc49", client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b", redirect_uri="http://google.com/")
print("testing")
if token:
    print("got into if statement")
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)
else:
    print("nothing")
