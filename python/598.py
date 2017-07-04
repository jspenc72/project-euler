#!/usr/bin/env python
import numpy as np
from collections import Counter
from utils import sieve, factor

"""
Basic strategy: number of divisors of a number is product of each multiplicity
+1 of that number. So we do dp over the factorization of N!, splitting
multiplicities between a and b.  We prune paths for which it is impossible to
achieve same # of factors in a and b by keeping track of the largest
multiplicity possible for each prime for factorizing multiplicities starting
from the ith factor of N!. Note that we get the most pruning by considering the
factors of N! in decreasing order of multiplicity.

Last trick is a counting trick: if a<b and a and b have same number of factors,
note that we will double count this case if we do not have some extra
bookkeeping. Instead of tracking whether a<b in the dp (which is hard), we
track whether a==b in the dp (which is much easier), and if the have the same
number of factors in the end, we add 2 to the total instead of 1. Since we have
now double-counted all the cases, the final answer is achieved halving.
"""

N = 100
# we need to factor largest multiplicity of anything <= 100 (+1), which will never exceed 100 itself
primes = np.nonzero(sieve(N))[0]
factors = Counter()
for i in xrange(2, N+1):
    factors.update(factor(i, primes))

_mem = {}
def same_divisor_count(i, div_factor_diff, equal, factorcounts, bounds):
    # remove 0 entries and do bounds check
    for k, c in div_factor_diff.items():
        if c==0: del div_factor_diff[k]
        else:
            if i==len(bounds) or abs(c) > bounds[i][k]:
                return 0
    if i==len(factorcounts):
        assert len(div_factor_diff) == 0
        return 2 if equal else 1
    key = (i, frozenset(div_factor_diff.items()), equal)
    if key in _mem:
        return _mem[key]
    ret = 0
    for j in xrange(factorcounts[i]+1):
        newequal = (equal and j == factorcounts[i]-j)
        af, bf = factor(j+1, primes), factor(factorcounts[i]-j+1, primes)
        div_factor_diff.update(bf)
        div_factor_diff.subtract(af)
        ret += same_divisor_count(i+1, div_factor_diff, newequal, factorcounts, bounds)
        div_factor_diff.subtract(bf)
        div_factor_diff.update(af)
    _mem[key] = ret
    return ret

fvalues = factors.values()
fvalues.sort()
bounds = []
for v in fvalues:
    maxc = Counter()
    for i in xrange(1,v+1):
        for k,c in factor(i+1, primes).iteritems():
            maxc[k] = max(maxc[k], c)
    if len(bounds) > 0:
        maxc.update(bounds[-1])
    bounds.append(maxc)
fvalues.reverse()
bounds.reverse()
print same_divisor_count(0, Counter(), True, fvalues, bounds) / 2
