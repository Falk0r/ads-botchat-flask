from pymongo import MongoClient
from keys import keys

client = MongoClient()
client = MongoClient(keys.mongodb['dbURI'])

mydb = client['ads']
myAds = mydb['ads']


def getAllAds():
    """
    Get All Ads from an user
    """
    ads = list(myAds.find())
    return ads