#!/usr/bin/env python3

import time
import praw
from urllib.parse import quote_plus
from assets.colors import red,white,yellow,reset
from config.credentials import client_secret, client_id, username, password, user_agent


class Lmgtfy:
	def __init__(self):
		self.reddit = self.authenticate()
		
		# Name of subreddit to monitor
		self.subreddit = "askscience"
		
		# List of questions 
		self.questions = ["what is", "who is", "what are","why are","why is","how do","how is","how are","when is","where is"]
		
		# Bot reply to questions
		self.reply_template = "[Let me google that for you](https://lmgtfy.com/?q={})"
	
	# Create an authentication object		
	def authenticate(self):
	 	reddit = praw.Reddit(client_id = client_id,
	 	                  client_secret = client_secret,
	 	                  username = username,
	 	                  password = password,
	 	                  user_agent = user_agent)
	 	                  
	 	return reddit
	 	                  
		                  
	def main(self):
	   print(f"{white}Connecting to reddit...{reset}")
	   while True:
	   	try:
	   		subreddit = self.reddit.subreddit(self.subreddit)
	   		for submission in subreddit.stream.submissions():
	   			self.process_submission(submission)
	   			
	   	except Exception as e:
	   		print(f"{white}An error occured: {red}{e}{reset}")
	   		print(f"{white}Reconnecting...{reset}")
	   		
	   	except KeyboardInterrupt:
	   		print(f"{white}Disconnecting...{reset}")
	   		time.sleep(2)
	   		break
	   	
	
	def process_submission(self,submission):
	   # Ignore titles with more than 10 words as they probably are not simple questions.
	   if len(submission.title.split()) > 10:
	   	return
	   	
	   normalized_title = submission.title.lower()
	   for phrase in self.questions:
	   	if phrase in normalized_title:
	   	    url_title = quote_plus(submission.title
	   	    
	   	    print(f"{white}Replying to: {yellow}{submission.title}{reset}")
	   	    submission.reply(self.reply_template.format(url_title))
	   	    print(f"{white}Reply sent.{reset}\n\n")

if __name__ == "__main__":
    Lmgtfy().main()
