from pymongo import MongoClient
from keys import keys

client = MongoClient()
client = MongoClient(keys.mongodb['dbURI'])

mydb = client['ads']
dbAds = mydb['ads']


def getAllAds(id):
    """
    Get All Ads from an user with id
    """
    ads = list(dbAds.find({"user" : id}))
    for ad in ads:
        ad['_id'] = str(ad['_id'])
    return ads

def addAd(ad, user):
    """
    Add an ad for the ID's user
    """
    newAd = dbAds.insert_one({
        "user" : str(user["_id"]),
        "text" : ad["text"],
        "image" : ad["image"],
        "url" : ad["url"]
    }).inserted_id
    newAd
    if newAd:
        return True
    else:
        return False