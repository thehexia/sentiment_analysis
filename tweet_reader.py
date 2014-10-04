import pickle
import sys

#custom modules
import tweet_printer

def unpickle_tweets(filename):
	with open(filename, 'rb') as f:
		tweets = pickle.load(f)
	return tweets

tweets = unpickle_tweets(sys.argv[1])

tweet_printer.pretty_print_timeline(tweets)