from textblob import TextBlob
import os, sys, traceback
import pickle
import glob

# results
result_scores = [0, 0]
result_count = [0, 0, 0]

#reads files and unpickles them
def unpickle_tweets(filename):
	with open(filename, 'rb') as f:
		tweets = pickle.load(f)
	return tweets

# performs sentiment analysis on tweets and returns the score
# returns a list[2] 
def sentiment_analysis(tweets):
	for tweet in tweets:
		#add a try/except block just in case a tweet is corrupted
		try:
			text = tweet["text"]
			blob = TextBlob(text)
			#polarity score between [-1.0, 1.0]
			polarity = blob.sentiment.polarity
			#subjectivity score between [0.0, 1.0]
			#0 is very objective, 1.0 is very subjective
			subjectivity = blob.sentiment.subjectivity
			# design a score algorithm to account polarity and subjectivity together
			# score = polarity * subjectivity
			# if the score is between [-1.0, -0.1) it is a negative tweet
			# if the tweet is between [-0.1, 0.1] it is a neutral tweet
			# if the tweet is between (0.1, 1.0] it is a positive tweet
			score = polarity
			if (score >= 0.1):
				result_scores[0] += score
				result_count[0] += 1
			elif(score <= -0.1):
				result_scores[1] += score
				result_count[2] += 1
			else:
				# it doesnn't make sense to add neutral scores together
				# the idea of "level of neutral" doesnt make much sense
				result_count[1] += 1
		except:
			traceback.print_exc(file=sys.stdout)




#read the filenames from the directory given by the command line argument
dir_name = sys.argv[1]
filenames = []
for filename in os.listdir(dir_name):
	filenames.append(dir_name + "/" + filename)


#read the input file
for filename in filenames:
	tweets = unpickle_tweets(filename)
	result = sentiment_analysis(tweets)
print("Positivity Score: " + str(result_scores[0]))
print("Negativity Score: " + str(result_scores[1]))
print("Positivity Count: " + str(result_count[0]))
print("Neutrality Count: " + str(result_count[1]))
print("Negativity Count: " + str(result_count[2]))