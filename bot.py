#!/usr/bin/env python
import tweepy, random
import time
import os, pickle

##########################################################################################
CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXX"                                              #
CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXX"                                           #
ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXX"                                              #
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXX"                                       #
##########################################################################################

processed_tweets = []

try:
   with open('twts.pkl', 'rb') as f:
      processed_tweets=pickle.load(f)
except FileNotFoundError:
   pass

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
twt = api.search_tweets("#TVD",result_type="new",count=4) 
 
for s in twt:
   if s.id not in processed_tweets:
      time.sleep(3)
      sn = s.user.screen_name
      m = "@%s " %sn + random.choice(open('tweets.txt').readlines()).strip("\n") 
      api.update_status(status=m, in_reply_to_status_id = s.id)
      processed_tweets.append(s.id)
      print(s.id)

with open('twts.pkl', 'wb') as f:
   pickle.dump(processed_tweets, f)
print("Done replying!")
