import praw
import datetime
import time
import feedparser

def generate_existing(target_subreddit,existing_posts):
    for submission in target_subreddit.hot(limit=1000):
        existing_posts.append(submission.title)
    return existing_posts

def main():
    reddit = praw.Reddit(client_id='',
                        client_secret='',
                        password='',
                        username='guitar_remover_bot',
                        user_agent='my user agent')

    target_subreddit = reddit.subreddit('7330313')

    username = 'guitar_remover_bot'
                        
    feed = feedparser.parse('http://api.crackwatch.com/rss/cracks.xml')

    existing_posts = []



    while True:
        post_link(existing_posts, target_subreddit, username)
        time.sleep(60)


def post_link(existing_posts, target_subreddit, username):
    feed = feedparser.parse('http://api.crackwatch.com/rss/cracks.xml')

    generate_existing(target_subreddit,existing_posts)

    for post in feed.entries:
        if post.title in existing_posts:
            print(post.title + " exists!")

        if post.title not in existing_posts:
            print("Posting " + post.title)
            target_subreddit.submit(title=post.title, url=post.link)

        for queue_submission in target_subreddit.mod.modqueue(limit=None):
            if queue_submission.author == username:
                queue_submission.mod.approve()


if __name__ == '__main__':
    main()

