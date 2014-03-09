#!/usr/bin/env python
try:
    from gmpy import mpq # much, much faster than Fraction
    myfrac = mpq
except ImportError: # use slow python fractions if gmpy not installed
    from fractions import Fraction
    myfrac = Fraction

# Winning w times gives winnings of (1+2f)^w * (1-f)^(1000-w).
# There are c(1000,w) ways to do this (binomial distribution).
# Max that can be won w times occurs when f = (2w-l)/2000 (calculus).
# Furthermore, if this f works when we win w times, it will work for w+1 (monotonicity).

fact=[1]
for i in xrange(1,1001): fact.append(i*fact[-1])
def c(n,k):
    return fact[n]/fact[k]/fact[n-k]

n = 10**12
# find minimum wins required
w, l = 999, 1
f = myfrac(2*w-l,2000)
while pow(1+2*f,w)*pow(1-f,l) >= n:
    w, l = w-1, l+1
    f = myfrac(2*w-l,2000)

print float(myfrac(sum(c(1000,wins) for wins in xrange(w+1,1001)),2**1000))
