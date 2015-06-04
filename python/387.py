#!/usr/bin/env python
import numpy as np

N=10**14
P=int(N**.5 + 100)
isprime = np.ones(P,dtype=bool)
isprime[0]=isprime[1]=False
for i in xrange(P):
    if i*i >= P: break
    if not isprime[i]: continue
    for j in xrange(i*i, P, i):
        isprime[j] = False

#print 'got dem primes'

primes = np.nonzero(isprime)[0]
def prime(x):
    if x<len(isprime): return isprime[x]
    for p in primes:
        if x%p == 0: return False
    return True

def strong(n, s):
    if n >= N: return False
    if prime(n//s): return True
    return False

def harshads(n, s):
    if n>=N or not n%s==0:
        return
    else:
        yield (n,s)
        v = 10*n
        for i in xrange(10):
            for (hh, ss) in harshads(v+i, s+i):
                yield (hh, ss)

def primeExtensions(n):
    v = 10*n
    for d in [1,3,7,9]:
        if v+d < N and prime(v+d):
            yield v+d

ans=0
for i in xrange(1,10):
    for h, s in harshads(i,i):
        if strong(h,s):
            for p in primeExtensions(h):
                ans += p
print ans
