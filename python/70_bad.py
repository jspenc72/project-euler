#!/usr/bin/env python

isPrime = [True]*10**7

for i in xrange(2, 10**7):
    if not isPrime[i]: continue
    for j in xrange(2*i, 10**7, i):
        isPrime[j] = False

primes = []
for i in xrange(2, 10**7):
    if isPrime[i]: primes.append(i)

def phi(n):
    if isPrime[n]: return n-1
    val = n
    for p in primes:
        if 2*p > n: break
        if n%p == 0: val = val/p*(p-1)
    return val

def perm(m,n):
    m = str(m)
    n = str(n)
    if len(m) != len(n): return False
    for c in m:
        if not c in n: return False
        i = n.index(c)
        n = n[:i] + n[i+1:]
    return True

smallest = 10.0
x = -1
for n in xrange(2, 10**7):
    f = phi(n)
    if not perm(n,f): continue
    r = float(n)/f
    if r < smallest:
        smallest = r
        x = n
print x, phi(x)
