#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
twt = api.search("#TVD",result_type="mixed",count=3) 
 
for s in twt:
   print(s.id)
   sn = s.user.screen_name
   m = "@%s Good Morning Sunshine!" % (sn)
   api.update_status(status=m, in_reply_to_status_id = s.id)
print("Done!!!")