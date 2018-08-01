import requests
import json
import time
#create url variables for every type of api call

#get unix time
unixTime = int(time.time())
apiKey="u8b9c5u6cwwt3mnns9ubdah6"
apiSecret = "gwGXJdarNB"
print(unixTime)
#make a get request to get the music of mood happy?
#response = requests.get("http://api.rovicorp.com/data/v1.1/descriptor/musicmoods?moodids=happy&country=US&language=en&format=json&apikey=u8b9c5u6cwwt3mnns9ubdah6&sig=333937bd111c422ea3e7fe67895b3898")
response = requests.get("http://api.rovicorp.com/data/v1/album/moods?apikey=u8b9c5u6cwwt3mnns9ubdah6&sig=842156e101f98b356459c08cafbec8c3&albumid=MW0000111184")
print(response.status_code)

#figure out how to get back JSON data
#parse said data to get just the song name and artist name
# Print the content of the response (the data the server returned)
#print(response.content)
