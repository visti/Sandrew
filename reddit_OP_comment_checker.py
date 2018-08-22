import praw
import datetime
import time

def main():
    reddit = praw.Reddit(client_id='T80z6DeG_mJL7A',
                        client_secret='nYV5dPqc94rPLkRaYjr1QNWDxSo',
                        password='klonklon',
                        username='guitar_remover_bot',
                        user_agent='my user agent')

    target_subreddit = reddit.subreddit('7330313')

    username = 'guitar_remover_bot'
                        
    current_time=datetime.datetime.now()
    current_time=current_time.replace(second=0,microsecond=0)

    while True:
        for submission in target_subreddit.new(limit=100):
            submission_checker(submission, username)
        time.sleep(60)


def submission_checker(submission, username):
        comment_authors=[]
        print("THREAD TITLE: " + "\"" + submission.title + "\"")
        thread_age = datetime.datetime.now(datetime.timezone.utc).timestamp()-submission.created_utc
        thread_age = thread_age/60
        print(str(thread_age).split(".")[0] + " mins old.")
        
        for top_level_comment in submission.comments:
                comment_authors.append(top_level_comment.author.name)
                
        print( "OP = " + str(submission.author))
        print("Commenters: " + str(comment_authors) + "\n")
        
        if submission.author in comment_authors:
            print("## OP Commented. ##\n\n")
        
        if thread_age > 30:
            if submission.author not in comment_authors:
                print("## Thread overdue. ##\n## OP has not commented. ## \n")
                submission.mod.remove()
                print("## Thread removed. ##")
                print("----------------------------------------------------------\n")

        if thread_age > 10:
             if submission.author in comment_authors:
                for top_level_comment in submission.comments:
                    if top_level_comment.author == username:
                        top_level_comment.mod.remove()
                        print("## Removed warning message. ##")

             if submission.author not in comment_authors:
                submission.reply("Friendly reminder that all submisssions must feature a comment from the author.\nThis submission will be removed in 20 minutes if not descriptive comment is made.")
             print("----------------------------------------------------------\n")

if __name__ == '__main__':
    main()

