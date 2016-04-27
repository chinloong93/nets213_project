import praw
import random
import sys
#from ..credentials import app_secret, app_refresh

app_id = 'RcDWOGZcajoyHg'
app_uri = 'https://help-text.herokuapp.com/authorize_callback'
app_ua = 'try something new'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'reWp15hGNfrB6YG_NhDyfi8W4RA'

def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, 'NQ-k-lhh8leMTOiQwPw-ji12kWE', app_uri)
    r.refresh_access_information('11799219-t3T0HETO75UoWwO3vNmNIYt7YPo')
    print 'successful login','\t',r
    sys.stdout.flush()
    return r

def post_to_reddit(r, message):
    post = r.submit('txthotline', str(random.randint(0,10000000)), text=message)
    return post.id

if __name__ == "__main__":
    r = login()
    post_to_reddit(r, "hello")