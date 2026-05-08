from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd

class Import_tweet_sentiment:

	# consumer_key="user consumer_key"
	# consumer_secret="user consumer_secret"
	# access_token="user access_token"
	# access_token_secret="user access_token_secret"

	consumer_key="2gHMzINygSDIBOJYedxxykcWT"
	consumer_secret="ihTu6Ig35ANi7XdAAfoKjbIofK0oSCYJjIaLIwC0QhTbjHgQim"
	access_token="1910940147291750400-djjEFYOyBn4UfwFhToFiZcApg8kVVl"
	access_token_secret="mDg35CxyL5ZpGSH4Zs2GVuwFAb9oaPkwl5z9wgmRnfAuu"

	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = handle
		item = auth_api.user_timeline(id=account,count=20)
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(20):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(auth_api.search, q=account, lang='en').items(20):
			all_tweets.append(tweet.text)

		return all_tweets
