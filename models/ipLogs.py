from pymongo import MongoClient
from keys import keys
import datetime

client = MongoClient()
client = MongoClient(keys.mongodb['dbURI'])

mydb = client['ads']
dbIpLogs = mydb['ip-logs']

def addIpLogs(tracking, link):
    now = datetime.datetime.now()
    newIpLog = dbIpLogs.insert_one({
        "linkId"    : link,
        "date"      : now,
        "address_ip" : tracking["address_ip"],
        "agent"     : tracking["agent"],
        "origin"    : tracking["origin"]
    })
    newLog = newIpLog
    if newLog:
        return True
    else:
        return False