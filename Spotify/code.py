import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint


if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Fall Out Boy'

client_id = "b7642ea152d44cbf95e9d7efd223cc49"
client_secret = "1094e61f08a845a6b1e9a651fe9a1e2b"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.search(search_str)
pprint.pprint(result)
