#!/usr/bin/python

# Q2: highest sale

import sys

maxSale = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", maxSale
        maxSale = 0

    oldKey = thisKey
    if maxSale < float(thisSale): 
        maxSale = float(thisSale)

if oldKey != None:
    print oldKey, "\t", maxSale
