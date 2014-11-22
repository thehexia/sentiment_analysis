from textblob import TextBlob
import os, sys, traceback
import pickle
import glob
import time

#reads files and unpickles them
def unpickle_tweets(filename):
	with open(filename, 'rb') as f:
		tweets = pickle.load(f)
	return tweets

def one_tweet_sentiment_analysis(tweet):
	text = tweet["text"]
	blob = TextBlob(text)
	return blob.sentiment.polarity, blob.sentiment.subjectivity

# performs sentiment analysis on tweets and returns the score
# returns a list[2] 
def sentiment_analysis(tweets):
	# results
	result_scores = [0, 0]
	result_count = [0, 0, 0]

	for tweet in tweets:
		#add a try/except block just in case a tweet is corrupted
		try:
			text = tweet["text"]
			blob = TextBlob(text)
			#polarity score between [-1.0, 1.0]
			polarity = blob.sentiment.polarity
			#subjectivity score between [0.0, 1.0]
			#0 is very objective, 1.0 is very subjective
			subjectivity = blob.sentiment.subjectivity
			# design a score algorithm to account polarity and subjectivity together
			# score = polarity * (1 + retweet_count)
			# if the score is between [-1.0, -0.1) it is a negative tweet
			# if the tweet is between [-0.1, 0.1] it is a neutral tweet
			# if the tweet is between (0.1, 1.0] it is a positive tweet
			score = polarity * (1 + tweet["retweet_count"])

			#positive polarity is x | 0.1 < x <= 1
			#neutral polarity is x | -0.1 <= x <= 0.1
			#negative polarity is x | -1 <= x < -0.1
			if (polarity >= 0.1):
				result_scores[0] += score
				result_count[0] += 1
			elif(polarity <= -0.1):
				result_scores[1] += score
				result_count[2] += 1
			else:
				# it doesnn't make sense to add neutral scores together
				# the idea of "level of neutral" doesnt make much sense
				result_count[1] += 1
		except:
			traceback.print_exc(file=sys.stdout)
	return result_scores, result_count

def meta_analysis(tweets):
	# average length of each tweet [pos, neutral, neg]
	avg_length = [0, 0, 0] 
	total_length = [0, 0, 0]
	count = [0, 0, 0]

	for tweet in tweets:
		#add a try/except block just in case a tweet is corrupted
		try:
			text = tweet["text"]
			blob = TextBlob(text)
			#polarity score between [-1.0, 1.0]
			polarity = blob.sentiment.polarity
			#subjectivity score between [0.0, 1.0]
			#0 is very objective, 1.0 is very subjective
			subjectivity = blob.sentiment.subjectivity
			# design a score algorithm to account polarity and subjectivity together
			# score = polarity * (1 + retweet_count)
			# if the score is between [-1.0, -0.1) it is a negative tweet
			# if the tweet is between [-0.1, 0.1] it is a neutral tweet
			# if the tweet is between (0.1, 1.0] it is a positive tweet
			score = polarity * (1 + tweet["retweet_count"])

			#positive polarity is x | 0.1 < x <= 1
			#neutral polarity is x | -0.1 <= x <= 0.1
			#negative polarity is x | -1 <= x < -0.1
			if (polarity >= 0.1):
				total_length[0] += len(text)
				count[0] += 1
			elif(polarity <= -0.1):
				total_length[2] += len(text)
				count[2] += 1
			else:
				total_length[1] += len(text)
				count[1] += 1
		except:
			traceback.print_exc(file=sys.stdout)

		avg_length[0] = total_length[0] / count[0]
		avg_length[1] = total_length[1] / count[1]
		avg_length[2] = total_length[2] / count[2]

	return avg_length