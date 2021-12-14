import praw
import os

reddit = praw.Reddit(
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    password=os.environ['password'],
    user_agent="USERAGENT",
    username="bot-of-grond",
)

subreddit = reddit.subreddit("lotrmemes")

for comment in subreddit.stream.comments(skip_existing=True):
  try:
    text = comment.body.lower()
    if ("grond" in text or "gonk" in text or "wolf's head" in text or "open the gate" in text) and comment.author != "bot-of-grond":
      comment.reply("GROND")
  except Exception as exception:
    print(exception)