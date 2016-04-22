from flask import Flask, request, redirect
import twilio.twiml
import requests
from pymongo import MongoClient
import threading
import time
from twilio.rest import TwilioRestClient
import sys
from src.reddit_post import *
from db.database import *
from src.reddit_quality_control import *
 
app = Flask(__name__)

ACCOUNT_SID = "AC2211707adb4cde52955bca7cfa0db513" 
AUTH_TOKEN = "4231c1beb1058d77cda8cab30fe95895" 
 
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
            print 'success', '\t', r
            post_id = post_to_reddit(r, message)
            activate(from_number, post_id)
            resp.message("Your request has been submitted! We will text you back when your response is ready.")
            t = threading.Timer(10.0, handle_request, [post_id, 0])
            t.start()


    return str(resp)

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

def handle_request(post_id, time):
    r = login()
    comment = get_most_upvoted_comment(r, post_id)

    if comment is None and time < 60:
        time += 10
        t = threading.Timer(10.0, handle_request, [post_id, time])
        t.start()
        return None
    elif comment is None and time >= 60:
        number = user_number(post_id)
        message = client.messages.create(to=number, from_="+12674600904", \
            body="We were not able to get a response for you.\nWe have cancelled your request due to lack of responses. Text again to submit a new message request")
        deactivate(number)
    else:
        number = user_number(post_id)
        response = comment[0] + "\nText again to submit a new message request"
        message = client.messages.create(to=number, from_="+12674600904", body=response)
        deactivate(number)

if __name__ == "__main__":
    app.run(debug=True)