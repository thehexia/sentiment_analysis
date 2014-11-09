from os.path import basename
from os.path import isfile
import sys, os, time

import tweet_printer

#get the command line argument
dir_name = sys.argv[1]

#check if the folders exist. if they don,t make them
if not os.path.exists(dir_name + "csv"):
    os.makedirs(dir_name + "csv")
#create a csv folder inside the target directory
output_dir_name = dir_name + "csv"

#read the filenames from the directory given by the command line argument
filenames = []
for filename in os.listdir(dir_name):
	if(os.path.isfile(dir_name + filename)):
		filenames.append(dir_name + filename)

#read the input files and transform them into csv
count = 1
for filename in filenames:
	time.sleep(0.1)
	tweets = tweet_printer.unpickle_tweets(filename)
	out_filename = output_dir_name + "/" + os.path.basename(filename).replace("pickle", "csv")
	result = tweet_printer.csv_print(tweets, out_filename)
	sys.stdout.write("\r" + str(count))
	count += 1
	sys.stdout.flush()