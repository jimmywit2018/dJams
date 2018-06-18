import sys
import spotipy
import spotipy.util as util
import simplejson as json

scope = 'user-library-read'
username= input("Enter user name: ")

#with open ('clientID.txt', 'rt') as in_file:
#    client_id = in_file.read()
#with open ('clientSecret.txt', 'rt') as in_file:
#    client_secret = in_file.read()
token = util.prompt_for_user_token(username, scope, client_id="b7642ea152d44cbf95e9d7efd223cc49", client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b" , redirect_uri="http://google.com/")

if token:
    sp = spotipy.Spotify(auth=token)
    print("You have successsfully linked dJbeats to your spotify account")
    sp.trace = False
    results = sp.current_user_playlists(limit=50)
    for i, item in enumerate(results['items']):
        print("%d %s" %(i, item['name']))
else:
    print("Can't get token for", username)
