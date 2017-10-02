#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:54:10 2017

@author: linda
"""
#%%

import nltk
nltk.download()

from nltk.stem.snowball import SnowballStemmer
stemmer=SnowballStemmer("english")

from nltk.corpus import stopwords
stopwords = stopwords.words('english')

import re

moraldic = open("/home/linda/manifestos/mf/moral foundations dictionary.dic").read().replace("\t", "").replace("\s", "")


harmvirtue = re.findall('([a-z]+\*?).*[0][1]', moraldic)
harmvice = re.findall('([a-z]+\*?).*[0][2]', moraldic)
fairnessvirtue = re.findall('([a-z]+\*?).*[0][3]', moraldic)
fairnessvice = re.findall('([a-z]+\*?).*[0][4]', moraldic)
ingroupvirtue = re.findall('([a-z]+\*?).*[0][5]', moraldic)
ingroupvice = re.findall('([a-z]+\*?).*[0][6]', moraldic)
authorityvirtue = re.findall('([a-z]+\*?).*[0][7]', moraldic)
authorityvice = re.findall('([a-z]+\*?).*[0][8]', moraldic)
purityvirtue = re.findall('([a-z]+\*?).*[0][9]', moraldic)
purityvice = re.findall('([a-z]+\*?).*[1][0]', moraldic)
moralitygeneral = re.findall('([a-z]+\*?).*[1][1]', moraldic)


moralityall = re.findall('([a-z]+\*?).*[01-11]', moraldic)

#%%

## met tweepy laatste 3240 tweets downloaden
## https://gist.github.com/yanofsky/5436496

import csv
text=[]
ids=[]
dates=[]
with open('/home/linda/manifestos/tweets/Nigel_Farage_tweets.csv', encoding='utf-8',mode='r',newline='') as Farage_tweets:
    reader = csv.reader(Farage_tweets,delimiter=',')
    for row in csv.reader(islice(Farage_tweets, None)):
        ids.append(row[0])
        dates.append(row[1])
        text.append(row[2])
        
            
exec(open("/home/linda/manifestos/tweets/script tweets.py").read(), globals())

output = zip(ids,tsc,dates,morallist, moralratio, harmvirtuelist, harmvicelist, harmlist, harmratio, fairnessvirtuelist, fairnessvicelist, fairnesslist, fairnessratio, ingroupvirtuelist, ingroupvicelist, ingrouplist, ingroupratio, purityvirtuelist, purityvicelist, puritylist, purityratio, authorityvirtuelist, authorityvicelist, authoritylist, authorityratio, length)
with open("/home/linda/manifestos/tweets/farage.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)
#%%

import os
import glob
import pandas as pd
import numpy as np

df = pd.read_csv("/home/linda/manifestos/tweets/farage.csv",index_col=None, header=0)

df.columns = ['ids','tweets','dates', 'morallist', 'moralratio', 'harmvirtuelist', 'harmvicelist', 'harmlist', 'harmratio', 'fairnessvirtuelist', 'fairnessvicelist',  'fairnesslist', 'fairnessratio', 'ingroupvirtuelist', 'ingroupvicelist', 'ingrouplist', 'ingroupratio', 'purityvirtuelist', 'purityvicelist', 'puritylist', 'purityratio', 'authorityvirtuelist', 'authorityvicelist', 'authoritylist', 'authorityratio', 'length']

## dit werkt. ik kan dus tweets downloaden en het moral foundations-script laten draaien, en hier vervolgens een dataframe van maken


#%% 

df

#%%

