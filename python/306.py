#!/usr/bin/env python

#from itertools import count
#
#N = 137
#strips = [0]*(N+1)
#
#for i in xrange(2,N+1):
#    ret = 0
#    for j in xrange(2, i/2 + 2):
#        ret |= (1<<(strips[j-2] ^ strips[i-j]))
##    for j in count(0):
##        if j in s: continue
##        strips[i] = j
##        break
#    bit = 1
#    pos = 0
#    while ret & bit:
#        pos += 1
#        bit <<= 1
#    strips[i] = pos
#
#t1 = 0
#t2 = 0
#for i in xrange(137-33,N+1):
#    if strips[i] != 0: t1 += 1
#for i in xrange(137-33,137-33+(10**6+2)%34):
#    if strips[i] != 0: t2 += 1
#print t1*((10**6+2)/34) + t2 - 4
n = 10**6
mods = [5,9,21,25,34]
total = n-3
for m in mods:
    total -= (n+m)/34
print total
