import praw
import os

print("GROND")

reddit = praw.Reddit(
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    password=os.environ['password'],
    user_agent="USERAGENT",
    username="bot-of-grond",
)

triggers = [
    "grond",
    "gonk",
    "gronk",
    "wolf's head",
    "hound's head",
    "open the gate",
    "speak friend and enter",
    "you are soldiers of gondor",
    "hammer of the underworld",
    "morgoth's warhammer"
] #need more... ?

subreddit = reddit.subreddit("lotrmemes")

for comment in subreddit.stream.comments(skip_existing=True):
  try:
    text = comment.body.lower()

    if any(trigger in text for trigger in triggers) and comment.author != "bot-of-grond": #avoid infinite GROND chain
      comment.reply("GROND") #GROND

  except Exception as exception:
    print(exception) #evil code that stinks

    
