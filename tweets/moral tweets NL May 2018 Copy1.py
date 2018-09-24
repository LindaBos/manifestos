
# coding: utf-8

# In[44]:

import nltk
nltk.download()

from nltk.stem.snowball import SnowballStemmer
stemmer=SnowballStemmer("dutch")

from nltk.corpus import stopwords
stopwords_ned = stopwords.words('dutch')
stopwords_eng = stopwords.words('english')
stopwords = stopwords_eng + stopwords_ned

import re

moraldic = open("/home/linda/manifestos/manifestos/mf/dutch moral foundations dictionary ext.1.dic").read().replace("\t", "").replace("\s", "")


harmvirtue_ned = re.findall('([a-z]+\*?).*[0][1]', moraldic)
harmvice_ned = re.findall('([a-z]+\*?).*[0][2]', moraldic)
fairnessvirtue_ned = re.findall('([a-z]+\*?).*[0][3]', moraldic)
fairnessvice_ned = re.findall('([a-z]+\*?).*[0][4]', moraldic)
ingroupvirtue_ned = re.findall('([a-z]+\*?).*[0][5]', moraldic)
ingroupvice_ned = re.findall('([a-z]+\*?).*[0][6]', moraldic)
authorityvirtue_ned = re.findall('([a-z]+\*?).*[0][7]', moraldic)
authorityvice_ned = re.findall('([a-z]+\*?).*[0][8]', moraldic)
purityvirtue_ned = re.findall('([a-z]+\*?).*[0][9]', moraldic)
purityvice_ned = re.findall('([a-z]+\*?).*[1][0]', moraldic)
moralitygeneral_ned = re.findall('([a-z]+\*?).*[1][1]', moraldic)
libertyvirtue_ned = re.findall('([a-z]+\*?).*[1][2]', moraldic)
libertyvice_ned = re.findall('([a-z]+\*?).*[1][3]', moraldic)


moralityall_ned = re.findall('([a-z]+\*?).*[01-11]', moraldic)


# In[45]:
    
    # test

print(purityvice_ned)


# In[46]:

moraldic_eng = open("/home/linda/manifestos/manifestos/mf/moral foundations dictionary ext.1.dic").read().replace("\t", "").replace("\s", "")


harmvirtue_eng = re.findall('([a-z]+\*?).*[0][1]', moraldic_eng)
harmvice_eng = re.findall('([a-z]+\*?).*[0][2]', moraldic_eng)
fairnessvirtue_eng = re.findall('([a-z]+\*?).*[0][3]', moraldic_eng)
fairnessvice_eng = re.findall('([a-z]+\*?).*[0][4]', moraldic_eng)
ingroupvirtue_eng = re.findall('([a-z]+\*?).*[0][5]', moraldic)
ingroupvice_eng = re.findall('([a-z]+\*?).*[0][6]', moraldic_eng)
authorityvirtue_eng = re.findall('([a-z]+\*?).*[0][7]', moraldic_eng)
authorityvice_eng = re.findall('([a-z]+\*?).*[0][8]', moraldic_eng)
purityvirtue_eng = re.findall('([a-z]+\*?).*[0][9]', moraldic_eng)
purityvice_eng = re.findall('([a-z]+\*?).*[1][0]', moraldic_eng)
moralitygeneral_eng = re.findall('([a-z]+\*?).*[1][1]', moraldic_eng)
libertyvirtue_eng = re.findall('([a-z]+\*?).*[1][2]', moraldic_eng)
libertyvice_eng = re.findall('([a-z]+\*?).*[1][3]', moraldic_eng)


moralityall_eng = re.findall('([a-z]+\*?).*[01-11]', moraldic_eng)


# In[47]:

    # test
    
print(libertyvice_eng)


# In[48]:

harmvirtue = harmvirtue_eng + harmvirtue_ned
harmvice = harmvice_eng + harmvice_ned
fairnessvirtue = fairnessvirtue_eng + fairnessvirtue_ned
fairnessvice = fairnessvice_eng + fairnessvice_ned
ingroupvirtue = ingroupvirtue_eng + ingroupvirtue_ned
ingroupvice = ingroupvice_eng + ingroupvice_ned
authorityvirtue = authorityvirtue_eng + authorityvirtue_ned
authorityvice = authorityvice_eng + authorityvice_ned
purityvirtue = purityvirtue_eng + purityvirtue_ned
purityvice = purityvice_eng + purityvice_ned
libertyvirtue = libertyvirtue_eng + libertyvirtue_ned
libertyvice = libertyvice_eng + libertyvice_ned
moralitygeneral = moralitygeneral_eng + moralitygeneral_ned
moralityall = moralityall_eng + moralityall_ned


