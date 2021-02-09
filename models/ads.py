from pymongo import MongoClient
from keys import keys
from bson import ObjectId
from controllers.customJS import createDisplayJs

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
        "url" : ad["url"],
        "title" : ad["title"],
        "status" : "pending"
    }).inserted_id
    newId = newAd
    print("newId ", newId)
    createDisplayJs(ad, newId)
    if newAd:
        return True
    else:
        return False

def deleteAd(ad, user):
    """
    Delete an ad for the ID's user and ID's ad
    """
    removeAd = dbAds.delete_one({
        "user" : str(user["_id"]),
        "_id" : ObjectId(ad)
    })
    removeAd
    print(removeAd)
    if removeAd:
        return True
    else:
        return False

def updateAd(ad, user):
    """
    Update an ad for the ID's user and ID's ad
    """
    print(ad)
    updateValue = { "$set" : {
        "text": ad["text"],
        "image": ad["image"],
        "url": ad["url"],
        "title": ad["title"],
        "status": ad["status"]
    }}
    updatingAd = dbAds.update_one({
        "user" : str(user["_id"]),
        "_id" : ObjectId(ad["_id"])
    }, updateValue)
    updatingAd
    if updatingAd:
        return True
    else:
        return False