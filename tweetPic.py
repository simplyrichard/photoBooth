#!/usr/bin/env python2.7  
# tweetpic.py take a photo with the Pi camera and tweet it  
# by Alex Eames http://raspi.tv/?p=5918  
import tweepy
import random  
from subprocess import call  
from datetime import datetime  
   
#i = datetime.now()               #take time and date for filename  
#now = i.strftime('%Y%m%d-%H%M%S')  
#photo_name = now + '.jpg'  
# cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name
# FSWEBCAM command   
#call ([cmd], shell=True)         #shoot the photo  
  
# Consumer keys and access tokens, used for OAuth  
consumer_key = 'IeE7jBvb3wtFBThqzdrquEHjb'  
consumer_secret = 'qcL3B3yel4FYgdtNNZpauWMeTn8U2Er1qqRfA2SE0PDxAB8hE3'  
access_token = '394321578-ZobON1eD3zXUcNJjREnRTPUCCjfCXCHKPgVh1Q1V'  
access_token_secret = 'Vcbg2eTaGqQ5tHda5Zhquxx3GbUZHyeGlnEcYe99EOX3v'  
  
# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
   
# Creation of the actual interface, using authentication  
api = tweepy.API(auth)  
possibleTweets = ["PUSSY PATROL","HAMMOND MISSES YOU", "CHILDISH GAMBINO", "#JewFro", "DANK MEMES", "Wish u where here", "we MISS you", "#FillHerButt", "#NYE2KXVI", "A Dab'll do ya", "Stockwell Massif", "Straight outta Ktown", "Loose Fosters", "DJ Yodam, Minnie The Moocher", "#GirlsonFilm"] 
tweetString = random.choice(possibleTweets)

# Send the tweet with photo  
photo_path = '/tempPic/mike.png' #Absolute path on device form root  
status = tweetString+" #WhereRPhil NYE2015"   
api.update_with_media(photo_path, status=status)  

