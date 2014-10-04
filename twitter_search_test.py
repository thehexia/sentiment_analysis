#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search-geo
#  - performs a search for tweets close to New Cross, and outputs
#    them to a CSV file.
#-----------------------------------------------------------------------

from twitter import *
import re

import sys
import csv

# these tokens are necessary for user authentication
consumer_key = "vd0jfFzb5EsgA32oiY5tqkoYe"
consumer_secret = "QpWU2EzpTpBjmn1CCXDuw3gNKfL0VNdsTrTAD9sjnjkwNEXVVF"
access_key = "2811413132-BrPwF6L4TujzhaZXQHTghBbsxexsTtRfs2X0rbk"
access_secret = "zGdDuzF3FdW32xg8jLmEj8Q8fXTpBLkC08MdHfPhR6W4S"

# create twitter API object
twitter = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

query = twitter.search.tweets(q="", count=180)

#want to get the last index and use it as the max_id for the first one
#NOTE: the max_id parameter tells twitter we want all tweets less than max_id.
last_id = query[-1]["statuses"]["id"]

#loop the query until we get an empty response
while (True):
	print ( "Working ... Last ID:" + str(last_id) )
	query2 = twitter.search.tweets(q="", count=180, max_id=last_id)
	last_id = query2[-1]["id"]
	if (len(query2) <= 1):
		break
	query = query + query2

for tweet in query:
	print query["statuses"]["name"]
	print query["statuses"]["text"]