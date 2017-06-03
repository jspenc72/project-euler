#!/usr/bin/env python
from utils import gcd

mod = 10**8

def M(n,k):
    if gcd((pow(2,n,n)-1)%n,n) == 1:
        # if gcd((2**n-1)%n, n) is 1, then we are definitely already reduced!
        # this is because gcd(2**n-1, (2**n-1)*(k-1)+n) == gcd(2**n-1,n) == gcd((2**n-1)%n, n)
        pass
    else:
        # otherwise, I don't know how to guarantee that gcd((2**n-1)**2, (2**n-1)*(k-1)+n) == gcd(2**n-1, (2**n-1)*(k-1)+n),
        # in which case things become messier since some factors of the latter could possibly be duplicated in the gcd.
        # fortunately this doesn't happen for the input requested by PE. If it did, one possibility is to find the gcd
        # gcd(2**n-1, n) with gcd(k-1, n) -- I haven't proved it but I think these factors would be replicated in both
        # numerator and denominator.
        raise Exception("we maybe need more heavy lifting because of the square in the denominator")
    x = (pow(2,n,mod)-1)%mod
    numerator = pow(2, n-k, mod)*((k-1)*x % mod + n)%mod
    denominator = pow(x, 2, mod) % mod
    return numerator * denominator % mod

print M(10**8+7,10**4+7)
