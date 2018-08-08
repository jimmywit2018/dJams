import pymongo
from pymongo import MongoClient
from pprint import pprint
import json

##################################################################################################################################################
#sets up the connection to mongodb
client = pymongo.MongoClient("mongodb+srv://dannyzidelis:DJAMSdurga1!@djamscluster-u6bx0.mongodb.net/dJamsDB")

db = client.dJamsDB

coll_pref = db.MusicPref
##################################################################################################################################################

##################################################################################################################################################
#gets all the preference responses from the survey responses
with open(r'C:\Users\zidel\Documents\GitHub\dJams\templates\example.json') as infile:
     example = json.loads(infile.read())
email = example['email'][0]
username = example['Username']
types = example['types'][0]
sunnylisten = example['sunnylisten'][0]
sunnymood = example['sunnymood'][0]
rainylisten = example['rainylisten'][0]
rainymood = example['rainymood'][0]
cloudylisten = example['cloudylisten'][0]
cloudymood = example['cloudymood'][0]
workout = example['workout'][0]
working = example['working'][0]
relaxing = example['relaxing'][0]
##################################################################################################################################################

##################################################################################################################################################
#enters all the responses from the survey responses to the db collection music preference
pref_rec = {"username":username,
                "email": email,
                "types": types,
                "sunnylisten": sunnylisten,
                "sunnymood": sunnymood,
                "rainylisten": rainylisten,
                "rainymood": rainymood,
                "cloudylisten": cloudylisten,
                "cloudymood":cloudymood,
                "workout": workout,
                "working": working,
                "relaxing": relaxing
                }
rec_id = coll_pref.insert_one(pref_rec)
##################################################################################################################################################
