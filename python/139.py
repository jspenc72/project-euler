#!/usr/bin/env python
from itertools import count

P=10**8

def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x

total=0
for n in count(1):
    if 2*(n+1)*(2*n+1) >= P: break
    for m in count(n+1):
        if (m-n)%2==0 or gcd(m,n) != 1: continue
        p = 2*m*(m+n)
        if p >= P: break
        hyp = m**2+n**2
        diff = 2*m*n-m**2+n**2
        if hyp%diff==0:
            total += P/p
            #print p, m**2-n**2, 2*m*n, m**2+n**2
print total
