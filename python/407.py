#!/usr/bin/env python
import numpy as np
from collections import Counter

# factor all a, iterate over divisors, update M[n]
# to be max such a
#
# This would be way faster in C++ and would probably
# fall in the 1 minute rule, but easier in Python.

N=10**7
P=int(N**.5 + 100)
isprime = np.ones(P,dtype=bool)
isprime[0]=isprime[1]=False
for i in xrange(P):
    if i*i >= P: break
    if not isprime[i]: continue
    for j in xrange(i*i, P, i):
        isprime[j] = False

primes = np.nonzero(isprime)[0]

F={}
def factor(x):
    if x in F: return F[x]
    factors = Counter()
    for p in primes:
        while x%p==0:
            factors[p] += 1
            x //= p
        if x == 1:
            break
    if x > 1: # then x is prime
        factors[x] = 1
    F[x] = factors
    return factors

def prime(x):
    if x<len(isprime): return isprime[x]
    for p in primes:
        if x%p == 0: return False
    return True

def divisors(a):
    divs = (factor(a-1) + factor(a)).items()
    def divsHelper(i, d):
        if d > N: return
        if i==len(divs):
            if a < d: yield d
        else:
            p, v = divs[i]
            f = 1
            for j in xrange(v+1):
                for div in divsHelper(i+1, d*f):
                    yield div
                f *= p
    for d in divsHelper(0, 1):
        yield d

M = np.ones(N+1,dtype=int)
M[0] = M[1] = 0

for a in xrange(2, N):
    #if a%1000 == 0: print a
    for n in divisors(a):
        M[n] = max(M[n], a)
    

print np.sum(M)
