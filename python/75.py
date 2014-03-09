#!/usr/bin/env python

from itertools import count

N=1500000

tricount = [0]*(N+1)
total = 0

def gcd(x,y):
    while y != 0:
        x,y = y,x%y
    return x

for m in count(1):
    if 2*(m+1)*(m+1) + 2*m*(m+1) > N: break
    for n in count(m+1):
        length = 2*n*n + 2*m*n
        if length > N: break
        if (m+n)%2 == 0 or gcd(m,n) != 1: continue
        for i in xrange(length,N,length): tricount[i] += 1

for i in xrange(N+1):
    if tricount[i] == 1: total += 1

print total
