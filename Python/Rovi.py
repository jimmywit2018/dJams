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

scope = "playlist-modify-public"
username = 'h0m596l5gz014wayiyy29p0gg'
#create and assign apiKey and apiSecret values
apiKey="u8b9c5u6cwwt3mnns9ubdah6"
apiSecret = "gwGXJdarNB"
apiK= "7d02f117f44c9fcc4205c77ef98e6288"
apiS= "2fbb022389b40a3d6efcc9faf23432aa"
client_id = 'b7642ea152d44cbf95e9d7efd223cc49'
client_secret = '1094e61f08a845a6b1e9a651fe9a1e2b'
track_ids=[]
#hardcoded playlistid for now

playlist_id = "spotify:user:h0m596l5gz014wayiyy29p0gg:playlist:4wzIR8MBz1jDxritbIHcDD"
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret = client_secret , redirect_uri="http://google.com/")

sp = spotipy.Spotify(auth=token)
#set up hash
m = hashlib.md5()

#create url variables for every type of api call

#get unix time as an integer so there are no decimals,
#possibly print for decoding purposes
unixTime = int(time.time())
#print(unixTime)
if os.path.exists('musicapisearchtop.json') == True:
    os.remove('musicapisearchtop.json')
limit = "100"
tag = "disco"
url = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit=20&api_key=7d02f117f44c9fcc4205c77ef98e6288&format=json"
similar = "https://ws.audioscrobbler.com/2.0/?method=tag.getsimilar&tag="+tag+"&api_key="+apiK+"&format=json"
#call API
responsetop = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit="+limit+"&api_key="+apiK+"&format=json")
resulttop = json.loads(responsetop.text)
with open('musicapisearchtop.json', 'w') as outfiletop:
         json.dump(resulttop, outfiletop, indent=4, sort_keys=True)
with open('musicapisearchtop.json') as top:
    datatop = json.loads(top.read())
# artistName = data['tracks']['track'][0]['artist']['name']
# songName = data['tracks']['track'][0]['name']
# print(artistName, songName)

iter = 0
while iter <= int(float(limit)):

    try:
        artistName = datatop['tracks']['track'][iter]['artist']['name']
        songName = datatop['tracks']['track'][iter]['name']
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