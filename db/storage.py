from pymongo import MongoClient


#MongoDB client
client = MongoClient("mongodb://admin:password@ds039000.mlab.com:39000/heroku_d7ctc0xz")
db = client.get_default_database()

assert db.name = 'comment_data'

#Pushes string of comment data to MongoDB
#string input must include post_id, comment_id, comment_body, 
#and comment_upvotes
def store(comm_str):
	comment_object = json.loads(comm_str)

	db.comment_data.insert(
		{ 
			comment_object[post_id]:
				{
				comment_object[comment_id]:
				{
					"comment_body":comment_object[comment_body],
					"comment_upvotes":comment_object[comment_upvotes]
				}
			}
		}
	)

