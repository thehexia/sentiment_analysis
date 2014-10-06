#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#-----------------------------------------------------------------------

from twitter import *
import re

# import a load of external features, for text display and date handling
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

#system packages
import sys
from time import sleep

#custom packages
import tweet_printer

#options
zone_one = "Eastern Time (US & Canada)"
zone_two = "Central Time (US & Canada)"
zone_three = "Mountain Time (US & Canada)"
zone_four = "Pacific Time (US & Canada)"

#count - number of tweets to collect for stopping
#timezone - timezone where the tweets will be collected from
#stream - the twitter authentication object
def stream_reader(count, stream):
	print("Stream created")
	tweet_iter = stream.statuses.sample(language = "en")
	
	#results
	result_1 = []
	result_2 = []
	result_3 = []
	result_4 = []

	#counter for each timezone
	i_1 = 0
	i_2 = 0
	i_3 = 0
	i_4 = 0

	for tweet in tweet_iter:
		try:
			#add if they match a time zone
			if (tweet["user"]["time_zone"] == zone_one and i_1 < count):
				result_1.append(tweet)
				i_1 += 1
				print(str(i_1) + "/" + str(count) + " " + str(i_2) + "/" + str(count) + " " + str(i_3) + "/" + str(count) + " " + str(i_4) + "/" + str(count))
			if (tweet["user"]["time_zone"] == zone_two and i_2 < count):
				result_2.append(tweet)
				i_2 += 1
				print(str(i_1) + "/" + str(count) + " " + str(i_2) + "/" + str(count) + " " + str(i_3) + "/" + str(count) + " " + str(i_4) + "/" + str(count))
			#if (tweet["user"]["time_zone"] == zone_three and i_3 < count):
			#	result_3.append(tweet)
			#	i_3 += 1
			#	print(str(i_1) + "/" + str(count) + " " + str(i_2) + "/" + str(count) + " " + str(i_3) + "/" + str(count) + " " + str(i_4) + "/" + str(count))
			if (tweet["user"]["time_zone"] == zone_four and i_4 < count):
				result_4.append(tweet)
				i_4 += 1
				print(str(i_1) + "/" + str(count) + " " + str(i_2) + "/" + str(count) + " " + str(i_3) + "/" + str(count) + " " + str(i_4) + "/" + str(count))
		except:
			print("Broken tweet")
		#break when all i_x = count
		if(i_1 == count and i_2 == count and i_4 == count):
			break
	return result_1, result_2, result_3, result_4
	


