from pymongo import MongoClient
from keys import keys

client = MongoClient()
client = MongoClient(keys.mongodb['dbURI'])

mydb = client['ads']
dbUsers = mydb['users']


def getAllUsers():
    """
    Get All users
    """
    users = list(dbUsers.find())
    return users

def findUser(email):
    """
    Find one user with email
    """
    user = dbUsers.find_one({"email" : email})
    print(user)
    return user

def addUser(name, email, password):
    """
    Create User with name, email and password
    """
    user = dbUsers.insert_one({
        "name" : name,
        "email": email,
        "password" : password
    })
    user
    print(user)
    return user