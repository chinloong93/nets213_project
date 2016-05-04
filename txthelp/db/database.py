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
    db.users.insert( { "user": {"number":number, "active": "", "voted":"" } } )

# Activate user by adding a post id to the database
def activate(number, postId):
    # Get cursor
    db.users.update(
        { "user.number": number }, { "user": { "number":number, "active":postId, "voted":"" } } )

# Deactivate user by removing a post from the database
def deactivate(number):
    # Get cursor
    db.users.update( { "user.number": number }, { "user": { "number":number, "active":"", "voted":"" } } )

# Remove user from database
def remove_user(number):
    db.users.remove({"user.number": number })

# Checks whether the user has an active post
def user_active(number):
    cursor = db.users.find( { "user.number": number } )
    for elt in cursor:
        if elt['user']['active'] == '':
            return False
        else:
            return True

def get_active_post(number):
    cursor = db.users.find( { "user.number": number } )
    for elt in cursor:
        if elt['user']['active'] == '':
            return None
        else:
            return elt['user']['active']

# Checks whether the user has an active post
def user_number(post_id):
    cursor = db.users.find( { "user.active": post_id } )
    for elt in cursor:
        return elt['user']['number']

# Change the state of vote for user
def activate_user_vote(number, reddit_user):
    db.users.update(
        { "user.number": number }, { "user": { "number":number, "active":"active", "voted":reddit_user } } )
    

# Check if user has voted
def user_has_voted(number):
    cursor = db.users.find({"user.number": number})
    for elt in cursor:
        if elt['user']['voted'] != "":
            return elt['user']['voted']
        else:
            return None

# creates user with 0 quality in database
def create_reddit_user(username):
    db.qualities.insert({"user": {"username": username, "quality":0.0, "votes": 0.0}})

# check if reddit user exists
def check_if_reddit_user_exists(username):
    cursor = db.qualities.find({"user.username": username})
    for elt in cursor:
        if elt['user']['username'] == username:
            return True
        else:
            return False

# check if reddit user has been graded yet
def check_if_reddit_user_has_votes(username):
    cursor = db.qualities.find({"user.username": username})
    for elt in cursor:
        if elt['user']['votes'] == 0.0:
            return False
        else:
            return True

def get_quality_reddit_user(username):
    cursor = db.qualities.find({"user.username": username})
    for elt in cursor:
        return elt['user']['quality']

# updates quality of user in db
def update_quality_reddit_user(username, quality):
    cursor = db.qualities.find({"user.username": username})
    votes = 0.0
    for elt in cursor:
        votes = elt['user']['votes']
        quality = quality + elt['user']['quality']*votes
        votes = votes + 1.0
        quality = quality/votes

    db.qualities.update(
        {"user.username": username}, {"user": {"username": username, "quality": quality, "votes": votes }})

if __name__ == "__main__":
    print user_active("+12154602034")

