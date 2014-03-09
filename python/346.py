#!/usr/bin/env python

from itertools import count

M=10**12
N=int(M**.5)+1

def val(b, n):
    return (b**n - 1)/(b-1)

reps = set([1])

for base in xrange(2, N):
    num = val(base, 2)
    for ones in count(3):
        num = num*base + 1
        if num >= M: break
        reps.add(num)

print sum(reps)
