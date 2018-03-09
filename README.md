# TwitterAutoReplyBot
This is a tiny Python script that replies to specified number of tweets containing a specified hashtag.

This Twitter bot uses Tweepy, a Python module to deal with the Twitter API.

 > Replace the API credentials with yours in the keys.py file.
 > Specify the number of tweets to fetch from Twitter and specify a hashtag. For this, open bot.py and then make neccessary edits on line    15. Also, customize the reply text at line 20.
 
 Successfully tested and ran with Python27, running on Windows 10, build 15063.726
 
 A lot of updates are coming, cheers !!!!

## Update 1:
>Added functioanlity to use random tweet for reply from a text file.
 Now, you can define the tweets in "tweets.txt" file and start the bot.
 
##Todo
> Add a GUI for simplicity.....

#Running:

1: pip or pip2.7 install tweepy
2: Enter the Twitter keys in keys.py.
3:Customize the search query, hashtag, and number of tweets to fetch at line 16 of bot.py.
4: python or py -2 bot.py
