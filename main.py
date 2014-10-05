#imports
import sys, os
from os.path import expanduser
from twitter import *
import re
from time import strftime

#custom module import
import pull_timeline
import twitter_stream
import tweet_printer

#helper functions
#-----------------
def filecount(dir_name):
	return len([f for f in os.listdir(dir_name)])
#-----------------

#-----------------
# Start of the actual script
# Consider this the main()
#-----------------

home = expanduser("~")

#create the directories we need
est_dir = home + "/tweets/EST_tweets"    #eastern standard time
ct_dir = home + "/tweets/CT_tweets"      #central time
pst_dir = home +"/tweets/PST_tweets"    #pacific standard time

#check if the folders exist. if they don,t make them
if not os.path.exists(est_dir):
    os.makedirs(est_dir)

if not os.path.exists(ct_dir):
    os.makedirs(ct_dir)

if not os.path.exists(pst_dir):
    os.makedirs(pst_dir)

# these tokens are necessary for user authentication
consumer_key = "vd0jfFzb5EsgA32oiY5tqkoYe"
consumer_secret = "QpWU2EzpTpBjmn1CCXDuw3gNKfL0VNdsTrTAD9sjnjkwNEXVVF"
#these keys are specific to each user of the twitter application. you must accept the terms and put your keys here
access_key = "2811413132-BrPwF6L4TujzhaZXQHTghBbsxexsTtRfs2X0rbk"
access_secret = "zGdDuzF3FdW32xg8jLmEj8Q8fXTpBLkC08MdHfPhR6W4S"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)
stream = TwitterStream(auth = auth, secure = True)

#how many tweets we want to collect from each zone
tweet_count = 100

#get the results
aggregate_result = twitter_stream.stream_reader(tweet_count, stream)

# tweet_printer.pretty_print_timeline(aggregate_result[0])
# tweet_printer.pretty_print_timeline(aggregate_result[1])
# #tweet_printer.pretty_print_timeline(aggregate_result[2])
# tweet_printer.pretty_print_timeline(aggregate_result[3])

#come up with file names
filename_est = str(filecount(est_dir)) + '_' + strftime("%m-%d-%Y_%H-%M-%S") + "_EST.pickle"
filename_ct = str(filecount(ct_dir)) + '_' + strftime("%m-%d-%Y_%H-%M-%S") + "_CT.pickle"
filename_pst = str(filecount(pst_dir)) + '_' + strftime("%m-%d-%Y_%H-%M-%S") + "_PST.pickle"

#write them to file
tweet_printer.raw_print(aggregate_result[0], est_dir + "/" + filename_est)
tweet_printer.raw_print(aggregate_result[1], ct_dir + "/" + filename_ct)
tweet_printer.raw_print(aggregate_result[3], pst_dir + "/" + filename_pst)