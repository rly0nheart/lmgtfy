A Reddit Lmgtfy(Let me google that for you) bot
that replies to questions in specified subreddits.
It will reply to questions that contain *Who is*, *What is*, *Where is*, *How is*, *What are*, etc.


# Prerequisites
* Reddit client id
* Reddit client secret

# Installation
**Clone the repo**

<code>$ git clone https://github.com/rlyonheart/lmgtfy.git</code>

<code>$ cd lmgtfy</code>

<code>$ pip install -r requirements.txt</code>

# Getting Started
* Assuming your're already logged in to Reddit

The first step is to create an application to query the API.

* Go to [Reddit Apps](https://reddit.com/prefs/apps)
* Select “script” as the type of app.
* Name your app and give it a description.
* Set-up the redirect uri (you can just put https://example.com for this purpose)
* Click “Create app”, you will be given your *client_id* and *client_secret* key. you will use these in the *config/credentials.py file*

**After getting the keys**

Move to the *config/credentials.py* file, you will have to put your Reddit username and password then add the keys you got from Reddit.

* Then move to the lmgtfy.py file and add the name of the subreddit you what to monitor.
* Once that's done, run <code>python lmgtfy.py</code>.

You can also customize the bot's reply to suit your needs
