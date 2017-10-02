#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:34:02 2017

@author: linda
"""

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
import sys
import glob
from itertools import islice

screen_names=[]
parties=[]

lidmaatschap = {}

with open('/home/linda/manifestos/tweets/NL/NL_twitter_mp.csv', encoding='utf-8',mode='r',newline='') as twitterlist:
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

for screen_name in screen_names[:1]:
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
    outtweets = [] #initialize master list to hold our ready tweets
    for tweet in alltweets:
                #not all tweets will have media url, so lets skip them
                try:
                        print (tweet.entities['media'][0]['media_url'])
                except (NameError, KeyError):
                        #we dont want to have any entries without the media_url so lets do nothing
                        pass
                else:
                #got media_url - means add it to the output
                        outtweets.append([tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.entities['media'][0]['media_url']])
    outputfile = '/home/linda/manifestos/tweets/downloads/NL/Party leaders/test/{}_{}_tweets_images.csv'.format(screen_name,lidmaatschap[screen_name])
    print("Writing stuff to {}".format(outputfile))
    with open(outputfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text","media_url"])
        writer.writerows(outtweets)

#%%
#pass

#allems = glob.glob("/home/linda/manifestos/*.csv")
#partijen = [p.split('/')[-1].strip('.csv.') for p in allems]
 
 