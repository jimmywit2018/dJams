import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
username= input("Enter user name: ")
#if len(sys.argv) > 1:
#    username = sys.argv[1]
#else:
#    print("Usage: %s username" % (sys.argv[0],))
#    sys.exit()
with open ('clientID.txt', 'rt') as in_file:
    contents = in_file.read()
    print(contents)
#something is up with the userauthentication
token = util.prompt_for_user_token(username, scope, client_id = "b7642ea152d44cbf95e9d7efd223cc49", client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b", redirect_uri="http://google.com/")

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)
# scopes = 'user-read-private user-read-email';
# res.redirect('https://accounts.spotify.com/authorize' +
#   '?response_type=code' +
#   '&client_id=' + my_client_id +
#   (scopes + encodeURIComponent(scopes) : '') +
#   '&redirect_uri=' + encodeURIComponent(redirect_uri));
