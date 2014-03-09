#!/usr/bin/env python

# just iterate through all pairs of three digit numbers

def pal(n):
    s = str(n)
    l = len(s)
    for i in xrange(l//2):
        if s[i] != s[l-i-1]: return False
    return True

ans = 0
for i in xrange(100,1000):
    for j in xrange(i,1000):
        if pal(i*j):
            ans = max(ans,i*j)
print ans
