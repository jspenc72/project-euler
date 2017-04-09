#!/usr/bin/env python
import tqdm
from utils import c, sieve

"""
Idea: write S(L) as a summation, sum over terms with
same power of 5. Tricky part is computing the coefficient;
for this we can use identity

sum(c(n,i) for i in xrange(k+1)) == c(n+1,k+1)
"""

N = 50*10**6
prime = sieve(N)

pi = [0]*(N+1)
for i in xrange(2,N+1):
    pi[i] = pi[i-1] + prime[i]

def check(n):
    ret = 0
    for k in xrange(pi[n]+1):
        ret += 6*c(n-1,k)*5**(n-1-k)
    return ret

mod = 10**9+7
ans=0
stop = 0
for diff in tqdm.tqdm(xrange(1, N+1)):
    while stop<N and stop+1-pi[stop+1]<=diff:
        stop += 1
    ans += 6*c(stop,stop-diff,mod)*pow(5,diff-1,mod) % mod
    ans %= mod

print ans
