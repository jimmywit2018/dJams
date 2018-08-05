import sys
import pprint
import requests
import json
import urllib
from urllib.request import urlopen
#import simplejson as json


apiK= "7d02f117f44c9fcc4205c77ef98e6288"
apiS= "2fbb022389b40a3d6efcc9faf23432aa"

url = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=disco&limit=2&api_key=7d02f117f44c9fcc4205c77ef98e6288&format=json"
#call API
responsetop = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=disco&limit=2&api_key="+apiK+"&format=json")
responseweek = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.getweeklychartlist&tag=disco&api_key="+apiK+"&format=json")

result = json.loads(responsetop.text)
with open('musicapisearch.json', 'w') as outfile:
         json.dump(result, outfile, indent=4, sort_keys=True)
#print('"tracks":', result['tracks']['track']['name'])

url=urlopen("https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=disco&limit=2&api_key="+apiK+"&format=json").read()
url = json.loads(url)

#print(url.get('tracks').get('track').get('name'))
#contents = page.read()
#print(contents)
#print(responsetop.status_code)
# print(responsetop.text)
# print(responseweek.status_code)
# print(responseweek.text)
