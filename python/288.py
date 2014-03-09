#!/usr/bin/env python

S={}
def s(n):
    if n==0: return 290797
    if n in S: return S[n]
    ret = S[n] = s(n-1)*s(n-1)%50515093
    return ret

p, q, t = 61, 10**7, 10
pmod = p**t
T = [s(i)%p for i in xrange(1,q+1)]
for i in xrange(q-1,0,-1):
    T[i-1] += T[i]

ans = 0
for i in xrange(t):
    ans = (ans + T[i]*p**i)%pmod
print ans
