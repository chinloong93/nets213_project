from pymongo import MongoClient
from datetime import datetime


client = MongoClient("mongodb://admin:password@ds039000.mlab.com:39000/heroku_d7ctc0xz")
db = client.get_default_database()


db.users.insert({'house':'cool'})


    #def getFromDatabase(number):
    #    if (db.user.find())
