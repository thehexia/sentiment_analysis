#!/bin/bash

python tweets2csv.py tweets/EST_tweets/
python tweets2csv.py tweets/PST_tweets/
python tweets2csv.py tweets/CT_tweets/

echo "tweets/EST_tweets/by_day/\n";
for dir in `ls tweets/EST_tweets/by_day/`;
do
	echo "tweets/EST_tweets/by_day/"$dir"/"
	python tweets2csv.py "tweets/EST_tweets/by_day/"$dir"/"
	cat "tweets/EST_tweets/by_day/"$dir"/csv/"* > "tweets/EST_tweets/by_day/"$dir"/csv/"merge.csv;
done

echo "tweets/EST_tweets/by_hour/\n";
for dir in `ls tweets/EST_tweets/by_hour/`;
do
	echo "tweets/EST_tweets/by_hour/"$dir"/"
	python tweets2csv.py "tweets/EST_tweets/by_hour/"$dir"/"
	cat "tweets/EST_tweets/by_hour/"$dir"/csv/"* > merge.csv;
done

echo "tweets/PST_tweets/by_day/\n";
for dir in `ls tweets/PST_tweets/by_day/`;
do
	echo "tweets/PST_tweets/by_day/"$dir"/"
	python tweets2csv.py "tweets/PST_tweets/by_day/"$dir"/"
	cat "tweets/PST_tweets/by_day/"$dir"/csv/"* > merge.csv;
done

echo "tweets/PST_tweets/by_hour/\n";
for dir in `ls tweets/PST_tweets/by_hour/`;
do
	echo "tweets/PST_tweets/by_hour/"$dir"/"
	python tweets2csv.py "tweets/PST_tweets/by_hour/"$dir"/"
	cat "tweets/PST_tweets/by_hour/"$dir"/csv/"* > merge.csv;
done

echo "tweets/CT_tweets/by_day/\n";
for dir in `ls tweets/CT_tweets/by_day/`;
do
	echo "tweets/CT_tweets/by_day/"$dir"/"
	python tweets2csv.py "tweets/CT_tweets/by_day/"$dir"/"
	cat "tweets/CT_tweets/by_day/"$dir"/csv/"* > merge.csv;
done

echo "tweets/CT_tweets/by_hour/\n"
for dir in `ls tweets/CT_tweets/by_hour/`;
do
	echo "tweets/CT_tweets/by_hour/"$dir"/"
	python tweets2csv.py "tweets/CT_tweets/by_hour/"$dir"/"
	cat "tweets/CT_tweets/by_hour/"$dir"/csv/"* > merge.csv
done