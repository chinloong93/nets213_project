from flask import Flask, request, redirect
import twilio.twiml
import requests
from pymongo import MongoClient
 
app = Flask(__name__)

#MongoDB client
client = MongoClient("yoursecret")
db = client.get_default_database()

@app.route("/", methods=['GET', 'POST'])
def respond():
    from_number = request.values.get('From', None)
    name = request.values.get('Body', None)

    db.users.insert({from_number:name})

    resp = twilio.twiml.Response()
    resp.message('hello '+from_number)
    return str(resp)

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

if __name__ == "__main__":
    app.run(debug=True)