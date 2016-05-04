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
from src.grammar_control import *
 
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
    	resp.message(
            "Hi. Welcome to the txt-message hotline.\nWhat is the message that you are trying to respond to?\n(Please send request as one single text)")
    else:
    	if (user_active(from_number)):
            print "user is active"
            reddit_user = user_has_voted(from_number)
            print reddit_user
            if reddit_user != None:
                if message.isdigit() and float(message) >= 0.0 and float(message) <= 5.0:
                    if not check_if_reddit_user_exists(reddit_user):
                        print "creating reddit user"
                        create_reddit_user(reddit_user)
                    update_quality_reddit_user(reddit_user, quality)
                    print "updated quality " + message
                    remove_user(from_number)
                    message = client.messages.create(to=number, from_="+12674600904", \
                        body="Thank you for your response. We're always here to help!")
                else:
                    print "vote is not valid"
                    message = client.messages.create(to=number, from_="+12674600904", \
                        body="Please rate the response. We are trying to improve our service.")
            else:
                print 'this is not a vote message'
                resp.message("Hang tight. We are working on your response.")
            sys.stdout.flush()

    	else:
            print ' we are trying to log you in'
            reddit = login()
            print 'success', '\t', reddit
            
            message = censor_sentence(message)

            title = ""

            if len(message) > 100:
                title = message[:100] + "..."
            else:
                title = message
            
            
            message = message + '''
            
            Please help this person answer to this message. Write something useful and no swearing please'''
            post_id = post_to_reddit(reddit, message, title)
            print 'post_id', '\t', post_id
            activate(from_number, post_id)
            resp.message("Your request has been submitted! We will text you back when your response is ready.")
            t = threading.Timer(30.0, handle_request, [post_id, str(0)])
            t.start()
            sys.stdout.flush()


    return str(resp)

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

def handle_request(post_id, time):
    r = login()
    time = int(time)
    comment = get_most_upvoted_comment(r, post_id)
    comments = get_comments_in_order(r, post_id)

    if comment is None and time < 60:
        time += 30
        t = threading.Timer(30.0, handle_request, [post_id, str(time)])
        t.start()
        return None
    elif comment is None and time >= 60:
        number = user_number(post_id)
        message = client.messages.create(to=number, from_="+12674600904", \
            body="We were not able to get a response for you.\nWe have cancelled your request due to lack of responses. Text again to submit a new message request")
        remove_user(number)
    else:
        number = user_number(post_id)
        response = ""
        author = ""
        for single_comment in comments:
            author = single_comment[2]
            if not check_if_reddit_user_exists(author):
                create_reddit_user(author)
            if not check_if_reddit_user_has_votes(author):
                response = single_comment[0]
                break
            quality = get_quality_reddit_user(author)
            if quality >= 3.0:
                response = single_comment[0]
                break

        if response == "" and time >= 60:
            message = client.messages.create(to=number, from_="+12674600904", \
            body="We were not able to get a response for you.\nWe have cancelled your request due to lack of responses. Text again to submit a new message request")
            remove_user(number)
        elif response == "":
            time += 30
            t = threading.Timer(30.0, handle_request, [post_id, str(time)])
            t.start()
        else:
            pre_message = client.messages.create(to=number, from_="+12674600904", \
                body="This is the response that the crowd has created for you:")
            message = client.messages.create(to=number, from_="+12674600904", body=response)
            post_message = client.messages.create(to=number, from_="+12674600904", \
                body="Rate your response with a number between 1 (awful) and 5 (awesome)")
            activate_user_vote(number, author)
            # start new thread to check if they respond
            

if __name__ == "__main__":
    app.run(debug=True)