#Call this using a crontab on your server with the following settings to run once per minute:
#* * * * * cd ~/python/reddit_script_template/src; reddit_script_template.py

#If you don't own a server, consider using vagrant https://www.vagrantup.com/intro/getting-started/
#* * * * * cd /vagrant/reddit_script_template/src; reddit_script_template.py

import praw
import re
import datetime

def login():
    reddit = praw.Reddit('reddit_script_template')
    return reddit

def run(r):
    subreddit = r.subreddit("YourSubreddit")

    #Checks the top 5 posts in the "hot" category in the subreddit
    num_posts_to_check = 5

    regex_pattern = re.compile("text to reply to", re.IGNORECASE)

    for submission in subreddit.hot(limit=num_posts_to_check):
        #Replaces the "more comments" objects in the comments field
        submission.comments.replace_more(limit=0)
        comment_list = submission.comments.list()

        for comment in comment_list:
            comment_text = str(comment.body)
            time_now = datetime.datetime.utcnow()
            comment_time = datetime.datetime.utcfromtimestamp(comment.created_utc)
            time_since = (time_now - comment_time).total_seconds()
            check_some_regex = re.search(regex_pattern, comment_text)
            #If comment is less than a minute old and contains the pattern we want
            #We use a minute because we set our cron job to run once a minute
            if time_since <= 60 and check_some_regex:
                comment.reply("replying to text to reply to")

run(login())
