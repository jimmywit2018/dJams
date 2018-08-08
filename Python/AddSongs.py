import pprint
import sys
import requests
import spotipy
import spotipy.util as util

#harcode username and playlist id temporarily until we can pull those
#should ask for username in survey and store in db
scope = 'playlist-modify-public'
username = 'h0m596l5gz014wayiyy29p0gg'
playlist_id = '3b6zyg3kZnWE18tTP04C0U'
track_ids = ['6lanRgr6wXibZr8KgzXxBl','4kflIGfjdZJW4ot2ioixTB']
client_id = 'b7642ea152d44cbf95e9d7efd223cc49'
client_secret = '1094e61f08a845a6b1e9a651fe9a1e2b'
#get list of track ideas from user to put into list
#track_ids = input("enter list of track ids").split(",")
print (track_ids)

token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret = client_secret , redirect_uri="http://google.com/")

sp = spotipy.Spotify(auth=token)
sp.trace = False
results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
print(results)
