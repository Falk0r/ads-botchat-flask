from pymongo import MongoClient
from keys import keys
from bson import ObjectId
client = MongoClient()
client = MongoClient(keys.mongodb['dbURI'])

mydb = client['ads']
dbLinks = mydb['links']

def getAllLinks():
    """
    Get All links
    """
    links = list(dbLinks.find())
    return links

def findLink(id):
    """
    Find one link with ID
    """
    link = dbLinks.find_one({"_id" : ObjectId(id)})
    print(link)
    if link:
        return link["url"]
    else:
        return False

def addLink(ad, user):
    """
    Add a new link for ad url with user's id.
    """
    newLink = dbLinks.insert_one({
        "user"  : str(user["_id"]),
        "url"   : ad["url"]
    }).inserted_id
    newId = newLink
    if newId:
        return newId
    else:
        return False

