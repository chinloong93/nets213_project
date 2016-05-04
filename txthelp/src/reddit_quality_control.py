import praw
#from ..credentials import app_secret, app_refresh

app_id = 'RcDWOGZcajoyHg'
app_uri = 'https://help-text.herokuapp.com/authorize_callback'
app_ua = 'try something new'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'reWp15hGNfrB6YG_NhDyfi8W4RA'

def login2():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, 'NQ-k-lhh8leMTOiQwPw-ji12kWE', app_uri)
    print 'set oauth app'
    r.refresh_access_information('11799219-t3T0HETO75UoWwO3vNmNIYt7YPo')
    return r

def top_posts(r):
    submissions = r.get_subreddit('txthotline').get_top(limit=10)
    return list(submissions)

def get_comments(r, post_id):
    comments = r.get_comments(post_id)
    return comments

def get_submission(r, post_id):
    return r.get_submission(url=None, submission_id=post_id, comment_limit=0, comment_sort=None, params=None)

def get_most_upvoted_comment(r, post_id):
    post = get_submission(r, post_id)
    if len(post.comments) > 0:
        comment = post.comments[0]
        most_upvoted_string = str(comment) + '\t' +  str(comment.id) + '\t' + str(comment.score)
        return [str(comment), str(comment.score), str(comment.author.name)]
    else:
        return None

def get_comments_in_order(r, post_id):
    post = get_submission(r, post_id)
    if len(post.comments) > 0:
        comment_array = []
        for comment in post.comments:
            comment_array.append([str(comment), str(comment.score), str(comment.author.name)])
        return comment_array
    else:
        return None


if __name__ == "__main__":
    r = login2()
    top_posts = top_posts(r)
    for post in top_posts:
        #comment = get_most_upvoted_comment(r, post.id)
        #print comment
        print get_comments_in_order(r, post.id)
        # flat_comments = praw.helpers.flatten_tree(post.comments)
        # for comment in flat_comments:
        #     print comment,'\t', comment.id, '\t', comment.score

         