# NETS213 Final Project Code
1. Our backend is written in Python using the Flask framework.
2. Our server, which accepts HTTP GET/POST requests, is hosted on Heroku.
3. Our database is a MongoDB database which stores a document containing a user's phone number and a users status to indicate whether the user has a request to satisfy. If the user is inactive, the active field is an empty string else the field is the ID of the post we need to respond to
4. Our app leverages the TwilioAPI and Reddit API to send text messages to our users and to post users request to Reddit respectively.
5.  When our server receives a request it does the following based on different conditions:
 * If the user has not used our service before, the new user's phone number is stored in our database and the user is marked as 'inactive'. Then, using the Twilio API, our server sends a text message to the user prompting him to reply to our server with his/her request.
 * If the user has used our service before and is 'inactive', we process the user's request and submit a post to Reddit to gather responses. We then get the id of the post we have submitted to Reddit using the Reddit API and set the active field of the user to the id of the Reddit post. Next, we start a thread which would query the post for its most upvoted comment every 30 minutes. If the comment satisfies our quality control, that comment would be sent to the user using the Twilio API, the running thread is killed and the user's status will be set to 'inactive' in the database. If the comment does not satisfy our quality control, the thread will query Reddit again in 30 minutes.
 * If the user has used our services before and is 'active'. We will send the user a text message telling the user that we are currently processing his/her request.

