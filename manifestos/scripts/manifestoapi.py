#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:36:11 2017

@author: linda
"""

import requests
import pandas as pd

myurl = "https://manifesto-project.wzb.eu/tools/api_get_core.json?api_key=ecc627a300c3c8f9a765f20f6e8d8231&key=MPDS2016b"

data = requests.request(url=myurl,method='get').json()

print("We hebben wat data gedownload\nAantal rijen:{}".format(len(data)))

print("It seems that the API delivers a list of lists, we are going to transform it into a Pandas dataframe for easier handling")
df = pd.DataFrame.from_records(data)

## ik wilde nu eigenlijk gaan kijken naar de manifesto api om heel veel manifestos automatisch te downloaden
## echter,dat blijkt niet zo simpel, aangezien je daarbij zowel geannoteerde als niet-geannoteerd texten binnenhaalt
## c.q, manifestos die zijn opgeknipt in onderwerpen als manifestos in zijn geheel
## van de uk is 2015 geannoteerd, en dan pas weer een aantal jaar terug
## als ik naar de hele manifestos wil kijken is het wellicht interessant om over de tijd te kijken. maar dan kan ik de api niet gebruiken want
## die geeft de geannoteerde text als die er is