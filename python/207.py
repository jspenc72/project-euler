#!/usr/bin/env python
from math import log

def x1(u): return 4*u + 1
def y1(u): return 4*u*u + 2*u

def x2(u): return 4*u + 3
def y2(u): return 4*u*u + 6*u + 2

def nextk():
    u1, u2 = 1, 0
    while True:
        if y1(u1)<y2(u2):
            yield (y1(u1),(x1(u1)+1)/2)
            u1 += 1
        else:
            yield (y2(u2),(x2(u2)+1)/2)
            u2 += 1

i=0
for t in nextk():
    n = t[1]
    if 12345*int(log(n,2)) < n-1:
        print t[0]
        break
