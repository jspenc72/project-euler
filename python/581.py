#!/usr/bin/env python
import sys
from collections import Counter
from utils import sieve

P=47
isprime = sieve(P)
primes = []
for i in xrange(P+1):
    if isprime[i]:
        primes.append(i)

# it's same as for up to 10^14
# so that's how we know when to stop :)
# technically supposed to use: 
# https://en.wikipedia.org/wiki/St%C3%B8rmer%27s_theorem
# to get the bound.
# w/e, I'm too busy to know random number theory facts.
MAX=10**13

def printc(c):
    todelete=[]
    for k, v in c.iteritems():
        if v==0:
            todelete.append(k)
    for k in todelete:
        del c[k]

psmooth = set()
def recurse(prod=1, minp=0):
    # 1 is a special case that is handled properly thanks to canceling errors
    if prod > MAX:
        return 0
    psmooth.add(prod)
    ret = 0
    if prod-1 in psmooth:
        ret += prod-1
    if prod+1 in psmooth:
        ret += prod
    for i in xrange(minp, len(primes)):
        p = primes[i]
        prod *= p
        ret += recurse(prod, i)
        prod //= p
    return ret

print recurse()
