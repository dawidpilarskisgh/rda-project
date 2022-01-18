import tweepy
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Token to connect to twitter API
API_key = ''
API_key_secret = ''
access_token = ''
access_token_secret = ''

def connect_twitter():
    auth = tweepy.OAuthHandler(API_key, API_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def search_twitts(api, text_to_search):
    tweets = api.search_tweets(text_to_search, count=250, lang='en', tweet_mode='extended')
    return tweets

def create_df_from_twitts(found_tweets):
    df = pd.DataFrame(data=[tweet.full_text for tweet in found_tweets], columns=['original_Tweets'])
    df['len'] = np.array([len(tweet.full_text) for tweet in found_tweets])
    df['Date'] = np.array([tweet.created_at for tweet in found_tweets])
    df['Date'] = pd.to_datetime(df.Date).dt.tz_localize(None)
    df['Likes'] = np.array([tweet.favorite_count for tweet in found_tweets])
    df['RTs'] = np.array([tweet.retweet_count for tweet in found_tweets])
    # Filter data to last hour
    start_date = datetime.now() - timedelta(hours=2)
    df_latest_data = df[(df['Date'] > start_date)]
    return df_latest_data

WORDS_TO_SEARCH = ['bitcoin', 'crypto', 'cryptonews', 'cryptocurrency', 'cryptocurrencies', 'BTC']

all_tweets = pd.DataFrame()

for word in WORDS_TO_SEARCH:
    found_tweets = search_twitts(connect_twitter(), word)
    df_tweet = create_df_from_twitts(found_tweets)
    frames = [all_tweets, df_tweet]
    all_tweets = pd.concat(frames)

# print(all_tweets)
all_tweets.to_csv('bitcoin_data.csv')
