from pymongo import MongoClient
from keys import keys

client = MongoClient()
client = MongoClient(keys.mongodb['dbURI'])

mydb = client['ads']
myAds = mydb['ads']

# for ad in myAds.find():
#     print(ad)
