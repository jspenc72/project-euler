#!/usr/bin/env python
from gmpy import mpq
from operator import add, mul, sub, div

# completely straightforward
# use gmp fractions for additional speed (~19s as of writing)

def concat(a,b):
    return mpq(int(''.join(map(str,range(a,b)))))

_reachable={}
def reachable(a,b):
    if (a,b) in _reachable:
        return _reachable[a,b]
    ans = set()
    ans.add(concat(a,b))
    for c in xrange(a+1,b):
        for op in [add, mul, sub, div]:
            for val1 in reachable(a,c):
                for val2 in reachable(c,b):
                    if op==div and val2==0:
                        continue
                    ans.add(op(val1, val2))
    _reachable[a,b] = ans
    return ans

total=0
for val in reachable(1,10):
    if val>0 and val.denominator == 1:
        total += val

print total
