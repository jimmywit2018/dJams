import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import spotipy.util as util
import requests
import json
import mmap
import re

scope = "user-read-private"
username = 'h0m596l5gz014wayiyy29p0gg'

search_str_song = input("Enter the name of the song you would like to search: ")
search_str_art = input("Enter name of artist of the song:  ")

client_id = 'b7642ea152d44cbf95e9d7efd223cc49'
client_secret = '1094e61f08a845a6b1e9a651fe9a1e2b'
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret = client_secret , redirect_uri="http://google.com/")

#call API
sp = spotipy.Spotify(auth=token)

headers = {"Authorization": "Bearer " + token, "Accept": "application/json", "Content-Type": "application/json"}
url = "https://api.spotify.com/v1/search?q=track:"+search_str_song+"%20artist:"+search_str_art+"&type=track"
response = requests.get(url, headers=headers)

#print(response)
#print(response.text)

#loads the response into a json_data
json_data= json.loads(response.text)
with open('search.json', 'w') as outfile:
        json.dump(json_data, outfile)
if "spotify:track:" in open('search.json').read():
    print("true")

file = open('search.json', 'r+b')
mf = mmap.mmap(file.fileno(), 0)
mf.seek(0) # reset file cursor
search = "spotify:track"
search_as_byte = str.encode(search)
#print(type(search_as_byte))
m = re.search(search_as_byte, mf)
#print(m.start(), m.end())
mf.close()
file.close()
# playresponse = requests.get("https://api.spotify.com/v1/search?q=%22durga11%22&type=playlist", headers=headers)
# print(playresponse)
# print(playresponse.text)
#result = sp.search(search_str)
#pprint.pprint(result)
