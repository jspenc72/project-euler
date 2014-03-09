#!/usr/bin/env python
from itertools import count

N=100
prime=[True]*N
prime[0]=prime[1]=False
for i in xrange(N):
    if i*i >= N: break
    if not prime[i]: continue
    for j in xrange(i*i,N,i): prime[j]=False

phi,n=1,1
num,den=15499,94744

for i in xrange(N):
    if not prime[i]: continue
    phi *= (i-1)
    n *= i
    if phi*den<(n-1)*num:
        phi /= (i-1)
        n /= i
        break

for i in count(2):
    if phi*i*den < (n*i-1)*num:
        print n*i
        break
