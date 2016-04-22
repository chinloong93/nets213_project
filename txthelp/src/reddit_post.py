import praw
import random
#from ..credentials import app_secret, app_refresh

app_id = 'RcDWOGZcajoyHg'
app_uri = 'https://help-text.herokuapp.com/authorize_callback'
app_ua = 'description of the text'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'sl5YGDVzOPkolZ7vMi7HB26F0B8'

def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, 'NQ-k-lhh8leMTOiQwPw-ji12kWE', app_uri)
    r.refresh_access_information('11799219-ekf0ZjFmu29aCxh7WR8VsicOxXg')
    print 'successful login','\t',r
    return r

def post_to_reddit(r, message):
    post = r.submit('txthotline', str(random.randint(0,10000000)), text=message)
    return post.id

if __name__ == "__main__":
    r = login()
    post_to_reddit(r, "hello")