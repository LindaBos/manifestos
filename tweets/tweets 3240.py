#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:51:39 2017

@author: linda
"""

# copy https://gist.github.com/yanofsky/5436496

import tweepy
import re
import csv
import glob
from itertools import islice

screen_names=[]
parties=[]

lidmaatschap = {}

with open('/home/linda/manifestos/tweets/uk_twitter_mp.csv', encoding='utf-8',mode='r',newline='') as twitterlist:
    reader = csv.reader(twitterlist,delimiter=',')
    for row in csv.reader(islice(twitterlist, None)):
        screen_names.append(row[0])
        parties.append(row[1])
        lidmaatschap[row[0]] = row[1]

#nameparty = '{}_{}'.format(screen_name, party) 

#nameparty = []
#for a,b in zip(screen_names,parties):
#    nameparty.append("{}_{}".format(a,b))

      
#%%
        
#authorize twitter, initialize tweepy

auth = tweepy.OAuthHandler('RuYN0e3wWRrLpnvA8X2QFyLtH', 'qxs2ZdcPbnwB0kQlbgiygzF1LI3B3rcYA7pNaw1ApaMDj3xFDR',)
auth.set_access_token('1398102110-z9BBCXR9QAeNdXjnPTnrUwKRodGx8OVJzGiCGGi', 'RMVd2CFC3O8NjTDbgG3FVdj9BTV5NqWSkFuLk1Kl9ymd2')
api = tweepy.API(auth)

#%%

#initialize a list to hold all the tweepy Tweets

for screen_name in screen_names:
    print("Starting to get tweets from {}".format(screen_name))
    alltweets = []	
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)	
        oldest = alltweets[-1].id - 1
        print ("...%s tweets downloaded so far" % (len(alltweets)))
    cleaned_text = [re.sub(r'http[s]?:\/\/.*[\W]*', '', i.text, flags=re.MULTILINE) for i in alltweets] # remove urls
    cleaned_text = [re.sub(r'@[\w]*', '', i, flags=re.MULTILINE) for i in cleaned_text] # remove the @twitter mentions 
    cleaned_text = [re.sub(r'RT.*','', i, flags=re.MULTILINE) for i in cleaned_text] # delete the retweets
    outtweets = [[tweet.id_str, tweet.favorite_count, tweet.retweet_count, tweet.created_at, cleaned_text[idx].encode("utf-8")] for idx,tweet in enumerate(alltweets)]
    outputfile = '/home/linda/manifestos/tweets/downloads/{}_{}_tweets.csv'.format(screen_name,lidmaatschap[screen_name])
    print("Writing stuff to {}".format(outputfile))
    with open(outputfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","favourite_count","retweet_count", "created_at","text"])
        writer.writerows(outtweets)

pass

#allems = glob.glob("/home/linda/manifestos/*.csv")
#partijen = [p.split('/')[-1].strip('.csv.') for p in allems]
 
 