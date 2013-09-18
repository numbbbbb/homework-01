#!/usr/bin/python

inputfile = open("number", "r")
allnum = []
for line in inputfile.readlines():
    allnum.append(int(line))
inputfile.close()
n = len(allnum)
themax = min(allnum)

for i in range(0, n):
    sumnum = 0
    for j in range(i, n):
        sumnum += allnum[j]
        themax = max(sumnum, themax)
print themax
