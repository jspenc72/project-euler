#!/usr/bin/env python

# number of routes is c(40,20)
# (number of binary strings with
# 20 0's and 20 1's)

def fact(n):
    return reduce(lambda x,y:x*y, xrange(2,n+1))

print fact(40)/(fact(20)*fact(20))
