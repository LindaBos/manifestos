#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:54:03 2017

@author: linda
"""

import os
import glob
import pandas as pd
import numpy as np

path = "/home/linda/manifestos/data/NL"
allfiles = glob.glob(os.path.join(path,"*.csv"))


np_array_list = []
for file_ in allfiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    np_array_list.append(df.as_matrix())

comb_np_array = np.vstack(np_array_list)
big_frame = pd.DataFrame(comb_np_array)

big_frame.columns = ['text','cmp_code', 'morallist','harmvirtuelist', 'harmvicelist', 'harmlist', 'fairnessvirtuelist', 'fairnessvicelist',  'fairnesslist', 'ingroupvirtuelist', 'ingroupvicelist', 'ingrouplist', 'purityvirtuelist', 'purityvicelist', 'puritylist',  'authorityvirtuelist', 'authorityvicelist', 'authoritylist', 'libertyvirtuelist', 'libertyvicelist', 'libertylist', 'moralgenlist', 'length', 'party', 'year', 'country']

#%% missing values hercoderen

bf = big_frame.fillna(value = 0)

 

# https://manifestoproject.wzb.eu/coding_schemes/mp_v4

#%% dummies maken voor analyses

parties = pd.get_dummies(bf['party'])

issues = pd.get_dummies(bf['cmp_code'])

countries = pd.get_dummies(bf['country'])

yr = pd.get_dummies(bf['year'])

bfd = pd.concat([bf, parties,issues, countries, yr ], axis=1)    

bfd.rename(columns={101: 'i101', 103: 'i103', 104: 'i104', 105: 'i105', 106: 'i106', 107: 'i107', 108: 'i108', 109: 'i109', 110: 'i110'}, inplace=True)

bfd.rename(columns={201: 'i201', 202: 'i202', 203: 'i203', 204: 'i204'}, inplace=True)

bfd.rename(columns={301: 'i301', 302: 'i302', 303: 'i303', 304: 'i304', 305: 'i305'}, inplace=True)

bfd.rename(columns={401: 'i401', 402: 'i402', 403: 'i403', 404: 'i404', 405: 'i405', 406: 'i406', 407: 'i407', 408: 'i408', 409: 'i409', 410: 'i410', 411: 'i411', 412: 'i412', 413: 'i413', 414: 'i414', 416: 'i416'}, inplace=True)

bfd.rename(columns={501: 'i501', 502: 'i502', 503: 'i503', 504: 'i504', 505: 'i505', 506: 'i506'}, inplace=True)

bfd.rename(columns={601: 'i601', 602: 'i602', 603: 'i603', 604: 'i604', 605: 'i605', 606: 'i606', 607: 'i607', 608: 'i608'}, inplace=True)

bfd.rename(columns={701: 'i701', 702: 'i702', 703: 'i703', 706: 'i706'}, inplace=True)

#%%

#recode parfam  

##C n.b. nu ukip nationalistische partij gemaakt en sgp christelijk

bfd['com'] = bfd.sp
bfd['eco'] = bfd.gl
bfd['lib'] = bfd.vvd
bfd['sip'] = bfd.p50p + bfd.pvdd 
bfd['soc'] = bfd.d66 + bfd.pvda
bfd['nat'] = bfd.pvv 
bfd['chr'] = bfd.cda + bfd.cu + bfd.sgp
bfd['pop'] = bfd.p50p + bfd.pvv



#%% recode issues

bfd['exter'] = bfd.i101 + bfd.i103 +bfd.i104 +bfd.i105 +bfd.i106 +bfd.i107 +bfd.i108 + bfd.i109 + bfd.i110
#bfd['freedom'] = bfd.i201 + bfd.i203 +bfd.i204 +bfd.i203
bfd['freedom'] = bfd.i201 + bfd.i203 +bfd.i203
bfd['polsys'] = bfd.i301 + bfd.i303 +bfd.i304 +bfd.i303 + bfd.i305
bfd['economy'] = bfd.i401 + bfd.i402 + bfd.i403 +bfd.i404 +bfd.i405 +bfd.i406 +bfd.i407 +bfd.i408 + bfd.i409 + bfd.i410 + bfd.i411 + bfd.i412 + bfd.i413 + bfd.i414 + bfd.i416
bfd['welfare'] = bfd.i501 + bfd.i503 +bfd.i502 +bfd.i503 + bfd.i505
bfd['fabric'] = bfd.i601 + bfd.i602 + bfd.i603 +bfd.i604 +bfd.i605 +bfd.i606 +bfd.i607 +bfd.i608
#bfd['groups'] = bfd.i701 + bfd.i702 + bfd.i703 +bfd.i706 
bfd['groups'] = bfd.i701 + bfd.i703 +bfd.i706 


#%%

bfd.to_csv('/home/linda/manifestos/combined data/Dutch manifestos 06 10 12.csv')
 
#%% beetje kijken naar de data

for foundation in ['harmlist','puritylist','ingrouplist','authoritylist', 'fairnesslist', 'libertylist', 'moralgenlist', 'morallist']:
    print(foundation.upper())
    print(bfd[foundation].value_counts(sort=True, normalize=True))
    print('-------------------------------------------\n')



#%%

from statsmodels.formula.api import ols

myfittedregression = ols(formula = 'morallist ~ length + year + lib + eco + com + sip + soc + chr + nat', data = bfd).fit()
print(myfittedregression.summary())

#%%

myfittedregression = ols(formula = 'morallist ~ length + pop + exter + freedom + polsys + welfare + fabric + groups ', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'morallist ~ length + pop', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'ingrouplist ~ length + pop', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'harmlist ~ length + pop', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'puritylist ~ length + pop', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'authoritylist ~ length +  pop', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'fairnesslist ~ length + pop', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'libertylist ~ length + pop', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'moralgenlist ~ length + pop', data = bfd).fit()
print(myfittedregression.summary())

#%%



myfittedregression = ols(formula = 'morallist ~ length + sp + gl + pvdd + pvda + p50p + cu + cda + sgp + vvd + pvv ', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'morallist ~ length + sp + gl + pvdd + pvda + p50p + cu + cda + sgp + vvd + pvv ', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'ingrouplist ~ length + sp + gl + pvdd + pvda + p50p + cu + cda + sgp + vvd + pvv ', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'harmlist ~ length + sp + gl + pvdd + pvda + p50p + cu + cda + sgp + vvd + pvv ', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'puritylist ~ length + sp + gl + pvdd + pvda + p50p + cu + cda + sgp + vvd + pvv ', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'authoritylist ~ length + sp + gl + pvdd + pvda + p50p + cu + cda + sgp + vvd + pvv ', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'fairnesslist ~ length + sp + gl + pvdd + pvda + p50p + cu + cda + sgp + vvd + pvv ', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'libertylist ~ length + sp + gl + pvdd + pvda + p50p + cu + cda + sgp + vvd + pvv ', data = bfd).fit()
print(myfittedregression.summary())

myfittedregression = ols(formula = 'moralgenlist ~ length + sp + gl + pvdd + pvda + p50p + cu + cda + sgp + vvd + pvv ', data = bfd).fit()
print(myfittedregression.summary())


#%% per moral foundation

bfd['moralratio'] = bfd['morallist']/bfd['length']
bfd['harmratio'] = bfd['harmlist']/bfd['length']
bfd['fairnessratio'] = bfd['fairnesslist']/bfd['length']
bfd['ingroupratio'] = bfd['ingrouplist']/bfd['length']
bfd['authorityratio'] = bfd['authoritylist']/bfd['length']
bfd['purityratio'] = bfd['puritylist']/bfd['length']
bfd['libertyratio'] = bfd['libertylist']/bfd['length']
bfd['moralgenratio'] = bfd['moralgenlist']/bfd['length']

bfd['moraldummy'] = np.where(bfd['morallist']>0, '1', '0')
bfd['harmdummy'] = np.where(bfd['harmlist']>0, '1', '0')
bfd['fairnessdummy'] = np.where(bfd['fairnesslist']>0, '1', '0')
bfd['ingroupdummy'] = np.where(bfd['ingrouplist']>0, '1', '0')
bfd['authoritydummy'] = np.where(bfd['authoritylist']>0, '1', '0')
bfd['puritydummy'] = np.where(bfd['puritylist']>0, '1', '0')
bfd['libertydummy'] = np.where(bfd['libertylist']>0, '1', '0')
bfd['moralgendummy'] = np.where(bfd['moralgenlist']>0, '1', '0')

#%%

bfd.to_csv('/home/linda/manifestos/combined data/Dutch manifestos 06 10 12.csv')

#%%

#zodirect even snel naar analyses kijken en false positives nalopen 