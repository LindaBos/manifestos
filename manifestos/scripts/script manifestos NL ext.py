import re
import string

moraldic = open("/home/linda/manifestos/manifestos/mf/dutch moral foundations dictionary ext.1.dic").read().replace("\t", "").replace("\s", "")


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
libertyvirtue = re.findall('([a-z]+\*?).*[1][2]', moraldic)
libertyvice = re.findall('([a-z]+\*?).*[1][3]', moraldic)



moralityall = re.findall('([a-z]+\*?).*[01-13]', moraldic) 



#lege zinnen weglaten
#stopwoorden en leestekens verwijderen


text = [t.strip() for t in text if t.strip()!=""]
text = [' '.join(w for w in text.split() if w.lower() not in stopwords) for text in text]
text = [t.lower() for t in text]
translate_table = dict((ord(char), None) for char in string.punctuation)   
text = [t.translate(translate_table) for t in text]


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
moralgenlist = []
libertyvirtuelist = []
libertyvicelist = []
harmlist = []
fairnesslist = []
ingrouplist = []
authoritylist = []
puritylist = []
libertylist = []
length=[]
party = []
year= []
country = []
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
    pn=partyname
    y=yr
    c=ctr
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
    party.append(pn)
    year.append(y)
    country.append(c)
    length.append(len(line))
    


   
