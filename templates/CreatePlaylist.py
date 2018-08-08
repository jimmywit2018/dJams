import pprint
import sys
import os
import subprocess
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pymongo
from pymongo import MongoClient
import pprint
import json
from bson import ObjectId
from bson import BSON
from bson import json_util
import requests

client = pymongo.MongoClient("mongodb+srv://dannyzidelis:DJAMSdurga1!@djamscluster-u6bx0.mongodb.net/dJamsDB")

db = client.dJamsDB

coll = db.MusicPref

#define the scope of what class is allowed to do
scope = 'playlist-modify-public'

#asks user for name of desired playlist, will change when code is melded with jimmys
#playlist_name = input("What is the name of the playlist you wish to create? : ")
playlist_name = ["Work", "Work Out", "Rain", "Relax", "Sunny"]

#hardcode username, apiKey and apiSecret
with open('currentuser.txt', 'r') as myfile:
    email=myfile.read().replace('\n', '')
# print(email)
query_results = coll.find_one({"email": email})
query_results = json.dumps(query_results, indent=4, default=json_util.default)
query_results = json.loads(query_results)
#print(query_results['username'])

username = query_results['username']
client_id = 'b7642ea152d44cbf95e9d7efd223cc49'
client_secret = '1094e61f08a845a6b1e9a651fe9a1e2b'

token = util.prompt_for_user_token(username, scope=scope, client_id=client_id, client_secret = client_secret, redirect_uri="http://google.com/")

sp = spotipy.Spotify(auth=token)

headers = {"Authorization": "Bearer " + token, "Accept": "application/json", "Content-Type": "application/json"}
url = "https://api.spotify.com/v1/users/"+username+"/playlists"
response = requests.get(url, headers=headers)

sp.trace = False
iter = 0
while iter < 5:
    sp.user_playlist_create(username, playlist_name[iter], public=True,)
    print("created playlist: ", playlist_name[iter])
    iter=iter+1


#scrap code
# playlist = input("What is the id of the playlist you wish to add songs to? : ")
# results = sp.user_playlist_change_details(username, playlist, name=playlist_name, public=False,collaborative=True)
# print(results)

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
