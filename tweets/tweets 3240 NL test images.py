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
    cleaned_text = [re.sub(r'http[s]?:\/\/.*[\W]*', '', i.text, flags=re.MULTILINE) for i in alltweets] # remove urls
    cleaned_text = [re.sub(r'@[\w]*', '', i, flags=re.MULTILINE) for i in cleaned_text] # remove the @twitter mentions 
    cleaned_text = [re.sub(r'RT.*','', i, flags=re.MULTILINE) for i in cleaned_text] # delete the retweets
    pictures = []
    for tweet in alltweets:
        if 'media' in tweet.entities:
            for image in  tweet.entities['media']:
                picture = image['media_url']
        elif 'media'not in tweet.entities:
            picture = 'no picture'
        pictures.append(picture)
    outtweets = [[tweet.id_str, tweet.favorite_count, tweet.retweet_count, tweet.created_at, pictures[idx], cleaned_text[idx]] for idx,tweet in enumerate(alltweets)]
    outputfile = '/home/linda/manifestos/tweets/downloads/NL/Party leaders/test/{}_{}_tweets_images.csv'.format(screen_name,lidmaatschap[screen_name])
    print("Writing stuff to {}".format(outputfile))
    with open(outputfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","favourite_count","retweet_count", "created_at", "image", "text"])
        writer.writerows(outtweets)

pass

#%%

#get text from images

# first download the images:

import wget

for p in pictures:
    if p is not 'no picture':
        wget.download(p)

# does not work, have to improve the code

# code below should be able to extract text from images, which should be doable if it are ads

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("/home/linda/manifestos/test/DJy5ELxXoAEH3M-.jpg") # the second one 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save("/home/linda/manifestos/test/testje.jpg")
text = pytesseract.image_to_string(Image.open("/home/linda/manifestos/test/testje.jpg"))
print(text) 