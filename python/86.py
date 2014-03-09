#!/usr/bin/env python

def issquare(n):
    return (int(round(n**.5)))**2 == n

total=m=0
while total < 10**6:
    m += 1
    for ipj in xrange(2*m+1):
        if not issquare(ipj**2+m**2): continue
        if ipj > m+1: total += (2*m+2-ipj)/2
        else: total += ipj/2
print m
