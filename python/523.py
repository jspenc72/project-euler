#!/usr/bin/env python
from utils import memoize

@memoize
def s(n):
    if n==0:
        return 0.
    return t(n) + s(n-1)

# probably easy to get an explicit form for this
# but why bother; it's linear
# represents # of steps needed to get nth smallest
# item into correct position starting from 0th position
# that is, # steps for:
# [n, 0, 1, 2, ..., n-1] ==> [0, 1, 2, ..., n]

@memoize
def t(n):
    if n==0:
        return 0.
    if n==1:
        return 1.
    return n + s(n-1)

# with probability 1/n, kth smallest item goes in last position
# then we need e(n-1) moves in expectation to sort left side of
# list; then another 1+t(k) moves to put rightmost element into
# correct position. the reason we can use e(n-1) is because we
# only care about the rank of items, and the distribution of ranks
# given the rightmost element is still uniform.

@memoize
def e(n):
    if n==0:
        return 0.
    ans = 0.
    for k in xrange(n-1):
        ans += (e(n-1) + 1. + t(k)) / n
    return ans + e(n-1) / n

print '%.2f' % e(30)
