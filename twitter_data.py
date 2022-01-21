import tweepy
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from textblob import TextBlob
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def connect_twitter():
    with open('credentials.json', 'r') as c:
        credentials = json.load(c)
    auth = tweepy.OAuthHandler(credentials['API_key'], credentials['API_key_secret'] )
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
    api = tweepy.API(auth)
    return api


def search_twitts(api, text_to_search):
    tweets = api.search_tweets(text_to_search, count=250, lang='en', result_type = 'mixed', tweet_mode='extended')
    return tweets


def create_df_from_twitts(found_tweets):
    sentiment_i_a = SentimentIntensityAnalyzer()

    df = pd.DataFrame(data=[tweet.full_text for tweet in found_tweets], columns=['original_Tweets'])
    df['len'] = np.array([len(tweet.full_text) for tweet in found_tweets])
    df['Date'] = np.array([tweet.created_at for tweet in found_tweets])
    df['Date'] = pd.to_datetime(df.Date).dt.tz_localize(None)
    df['Likes'] = np.array([tweet.favorite_count for tweet in found_tweets])
    df['RTs'] = np.array([tweet.retweet_count for tweet in found_tweets])

    sentiment_objects = [TextBlob(tweet.full_text) for tweet in found_tweets]
    sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]
    sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "tweet"])
    df['sentiment_text_blob'] = sentiment_df['polarity']

    sentiment_nltk = [sentiment_i_a.polarity_scores(tweet.full_text) for tweet in found_tweets]
    sentiment_nltk_df = pd.DataFrame(sentiment_nltk, columns=["neg", "neu", "pos"])
    df['Negative_nltk'] = sentiment_nltk_df['neg']
    df['Neutral_nltk'] = sentiment_nltk_df['neu']
    df['Positive_nltk'] = sentiment_nltk_df['pos']

    # Filter data to last hour
    start_date = datetime.now() - timedelta(hours=2)
    df_latest_data = df[(df['Date'] > start_date)]

    return df_latest_data


def get_data_from_API(WORDS_TO_SEARCH):
    all_tweets = pd.DataFrame()
    connection = connect_twitter()
    for word in WORDS_TO_SEARCH:
        found_tweets = search_twitts(connection, word)
        df_tweet = create_df_from_twitts(found_tweets)
        all_tweets = all_tweets.append(df_tweet, ignore_index=True)

    all_tweets.to_csv('nazwa_pliku_csv')
    return all_tweets
