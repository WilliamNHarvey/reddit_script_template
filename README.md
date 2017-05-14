# reddit_script_template
A template for a reddit bot built in python

In order to automate this bot, use a crontab. Instructions are written in reddit_script_template.py

View or test here: https://www.reddit.com/r/redditScriptTemplate/

# Troubleshooting
If you have trouble setting up your crontab on a web server, check which version of python your crontab is running on. Sometimes, a crontab will recognize python as an alias for the server's default python rather than your own download. This can cause issues importing the Praw module. To mediate this, use the absolute file path for your python download in your crontab command.

```which python```

=> outputs ```~/path/to/python/python27/bin/python```

new crontab:

```* * * * * ~/path/to/python/python27/bin/python ~/python/reddit_script_template/src/reddit_script_template.py```
