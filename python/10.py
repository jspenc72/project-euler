#!/usr/bin/env python

#simple sieve
n = 2*10**6
prime = [True]*n
prime[0]=prime[1]=False
for i in xrange(n):
    if i*i>=n: break
    if not prime[i]: continue
    for j in xrange(i<<1,n,i):
        prime[j] = False
print sum(prime[i]*i for i in xrange(n))
