import requests
import json
import time
import hashlib
import sys
import pprint
import urllib
import os
from urllib.request import urlopen
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
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
coll_pref = db.MusicPref
coll_spot =db.Spotify
with open('currentuser.txt', 'r') as myfile:
    email=myfile.read().replace('\n', '')
query_results = coll_spot.find_one({"email": email})
query_results = json.dumps(query_results, indent=4, default=json_util.default)
query_results = json.loads(query_results)

relax_results = coll_spot.find_one({"email": email})
relax_results = json.dumps(relax_results, indent=4, default=json_util.default)
relax_results = json.loads(relax_results)
relaxid = relax_results['PlaylistID']
rain_results = coll_spot.find_one({"email": email})
rain_results = json.dumps(rain_results, indent=4, default=json_util.default)
rain_results = json.loads(rain_results)
rainid = relax_results['PlaylistID']
work_results = coll_spot.find_one({"email": email})
work_results = json.dumps(work_results, indent=4, default=json_util.default)
work_results = json.loads(work_results)
workid = relax_results['PlaylistID']
workout_results = coll_spot.find_one({"email": email})
workout_results = json.dumps(workout_results, indent=4, default=json_util.default)
workout_results = json.loads(workout_results)
workoutid = relax_results['PlaylistID']
sunny_results = coll_spot.find_one({"email": email})
sunny_results = json.dumps(sunny_results, indent=4, default=json_util.default)
sunny_results = json.loads(sunny_results)

scope = "playlist-modify-public"
#get info from db
username = query_results['username']
#create and assign apiKey and apiSecret values
apiKey="u8b9c5u6cwwt3mnns9ubdah6"
apiSecret = "gwGXJdarNB"
apiK= "7d02f117f44c9fcc4205c77ef98e6288"
apiS= "2fbb022389b40a3d6efcc9faf23432aa"
client_id = 'b7642ea152d44cbf95e9d7efd223cc49'
client_secret = '1094e61f08a845a6b1e9a651fe9a1e2b'
track_ids=[]
#hardcoded playlistid for now

playlist_id = "spotify:user:h0m596l5gz014wayiyy29p0gg:playlist:6HgvHLnb2O6XzwfVSAGcI9"
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret = client_secret , redirect_uri="http://google.com/")

sp = spotipy.Spotify(auth=token)
#set up hash
m = hashlib.md5()

#create url variables for every type of api call

#get unix time as an integer so there are no decimals,
#possibly print for decoding purposes
unixTime = int(time.time())
#print(unixTime)

##################################################################################################################################################
#gets the music for relax playlist
if os.path.exists('musicapisearchrelax.json') == True:
    os.remove('musicapisearchrelax.json')
limit = "100"
tag = "disco"
url = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit=20&api_key=7d02f117f44c9fcc4205c77ef98e6288&format=json"
similar = "https://ws.audioscrobbler.com/2.0/?method=tag.getsimilar&tag="+tag+"&api_key="+apiK+"&format=json"
#call API
responserelax = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit="+limit+"&api_key="+apiK+"&format=json")
resultrelax = json.loads(responserelax.text)
with open('musicapisearchrelax.json', 'w') as outfilerelax:
         json.dump(resultrelax, outfilerelax, indent=4, sort_keys=True)
with open('musicapisearchrelax.json') as relax:
    datarelax = json.loads(relax.read())
##################################################################################################################################################

##################################################################################################################################################
#gets the music for work playlist
if os.path.exists('musicapisearchwork.json') == True:
    os.remove('musicapisearchwork.json')
limit = "100"
tag = "disco"
url = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit=20&api_key=7d02f117f44c9fcc4205c77ef98e6288&format=json"
similar = "https://ws.audioscrobbler.com/2.0/?method=tag.getsimilar&tag="+tag+"&api_key="+apiK+"&format=json"
#call API
responsework = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit="+limit+"&api_key="+apiK+"&format=json")
resultwork = json.loads(responsework.text)
with open('musicapisearchwork.json', 'w') as outfilework:
         json.dump(resultwork, outfilework, indent=4, sort_keys=True)
with open('musicapisearchwork.json') as work:
    datawork = json.loads(work.read())
##################################################################################################################################################

##################################################################################################################################################
#gets the music for workout playlist
if os.path.exists('musicapisearchworkout.json') == True:
    os.remove('musicapisearchworkout.json')
