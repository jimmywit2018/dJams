import pymongo
from pymongo import MongoClient
from pprint import pprint

client = pymongo.MongoClient("mongodb+srv://dannyzidelis:THEbigZ1!@djamscluster-u6bx0.mongodb.net/dJamsDB")

db = client.dJamsDB

coll = db.dataset

print(client.database_names())
print(coll)
