#!/usr/bin/env python

n = 28123
d = [0]*(n+1)
for i in xrange(1,n+1):
    for j in xrange(i<<1,n+1,i):
        d[j] += i

abundant = [i for i in xrange(n+1) if d[i]>i]
l = len(abundant)
possible = set([])
for i in xrange(l):
    for j in xrange(i,l):
        a = abundant[i]+abundant[j]
        if a<=n: possible.add(a)
m = max(possible)
print m*(m+1)/2 - sum(possible)
