#!/bin/bash

python tweets2csv.py ~/tweets/EST_tweets/ csv/EST_tweets
python tweets2csv.py ~/tweets/PST_tweets/ csv/PST_tweets
python tweets2csv.py ~/tweets/CT_tweets/ csv/CT_tweets
