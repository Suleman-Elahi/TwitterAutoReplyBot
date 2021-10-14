# TwitterAutoReplyBot
This is a tiny Python script that replies to specified number of tweets containing a specified hashtag.

This Twitter bot uses Tweepy, a Python module to deal with the Twitter API.

Successfully tested and ran with Python27, running on Windows 10, build 15063.726

Run as a cron job or via Task Scheduler to automatically reply to certain tweets of your interest.

A lot of updates are coming, cheers !!!!

## Update :
>Added functioanlity to use random tweet for reply from a text file.
 Now, you can define the tweets in "tweets.txt" file and start the bot.
 Also prevents replyign to same tweet again and again. Works with Tweepy v4.
 
### Todo
> Add a GUI for simplicity.....

## Running:

1. `pip3 install tweepy`
2. Enter the Twitter keys in bot.py at lines 6-11.
3. Customize the search query, hashtag, and number of tweets to fetch at line 25 of "bot.py".
4. Run as:  `python bot.py` or `python3 bot.py`
