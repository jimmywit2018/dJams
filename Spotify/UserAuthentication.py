import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
username= input("Enter user name: ")

with open ('clientID.txt', 'rt') as in_file:
    client_id = in_file.read()
with open ('clientSecret.txt', 'rt') as in_file:
    client_secret = in_file.read()
token = util.prompt_for_user_token(username, scope, client_id="b7642ea152d44cbf95e9d7efd223cc49", client_secret , redirect_uri="http://localhost:8888/callback/")
print(client_id)
print(contents_client_id)
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)
