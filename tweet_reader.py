import pickle
import sys
from os.path import expanduser

#custom modules
import tweet_printer

def unpickle_tweets(filename):
	with open(filename, 'rb') as f:
		tweets = pickle.load(f)
	return tweets

home = expanduser('~')
path = sys.argv[1].replace('~', home)
tweets = unpickle_tweets(path)

tweet_printer.pretty_print_timeline(tweets)

