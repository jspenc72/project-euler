#!/usr/bin/env python

_M = {}
def M(c,r):
    if r < c:
        return r+1
    if (c,r) in _M:
        return _M[c,r]
    x = M(c,r-1)
    ret=0
#    while x>c-1:
#        ret += c
#        x -= (c-2)
#    ret += (x+1)
    p = (x-2)//(c-2) # x-2 == ((x-c)+(c-2))
    q = x - p*(c-2)
    ret += p*c + q+1
    _M[c,r] = ret
    return ret

print sum(M(c,30) for c in xrange(3,41))