# In[50]:

import csv
from glob import glob
import re
from itertools import islice
import string

names=[]
parties=[]
lidmaatschap = {}


alltweets = glob("/home/linda/manifestos/tweets/downloads/NL 2018/tweets/*.csv")
peeps = [p.split('/')[-1].strip('.csv.') for p in alltweets]

names = [pp.split('_')[-3].strip() for pp in peeps]
parties = [pp.split('_')[-2].strip() for pp in peeps]

lidmaatschap = dict(zip(names,parties))
filenames = dict(zip(names, alltweets))


for name in names:
    ids=[]
    favourites=[]
    retweets=[]
    dates=[]
    quote=[]
    rt=[]
    text=[]
    file = filenames[name]
    print("now opening", file)
    with open(file) as fi:
        reader = csv.reader(fi,delimiter=',')
        for row in csv.reader(islice(fi, None)):
            ids.append(row[0])
            favourites.append(row[1])
            retweets.append(row[2])
            dates.append(row[3])
            quote.append(row[4])
            rt.append(row[5])
            text.append(row[6]) 
        translate_table = dict((ord(char), None) for char in string.punctuation)   
        text = [t.translate(translate_table) for t in text]
        text = [t.lower() for t in text]
        text = [t.strip() for t in text if t.strip()!=""]
        text = [t.strip() for t in text if len(t)> 10]
        text = [' '.join(w for w in t.split() if w.lower() not in stopwords) for t in text]
        morallist=[]
        harmvirtuelist = []
        harmvicelist = []
        fairnessvirtuelist = []
        fairnessvicelist = []
        ingroupvirtuelist = []
        ingroupvicelist = []
        authorityvirtuelist = []
        authorityvicelist = []
        purityvirtuelist = []
        purityvicelist = []
        moralgenlist = []
        libertyvirtuelist = []
        libertyvicelist = []
        harmlist = []
        fairnesslist = []
        ingrouplist = []
        authoritylist = []
        puritylist = []
        libertylist=[]
        length=[]
        for line in text:
            moralcount=0
            harmvirtuecount=0
            harmvicecount=0
            fairnessvirtuecount=0
            fairnessvicecount=0
            ingroupvirtuecount=0
            ingroupvicecount=0
            authorityvirtuecount=0
            authorityvicecount=0
            purityvirtuecount=0
            purityvicecount=0
            libertyvirtuecount=0
            libertyvicecount=0
            moralgencount=0
            for pattern in moralityall:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        moralcount+=1
            for pattern in harmvirtue:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        harmvirtuecount+=1
            for pattern in harmvice:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        harmvicecount+=1
            for pattern in fairnessvirtue:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        fairnessvirtuecount+=1
            for pattern in fairnessvice:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        fairnessvicecount+=1
            for pattern in ingroupvirtue:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        ingroupvirtuecount+=1
            for pattern in ingroupvice:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        ingroupvicecount+=1
            for pattern in authorityvirtue:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        authorityvirtuecount+=1
            for pattern in authorityvice:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        authorityvicecount+=1
            for pattern in purityvirtue:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        purityvirtuecount+=1
            for pattern in purityvice:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        purityvicecount+=1        
            for pattern in libertyvirtue:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        libertyvirtuecount+=1
            for pattern in libertyvice:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        libertyvicecount+=1
            for pattern in moralitygeneral:
                for word in line.split():
                    if pattern[-1] == '*' and word.startswith(pattern[:-1]) or word == pattern:
                        moralgencount+=1
            morallist.append(moralcount)
            harmvirtuelist.append(harmvirtuecount)
            harmvicelist.append(harmvicecount)
            harmlist.append(harmvicecount+harmvirtuecount)
            fairnessvirtuelist.append(fairnessvirtuecount)
            fairnessvicelist.append(fairnessvicecount)
            fairnesslist.append(fairnessvicecount+fairnessvirtuecount)
            ingroupvirtuelist.append(ingroupvirtuecount)
            ingroupvicelist.append(ingroupvicecount)
            ingrouplist.append(ingroupvirtuecount + ingroupvicecount)
            authorityvirtuelist.append(authorityvirtuecount)
            authorityvicelist.append(authorityvicecount)
            authoritylist.append(authorityvicecount + authorityvirtuecount)
            purityvirtuelist.append(purityvirtuecount)
            purityvicelist.append(purityvicecount)
            puritylist.append(purityvicecount + purityvirtuecount)
            libertyvirtuelist.append(libertyvirtuecount)
            libertyvicelist.append(libertyvicecount)
            libertylist.append(libertyvicecount + libertyvirtuecount)
            moralgenlist.append(moralgencount)
            length.append(len(line))
        output = zip(ids,text,dates, favourites, retweets, quote, rt, morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length)
        outputfile = "/home/linda/manifestos/tweets/downloads/NL 2018/coded/{}_{}_coded.csv".format(name,lidmaatschap[name])
        print("Writing stuff to {}".format(outputfile))
        with open(outputfile, "w") as fo:
            writer=csv.writer(fo)
            writer.writerows(output)
         


