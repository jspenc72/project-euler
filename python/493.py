#!/usr/bin/env python
from math import factorial as f

def c(n,k):
    return f(n)/f(k)/f(n-k)

if __name__=="__main__":
    # given color is present with probability
    # 1 - c(60,20)/c(70,20)
    print "%.9f" % (7.*(1. - float(c(60,20))/c(70,20)))
