#!/usr/bin/env python

def p(m):
    ret=1
    for i in xrange(1,m/2+1):
        x = float(2*i)/(m+1)
        ret *= x**i*(2-x)**(m+1-i)
    return ret

print sum(map(int, (p(i) for i in xrange(2,16))))
