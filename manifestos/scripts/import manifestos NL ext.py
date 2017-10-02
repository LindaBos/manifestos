#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:30:20 2017

@author: linda
"""
from itertools import islice

import nltk
nltk.download()

from nltk.stem.snowball import SnowballStemmer
stemmer=SnowballStemmer("dutch")

from nltk.corpus import stopwords
stopwords = stopwords.words('dutch')

    
    
    

#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/gl_2012.csv', encoding='utf-8',mode='r',newline='') as gl_2012:
    reader = csv.reader(gl_2012,delimiter=',')
    for row in csv.reader(islice(gl_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "gl"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralgl12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/sp_2012.csv', encoding='utf-8',mode='r',newline='') as sp_2012:
    reader = csv.reader(sp_2012,delimiter=',')
    for row in csv.reader(islice(sp_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "sp"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralsp12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/pvda_2012.csv', encoding='utf-8',mode='r',newline='') as pvda_2012:
    reader = csv.reader(pvda_2012,delimiter=',')
    for row in csv.reader(islice(pvda_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "pvda"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralpvda12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/d66_2012.csv', encoding='utf-8',mode='r',newline='') as d66_2012:
    reader = csv.reader(d66_2012,delimiter=',')
    for row in csv.reader(islice(d66_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "d66"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/morald6612.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/vvd_2012.csv', encoding='utf-8',mode='r',newline='') as vvd_2012:
    reader = csv.reader(vvd_2012,delimiter=',')
    for row in csv.reader(islice(vvd_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "vvd"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralvvd12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/cda_2012.csv', encoding='utf-8',mode='r',newline='') as cda_2012:
    reader = csv.reader(cda_2012,delimiter=',')
    for row in csv.reader(islice(cda_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "cda"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralcda12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/cu_2012.csv', encoding='utf-8',mode='r',newline='') as cu_2012:
    reader = csv.reader(cu_2012,delimiter=',')
    for row in csv.reader(islice(cu_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "cu"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralcu12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/pvv_2012.csv', encoding='utf-8',mode='r',newline='') as pvv_2012:
    reader = csv.reader(pvv_2012,delimiter=',')
    for row in csv.reader(islice(pvv_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "pvv"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralpvv12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/pvdd_2012.csv', encoding='utf-8',mode='r',newline='') as pvdd_2012:
    reader = csv.reader(pvdd_2012,delimiter=',')
    for row in csv.reader(islice(pvdd_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "pvdd"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralpvdd12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/50p_2012.csv', encoding='utf-8',mode='r',newline='') as p50p_2012:
    reader = csv.reader(p50p_2012,delimiter=',')
    for row in csv.reader(islice(p50p_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "p50p"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moral50p12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/sgp_2012.csv', encoding='utf-8',mode='r',newline='') as sgp_2012:
    reader = csv.reader(sgp_2012,delimiter=',')
    for row in csv.reader(islice(sgp_2012, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "sgp"
yr = 2012
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralsgp12.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)
    

    

#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/gl_2010.csv', encoding='utf-8',mode='r',newline='') as gl_2010:
    reader = csv.reader(gl_2010,delimiter=',')
    for row in csv.reader(islice(gl_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "gl"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralgl10.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/sp_2010.csv', encoding='utf-8',mode='r',newline='') as sp_2010:
    reader = csv.reader(sp_2010,delimiter=',')
    for row in csv.reader(islice(sp_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "sp"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralsp10.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/pvda_2010.csv', encoding='utf-8',mode='r',newline='') as pvda_2010:
    reader = csv.reader(pvda_2010,delimiter=',')
    for row in csv.reader(islice(pvda_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "pvda"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralpvda10.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/d66_2010.csv', encoding='utf-8',mode='r',newline='') as d66_2010:
    reader = csv.reader(d66_2010,delimiter=',')
    for row in csv.reader(islice(d66_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "d66"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/morald6610.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/vvd_2010.csv', encoding='utf-8',mode='r',newline='') as vvd_2010:
    reader = csv.reader(vvd_2010,delimiter=',')
    for row in csv.reader(islice(vvd_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "vvd"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralvvd10.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/cda_2010.csv', encoding='utf-8',mode='r',newline='') as cda_2010:
    reader = csv.reader(cda_2010,delimiter=',')
    for row in csv.reader(islice(cda_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "cda"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralcda10.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/cu_2010.csv', encoding='utf-8',mode='r',newline='') as cu_2010:
    reader = csv.reader(cu_2010,delimiter=',')
    for row in csv.reader(islice(cu_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "cu"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralcu10.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/pvv_2010.csv', encoding='utf-8',mode='r',newline='') as pvv_2010:
    reader = csv.reader(pvv_2010,delimiter=',')
    for row in csv.reader(islice(pvv_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "pvv"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralpvv10.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/pvdd_2010.csv', encoding='utf-8',mode='r',newline='') as pvdd_2010:
    reader = csv.reader(pvdd_2010,delimiter=',')
    for row in csv.reader(islice(pvdd_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "pvdd"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralpvdd10.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)



#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/sgp_2010.csv', encoding='utf-8',mode='r',newline='') as sgp_2010:
    reader = csv.reader(sgp_2010,delimiter=',')
    for row in csv.reader(islice(sgp_2010, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "sgp"
yr = 2010
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralsgp10.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)    
    

    

#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/gl_2006.csv', encoding='utf-8',mode='r',newline='') as gl_2006:
    reader = csv.reader(gl_2006,delimiter=',')
    for row in csv.reader(islice(gl_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "gl"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralgl06.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/sp_2006.csv', encoding='utf-8',mode='r',newline='') as sp_2006:
    reader = csv.reader(sp_2006,delimiter=',')
    for row in csv.reader(islice(sp_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "sp"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralsp06.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/pvda_2006.csv', encoding='utf-8',mode='r',newline='') as pvda_2006:
    reader = csv.reader(pvda_2006,delimiter=',')
    for row in csv.reader(islice(pvda_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "pvda"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralpvda06.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/d66_2006.csv', encoding='utf-8',mode='r',newline='') as d66_2006:
    reader = csv.reader(d66_2006,delimiter=',')
    for row in csv.reader(islice(d66_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "d66"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/morald6606.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/vvd_2006.csv', encoding='utf-8',mode='r',newline='') as vvd_2006:
    reader = csv.reader(vvd_2006,delimiter=',')
    for row in csv.reader(islice(vvd_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "vvd"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralvvd06.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/cda_2006.csv', encoding='utf-8',mode='r',newline='') as cda_2006:
    reader = csv.reader(cda_2006,delimiter=',')
    for row in csv.reader(islice(cda_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "cda"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralcda06.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/cu_2006.csv', encoding='utf-8',mode='r',newline='') as cu_2006:
    reader = csv.reader(cu_2006,delimiter=',')
    for row in csv.reader(islice(cu_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "cu"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralcu06.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/pvv_2012.csv', encoding='utf-8',mode='r',newline='') as pvv_2006:
    reader = csv.reader(pvv_2006,delimiter=',')
    for row in csv.reader(islice(pvv_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "pvv"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralpvv06.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/pvdd_2006.csv', encoding='utf-8',mode='r',newline='') as pvdd_2006:
    reader = csv.reader(pvdd_2006,delimiter=',')
    for row in csv.reader(islice(pvdd_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "pvdd"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralpvdd06.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)



#%%

import csv
text=[]
cmp_code=[]
with open('/home/linda/manifestos/NL/sgp_2006.csv', encoding='utf-8',mode='r',newline='') as sgp_2006:
    reader = csv.reader(sgp_2006,delimiter=',')
    for row in csv.reader(islice(sgp_2006, 8, None)):
        text.append(row[0])
        cmp_code.append(row[1])

partyname = "sgp"
yr = 2006
ctr = "NL"


exec(open("/home/linda/manifestos/scripts/script manifestos NL ext.py").read(), globals())

output = zip(text,cmp_code,morallist, harmvirtuelist, harmvicelist, harmlist, fairnessvirtuelist, fairnessvicelist, fairnesslist, ingroupvirtuelist, ingroupvicelist, ingrouplist, purityvirtuelist, purityvicelist, puritylist, authorityvirtuelist, authorityvicelist, authoritylist, libertyvirtuelist, libertyvicelist, libertylist, moralgenlist, length, party, year, country)
with open("/home/linda/manifestos/data/NL/moralsgp06.csv", mode= "w", encoding = "utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)