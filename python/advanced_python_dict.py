#PLACE YOUR CODE HERE

import csv
import re
from pprint import pprint 
from collections import OrderedDict




#Q6  CREATE DICTIONARY
facdict = OrderedDict()
f = open("faculty.csv", "rb")
faculty = csv.reader(f)
next(faculty)
for row in faculty:
    last =  row[0].split(' ')[-1]
    values = [[row[1], row[2], row[3]]]
    if last in facdict:
        facdict[last].append(values)
    else:
        facdict[last] = values
    
pprint (facdict.items()[0:3])



#Q7 TUPLE NAME
facdict = OrderedDict()
f = open("faculty.csv", "rb")
faculty = csv.reader(f)
next(faculty)
for row in sorted(faculty):
    last =  row[0].split(' ')
    nametup = (last[0],last[-1])
    values = [[row[1], row[2], row[3]]]
    if nametup in facdict:
        facdict[nametup].append(values)
    else:
        facdict[nametup] = values
    
pprint (facdict.items()[0:3])



#Q8 REVERSE SORT
facdict = OrderedDict()
f = open("faculty.csv", "rb")
faculty = csv.reader(f)
next(faculty)
for row in faculty:
    last =  row[0].split(' ')
    nametup = (last[0],last[-1])
    values = [[row[1], row[2], row[3]]]
    if nametup in facdict:
        facdict[nametup].append(values)
    else:
        facdict[nametup] = values
    
pprint(sorted(facdict.items()[0:3], key =lambda key:key[0][1],reverse =True))
#pprint(sorted(facdict.items(), key =lambda key:key[0][1],reverse =True)) #full print is ordered
#indexing here doesn't work well because dictionaries are inherently unordered so the first 3 are from the middle
