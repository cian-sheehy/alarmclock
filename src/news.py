import praw

reddit = praw.Reddit(("bot"), user_agent=("Retrieve news for Alarm v1"))

def getNews():
    lst = []
    for submission in reddit.subreddit("UpliftingNews").hot(limit=3):
        lst.append(submission.title)
    myNews = (".\n").join(lst)
    return myNews
