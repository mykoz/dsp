    #PLACE YOUR CODE HERE


import csv
import re

def degreecount(data):
    f = open(data, "rb")

    phdcount = 0
    scdcount = 0
    mdcount = 0
    mphcount = 0
    bscount = 0
    mscount = 0
    jdcount = 0

    faculty = csv.reader(f)
    for row in faculty:

        findphd = re.compile(r'Ph\.?D', re.I|re.M)
        findscd = re.compile(r'Sc\.?D', re.I|re.M)
        findmd = re.compile(r'M\.?D', re.I|re.M)
        findmph = re.compile(r'M\.?P\.?H', re.I|re.M)
        findbs = re.compile(r'B\.?S\.?Ed', re.I|re.M)
        findms = re.compile(r'M\.?S', re.I|re.M)
        findjd = re.compile(r'J\.?D', re.I|re.M)

        phd = findphd.findall(row[1])
        scd = findscd.findall(row[1])
        md = findmd.findall(row[1])
        mph = findmph.findall(row[1])
        bs = findbs.findall(row[1])
        ms = findms.findall(row[1])
        jd = findjd.findall(row[1])

        if phd:
            phdcount += 1
        if scd:
            scdcount += 1
        if md:
            mdcount += 1
        if mph:
            mphcount += 1
        if bs:
            bscount += 1
        if ms:
            mscount += 1
        if jd:
            jdcount += 1

    print "PhD:", phdcount
    print "ScD:", scdcount
    print "MD :", mdcount 
    print "MPH:", mphcount
    print "BS :", bscount 
    print "MS :", mscount 
    print "JD :", jdcount
    f.close()

#DIFFERENT TITLES (PROF, ASSISTPROF, ETC)

def titlecount(data):
    f = open(data,"rb")
    faculty = csv.reader(f)
    titlewords = [] #List of words used in Title
    profcount = 0
    assoccount = 0
    assistcount = 0
    for row in faculty:
        splitrow = re.findall(r"[\w']+", row[2])
        if 2< len(splitrow) <4:
            profcount += 1

        for word in splitrow:
            if word == "Associate":
                assoccount += 1
            if word == "Assistant":
                assistcount += 1
            if word not in titlewords and len(word) > 5 and word != "Biostatistics":
                titlewords.append(word) 
    print "Number of titles: ",len(titlewords)
    print "Professors:", profcount
    print "Associate Professors: ",assoccount
    print "Assistant Professors: ", assistcount

#RETRIEVE EMAILS

def getemail(data):
    f = open(data,"rb")
    faculty = csv.reader(f)
    elist = []
    for row in faculty:
        if "@" in row[3]:
            elist.append(row[3])

    print elist

def domaincount(data):
    f = open(data,"rb")
    faculty = csv.reader(f)
    domainlist = []
    for row in faculty:
        for entry in row:
            domain = re.findall(r'@[\w.]+', entry)
            if domain not in domainlist and domain != []:
                domainlist.append(domain)
    print domainlist
    print "Number of unique UPenn domains: ", len(domainlist)


#print degreecount("faculty.csv")
#print titlecount("faculty.csv")
#print getemail("faculty.csv")
print domaincount("faculty.csv")
