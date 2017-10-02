#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:30:20 2017

@author: linda
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:16:28 2017

@author: linda
"""
 



#lege zinnen weglaten
#stopwoorden verwijderen en stemmen

t = [r.strip() for r in text if r.strip()!="b''"]
ts = [' '.join(w for w in t.split() if w.lower() not in stopwords) for t in t]
tsc = [" ".join([stemmer.stem(w) for w in t.split(" ")]) for t in ts]

#morele woorden tellen en opslaan als csv

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
harmlist = []
fairnesslist = []
ingrouplist = []
authoritylist = []
puritylist = []
harmratio = []
fairnessratio = []
ingroupratio = []
authorityratio = []
purityratio = []
moralratio=[]
length=[]
party = []
year= []
country = []
for line in tsc:
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
    for word in line.split():
        if word in moralityall:
            moralcount+=1
        if word in harmvirtue:
            harmvirtuecount+=1
        if word in harmvice:
            harmvicecount+=1
        if word in fairnessvirtue:
            fairnessvirtuecount+=1
        if word in fairnessvice:
            fairnessvicecount+=1
        if word in ingroupvirtue:
            ingroupvirtuecount+=1
        if word in ingroupvice:
            ingroupvicecount+=1
        if word in authorityvirtue:
            authorityvirtuecount+=1
        if word in authorityvice:
            authorityvicecount+=1
        if word in purityvirtue:
            purityvirtuecount+=1
        if word in purityvice:
            purityvicecount+=1            
    morallist.append(moralcount)
    harmvirtuelist.append(harmvirtuecount)
    harmvicelist.append(harmvicecount)
    harmlist.append(harmvicecount+harmvirtuecount)
    harmratio.append((harmvicecount+harmvirtuecount)/len(line))
    fairnessvirtuelist.append(fairnessvirtuecount)
    fairnessvicelist.append(fairnessvicecount)
    fairnesslist.append(fairnessvicecount+fairnessvirtuecount)
    fairnessratio.append((fairnessvicecount+fairnessvirtuecount)/len(line))   
    ingroupvirtuelist.append(ingroupvirtuecount)
    ingroupvicelist.append(ingroupvicecount)
    ingrouplist.append(ingroupvirtuecount + ingroupvicecount)
    ingroupratio.append((ingroupvirtuecount + ingroupvicecount)/len(line))
    authorityvirtuelist.append(authorityvirtuecount)
    authorityvicelist.append(authorityvicecount)
    authoritylist.append(authorityvicecount + authorityvirtuecount)
    authorityratio.append((authorityvicecount + authorityvirtuecount)/len(line))
    purityvirtuelist.append(purityvirtuecount)
    purityvicelist.append(purityvicecount)
    puritylist.append(purityvicecount + purityvirtuecount)
    purityratio.append((purityvicecount + purityvirtuecount)/len(line))
    moralratio.append((moralcount)/len(line))
    length.append(len(line))
    


   
