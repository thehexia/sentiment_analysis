# import a load of external features, for text display and date handling
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

#csv module
import csv

#for object serialization
import pickle

#save tweets to parseable csv
#first line is username
#format tweet_id, hour:minute:second, mm/dd/yyyy, location, text, retweet_count, is_a_retweet ? true : false
def csv_print(query, user, filename):
	#open the file
	f = open(filename, "w")

	for tweet in query:
		# each line of the csv
		tweet_line = ""

		#tweet id
		tweet_id = tweet["id_str"]

		# turn the date string into a date object that python can handle
		timestamp = parsedate(tweet["created_at"])

		# determine location
		location = "";
		#try to get location since this may not be possible
		try:
			location = tweet["location"]
		except:
			location = "Unknown"

		#get the tweet text
		#make sure to enclose in double-quotes to handle special chars that appear
		tweet_text = "\"" + tweet["text"] + "\""

		#get the retweet count
		retweet_count = str(tweet["retweet_count"])

		#determine if the tweet was a retweet
		was_retweeted = str(tweet["retweeted"])

		#build up the line of the csv
		tweet_line += tweet_id + "," + strftime("%H:%M:%S,%m/%d/%y", timestamp) + "," + location + "," + tweet_text + "," + retweet_count + "," + was_retweeted
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
		time_colored = colored(timetext, color = "white", attrs = [ "bold" ])
		user_colored = colored(tweet["user"]["screen_name"], "green")
		text_colored = tweet["text"]

		# add some indenting to each line and wrap the text nicely
		indent = " " * 11
		text_colored = fill(text_colored, 80, initial_indent = indent, subsequent_indent = indent)

		# now output our tweet
		print id_colored
		print "(%s) @%s" % (time_colored, user_colored)
		print "%s" % (text_colored)

	#print out total number of tweets retreived
	print ("Number of tweets: " + str(len(query)) )

#takes the result of a query and stores the raw JSON from twitter
# serializes the object for file storage
def raw_print(query, filename):
	with open(filename, 'wb') as output:
		pickle.dump(query, output, pickle.HIGHEST_PROTOCOL)