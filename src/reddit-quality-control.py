import praw

app_id = 'RcDWOGZcajoyHg'
app_secret = 'yoursecret'
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_ua = 'description of the text'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'sl5YGDVzOPkolZ7vMi7HB26F0B8'
app_refresh = 'yoursecret'

def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r

def top_posts(r):
    submissions = r.get_subreddit('txthotline').get_top(limit=10)
    return list(submissions)

def get_comments(r, post_id):
    comments = r.get_comments(post_id)
    return comments

def get_submission(r, post_id):
    return r.get_submission(url=None, submission_id=post_id, comment_limit=0, comment_sort=None, params=None)

def get_most_upvoted_comment(r, post):
    if len(post.comments) > 0:
        comment = post.comments[0]
        most_upvoted_string = str(comment) + '\t' +  str(comment.id) + '\t' + str(comment.score)
        return most_upvoted_string
    else:
        return 'no comments yet'


if __name__ == "__main__":
    r = login()
    top_posts = top_posts(r)
    for post in top_posts:
        comment = get_most_upvoted_comment(r, post)
        print comment
        # flat_comments = praw.helpers.flatten_tree(post.comments)
        # for comment in flat_comments:
        #     print comment,'\t', comment.id, '\t', comment.score

         