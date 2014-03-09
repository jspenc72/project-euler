#!/usr/bin/env python

N = 10**6

prime = [True]*N
psquared = set([])
prime[0]=prime[1] = False
for i in xrange(N):
    if not prime[i]: continue
    psquared.add(i*i)
    for j in xrange(i<<1, N, i): prime[j] = False
maxp = max(psquared)

total = 0

for ps in psquared:
    n = (ps+13)/2
    k = n/4+1
    q = n-3*k
    total += 2*((q+1)/3)
    if (ps+11)%8 == 0:
        total += 1

print total
