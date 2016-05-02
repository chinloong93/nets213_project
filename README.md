# NETS213 Final Project
## Milestone 1: Set up server *4pts*
* ~~Create server using Flask hosted on Heroku~~ 
* ~~Handle Twilio messaging request~~
* ~~Set up database to store phone number, request id etc.~~

## Milestone 2: Post to crowdsourcing platform (Aggregation Module) *4pts*
* ~~Parse request from user~~
* ~~Store request in database~~
* ~~Post request to Reddit~~

## Milestone 3: Check highest quality response (QC Module) *4pts*
* ~~Allow time to gather response (30 minutes)~~ *Used threads*
* ~~Choose the top n upvoted response on reddit~~
* ~~Check for results with valid English grammar and store the results in a database~~
* Allow message requester to rate response

## Milestone 4: Response to user *4pts*
* ~~Pull data from database~~
* ~~Notify users of top n results~~

## Project updates:
### Quality Control Module:
Since we are using Reddit as our quality control tool, our sample data is simply a set of fake posts that we have created in the following subreddit: [txt-hotline](https://www.reddit.com/r/txthotline).
We will pick the most upvoted comment in a post as the response to the "message help" request.
##### TODO:
* Before sending the message to the "message help" requester, we need to parse this most upvoted comment to check if it's actually meaningful.
* We also need to make sure that the "message help" requester does some QC himself/herself. He/she will be able to flag a certain "message help" response and get the next upvoted comment.

### Aggregation module
Aggregation also happens within Reddit. People post comments ("message help" responses) to a particular post ("message help" text). The top 25 will always be stored in the database and updated at specific time intervals.
##### TODO:
* We have a function that can push comments to the database, but we want this to happen automatically at specific time intervals. 
