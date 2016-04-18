from flask import Flask, request, redirect
import twilio.twiml
import requests
from pymongo import MongoClient
import threading
import time
from twilio.rest import TwilioRestClient
from src.reddit_post import *
from db.database import *
from src.reddit_quality_control import *
 
app = Flask(__name__)

ACCOUNT_SID = "AC2211707adb4cde52955bca7cfa0db513" 
AUTH_TOKEN = "5a94478226313be17001a52be80f8b33" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

@app.route("/", methods=['GET', 'POST'])
def respond():
    from_number = request.values.get('From', None)
    message = request.values.get('Body', None)

    resp = twilio.twiml.Response()

    if (not user_exists(from_number)):
    	add_user(from_number)
    	resp.message("Hi. Welcome to the txt-message hotline.\nWhat is the message that you are trying to respond to?")
    else:
    	if (user_active(from_number)):
                resp.message("Hang tight. We are working on your response")
                # possibly add url to reddit
    	else:
            r = login()
            post_id = post_to_reddit(r, message)
            activate(from_number, post_id)
            resp.message("Your request has been submitted! We will text you back when your response is ready.")
            t = threading.Timer(10.0, handle_request, [post_id])
            t.start()


    return str(resp)

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

def handle_request(post_id):
    r = login()
    comment = get_most_upvoted_comment(r, post_id)

    if comment is None:
        t = threading.Timer(10.0, handle_request, [post_id])
        t.start()
        return None
    else:
        number = user_number(post_id)
        message = client.messages.create(to=number, from_="+12674600904", body=comment)
        deactivate(number)

if __name__ == "__main__":
    app.run(debug=True)