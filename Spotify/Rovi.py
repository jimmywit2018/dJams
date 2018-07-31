import requests
#create url variables for every type of api call

#make a get request to get the music of mood happy?
response = requests.get("http://api.rovicorp.com/data/v1.1/descriptor/significantsongs?apikey=u8b9c5u6cwwt3mnns9ubdah6&sig=sig&genreids=MA0000002533,MA0000002960")

print(response.status_code)

#figure out how to get back JSON data

#parse said data to get just the song name and artist name

# Print the content of the response (the data the server returned)
print(response.content)
