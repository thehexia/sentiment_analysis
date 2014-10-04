#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#-----------------------------------------------------------------------

from twitter import *
import re

search_term = "Microsoft"

# import a load of external features, for text display and date handling
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

#custom packages
import tweet_printer

# these tokens are necessary for user authentication
consumer_key = "vd0jfFzb5EsgA32oiY5tqkoYe"
consumer_secret = "QpWU2EzpTpBjmn1CCXDuw3gNKfL0VNdsTrTAD9sjnjkwNEXVVF"
access_key = "2811413132-BrPwF6L4TujzhaZXQHTghBbsxexsTtRfs2X0rbk"
access_secret = "zGdDuzF3FdW32xg8jLmEj8Q8fXTpBLkC08MdHfPhR6W4S"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
stream = TwitterStream(auth = auth, secure = True)

print("Stream created")

# iterate over tweets matching this filter text
# IMPORTANT! this is not quite the same as a standard twitter search
# tweet_iter = stream.statuses.filter(track = search_term)
tweet_iter = stream.statuses.sample(q="", language = "en")

print("filter")

pattern = re.compile("%s" % search_term, re.IGNORECASE)

for tweet in tweet_iter:
	# print("trying to print tweet")
	# check whether this is a valid tweet
	if tweet.get('text'):

		# turn the date string into a date object that python can handle
		timestamp = parsedate(tweet["created_at"])
		# now format this nicely into HH:MM:SS format
		timetext = strftime("%H:%M:%S | %m/%d/%y", timestamp)

		# colour our tweet's time, user and text
		time_colored = colored(timetext, color = "white", attrs = [ "bold" ])
		user_colored = colored(tweet["user"]["screen_name"], "green")
		text_colored = tweet["text"]
		# replace each instance of our search terms with a highlighted version
		text_colored = pattern.sub(colored(search_term.upper(), "yellow"), text_colored)

		# add some indenting to each line and wrap the text nicely
		indent = " " * 11
		text_colored = fill(text_colored, 80, initial_indent = indent, subsequent_indent = indent)

		# now output our tweet
		#print timezone
		#print "(%s) @%s" % (time_colored, user_colored)
		#print "%s" % (text_colored)
		tweet_printer.raw_print(query, )
