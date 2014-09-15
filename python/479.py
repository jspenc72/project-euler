#!/usr/bin/env python

# strategy: use algebra
# (can show that (a_k+b_k)*(a_k+c_k)*(b_k+c_k) = 1-k*k

M=10**9+7
N=10**6
def f(k):
    return ((pow(1-k*k,N+1,M)-1)*pow(-k*k,M-2,M)-1)%M

print sum(f(k) for k in xrange(1,N+1))%M
