echo '====================PT tweets===================='
for f in `ls ~/tweets/PST_tweets`
do
	python tweet_reader.py "~/tweets/PST_tweets/"$f
done

echo '====================CT tweets===================='
for f in `ls ~/tweets/CT_tweets`
do
	python tweet_reader.py "~/tweets/CT_tweets/"$f
done

echo '====================EST tweets===================='
for f in `ls ~/tweets/EST_tweets`
do
	python tweet_reader.py "~/tweets/EST_tweets/"$f
done