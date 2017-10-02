#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:13:25 2017

@author: linda
"""
#WIP!!!#


## even nadenken hoe ik csv files kan lezen met glob
## wellicht

import glob

path = "/home/linda/manifestos/"
allfiles = glob.glob(os.path.join(path,"*.dic"))

#allems = glob.glob("/home/linda/manifestos/*.csv")
#partijen = [p.split('/')[-1].strip('.csv.') for p in allems]


#import csv files met glob
for file in allfiles:
    partyname = "ukip"
    yr = 2015
    ctr = "UK"
    exec(open("/home/linda/manifestos/scripts/script manifestos.py").read(), globals())
    output = zip(tsc,cmp_code,morallist, moralratio, harmvirtuelist, harmvicelist, harmlist, harmratio, fairnessvirtuelist, fairnessvicelist, fairnesslist, fairnessratio, ingroupvirtuelist, ingroupvicelist, ingrouplist, ingroupratio, purityvirtuelist, purityvicelist, puritylist, purityratio, authorityvirtuelist, authorityvicelist, authoritylist, authorityratio, length, party, year, country)
    with open("/home/linda/manifestos/data/moralukip15.csv", mode= "w", encoding = "utf-8") as fo:
        writer=csv.writer(fo)
        writer.writerows(output)

## check het script 3240 tweets, want daarin staat een tip om databestandsnaam en naam lijst zelfde te maken