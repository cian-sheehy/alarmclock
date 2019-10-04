import praw

reddit = praw.Reddit(("bot"), user_agent=("Retrieve news for Alarm v1"))


def getNews():
    lst = []
    for submission in reddit.subreddit('worldnews').hot(limit=5):
        if "trump" not in submission.title.lower():
            lst.append(submission.title)
    myNews = (".\n").join(lst)
    return myNews