from flask import Flask, request, redirect
import twilio.twiml
import requests
from pymongo import MongoClient
 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def respond():
    resp = twilio.twiml.Response()
    resp.message('hello')
    return str(resp)

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

if __name__ == "__main__":
    app.run(debug=True)