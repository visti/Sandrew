import praw
import datetime
import time

def main():

	# Authenticate Reddit bot. Needs API client_id and client_secret
    reddit = praw.Reddit(client_id='',
                        client_secret='',
                        password='',
                        username='guitar_remover_bot',
                        user_agent='my user agent')

     
	# Active Subreddit for the bot
    target_subreddit = reddit.subreddit('7330313')

	# username for the bot – Used to make sure there's no duplicate warning messages
    bot_username = 'guitar_remover_bot'
                        
	
	# Getting current time and stripping it of seconds and microseconds
    current_time=datetime.datetime.now()
    current_time=current_time.replace(second=0,microsecond=0)

	# Main loop, runs every minute
    while True:
        for submission in target_subreddit.new(limit=100):
            submission_checker(submission, username)
        time.sleep(60)


# The base function that checks every submission
def submission_checker(submission, username):
		# Create list of all usernames to comment on a submission
        comment_authors=[]
        print("THREAD TITLE: " + "\"" + submission.title + "\"")
		
		# Check thread age and convert to minutes
        thread_age = datetime.datetime.now(datetime.timezone.utc).timestamp()-submission.created_utc
        thread_age = thread_age/60
        print(str(thread_age).split(".")[0] + " mins old.")
        
		# Add all current commenters to the list
        for top_level_comment in submission.comments:
                comment_authors.append(top_level_comment.author.name)
        
		# Print out submission OP and active commenters
        print( "OP = " + str(submission.author))
        print("Commenters: " + str(comment_authors) + "\n")
        
		# Print out message if OP has already replied
        if submission.author in comment_authors:
            print("## OP Commented. ##\n\n")
        
		# If the thread is older than 30 minutes:
        if thread_age > 30:
			# and OP has not replied:
            if submission.author not in comment_authors:
				# print messages to console and remove thread
                print("## Thread overdue. ##\n## OP has not commented. ## \n")
                submission.mod.remove()
                print("## Thread removed. ##")
                print("----------------------------------------------------------\n")
		
		# if thread is older than 10 minutes:
        if thread_age > 10:
			# and OP HAS replied:
             if submission.author in comment_authors:
                 for top_level_comment in submission.comments:
					# remove flair and delete warning message
                    if top_level_comment.author == bot_username:
                        submission.mod.flair("")
                        top_level_comment.delete()
                        print("## Removed warning message. ##")

			# if OP has NOT replied:			
             if submission.author not in comment_authors:
				# set flair
                 submission.mod.flair('Missing OP comment')
				 # post warning message
                 if username not in comment_authors:
                    submission.reply("Friendly reminder that all submisssions must feature a comment from the author.\nThis submission will be removed in 20 minutes if not descriptive comment is made.")
                 print("----------------------------------------------------------\n")

if __name__ == '__main__':
    main()

