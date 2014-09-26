from twitter import *
import re

#custom modules written by me
import tweet_printer

# these tokens are necessary for user authentication
consumer_key = "vd0jfFzb5EsgA32oiY5tqkoYe"
consumer_secret = "QpWU2EzpTpBjmn1CCXDuw3gNKfL0VNdsTrTAD9sjnjkwNEXVVF"
#these keys are specific to each user of the twitter application. you must accept the terms and put your keys here
access_key = "2811413132-BrPwF6L4TujzhaZXQHTghBbsxexsTtRfs2X0rbk"
access_secret = "zGdDuzF3FdW32xg8jLmEj8Q8fXTpBLkC08MdHfPhR6W4S"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

def pull_timeline(user):
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
	#pretty print timeline
	#tweet_printer.pretty_print_timeline(query)
	#csv print
	tweet_printer.csv_print(query, user, "test.txt")
	#raw print
	#tweet_printer.raw_print(query, "test.txt")