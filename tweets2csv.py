from os.path import basename
import sys, os, time

import tweet_printer

#check if the folders exist. if they don,t make them
if not os.path.exists("csv"):
    os.makedirs("csv")

#read the filenames from the directory given by the command line argument
dir_name = sys.argv[1]
filenames = []
for filename in os.listdir(dir_name):
	filenames.append(dir_name + filename)

output_dir_name = sys.argv[2]

if not os.path.exists(output_dir_name):
	os.makedirs(output_dir_name)

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