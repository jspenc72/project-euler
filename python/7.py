#!/usr/bin/env python

# sieve of eratosthenes
# pretty sure density of primes is n/ln(n),
# so 10^6 should be sufficiently large

N = 1000000
prime = [True]*N
for i in xrange(2,N):
    if i*i>N: break
    if not prime[i]: continue
    for j in xrange(i<<1,N,i): prime[j]=False

c = 0
for i in xrange(2,N):
    if prime[i]: c+=1
    if c==10001:
        print i
        break
