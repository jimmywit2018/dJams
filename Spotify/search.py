import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import spotipy.util as util
import requests
import json
import mmap
import re

scope = "playlist-modify-public"
username = 'h0m596l5gz014wayiyy29p0gg'


client_id = 'b7642ea152d44cbf95e9d7efd223cc49'
client_secret = '1094e61f08a845a6b1e9a651fe9a1e2b'
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret = client_secret , redirect_uri="http://google.com/")

sp = spotipy.Spotify(auth=token)

headers = {"Authorization": "Bearer " + token, "Accept": "application/json", "Content-Type": "application/json"}
url = "https://api.spotify.com/v1/users/"+username+"/playlists"
response = requests.get(url, headers=headers)
print(response.status_code)
#print(response.text)

json_data= json.loads(response.text)
with open('playlists.json', 'w') as outfile:
         json.dump(json_data, outfile,indent=4, sort_keys=True)
with open('playlists.json') as infile:
     dataplaylist = json.loads(infile.read())
iter = 0
for track in dataplaylist['items']:

    print(len(track))
    while iter < 5:
        print(iter)
        playlist_name = dataplaylist['items'][iter]['name']
        playlist_uri= dataplaylist['items'][iter]['uri']
        print(playlist_name, playlist_uri)
        iter= iter+1
# print(items)
# outfile.close()
# infile.close()
