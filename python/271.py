#!/usr/bin/env python

# Simple idea: that huge number (13082761331670030)
# has only small prime factors of multiplicity 1.
# We find what each solution to x^3 == 1 (mod p)
# for each prime factor and use the CRT to construct
# each solution.

def cra2(a1,m1,a2,m2,phi2):
    return a1 + (a2-a1)*pow(m1,phi2-1,m2)%m2*m1

#primes = [7, 13] # for test
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
mod = reduce(lambda x,y: x*y, primes)
sols = {p:[] for p in primes}
for p in primes:
    for i in xrange(1,p):
        if i%p==1 or (i*i+i)%p==p-1:
            sols[p].append(i)

def crasol(i,a1,m1):
    if i==len(primes): yield a1
    else:
        p = primes[i]
        for a2 in sols[p]:
            for s in crasol(i+1, cra2(a1,m1,a2,p,p-1), m1*p):
                yield s

ans=0
for s in crasol(0,0,1): ans += s
print ans-1 # subtract trivial solution
