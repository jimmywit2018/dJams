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

##################################################################################################################################################
#sets up the connection to mongodb
client = pymongo.MongoClient("mongodb+srv://dannyzidelis:DJAMSdurga1!@djamscluster-u6bx0.mongodb.net/dJamsDB")

db = client.dJamsDB

coll_pref = db.MusicPref
##################################################################################################################################################

#define the scope of what class is allowed to do as well as the client_id and secret
scope = 'playlist-modify-public'
client_id = 'b7642ea152d44cbf95e9d7efd223cc49'
client_secret = '1094e61f08a845a6b1e9a651fe9a1e2b'

#asks user for name of desired playlist, will change when code is melded with jimmys
#playlist_name = input("What is the name of the playlist you wish to create? : ")
playlist_name = ["Work", "Work Out", "Rain", "Relax", "Sunny"]

##################################################################################################################################################
#gets the information about the user from the music preference collection
with open('currentuser.txt', 'r') as myfile:
    email=myfile.read().replace('\n', '')
# print(email)
query_results = coll_pref.find_one({"email": email})
query_results = json.dumps(query_results, indent=4, default=json_util.default)
query_results = json.loads(query_results)
username = query_results['username']
##################################################################################################################################################

#set up the Spotipy API for creating of playlists
token = util.prompt_for_user_token(username, scope=scope, client_id=client_id, client_secret = client_secret, redirect_uri="http://google.com/")
sp = spotipy.Spotify(auth=token)

##################################################################################################################################################
#creates the playlists in the users spotify account
iter = 0
while iter < 5:
    sp.user_playlist_create(username, playlist_name[iter], public=True,)
    iter=iter+1
##################################################################################################################################################
