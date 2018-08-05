import sys
import pprint
import requests

apiK= "7d02f117f44c9fcc4205c77ef98e6288"
apiS= "2fbb022389b40a3d6efcc9faf23432aa"

#call API
responsetop = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=disco&limit=2&api_key="+apiK+"&format=json")
responseweek = requests.get("https://ws.audioscrobbler.com/2.0/?method=tag.getweeklychartlist&tag=disco&api_key="+apiK+"&format=json")
print(responsetop.status_code)
print(responsetop.text)
print(responseweek.status_code)
print(responseweek.text)
