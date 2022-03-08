#!/usr/bin/env python
import tweepy, random
import time
import pickle

##########################################################################################
CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"                           #
CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"                   #
ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"                      #
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"                    #
HASHTAG = "#tvd"                                                                         #
NUMBER_OF_TWEETS_TO_RERPLY = 5                                                           #
TWEETS_TYPE = "recent" #can be set to "mixed" or "popular" as well                       #
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
 
twt = api.search_tweets(HASHTAG,result_type=TWEETS_TYPE,count=NUMBER_OF_TWEETS_TO_RERPLY) 
 
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
