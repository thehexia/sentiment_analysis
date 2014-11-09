# import a load of external features, for text display and date handling
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate
import twitter_sentiment

#csv module
import csv

#for object serialization
import pickle

#save tweets to parseable csv
#format tweet_id, hour:minute:second, mm/dd/yyyy, location, text, retweet_count, is_a_retweet ? true : false
#id, polarity, subjectivity, created_time (hour:minute:second), mm/dd/yyyy ,time_zone, retweet_count, tweet_length
def csv_print(query, filename):
	#open the file
	f = open(filename, "wb")

	for tweet in query:
		# each line of the csv
		tweet_line = ""

		#tweet id
		tweet_id = tweet["id_str"]

		# turn the date string into a date object that python can handle
		timestamp = parsedate(tweet["created_at"])

		# determine location
		#try to get location since this may not be possible
		time_zone = tweet["user"]["time_zone"]

		# get the length of the tweet
		tweet_length = len(tweet["text"])

		#get the retweet count
		retweet_count = str(tweet["retweet_count"])

		polarity, subjectivity = twitter_sentiment.one_tweet_sentiment_analysis(tweet)

		#build up the line of the csv
		tweet_line += tweet_id + "," + str(polarity) + "," + str(subjectivity) + "," + strftime("%H:%M:%S,%m/%d/%y", timestamp) + "," + time_zone + "," + retweet_count
		tweet_line = tweet_line.encode('utf-8')

		#write the line
		f.write(tweet_line + '\n')
	#close the file
	f.close()

def pretty_print_timeline(query):
	#print out all the tweets
	for tweet in query:
		# turn the date string into a date object that python can handle
		timestamp = parsedate(tweet["created_at"])

		# now format this nicely into HH:MM:SS format
		timetext = strftime("%H:%M:%S | %m/%d/%y", timestamp)

		# colour our tweet's time, user and text
		id_colored   = colored(tweet["id"], "red")
		retweet_count = colored(tweet["retweet_count"], "red")
		time_colored = colored(timetext, color = "white", attrs = [ "bold" ])
		user_colored = colored(tweet["user"]["screen_name"], "green")
		text_colored = tweet["text"]

		# add some indenting to each line and wrap the text nicely
		indent = " " * 11
		text_colored = fill(text_colored, 80, initial_indent = indent, subsequent_indent = indent)

		# now output our tweet
		print id_colored
		print retweet_count
		print "(%s) @%s" % (time_colored, user_colored)
		print "%s" % (text_colored)

	#print out total number of tweets retreived
	print ("Number of tweets: " + str(len(query)) )

#takes the result of a query and stores the raw JSON from twitter
# serializes the object for file storage
def raw_print(query, filename):
	with open(filename, 'wb') as output:
		pickle.dump(query, output, pickle.HIGHEST_PROTOCOL)

#reads files and unpickles them
def unpickle_tweets(filename):
	try:
		with open(filename, 'rb') as f:
			tweets = pickle.load(f)
		return tweets
	except:
		print "Error " + filename + " was a directory. Skipping." 