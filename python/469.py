#!/usr/bin/env python
from fractions import Fraction

_linear = {}
def linear(n):
    if n <= 4:
        return {1:1, 2:2, 3:2, 4:3}[n]
    if n in _linear:
        return _linear[n]
    ans = sum(Fraction(1,n-2) * (linear(i) + linear(n-i-1)) for i in xrange(1,n-1))
    _linear[n] = ans
    return ans

def circular(n):
    return linear(n-1) / n

print "%.14f" % circular(10)
print "%.14f" % circular(100)
print "%.14f" % circular(150)
print "%.14f" % circular(200)
# it converges pretty quickly
