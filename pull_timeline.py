from twitter import *
import re

# import a load of external features, for text display and date handling
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate
from textblob import TextBlob

# these tokens are necessary for user authentication
consumer_key = "vd0jfFzb5EsgA32oiY5tqkoYe"
consumer_secret = "QpWU2EzpTpBjmn1CCXDuw3gNKfL0VNdsTrTAD9sjnjkwNEXVVF"
#these keys are specific to each user of the twitter application. you must accept the terms and put your keys here
access_key = "2811413132-BrPwF6L4TujzhaZXQHTghBbsxexsTtRfs2X0rbk"
access_secret = "zGdDuzF3FdW32xg8jLmEj8Q8fXTpBLkC08MdHfPhR6W4S"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

user = "Kanye"

#query the twitter db
#using documentation found here https://dev.twitter.com/rest/reference/get/statuses/user_timeline
query = twitter.statuses.user_timeline(screen_name = user, count = 200)

#want to get the last index and use it as the max_id for the first one
#NOTE: the max_id parameter tells twitter we want all tweets less than max_id.
last_id = query[-1]["id"]

#loop the query until we get an empty response
while (True):
	print ( "Working ... Last ID:" + str(last_id) )
	query2 = twitter.statuses.user_timeline(screen_name = user, count = 200, max_id = last_id)
	last_id = query2[-1]["id"]
	if (len(query2) <= 1):
		break
	query = query + query2

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