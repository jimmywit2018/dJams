import requests
import json
import time
import hashlib

#create and assign apiKey and apiSecret values
apiKey="u8b9c5u6cwwt3mnns9ubdah6"
apiSecret = "gwGXJdarNB"

#set up hash
m = hashlib.md5()

#create url variables for every type of api call

#get unix time as an integer so there are no decimals,
#possibly print for decoding purposes
unixTime = int(time.time())
#print(unixTime)

#create a value for the signature to hash / print for decoding purposes
sig = apiKey+apiSecret+str(unixTime)
print("signature before md5 hash: ", sig)

#hashes the signature for the API call
m.update(sig.encode('utf8'))
hashed = m.hexdigest()

#print hashed values to know if it is matching
#print("hashed value", hashed)

#call API
response = requests.get("http://api.rovicorp.com/data/v1/album/moods?apikey="+apiKey+"&sig="+hashed+"&albumid=MW0000111184")
print(response.status_code)
print(response.text)

#figure out how to get back JSON data
#parse said data to get just the song name and artist name
# Print the content of the response (the data the server returned)
#print(response.content)
