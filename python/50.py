#!/usr/bin/env python

N=10**6
isprime = [True]*N
isprime[0]=isprime[1]=False
sumprime = []

for i in xrange(N):
    if not isprime[i]: continue
    for j in xrange(i<<1,N,i): isprime[j] = False

total = 0
for i in xrange(N):
    if not isprime[i]: continue
    total += i
    sumprime.append(total)

s = len(sumprime)
cont = True
for i in xrange(s-1,-1,-1):
    if not cont: break
    if sumprime[i] - sumprime[0] >= N: continue
    for j in xrange(s-1,-1,-1):
        if j-i<0: break
        diff = sumprime[j] - sumprime[j-i]
        if diff >= N: continue
        if isprime[diff]:
            print diff
            cont = False
            break
