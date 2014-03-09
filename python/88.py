#!/usr/bin/env python

from itertools import count

minpsnum = [float('inf')]*12001
minpsnum[0]=0
minpsnum[1]=0
minpsnum[2]=4

def tryfactors(p, s, prev, place, depth):
    if place==depth and p<=24000:
        val = place+p-s
        if val <= 12000: minpsnum[val] = min(minpsnum[val], p)
    else:
        for i in count(prev):
            pn = p*i
            if pn>24000: break
            tryfactors(pn, s+i, i, place+1, depth)

maxfactors = 0
thing = 1
while thing < 24000:
    maxfactors += 1
    thing <<= 1

for i in xrange(2, maxfactors+1):
    tryfactors(1, 0, 2, 0, i)

s = set([])
for m in minpsnum: s.add(m)
print sum(s)
