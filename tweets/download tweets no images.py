#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 18:42:13 2017

@author: linda
"""

import tweepy
import re
import csv
#import glob
from itertools import islice
import os
#import os, sys
#import wget
#import pytesseract
#from PIL import Image, ImageEnhance, ImageFilter


screen_names=[]
parties=[]

lidmaatschap = {}

with open('/home/linda/manifestos/tweets/NL/NL_twitter_mp_all_new.csv', encoding='utf-8',mode='r',newline='') as twitterlist:
    reader = csv.reader(twitterlist,delimiter=',')
    for row in csv.reader(islice(twitterlist, None)):
        screen_names.append(row[0])
        parties.append(row[1])
        lidmaatschap[row[0]] = row[1]
        
#%%

auth = tweepy.OAuthHandler('RuYN0e3wWRrLpnvA8X2QFyLtH', 'qxs2ZdcPbnwB0kQlbgiygzF1LI3B3rcYA7pNaw1ApaMDj3xFDR',)
auth.set_access_token('1398102110-z9BBCXR9QAeNdXjnPTnrUwKRodGx8OVJzGiCGGi', 'RMVd2CFC3O8NjTDbgG3FVdj9BTV5NqWSkFuLk1Kl9ymd2')
api = tweepy.API(auth)


# In[ ]:

# Note: script hieronder werkt bijna helemaal:
# images worden gedownload, opgeslagen en geanalyseerd
# text uit images wordt opgeslagen en gekoppeld aan tweet
# krijg alleen nu niet voor elkaar om die text samen te voegen met de text van de tweet zelf
# zou zijn omdat een van beide een list is, maar ik weet eigenlijk niet welke.

# daarnaast gaat dit in jupyter notebook echt veel te langzaam
# vraag me ook af of dat enhancen noodzakelijk is
# In[6]:

for screen_name in screen_names[110:]:
    print("Starting to get tweets from {}".format(screen_name))
#    os.makedirs("/home/linda/manifestos/tweets/downloads/NL/Images/images_{}_{}".format(screen_name,lidmaatschap[screen_name]))    
    #os.chdir("/home/linda/manifestos/tweets/downloads/NL/Images/images_{}_{}".format(screen_name,lidmaatschap[screen_name]))    
    #os.chdir("/home/linda/manifestos/tweets/downloads/NL/Images")
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
    cleaned_text = [re.sub(r'RT : ','', i, flags=re.MULTILINE) for i in cleaned_text] # delete the retweets
    #picturetext=[]
    #pictures=[]
    #ttext=[]
    RT=[]
    for tweet in alltweets: 
        #if 'media' in tweet.entities:
        #    for image in  tweet.entities['media']:
         #       picture = image['media_url']
         #       pic = picture.split("/")[-1]
             #   if not os.path.isfile(pic):
             #       wget.download(picture)
             #   im = Image.open(pic)
             #   im = im.filter(ImageFilter.MedianFilter())
             #   enhancer = ImageEnhance.Contrast(im)
             #   im = enhancer.enhance(2)
             #   im = im.convert('1')
             #   im.save('temp.jpg')
          #      text_from_picture = pytesseract.image_to_string(Image.open('pic'))
             #   os.remove('temp.jpg')
       # elif 'media' not in tweet.entities:
        #    picture = 'no picture'
        #    text_from_picture = ''
        retweet=0
        if 'RT' in tweet.text:
            retweet+=1
        RT.append(retweet)
        #picturetext.append(text_from_picture)
        #ttext = ['{}{}'.format(i,j) for i, j in zip(cleaned_text, picturetext)] 
        #pictures.append(picture)
    outtweets = [[tweet.id_str, tweet.favorite_count, tweet.retweet_count, tweet.created_at, tweet.is_quote_status,RT[idx], cleaned_text[idx]] for idx,tweet in enumerate(alltweets)]
    outputfile = '/home/linda/manifestos/tweets/downloads/NL/{}_{}_tweets.csv'.format(screen_name,lidmaatschap[screen_name])
    print("Writing stuff to {}".format(outputfile))
    with open(outputfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "favourite_count", "retweet_count", "created_at", "quote", "RT", "cleaned_text"])
        writer.writerows(outtweets)

pass

####klopt dus niet