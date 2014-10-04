#imports
import sys

#custom module import
import pull_timeline
import twitter_stream
import tweet_printer

#options
option_one = "Eastern Time (US & Canada)"
option_two = "Central Time (US & Canada)"
option_three = "Mountain Time (US & Canada)"
option_four = "Pacific Time (US & Canada)"

tweet_count = 10

#parse the args
#set timezone based on args
for arg in sys.argv:
	if arg == '1':
		result = twitter_stream.stream_reader(tweet_count, option_one)
		tweet_printer.pretty_print_timeline(result)
	if arg == '2':
		result = twitter_stream.stream_reader(tweet_count, option_two)
		tweet_printer.pretty_print_timeline(result)
	if arg == '3':
		result = twitter_stream.stream_reader(tweet_count, option_three)
		tweet_printer.pretty_print_timeline(result)
	if arg == '4':
		result = twitter_stream.stream_reader(tweet_count, option_four)
		tweet_printer.pretty_print_timeline(result)


#actual script
#pull_timeline.pull_timeline("Drake")
