#!/usr/bin/env python

m=10**9+7

def g(n,k):
    if k==0: return 1
    c = pow(2,k-1,m)
    if (k&1): return c*pow(2,(k-1)*(n-1),m)%m
    ans=c
    c-=1
    for i in xrange(1,n):
        ans = (ans+c*pow(2,i*(k-1)%(m-1),m)%m)%m
    return ans

def f(n,k):
    if k==0: return 1
    return (pow(2,n*k%(m-1),m) - g(n,k) - (pow(2,n*(k-1)%(m-1),m) - g(n,k-1)))%m

def w(n):
    return (f(n,n) - (pow(2,n,m)-1)*f(n,n-2)%m)%m

print f(3,3)

n=3
ans=0
for i in xrange(2**n):
    if i==0: continue
    for j in xrange(2**n):
        if j==0: continue
        #if i==j: continue
        for k in xrange(2**n):
            if k==0: continue
            #if i==k or j==k: continue
            if i^j^k: ans+=1
print ans
