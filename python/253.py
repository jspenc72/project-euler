#!/usr/bin/env python
from collections import Counter
from fractions import Fraction
from utils import memoize

"""
Simple idea: memoize on partitions of unused blocks (special-casing left and right boundaries).
Better idea would have been to start from full caterpillar and remove pieces.
"""

def splits(n):
    if n==1:
        yield (0,0,-1)
    else:
        yield (0,n-1,0)
        for i in xrange(1,n-1):
            yield (i, n-i-1, 1)
        yield (n-1,0,0)

def left_edge_splits(n):
    if n<=0: return
    for i in xrange(n-1):
        yield (i, n-i-1, 1)
    yield (n-1, 0, 0)

def right_edge_splits(n):
    if n<=0: return
    yield (0, n-1, 0)
    for i in xrange(1,n):
        yield (i, n-i-1, 1)

def cmap(c, i):
    if i==0:
        return c
    newC = Counter()
    for k,v in c.iteritems():
        newC[max(k+i,0)] += v
    return newC

def canon(part):
    return tuple(sorted(part))

@memoize
def numways(left, right, part):
    if left==0 and right==0 and len(part)==0:
        return Counter({0:1})
    M = Counter()
    part = list(part)
    for newleft, newp, inc in left_edge_splits(left):
        if newp==0:
            newpart = tuple(part)
        else:
            newpart = canon(part + [newp])
        subM = numways(newleft, right, newpart)
        M.update(cmap(subM, inc))
    for newp, newright, inc in right_edge_splits(right):
        if newp==0:
            newpart = tuple(part)
        else:
            newpart = canon(part + [newp])
        subM = numways(left, newright, newpart)
        M.update(cmap(subM, inc))
    for i, p in enumerate(part):
        for newpl, newpr, inc in splits(p):
            if newpl==0 and newpr==0:
                newpart = tuple(part[:i] + part[i+1:])
            elif newpl==0:
                part[i] = newpr
                newpart = canon(part)
                part[i] = p
            else:
                part[i] = newpl
                newpart = canon(part + [newpr] if newpr>0 else part)
                part[i] = p
            subM = numways(left, right, newpart)
            M.update(cmap(subM, inc))
    return M

def expected(M):
    denom = sum(M.values())
    ans = 0.
    for k,v in M.iteritems():
        ans += float(Fraction(k*v, denom))
    return ans

N = 40
M = Counter()
for i in xrange(N):
    M.update(cmap(numways(i, N-i-1, ()), 1))
print '%.6f' % expected(M)
