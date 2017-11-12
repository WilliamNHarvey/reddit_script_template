#Call this using a crontab on your server with the following settings to run once a day:
#0 1 * * * kill myredditbot; cd ~/python/reddit_script_template/src; exec -a myredditbot python reddit_script_template.py
#This command stops the bot, then restarts it forcing it to relog in.

#If you don't own a server, consider using vagrant https://www.vagrantup.com/intro/getting-started/
#0 1 * * * kill myredditbot; cd /vagrant/reddit_script_template/src; exec -a myredditbot python reddit_script_template.py

import praw
import re
import datetime

r = praw.Reddit('reddit_script_template')

def run():
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
            #If comment is less than 15 seconds old and contains the pattern we want
            #15 seconds is how long we sleep between checking for new comments to make
            if time_since <= 15 and check_some_regex:
                comment.reply("replying to text to reply to")

def main():
    while(1):
        run()
        time.sleep(15)

if __name__ == '__main__':
    main()
