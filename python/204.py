#!/usr/bin/env python
from itertools import count

N=100
M=10**9
prime = [True]*N
parr=[]
prime[0]=prime[1]=False

for i in count(2):
    if i*i>=N: break
    if not prime[i]: continue
    for j in xrange(i*i,N,i):
        prime[j]=False
for i in xrange(N):
    if prime[i]: parr.append(i)

def porking(i,curval):
    if i==len(parr): return 1
    if curval > M: return 0
    return porking(i,curval*parr[i]) + porking(i+1,curval)

print porking(0,1)
