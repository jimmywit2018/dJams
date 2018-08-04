import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import spotipy.util as util
import requests

scope = "user-read-private"
username = 'h0m596l5gz014wayiyy29p0gg'
search_str = 'Radiohead'
search_str = input("Enter name of artist you would like to search?  ")
#if len(sys.argv) > 1:
 #   search_str = sys.argv[1]
#else:
 #   search_str = 'Fall Out Boy'

client_id = "b7642ea152d44cbf95e9d7efd223cc49"
client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b"
token = util.prompt_for_user_token(username, scope, client_id="b7642ea152d44cbf95e9d7efd223cc49", client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b" , redirect_uri="http://google.com/")
#client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
#sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#call API
sp = spotipy.Spotify(auth=token)
print(token)
headers = {"Authorization": "Bearer " + token, "Accept": "application/json", "Content-Type": "application/json"}
#url = 'https://api.spotify.com/v1/search?q=track:%20artist:bieber&type=track&Authorization:'
response = requests.get("https://api.spotify.com/v1/search?q=track:despacito%20artist:bieber&type=track", headers=headers)
#print("https://api.spotify.com/v1/search?q=track:%20artist:bieber&type=track&Authorization: Bearer " + token)
#headers = {'Authorization: Bearer BQDGm5E3KcVPrn74WjOpGMqyx_sWkgJZBvriHVP5Wy6In1gy25lQP-qA3dJL6I3rV5CPr6jwqyMniJvamItVnbFqG1rLII-mkuD6dU6rEiOYTg8WX9cg4yhBmO_8wEHOCbDr5TL2g0Vn1irXis1YGNPZD2VWRvG8Hh9Yv2-kG_5C_gB89KoHDW_PfaM'}
#r = requests.post(url,headers=headers)
print(response)
print(response.text)
#print("hello")
#result = sp.search(search_str)
#pprint.pprint(result)
