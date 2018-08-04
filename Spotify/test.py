# shows artist info for a URN or URL
import spotipy.util as util
import spotipy
import sys
import pprint

scope = "user-read-private"
username = "h0m596l5gz014wayiyy29p0gg"
search_str = 'Radiohead'
token = util.prompt_for_user_token(username, scope, client_id="b7642ea152d44cbf95e9d7efd223cc49", client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b" , redirect_uri="http://google.com/")

sp = spotipy.Spotify()
result = sp.search(search_str)
pprint.pprint(result)
