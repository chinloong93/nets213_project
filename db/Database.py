from pymongo import MongoClient
from datetime import datetime


client = MongoClient("yoursecret")
db = client.get_default_database()


db.users.insert({'house':'cool'})


    #def getFromDatabase(number):
    #    if (db.user.find())
