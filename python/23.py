#!/usr/bin/env python

N = 28124

divsum = [1]*N
divsum[0] = 0
abundant = []
aset = set([])
total=N*(N-1)/2

for i in xrange(2,N):
    for j in xrange(i<<1,N,i):
        divsum[j] += i

for i in xrange(N):
    if divsum[i] > i:
        abundant.append(i)
        aset.add(i)

for i in xrange(N):
    for j in xrange(len(abundant)):
        if i-abundant[j] in aset:
            total -= i
            break

print total
