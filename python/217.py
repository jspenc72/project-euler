#!/usr/bin/env python

N=47
mod=3**15

L={}
def left(n,m): # disallows first in sequence to be 0
    if n==0 and m==0: return 1
    if n<=0 or m<=0: return 0
    if (n,m) in L: return L[n,m]
    total=0
    for i in xrange(10):
        total = (total + left(n-i,m-1))%mod
    L[n,m]=total
    return total

R={}
def right(n,m): # only difference is we allow first in sequence to be 0
    if n==0: return 1
    if n<0 or m<=0: return 0
    if (n,m) in R: return R[n,m]
    total=0
    for i in xrange(10):
        total = (total + right(n-i,m-1))%mod
    R[n,m]=total
    return total

ans=0
for i in xrange(1,N+1):
    M=9*(i//2)
    if i&1:
        for s in xrange(M+1):
            ans = (ans + left(s,i//2)*right(s,i//2)%mod*(45*10**(i//2))%mod)%mod
    for j in xrange(1,10):
        for s in xrange(M-j+1):
            if i&1:
                # right side
                ans = (ans + 10*left(s+j,i//2)*right(s,i//2-1)%mod*j*(10**(i//2)-1)//9%mod)%mod
                # left side, but not leftmost
                ans = (ans + 10*left(s,i//2-1)*right(s+j,i//2)%mod*j*((10**(i-1) - 10**((i+1)//2))//9)%mod)%mod
                # leftmost
                ans = (ans + 10*right(s,i//2-1)*right(s+j,i//2)%mod*j*10**(i-1)%mod)%mod
            else:
                # right side
                ans = (ans + left(s+j,i//2)*right(s,i//2-1)%mod*j*(10**(i//2)-1)//9%mod)%mod
                # left side, but not leftmost
                ans = (ans + left(s,i//2-1)*right(s+j,i//2)%mod*j*(10**(i-1) - 10**(i//2))//9%mod)%mod
                # leftmost
                ans = (ans + right(s,i//2-1)*right(s+j,i//2)%mod*j*10**(i-1)%mod)%mod
print ans
