#!/usr/bin/env python
from utils import lucas

# first, figure out that:
# e(n,p) == (1-p)**(n+1)*sum(k**n*p**k,k,1,oo)
# then refer to the following pages :)
# http://mathworld.wolfram.com/Polylogarithm.html
# http://mathworld.wolfram.com/EulerianNumber.html

mod = 10**9+7
N=10**7
K=4*10**6

ans = 0
for j in xrange(N-K+1):
    ans = (ans + pow(-1,j)*lucas(N+1,j,mod)*pow(N-K+1-j,N,mod)%mod)%mod
print ans
