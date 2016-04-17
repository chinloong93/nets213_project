from pymongo import MongoClient
from datetime import datetime
#from ..credentials import db_url

client = MongoClient("mongodb://admin:password@ds039000.mlab.com:39000/heroku_d7ctc0xz")
db = client.get_default_database()

# Checks whether the user exists in the database
def user_exists(number):
    cursor = db.users.find({ "user.number": number })
    if cursor.count() > 0:
        return True
    else:
        return False

# Add an inactive user to the database
def add_user(number):
    db.users.insert( { "user": {"number":number, "active": "" } } )

# Activate user by adding a post id to the database
def activate(number, postId):
    # Get cursor
    db.users.update(
        { "user.number": number }, { "user": { "number":number, "active":postId } } )

# Deactivate user by removing a post from the database
def deactivate(number):
    # Get cursor
    db.users.update( { "user.number": number }, { "user": { "number":number, "active":"" } } )

# Checks whether the user has an active post
def user_active(number):
    cursor = db.users.find( { "user.number": number } )
    for elt in cursor:
        if elt['user']['active'] == '':
            return False
        else:
            return True