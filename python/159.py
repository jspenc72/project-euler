#!/usr/bin/env python

def drs(n):
    while n>=10:
        s = 0
        while n>0:
            s += n%10
            n /= 10
        n = s
    return n

N=10**6
div = [[] for i in xrange(N)]
mdrs = [0]*N

for i in xrange(2,N):
    for j in xrange(i,N,i):
        div[j].append(i)

for i in xrange(2,N):
    if len(div[i])==1:
        mdrs[i] = drs(i)
        continue
    for d in div[i]:
        mdrs[i] = max(mdrs[i], drs(d)+mdrs[i/d])
print sum(mdrs)