# In[56]:

import glob
import pandas as pd
import numpy as np
import re
import os

path = "/home/linda/manifestos/tweets/downloads/NL 2018/coded/"
allfiles = glob.glob(os.path.join(path,"*.csv"))

peeps = [p.split('/')[-1].strip('.csv.') for p in allfiles]

names = [pp.split('_')[-3].strip() for pp in peeps]
parties = [pp.split('_')[-2].strip() for pp in peeps]

lidmaatschap = dict(zip(names,parties))
namefile = dict(zip(names,allfiles))



# In[57]:
    
    # test 

print(lidmaatschap)
print(namefile)


# In[58]:

np_array_list = []
data = []
for name in names:
    file_= namefile[name]
    df = pd.read_csv(file_,index_col=None, header=0)
    df['politicians'] = name
    df['party'] = lidmaatschap[name]
    data.append(df)
    np_array_list.append(df.as_matrix())

comb_np_array = np.vstack(np_array_list)
big_frame = pd.DataFrame(comb_np_array)

big_frame.columns = ['id','tweet','date', 'likes', 'retweets', 'quote', 'rt', 'morallist', 'harmvirtuelist', 'harmvicelist', 'harmlist', 'fairnessvirtuelist', 'fairnessvicelist',  'fairnesslist', 'ingroupvirtuelist', 'ingroupvicelist', 'ingrouplist', 'purityvirtuelist', 'purityvicelist', 'puritylist', 'authorityvirtuelist', 'authorityvicelist', 'authoritylist', 'libertyvirtuelist', 'libertyvicelist', 'libertylist', 'moralgenlist', 'length', 'name', 'party']

bf = big_frame.fillna(value = 0)



# In[59]:

parties = pd.get_dummies(bf['party'])

bfd = pd.concat([bf, parties], axis=1)  


# In[60]:

for foundation in ['harmlist','puritylist','ingrouplist','authoritylist', 'fairnesslist', 'libertylist','moralgenlist',  'morallist']:
    print(foundation.upper())
    print(bfd[foundation].value_counts(sort=True, normalize=True))
    print('-------------------------------------------\n')


# In[65]:

bfd['moraldummy'] = np.where(bfd['morallist']>0, '1', '0')
bfd['harmdummy'] = np.where(bfd['harmlist']>0, '1', '0')
bfd['fairnessdummy'] = np.where(bfd['fairnesslist']>0, '1', '0')
bfd['ingroupdummy'] = np.where(bfd['ingrouplist']>0, '1', '0')
bfd['authoritydummy'] = np.where(bfd['authoritylist']>0, '1', '0')
bfd['puritydummy'] = np.where(bfd['puritylist']>0, '1', '0')
bfd['libertydummy'] = np.where(bfd['libertylist']>0, '1', '0')
bfd['moralgendummy'] = np.where(bfd['moralgenlist']>0, '1', '0')



# In[68]:

bfd.to_csv('/home/linda/manifestos/combined data/Dutch tweets 2018.csv')



