from flask import Flask, request, redirect
import twilio.twiml
import requests
from pymongo import MongoClient
from src.reddit_post import *
from db.database import *
 
app = Flask(__name__)

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
            login()
            post_id = post_to_reddit(message)
            activate(from_number, post_id)
            resp.message("Your request has been submitted! We will text you back when your response is ready.")

    return str(resp)

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

if __name__ == "__main__":
    app.run(debug=True)