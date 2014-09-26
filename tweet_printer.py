# import a load of external features, for text display and date handling
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

def csv_print(query):
	print ""

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