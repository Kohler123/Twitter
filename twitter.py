#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:24:35 2022

@author: brandonkohler
"""

import tweepy
import configparser
import pandas as pd

class TwitterStreamer():
    
    def __init__(self):
        pass
    
    
##Keys
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

##Authenication

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


columns = ['time:', 'user:', 'Tweet:']
data = []
public_tweets = api.home_timeline()

for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])
df = pd.DataFrame(data, columns=columns)

print(df)

