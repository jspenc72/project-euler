#!/usr/bin/env python
try:
    from gmpy import mpq # much, much faster than Fraction
    one = mpq(1)
except ImportError: # use slow python fractions if gmpy not installed
    from fractions import Fraction
    one = Fraction(1)

n = 18
caps = [set([]) for i in xrange(n+1)]
caps[1].add(one)

for i in xrange(2,n+1):
    for j in xrange(1,i/2 + 1):
        for c1 in caps[j]:
            for c2 in caps[i-j]:
                caps[i].add(c1+c2)
                caps[i].add(1/(1/c1 + 1/c2))

print len(reduce(set.union, caps))
