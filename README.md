# TwitterAutoReplyBot
This is a tiny Python script that replies to specified number of tweets containing a specified hashtag.

This Twitter bot uses Tweepy, a Python module to deal with the Twitter API.

Successfully tested and ran with Python38, running on Windows 11.

Run as a cron job or via Task Scheduler to automatically reply to certain tweets of your interest.

## Update 2021 :
>Added functioanlity to use random tweet for reply from a text file.
 Now, you can define the tweets in "tweets.txt" file and start the bot.
 Also prevents replyign to same tweet again and again. Works with Tweepy v4.
 
### Todo
> Add a GUI for simplicity.....

## Running:

1. Open Terminal or Command Prompt(cmd.exe) or PowerShell. Make sure `git` is installed.
2. `git clone https://github.com/Suleman-Elahi/TwitterAutoReplyBot && cd TwitterAutoReplyBot`
3. `pip3 install tweepy`
4. Enter the Twitter keys in `bot.py` file at lines 7-10.
5. Customize the hashtag, number of tweets to reply to, and tweets type to fetch at line 11-13 of "bot.py".
6. Define the tweets in each line of the text file, `tweets.txt`.
7. Run as:  `python bot.py` or `python3 bot.py`
