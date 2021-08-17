#!/usr/bin/env python
import tweepy, random
import time

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
twt = api.search("#TVD",result_type="new",count=5) 
 
for s in twt:
   time.sleep(3)
   print(s.id)
   sn = s.user.screen_name
   m = "@%s " %sn + random.choice(open('tweets.txt').readlines()).strip("\n") 
   api.update_status(status=m, in_reply_to_status_id = s.id)
print("Done!!!")
