#!/usr/bin/env python
from itertools import count

D={1:1}
def divisors(x,s=2):
    if x in D: return D[x]
    y = x
    d=1
    for p in count(s):
        m=0
        while not x%p:
            x//=p
            m+=1
        if m>0:
            d=(m+1)*divisors(x,p+1)
            break
    D[y] = d
    return d

total=0
n=9
for va2 in xrange(2*n+1):
    for va5 in xrange(2*n+1):
        ap = 2**va2 * 5**va5
        for vb2 in xrange(2*n+1):
            if 2**vb2 > ap: break
            for vb5 in xrange(2*n+1):
                bp = 2**vb2 * 5**vb5
                if bp > ap: break
                v2, v5 = va2+vb2, va5+vb5
                c = ap + bp
                while not c%2:
                    c//=2
                    v2-=1
                while not c%5:
                    c//=5
                    v5-=1
                if max(v2,v5) > n: continue
                total += divisors(c)*min(n+1-max(v2,v5),n)
print total
