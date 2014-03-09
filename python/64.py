#!/usr/bin/env python

from itertools import count

def nextfrac(S,a0,m,d,a):
    m1 = d*a-m
    d1 = (S-m1*m1)/d
    a1 = (a0+m1)/d1
    return (m1,d1,a1)

def issquare(n):
    r = n**.5
    return abs(r-int(round(r))) < .001

total = 0

for i in xrange(2, 10000):
    if issquare(i): continue
    s = set([])
    a0,m,d,a = int(i**.5),0,1,int(i**.5)
    t = (m,d,a)
    for j in count(0):
        t = nextfrac(i,a0,*t)
        if t in s:
            total += j%2
            break
        s.add(t)
print total
