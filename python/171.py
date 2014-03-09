#!/usr/bin/env python
from itertools import count

mod = 10**9
ans = 0

# num ways (mod 10**9) to make sum of squared digits to sum to n, using k digits
# allows for leading zero digits
F = {}
def f(n,k):
    if n==0 and k==0: return 1
    if n<0 or k<=0: return 0
    if (n,k) in F: return F[n,k]
    total = 0
    for x in xrange(10):
        total = (total + f(n-x*x,k-1))%mod
    F[n,k] = total
    return total

for d in xrange(1,21):
    M = 9*9*d
    for i in count(1):
        if i*i > M: break
        for x in xrange(1,10):
            ans = (ans + f(i*i-x*x,d-1)*x%mod*(10**(d-1))%mod)%mod # force x to lead
            for y in xrange(1,10):
                ans = (ans + f(i*i-y*y-x*x,d-2)*x%mod*((10**(d-1)-1)//9)%mod)%mod # y must lead, x may appear anywhere else
print ans
