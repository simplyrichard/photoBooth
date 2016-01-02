#!/usr/bin/env python2.7    
import tweepy
import random  
from subprocess import call  
from datetime import datetime  
   
# Consumer keys and access tokens, used for OAuth  
consumer_key = 'CONSUMER API KEY'  
consumer_secret = 'CONSUMER_SECRET API KEY'  
access_token = 'ACCESS_TOKEN API KEY'  
access_token_secret = 'ACCESS_TOKEN API KEY'  
  
# Auth with Twitter using Keys above  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
   
# Creation of the actual interface, using authentication  
api = tweepy.API(auth)  
possibleTweets = ["Possible Tweet 1", "Possible Tweet 2", "Possible Tweet 3"] 
tweetString = random.choice(possibleTweets)

# Add path to photo, this is an absolute path from the root of device, eg. /var/www/latestPhoto.png  
photo_path = 'PATH TO PHOTO'

#String you would to go along with tweet
status = "@chris_vasey I am testing your python script"

#Tweet Text with Photo and String Specified Above 
api.update_with_media(photo_path, status=status)  



