import requests
import json

#use playlistid to get the playlist uri which is what is needed for the spotify playlist?
json_data = requests.get("https://api.spotify.com/v1/users/h0m596l5gz014wayiyy29p0gg/playlists/3b6zyg3kZnWE18tTP04C0U").json()
print(json_data)