limit = "100"
tag = "disco"
url = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit=20&api_key=7d02f117f44c9fcc4205c77ef98e6288&format=json"
similar = "https://ws.audioscrobbler.com/2.0/?method=tag.getsimilar&tag="+tag+"&api_key="+apiK+"&format=json"
#call API
responseworkout = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit="+limit+"&api_key="+apiK+"&format=json")
resultworkout = json.loads(responseworkout.text)
with open('musicapisearchworkout.json', 'w') as outfileworkout:
         json.dump(resultworkout, outfileworkout, indent=4, sort_keys=True)
with open('musicapisearchworkout.json') as workout:
    dataworkout = json.loads(workout.read())
##################################################################################################################################################

##################################################################################################################################################
#gets the music for sunny playlist
if os.path.exists('musicapisearchsunny.json') == True:
    os.remove('musicapisearchsunny.json')
limit = "100"
tag = "disco"
url = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit=20&api_key=7d02f117f44c9fcc4205c77ef98e6288&format=json"
similar = "https://ws.audioscrobbler.com/2.0/?method=tag.getsimilar&tag="+tag+"&api_key="+apiK+"&format=json"
responsesunny = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit="+limit+"&api_key="+apiK+"&format=json")
resultsunny = json.loads(responsesunny.text)
with open('musicapisearchsunny.json', 'w') as outfilesunny:
         json.dump(resultsunny, outfilesunny, indent=4, sort_keys=True)
with open('musicapisearchsunny.json') as sunny:
    datasunny = json.loads(sunny.read())
##################################################################################################################################################

##################################################################################################################################################
#gets the music for rain playlist
if os.path.exists('musicapisearchrain.json') == True:
    os.remove('musicapisearchrain.json')
limit = "100"
tag = "disco"
url = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit=20&api_key=7d02f117f44c9fcc4205c77ef98e6288&format=json"
similar = "https://ws.audioscrobbler.com/2.0/?method=tag.getsimilar&tag="+tag+"&api_key="+apiK+"&format=json"
responserain = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit="+limit+"&api_key="+apiK+"&format=json")
resultrain = json.loads(responserain.text)
with open('musicapisearchrain.json', 'w') as outfilerain:
         json.dump(resultrain, outfilerain, indent=4, sort_keys=True)
with open('musicapisearchrain.json') as rain:
    datarain = json.loads(rain.read())
##################################################################################################################################################

iter = 0
while iter <= int(float(limit)):

    try:
        artistName = datarelax['tracks']['track'][iter]['artist']['name']
        songName = datarelax['tracks']['track'][iter]['name']
        # print(iter, " ", artistName, songName)
        headers = {"Authorization": "Bearer " + token, "Accept": "application/json", "Content-Type": "application/json"}
        url = "https://api.spotify.com/v1/search?q=track:"+songName+"%20artist:"+artistName+"&type=track"
        response = requests.get(url, headers=headers)
        #print("got passed the spotify api call")
        json_data= json.loads(response.text)
        with open('search.json', 'w') as outfile:
            json.dump(json_data, outfile,indent=4, sort_keys=True)
        with open('search.json') as infile:
            data = json.loads(infile.read())
        # print(data['tracks']['href'])
        track_uri = data['tracks']['items'][0]['uri']
    except IndexError:
        iter=iter+1
        pass
        continue
    # print(iter, " ",track_uri)
    track_ids.append(track_uri)
    iter= iter+1

#print( "TRACK IDS: ",track_ids)
sp = spotipy.Spotify(auth=token)
sp.trace = False
results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
# print(results)
outfiletop.close()
top.close()
#create a value for the signature to hash / print for decoding purposes
sig = apiKey+apiSecret+str(unixTime)
#print("signature before md5 hash: ", sig)

#hashes the signature for the API call
m.update(sig.encode('utf8'))
hashed = m.hexdigest()

#print hashed values to know if it is matching
#print("hashed value", hashed)

#call API
response = requests.get("http://api.rovicorp.com/data/v1/album/moods?apikey="+apiKey+"&sig="+hashed+"&albumid=MW0000111184")
status = response.status_code
response_text = response.text

#figure out how to get back JSON data
#parse said data to get just the song name and artist name
# Print the content of the response (the data the server returned)
#print(response.content)
