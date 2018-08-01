import requests
import json

#use playlistid to get the playlist uri which is what is needed for the spotify playlist?
response = requests.get("https://api.spotify.com/v1/users/h0m596l5gz014wayiyy29p0gg/playlists/59ZbFPES4DQwEjBpWHzrtC")
print(response.status_code)
