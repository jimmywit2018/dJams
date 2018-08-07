import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import spotipy.util as util
import requests
import json
import mmap
import re
import pymongo
from pymongo import MongoClient
import pprint
from bson import ObjectId
from bson import BSON
from bson import json_util

client = pymongo.MongoClient("mongodb+srv://dannyzidelis:DJAMSdurga1!@djamscluster-u6bx0.mongodb.net/dJamsDB")
db = client.dJamsDB
coll_in = db.MusicPref
coll_out =db.Spotify

with open('currentuser.txt', 'r') as myfile:
    email=myfile.read().replace('\n', '')
# print(email)
query_results = coll_in.find_one({"email": email})
query_results = json.dumps(query_results, indent=4, default=json_util.default)
query_results = json.loads(query_results)
# print(query_results)
#print(query_results['username'])
print(query_results)
username = query_results['username']
client_id = 'b7642ea152d44cbf95e9d7efd223cc49'
client_secret = '1094e61f08a845a6b1e9a651fe9a1e2b'

scope = 'playlist-modify-public'

token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret = client_secret , redirect_uri="http://google.com/")

sp = spotipy.Spotify(auth=token)

headers = {"Authorization": "Bearer " + token, "Accept": "application/json", "Content-Type": "application/json"}
url = "https://api.spotify.com/v1/users/"+username+"/playlists"
response = requests.get(url, headers=headers)
#print(response.status_code)
#print(response.text)

json_data= json.loads(response.text)
with open('playlists.json', 'w') as outfile:
         json.dump(json_data, outfile,indent=4, sort_keys=True)
with open('playlists.json') as infile:
     dataplaylist = json.loads(infile.read())
iter = 0
for track in dataplaylist['items']:
    playlist_owner= dataplaylist['items'][iter]['owner']['id']
    if(playlist_owner==username):
        playlist_name = dataplaylist['items'][iter]['name']
        playlist_uri= dataplaylist['items'][iter]['uri']
        playlist_id = dataplaylist['items'][iter]['id']
        # print(playlist_name, playlist_uri, playlist_id)
        if playlist_name == "Relax":
            playlist_rec = {"username": username, "email": email, "Playlist Name":"Relax", "PlaylistID": playlist_id, "PlaylistURI": playlist_uri}
            rec_id = coll_out.insert_one(playlist_rec)
        elif playlist_name == "Rain":
            playlist_rec = {"username": username, "email": email, "Playlist Name":"Rain", "PlaylistID": playlist_id, "PlaylistURI": playlist_uri}
            rec_id = coll_out.insert_one(playlist_rec)
        elif playlist_name == "Work Out":
            playlist_rec = {"username": username, "email": email, "Playlist Name":"Work Out", "PlaylistID": playlist_id, "PlaylistURI": playlist_uri}
            rec_id = coll_out.insert_one(playlist_rec)
        elif playlist_name == "Work":
            playlist_rec = {"username": username, "email": email, "Playlist Name":"Work", "PlaylistID": playlist_id, "PlaylistURI": playlist_uri}
            rec_id = coll_out.insert_one(playlist_rec)
        elif playlist_name == "Sunny":
            playlist_rec = {"username": username, "email": email, "Playlist Name":"Sunny", "PlaylistID": playlist_id, "PlaylistURI": playlist_uri}
            rec_id = coll_out.insert_one(playlist_rec)
        iter= iter+1
# print(items)
# outfile.close()
# infile.close()
