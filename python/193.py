#!/usr/bin/env python
from itertools import count

# takes slightly over 1 minute on my machine
# good enough

M=2**50-1
N=2**25
div = [0]*N
for i in count(2):
    if i*i>=M: break
    if div[i]!=0: continue
    if div[i]==-1: continue
    if i*i<N:
        for j in xrange(i*i,N,i*i):
            div[j]=-1
    for j in xrange(i,N,i):
        if div[j]==-1: continue
        div[j] += 1
total=0
for i in xrange(2,N):
    if div[i]==-1: continue
    test = M/(i*i)
    if div[i]&1: total+=test
    else: total-=test
print M-total
